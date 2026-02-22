"""Connector catalog — control plane for listing and inspecting connectors."""

from __future__ import annotations

from typing import Any, Dict, List

from fastn._constants import SEARCH_CONNECTORS_QUERY
from fastn._http import _gql_call_async
from fastn.exceptions import ConnectorNotFoundError, ToolNotFoundError


class _ConnectorCatalog:
    """Control plane: list and inspect available connectors and their tools.

    Accessed as ``fastn.connectors.*``.
    """

    def __init__(self, registry: Dict[str, Any]) -> None:
        self._registry = registry

    def list(self) -> List[Dict[str, Any]]:
        """List all connectors (integrations like Gmail, Slack, Jira) in the registry."""
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
        """Get details for a specific connector."""
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
        """Get all tools for a connector with their raw schemas.

        Returns a list of tool dicts, each containing:
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
        """Get a single tool's details including raw input/output schemas.

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


class _ConnectorCatalogAsync(_ConnectorCatalog):
    """Connector catalog (async): list connectors via the Fastn API.

    Accessed as ``fastn.connectors.*`` on ``AsyncFastnClient``.
    Inherits registry-based ``get``, ``get_tools``, and ``get_tool`` from
    ``_ConnectorCatalog``, but overrides ``list()`` to fetch connectors
    from the GraphQL API instead of the local registry file.
    """

    def __init__(self, client: Any, registry: Dict[str, Any]) -> None:
        super().__init__(registry)
        self._client = client

    async def _fetch_scope(
        self, scope_id: str, is_community: bool = False,
    ) -> List[Dict[str, Any]]:
        """Fetch connectors for a single scope (workspace or community)."""
        variables = {
            "input": {
                "clientId": scope_id,
                "first": 500,
                "connectorId": scope_id,
                "query": '{"input":{"limit":500,"offset":0,"sort":"asc","query":"","filter":{}}}',
                "isCommunity": is_community,
                "offset": 0,
            }
        }
        data = await _gql_call_async(
            self._client, SEARCH_CONNECTORS_QUERY, variables,
            extra_headers={"x-fastn-space-id": scope_id},
        )
        search_result = data.get("searchDataSourceGroups") or {}
        edges = search_result.get("edges") or []
        results: List[Dict[str, Any]] = []
        for edge in edges:
            node = edge.get("node", {})
            name = node.get("name", "")
            results.append({
                "name": name.lower().replace(" ", "_").replace("-", "_"),
                "display_name": name,
                "id": node.get("id", ""),
            })
        return results

    async def list(self) -> List[Dict[str, Any]]:
        """List all connectors: workspace + community catalog (async).

        Fetches from two sources (matching the CLI ``fastn sync`` pattern):
        1. Workspace — connectors configured in the user's project
        2. Community — the full 200+ public connector catalog

        Workspace connectors take priority over community duplicates.
        """
        self._client._ensure_fresh_token()
        project_id = self._client._config.resolve_project_id()

        # 1. Workspace connectors
        workspace = await self._fetch_scope(project_id)

        # 2. Community connectors
        try:
            community = await self._fetch_scope("community", is_community=True)
        except Exception:
            community = []

        # Merge: workspace takes priority
        seen = {c["name"] for c in workspace}
        merged = list(workspace)
        for c in community:
            if c["name"] not in seen:
                merged.append(c)
                seen.add(c["name"])

        return merged
