"""Flow management namespace — create, run, list, update, delete flows."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from fastn._constants import FLOWS_API_URL, LIST_FLOWS_QUERY
from fastn._http import _api_call_sync, _api_call_async, _gql_call_sync, _gql_call_async
from fastn.exceptions import FlowNotFoundError


def _build_flows_query_variables(client: Any) -> Dict[str, Any]:
    """Build the GraphQL variables for the ``apis`` query."""
    workspace_id = client._config.resolve_project_id()
    return {
        "input": {
            "clientId": workspace_id,
            "first": 500,
            "after": None,
            "query": '{"input":{"limit":500,"offset":0,"sort":"desc","query":"","filter":{}}}',
        }
    }


def _parse_flows_response(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Parse the ``apis`` GraphQL response into a list of flow dicts."""
    result = data.get("apis") or {}
    edges = result.get("edges") or []

    flows: List[Dict[str, Any]] = []
    for edge in edges:
        if not isinstance(edge, dict):
            continue
        node = edge.get("node") or {}
        if not isinstance(node, dict):
            continue

        flow: Dict[str, Any] = {
            "flow_id": node.get("id", ""),
            "name": node.get("name", ""),
            "description": node.get("description", ""),
            "status": node.get("status", ""),
            "version": node.get("version", ""),
            "updatedAt": node.get("updatedAt", ""),
            "deployedAt": node.get("deployedAt", ""),
        }

        meta = node.get("metaData") or {}
        if meta:
            flow["flowType"] = meta.get("flowType", "")
            flow["architecture"] = meta.get("architecture", "")
            flow["isAsync"] = meta.get("isAsync", False)

        flows.append(flow)

    return flows


def _fetch_flows_sync(client: Any) -> List[Dict[str, Any]]:
    """Fetch all flows from the workspace using the ``apis`` GraphQL query (sync)."""
    variables = _build_flows_query_variables(client)
    data = _gql_call_sync(client, LIST_FLOWS_QUERY, variables)
    return _parse_flows_response(data)


async def _fetch_flows_async(client: Any) -> List[Dict[str, Any]]:
    """Fetch all flows from the workspace using the ``apis`` GraphQL query (async)."""
    variables = _build_flows_query_variables(client)
    data = await _gql_call_async(client, LIST_FLOWS_QUERY, variables)
    return _parse_flows_response(data)


# ---------------------------------------------------------------------------
# Name → ID resolution helpers
# ---------------------------------------------------------------------------

def _resolve_flow_id_sync(client: Any, name_or_id: str) -> str:
    """Resolve a flow name to its base flow_id by listing flows.

    Raises FlowNotFoundError if no match is found.
    """
    flows = _fetch_flows_sync(client)
    for flow in flows:
        if flow.get("name") == name_or_id:
            return flow["flow_id"]
    raise FlowNotFoundError(name_or_id)


async def _resolve_flow_id_async(client: Any, name_or_id: str) -> str:
    """Resolve a flow name to its base flow_id by listing flows (async).

    Raises FlowNotFoundError if no match is found.
    """
    flows = await _fetch_flows_async(client)
    for flow in flows:
        if flow.get("name") == name_or_id:
            return flow["flow_id"]
    raise FlowNotFoundError(name_or_id)


class _FlowsSync:
    """Flow management namespace (sync): ``fastn.flows.*``

    Provides operations for Fastn integration flows.

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

        Accepts either the base flow ID (e.g. ``"testflow"``) or a versioned
        name (e.g. ``"testflow_v1"``).  If the given identifier is not found
        directly, the method lists all flows and resolves the name to the
        correct base flow ID before retrying.

        Args:
            flow_id: The base flow ID or versioned flow name.

        Returns:
            Confirmation dict.

        Raises:
            FlowNotFoundError: If the flow cannot be found by ID or name.
        """
        try:
            return _api_call_sync(
                self._client, "POST", f"{FLOWS_API_URL}/delete", {"flow_id": flow_id}
            )
        except FlowNotFoundError:
            # The given string may be a versioned name — resolve to base ID.
            resolved_id = _resolve_flow_id_sync(self._client, flow_id)
            return _api_call_sync(
                self._client, "POST", f"{FLOWS_API_URL}/delete", {"flow_id": resolved_id}
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

        Fetches flows from the workspace via the ``apis`` GraphQL query.

        Args:
            status: Optional filter — ``"active"``, ``"paused"``, ``"draft"``,
                or ``None`` for all.

        Returns:
            A list of flow summary dicts with ``flow_id``, ``name``,
            ``description``, ``status``, ``version``, ``updatedAt``,
            and ``deployedAt``.
        """
        flows = _fetch_flows_sync(self._client)

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
        """Delete a flow (async).

        Accepts either the base flow ID or a versioned name.  Resolves
        automatically if the initial ID is not found.
        """
        try:
            return await _api_call_async(
                self._client, "POST", f"{FLOWS_API_URL}/delete", {"flow_id": flow_id}
            )
        except FlowNotFoundError:
            resolved_id = await _resolve_flow_id_async(self._client, flow_id)
            return await _api_call_async(
                self._client, "POST", f"{FLOWS_API_URL}/delete", {"flow_id": resolved_id}
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

        Fetches flows from the workspace via the ``apis`` GraphQL query.
        """
        flows = await _fetch_flows_async(self._client)

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
