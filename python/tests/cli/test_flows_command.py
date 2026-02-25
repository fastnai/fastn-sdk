"""Tests for the fastn flow CLI commands."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner

from fastn.cli import cli
from fastn._flows import _extract_input_fields, _extract_output_fields


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _mock_config():
    """Return a mock config with valid auth."""
    config = MagicMock()
    config.auth_token = "fake-token"
    config.api_key = "test-key"
    config.project_id = "test-project-id"
    config.tenant_id = None
    config.stage = None
    config.timeout = 30.0
    config.refresh_token = None
    config.token_expiry = None
    config.resolve_project_id.return_value = "test-project-id"
    config.get_headers.return_value = {"Authorization": "Bearer fake-token"}
    return config


def _mock_response(status_code=200, json_data=None, text=""):
    """Create a mock httpx response."""
    resp = MagicMock()
    resp.status_code = status_code
    resp.json.return_value = json_data or {}
    resp.text = text or json.dumps(json_data or {})
    return resp


_SAMPLE_FLOWS_GQL = {
    "data": {
        "apis": {
            "pageInfo": {"totalCount": 2},
            "edges": [
                {"node": {"id": "testflow", "name": "Test Flow", "description": "A test flow", "status": "active", "version": "1", "updatedAt": "2025-01-01", "deployedAt": "2025-01-01", "metaData": {"flowType": "integration", "architecture": "sequential", "isAsync": False}}},
                {"node": {"id": "syncflow", "name": "Sync Flow", "description": "Syncs data", "status": "paused", "version": "2", "updatedAt": "2025-02-01", "deployedAt": "2025-02-01", "metaData": None}},
            ],
        }
    }
}


# ---------------------------------------------------------------------------
# fastn flow (list)
# ---------------------------------------------------------------------------

class TestFlowsListCommand:
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_list_success(self, mock_load, mock_post):
        """Lists flows in a table format."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(json_data=_SAMPLE_FLOWS_GQL)

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "ls"])

        assert result.exit_code == 0
        assert "Test Flow" in result.output
        assert "Sync Flow" in result.output
        assert "testflow" in result.output
        assert "syncflow" in result.output
        assert "2 flow(s) found" in result.output

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_list_with_status_filter(self, mock_load, mock_post):
        """Filters flows by status."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(json_data=_SAMPLE_FLOWS_GQL)

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "ls", "--status", "active"])

        assert result.exit_code == 0
        assert "Test Flow" in result.output
        assert "Sync Flow" not in result.output
        assert "1 flow(s) found" in result.output

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_list_empty(self, mock_load, mock_post):
        """Shows message when no flows exist."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"data": {"apis": {"pageInfo": {"totalCount": 0}, "edges": []}}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "ls"])

        assert result.exit_code == 0
        assert "No flows found" in result.output

    @patch("fastn.cli.flows_command.load_config")
    def test_flows_no_auth(self, mock_load):
        """Errors when not authenticated."""
        config = MagicMock()
        config.auth_token = ""
        config.api_key = ""
        mock_load.return_value = config

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "ls"])

        assert result.exit_code != 0
        assert "Not authenticated" in result.output

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_list_401(self, mock_load, mock_post):
        """Handles 401 authentication error."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(status_code=401, text="Unauthorized")

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "ls"])

        assert result.exit_code != 0
        assert "Authentication failed" in result.output

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_list_graphql_error(self, mock_load, mock_post):
        """Handles GraphQL-level errors."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"errors": [{"message": "Not authorized"}]}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "ls"])

        assert result.exit_code != 0
        assert "GraphQL error" in result.output


# ---------------------------------------------------------------------------
# fastn flow generate
# ---------------------------------------------------------------------------

class TestFlowsCreateCommand:
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_generate_success(self, mock_load, mock_post):
        """Creates a flow and shows the flow_id on first response."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"body": {"flow_id": "new_flow_123", "message": "Flow created!"}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "generate", "-p", "Post to Slack when Jira ticket created"])

        assert result.exit_code == 0
        assert "new_flow_123" in result.output

        # Verify correct API endpoint and payload
        call_args = mock_post.call_args
        assert "flowBuilderAgent" in call_args[0][0]
        assert call_args[1]["headers"]["x-fastn-custom-auth"] == "true"
        payload = call_args[1]["payload"]
        assert payload["input"]["chatInput"] == "Post to Slack when Jira ticket created"
        assert "sessionID" in payload["input"]

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_generate_multi_turn(self, mock_load, mock_post):
        """Handles multi-turn conversation: agent asks, user answers, flow created."""
        mock_load.return_value = _mock_config()
        # First response: agent asks a question; second: flow created
        mock_post.side_effect = [
            _mock_response(json_data={"body": {"message": "Which Slack channel?"}}),
            _mock_response(json_data={"body": {"flow_id": "flow_456", "message": "Done!"}}),
        ]

        runner = CliRunner()
        result = runner.invoke(
            cli, ["flow", "generate", "-p", "Sync data"],
            input="#general\n",
        )

        assert result.exit_code == 0
        assert "Which Slack channel?" in result.output
        assert "flow_456" in result.output
        assert mock_post.call_count == 2

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_generate_empty_input_exits(self, mock_load, mock_post):
        """Empty follow-up input ends the session."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"body": {"message": "Which Slack channel?"}}
        )

        runner = CliRunner()
        result = runner.invoke(
            cli, ["flow", "generate", "-p", "Sync data"],
            input="\n",
        )

        assert result.exit_code == 0
        assert "Session ended" in result.output

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_generate_401(self, mock_load, mock_post):
        """Handles 401 from the flow builder agent."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(status_code=401, text="Unauthorized")

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "generate", "-p", "Sync data"])

        assert result.exit_code != 0
        assert "Authentication failed" in result.output


# ---------------------------------------------------------------------------
# fastn flow run (v1 API)
# ---------------------------------------------------------------------------

class TestFlowsRunCommand:
    @patch("fastn.cli.flows_command._discover_input_fields", return_value=([], {}))
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_run_success(self, mock_load, mock_post, mock_discover):
        """Runs a flow via the v1 API with no discovered fields."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(200, {"body": {"result": "ok"}})

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "run", "testflow"])

        assert result.exit_code == 0
        assert "executed successfully" in result.output

        # Verify v1 API was called with correct URL, payload, and custom-auth header
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        assert call_args[0][0] == "https://live.fastn.ai/api/v1/testflow"
        assert call_args[1]["payload"] == {"input": {}}
        assert call_args[1]["headers"]["x-fastn-custom-auth"] == "true"

    @patch("fastn.cli.flows_command._discover_input_fields", return_value=([], {}))
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_run_with_stage(self, mock_load, mock_post, mock_discover):
        """Passes stage header to the v1 API."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(200, {"body": {"result": "ok"}})

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "run", "testflow", "--stage", "DRAFT"])

        assert result.exit_code == 0

        call_args = mock_post.call_args
        assert call_args[1]["headers"]["stage"] == "DRAFT"

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_run_with_input(self, mock_load, mock_post):
        """Passes input data as JSON, skips schema discovery."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(200, {"body": {"result": "ok"}})

        runner = CliRunner()
        result = runner.invoke(cli, [
            "flow", "run", "testflow",
            "-d", '{"name": "hello", "email": "test@example.com"}'
        ])

        assert result.exit_code == 0

        call_args = mock_post.call_args
        assert call_args[1]["payload"] == {"input": {"name": "hello", "email": "test@example.com"}}

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_run_invalid_json(self, mock_load, mock_post):
        """Handles invalid JSON input."""
        mock_load.return_value = _mock_config()

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "run", "testflow", "-d", "not json"])

        assert result.exit_code != 0
        assert "Invalid JSON" in result.output

    @patch("fastn.cli.flows_command._discover_input_fields", return_value=([], {}))
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_run_401(self, mock_load, mock_post, mock_discover):
        """Handles 401 authentication error."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(401, text="Unauthorized")

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "run", "testflow"])

        assert result.exit_code != 0
        assert "Authentication failed" in result.output

    @patch("fastn.cli.flows_command._discover_input_fields")
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_run_auto_schema_prompts(self, mock_load, mock_post, mock_discover):
        """Discovers input fields and prompts the user for values."""
        mock_load.return_value = _mock_config()
        mock_discover.return_value = (
            ["email", "name"],
            {"type": "object", "properties": {"name": {"type": "string"}, "email": {"type": "string"}}},
        )
        mock_post.return_value = _mock_response(200, {"body": {"result": "ok"}})

        runner = CliRunner()
        # Provide input for the two prompts (name and email, sorted)
        result = runner.invoke(
            cli, ["flow", "run", "testflow"], input="test@example.com\nhello\n"
        )

        assert result.exit_code == 0
        assert "executed successfully" in result.output

        # Verify the constructed input payload
        call_args = mock_post.call_args
        assert call_args[1]["payload"] == {"input": {"email": "test@example.com", "name": "hello"}}

    @patch("fastn.cli.flows_command._discover_input_fields")
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_run_auto_schema_nested_fields(self, mock_load, mock_post, mock_discover):
        """Handles nested dot-path fields in auto-schema prompting."""
        mock_load.return_value = _mock_config()
        mock_discover.return_value = (
            ["user.email", "user.name"],
            {"type": "object", "properties": {"user": {"type": "object"}}},
        )
        mock_post.return_value = _mock_response(200, {"body": {"result": "ok"}})

        runner = CliRunner()
        result = runner.invoke(
            cli, ["flow", "run", "testflow"], input="test@x.com\nAlice\n"
        )

        assert result.exit_code == 0
        call_args = mock_post.call_args
        assert call_args[1]["payload"] == {"input": {"user": {"email": "test@x.com", "name": "Alice"}}}

    @patch("fastn.cli.flows_command._discover_input_fields")
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_run_explicit_input_skips_discovery(self, mock_load, mock_post, mock_discover):
        """--input flag skips schema discovery entirely."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(200, {"body": {"result": "ok"}})

        runner = CliRunner()
        result = runner.invoke(cli, [
            "flow", "run", "testflow", "-d", '{"x": 1}'
        ])

        assert result.exit_code == 0
        mock_discover.assert_not_called()

        call_args = mock_post.call_args
        assert call_args[1]["payload"] == {"input": {"x": 1}}

    @patch("fastn.cli.flows_command._discover_input_fields")
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_run_json_values_in_prompt(self, mock_load, mock_post, mock_discover):
        """Prompt values that look like JSON are parsed as such."""
        mock_load.return_value = _mock_config()
        mock_discover.return_value = (["count", "tags"], {})
        mock_post.return_value = _mock_response(200, {"body": {"result": "ok"}})

        runner = CliRunner()
        result = runner.invoke(
            cli, ["flow", "run", "testflow"], input='42\n["a","b"]\n'
        )

        assert result.exit_code == 0
        call_args = mock_post.call_args
        assert call_args[1]["payload"] == {"input": {"count": 42, "tags": ["a", "b"]}}


# ---------------------------------------------------------------------------
# fastn flow deploy
# ---------------------------------------------------------------------------

class TestFlowsDeployCommand:
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_deploy_success(self, mock_load, mock_post):
        """Deploys a flow to LIVE (default stage)."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"data": {"deployApiToStage": {"id": "testflow", "__typename": "Api"}}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "deploy", "testflow"])

        assert result.exit_code == 0
        assert "deployed to LIVE" in result.output

        # Verify mutation variables
        call_args = mock_post.call_args
        payload = call_args[1].get("payload") or call_args[0][2]
        variables = payload["variables"]
        assert variables["input"]["clientId"] == "test-project-id"
        assert variables["input"]["env"] == "LIVE"
        assert variables["input"]["id"] == "testflow"

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_deploy_with_stage_draft(self, mock_load, mock_post):
        """Deploys a flow to DRAFT stage."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"data": {"deployApiToStage": {"id": "testflow", "__typename": "Api"}}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "deploy", "testflow", "--stage", "DRAFT"])

        assert result.exit_code == 0
        assert "deployed to DRAFT" in result.output

        call_args = mock_post.call_args
        payload = call_args[1].get("payload") or call_args[0][2]
        assert payload["variables"]["input"]["env"] == "DRAFT"

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_deploy_with_comment(self, mock_load, mock_post):
        """Passes the deployment comment in the mutation variables."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"data": {"deployApiToStage": {"id": "testflow", "__typename": "Api"}}}
        )

        runner = CliRunner()
        result = runner.invoke(
            cli, ["flow", "deploy", "testflow", "-m", "Production release"]
        )

        assert result.exit_code == 0

        call_args = mock_post.call_args
        payload = call_args[1].get("payload") or call_args[0][2]
        assert payload["variables"]["input"]["comment"] == "Production release"

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_deploy_401(self, mock_load, mock_post):
        """Handles 401 authentication error."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(status_code=401, text="Unauthorized")

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "deploy", "testflow"])

        assert result.exit_code != 0
        assert "Authentication failed" in result.output

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_deploy_gql_error(self, mock_load, mock_post):
        """Handles GraphQL-level errors."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"errors": [{"message": "Flow not found"}]}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "deploy", "testflow"])

        assert result.exit_code != 0
        assert "GraphQL error" in result.output


# ---------------------------------------------------------------------------
# fastn flow schema
# ---------------------------------------------------------------------------

_SAMPLE_FLOW_WITH_STEPS = {
    "data": {
        "api": {
            "id": "testflow",
            "name": "testflow",
            "description": "A test flow",
            "status": "active",
            "version": "1",
            "inputModel": None,
            "outputModel": None,
            "resolver": {
                "steps": [
                    {
                        "id": "step1",
                        "type": "inline",
                        "inline": {
                            "code": "const name = params.data.input.name;\nconst email = params.data.input.email;\nreturn {name, email};",
                            "uiCode": None,
                        },
                    },
                    {
                        "id": "step2",
                        "type": "aiAgent",
                        "aiAgent": {
                            "prompt": "Hello {{input.greeting}}, process the request for {{input.name}}",
                            "systemPrompt": "You are a helpful assistant",
                        },
                    },
                    {
                        "id": "step3",
                        "type": "logger",
                        "logger": {
                            "message": "Processing {{input.message}}",
                            "context": None,
                        },
                    },
                ],
            },
        }
    }
}


class TestFlowsSchemaCommand:
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_schema_ai_tool_format(self, mock_load, mock_post):
        """Outputs AI tool format JSON with name, description, actionId, inputSchema, outputSchema."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(json_data=_SAMPLE_FLOW_WITH_STEPS)

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "schema", "testflow"])

        assert result.exit_code == 0
        tool = json.loads(result.output)
        assert tool["name"] == "testflow"
        assert tool["description"] == "A test flow"
        assert tool["actionId"] == "testflow"

        # inputSchema discovered from steps
        inp = tool["inputSchema"]
        assert inp["type"] == "object"
        assert "email" in inp["properties"]
        assert "greeting" in inp["properties"]
        assert "message" in inp["properties"]
        assert "name" in inp["properties"]

        # outputSchema empty (no outputModel)
        out = tool["outputSchema"]
        assert out["type"] == "object"
        assert out["properties"] == {}

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_schema_with_input_model(self, mock_load, mock_post):
        """Uses inputModel.jsonSchema when available instead of step scanning."""
        mock_load.return_value = _mock_config()
        input_schema = {
            "type": "object",
            "properties": {
                "channel": {"type": "string", "description": "Slack channel"},
                "message": {"type": "string", "description": "Message to send"},
            },
            "required": ["channel", "message"],
        }
        mock_post.return_value = _mock_response(json_data={
            "data": {
                "api": {
                    "id": "slackflow",
                    "name": "Send to Slack",
                    "description": "Posts a message to Slack",
                    "inputModel": {"id": "m1", "name": "SlackInput", "jsonSchema": json.dumps(input_schema)},
                    "outputModel": None,
                    "resolver": {"steps": []},
                }
            }
        })

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "schema", "slackflow"])

        assert result.exit_code == 0
        tool = json.loads(result.output)
        assert tool["name"] == "Send to Slack"
        assert tool["actionId"] == "slackflow"
        assert tool["inputSchema"] == input_schema

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_schema_with_output_model(self, mock_load, mock_post):
        """Uses outputModel.jsonSchema when available."""
        mock_load.return_value = _mock_config()
        output_schema = {
            "type": "object",
            "properties": {"status": {"type": "string"}},
            "required": ["status"],
        }
        mock_post.return_value = _mock_response(json_data={
            "data": {
                "api": {
                    "id": "myflow",
                    "name": "myflow",
                    "description": "",
                    "inputModel": None,
                    "outputModel": {"id": "o1", "name": "Out", "jsonSchema": json.dumps(output_schema)},
                    "resolver": {"steps": [
                        {"id": "s1", "type": "aiAgent", "aiAgent": {"prompt": "{{input.query}}"}}
                    ]},
                }
            }
        })

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "schema", "myflow"])

        assert result.exit_code == 0
        tool = json.loads(result.output)
        assert tool["outputSchema"] == output_schema
        # inputSchema falls back to step scanning
        assert "query" in tool["inputSchema"]["properties"]

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_schema_no_inputs_empty_schema(self, mock_load, mock_post):
        """Returns empty inputSchema/outputSchema when nothing found."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={
                "data": {
                    "api": {
                        "id": "noflow",
                        "name": "noflow",
                        "description": "",
                        "inputModel": None,
                        "outputModel": None,
                        "resolver": {"steps": [{"id": "s1", "type": "logger", "logger": {"message": "hello world"}}]},
                    }
                }
            }
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "schema", "noflow"])

        assert result.exit_code == 0
        tool = json.loads(result.output)
        assert tool["name"] == "noflow"
        assert tool["inputSchema"]["properties"] == {}
        assert tool["outputSchema"]["properties"] == {}

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_schema_flow_not_found(self, mock_load, mock_post):
        """Handles flow not found."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"data": {"api": None}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "schema", "nonexistent"])

        assert result.exit_code != 0
        assert "not found" in result.output.lower()

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_schema_input_model_fallback_to_steps(self, mock_load, mock_post):
        """Falls back to step scanning when inputModel has empty jsonSchema."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(json_data={
            "data": {
                "api": {
                    "id": "testflow",
                    "name": "testflow",
                    "description": "Fallback test",
                    "inputModel": {"id": "m1", "name": "Empty", "jsonSchema": None},
                    "outputModel": None,
                    "resolver": {"steps": [
                        {"id": "s1", "type": "aiAgent", "aiAgent": {"prompt": "Hello {{input.name}}"}}
                    ]},
                }
            }
        })

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "schema", "testflow"])

        assert result.exit_code == 0
        tool = json.loads(result.output)
        assert "name" in tool["inputSchema"]["properties"]

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_schema_uses_id_variable(self, mock_load, mock_post):
        """Sends 'id' (not 'name') in the GraphQL variables."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(json_data={
            "data": {
                "api": {
                    "id": "myflow",
                    "name": "myflow",
                    "description": "",
                    "inputModel": None,
                    "outputModel": None,
                    "resolver": {"steps": []},
                }
            }
        })

        runner = CliRunner()
        runner.invoke(cli, ["flow", "schema", "myflow"])

        call_args = mock_post.call_args
        payload = call_args[1].get("payload") or call_args[0][2]
        variables = payload.get("variables", {})
        assert variables["input"]["id"] == "myflow"
        assert "name" not in variables["input"]

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_schema_output_from_has_response(self, mock_load, mock_post):
        """Extracts outputSchema from steps with hasResponse: true."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(json_data={
            "data": {
                "api": {
                    "id": "myflow",
                    "name": "myflow",
                    "description": "Test output",
                    "inputModel": None,
                    "outputModel": None,
                    "resolver": {"steps": [
                        {
                            "id": "s1",
                            "type": "inline",
                            "inline": {
                                "hasResponse": True,
                                "code": '{"done": "value"}',
                                "uiCode": json.dumps({
                                    "targetType": "object",
                                    "target": {
                                        "done": {"targetType": "string", "target": "value"},
                                    },
                                }),
                            },
                        },
                    ]},
                }
            }
        })

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "schema", "myflow"])

        assert result.exit_code == 0
        tool = json.loads(result.output)
        assert "done" in tool["outputSchema"]["properties"]
        assert tool["outputSchema"]["properties"]["done"]["type"] == "string"

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_schema_output_model_takes_priority(self, mock_load, mock_post):
        """outputModel.jsonSchema takes priority over hasResponse scanning."""
        mock_load.return_value = _mock_config()
        explicit_schema = {
            "type": "object",
            "properties": {"official": {"type": "string"}},
            "required": ["official"],
        }
        mock_post.return_value = _mock_response(json_data={
            "data": {
                "api": {
                    "id": "myflow",
                    "name": "myflow",
                    "description": "",
                    "inputModel": None,
                    "outputModel": {"id": "o1", "name": "Out", "jsonSchema": json.dumps(explicit_schema)},
                    "resolver": {"steps": [
                        {
                            "id": "s1",
                            "type": "inline",
                            "inline": {
                                "hasResponse": True,
                                "uiCode": json.dumps({
                                    "targetType": "object",
                                    "target": {"scanned": {"targetType": "string"}},
                                }),
                            },
                        },
                    ]},
                }
            }
        })

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "schema", "myflow"])

        assert result.exit_code == 0
        tool = json.loads(result.output)
        # outputModel wins
        assert tool["outputSchema"] == explicit_schema
        assert "scanned" not in tool["outputSchema"].get("properties", {})


# ---------------------------------------------------------------------------
# fastn flow get-run
# ---------------------------------------------------------------------------

class TestFlowsGetRunCommand:
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_get_run_success(self, mock_load, mock_post):
        """Shows run status details."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"body": {
                "run_id": "run_abc",
                "status": "completed",
                "started_at": "2025-01-01T10:00:00Z",
                "completed_at": "2025-01-01T10:01:00Z",
                "result": {"ok": True},
            }}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "get-run", "run_abc"])

        assert result.exit_code == 0
        assert "completed" in result.output
        assert "run_abc" in result.output

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_get_run_not_found(self, mock_load, mock_post):
        """Handles run not found error."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            status_code=404, json_data={"error": "RUN_NOT_FOUND"}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "get-run", "nonexistent"])

        assert result.exit_code != 0
        assert "not found" in result.output.lower()


# ---------------------------------------------------------------------------
# fastn flow delete
# ---------------------------------------------------------------------------

class TestFlowsDeleteCommand:
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_delete_success(self, mock_load, mock_post):
        """Deletes a flow with -y flag."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"body": {"deleted": True}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "delete", "testflow", "-y"])

        assert result.exit_code == 0
        assert "deleted" in result.output.lower()

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_delete_confirm(self, mock_load, mock_post):
        """Prompts for confirmation without -y flag."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"body": {"deleted": True}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "delete", "testflow"], input="y\n")

        assert result.exit_code == 0
        assert "deleted" in result.output.lower()

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_delete_cancel(self, mock_load, mock_post):
        """Cancels deletion when user says no."""
        mock_load.return_value = _mock_config()

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "delete", "testflow"], input="n\n")

        assert result.exit_code == 0
        assert "Cancelled" in result.output
        mock_post.assert_not_called()

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_delete_not_found(self, mock_load, mock_post):
        """Handles flow not found error."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            status_code=404, json_data={"error": "FLOW_NOT_FOUND"}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "delete", "nonexistent", "-y"])

        assert result.exit_code != 0
        assert "not found" in result.output.lower()


# ---------------------------------------------------------------------------
# fastn flow update
# ---------------------------------------------------------------------------

class TestFlowsUpdateCommand:
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_update_schedule(self, mock_load, mock_post):
        """Updates a flow's schedule."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"body": {"flow_id": "testflow", "schedule": "0 9 * * MON-FRI"}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "update", "testflow", "--schedule", "0 9 * * MON-FRI"])

        assert result.exit_code == 0
        assert "updated" in result.output.lower()

        call_args = mock_post.call_args
        payload = call_args[1].get("payload") or call_args[0][2]
        assert payload["flow_id"] == "testflow"
        assert payload["schedule"] == "0 9 * * MON-FRI"

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_update_disable(self, mock_load, mock_post):
        """Disables a flow."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"body": {"flow_id": "testflow", "enabled": False}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "update", "testflow", "--disabled"])

        assert result.exit_code == 0
        assert "updated" in result.output.lower()

    @patch("fastn.cli.flows_command.load_config")
    def test_flows_update_nothing(self, mock_load):
        """Errors when no update options are given."""
        mock_load.return_value = _mock_config()

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "update", "testflow"])

        assert result.exit_code != 0
        assert "Nothing to update" in result.output

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_update_sends_correct_payload(self, mock_load, mock_post):
        """Verifies the correct payload is sent."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"body": {"flow_id": "testflow"}}
        )

        runner = CliRunner()
        runner.invoke(cli, ["flow", "update", "testflow", "-p", "New prompt", "--enabled"])

        call_args = mock_post.call_args
        payload = call_args[1].get("payload") or call_args[0][2]
        assert payload["flow_id"] == "testflow"
        assert payload["prompt"] == "New prompt"
        assert payload["enabled"] is True


# ---------------------------------------------------------------------------
# _extract_input_fields unit tests
# ---------------------------------------------------------------------------

class TestExtractInputFields:
    def test_jinja_input_pattern(self):
        """Extracts fields from {{input.field}} patterns."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "aiAgent", "aiAgent": {"prompt": "Hello {{input.name}}, your email is {{input.email}}"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "name" in result["fields"]
        assert "email" in result["fields"]

    def test_jinja_with_spaces(self):
        """Extracts fields from {{ input.field }} with spaces."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "logger", "logger": {"message": "Hello {{ input.greeting }}"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "greeting" in result["fields"]

    def test_js_dot_notation(self):
        """Extracts fields from params.data.input.field patterns."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": "const x = params.data.input.userId;"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "userId" in result["fields"]

    def test_js_bracket_notation(self):
        """Extracts fields from params['data']['input']['field'] patterns."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": 'const x = params["data"]["input"]["apiKey"];'}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "apiKey" in result["fields"]

    def test_generic_input_dot(self):
        """Extracts fields from generic input.field patterns."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "variables", "variables": {"code": "let val = input.country;"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "country" in result["fields"]

    def test_nested_steps_in_loop(self):
        """Extracts fields from steps nested inside a loop."""
        flow_data = {
            "resolver": {
                "steps": [
                    {
                        "type": "loop",
                        "loop": {
                            "loopOver": "{{input.items}}",
                            "steps": [
                                {"type": "inline", "inline": {"code": "const x = params.data.input.batchSize;"}}
                            ]
                        }
                    }
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "items" in result["fields"]
        assert "batchSize" in result["fields"]

    def test_nested_steps_in_conditional(self):
        """Extracts fields from steps nested inside conditionals."""
        flow_data = {
            "resolver": {
                "steps": [
                    {
                        "type": "conditional",
                        "conditional": {
                            "expressions": [{"variable": "{{input.mode}}", "value": "test"}],
                            "steps": [
                                {"type": "logger", "logger": {"message": "Testing {{input.target}}"}}
                            ]
                        }
                    }
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "mode" in result["fields"]
        assert "target" in result["fields"]

    def test_no_inputs(self):
        """Returns empty when no input references found."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "logger", "logger": {"message": "Hello world, no inputs here"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert result["fields"] == []
        assert result["schema"]["properties"] == {}

    def test_empty_flow(self):
        """Handles flow with no resolver or steps."""
        result = _extract_input_fields({})
        assert result["fields"] == []

        result = _extract_input_fields({"resolver": {}})
        assert result["fields"] == []

        result = _extract_input_fields({"resolver": {"steps": []}})
        assert result["fields"] == []

    def test_deduplication(self):
        """Same field used in multiple steps is listed once."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "aiAgent", "aiAgent": {"prompt": "Hello {{input.name}}"}},
                    {"type": "logger", "logger": {"message": "Logging {{input.name}}"}},
                    {"type": "inline", "inline": {"code": "const n = params.data.input.name;"}},
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert result["fields"].count("name") == 1

    def test_schema_structure(self):
        """Schema has correct JSON Schema structure."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "aiAgent", "aiAgent": {"prompt": "{{input.name}} {{input.email}}"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        schema = result["schema"]
        assert schema["type"] == "object"
        assert "name" in schema["properties"]
        assert "email" in schema["properties"]
        assert schema["properties"]["name"]["type"] == "string"
        assert "name" in schema["required"]
        assert "email" in schema["required"]

    def test_mixed_patterns(self):
        """Extracts fields from multiple patterns in the same flow."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "aiAgent", "aiAgent": {"prompt": "Hello {{input.name}}"}},
                    {"type": "inline", "inline": {"code": "const e = params.data.input.email;"}},
                    {"type": "logger", "logger": {"message": "Country: {{input.country}}"}},
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert sorted(result["fields"]) == ["country", "email", "name"]

    def test_does_not_match_function_calls(self):
        """Does not match input.something() as a field name."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": "input.toString()"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "toString" not in result["fields"]

    # ── Python patterns ──

    def test_python_bracket_single_quotes(self):
        """Extracts fields from input['field'] (Python dict access)."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": "name = input['userName']"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "userName" in result["fields"]

    def test_python_bracket_double_quotes(self):
        """Extracts fields from input["field"] (Python dict access)."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": 'email = input["email"]'}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "email" in result["fields"]

    def test_python_get_method(self):
        """Extracts fields from input.get('field') (Python .get())."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": "val = input.get('apiKey')"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "apiKey" in result["fields"]

    def test_python_get_with_default(self):
        """Extracts fields from input.get('field', default) (Python .get() with default)."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": 'val = input.get("region", "us-east-1")'}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "region" in result["fields"]

    def test_python_data_input_bracket(self):
        """Extracts fields from data['input']['field'] (Python nested dict)."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": 'x = data["input"]["projectName"]'}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "projectName" in result["fields"]

    # ── Ruby patterns ──

    def test_ruby_symbol_access(self):
        """Extracts fields from input[:field] (Ruby symbol)."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": "name = input[:username]"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "username" in result["fields"]

    def test_ruby_params_symbol_chain(self):
        """Extracts fields from params[:data][:input][:field] (Ruby)."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": "val = params[:data][:input][:token]"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "token" in result["fields"]

    # ── PHP patterns ──

    def test_php_variable_access(self):
        """Extracts fields from $input['field'] (PHP)."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": "$name = $input['firstName'];"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "firstName" in result["fields"]

    def test_php_params_chain(self):
        """Extracts fields from $params['data']['input']['field'] (PHP)."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": "$val = $params['data']['input']['orderId'];"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "orderId" in result["fields"]

    # ── Cross-language patterns ──

    def test_mixed_languages_in_same_flow(self):
        """Extracts fields from multiple language patterns in one flow."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": "const x = params.data.input.jsField;"}},
                    {"type": "inline", "inline": {"code": "val = input.get('pyField')"}},
                    {"type": "inline", "inline": {"code": "x = input[:rbField]"}},
                    {"type": "aiAgent", "aiAgent": {"prompt": "Hello {{input.jinjaField}}"}},
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "jsField" in result["fields"]
        assert "pyField" in result["fields"]
        assert "rbField" in result["fields"]
        assert "jinjaField" in result["fields"]

    # ── Nested field tests ──

    def test_jinja_nested_fields(self):
        """Extracts nested dot-paths from {{input.user.name}} patterns."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "aiAgent", "aiAgent": {"prompt": "Hello {{input.user.name}}, email: {{input.user.email}}"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "user.name" in result["fields"]
        assert "user.email" in result["fields"]

    def test_js_dot_nested_fields(self):
        """Extracts nested dot-paths from params.data.input.obj.sub."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": "const city = params.data.input.address.city;"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "address.city" in result["fields"]

    def test_js_bracket_nested_fields(self):
        """Extracts nested paths from chained bracket notation."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": 'const t = params["data"]["input"]["config"]["timeout"];'}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "config.timeout" in result["fields"]

    def test_python_bracket_nested_fields(self):
        """Extracts nested paths from input["user"]["name"]."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": 'name = input["user"]["name"]'}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "user.name" in result["fields"]

    def test_python_get_chained(self):
        """Extracts nested paths from input.get("data").get("value")."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": 'val = input.get("data").get("value")'}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "data.value" in result["fields"]

    def test_ruby_symbol_nested(self):
        """Extracts nested paths from input[:user][:email]."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": "email = input[:user][:email]"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "user.email" in result["fields"]

    def test_php_bracket_nested(self):
        """Extracts nested paths from $input['config']['key']."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": "$key = $input['config']['key'];"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "config.key" in result["fields"]

    def test_mixed_flat_and_nested(self):
        """Handles mix of flat and nested fields in same flow."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "aiAgent", "aiAgent": {"prompt": "{{input.simple}} and {{input.user.name}}"}},
                    {"type": "inline", "inline": {"code": "const city = params.data.input.address.city;"}},
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "simple" in result["fields"]
        assert "user.name" in result["fields"]
        assert "address.city" in result["fields"]

    def test_nested_schema_structure(self):
        """Nested fields produce nested JSON Schema objects."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "aiAgent", "aiAgent": {"prompt": "{{input.user.name}} {{input.user.email}} {{input.simple}}"}},
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        schema = result["schema"]
        assert schema["type"] == "object"

        # "simple" is a flat leaf
        assert schema["properties"]["simple"]["type"] == "string"

        # "user" is a nested object
        user_schema = schema["properties"]["user"]
        assert user_schema["type"] == "object"
        assert "name" in user_schema["properties"]
        assert "email" in user_schema["properties"]
        assert user_schema["properties"]["name"]["type"] == "string"
        assert user_schema["properties"]["email"]["type"] == "string"

        # Top-level required includes "simple" and "user"
        assert "simple" in schema["required"]
        assert "user" in schema["required"]

    def test_deeply_nested_fields(self):
        """Handles 3+ levels of nesting."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "inline", "inline": {"code": 'val = input["config"]["database"]["host"]'}},
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "config.database.host" in result["fields"]
        schema = result["schema"]
        config = schema["properties"]["config"]
        assert config["type"] == "object"
        db = config["properties"]["database"]
        assert db["type"] == "object"
        assert db["properties"]["host"]["type"] == "string"

    def test_generic_dot_nested(self):
        """Generic input.a.b pattern captures full path."""
        flow_data = {
            "resolver": {
                "steps": [
                    {"type": "variables", "variables": {"code": "let val = input.settings.theme;"}}
                ]
            }
        }
        result = _extract_input_fields(flow_data)
        assert "settings.theme" in result["fields"]


# ---------------------------------------------------------------------------
# _extract_output_fields unit tests
# ---------------------------------------------------------------------------

class TestExtractOutputFields:
    def test_uicode_target_extraction(self):
        """Extracts output fields from uiCode target keys."""
        flow_data = {
            "resolver": {
                "steps": [
                    {
                        "type": "inline",
                        "inline": {
                            "code": '{"done": "value"}',
                            "uiCode": json.dumps({
                                "actionType": "map",
                                "targetType": "object",
                                "target": {
                                    "done": {
                                        "actionType": "map",
                                        "targetType": "string",
                                        "target": "{{data.input.name}}",
                                    }
                                },
                            }),
                            "hasResponse": True,
                        },
                    }
                ]
            }
        }
        result = _extract_output_fields(flow_data)
        assert "done" in result["fields"]
        assert result["schema"]["properties"]["done"]["type"] == "string"

    def test_uicode_multiple_fields(self):
        """Extracts multiple output fields from uiCode target."""
        flow_data = {
            "resolver": {
                "steps": [
                    {
                        "type": "inline",
                        "inline": {
                            "hasResponse": True,
                            "uiCode": json.dumps({
                                "targetType": "object",
                                "target": {
                                    "status": {"targetType": "string"},
                                    "count": {"targetType": "number"},
                                    "active": {"targetType": "boolean"},
                                },
                            }),
                        },
                    }
                ]
            }
        }
        result = _extract_output_fields(flow_data)
        assert sorted(result["fields"]) == ["active", "count", "status"]
        assert result["schema"]["properties"]["status"]["type"] == "string"
        assert result["schema"]["properties"]["count"]["type"] == "number"
        assert result["schema"]["properties"]["active"]["type"] == "boolean"

    def test_code_json_key_extraction(self):
        """Falls back to extracting JSON keys from code when no uiCode."""
        flow_data = {
            "resolver": {
                "steps": [
                    {
                        "type": "inline",
                        "inline": {
                            "hasResponse": True,
                            "code": '{\n  "done": {% if data.input.name is defined %}{{data.input.name | tojson}}{% else %}null{% endif %}\n}',
                        },
                    }
                ]
            }
        }
        result = _extract_output_fields(flow_data)
        assert "done" in result["fields"]

    def test_code_js_return_extraction(self):
        """Extracts fields from JS return { key1, key2 } patterns."""
        flow_data = {
            "resolver": {
                "steps": [
                    {
                        "type": "inline",
                        "inline": {
                            "hasResponse": True,
                            "code": "const name = params.data.input.name;\nreturn { name, email, status };",
                        },
                    }
                ]
            }
        }
        result = _extract_output_fields(flow_data)
        assert "name" in result["fields"]
        assert "email" in result["fields"]
        assert "status" in result["fields"]

    def test_no_has_response_no_output(self):
        """Does not extract output from steps without hasResponse."""
        flow_data = {
            "resolver": {
                "steps": [
                    {
                        "type": "inline",
                        "inline": {
                            "code": 'return { result: "ok" };',
                            "hasResponse": False,
                        },
                    }
                ]
            }
        }
        result = _extract_output_fields(flow_data)
        assert result["fields"] == []

    def test_missing_has_response_no_output(self):
        """Does not extract output when hasResponse key is absent."""
        flow_data = {
            "resolver": {
                "steps": [
                    {
                        "type": "inline",
                        "inline": {
                            "code": '{"result": "ok"}',
                        },
                    }
                ]
            }
        }
        result = _extract_output_fields(flow_data)
        assert result["fields"] == []

    def test_nested_object_output(self):
        """Extracts nested object output from uiCode."""
        flow_data = {
            "resolver": {
                "steps": [
                    {
                        "type": "inline",
                        "inline": {
                            "hasResponse": True,
                            "uiCode": json.dumps({
                                "targetType": "object",
                                "target": {
                                    "user": {
                                        "targetType": "object",
                                        "target": {
                                            "name": {"targetType": "string"},
                                            "age": {"targetType": "number"},
                                        },
                                    },
                                    "status": {"targetType": "string"},
                                },
                            }),
                        },
                    }
                ]
            }
        }
        result = _extract_output_fields(flow_data)
        assert "status" in result["fields"]
        assert "user" in result["fields"]
        user_props = result["schema"]["properties"]["user"]
        assert user_props["type"] == "object"
        assert "name" in user_props["properties"]
        assert "age" in user_props["properties"]
        assert user_props["properties"]["age"]["type"] == "number"

    def test_direct_output_schema_on_node(self):
        """Uses outputSchema directly when present on the node."""
        flow_data = {
            "resolver": {
                "steps": [
                    {
                        "type": "inline",
                        "inline": {
                            "hasResponse": True,
                            "outputSchema": {
                                "type": "object",
                                "properties": {"result": {"type": "string"}},
                                "required": ["result"],
                            },
                        },
                    }
                ]
            }
        }
        result = _extract_output_fields(flow_data)
        assert "result" in result["fields"]

    def test_has_response_in_loop_step(self):
        """Finds hasResponse inside nested loop steps."""
        flow_data = {
            "resolver": {
                "steps": [
                    {
                        "type": "loop",
                        "loop": {
                            "loopOver": "items",
                            "steps": [
                                {
                                    "type": "inline",
                                    "inline": {
                                        "hasResponse": True,
                                        "uiCode": json.dumps({
                                            "targetType": "object",
                                            "target": {
                                                "processed": {"targetType": "boolean"},
                                            },
                                        }),
                                    },
                                }
                            ],
                        },
                    }
                ]
            }
        }
        result = _extract_output_fields(flow_data)
        assert "processed" in result["fields"]

    def test_empty_flow_no_output(self):
        """Returns empty for flows with no steps."""
        result = _extract_output_fields({})
        assert result["fields"] == []
        assert result["schema"]["properties"] == {}

        result = _extract_output_fields({"resolver": {"steps": []}})
        assert result["fields"] == []

    def test_walks_entire_tree(self):
        """Finds hasResponse regardless of where it is in the tree."""
        flow_data = {
            "some": {
                "deeply": {
                    "nested": {
                        "node": {
                            "hasResponse": True,
                            "uiCode": json.dumps({
                                "targetType": "object",
                                "target": {
                                    "found": {"targetType": "string"},
                                },
                            }),
                        }
                    }
                }
            }
        }
        result = _extract_output_fields(flow_data)
        assert "found" in result["fields"]
