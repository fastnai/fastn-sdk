"""Flow management namespace — create, run, list, update, delete flows."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Optional

from fastn._constants import CALL_CORE_PROJECT_FLOW_QUERY, FLOWS_API_URL
from fastn._http import _api_call_sync, _api_call_async, _gql_call_sync, _gql_call_async


def _build_flows_query_variables(client: Any) -> Dict[str, Any]:
    """Build the GraphQL variables for fetching flows."""
    workspace_id = client._config.resolve_project_id()
    connector_id = workspace_id
    return {
        "input": {
            "operationName": "getConnectorRegisteredTools_v1",
            "input": {
                "connectorId": connector_id,
                "orgId": workspace_id,
                "workspaceId": workspace_id,
                "gatewayId": workspace_id,
            },
        }
    }


def _parse_flows_response(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Parse the callCoreProjectFlow response into a list of flow dicts."""
    result = data.get("callCoreProjectFlow") or {}
    items = result.get("data") or []

    if isinstance(items, str):
        try:
            items = json.loads(items)
        except (json.JSONDecodeError, TypeError):
            items = []

    _FLOW_KEYS = {"id", "name", "description", "inputSchema", "outputSchema"}
    flows = []
    for item in items:
        if not isinstance(item, dict):
            continue
        flow: Dict[str, Any] = {
            "flow_id": item.get("id", ""),
            "name": item.get("name", ""),
            "description": item.get("description", ""),
            "inputSchema": item.get("inputSchema", {}),
            "outputSchema": item.get("outputSchema", {}),
        }
        # Pass through any extra fields (e.g. status) from the API
        for key, val in item.items():
            if key not in _FLOW_KEYS:
                flow[key] = val
        flows.append(flow)

    return flows


def _fetch_flows_sync(client: Any) -> List[Dict[str, Any]]:
    """Fetch all flows from the workspace using the GraphQL API (sync)."""
    variables = _build_flows_query_variables(client)
    data = _gql_call_sync(client, CALL_CORE_PROJECT_FLOW_QUERY, variables)
    return _parse_flows_response(data)


async def _fetch_flows_async(client: Any) -> List[Dict[str, Any]]:
    """Fetch all flows from the workspace using the GraphQL API (async)."""
    variables = _build_flows_query_variables(client)
    data = await _gql_call_async(client, CALL_CORE_PROJECT_FLOW_QUERY, variables)
    return _parse_flows_response(data)


class _FlowsSync:
    """Flow management namespace (sync): ``fastn.flows.*``

    Provides operations for Fastn integration flows. Flows are managed
    through the GraphQL API (callCoreProjectFlow proxy).

    Usage::

        fastn = FastnClient(api_key="...", project_id="...")

        # List all flows
        flows = fastn.flows.list()

        # Trigger a flow run
        run = fastn.flows.run(flow_id="flow_abc")

        # Check run status
        status = fastn.flows.get_run(run_id="run_xyz")
    """

    def __init__(self, client: Any) -> None:
        self._client = client

    def create(
        self,
        prompt: str,
        answers: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Create an integration flow from a plain-English prompt.

        Fastn generates the full flow definition internally — you do not need
        to know connector schemas or step syntax.

        If the flow requires more information, a ``questions`` list is returned.
        Collect the answers and call ``create()`` again with the ``answers``
        parameter populated.

        Args:
            prompt: Plain English description of the integration to create.
            answers: Key-value pairs answering questions from a previous call.

        Returns:
            A dict containing at minimum ``flow_id`` on success, or
            ``questions`` if more info is needed.
        """
        payload: Dict[str, Any] = {"prompt": prompt}
        if answers:
            payload["answers"] = answers
        return _api_call_sync(self._client, "POST", f"{FLOWS_API_URL}/create", payload)

    def delete(self, flow_id: str) -> Dict[str, Any]:
        """Delete a flow.

        Args:
            flow_id: The ID of the flow to delete.

        Returns:
            Confirmation dict.

        Raises:
            FlowNotFoundError: If the flow_id does not exist.
        """
        return _api_call_sync(
            self._client, "POST", f"{FLOWS_API_URL}/delete", {"flow_id": flow_id}
        )

    def run(
        self,
        flow_id: str,
        user_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Trigger a flow run.

        Args:
            flow_id: The ID of the flow to run.
            user_id: Optional end-user ID for multi-tenant flows.

        Returns:
            A dict containing ``run_id`` and initial ``status``.

        Raises:
            FlowNotFoundError: If the flow_id does not exist.
        """
        payload: Dict[str, Any] = {"flow_id": flow_id}
        if user_id:
            payload["user_id"] = user_id
        return _api_call_sync(self._client, "POST", f"{FLOWS_API_URL}/run", payload)

    def get_run(self, run_id: str) -> Dict[str, Any]:
        """Get the status of a flow run.

        Args:
            run_id: The ID of the run to check.

        Returns:
            A dict with ``run_id``, ``status``, ``steps``, ``started_at``,
            ``completed_at``, and ``result`` or ``error``.

        Raises:
            RunNotFoundError: If the run_id does not exist.
        """
        return _api_call_sync(
            self._client, "POST", f"{FLOWS_API_URL}/get_run", {"run_id": run_id}
        )

    def list(self, status: Optional[str] = None) -> List[Dict[str, Any]]:
        """List flows in the project.

        Fetches flows from the workspace via the GraphQL API using the
        same mechanism as ``fastn list flows``.

        Args:
            status: Optional filter — ``"active"``, ``"paused"``, ``"draft"``,
                or ``None`` for all.

        Returns:
            A list of flow summary dicts with ``flow_id``, ``name``,
            ``description``, ``inputSchema``, and ``outputSchema``.
        """
        flows = _fetch_flows_sync(self._client)

        # Client-side status filter (if the API ever provides status info)
        if status:
            flows = [f for f in flows if f.get("status") == status]

        return flows

    def update(
        self,
        flow_id: str,
        prompt: Optional[str] = None,
        schedule: Optional[str] = None,
        enabled: Optional[bool] = None,
        answers: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Update an existing flow.

        Args:
            flow_id: The ID of the flow to update.
            prompt: New prompt to regenerate the flow definition.
            schedule: New cron schedule (e.g. ``"0 9 * * MON-FRI"``).
            enabled: Enable or disable the flow.
            answers: Answers to questions from a regeneration.

        Returns:
            Updated flow dict.

        Raises:
            FlowNotFoundError: If the flow_id does not exist.
        """
        payload: Dict[str, Any] = {"flow_id": flow_id}
        if prompt is not None:
            payload["prompt"] = prompt
        if schedule is not None:
            payload["schedule"] = schedule
        if enabled is not None:
            payload["enabled"] = enabled
        if answers is not None:
            payload["answers"] = answers
        return _api_call_sync(
            self._client, "POST", f"{FLOWS_API_URL}/update", payload
        )


class _FlowsAsync:
    """Flow management namespace (async): ``fastn.flows.*``

    Async equivalent of :class:`_FlowsSync`. See its docstring for full
    method documentation.
    """

    def __init__(self, client: Any) -> None:
        self._client = client

    async def create(
        self,
        prompt: str,
        answers: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Create an integration flow from a plain-English prompt (async)."""
        payload: Dict[str, Any] = {"prompt": prompt}
        if answers:
            payload["answers"] = answers
        return await _api_call_async(
            self._client, "POST", f"{FLOWS_API_URL}/create", payload
        )

    async def delete(self, flow_id: str) -> Dict[str, Any]:
        """Delete a flow (async)."""
        return await _api_call_async(
            self._client, "POST", f"{FLOWS_API_URL}/delete", {"flow_id": flow_id}
        )

    async def run(
        self,
        flow_id: str,
        user_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Trigger a flow run (async)."""
        payload: Dict[str, Any] = {"flow_id": flow_id}
        if user_id:
            payload["user_id"] = user_id
        return await _api_call_async(
            self._client, "POST", f"{FLOWS_API_URL}/run", payload
        )

    async def get_run(self, run_id: str) -> Dict[str, Any]:
        """Get the status of a flow run (async)."""
        return await _api_call_async(
            self._client, "POST", f"{FLOWS_API_URL}/get_run", {"run_id": run_id}
        )

    async def list(self, status: Optional[str] = None) -> List[Dict[str, Any]]:
        """List flows in the project (async).

        Fetches flows from the workspace via the GraphQL API using the
        same mechanism as ``fastn list flows``.
        """
        flows = await _fetch_flows_async(self._client)

        # Client-side status filter (if the API ever provides status info)
        if status:
            flows = [f for f in flows if f.get("status") == status]

        return flows

    async def update(
        self,
        flow_id: str,
        prompt: Optional[str] = None,
        schedule: Optional[str] = None,
        enabled: Optional[bool] = None,
        answers: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Update an existing flow (async)."""
        payload: Dict[str, Any] = {"flow_id": flow_id}
        if prompt is not None:
            payload["prompt"] = prompt
        if schedule is not None:
            payload["schedule"] = schedule
        if enabled is not None:
            payload["enabled"] = enabled
        if answers is not None:
            payload["answers"] = answers
        return await _api_call_async(
            self._client, "POST", f"{FLOWS_API_URL}/update", payload
        )
