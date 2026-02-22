"""Tests for exception classes."""

from __future__ import annotations

from fastn.exceptions import (
    APIError,
    AuthError,
    ConfigError,
    ConnectionNotFoundError,
    ConnectorNotFoundError,
    ToolNotFoundError,
    FastnError,
    RegistryError,
)


class TestExceptions:
    def test_fastn_error(self) -> None:
        err = FastnError("test error", details={"key": "val"})
        assert str(err) == "test error"
        assert err.message == "test error"
        assert err.details == {"key": "val"}

    def test_auth_error(self) -> None:
        err = AuthError("bad auth")
        assert isinstance(err, FastnError)
        assert "bad auth" in str(err)

    def test_config_error(self) -> None:
        err = ConfigError("missing field")
        assert isinstance(err, FastnError)

    def test_connector_not_found(self) -> None:
        err = ConnectorNotFoundError("slack")
        assert "slack" in str(err)
        assert err.connector_name == "slack"
        assert "fastn sync" in str(err)
        assert "fastn add slack" in str(err)

    def test_tool_not_found(self) -> None:
        err = ToolNotFoundError("slack", "send_message")
        assert "send_message" in str(err)
        assert "slack" in str(err)
        assert err.connector_name == "slack"
        assert err.tool_name == "send_message"

    def test_tool_not_found_no_tools_installed(self) -> None:
        err = ToolNotFoundError("slack", "send_message", has_tools=False)
        assert "fastn add slack" in str(err)
        assert "no tools installed" in str(err).lower()
        assert err.connector_name == "slack"
        assert err.tool_name == "send_message"

    def test_connection_not_found_default(self) -> None:
        err = ConnectionNotFoundError()
        assert "connection_id" in str(err)
        assert isinstance(err, FastnError)

    def test_connection_not_found_custom(self) -> None:
        err = ConnectionNotFoundError("Custom message")
        assert str(err) == "Custom message"

    def test_api_error(self) -> None:
        err = APIError("server error", status_code=500, response_body={"error": "oops"})
        assert err.status_code == 500
        assert err.response_body == {"error": "oops"}
        assert isinstance(err, FastnError)

    def test_registry_error(self) -> None:
        err = RegistryError("sync failed")
        assert isinstance(err, FastnError)
