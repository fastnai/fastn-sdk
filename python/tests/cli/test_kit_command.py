"""Tests for the fastn kit (Connect Kit) CLI commands."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

from click.testing import CliRunner

from fastn.cli import cli


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


# ---------------------------------------------------------------------------
# Shared sample data
# ---------------------------------------------------------------------------

_SAMPLE_CONNECTORS_RESPONSE = {
    "data": {
        "widgetConnectors": {
            "edges": [
                {
                    "node": {
                        "id": "_knexa_conn-001",
                        "name": "Slack",
                        "active": True,
                        "connectionId": "cid-001",
                        "widgetType": "messaging",
                        "labels": ["chat"],
                        "imageUri": "https://example.com/slack.png",
                    }
                },
                {
                    "node": {
                        "id": "_knexa_conn-002",
                        "name": "HubSpot",
                        "active": False,
                        "connectionId": "cid-002",
                        "widgetType": "crm",
                        "labels": ["sales"],
                        "imageUri": "https://example.com/hubspot.png",
                    }
                },
            ]
        }
    }
}

_SAMPLE_KIT_METADATA = {
    "data": {
        "widgetMetadata": {
            "authenticationApi": "fastnCustomAuth",
            "isCustomAuthenticationEnabled": True,
            "filterWidgets": ["slack", "hubspot"],
            "showFilterBar": True,
            "showLabels": True,
            "isRBACEnabled": False,
            "styles": None,
            "disableFor": None,
            "isAIAgentWidgetEnabled": True,
            "labelsLayout": "horizontal",
            "advancedSettings": None,
            "widgetsMetrics": None,
            "__typename": "WidgetMetadata",
        }
    }
}

_SAMPLE_SAVE_RESPONSE = {
    "data": {
        "saveWidgetMetadata": {
            "authenticationApi": None,
            "isCustomAuthenticationEnabled": False,
            "advancedSettings": None,
            "__typename": "WidgetMetadata",
        }
    }
}

_SAMPLE_CONNECTOR_DETAIL = {
    "data": {
        "connector": {
            "id": "_knexa_conn-001",
            "name": "Slack",
            "imageUri": "https://example.com/slack.png",
            "active": True,
            "deployed": True,
            "widgetType": "messaging",
            "description": "Slack messaging connector",
            "actions": [
                {
                    "name": "send_message",
                    "handler": "slack_send",
                    "actionType": "action",
                    "__typename": "ConnectorAction",
                }
            ],
            "events": [],
            "connectedConnectors": [],
            "labels": ["chat"],
            "__typename": "Connector",
        }
    }
}


# ---------------------------------------------------------------------------
# fastn kit ls
# ---------------------------------------------------------------------------

class TestKitLsCommand:
    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_ls_success(self, mock_load, mock_post):
        """Lists kit connectors with name and ID."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(json_data=_SAMPLE_CONNECTORS_RESPONSE)

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "ls"])

        assert result.exit_code == 0
        assert "Slack" in result.output
        assert "HubSpot" in result.output
        assert "_knexa_conn-001" in result.output
        assert "_knexa_conn-002" in result.output
        assert "2 connector(s) found" in result.output

        # Verify GraphQL variables
        call_args = mock_post.call_args
        payload = call_args[1].get("payload") or call_args[0][2]
        variables = payload["variables"]
        assert variables["input"]["projectId"] == "test-project-id"
        assert variables["input"]["first"] == 50

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_ls_with_query(self, mock_load, mock_post):
        """Passes the -q search query to the API."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(json_data=_SAMPLE_CONNECTORS_RESPONSE)

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "ls", "-q", "slack"])

        assert result.exit_code == 0

        # Verify the inner query contains the search term
        call_args = mock_post.call_args
        payload = call_args[1].get("payload") or call_args[0][2]
        variables = payload["variables"]
        inner_query = json.loads(variables["input"]["query"])
        assert inner_query["input"]["query"] == "slack"

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_ls_empty(self, mock_load, mock_post):
        """Handles no connectors found."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"data": {"widgetConnectors": {"edges": []}}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "ls"])

        assert result.exit_code == 0
        assert "No Connect Kit connectors found" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_ls_null_connectors(self, mock_load, mock_post):
        """Handles null widgetConnectors gracefully."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"data": {"widgetConnectors": None}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "ls"])

        assert result.exit_code == 0
        assert "No Connect Kit connectors found" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_ls_401(self, mock_load, mock_post):
        """Handles 401 authentication error."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(status_code=401, text="Unauthorized")

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "ls"])

        assert result.exit_code != 0
        assert "Authentication failed" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_ls_gql_error(self, mock_load, mock_post):
        """Handles GraphQL-level errors."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"errors": [{"message": "Permission denied"}]}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "ls"])

        assert result.exit_code != 0
        assert "GraphQL error" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_ls_not_authenticated(self, mock_load, mock_post):
        """Rejects unauthenticated users."""
        config = MagicMock()
        config.auth_token = ""
        config.api_key = ""
        mock_load.return_value = config

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "ls"])

        assert result.exit_code != 0
        assert "Not authenticated" in result.output


# ---------------------------------------------------------------------------
# fastn kit get <name>
# ---------------------------------------------------------------------------

class TestKitGetCommand:
    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_get_success(self, mock_load, mock_post):
        """Fetches connector details by name."""
        mock_load.return_value = _mock_config()
        # First call: list connectors; second call: get connector detail
        mock_post.side_effect = [
            _mock_response(json_data=_SAMPLE_CONNECTORS_RESPONSE),
            _mock_response(json_data=_SAMPLE_CONNECTOR_DETAIL),
        ]

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "get", "Slack"])

        assert result.exit_code == 0
        assert "Slack" in result.output
        assert "send_message" in result.output
        assert "_knexa_conn-001" in result.output

        # Verify the GetConnector call variables
        second_call = mock_post.call_args_list[1]
        payload = second_call[1].get("payload") or second_call[0][2]
        variables = payload["variables"]
        assert variables["input"]["projectId"] == "test-project-id"
        assert variables["input"]["id"] == "_knexa_conn-001"
        assert variables["input"]["template"] is False

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_get_case_insensitive(self, mock_load, mock_post):
        """Finds connector with case-insensitive name match."""
        mock_load.return_value = _mock_config()
        mock_post.side_effect = [
            _mock_response(json_data=_SAMPLE_CONNECTORS_RESPONSE),
            _mock_response(json_data=_SAMPLE_CONNECTOR_DETAIL),
        ]

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "get", "slack"])

        assert result.exit_code == 0
        assert "Slack" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_get_not_found(self, mock_load, mock_post):
        """Handles connector name not in list."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(json_data=_SAMPLE_CONNECTORS_RESPONSE)

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "get", "nonexistent"])

        assert result.exit_code != 0
        assert "not found" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_get_detail_empty(self, mock_load, mock_post):
        """Handles null connector detail response."""
        mock_load.return_value = _mock_config()
        mock_post.side_effect = [
            _mock_response(json_data=_SAMPLE_CONNECTORS_RESPONSE),
            _mock_response(json_data={"data": {"connector": None}}),
        ]

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "get", "Slack"])

        assert result.exit_code != 0
        assert "Could not fetch details" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_get_401(self, mock_load, mock_post):
        """Handles 401 authentication error."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(status_code=401, text="Unauthorized")

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "get", "Slack"])

        assert result.exit_code != 0
        assert "Authentication failed" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_get_not_authenticated(self, mock_load, mock_post):
        """Rejects unauthenticated users."""
        config = MagicMock()
        config.auth_token = ""
        config.api_key = ""
        mock_load.return_value = config

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "get", "Slack"])

        assert result.exit_code != 0
        assert "Not authenticated" in result.output

    def test_kit_get_requires_name(self):
        """Fails if no connector name is given."""
        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "get"])

        assert result.exit_code != 0
        assert "Missing argument" in result.output


# ---------------------------------------------------------------------------
# fastn kit config (show / update)
# ---------------------------------------------------------------------------

class TestKitConfigCommand:
    # --- Show mode (no --data) ---

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_config_show(self, mock_load, mock_post):
        """Shows kit configuration as JSON."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(json_data=_SAMPLE_KIT_METADATA)

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "config"])

        assert result.exit_code == 0
        assert "authenticationApi" in result.output
        assert "isCustomAuthenticationEnabled" in result.output

        # Verify GraphQL variables
        call_args = mock_post.call_args
        payload = call_args[1].get("payload") or call_args[0][2]
        variables = payload["variables"]
        assert variables["input"]["id"] == "test-project-id"
        assert variables["input"]["clientId"] == "test-project-id"

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_config_show_empty(self, mock_load, mock_post):
        """Handles empty/null widgetMetadata gracefully."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"data": {"widgetMetadata": None}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "config"])

        assert result.exit_code == 0
        assert "No Connect Kit configuration found" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_config_show_401(self, mock_load, mock_post):
        """Handles 401 authentication error in show mode."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(status_code=401, text="Unauthorized")

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "config"])

        assert result.exit_code != 0
        assert "Authentication failed" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_config_show_gql_error(self, mock_load, mock_post):
        """Handles GraphQL-level errors in show mode."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"errors": [{"message": "Not authorized"}]}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "config"])

        assert result.exit_code != 0
        assert "GraphQL error" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_config_show_not_authenticated(self, mock_load, mock_post):
        """Rejects unauthenticated users in show mode."""
        config = MagicMock()
        config.auth_token = ""
        config.api_key = ""
        mock_load.return_value = config

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "config"])

        assert result.exit_code != 0
        assert "Not authenticated" in result.output

    # --- Update mode (with --data) ---

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_config_update_success(self, mock_load, mock_post):
        """Updates kit configuration and shows success."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(json_data=_SAMPLE_SAVE_RESPONSE)

        runner = CliRunner()
        result = runner.invoke(
            cli, ["kit", "config", "-d", '{"showFilterBar": true, "showLabels": false}']
        )

        assert result.exit_code == 0
        assert "updated successfully" in result.output

        # Verify mutation variables
        call_args = mock_post.call_args
        payload = call_args[1].get("payload") or call_args[0][2]
        variables = payload["variables"]
        assert variables["input"]["projectId"] == "test-project-id"
        assert variables["input"]["showFilterBar"] is True
        assert variables["input"]["showLabels"] is False

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_config_update_invalid_json(self, mock_load, mock_post):
        """Handles invalid JSON input."""
        mock_load.return_value = _mock_config()

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "config", "-d", "not json"])

        assert result.exit_code != 0
        assert "Invalid JSON" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_config_update_non_object_json(self, mock_load, mock_post):
        """Rejects non-object JSON values."""
        mock_load.return_value = _mock_config()

        runner = CliRunner()
        result = runner.invoke(cli, ["kit", "config", "-d", '"just a string"'])

        assert result.exit_code != 0
        assert "must be a JSON object" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_config_update_401(self, mock_load, mock_post):
        """Handles 401 authentication error in update mode."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(status_code=401, text="Unauthorized")

        runner = CliRunner()
        result = runner.invoke(
            cli, ["kit", "config", "-d", '{"showFilterBar": true}']
        )

        assert result.exit_code != 0
        assert "Authentication failed" in result.output

    @patch("fastn.cli.kit_command._verbose_post")
    @patch("fastn.cli.kit_command.load_config")
    def test_kit_config_update_gql_error(self, mock_load, mock_post):
        """Handles GraphQL-level errors in update mode."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"errors": [{"message": "Invalid input"}]}
        )

        runner = CliRunner()
        result = runner.invoke(
            cli, ["kit", "config", "-d", '{"showFilterBar": true}']
        )

        assert result.exit_code != 0
        assert "GraphQL error" in result.output
