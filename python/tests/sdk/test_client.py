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


def _create_multi_connector_env(tmpdir: str) -> str:
    """Create a .fastn dir with config and registry containing slack + jira."""
    fastn_dir = Path(tmpdir) / ".fastn"
    fastn_dir.mkdir()

    config = {
        "api_key": "test-api-key",
        "project_id": "test-project-id",
        "stage": "LIVE",
    }
    (fastn_dir / "config.json").write_text(json.dumps(config))

    registry = {
        "version": "2025.02.14",
        "connectors": {
            "slack": {
                "id": "conn_slack_001",
                "display_name": "Slack",
                "category": "communication",
                "tools": {
                    "send_message": {
                        "actionId": "act_slack_send_message",
                        "description": "Send a message to a channel",
                        "inputSchema": _SAMPLE_INPUT_SCHEMA,
                    },
                    "create_channel": {
                        "actionId": "act_slack_create_channel",
                        "description": "Create a new channel",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "body": {
                                    "type": "object",
                                    "properties": {
                                        "name": {"type": "string"},
                                    },
                                    "required": ["name"],
                                }
                            },
                        },
                    },
                },
            },
            "jira": {
                "id": "conn_jira_001",
                "display_name": "Jira",
                "category": "project_management",
                "tools": {
                    "create_issue": {
                        "actionId": "act_jira_create_issue",
                        "description": "Create a Jira issue",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "body": {
                                    "type": "object",
                                    "properties": {
                                        "summary": {"type": "string"},
                                        "project": {"type": "string"},
                                    },
                                    "required": ["summary", "project"],
                                }
                            },
                        },
                    },
                },
            },
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
            # execute() sends params flat (no wrapper key)
            assert body["input"]["parameters"]["channel"] == "general"

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

    # --- Connector-based tests (local registry lookup) ---

    def test_openai_format(self) -> None:
        """get_tools_for(connector=..., format='openai') returns OpenAI format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack tools", connector="slack", format="openai")

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
        """get_tools_for(connector=..., format='anthropic') returns Anthropic format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack tools", connector="slack", format="anthropic")

            assert len(tools) == 2
            send = next(t for t in tools if t["name"] == "send_message")
            assert "input_schema" in send
            assert "description" in send
            # Unwrapped
            assert "channel" in send["input_schema"].get("properties", {})

    def test_gemini_format(self) -> None:
        """get_tools_for(connector=..., format='gemini') returns Google Gemini format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack tools", connector="slack", format="gemini")

            assert len(tools) == 2
            send = next(t for t in tools if t["name"] == "send_message")
            assert "parameters" in send
            assert "description" in send
            assert "channel" in send["parameters"].get("properties", {})

    def test_bedrock_format(self) -> None:
        """get_tools_for(connector=..., format='bedrock') returns AWS Bedrock format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack tools", connector="slack", format="bedrock")

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
        """get_tools_for(connector=..., format='raw') returns raw schemas with actionId."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack tools", connector="slack", format="raw")

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
                client.get_tools_for("slack tools", connector="slack", format="invalid")

    def test_connector_not_found(self) -> None:
        """get_tools_for(connector='nonexistent') raises ConnectorNotFoundError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            with pytest.raises(ConnectorNotFoundError):
                client.get_tools_for("tools", connector="nonexistent", format="openai")

    def test_unwraps_single_wrapper_key(self) -> None:
        """Schemas with a single 'body' wrapper are unwrapped for LLMs."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack tools", connector="slack", format="openai")
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
            tools = client.get_tools_for("slack tools", connector="slack")
            assert tools[0]["type"] == "function"

    # --- Connector-based: limit and multi-connector ---

    def test_limit_default(self) -> None:
        """Default limit=5 returns all when fewer than 5 tools exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack tools", connector="slack", format="openai")
            assert len(tools) == 2  # only 2 tools in fixture, below limit

    def test_limit_one(self) -> None:
        """limit=1 returns only 1 tool."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)
            tools = client.get_tools_for("slack tools", connector="slack", format="openai", limit=1)
            assert len(tools) == 1

    def test_multiple_connectors(self) -> None:
        """Passing a list of connector names returns tools from all."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_multi_connector_env(tmpdir)
            client = FastnClient(config_path=config_path)
            tools = client.get_tools_for(
                "project tools",
                connector=["slack", "jira"],
                format="openai",
                limit=100,
            )
            names = [t["function"]["name"] for t in tools]
            assert "send_message" in names
            assert "create_issue" in names

    def test_multiple_connectors_with_limit(self) -> None:
        """Limit applies to total tools across all connectors."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_multi_connector_env(tmpdir)
            client = FastnClient(config_path=config_path)
            tools = client.get_tools_for(
                "project tools",
                connector=["slack", "jira"],
                format="openai",
                limit=2,
            )
            assert len(tools) == 2

    # --- Prompt-based tests (API call) ---

    def test_prompt_openai(self, httpx_mock: HTTPXMock) -> None:
        """Prompt-based get_tools_for() calls /getTools API and returns OpenAI format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)

            # Mock the /getTools API response
            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/getTools",
                json={
                    "tools": [
                        {
                            "actionId": "act_slack_send_message",
                            "name": "send_message",
                            "description": "Send a message",
                            "inputSchema": _SAMPLE_INPUT_SCHEMA,
                        }
                    ]
                },
            )

            tools = client.get_tools_for("Send a message on Slack", format="openai")
            assert len(tools) == 1
            assert tools[0]["type"] == "function"
            assert tools[0]["function"]["name"] == "send_message"

            # Verify the API was called with prompt
            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["input"]["prompt"] == "Send a message on Slack"
            assert body["input"]["limit"] == 5

    def test_prompt_with_limit(self, httpx_mock: HTTPXMock) -> None:
        """Prompt-based discovery sends limit to API."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/getTools",
                json={"tools": []},
            )

            tools = client.get_tools_for("List Jira issues", format="openai", limit=10)
            assert tools == []

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["input"]["limit"] == 10

    def test_prompt_raw_format(self, httpx_mock: HTTPXMock) -> None:
        """Prompt-based with format='raw' returns API response directly."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)

            raw_tool = {
                "actionId": "act_slack_send_message",
                "name": "send_message",
                "description": "Send a message",
                "inputSchema": _SAMPLE_INPUT_SCHEMA,
            }
            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/getTools",
                json={"tools": [raw_tool]},
            )

            tools = client.get_tools_for("Send a Slack message", format="raw")
            assert len(tools) == 1
            assert tools[0]["actionId"] == "act_slack_send_message"

    def test_prompt_api_error(self, httpx_mock: HTTPXMock) -> None:
        """Prompt-based discovery raises APIError on failure."""
        with tempfile.TemporaryDirectory() as tmpdir:
            client = self._make_client(tmpdir)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/getTools",
                status_code=500,
                text="Internal Server Error",
            )

            with pytest.raises(APIError, match="Tool discovery failed"):
                client.get_tools_for("Send a message", format="openai")


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

    @pytest.mark.asyncio
    async def test_get_tools_for_connector_openai(self) -> None:
        """Async client get_tools_for(connector=...) returns OpenAI format."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir, with_schemas=True)
            client = AsyncFastnClient(config_path=config_path)
            tools = await client.get_tools_for("slack tools", connector="slack", format="openai")
            assert len(tools) == 2
            assert tools[0]["type"] == "function"

    @pytest.mark.asyncio
    async def test_get_tools_for_connector_anthropic(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir, with_schemas=True)
            client = AsyncFastnClient(config_path=config_path)
            tools = await client.get_tools_for("slack tools", connector="slack", format="anthropic")
            assert len(tools) == 2
            assert "input_schema" in tools[0]

    @pytest.mark.asyncio
    async def test_get_tools_for_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir, with_schemas=True)
            client = AsyncFastnClient(config_path=config_path)
            with pytest.raises(ValueError, match="Unsupported format"):
                await client.get_tools_for("slack tools", connector="slack", format="cohere")

    @pytest.mark.asyncio
    async def test_get_tools_for_multiple_connectors(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_multi_connector_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)
            tools = await client.get_tools_for(
                "project tools",
                connector=["slack", "jira"],
                format="openai",
                limit=100,
            )
            assert len(tools) == 3  # 2 slack + 1 jira

    @pytest.mark.asyncio
    async def test_get_tools_for_with_limit(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_multi_connector_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)
            tools = await client.get_tools_for("slack tools", connector="slack", format="openai", limit=1)
            assert len(tools) == 1


# ---------------------------------------------------------------------------
# Flows connector tests
# ---------------------------------------------------------------------------

def _create_flows_test_env(tmpdir: str) -> str:
    """Create a .fastn directory with config, registry including flows connector."""
    fastn_dir = Path(tmpdir) / ".fastn"
    fastn_dir.mkdir()

    config = {
        "api_key": "test-api-key",
        "project_id": "my-project-id",
        "stage": "LIVE",
    }
    (fastn_dir / "config.json").write_text(json.dumps(config))

    registry = {
        "version": "2025.02.14",
        "connectors": {
            "slack": {
                "id": "conn_slack_001",
                "display_name": "Slack",
                "category": "communication",
                "tools": {
                    "send_message": {
                        "actionId": "act_slack_send_message",
                        "description": "Send a message",
                    },
                },
            },
            "flows": {
                "id": "conn_flows_001",
                "display_name": "Flows",
                "category": "workflow",
                "connector_type": "FLOW",
                "tools": {
                    "run_onboarding": {
                        "actionId": "act_flows_run_onboarding",
                        "description": "Run the onboarding flow",
                    },
                },
            },
        },
    }
    (fastn_dir / "registry.json").write_text(json.dumps(registry))

    return str(fastn_dir / "config.json")


class TestFlowsConnector:
    def test_flows_uses_registry_id(self) -> None:
        """Flows connector should use the registry-assigned connector ID."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_flows_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            proxy = client.flows
            assert proxy._connector_id == "conn_flows_001"

    def test_regular_connector_uses_registry_id(self) -> None:
        """Regular connectors should use the registry-assigned connector ID."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_flows_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            proxy = client.slack
            assert proxy._connector_id == "conn_slack_001"

    def test_flows_sends_connector_id_in_payload(self, httpx_mock: HTTPXMock) -> None:
        """Flows tool call should send the registry connector ID in the payload."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_flows_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/ucl/executeTool",
                json={"ok": True},
            )

            client.flows.run_onboarding(name="Alice")

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["input"]["connectorId"] == "conn_flows_001"
            assert body["input"]["actionId"] == "act_flows_run_onboarding"

    @pytest.mark.asyncio
    async def test_async_flows_uses_registry_id(self) -> None:
        """Async client flows connector should also use registry ID."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_flows_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)
            proxy = client.flows
            assert proxy._connector_id == "conn_flows_001"
