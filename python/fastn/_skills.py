"""Skills namespace — list agent skills in the project."""

from __future__ import annotations

from typing import Any, Dict, List

from fastn._constants import LIST_SKILLS_QUERY
from fastn._http import _gql_call_async, _gql_call_sync


class _SkillsSync:
    """Skills namespace (sync): ``fastn.skills.*``

    List agent skills configured in the current project.

    Usage::

        fastn = FastnClient(api_key="...", project_id="...")
        skills = fastn.skills.list()
        # [{"id": "sk_abc", "name": "My Skill", "description": "..."}, ...]
    """

    def __init__(self, client: Any) -> None:
        self._client = client

    def list(self) -> List[Dict[str, Any]]:
        """List all agent skills in the current project.

        Returns a list of dicts with ``id``, ``projectId``, ``name``,
        ``description``, ``createdAt``, ``updatedAt``.
        """
        self._client._ensure_fresh_token()
        project_id = self._client._config.resolve_project_id()
        variables = {"input": {"projectId": project_id}}
        data = _gql_call_sync(self._client, LIST_SKILLS_QUERY, variables)
        return data.get("listUCLAgents") or []


class _SkillsAsync:
    """Skills namespace (async): ``fastn.skills.*``

    Async equivalent of :class:`_SkillsSync`. See its docstring for full
    method documentation.
    """

    def __init__(self, client: Any) -> None:
        self._client = client

    async def list(self) -> List[Dict[str, Any]]:
        """List all agent skills in the current project (async)."""
        self._client._ensure_fresh_token()
        project_id = self._client._config.resolve_project_id()
        variables = {"input": {"projectId": project_id}}
        data = await _gql_call_async(self._client, LIST_SKILLS_QUERY, variables)
        return data.get("listUCLAgents") or []
