"""Tests for the fastn flow CLI commands."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest
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
# fastn flow create
# ---------------------------------------------------------------------------

class TestFlowsCreateCommand:
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_create_success(self, mock_load, mock_post):
        """Creates a flow and shows the flow_id."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"body": {"flow_id": "new_flow_123"}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "create", "-p", "Post to Slack when Jira ticket created"])

        assert result.exit_code == 0
        assert "new_flow_123" in result.output

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_create_with_questions(self, mock_load, mock_post):
        """Shows follow-up questions when flow needs more info."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"body": {"questions": ["Which Slack channel?", "What priority?"]}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "create", "-p", "Sync data"])

        assert result.exit_code == 0
        assert "Which Slack channel?" in result.output
        assert "more information" in result.output


# ---------------------------------------------------------------------------
# fastn flow run
# ---------------------------------------------------------------------------

class TestFlowsRunCommand:
    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_run_success(self, mock_load, mock_post):
        """Triggers a flow run and shows run_id."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"body": {"run_id": "run_abc", "status": "running"}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "run", "testflow"])

        assert result.exit_code == 0
        assert "run_abc" in result.output
        assert "running" in result.output

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_run_with_user_id(self, mock_load, mock_post):
        """Passes user_id for multi-tenant flows."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            json_data={"body": {"run_id": "run_abc", "status": "running"}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "run", "testflow", "--user-id", "user_42"])

        assert result.exit_code == 0
        # Verify user_id was sent
        call_args = mock_post.call_args
        payload = call_args[1].get("payload") or call_args[0][2]
        assert payload["user_id"] == "user_42"

    @patch("fastn.cli.flows_command._verbose_post")
    @patch("fastn.cli.flows_command.load_config")
    def test_flows_run_not_found(self, mock_load, mock_post):
        """Handles flow not found error."""
        mock_load.return_value = _mock_config()
        mock_post.return_value = _mock_response(
            status_code=404, json_data={"error": "FLOW_NOT_FOUND"}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["flow", "run", "nonexistent"])

        assert result.exit_code != 0
        assert "not found" in result.output.lower()


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
