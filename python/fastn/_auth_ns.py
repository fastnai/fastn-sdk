"""Auth namespace — OAuth connection management and custom auth configuration."""

from __future__ import annotations

import json
from typing import Any, Dict, Optional

from fastn._constants import _UPDATE_RESOLVER_STEP_MUTATION, CONNECTIONS_API_URL
from fastn._http import _api_call_sync, _api_call_async, _gql_call_sync, _gql_call_async


def _build_custom_auth_step(client_id: str, userinfo_url: str) -> Dict[str, Any]:
    """Build the updateResolverStep mutation variables."""
    code_obj = {
        "actionType": "map",
        "target": {
            "auth": {
                "actionType": "map",
                "target": {
                    "bearerToken": {
                        "actionType": "map",
                        "target": "{{data.headers.authorization}}",
                        "targetType": "string",
                        "actions": [],
                        "enum": [],
                        "title": "",
                        "description": "",
                        "isRequred": False,
                        "default": "",
                        "autoEscape": "MANUAL",
                    }
                },
                "targetType": "object",
                "actions": [],
                "enum": [],
                "title": "",
                "description": "",
                "isRequred": False,
                "default": [],
            },
            "url": {
                "actionType": "map",
                "target": {
                    "baseUrl": {
                        "actionType": "map",
                        "target": userinfo_url,
                        "targetType": "string",
                        "actions": [],
                        "default": "",
                    }
                },
                "targetType": "object",
                "actions": [],
                "default": [],
            },
            "headers": {
                "path": "headers",
                "key": "headers",
                "position": ["headers"],
                "selected": True,
                "actionType": "map",
                "target": {},
                "targetType": "object",
                "actions": [],
                "enum": [],
                "title": "",
                "description": "",
                "isRequred": False,
                "default": [],
                "autoEscape": "MANUAL",
                "byUser": True,
            },
            "params": {
                "path": "params",
                "key": "params",
                "position": ["params"],
                "selected": True,
                "actionType": "map",
                "target": {},
                "targetType": "object",
                "actions": [],
                "enum": [],
                "title": "",
                "description": "",
                "isRequred": False,
                "default": [],
                "autoEscape": "MANUAL",
                "byUser": True,
            },
        },
        "targetType": "object",
        "actions": [],
        "default": [],
    }
    code_str = json.dumps(code_obj)
    output_schema = json.dumps({
        "type": "object",
        "title": "",
        "description": "",
        "properties": {
            "headers": {"type": "object"},
            "auth": {"type": "object", "properties": {"bearerToken": {"type": "string"}}},
            "params": {"type": "object"},
            "url": {"type": "object", "properties": {"baseUrl": {"type": "string"}}},
        },
    })
    return {
        "input": {
            "id": "fastnCustomAuth",
            "clientId": client_id,
            "expression": 0,
            "isDefault": False,
            "nodeId": "getUser",
            "parentIds": [],
            "newNodeId": "getUser",
            "step": {
                "id": "getUser",
                "type": "COMPOSITE",
                "next": "checkIfUserExists",
                "composite": {
                    "next": "checkIfUserExists",
                    "steps": [
                        {
                            "type": "INLINE",
                            "id": "getUserMap",
                            "inline": {
                                "code": code_str,
                                "uiCode": code_str,
                                "language": "JINJA",
                                "next": "getUserApi",
                                "hasResponse": False,
                                "isError": False,
                                "statusCode": 200,
                                "outputSchema": output_schema,
                            },
                            "enableDebug": False,
                            "debugBreakAfter": 1,
                        },
                        {
                            "id": "getUserApi",
                            "type": "FUNCTION",
                            "next": None,
                            "function": {
                                "id": "_knexa_2oJHX7z7aZS6i18TWhnnflZSPix",
                                "imageUrl": "https://w7.pngwing.com/pngs/343/50/png-transparent-authorization-computer-icons-grants-of-dalvey-angle-black-authorization.png",
                                "name": "getUser",
                                "version": "1.0.3",
                                "groupId": "_knexa_ba5af4e1-615d-4dfd-8478-d63e2d7dd49a",
                                "connectorId": "community",
                                "configuration": {
                                    "enableCache": False,
                                    "cacheTtlInSeconds": 0,
                                    "required": False,
                                    "validate": False,
                                    "enableRetry": False,
                                    "requestSetting": None,
                                    "enableAuth": False,
                                    "authType": "BEARER",
                                    "auth": {
                                        "identifier": None,
                                        "enableMultiConnection": None,
                                        "isWorkspaceIdentifier": None,
                                    },
                                    "retry": {
                                        "maxRetries": 1,
                                        "maxDelayMilliseconds": 1000,
                                        "enableConnectionErrors": False,
                                        "retryList": [
                                            {"delayMilliseconds": 50, "statusCode": 500, "body": None}
                                        ],
                                    },
                                },
                            },
                            "enableDebug": False,
                            "debugBreakAfter": 1,
                        },
                    ],
                },
                "settings": {
                    "failureBehavior": "FAILURE",
                    "errorMessage": "",
                    "stepNote": "",
                },
                "enableDebug": False,
                "debugBreakAfter": 1,
            },
        }
    }


def _configure_custom_auth_sync(client: Any, userinfo_url: str) -> Dict[str, Any]:
    """Execute the updateResolverStep GraphQL mutation (sync)."""
    client_id = client._config.resolve_project_id()
    variables = _build_custom_auth_step(client_id, userinfo_url)
    return _gql_call_sync(client, _UPDATE_RESOLVER_STEP_MUTATION, variables)


async def _configure_custom_auth_async(client: Any, userinfo_url: str) -> Dict[str, Any]:
    """Execute the updateResolverStep GraphQL mutation (async)."""
    client_id = client._config.resolve_project_id()
    variables = _build_custom_auth_step(client_id, userinfo_url)
    return await _gql_call_async(client, _UPDATE_RESOLVER_STEP_MUTATION, variables)


class _AuthSync:
    """Auth namespace (sync): fastn.auth.*

    Manage OAuth connections for connectors.

    Usage::

        fastn = FastnClient(api_key="...", project_id="...")

        # Initiate OAuth for a connector
        result = fastn.auth.connect(
            connector="slack",
            tenant_id="acme-corp",
            redirect_url="https://myapp.com/callback",
        )
        # result = {"connection_id": "...", "auth_url": "...", "status": "pending", "expires_in": 600}

        # Check connection status
        status = fastn.auth.status(connection_id="conn_abc")
    """

    def __init__(self, client: Any) -> None:
        self._client = client

    def connect(
        self,
        connector: str,
        tenant_id: str,
        redirect_url: str,
    ) -> Dict[str, Any]:
        """Start an OAuth connection flow for a connector.

        Returns an ``auth_url`` that the end user must visit to authorize.

        Args:
            connector: Connector name (e.g. ``"slack"``, ``"github"``).
            tenant_id: Tenant or user identifier in your system.
            redirect_url: URL to redirect to after authorization completes.

        Returns:
            A dict with ``connection_id``, ``auth_url``, ``status``,
            and ``expires_in``.
        """
        payload: Dict[str, Any] = {
            "connector": connector,
            "tenant_id": tenant_id,
            "redirect_url": redirect_url,
        }
        return _api_call_sync(
            self._client, "POST", f"{CONNECTIONS_API_URL}/initiate", payload
        )

    def status(
        self,
        connection_id: Optional[str] = None,
        connector: Optional[str] = None,
        tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Check the status of a connection.

        Pass either ``connection_id`` directly, or ``connector`` + ``tenant_id``
        to look up by connector and tenant.

        Args:
            connection_id: The connection ID to check.
            connector: Connector name to look up.
            tenant_id: Tenant ID to look up.

        Returns:
            A dict with ``connection_id``, ``connector``, ``status``,
            ``tenant_id``, and ``created_at``.
        """
        payload: Dict[str, Any] = {}
        if connection_id:
            payload["connection_id"] = connection_id
        if connector:
            payload["connector"] = connector
        if tenant_id:
            payload["tenant_id"] = tenant_id
        return _api_call_sync(
            self._client, "POST", f"{CONNECTIONS_API_URL}/status", payload
        )

    def configure_custom(self, userinfo_url: str) -> Dict[str, Any]:
        """Register a custom auth provider with Fastn.

        Configures Fastn to validate end-user tokens by calling your
        userinfo endpoint. Once configured, pass end-user tokens via
        the ``X-User-Token`` header and Fastn will verify them.

        Args:
            userinfo_url: Your OpenID Connect userinfo endpoint
                (e.g. ``"https://myapp.auth0.com/userinfo"``).

        Returns:
            Confirmation dict from the API.
        """
        return _configure_custom_auth_sync(self._client, userinfo_url)


class _AuthAsync:
    """Auth namespace (async): fastn.auth.*

    Async equivalent of :class:`_AuthSync`. See its docstring for full
    method documentation.
    """

    def __init__(self, client: Any) -> None:
        self._client = client

    async def connect(
        self,
        connector: str,
        tenant_id: str,
        redirect_url: str,
    ) -> Dict[str, Any]:
        """Start an OAuth connection flow for a connector (async)."""
        payload: Dict[str, Any] = {
            "connector": connector,
            "tenant_id": tenant_id,
            "redirect_url": redirect_url,
        }
        return await _api_call_async(
            self._client, "POST", f"{CONNECTIONS_API_URL}/initiate", payload
        )

    async def status(
        self,
        connection_id: Optional[str] = None,
        connector: Optional[str] = None,
        tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Check the status of a connection (async)."""
        payload: Dict[str, Any] = {}
        if connection_id:
            payload["connection_id"] = connection_id
        if connector:
            payload["connector"] = connector
        if tenant_id:
            payload["tenant_id"] = tenant_id
        return await _api_call_async(
            self._client, "POST", f"{CONNECTIONS_API_URL}/status", payload
        )

    async def configure_custom(self, userinfo_url: str) -> Dict[str, Any]:
        """Register a custom auth provider with Fastn (async).

        See ``_AuthSync.configure_custom()`` for full documentation.
        """
        return await _configure_custom_auth_async(self._client, userinfo_url)
