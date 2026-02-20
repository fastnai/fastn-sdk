"""Fastn SDK client — sync and async.

This module contains the two main entry points: ``FastnClient`` (sync) and
``AsyncFastnClient`` (async). Both provide identical APIs for:

Data plane — call tools directly:
    fastn = FastnClient(api_key="...", project_id="...")
    fastn.slack.send_message(channel="general", text="Hello!")

    # With a specific connection:
    fastn.slack.send_message(connection_id="conn_abc", channel="general", text="Hi")

    # With a tenant override:
    fastn.slack.send_message(tenant_id="acme", channel="general", text="Hi")

    # Bind a connection for repeated use:
    slack = fastn.connect("conn_abc")
    slack.send_message(channel="general", text="Hi")

Control plane — inspect the tool registry:
    connectors = fastn.admin.connectors.list()
    tools = fastn.get_tools("slack")
    tool = fastn.get_tool("slack", "send_message")

LLM agent integration — describe what you need, get tool schemas:
    tools = fastn.get_tools_for("Send a message on Slack", format="openai")
    # Also: "anthropic", "gemini", "bedrock", "raw"

    # Then execute the LLM's tool call:
    result = fastn.execute(action_id="act_slack_send_message", params={...})

AI-powered mode — natural language tool discovery:
    result = fastn.run("Send hello to #general on Slack")

Environments — switch between LIVE, STAGING, DEV:
    fastn = FastnClient(api_key="...", project_id="...", stage="DEV")

Constructor parameters:
    api_key:      Fastn API key (or FASTN_API_KEY env var)
    project_id:   Fastn project ID (or FASTN_PROJECT_ID env var)
    auth_token:   JWT from ``fastn login`` (or FASTN_AUTH_TOKEN env var)
    tenant_id:    Tenant ID, default "" (empty) (or FASTN_TENANT_ID env var)
    stage:        "LIVE" | "STAGING" | "DEV" (or FASTN_STAGE env var)
    config_path:  Path to .fastn/config.json (auto-detected if omitted)
    timeout:      HTTP timeout in seconds (default: 30)
    max_retries:  Retry count for transient failures (default: 3)
    verbose:      Print debug output (default: False)
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import httpx

from fastn.auth import build_headers
from fastn.config import FastnConfig, load_config, load_migrations, load_registry
from fastn.connector import AsyncDynamicConnector, DynamicConnector
from fastn.exceptions import (
    APIError,
    AuthError,
    ConnectorNotFoundError,
    FastnError,
    ToolNotFoundError,
)


DEFAULT_TIMEOUT = 30.0
MAX_RETRIES = 3
BACKOFF_FACTOR = 0.5
API_BASE_URL = "https://live.fastn.ai/api/ucl"

# Supported LLM tool formats
_SUPPORTED_FORMATS = ("openai", "anthropic", "gemini", "bedrock", "raw")


# ---------------------------------------------------------------------------
# LLM tool format converters
# ---------------------------------------------------------------------------

def _unwrap_input_schema(schema: Dict[str, Any]) -> Dict[str, Any]:
    """Unwrap a single wrapper key (body/param/query) from an inputSchema.

    Fastn schemas wrap params under a top-level key like ``body``.  LLMs
    expect a flat object schema with the actual fields, so we unwrap one
    level when the schema has a single object property.
    """
    props = schema.get("properties", {})
    if len(props) == 1:
        wrapper = next(iter(props.values()))
        if isinstance(wrapper, dict) and wrapper.get("type") == "object":
            return {
                "type": "object",
                "properties": wrapper.get("properties", {}),
                "required": wrapper.get("required", []),
            }
    # Already flat or has multiple top-level keys — return as-is
    return schema


def _format_openai(tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Format tools for OpenAI's function-calling API."""
    result = []
    for tool in tools:
        params = _unwrap_input_schema(tool.get("inputSchema", {}))
        result.append({
            "type": "function",
            "function": {
                "name": tool["name"],
                "description": tool.get("description", ""),
                "parameters": params,
            },
        })
    return result


def _format_anthropic(tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Format tools for Anthropic's tool-use API."""
    result = []
    for tool in tools:
        params = _unwrap_input_schema(tool.get("inputSchema", {}))
        result.append({
            "name": tool["name"],
            "description": tool.get("description", ""),
            "input_schema": params,
        })
    return result


def _format_gemini(tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Format tools for Google Gemini / Vertex AI function-calling."""
    result = []
    for tool in tools:
        params = _unwrap_input_schema(tool.get("inputSchema", {}))
        result.append({
            "name": tool["name"],
            "description": tool.get("description", ""),
            "parameters": params,
        })
    return result


def _format_bedrock(tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Format tools for AWS Bedrock Converse API."""
    result = []
    for tool in tools:
        params = _unwrap_input_schema(tool.get("inputSchema", {}))
        result.append({
            "toolSpec": {
                "name": tool["name"],
                "description": tool.get("description", ""),
                "inputSchema": {"json": params},
            },
        })
    return result


_FORMAT_CONVERTERS = {
    "openai": _format_openai,
    "anthropic": _format_anthropic,
    "gemini": _format_gemini,
    "bedrock": _format_bedrock,
}


# ---------------------------------------------------------------------------
# Control plane helpers
# ---------------------------------------------------------------------------

class _ConnectorsAdmin:
    """Control plane: list and inspect available tools."""

    def __init__(self, registry: Dict[str, Any]) -> None:
        self._registry = registry

    def list(self) -> List[Dict[str, Any]]:
        """List all tools available in the registry."""
        result = []
        for name, data in self._registry.get("connectors", {}).items():
            result.append({
                "name": name,
                "display_name": data.get("display_name", name),
                "category": data.get("category", ""),
                "tool_count": data.get("tool_count", len(data.get("tools", {}))),
            })
        return result

    def get(self, connector_name: str) -> Dict[str, Any]:
        """Get details for a specific tool."""
        connectors = self._registry.get("connectors", {})
        data = connectors.get(connector_name)
        if data is None:
            raise ConnectorNotFoundError(connector_name)
        return {
            "name": connector_name,
            "display_name": data.get("display_name", connector_name),
            "category": data.get("category", ""),
            "tools": data.get("tools", {}),
        }

    def get_tools(self, connector_name: str) -> List[Dict[str, Any]]:
        """Get all actions for a tool with their raw schemas.

        Returns a list of action dicts, each containing:
            name, description, actionId, inputSchema, outputSchema
        """
        connectors = self._registry.get("connectors", {})
        data = connectors.get(connector_name)
        if data is None:
            raise ConnectorNotFoundError(connector_name)
        result = []
        for tool_name, tool_info in data.get("tools", {}).items():
            result.append({
                "name": tool_name,
                "description": tool_info.get("description", ""),
                "actionId": tool_info.get("actionId", ""),
                "inputSchema": tool_info.get("inputSchema", {}),
                "outputSchema": tool_info.get("outputSchema", {}),
            })
        return result

    def get_tool(self, connector_name: str, tool_name: str) -> Dict[str, Any]:
        """Get a single action's details including raw input/output schemas.

        Returns a dict with:
            name, description, actionId, inputSchema, outputSchema
        """
        connectors = self._registry.get("connectors", {})
        data = connectors.get(connector_name)
        if data is None:
            raise ConnectorNotFoundError(connector_name)
        tools = data.get("tools", {})
        tool_info = tools.get(tool_name)
        # Fallback: try without underscores (send_message -> sendmessage)
        if tool_info is None and "_" in tool_name:
            tool_info = tools.get(tool_name.replace("_", ""))
        if tool_info is None:
            raise ToolNotFoundError(connector_name, tool_name, has_tools=bool(tools))
        return {
            "name": tool_name,
            "description": tool_info.get("description", ""),
            "actionId": tool_info.get("actionId", ""),
            "inputSchema": tool_info.get("inputSchema", {}),
            "outputSchema": tool_info.get("outputSchema", {}),
        }


class _AdminSync:
    """Control plane namespace (sync): fastn.admin."""

    def __init__(self, registry: Dict[str, Any]) -> None:
        self.connectors = _ConnectorsAdmin(registry)


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _build_params_from_schema(
    tool_info: Dict[str, Any], kwargs: Dict[str, Any],
) -> Dict[str, Any]:
    """Route user kwargs into the parameter structure defined by the schema.

    The schema's top-level properties define the parameter layout the API
    expects. This function dynamically maps flat user kwargs into that
    structure without any hardcoded wrapper key assumptions.

    Patterns handled:
        Single wrapper   ``{body: {type: object, props: {channel, text}}}``
            → ``{"body": {"channel": ..., "text": ...}}``
        Multi wrapper    ``{param: {type: object, ...}, url: {type: object, ...}}``
            → ``{"param": {...}, "url": {...}}``
        Flat schema      ``{offset: {type: integer}, limit: {type: integer}}``
            → ``{"offset": ..., "limit": ...}``
        No schema        → ``{"body": {<all kwargs>}}`` (backward compat)
    """
    schema = tool_info.get("inputSchema", {})
    props = schema.get("properties", {})

    if not props:
        # No schema — fall back to wrapping under "body"
        return {"body": kwargs} if kwargs else {}

    # Build a map: inner field name → top-level group key
    # For object properties, their inner fields get routed into that group.
    # For primitive properties, they stay at the top level.
    object_groups: Dict[str, Dict[str, Any]] = {}  # group_key → inner props
    flat_fields: set = set()

    for key, pdata in props.items():
        if isinstance(pdata, dict) and pdata.get("type") == "object":
            inner = pdata.get("properties", {})
            object_groups[key] = inner
        else:
            flat_fields.add(key)

    # If there are no object groups, everything is flat
    if not object_groups:
        return kwargs

    # Route each kwarg into the correct group
    result: Dict[str, Any] = {}
    used: set = set()

    for group_key, inner_props in object_groups.items():
        group_params: Dict[str, Any] = {}
        for field_name in inner_props:
            if field_name in kwargs:
                group_params[field_name] = kwargs[field_name]
                used.add(field_name)
        if group_params:
            result[group_key] = group_params

    # Flat fields go at the top level
    for field_name in flat_fields:
        if field_name in kwargs:
            result[field_name] = kwargs[field_name]
            used.add(field_name)

    # Any remaining kwargs that weren't matched — add to the first group
    # or at top level if no groups exist
    remaining = {k: v for k, v in kwargs.items() if k not in used}
    if remaining:
        if object_groups:
            first_group = next(iter(object_groups))
            result.setdefault(first_group, {}).update(remaining)
        else:
            result.update(remaining)

    return result


def _resolve_connector(
    registry: Dict[str, Any], connector_name: str
) -> tuple:
    """Look up a connector in the registry.

    Returns (connector_id, tools_dict) where tools_dict maps
    tool_name -> {"actionId": str, "inputSchema": dict}.
    """
    connectors = registry.get("connectors", {})
    connector_data = connectors.get(connector_name)
    if connector_data is None:
        raise ConnectorNotFoundError(connector_name)
    connector_id = connector_data.get("id", "")
    tools = {}
    for tool_name, tool_info in connector_data.get("tools", {}).items():
        tools[tool_name] = {
            "actionId": tool_info.get("actionId", ""),
            "inputSchema": tool_info.get("inputSchema", {}),
        }
    return connector_id, tools


def _build_execute_payload(
    action_id: str,
    parameters: Dict[str, Any],
    connector_id: str = "",
    agent_id: str = "",
    connection_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Build the executeTool request body.

    *parameters* should already be structured to match the API schema
    (e.g. via ``_build_params_from_schema``).
    """
    payload: Dict[str, Any] = {
        "input": {
            "actionId": action_id,
            "connectorId": connector_id,
            "agentId": agent_id,
            "parameters": parameters,
        }
    }
    if connection_id:
        payload["input"]["connectionId"] = connection_id
    return payload


def _all_tools_from_registry(registry: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Collect all tool name -> {actionId, inputSchema} mappings across all connectors."""
    all_tools: Dict[str, Dict[str, Any]] = {}
    for connector_data in registry.get("connectors", {}).values():
        for tool_name, tool_info in connector_data.get("tools", {}).items():
            all_tools[tool_name] = {
                "actionId": tool_info.get("actionId", ""),
                "inputSchema": tool_info.get("inputSchema", {}),
            }
    return all_tools


def _redact_headers(headers: Dict[str, str]) -> Dict[str, str]:
    """Redact sensitive header values for logging."""
    redacted = {}
    for k, v in headers.items():
        if k.lower() in ("authorization", "x-fastn-api-key") and len(str(v)) > 20:
            redacted[k] = str(v)[:20] + "..."
        else:
            redacted[k] = v
    return redacted


def _init_config(
    api_key: Optional[str],
    project_id: Optional[str],
    timeout: Optional[float],
    config_path: Optional[str],
    auth_token: Optional[str],
    tenant_id: Optional[str] = None,
    stage: Optional[str] = None,
) -> FastnConfig:
    """Load config from file/env, override with explicit params."""
    file_config = load_config(config_path)

    resolved_api_key = api_key or file_config.api_key
    resolved_auth_token = auth_token or file_config.auth_token

    # If the user explicitly provided an api_key, don't inherit auth_token
    # from the config file — they've chosen API key auth, not JWT.
    if api_key and not auth_token:
        resolved_auth_token = ""

    return FastnConfig(
        api_key=resolved_api_key,
        project_id=project_id or file_config.project_id,
        tenant_id=tenant_id or file_config.tenant_id,
        stage=stage or file_config.stage,
        timeout=timeout or file_config.timeout,
        auth_token=resolved_auth_token,
    )


# ---------------------------------------------------------------------------
# Sync client
# ---------------------------------------------------------------------------

class FastnClient:
    """Synchronous Fastn SDK client.

    Usage:
        fastn = FastnClient(api_key="...", project_id="...")

        # Data plane — call tools directly
        fastn.slack.send_message(channel="general", text="Hello!")

        # Data plane — specific connection
        fastn.slack.send_message(connection_id="conn_123", channel="general", text="Hello!")

        # Data plane — bound connection
        slack = fastn.connect("conn_123")
        slack.send_message(channel="general", text="Hello!")

        # Control plane
        connectors = fastn.admin.connectors.list()

        # LLM agent integration
        tools = fastn.get_tools_for("Send a Slack message", format="openai")
        result = fastn.execute(action_id, llm_generated_params)

        # AI-powered
        result = fastn.run("Send hello to #general on Slack")
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        project_id: Optional[str] = None,
        timeout: Optional[float] = None,
        config_path: Optional[str] = None,
        auth_token: Optional[str] = None,
        agent_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
        stage: Optional[str] = None,
        max_retries: int = MAX_RETRIES,
        verbose: bool = False,
    ) -> None:
        self._config = _init_config(
            api_key, project_id,
            timeout, config_path, auth_token, tenant_id, stage,
        )
        self._config.validate()
        self._headers = build_headers(self._config)
        self._max_retries = max_retries
        self._agent_id = agent_id or self._config.resolve_project_id()
        self._verbose = verbose

        fastn_dir = None
        if config_path:
            fastn_dir = Path(config_path).parent
        self._registry = load_registry(fastn_dir)
        self._migrations = load_migrations(fastn_dir)
        self._connectors: Dict[str, DynamicConnector] = {}
        self._http = httpx.Client(
            timeout=self._config.timeout,
            headers=self._headers,
        )
        self.admin = _AdminSync(self._registry)

    def connect(self, connection_id: str) -> DynamicConnector:
        """Bind a connection_id and return a connector proxy.

        All tool calls through this proxy will use the given connection_id,
        so you don't have to pass it on every call.

        Usage:
            slack = fastn.connect("conn_slack_abc")
            slack.send_message(channel="general", text="Hello!")
            slack.create_channel(name="new-channel")
        """
        all_tools = _all_tools_from_registry(self._registry)
        return DynamicConnector(
            connector_name="*",
            tools=all_tools,
            execute_fn=self._execute_tool,
            connection_id=connection_id,
        )

    def __getattr__(self, name: str) -> DynamicConnector:
        """Resolve a connector name to a :class:`DynamicConnector` proxy.

        This is the mechanism behind ``fastn.slack.send_message(...)``:

        1. ``fastn.slack`` calls ``__getattr__("slack")``
        2. The local registry is searched for a connector called ``"slack"``
        3. A :class:`DynamicConnector` is created with the connector's
           action definitions and cached for subsequent accesses

        Args:
            name: Connector name (e.g. ``"slack"``, ``"jira"``, ``"github"``).

        Returns:
            A :class:`DynamicConnector` proxy whose methods correspond to
            the connector's actions.

        Raises:
            ConnectorNotFoundError: If *name* is not in the local registry
                (hint: run ``fastn sync && fastn add <name>``).
            AttributeError: If *name* is a reserved attribute (``admin``,
                ``connect``, ``execute``, etc.) or starts with ``_``.
        """
        if name.startswith("_") or name in (
            "admin", "connect", "run", "close", "execute",
            "get_tools", "get_tool", "get_tools_for",
        ):
            raise AttributeError(name)

        if name in self._connectors:
            return self._connectors[name]

        connector_id, tools = _resolve_connector(self._registry, name)

        connector_migrations = (
            self._migrations.get("connectors", {}).get(name, {})
        )
        proxy = DynamicConnector(
            connector_name=name,
            tools=tools,
            execute_fn=self._execute_tool,
            connector_id=connector_id,
            migrations=connector_migrations,
        )
        self._connectors[name] = proxy
        return proxy

    def _ensure_fresh_token(self) -> None:
        """Refresh the access token if it is expired."""
        if not self._config.refresh_token or not self._config.token_expiry:
            return
        from fastn.oauth import (
            compute_token_expiry,
            is_token_expired,
            refresh_access_token,
        )

        if is_token_expired(self._config.token_expiry):
            token_resp = refresh_access_token(self._config.refresh_token)
            self._config.auth_token = token_resp.access_token
            self._config.refresh_token = token_resp.refresh_token
            self._config.token_expiry = compute_token_expiry(token_resp.expires_in)
            self._headers["Authorization"] = f"Bearer {self._config.auth_token}"
            self._http.headers["Authorization"] = f"Bearer {self._config.auth_token}"

    def _log(self, *args: Any) -> None:
        """Print debug info when verbose mode is enabled."""
        if self._verbose:
            print("[fastn]", *args)

    def _execute_tool(
        self,
        action_id: str,
        params: Dict[str, Any],
        connector_id: str = "",
        tool_info: Optional[Dict[str, Any]] = None,
        connection_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
    ) -> Any:
        """Execute a tool via the Fastn API with retry logic."""
        self._ensure_fresh_token()
        url = f"{API_BASE_URL}/executeTool"
        # When tool_info is provided (SDK proxy path), route params dynamically
        # based on the tool's inputSchema. When tool_info is None (execute() /
        # LLM agent path), params are already structured by the caller.
        parameters = _build_params_from_schema(tool_info, params) if tool_info else params
        payload = _build_execute_payload(
            action_id, parameters, connector_id, self._agent_id, connection_id
        )

        # Per-call tenant override
        headers = dict(self._headers)
        if tenant_id:
            headers["x-fastn-space-tenantid"] = tenant_id

        self._log(f"POST {url}")
        self._log(f"Headers: {json.dumps(_redact_headers(headers), indent=2)}")
        self._log(f"Payload: {json.dumps(payload, indent=2)}")

        last_error: Optional[Exception] = None
        for attempt in range(self._max_retries + 1):
            try:
                response = self._http.post(url, json=payload, headers=headers)
                self._log(f"Response {response.status_code}: {response.text}")
                if response.status_code == 401:
                    raise AuthError(
                        "Authentication failed. Check your API key and credentials."
                    )
                if response.status_code == 429:
                    if attempt < self._max_retries:
                        time.sleep(BACKOFF_FACTOR * (2 ** attempt))
                        continue
                if response.status_code >= 400:
                    body = None
                    try:
                        body = response.json()
                    except Exception:
                        pass
                    raise APIError(
                        f"API error {response.status_code}: {response.text}",
                        status_code=response.status_code,
                        response_body=body,
                    )
                data = response.json()
                # Unwrap: API returns {body, statusCode, rawBody} — return just body
                if isinstance(data, dict) and "body" in data:
                    return data["body"]
                return data
            except (httpx.ConnectError, httpx.ReadTimeout) as e:
                last_error = e
                if attempt < self._max_retries:
                    time.sleep(BACKOFF_FACTOR * (2 ** attempt))
                    continue
                raise APIError(
                    f"Connection failed after {self._max_retries + 1} attempts: {e}"
                ) from e

        raise APIError(f"Request failed: {last_error}") from last_error

    # ----- Public API: tool execution -----

    def execute(
        self,
        action_id: str,
        params: Dict[str, Any],
        connection_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
    ) -> Any:
        """Execute a tool by action ID with pre-built parameters.

        Designed for LLM agent workflows where you:
        1. Get tool schemas via ``get_tools()`` or ``get_tools_for()``
        2. Feed the schema to an LLM to generate params
        3. Call ``execute()`` with the LLM-generated params

        Args:
            action_id: The tool's action ID (from ``get_tool()["actionId"]``).
            params: The parameters dict (e.g. from LLM function-calling output).
            connection_id: Optional connection ID for multi-connection setups.
            tenant_id: Optional tenant override.

        Returns:
            The API response as a dict.

        Example:
            tool = fastn.get_tool("slack", "sendmessage")
            # Feed tool["inputSchema"] to your LLM → get params
            result = fastn.execute(tool["actionId"], {"channel": "general", "text": "Hi"})
        """
        return self._execute_tool(
            action_id, params, "",
            tool_info=None, connection_id=connection_id, tenant_id=tenant_id,
        )

    # ----- Public API: tool discovery -----

    def run(
        self,
        prompt: str,
        connection_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """AI-powered tool execution.

        Uses natural language to discover the right tool and execute it.

        Args:
            prompt: Natural language description of what to do.
            connection_id: Optional connection ID.

        Returns:
            The API response as a dict.
        """
        self._ensure_fresh_token()
        get_tools_url = f"{API_BASE_URL}/getTools"
        discovery_payload: Dict[str, Any] = {
            "input": {
                "limit": 1,
                "prompt": prompt,
            }
        }
        response = self._http.post(get_tools_url, json=discovery_payload)
        if response.status_code >= 400:
            raise APIError(
                f"Tool discovery failed: {response.text}",
                status_code=response.status_code,
            )
        tools = response.json()

        tool_list = tools if isinstance(tools, list) else tools.get("tools", [])
        if not tool_list:
            raise FastnError(f"No tools found matching prompt: '{prompt}'")

        top_tool = tool_list[0]
        action_id = top_tool.get("actionId", "")

        execute_payload = _build_execute_payload(
            action_id, top_tool.get("parameters", {}),
            connection_id,
        )
        result = self._http.post(
            f"{API_BASE_URL}/executeTool", json=execute_payload
        )
        if result.status_code >= 400:
            raise APIError(
                f"Tool execution failed: {result.text}",
                status_code=result.status_code,
            )
        return result.json()

    # ----- Public API: schema access -----

    def get_tools(self, connector_name: str) -> List[Dict[str, Any]]:
        """Get all actions for a tool with raw input/output schemas.

        Args:
            connector_name: Name of the tool (e.g. "slack").

        Returns:
            List of action dicts with name, description, actionId, inputSchema, outputSchema.
        """
        return self.admin.connectors.get_tools(connector_name)

    def get_tool(self, connector_name: str, tool_name: str) -> Dict[str, Any]:
        """Get a single action's raw input/output schema.

        Args:
            connector_name: Name of the tool (e.g. "slack").
            tool_name: Name of the action (e.g. "sendmessage").

        Returns:
            Action dict with name, description, actionId, inputSchema, outputSchema.
        """
        return self.admin.connectors.get_tool(connector_name, tool_name)

    def get_tools_for(
        self,
        prompt: str,
        *,
        format: str = "openai",
        limit: int = 5,
        connector: Union[str, List[str], None] = None,
    ) -> List[Dict[str, Any]]:
        """Get tools formatted for a specific LLM provider's tool-use API.

        Describe what you need in natural language and Fastn discovers the
        right tools.  Alternatively, pass ``connector`` to select tools from
        specific connectors by name.

        Supported formats:
          - ``"openai"``    — OpenAI function-calling format
          - ``"anthropic"`` — Anthropic tool-use format
          - ``"gemini"``    — Google Gemini / Vertex AI format
          - ``"bedrock"``   — AWS Bedrock Converse API format
          - ``"raw"``       — Raw Fastn schemas

        Args:
            prompt: Natural language description of what you need
                (e.g. ``"Send a message on Slack"``).
            format: LLM provider format. Defaults to ``"openai"``.
            limit: Maximum number of tools to return. Defaults to 5.
            connector: Optional connector name or list of names for direct
                registry lookup instead of prompt-based discovery
                (e.g. ``"slack"`` or ``["slack", "jira"]``).

        Returns:
            List of tool definitions in the requested format.

        Raises:
            ValueError: If format is not supported.
            APIError: If prompt-based discovery fails.
            ConnectorNotFoundError: If a named connector is not in the registry.

        Example::

            # Prompt-based (recommended) — discovers the right tools
            tools = fastn.get_tools_for(
                "Send a message on Slack",
                format="openai",
            )

            # Multiple connectors by name (power user)
            tools = fastn.get_tools_for(
                "project tools",
                connector=["slack", "jira"],
                format="openai",
                limit=10,
            )
        """
        if format not in _SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported format '{format}'. "
                f"Choose from: {', '.join(_SUPPORTED_FORMATS)}"
            )

        if connector is not None:
            # Local registry lookup
            names = [connector] if isinstance(connector, str) else connector
            raw_tools: List[Dict[str, Any]] = []
            for name in names:
                raw_tools.extend(self.admin.connectors.get_tools(name))
            raw_tools = raw_tools[:limit]
            if format == "raw":
                return raw_tools
            return _FORMAT_CONVERTERS[format](raw_tools)

        # Prompt-based discovery via /getTools API
        self._ensure_fresh_token()
        headers = self._config.get_headers()
        response = self._http.post(
            f"{API_BASE_URL}/getTools",
            json={"input": {"prompt": prompt, "limit": limit}},
            headers=headers,
        )
        if response.status_code >= 400:
            raise APIError(
                f"Tool discovery failed: {response.text}",
                status_code=response.status_code,
            )
        data = response.json()
        tool_list = data if isinstance(data, list) else data.get("tools", [])
        if format == "raw":
            return tool_list
        return _FORMAT_CONVERTERS[format](tool_list)

    # ----- Lifecycle -----

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._http.close()

    def __enter__(self) -> FastnClient:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def __repr__(self) -> str:
        n = len(self._registry.get("connectors", {}))
        return f"<FastnClient ({n} tools in registry)>"


# ---------------------------------------------------------------------------
# Async client
# ---------------------------------------------------------------------------

class AsyncFastnClient:
    """Asynchronous Fastn SDK client.

    Usage:
        async with AsyncFastnClient(api_key="...", project_id="...") as fastn:
            response = await fastn.slack.send_message(channel="general", text="Hello!")

            # LLM agent integration
            tools = await fastn.get_tools_for("Send a Slack message", format="anthropic")
            result = await fastn.execute(action_id, llm_params)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        project_id: Optional[str] = None,
        timeout: Optional[float] = None,
        config_path: Optional[str] = None,
        auth_token: Optional[str] = None,
        agent_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
        stage: Optional[str] = None,
        max_retries: int = MAX_RETRIES,
        verbose: bool = False,
    ) -> None:
        self._config = _init_config(
            api_key, project_id,
            timeout, config_path, auth_token, tenant_id, stage,
        )
        self._config.validate()
        self._headers = build_headers(self._config)
        self._max_retries = max_retries
        self._agent_id = agent_id or self._config.resolve_project_id()
        self._verbose = verbose

        fastn_dir = None
        if config_path:
            fastn_dir = Path(config_path).parent
        self._registry = load_registry(fastn_dir)
        self._migrations = load_migrations(fastn_dir)
        self._connectors: Dict[str, AsyncDynamicConnector] = {}
        self._http = httpx.AsyncClient(
            timeout=self._config.timeout,
            headers=self._headers,
        )
        self.admin = _AdminSync(self._registry)

    def _log(self, *args: Any) -> None:
        """Print debug info when verbose mode is enabled."""
        if self._verbose:
            print("[fastn]", *args)

    def connect(self, connection_id: str) -> AsyncDynamicConnector:
        """Bind a connection_id and return an async connector proxy."""
        all_tools = _all_tools_from_registry(self._registry)
        return AsyncDynamicConnector(
            connector_name="*",
            tools=all_tools,
            execute_fn=self._execute_tool,
            connection_id=connection_id,
        )

    def __getattr__(self, name: str) -> AsyncDynamicConnector:
        """Resolve a connector name to an :class:`AsyncDynamicConnector` proxy.

        Async equivalent of :meth:`FastnClient.__getattr__`.  Usage::

            async with AsyncFastnClient() as fastn:
                result = await fastn.slack.send_message(channel="general", text="Hi")

        Args:
            name: Connector name (e.g. ``"slack"``, ``"jira"``).

        Returns:
            An :class:`AsyncDynamicConnector` whose methods are coroutines.

        Raises:
            ConnectorNotFoundError: If *name* is not in the local registry.
            AttributeError: If *name* is reserved or starts with ``_``.
        """
        if name.startswith("_") or name in (
            "admin", "connect", "run", "close", "execute",
            "get_tools", "get_tool", "get_tools_for",
        ):
            raise AttributeError(name)

        if name in self._connectors:
            return self._connectors[name]

        connector_id, tools = _resolve_connector(self._registry, name)

        connector_migrations = (
            self._migrations.get("connectors", {}).get(name, {})
        )
        proxy = AsyncDynamicConnector(
            connector_name=name,
            tools=tools,
            execute_fn=self._execute_tool,
            connector_id=connector_id,
            migrations=connector_migrations,
        )
        self._connectors[name] = proxy
        return proxy

    def _ensure_fresh_token(self) -> None:
        """Refresh the access token if it is expired (sync, for use before async calls)."""
        if not self._config.refresh_token or not self._config.token_expiry:
            return
        from fastn.oauth import (
            compute_token_expiry,
            is_token_expired,
            refresh_access_token,
        )

        if is_token_expired(self._config.token_expiry):
            token_resp = refresh_access_token(self._config.refresh_token)
            self._config.auth_token = token_resp.access_token
            self._config.refresh_token = token_resp.refresh_token
            self._config.token_expiry = compute_token_expiry(token_resp.expires_in)
            self._headers["Authorization"] = f"Bearer {self._config.auth_token}"
            self._http.headers["Authorization"] = f"Bearer {self._config.auth_token}"

    async def _execute_tool(
        self,
        action_id: str,
        params: Dict[str, Any],
        connector_id: str = "",
        tool_info: Optional[Dict[str, Any]] = None,
        connection_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
    ) -> Any:
        """Execute a tool via the Fastn API with retry logic (async)."""
        import asyncio

        self._ensure_fresh_token()
        url = f"{API_BASE_URL}/executeTool"
        # When tool_info is provided (SDK proxy path), route params dynamically
        # based on the tool's inputSchema. When tool_info is None (execute() /
        # LLM agent path), params are already structured by the caller.
        parameters = _build_params_from_schema(tool_info, params) if tool_info else params
        payload = _build_execute_payload(
            action_id, parameters, connector_id, self._agent_id, connection_id
        )

        # Per-call tenant override
        headers = dict(self._headers)
        if tenant_id:
            headers["x-fastn-space-tenantid"] = tenant_id

        self._log(f"POST {url}")
        self._log(f"Payload: {json.dumps(payload, indent=2)}")

        last_error: Optional[Exception] = None
        for attempt in range(self._max_retries + 1):
            try:
                response = await self._http.post(url, json=payload, headers=headers)
                if response.status_code == 401:
                    raise AuthError(
                        "Authentication failed. Check your API key and credentials."
                    )
                if response.status_code == 429:
                    if attempt < self._max_retries:
                        await asyncio.sleep(BACKOFF_FACTOR * (2 ** attempt))
                        continue
                if response.status_code >= 400:
                    body = None
                    try:
                        body = response.json()
                    except Exception:
                        pass
                    raise APIError(
                        f"API error {response.status_code}: {response.text}",
                        status_code=response.status_code,
                        response_body=body,
                    )
                data = response.json()
                # Unwrap: API returns {body, statusCode, rawBody} — return just body
                if isinstance(data, dict) and "body" in data:
                    return data["body"]
                return data
            except (httpx.ConnectError, httpx.ReadTimeout) as e:
                last_error = e
                if attempt < self._max_retries:
                    await asyncio.sleep(BACKOFF_FACTOR * (2 ** attempt))
                    continue
                raise APIError(
                    f"Connection failed after {self._max_retries + 1} attempts: {e}"
                ) from e

        raise APIError(f"Request failed: {last_error}") from last_error

    # ----- Public API: tool execution -----

    async def execute(
        self,
        action_id: str,
        params: Dict[str, Any],
        connection_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
    ) -> Any:
        """Execute a tool by action ID with pre-built parameters (async).

        See ``FastnClient.execute()`` for full documentation.
        """
        return await self._execute_tool(
            action_id, params, "",
            tool_info=None, connection_id=connection_id, tenant_id=tenant_id,
        )

    # ----- Public API: tool discovery -----

    async def run(
        self,
        prompt: str,
        connection_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """AI-powered tool execution (async version)."""
        self._ensure_fresh_token()
        get_tools_url = f"{API_BASE_URL}/getTools"
        discovery_payload: Dict[str, Any] = {
            "input": {
                "limit": 1,
                "prompt": prompt,
            }
        }
        response = await self._http.post(get_tools_url, json=discovery_payload)
        if response.status_code >= 400:
            raise APIError(
                f"Tool discovery failed: {response.text}",
                status_code=response.status_code,
            )
        tools = response.json()

        tool_list = tools if isinstance(tools, list) else tools.get("tools", [])
        if not tool_list:
            raise FastnError(f"No tools found matching prompt: '{prompt}'")

        top_tool = tool_list[0]
        action_id = top_tool.get("actionId", "")

        execute_payload = _build_execute_payload(
            action_id, top_tool.get("parameters", {}),
            connection_id,
        )
        result = await self._http.post(
            f"{API_BASE_URL}/executeTool", json=execute_payload
        )
        if result.status_code >= 400:
            raise APIError(
                f"Tool execution failed: {result.text}",
                status_code=result.status_code,
            )
        return result.json()

    # ----- Public API: schema access -----

    def get_tools(self, connector_name: str) -> List[Dict[str, Any]]:
        """Get all actions for a tool with raw input/output schemas."""
        return self.admin.connectors.get_tools(connector_name)

    def get_tool(self, connector_name: str, tool_name: str) -> Dict[str, Any]:
        """Get a single action's raw input/output schema."""
        return self.admin.connectors.get_tool(connector_name, tool_name)

    async def get_tools_for(
        self,
        prompt: str,
        *,
        format: str = "openai",
        limit: int = 5,
        connector: Union[str, List[str], None] = None,
    ) -> List[Dict[str, Any]]:
        """Get tools formatted for a specific LLM provider's tool-use API.

        See ``FastnClient.get_tools_for()`` for full documentation.
        """
        if format not in _SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported format '{format}'. "
                f"Choose from: {', '.join(_SUPPORTED_FORMATS)}"
            )

        if connector is not None:
            names = [connector] if isinstance(connector, str) else connector
            raw_tools: List[Dict[str, Any]] = []
            for name in names:
                raw_tools.extend(self.admin.connectors.get_tools(name))
            raw_tools = raw_tools[:limit]
            if format == "raw":
                return raw_tools
            return _FORMAT_CONVERTERS[format](raw_tools)

        # Prompt-based discovery via /getTools API
        self._ensure_fresh_token()
        headers = self._config.get_headers()
        response = await self._http.post(
            f"{API_BASE_URL}/getTools",
            json={"input": {"prompt": prompt, "limit": limit}},
            headers=headers,
        )
        if response.status_code >= 400:
            raise APIError(
                f"Tool discovery failed: {response.text}",
                status_code=response.status_code,
            )
        data = response.json()
        tool_list = data if isinstance(data, list) else data.get("tools", [])
        if format == "raw":
            return tool_list
        return _FORMAT_CONVERTERS[format](tool_list)

    # ----- Lifecycle -----

    async def close(self) -> None:
        """Close the underlying async HTTP client."""
        await self._http.aclose()

    async def __aenter__(self) -> AsyncFastnClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    def __repr__(self) -> str:
        n = len(self._registry.get("connectors", {}))
        return f"<AsyncFastnClient ({n} tools in registry)>"
