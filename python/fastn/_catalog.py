"""Connector catalog — control plane for listing and inspecting connectors."""

from __future__ import annotations

from typing import Any, Dict, List

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
