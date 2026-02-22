"""Projects namespace — list available projects."""

from __future__ import annotations

from typing import Any, Dict, List

from fastn._constants import GET_ORGANIZATIONS_QUERY
from fastn._http import _gql_call_sync, _gql_call_async
from fastn.exceptions import AuthError


class _ProjectsSync:
    """Projects namespace (sync): ``fastn.projects.*``

    List available projects for the authenticated user.

    Usage::

        fastn = FastnClient(auth_token="...")
        projects = fastn.projects.list()
        # [{"id": "abc", "name": "My Project", "packageType": "free"}, ...]
    """

    def __init__(self, client: Any) -> None:
        self._client = client

    def list(self) -> List[Dict[str, Any]]:
        """List all projects available to the authenticated user.

        Returns a list of dicts with ``id``, ``name``, ``packageType``.
        The ``id`` is the projectId to use in subsequent API calls.
        """
        from fastn.oauth import _decode_jwt_payload

        self._client._ensure_fresh_token()
        token = self._client._config.auth_token
        if not token:
            raise AuthError("No auth token available.")

        payload = _decode_jwt_payload(token)
        user_id = payload.get("sub", "")
        if not user_id:
            raise AuthError("Token does not contain a user ID.")

        variables = {"userId": user_id}
        data = _gql_call_sync(self._client, GET_ORGANIZATIONS_QUERY, variables)
        return data.get("getOrganizations") or []


class _ProjectsAsync:
    """Projects namespace (async): ``fastn.projects.*``

    Async equivalent of :class:`_ProjectsSync`. See its docstring for full
    method documentation.
    """

    def __init__(self, client: Any) -> None:
        self._client = client

    async def list(self) -> List[Dict[str, Any]]:
        """List all projects available to the authenticated user (async)."""
        from fastn.oauth import _decode_jwt_payload

        self._client._ensure_fresh_token()
        token = self._client._config.auth_token
        if not token:
            raise AuthError("No auth token available.")

        payload = _decode_jwt_payload(token)
        user_id = payload.get("sub", "")
        if not user_id:
            raise AuthError("Token does not contain a user ID.")

        variables = {"userId": user_id}
        data = await _gql_call_async(self._client, GET_ORGANIZATIONS_QUERY, variables)
        return data.get("getOrganizations") or []
