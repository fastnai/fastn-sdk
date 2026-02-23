"""Fastn SDK exceptions.

All exceptions inherit from ``FastnError``. Import from the top-level package:

    from fastn import FastnClient, AuthError, ConnectorNotFoundError

Exception hierarchy:
    FastnError                      Base class. Has .message and .details attrs.
    +-- AuthError                   Invalid/expired credentials (API key or JWT).
    |   +-- OAuthError              OAuth device flow failure. Has .error_code attr.
    +-- ConfigError                 Missing api_key/project_id. Run ``fastn login``.
    +-- ConnectorNotFoundError      Connector not in registry. Has .connector_name.
    +-- ToolNotFoundError           Tool not found in connector. Has .connector_name, .tool_name.
    +-- ConnectionNotFoundError     Multiple connections, none specified.
    +-- FlowNotFoundError           Flow not found. Has .flow_id attr.
    +-- RunNotFoundError            Run not found. Has .run_id attr.
    +-- APIError                    HTTP error from the API. Has .status_code, .response_body.
    +-- RegistryError               Registry sync/parse failure.

Usage:
    try:
        fastn.slack.send_message(channel="general", text="Hi")
    except AuthError:
        print("Check credentials")
    except ConnectorNotFoundError as e:
        print(f"Run: fastn connector sync && fastn connector add {e.connector_name}")
    except APIError as e:
        print(f"HTTP {e.status_code}: {e}")
"""

from __future__ import annotations

from typing import Any, Dict, Optional


class FastnError(Exception):
    """Base exception for all Fastn SDK errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}


class AuthError(FastnError):
    """Raised when authentication fails (invalid API key, missing headers)."""

    pass


class ConfigError(FastnError):
    """Raised when configuration is missing or invalid."""

    pass


class ConnectorNotFoundError(FastnError):
    """Raised when a connector (e.g. Slack, Jira) is not in the registry."""

    def __init__(self, connector_name: str) -> None:
        super().__init__(
            f"Connector '{connector_name}' not found in local registry. "
            f"Run `fastn connector sync` to update the registry, "
            f"then `fastn connector add {connector_name}` to install it."
        )
        self.connector_name = connector_name


class ToolNotFoundError(FastnError):
    """Raised when a tool (e.g. send_message) is not found in a connector's definition."""

    def __init__(
        self, connector_name: str, tool_name: str, has_tools: bool = True,
    ) -> None:
        if has_tools:
            msg = (
                f"Tool '{tool_name}' not found in connector '{connector_name}'. "
                f"Run `fastn connector sync` to update the registry, or check the tool name."
            )
        else:
            msg = (
                f"Connector '{connector_name}' has no tools installed. "
                f"Run `fastn connector add {connector_name}` to fetch its tools."
            )
        super().__init__(msg)
        self.connector_name = connector_name
        self.tool_name = tool_name


class ConnectionNotFoundError(FastnError):
    """Raised when a connection_id is required but not found or not provided."""

    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(
            message
            or "Multiple connections found. Pass connection_id to specify which one to use."
        )


class APIError(FastnError):
    """Raised when the Fastn API returns an error response."""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        response_body: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, details=response_body)
        self.status_code = status_code
        self.response_body = response_body


class OAuthError(AuthError):
    """Raised when the OAuth device authorization flow fails."""

    def __init__(self, message: str, error_code: Optional[str] = None) -> None:
        super().__init__(message)
        self.error_code = error_code


class FlowNotFoundError(FastnError):
    """Raised when a flow_id does not exist or does not belong to this project."""

    def __init__(self, flow_id: str) -> None:
        super().__init__(
            f"Flow '{flow_id}' not found or does not belong to this project."
        )
        self.flow_id = flow_id


class RunNotFoundError(FastnError):
    """Raised when a run_id does not exist or does not belong to this project."""

    def __init__(self, run_id: str) -> None:
        super().__init__(
            f"Run '{run_id}' not found or does not belong to this project."
        )
        self.run_id = run_id


class RegistryError(FastnError):
    """Raised when there's an issue with the registry (sync, fetch, parse)."""

    pass
