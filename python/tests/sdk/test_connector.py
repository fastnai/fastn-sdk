"""Tests for dynamic connector proxy."""

from __future__ import annotations

import pytest

from fastn.connector import AsyncDynamicConnector, DynamicConnector
from fastn.exceptions import ToolNotFoundError


def _make_tools(*names):
    """Helper to create tools dict in the format DynamicConnector expects."""
    return {
        name: {"actionId": f"act_{name}", "inputSchema": {}}
        for name in names
    }


class TestDynamicConnector:
    def test_tool_call(self) -> None:
        called_with = {}

        def mock_execute(action_id, params, connector_id="", action_info=None,
                         connection_id=None, tenant_id=None):
            called_with["action_id"] = action_id
            called_with["params"] = params
            called_with["connection_id"] = connection_id
            return {"ok": True}

        connector = DynamicConnector(
            connector_name="slack",
            tools=_make_tools("send_message"),
            execute_fn=mock_execute,
        )

        result = connector.send_message(channel="general", text="Hello")
        assert result == {"ok": True}
        assert called_with["action_id"] == "act_send_message"
        assert called_with["params"] == {"channel": "general", "text": "Hello"}
        assert called_with["connection_id"] is None

    def test_tool_not_found(self) -> None:
        connector = DynamicConnector(
            connector_name="slack",
            tools=_make_tools("send_message"),
            execute_fn=lambda *a, **kw: None,
        )

        with pytest.raises(ToolNotFoundError, match="nonexistent"):
            connector.nonexistent()

    def test_tool_not_found_empty_connector(self) -> None:
        """When connector has no tools (not yet added), suggest `fastn add`."""
        connector = DynamicConnector(
            connector_name="slack",
            tools={},
            execute_fn=lambda *a, **kw: None,
        )

        with pytest.raises(ToolNotFoundError, match="fastn add slack"):
            connector.send_message(channel="general")

    def test_underscore_fallback(self) -> None:
        """send_message should match 'sendmessage' in the registry."""
        called_with = {}

        def mock_execute(action_id, params, connector_id="", action_info=None,
                         connection_id=None, tenant_id=None):
            called_with["action_id"] = action_id
            called_with["params"] = params
            return {"ok": True}

        connector = DynamicConnector(
            connector_name="slack",
            tools={"sendmessage": {"actionId": "act_sendmessage", "inputSchema": {}}},
            execute_fn=mock_execute,
        )

        result = connector.send_message(channel="general", text="Hi")
        assert result == {"ok": True}
        assert called_with["action_id"] == "act_sendmessage"

    def test_private_attr(self) -> None:
        connector = DynamicConnector(
            connector_name="slack",
            tools={},
            execute_fn=lambda *a, **kw: None,
        )

        with pytest.raises(AttributeError):
            _ = connector._private

    def test_repr(self) -> None:
        connector = DynamicConnector(
            connector_name="slack",
            tools=_make_tools("a", "b"),
            execute_fn=lambda *a, **kw: None,
        )
        assert "slack" in repr(connector)
        assert "2 tools" in repr(connector)

    def test_dir(self) -> None:
        connector = DynamicConnector(
            connector_name="slack",
            tools=_make_tools("send_message", "create_channel"),
            execute_fn=lambda *a, **kw: None,
        )
        entries = dir(connector)
        assert "send_message" in entries
        assert "create_channel" in entries

    def test_tool_call_with_bound_connection_id(self) -> None:
        called_with = {}

        def mock_execute(action_id, params, connector_id="", action_info=None,
                         connection_id=None, tenant_id=None):
            called_with["connection_id"] = connection_id
            return {"ok": True}

        connector = DynamicConnector(
            connector_name="slack",
            tools=_make_tools("send_message"),
            execute_fn=mock_execute,
            connection_id="conn_abc",
        )

        connector.send_message(channel="general", text="Hello")
        assert called_with["connection_id"] == "conn_abc"

    def test_tool_call_per_call_connection_id_override(self) -> None:
        called_with = {}

        def mock_execute(action_id, params, connector_id="", action_info=None,
                         connection_id=None, tenant_id=None):
            called_with["connection_id"] = connection_id
            called_with["params"] = params
            return {"ok": True}

        connector = DynamicConnector(
            connector_name="slack",
            tools=_make_tools("send_message"),
            execute_fn=mock_execute,
            connection_id="conn_default",
        )

        connector.send_message(connection_id="conn_override", channel="general")
        assert called_with["connection_id"] == "conn_override"
        # connection_id should be popped from params
        assert "connection_id" not in called_with["params"]

    def test_repr_with_connection(self) -> None:
        connector = DynamicConnector(
            connector_name="slack",
            tools=_make_tools("a"),
            execute_fn=lambda *a, **kw: None,
            connection_id="conn_123",
        )
        r = repr(connector)
        assert "conn_123" in r


class TestAsyncDynamicConnector:
    @pytest.mark.asyncio
    async def test_async_tool_call(self) -> None:
        called_with = {}

        async def mock_execute(action_id, params, connector_id="", action_info=None,
                               connection_id=None, tenant_id=None):
            called_with["action_id"] = action_id
            called_with["params"] = params
            called_with["connection_id"] = connection_id
            return {"ok": True}

        connector = AsyncDynamicConnector(
            connector_name="slack",
            tools=_make_tools("send_message"),
            execute_fn=mock_execute,
        )

        result = await connector.send_message(channel="general", text="Hello")
        assert result == {"ok": True}
        assert called_with["action_id"] == "act_send_message"
        assert called_with["connection_id"] is None

    @pytest.mark.asyncio
    async def test_async_tool_call_with_connection_id(self) -> None:
        called_with = {}

        async def mock_execute(action_id, params, connector_id="", action_info=None,
                               connection_id=None, tenant_id=None):
            called_with["connection_id"] = connection_id
            return {"ok": True}

        connector = AsyncDynamicConnector(
            connector_name="slack",
            tools=_make_tools("send_message"),
            execute_fn=mock_execute,
            connection_id="conn_async",
        )

        await connector.send_message(channel="general")
        assert called_with["connection_id"] == "conn_async"

    @pytest.mark.asyncio
    async def test_async_tool_not_found(self) -> None:
        async def mock_execute(action_id, params, connector_id="", action_info=None,
                               connection_id=None, tenant_id=None):
            return {}

        connector = AsyncDynamicConnector(
            connector_name="slack",
            tools={},
            execute_fn=mock_execute,
        )

        with pytest.raises(ToolNotFoundError):
            await connector.nonexistent()
