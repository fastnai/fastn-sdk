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
    ToolNotFoundError,
    FastnError,
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
    """Create a .fastn dir with config and registry containing slack + jira connectors."""
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

    def test_connectors_list(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            connectors = client.connectors.list()
            assert len(connectors) == 1
            assert connectors[0]["name"] == "slack"

    def test_connectors_get(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            connector = client.connectors.get("slack")
            assert connector["name"] == "slack"
            assert "send_message" in connector["tools"]

    def test_connectors_get_not_found(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            with pytest.raises(ConnectorNotFoundError):
                client.connectors.get("nonexistent")


# ---------------------------------------------------------------------------
# execute() tests
# ---------------------------------------------------------------------------

class TestExecute:
    def test_execute_by_tool(self, httpx_mock: HTTPXMock) -> None:
        """execute() calls executeTool with the given tool and params."""
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

    def test_tool_not_found(self) -> None:
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
    async def test_execute_by_tool(self, httpx_mock: HTTPXMock) -> None:
        """Async execute() calls executeTool with tool and params."""
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
# Flows management namespace tests
# ---------------------------------------------------------------------------

class TestFlowsNamespace:
    def test_flows_is_management_namespace(self) -> None:
        """client.flows should be a _FlowsSync management namespace."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            # flows is now a management namespace, not a DynamicConnector
            assert hasattr(client.flows, "create")
            assert hasattr(client.flows, "delete")
            assert hasattr(client.flows, "run")
            assert hasattr(client.flows, "get_run")
            assert hasattr(client.flows, "list")
            assert hasattr(client.flows, "update")

    def test_flows_create(self, httpx_mock: HTTPXMock) -> None:
        """flows.create() sends prompt to the flows API."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/create",
                method="POST",
                json={"body": {"flow_id": "flow_abc123"}},
            )

            result = client.flows.create(prompt="When a Jira ticket is created, post to Slack")
            assert result["flow_id"] == "flow_abc123"

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["prompt"] == "When a Jira ticket is created, post to Slack"

    def test_flows_create_with_answers(self, httpx_mock: HTTPXMock) -> None:
        """flows.create() sends answers on follow-up call."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/create",
                method="POST",
                json={"body": {"flow_id": "flow_abc123"}},
            )

            result = client.flows.create(
                prompt="Sync data to Salesforce",
                answers={"channel": "#general", "frequency": "daily"},
            )
            assert result["flow_id"] == "flow_abc123"

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["answers"]["channel"] == "#general"

    def test_flows_delete(self, httpx_mock: HTTPXMock) -> None:
        """flows.delete() sends flow_id to the delete endpoint."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/delete",
                method="POST",
                json={"body": {"deleted": True}},
            )

            result = client.flows.delete(flow_id="flow_abc123")
            assert result["deleted"] is True

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["flow_id"] == "flow_abc123"

    def test_flows_run(self, httpx_mock: HTTPXMock) -> None:
        """flows.run() triggers a flow run and returns run_id."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/run",
                method="POST",
                json={"body": {"run_id": "run_xyz", "status": "running"}},
            )

            result = client.flows.run(flow_id="flow_abc123")
            assert result["run_id"] == "run_xyz"
            assert result["status"] == "running"

    def test_flows_run_with_user_id(self, httpx_mock: HTTPXMock) -> None:
        """flows.run() passes user_id for multi-tenant flows."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/run",
                method="POST",
                json={"body": {"run_id": "run_xyz", "status": "running"}},
            )

            client.flows.run(flow_id="flow_abc123", user_id="user_42")

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["user_id"] == "user_42"

    def test_flows_get_run(self, httpx_mock: HTTPXMock) -> None:
        """flows.get_run() returns run status."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/get_run",
                method="POST",
                json={"body": {"run_id": "run_xyz", "status": "completed", "result": {"ok": True}}},
            )

            result = client.flows.get_run(run_id="run_xyz")
            assert result["status"] == "completed"

    def test_flows_list(self, httpx_mock: HTTPXMock) -> None:
        """flows.list() returns list of flows via the apis GraphQL query."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/graphql",
                method="POST",
                json={
                    "data": {
                        "apis": {
                            "pageInfo": {"totalCount": 2},
                            "edges": [
                                {"node": {"id": "flow_1", "name": "Flow One", "description": "First flow", "status": "active", "version": "1", "updatedAt": "2024-01-01", "deployedAt": "2024-01-01", "metaData": {"flowType": "integration", "architecture": "sequential", "isAsync": False}}},
                                {"node": {"id": "flow_2", "name": "Flow Two", "description": "Second flow", "status": "active", "version": "2", "updatedAt": "2024-01-02", "deployedAt": "2024-01-02", "metaData": None}},
                            ],
                        }
                    }
                },
            )

            result = client.flows.list()
            assert len(result) == 2
            assert result[0]["flow_id"] == "flow_1"
            assert result[0]["name"] == "Flow One"
            assert result[0]["status"] == "active"
            assert result[0]["version"] == "1"
            assert result[1]["flow_id"] == "flow_2"

    def test_flows_list_with_status_filter(self, httpx_mock: HTTPXMock) -> None:
        """flows.list(status=...) filters flows client-side."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/graphql",
                method="POST",
                json={
                    "data": {
                        "apis": {
                            "pageInfo": {"totalCount": 2},
                            "edges": [
                                {"node": {"id": "flow_1", "name": "Flow One", "description": "Active", "status": "active", "version": "1", "updatedAt": "", "deployedAt": ""}},
                                {"node": {"id": "flow_2", "name": "Flow Two", "description": "Paused", "status": "paused", "version": "1", "updatedAt": "", "deployedAt": ""}},
                            ],
                        }
                    }
                },
            )

            result = client.flows.list(status="active")
            assert len(result) == 1
            assert result[0]["flow_id"] == "flow_1"

    def test_flows_update(self, httpx_mock: HTTPXMock) -> None:
        """flows.update() sends update payload."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/update",
                method="POST",
                json={"body": {"flow_id": "flow_abc", "enabled": False}},
            )

            result = client.flows.update(flow_id="flow_abc", enabled=False, schedule="0 9 * * MON-FRI")
            assert result["enabled"] is False

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["flow_id"] == "flow_abc"
            assert body["enabled"] is False
            assert body["schedule"] == "0 9 * * MON-FRI"

    def test_flows_auth_error(self, httpx_mock: HTTPXMock) -> None:
        """flows API returns 401 → raises AuthError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/create",
                method="POST",
                status_code=401,
            )

            with pytest.raises(AuthError):
                client.flows.create(prompt="test")

    def test_flows_not_found_error(self, httpx_mock: HTTPXMock) -> None:
        """flows.delete() raises FlowNotFoundError when ID and name resolution both fail."""
        from fastn.exceptions import FlowNotFoundError

        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            # Delete returns 404 → triggers name resolution
            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/delete",
                method="POST",
                status_code=404,
                json={"error": "FLOW_NOT_FOUND"},
            )
            # Resolution lists flows → no match found → FlowNotFoundError
            httpx_mock.add_response(
                url="https://live.fastn.ai/api/graphql",
                method="POST",
                json={"data": {"apis": {"pageInfo": {"totalCount": 0}, "edges": []}}},
            )

            with pytest.raises(FlowNotFoundError):
                client.flows.delete(flow_id="nonexistent")

    def test_flows_delete_resolves_versioned_name(self, httpx_mock: HTTPXMock) -> None:
        """flows.delete() resolves a versioned name to the base flow_id."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            # First delete with versioned name → 404
            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/delete",
                method="POST",
                status_code=404,
                json={"error": "FLOW_NOT_FOUND"},
            )
            # Resolution lists flows → finds match
            httpx_mock.add_response(
                url="https://live.fastn.ai/api/graphql",
                method="POST",
                json={
                    "data": {
                        "apis": {
                            "pageInfo": {"totalCount": 1},
                            "edges": [
                                {"node": {"id": "testflow", "name": "testflow_v1", "description": "", "status": "active", "version": "1", "updatedAt": "", "deployedAt": ""}},
                            ],
                        }
                    }
                },
            )
            # Second delete with resolved base ID → success
            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/delete",
                method="POST",
                json={"body": {"deleted": True}},
            )

            result = client.flows.delete(flow_id="testflow_v1")
            assert result["deleted"] is True

            # Verify: 3 requests made (delete, graphql list, delete)
            requests = httpx_mock.get_requests()
            assert len(requests) == 3
            # Last delete used the resolved base ID
            last_body = json.loads(requests[2].content)
            assert last_body["flow_id"] == "testflow"

    def test_flows_run_not_found_error(self, httpx_mock: HTTPXMock) -> None:
        """flows API returns RUN_NOT_FOUND → raises RunNotFoundError."""
        from fastn.exceptions import RunNotFoundError

        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/get_run",
                method="POST",
                status_code=404,
                json={"error": "RUN_NOT_FOUND"},
            )

            with pytest.raises(RunNotFoundError):
                client.flows.get_run(run_id="nonexistent")


# ---------------------------------------------------------------------------
# Auth management namespace tests
# ---------------------------------------------------------------------------

class TestAuthNamespace:
    def test_auth_is_management_namespace(self) -> None:
        """client.auth should be a _AuthSync management namespace."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)
            assert hasattr(client.auth, "connect")
            assert hasattr(client.auth, "status")

    def test_auth_connect(self, httpx_mock: HTTPXMock) -> None:
        """auth.connect() starts OAuth flow."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/connections/initiate",
                method="POST",
                json={"body": {
                    "connection_id": "conn_new",
                    "auth_url": "https://auth.example.com/authorize",
                    "status": "pending",
                    "expires_in": 600,
                }},
            )

            result = client.auth.connect(
                connector="slack",
                tenant_id="acme-corp",
                redirect_url="https://myapp.com/callback",
            )
            assert result["connection_id"] == "conn_new"
            assert result["auth_url"].startswith("https://")
            assert result["status"] == "pending"

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["connector"] == "slack"
            assert body["tenant_id"] == "acme-corp"
            assert body["redirect_url"] == "https://myapp.com/callback"

    def test_auth_status_by_id(self, httpx_mock: HTTPXMock) -> None:
        """auth.status() checks by connection_id."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/connections/status",
                method="POST",
                json={"body": {
                    "connection_id": "conn_abc",
                    "connector": "slack",
                    "status": "active",
                }},
            )

            result = client.auth.status(connection_id="conn_abc")
            assert result["status"] == "active"

    def test_auth_status_by_connector_and_tenant(self, httpx_mock: HTTPXMock) -> None:
        """auth.status() looks up by connector + tenant_id."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/connections/status",
                method="POST",
                json={"body": {
                    "connection_id": "conn_xyz",
                    "connector": "github",
                    "status": "active",
                    "tenant_id": "acme",
                }},
            )

            result = client.auth.status(connector="github", tenant_id="acme")
            assert result["connector"] == "github"

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert body["connector"] == "github"
            assert body["tenant_id"] == "acme"


# ---------------------------------------------------------------------------
# configure_custom_auth tests
# ---------------------------------------------------------------------------

class TestAuthConfigureCustom:
    def test_auth_configure_custom_sync(self, httpx_mock: HTTPXMock) -> None:
        """auth.configure_custom() sends updateResolverStep GraphQL mutation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/graphql",
                method="POST",
                json={
                    "data": {
                        "updateResolverStep": {
                            "id": "fastnCustomAuth",
                            "type": "COMPOSITE",
                            "warnings": None,
                            "__typename": "ResolverStep",
                        }
                    }
                },
            )

            result = client.auth.configure_custom(
                userinfo_url="https://myapp.auth0.com/userinfo",
            )
            assert result["updateResolverStep"]["id"] == "fastnCustomAuth"

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert "updateResolverStep" in body["query"]
            # Verify userinfo_url is embedded in the step payload
            variables_str = json.dumps(body["variables"])
            assert "https://myapp.auth0.com/userinfo" in variables_str
            # Verify variables use the "input" key as expected by the mutation
            assert "input" in body["variables"]

    @pytest.mark.asyncio
    async def test_auth_configure_custom_async(self, httpx_mock: HTTPXMock) -> None:
        """Async auth.configure_custom() sends updateResolverStep GraphQL mutation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/graphql",
                method="POST",
                json={
                    "data": {
                        "updateResolverStep": {
                            "id": "fastnCustomAuth",
                            "type": "COMPOSITE",
                            "warnings": None,
                            "__typename": "ResolverStep",
                        }
                    }
                },
            )

            result = await client.auth.configure_custom(
                userinfo_url="https://myapp.auth0.com/userinfo",
            )
            assert result["updateResolverStep"]["id"] == "fastnCustomAuth"


# ---------------------------------------------------------------------------
# Async flows / auth namespace tests
# ---------------------------------------------------------------------------

class TestAsyncFlowsNamespace:
    @pytest.mark.asyncio
    async def test_async_flows_create(self, httpx_mock: HTTPXMock) -> None:
        """Async flows.create() sends prompt to the flows API."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/create",
                method="POST",
                json={"body": {"flow_id": "flow_async_123"}},
            )

            result = await client.flows.create(prompt="Sync Jira to Slack")
            assert result["flow_id"] == "flow_async_123"

    @pytest.mark.asyncio
    async def test_async_flows_list(self, httpx_mock: HTTPXMock) -> None:
        """Async flows.list() returns list of flows via the apis GraphQL query."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/graphql",
                method="POST",
                json={
                    "data": {
                        "apis": {
                            "pageInfo": {"totalCount": 2},
                            "edges": [
                                {"node": {"id": "flow_1", "name": "Flow One", "description": "First", "status": "active", "version": "1", "updatedAt": "", "deployedAt": ""}},
                                {"node": {"id": "flow_2", "name": "Flow Two", "description": "Second", "status": "active", "version": "1", "updatedAt": "", "deployedAt": ""}},
                            ],
                        }
                    }
                },
            )

            result = await client.flows.list()
            assert len(result) == 2
            assert result[0]["flow_id"] == "flow_1"

    @pytest.mark.asyncio
    async def test_async_flows_delete_resolves_versioned_name(self, httpx_mock: HTTPXMock) -> None:
        """Async flows.delete() resolves a versioned name to the base flow_id."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)

            # First delete → 404
            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/delete",
                method="POST",
                status_code=404,
                json={"error": "FLOW_NOT_FOUND"},
            )
            # Resolution lists flows → finds match
            httpx_mock.add_response(
                url="https://live.fastn.ai/api/graphql",
                method="POST",
                json={
                    "data": {
                        "apis": {
                            "pageInfo": {"totalCount": 1},
                            "edges": [
                                {"node": {"id": "testflow", "name": "testflow_v1", "description": "", "status": "active", "version": "1", "updatedAt": "", "deployedAt": ""}},
                            ],
                        }
                    }
                },
            )
            # Second delete → success
            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/delete",
                method="POST",
                json={"body": {"deleted": True}},
            )

            result = await client.flows.delete(flow_id="testflow_v1")
            assert result["deleted"] is True

    @pytest.mark.asyncio
    async def test_async_flows_run(self, httpx_mock: HTTPXMock) -> None:
        """Async flows.run() triggers a flow."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/flows/run",
                method="POST",
                json={"body": {"run_id": "run_async", "status": "running"}},
            )

            result = await client.flows.run(flow_id="flow_abc")
            assert result["run_id"] == "run_async"

    @pytest.mark.asyncio
    async def test_async_auth_connect(self, httpx_mock: HTTPXMock) -> None:
        """Async auth.connect() starts OAuth flow."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/connections/initiate",
                method="POST",
                json={"body": {
                    "connection_id": "conn_async",
                    "auth_url": "https://auth.example.com/authorize",
                    "status": "pending",
                    "expires_in": 600,
                }},
            )

            result = await client.auth.connect(
                connector="slack",
                tenant_id="acme",
                redirect_url="https://myapp.com/callback",
            )
            assert result["connection_id"] == "conn_async"

    @pytest.mark.asyncio
    async def test_async_auth_status(self, httpx_mock: HTTPXMock) -> None:
        """Async auth.status() checks connection status."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_test_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)

            httpx_mock.add_response(
                url="https://live.fastn.ai/api/connections/status",
                method="POST",
                json={"body": {"connection_id": "conn_abc", "status": "active"}},
            )

            result = await client.auth.status(connection_id="conn_abc")
            assert result["status"] == "active"
