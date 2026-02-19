"""Tests for the Fastn SDK client."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest
import httpx
from pytest_httpx import HTTPXMock

from fastn.client import AsyncFastnClient, FastnClient
from fastn.exceptions import (
    APIError,
    AuthError,
    ConfigError,
    ConnectorNotFoundError,
    FastnError,
    ToolNotFoundError,
)


# ---------------------------------------------------------------------------
# Test fixtures
# ---------------------------------------------------------------------------

_SAMPLE_INPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "body": {
            "type": "object",
            "properties": {
                "channel": {
                    "type": "string",
                    "description": "The channel to send to",
                },
                "text": {
                    "type": "string",
                    "description": "Message text",
                },
            },
            "required": ["channel", "text"],
        }
    },
    "required": ["body"],
}

_SAMPLE_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"},
        "ts": {"type": "string"},
    },
}


def _create_test_env(tmpdir: str, with_schemas: bool = False) -> str:
    """Create a .fastn directory with config and registry for testing."""
    fastn_dir = Path(tmpdir) / ".fastn"
    fastn_dir.mkdir()

    config = {
        "api_key": "test-api-key",
        "project_id": "test-project-id",
        "stage": "LIVE",
    }
    (fastn_dir / "config.json").write_text(json.dumps(config))

    tools = {
        "send_message": {
            "actionId": "act_slack_send_message",
            "description": "Send a message to a channel",
        },
        "create_channel": {
            "actionId": "act_slack_create_channel",
            "description": "Create a new channel",
        },
    }
    if with_schemas:
        tools["send_message"]["inputSchema"] = _SAMPLE_INPUT_SCHEMA
        tools["send_message"]["outputSchema"] = _SAMPLE_OUTPUT_SCHEMA
        tools["create_channel"]["inputSchema"] = {
            "type": "object",
            "properties": {
                "body": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Channel name",
                        },
                    },
                    "required": ["name"],
                }
            },
        }

    registry = {
        "version": "2025.02.14",
        "connectors": {
            "slack": {
                "id": "conn_slack_001",
                "display_name": "Slack",
                "category": "communication",
                "tools": tools,
            }
        },
    }
    (fastn_dir / "registry.json").write_text(json.dumps(registry))

    return str(fastn_dir / "config.json")


# ---------------------------------------------------------------------------
# Sync client tests
# ---------------------------------------------------------------------------

class TestFastnClient:
    def test_init_from_explicit_config(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            assert repr(client).startswith("<FastnClient")

    def test_init_missing_config(self, monkeypatch) -> None:
        # Clear any real env vars that could provide credentials
        monkeypatch.delenv("FASTN_API_KEY", raising=False)
        monkeypatch.delenv("FASTN_PROJECT_ID", raising=False)
        monkeypatch.delenv("FASTN_AUTH_TOKEN", raising=False)
        with tempfile.TemporaryDirectory() as tmpdir:
            empty_path = str(Path(tmpdir) / ".fastn" / "config.json")
            with pytest.raises(ConfigError):
                FastnClient(api_key="", project_id="", config_path=empty_path)

    def test_init_with_stage(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path, stage="DEV")
            assert client._config.stage == "DEV"

    def test_init_stage_in_headers(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path, stage="STAGING")
            assert client._headers["stage"] == "STAGING"

    def test_init_default_stage_is_live(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            assert client._config.stage == "LIVE"

    def test_connector_access(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            slack = client.slack
            assert "send_message" in dir(slack)
            assert "create_channel" in dir(slack)

    def test_connector_not_found(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            with pytest.raises(ConnectorNotFoundError, match="nonexistent"):
                _ = client.nonexistent

    def test_execute_tool_success(self, httpx_mock: HTTPXMock) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path, max_retries=0)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/executeTool",
                method="POST",
                json={"ok": True, "message": "sent"},
            )

            result = client.slack.send_message(
                channel="general", text="Hello"
            )
            assert result["ok"] is True

            # Verify the request payload
            request = httpx_mock.get_request()
            assert request is not None
            body = json.loads(request.content)
            assert body["input"]["actionId"] == "act_slack_send_message"
            assert body["input"]["parameters"]["body"]["channel"] == "general"
            assert body["input"]["parameters"]["body"]["text"] == "Hello"

    def test_execute_tool_auth_error(self, httpx_mock: HTTPXMock) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path, max_retries=0)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/executeTool",
                method="POST",
                status_code=401,
            )

            with pytest.raises(AuthError):
                client.slack.send_message(channel="general", text="Hello")

    def test_execute_tool_api_error(self, httpx_mock: HTTPXMock) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path, max_retries=0)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/executeTool",
                method="POST",
                status_code=500,
                json={"error": "Internal server error"},
            )

            with pytest.raises(APIError, match="500"):
                client.slack.send_message(channel="general", text="Hello")

    def test_context_manager(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            with FastnClient(config_path=config_path) as client:
                assert repr(client).startswith("<FastnClient")

    def test_execute_tool_with_connection_id(self, httpx_mock: HTTPXMock) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path, max_retries=0)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/executeTool",
                method="POST",
                json={"ok": True},
            )

            result = client.slack.send_message(
                connection_id="conn_123", channel="general", text="Hello"
            )
            assert result["ok"] is True

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["input"]["connectionId"] == "conn_123"

    def test_connect_returns_bound_proxy(self, httpx_mock: HTTPXMock) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path, max_retries=0)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/executeTool",
                method="POST",
                json={"ok": True},
            )

            proxy = client.connect("conn_bound")
            result = proxy.send_message(channel="general", text="Hi")
            assert result["ok"] is True

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["input"]["connectionId"] == "conn_bound"

    def test_admin_connectors_list(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            connectors = client.admin.connectors.list()
            assert len(connectors) == 1
            assert connectors[0]["name"] == "slack"

    def test_admin_connectors_get(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            connector = client.admin.connectors.get("slack")
            assert connector["name"] == "slack"
            assert "send_message" in connector["tools"]

    def test_admin_connectors_get_not_found(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            with pytest.raises(ConnectorNotFoundError):
                client.admin.connectors.get("nonexistent")


# ---------------------------------------------------------------------------
# execute() tests
# ---------------------------------------------------------------------------

class TestExecute:
    def test_execute_by_action_id(self, httpx_mock: HTTPXMock) -> None:
        """execute() calls executeTool with the given action_id and params."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path, max_retries=0)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/executeTool",
                method="POST",
                json={"ok": True, "ts": "1234567890.123456"},
            )

            result = client.execute(
                "act_slack_send_message",
                {"channel": "general", "text": "Hello from LLM"},
            )
            assert result["ok"] is True

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["input"]["actionId"] == "act_slack_send_message"
            assert body["input"]["parameters"]["body"]["channel"] == "general"

    def test_execute_with_connection_id(self, httpx_mock: HTTPXMock) -> None:
        """execute() passes connection_id through to the API."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path, max_retries=0)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/executeTool",
                method="POST",
                json={"ok": True},
            )

            client.execute(
                "act_slack_send_message",
                {"channel": "general", "text": "Hi"},
                connection_id="conn_abc",
            )

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["input"]["connectionId"] == "conn_abc"

    def test_execute_auth_error(self, httpx_mock: HTTPXMock) -> None:
        """execute() raises AuthError on 401."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path, max_retries=0)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/executeTool",
                method="POST",
                status_code=401,
            )

            with pytest.raises(AuthError):
                client.execute("act_slack_send_message", {"channel": "general"})


# ---------------------------------------------------------------------------
# get_tools_for() tests
# ---------------------------------------------------------------------------

class TestGetToolsFor:
    def _make_client(self, tmpdir: str) -> FastnClient:
        config_path = _create_test_env(tmpdir, with_schemas=True)
        return FastnClient(config_path=config_path)

    def test_openai_format(self) -> None:
        """get_tools_for(format='openai') returns OpenAI function-calling format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack", format="openai")

            assert len(tools) == 2
            # Find send_message tool
            send = next(t for t in tools if t["function"]["name"] == "send_message")
            assert send["type"] == "function"
            assert "description" in send["function"]
            params = send["function"]["parameters"]
            # Should be unwrapped — channel and text directly, not under "body"
            assert "channel" in params.get("properties", {})
            assert "text" in params.get("properties", {})

    def test_anthropic_format(self) -> None:
        """get_tools_for(format='anthropic') returns Anthropic tool-use format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack", format="anthropic")

            assert len(tools) == 2
            send = next(t for t in tools if t["name"] == "send_message")
            assert "input_schema" in send
            assert "description" in send
            # Unwrapped
            assert "channel" in send["input_schema"].get("properties", {})

    def test_gemini_format(self) -> None:
        """get_tools_for(format='gemini') returns Google Gemini format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack", format="gemini")

            assert len(tools) == 2
            send = next(t for t in tools if t["name"] == "send_message")
            assert "parameters" in send
            assert "description" in send
            assert "channel" in send["parameters"].get("properties", {})

    def test_bedrock_format(self) -> None:
        """get_tools_for(format='bedrock') returns AWS Bedrock format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack", format="bedrock")

            assert len(tools) == 2
            send = next(
                t for t in tools
                if t["toolSpec"]["name"] == "send_message"
            )
            assert "toolSpec" in send
            spec = send["toolSpec"]
            assert "description" in spec
            assert "inputSchema" in spec
            assert "json" in spec["inputSchema"]
            assert "channel" in spec["inputSchema"]["json"].get("properties", {})

    def test_raw_format(self) -> None:
        """get_tools_for(format='raw') returns raw schemas with actionId."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack", format="raw")

            assert len(tools) == 2
            send = next(t for t in tools if t["name"] == "send_message")
            assert send["actionId"] == "act_slack_send_message"
            assert "inputSchema" in send
            assert "outputSchema" in send

    def test_invalid_format(self) -> None:
        """get_tools_for(format='invalid') raises ValueError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            with pytest.raises(ValueError, match="Unsupported format"):
                client.get_tools_for("slack", format="invalid")

    def test_connector_not_found(self) -> None:
        """get_tools_for('nonexistent', ...) raises ConnectorNotFoundError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            with pytest.raises(ConnectorNotFoundError):
                client.get_tools_for("nonexistent", format="openai")

    def test_unwraps_single_wrapper_key(self) -> None:
        """Schemas with a single 'body' wrapper are unwrapped for LLMs."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack", format="openai")
            send = next(t for t in tools if t["function"]["name"] == "send_message")
            params = send["function"]["parameters"]
            # Should NOT have 'body' as a property — it should be unwrapped
            assert "body" not in params.get("properties", {})
            assert params["type"] == "object"
            assert "channel" in params["properties"]

    def test_default_format_is_openai(self) -> None:
        """get_tools_for() defaults to openai format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack")
            assert tools[0]["type"] == "function"


# ---------------------------------------------------------------------------
# get_tools() / get_tool() tests
# ---------------------------------------------------------------------------

class TestGetTools:
    def test_get_tools(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir, with_schemas=True)
            client = FastnClient(config_path=config_path)
            tools = client.get_tools("slack")
            assert len(tools) == 2
            names = {t["name"] for t in tools}
            assert "send_message" in names
            assert "create_channel" in names

    def test_get_tool(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir, with_schemas=True)
            client = FastnClient(config_path=config_path)
            tool = client.get_tool("slack", "send_message")
            assert tool["name"] == "send_message"
            assert tool["actionId"] == "act_slack_send_message"
            assert "inputSchema" in tool

    def test_get_tool_not_found(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            with pytest.raises(ToolNotFoundError):
                client.get_tool("slack", "nonexistent_tool")

    def test_get_tools_connector_not_found(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            with pytest.raises(ConnectorNotFoundError):
                client.get_tools("nonexistent")


# ---------------------------------------------------------------------------
# Async client tests
# ---------------------------------------------------------------------------

class TestAsyncFastnClient:
    def test_init(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)
            assert repr(client).startswith("<AsyncFastnClient")

    def test_connector_access(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)
            slack = client.slack
            assert "send_message" in dir(slack)

    @pytest.mark.asyncio
    async def test_execute_tool_success(self, httpx_mock: HTTPXMock) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path, max_retries=0)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/executeTool",
                method="POST",
                json={"ok": True},
            )

            result = await client.slack.send_message(
                channel="general", text="Hello"
            )
            assert result["ok"] is True

    @pytest.mark.asyncio
    async def test_execute_tool_auth_error(self, httpx_mock: HTTPXMock) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path, max_retries=0)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/executeTool",
                method="POST",
                status_code=401,
            )

            with pytest.raises(AuthError):
                await client.slack.send_message(channel="general", text="Hello")

    @pytest.mark.asyncio
    async def test_execute_by_action_id(self, httpx_mock: HTTPXMock) -> None:
        """Async execute() calls executeTool with action_id and params."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path, max_retries=0)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/executeTool",
                method="POST",
                json={"ok": True},
            )

            result = await client.execute(
                "act_slack_send_message",
                {"channel": "general", "text": "Hello"},
            )
            assert result["ok"] is True

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["input"]["actionId"] == "act_slack_send_message"

    def test_get_tools_for_openai(self) -> None:
        """Async client get_tools_for() works (sync method, no await needed)."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir, with_schemas=True)
            client = AsyncFastnClient(config_path=config_path)
            tools = client.get_tools_for("slack", format="openai")
            assert len(tools) == 2
            assert tools[0]["type"] == "function"

    def test_get_tools_for_anthropic(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir, with_schemas=True)
            client = AsyncFastnClient(config_path=config_path)
            tools = client.get_tools_for("slack", format="anthropic")
            assert len(tools) == 2
            assert "input_schema" in tools[0]

    def test_get_tools_for_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir, with_schemas=True)
            client = AsyncFastnClient(config_path=config_path)
            with pytest.raises(ValueError, match="Unsupported format"):
                client.get_tools_for("slack", format="cohere")
