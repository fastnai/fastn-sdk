"""Fastn SDK client — sync and async.

This module contains the two main entry points: ``FastnClient`` (sync) and
``AsyncFastnClient`` (async). Both provide identical APIs for:

Data plane — call tools directly:
    fastn = FastnClient(api_key="...", project_id="...")
    fastn.slack.send_message(channel="general", text="Hello!")

Control plane — inspect the registry:
    connectors = fastn.connectors.list()
    tools = fastn.get_tools("slack")
    tool = fastn.get_tool("slack", "send_message")

LLM agent integration — describe what you need, get tool schemas:
    tools = fastn.get_tools_for("Send a message on Slack", format="openai")
    result = fastn.execute(tool="act_slack_send_message", params={...})

AI-powered mode — natural language tool discovery:
    result = fastn.run("Send hello to #general on Slack")

Constructor parameters:
    api_key, project_id, auth_token, tenant_id, stage,
    config_path, timeout, max_retries, verbose
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

# Internal modules — split from this file for maintainability
from fastn._constants import (
    API_BASE_URL,
    BACKOFF_FACTOR,
    MAX_RETRIES,
    _SUPPORTED_FORMATS,
)
from fastn._formatters import _FORMAT_CONVERTERS
from fastn._http import _redact_headers
from fastn._catalog import _ConnectorCatalog, _ConnectorCatalogAsync
from fastn._flows import _FlowsSync, _FlowsAsync
from fastn._auth_ns import _AuthSync, _AuthAsync
from fastn._projects import _ProjectsSync, _ProjectsAsync
from fastn._skills import _SkillsSync, _SkillsAsync
from fastn._kit import _KitSync, _KitAsync

# Re-exports for backward compatibility (CLI imports these from fastn.client)
from fastn._formatters import _unwrap_input_schema  # noqa: F401
from fastn._constants import GRAPHQL_URL, GET_ORGANIZATIONS_QUERY  # noqa: F401


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
        tenant_id=tenant_id if tenant_id is not None else file_config.tenant_id,
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

        # Control plane
        connector_list = fastn.connectors.list()

        # LLM agent integration
        tools = fastn.get_tools_for("Send a Slack message", format="openai")
        result = fastn.execute(tool=action_id, params=llm_generated_params)

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
        self.connectors = _ConnectorCatalog(self._registry)
        self.flows = _FlowsSync(self)
        self.auth = _AuthSync(self)
        self.projects = _ProjectsSync(self)
        self.skills = _SkillsSync(self)
        self.kit = _KitSync(self)

    def connect(self, connection_id: str) -> DynamicConnector:
        """Bind a connection_id and return a connector proxy."""
        all_tools = _all_tools_from_registry(self._registry)
        return DynamicConnector(
            connector_name="*",
            tools=all_tools,
            execute_fn=self._execute_tool,
            connection_id=connection_id,
        )

    def __getattr__(self, name: str) -> DynamicConnector:
        """Resolve a connector name to a :class:`DynamicConnector` proxy."""
        if name.startswith("_") or name in (
            "connectors", "connect", "run", "close", "execute",
            "get_tools", "get_tool", "get_tools_for",
            "flows", "auth", "projects", "skills", "kit",
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
        parameters = _build_params_from_schema(tool_info, params) if tool_info else params
        payload = _build_execute_payload(
            action_id, parameters, connector_id, self._agent_id, connection_id
        )

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

    def execute(
        self,
        tool: str,
        params: Dict[str, Any],
        connection_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
    ) -> Any:
        """Execute a tool by action ID with pre-built parameters."""
        action_id = tool
        return self._execute_tool(
            action_id, params, "",
            tool_info=None, connection_id=connection_id, tenant_id=tenant_id,
        )

    def run(
        self,
        prompt: str,
        connection_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """AI-powered tool execution."""
        self._ensure_fresh_token()
        get_tools_url = f"{API_BASE_URL}/getTools"
        discovery_payload: Dict[str, Any] = {
            "input": {
                "limit": 1,
                "prompt": prompt,
            }
        }
        self._log(f"POST {get_tools_url}")
        self._log(f"Payload: {json.dumps(discovery_payload, indent=2)}")
        response = self._http.post(get_tools_url, json=discovery_payload)
        self._log(f"Response {response.status_code}: {response.text[:2000]}")
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
            connection_id=connection_id,
        )
        self._log(f"POST {API_BASE_URL}/executeTool")
        self._log(f"Payload: {json.dumps(execute_payload, indent=2)}")
        result = self._http.post(
            f"{API_BASE_URL}/executeTool", json=execute_payload
        )
        self._log(f"Response {result.status_code}: {result.text[:2000]}")
        if result.status_code >= 400:
            raise APIError(
                f"Tool execution failed: {result.text}",
                status_code=result.status_code,
            )
        return result.json()

    def get_tools(self, connector_name: str) -> List[Dict[str, Any]]:
        """Get all tools for a connector with raw input/output schemas."""
        return self.connectors.get_tools(connector_name)

    def get_tool(self, connector_name: str, tool_name: str) -> Dict[str, Any]:
        """Get a single tool's raw input/output schema."""
        return self.connectors.get_tool(connector_name, tool_name)

    def get_tools_for(
        self,
        prompt: str,
        *,
        format: str = "openai",
        limit: int = 5,
        connector: Union[str, List[str], None] = None,
    ) -> List[Dict[str, Any]]:
        """Get tools formatted for a specific LLM provider's tool-use API."""
        if format not in _SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported format '{format}'. "
                f"Choose from: {', '.join(_SUPPORTED_FORMATS)}"
            )

        if connector is not None:
            names = [connector] if isinstance(connector, str) else connector
            raw_tools: List[Dict[str, Any]] = []
            for name in names:
                raw_tools.extend(self.connectors.get_tools(name))
            raw_tools = raw_tools[:limit]
            if format == "raw":
                return raw_tools
            return _FORMAT_CONVERTERS[format](raw_tools)

        self._ensure_fresh_token()
        headers = self._config.get_headers()
        discovery_payload = {"input": {"prompt": prompt, "limit": limit}}
        self._log(f"POST {API_BASE_URL}/getTools")
        self._log(f"Payload: {json.dumps(discovery_payload, indent=2)}")
        response = self._http.post(
            f"{API_BASE_URL}/getTools",
            json=discovery_payload,
            headers=headers,
        )
        self._log(f"Response {response.status_code}: {response.text[:2000]}")
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

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._http.close()

    def __enter__(self) -> FastnClient:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def __repr__(self) -> str:
        n = len(self._registry.get("connectors", {}))
        return f"<FastnClient ({n} connectors in registry)>"


# ---------------------------------------------------------------------------
# Async client
# ---------------------------------------------------------------------------

class AsyncFastnClient:
    """Asynchronous Fastn SDK client.

    Usage:
        async with AsyncFastnClient(api_key="...", project_id="...") as fastn:
            response = await fastn.slack.send_message(channel="general", text="Hello!")
            tools = await fastn.get_tools_for("Send a Slack message", format="anthropic")
            result = await fastn.execute(tool=action_id, params=llm_params)
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
        self.connectors = _ConnectorCatalogAsync(self, self._registry)
        self.flows = _FlowsAsync(self)
        self.auth = _AuthAsync(self)
        self.projects = _ProjectsAsync(self)
        self.skills = _SkillsAsync(self)
        self.kit = _KitAsync(self)

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
        """Resolve a connector name to an :class:`AsyncDynamicConnector` proxy."""
        if name.startswith("_") or name in (
            "connectors", "connect", "run", "close", "execute",
            "get_tools", "get_tool", "get_tools_for",
            "flows", "auth", "projects", "skills", "kit",
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
        parameters = _build_params_from_schema(tool_info, params) if tool_info else params
        payload = _build_execute_payload(
            action_id, parameters, connector_id, self._agent_id, connection_id
        )

        headers = dict(self._headers)
        if tenant_id:
            headers["x-fastn-space-tenantid"] = tenant_id

        self._log(f"POST {url}")
        self._log(f"Headers: {json.dumps(_redact_headers(headers), indent=2)}")
        self._log(f"Payload: {json.dumps(payload, indent=2)}")

        last_error: Optional[Exception] = None
        for attempt in range(self._max_retries + 1):
            try:
                response = await self._http.post(url, json=payload, headers=headers)
                self._log(f"Response {response.status_code}: {response.text[:2000]}")
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

    async def execute(
        self,
        tool: str,
        params: Dict[str, Any],
        connection_id: Optional[str] = None,
        tenant_id: Optional[str] = None,
    ) -> Any:
        """Execute a tool by action ID with pre-built parameters (async)."""
        action_id = tool
        return await self._execute_tool(
            action_id, params, "",
            tool_info=None, connection_id=connection_id, tenant_id=tenant_id,
        )

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
        self._log(f"POST {get_tools_url}")
        self._log(f"Payload: {json.dumps(discovery_payload, indent=2)}")
        response = await self._http.post(get_tools_url, json=discovery_payload)
        self._log(f"Response {response.status_code}: {response.text[:2000]}")
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
            connection_id=connection_id,
        )
        self._log(f"POST {API_BASE_URL}/executeTool")
        self._log(f"Payload: {json.dumps(execute_payload, indent=2)}")
        result = await self._http.post(
            f"{API_BASE_URL}/executeTool", json=execute_payload
        )
        self._log(f"Response {result.status_code}: {result.text[:2000]}")
        if result.status_code >= 400:
            raise APIError(
                f"Tool execution failed: {result.text}",
                status_code=result.status_code,
            )
        return result.json()

    def get_tools(self, connector_name: str) -> List[Dict[str, Any]]:
        """Get all tools for a connector with raw input/output schemas."""
        return self.connectors.get_tools(connector_name)

    def get_tool(self, connector_name: str, tool_name: str) -> Dict[str, Any]:
        """Get a single tool's raw input/output schema."""
        return self.connectors.get_tool(connector_name, tool_name)

    async def get_tools_for(
        self,
        prompt: str,
        *,
        format: str = "openai",
        limit: int = 5,
        connector: Union[str, List[str], None] = None,
    ) -> List[Dict[str, Any]]:
        """Get tools formatted for a specific LLM provider's tool-use API."""
        if format not in _SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported format '{format}'. "
                f"Choose from: {', '.join(_SUPPORTED_FORMATS)}"
            )

        if connector is not None:
            names = [connector] if isinstance(connector, str) else connector
            raw_tools: List[Dict[str, Any]] = []
            for name in names:
                raw_tools.extend(self.connectors.get_tools(name))
            raw_tools = raw_tools[:limit]
            if format == "raw":
                return raw_tools
            return _FORMAT_CONVERTERS[format](raw_tools)

        self._ensure_fresh_token()
        headers = self._config.get_headers()
        discovery_payload = {"input": {"prompt": prompt, "limit": limit}}
        self._log(f"POST {API_BASE_URL}/getTools")
        self._log(f"Payload: {json.dumps(discovery_payload, indent=2)}")
        response = await self._http.post(
            f"{API_BASE_URL}/getTools",
            json=discovery_payload,
            headers=headers,
        )
        self._log(f"Response {response.status_code}: {response.text[:2000]}")
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

    async def close(self) -> None:
        """Close the underlying async HTTP client."""
        await self._http.aclose()

    async def __aenter__(self) -> AsyncFastnClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    def __repr__(self) -> str:
        n = len(self._registry.get("connectors", {}))
        return f"<AsyncFastnClient ({n} connectors in registry)>"
