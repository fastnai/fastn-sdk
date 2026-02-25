"""Connect Kit namespace — manage connectors and configurations for the project."""

from __future__ import annotations

from typing import Any, Dict, List

from fastn._constants import (
    GET_CONNECTOR_QUERY,
    GET_KIT_CONNECTORS_QUERY,
    GET_KIT_METADATA_QUERY,
    SAVE_KIT_METADATA_MUTATION,
)
from fastn._http import _gql_call_async, _gql_call_sync


class _KitSync:
    """Connect Kit namespace (sync): ``fastn.kit.*``

    Manage Connect Kit connectors and configuration for the current project.

    Usage::

        fastn = FastnClient(api_key="...", project_id="...")
        metadata = fastn.kit.get()
        # {"authenticationApi": "...", "isRBACEnabled": True, ...}
    """

    def __init__(self, client: Any) -> None:
        self._client = client

    def get(self) -> Dict[str, Any]:
        """Get kit metadata for the current project.

        Returns a dict with kit configuration fields such as
        ``authenticationApi``, ``isCustomAuthenticationEnabled``,
        ``filterWidgets``, ``showFilterBar``, ``showLabels``,
        ``isRBACEnabled``, ``styles``, ``disableFor``,
        ``isAIAgentWidgetEnabled``, ``labelsLayout``,
        ``advancedSettings``, and ``widgetsMetrics``.
        """
        self._client._ensure_fresh_token()
        project_id = self._client._config.resolve_project_id()
        variables = {
            "input": {
                "id": project_id,
                "clientId": project_id,
            }
        }
        data = _gql_call_sync(self._client, GET_KIT_METADATA_QUERY, variables)
        return data.get("widgetMetadata") or {}

    def update(self, settings: Dict[str, Any]) -> Dict[str, Any]:
        """Update kit metadata for the current project.

        Uses the ``saveWidgetMetadata`` GraphQL mutation.

        Args:
            settings: A dict of kit configuration fields to update.
                Supported keys include ``authenticationApi``,
                ``isCustomAuthenticationEnabled``, ``showFilterBar``,
                ``showLabels``, ``styles``, ``labelsLayout``,
                ``disableFor``, ``filterWidgets``, ``isRBACEnabled``,
                and ``advancedSettings``.

        Returns:
            The saved kit metadata (``authenticationApi``,
            ``isCustomAuthenticationEnabled``, ``advancedSettings``).
        """
        self._client._ensure_fresh_token()
        project_id = self._client._config.resolve_project_id()
        variables = {
            "input": {
                "projectId": project_id,
                **settings,
            }
        }
        data = _gql_call_sync(self._client, SAVE_KIT_METADATA_MUTATION, variables)
        return data.get("saveWidgetMetadata") or {}

    def list(self, query: str = "", limit: int = 8, offset: int = 0) -> List[Dict[str, Any]]:
        """List kit connectors for the current project.

        Args:
            query: Optional search query string.
            limit: Maximum number of results (default 8).
            offset: Pagination offset (default 0).

        Returns:
            A list of kit connector dicts with ``id``, ``name``,
            ``active``, ``connectionId``, ``widgetType``, ``labels``,
            ``imageUri``, etc.
        """
        self._client._ensure_fresh_token()
        project_id = self._client._config.resolve_project_id()
        import json as _json
        inner_query = _json.dumps({
            "input": {
                "limit": limit,
                "offset": offset,
                "sort": "desc",
                "query": query,
                "filter": {},
            }
        })
        variables = {
            "input": {
                "projectId": project_id,
                "first": limit,
                "after": None,
                "query": inner_query,
            }
        }
        data = _gql_call_sync(self._client, GET_KIT_CONNECTORS_QUERY, variables)
        edges = (data.get("widgetConnectors") or {}).get("edges") or []
        return [e["node"] for e in edges if "node" in e]

    def get_connector(self, connector_id: str) -> Dict[str, Any]:
        """Get full details for a specific kit connector.

        Args:
            connector_id: The connector ID (e.g. ``_knexa_66da971c-...``).

        Returns:
            A dict with the connector's full details including ``id``,
            ``name``, ``active``, ``deployed``, ``widgetType``,
            ``description``, ``actions``, ``events``,
            ``connectedConnectors``, ``externalFlows``, etc.
        """
        self._client._ensure_fresh_token()
        project_id = self._client._config.resolve_project_id()
        variables = {
            "input": {
                "projectId": project_id,
                "id": connector_id,
                "template": False,
            }
        }
        data = _gql_call_sync(self._client, GET_CONNECTOR_QUERY, variables)
        return data.get("connector") or {}


class _KitAsync:
    """Connect Kit namespace (async): ``fastn.kit.*``

    Async equivalent of :class:`_KitSync`. See its docstring for full
    method documentation.
    """

    def __init__(self, client: Any) -> None:
        self._client = client

    async def get(self) -> Dict[str, Any]:
        """Get kit metadata for the current project (async)."""
        self._client._ensure_fresh_token()
        project_id = self._client._config.resolve_project_id()
        variables = {
            "input": {
                "id": project_id,
                "clientId": project_id,
            }
        }
        data = await _gql_call_async(self._client, GET_KIT_METADATA_QUERY, variables)
        return data.get("widgetMetadata") or {}

    async def update(self, settings: Dict[str, Any]) -> Dict[str, Any]:
        """Update kit metadata for the current project (async)."""
        self._client._ensure_fresh_token()
        project_id = self._client._config.resolve_project_id()
        variables = {
            "input": {
                "projectId": project_id,
                **settings,
            }
        }
        data = await _gql_call_async(self._client, SAVE_KIT_METADATA_MUTATION, variables)
        return data.get("saveWidgetMetadata") or {}

    async def list(self, query: str = "", limit: int = 8, offset: int = 0) -> List[Dict[str, Any]]:
        """List kit connectors for the current project (async)."""
        self._client._ensure_fresh_token()
        project_id = self._client._config.resolve_project_id()
        import json as _json
        inner_query = _json.dumps({
            "input": {
                "limit": limit,
                "offset": offset,
                "sort": "desc",
                "query": query,
                "filter": {},
            }
        })
        variables = {
            "input": {
                "projectId": project_id,
                "first": limit,
                "after": None,
                "query": inner_query,
            }
        }
        data = await _gql_call_async(self._client, GET_KIT_CONNECTORS_QUERY, variables)
        edges = (data.get("widgetConnectors") or {}).get("edges") or []
        return [e["node"] for e in edges if "node" in e]

    async def get_connector(self, connector_id: str) -> Dict[str, Any]:
        """Get full details for a specific kit connector (async)."""
        self._client._ensure_fresh_token()
        project_id = self._client._config.resolve_project_id()
        variables = {
            "input": {
                "projectId": project_id,
                "id": connector_id,
                "template": False,
            }
        }
        data = await _gql_call_async(self._client, GET_CONNECTOR_QUERY, variables)
        return data.get("connector") or {}
