"""Tests for the fastn skills CLI command."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner

from fastn.cli import cli


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_fastn_dir(tmpdir: str, *, config: dict = None) -> Path:
    """Create a .fastn directory with config and registry."""
    fastn_dir = Path(tmpdir) / ".fastn"
    fastn_dir.mkdir(parents=True, exist_ok=True)

    if config is None:
        config = {
            "api_key": "test-api-key",
            "project_id": "test-project-id",
            "stage": "LIVE",
        }
    (fastn_dir / "config.json").write_text(json.dumps(config))
    (fastn_dir / "registry.json").write_text(
        json.dumps({"version": "1.0.0", "connectors": {}})
    )
    (fastn_dir / "manifest.json").write_text(
        json.dumps({"installed": {}, "registry_version": "1.0.0"})
    )
    return fastn_dir


_SAMPLE_SKILLS = [
    {
        "id": "sk_001",
        "projectId": "test-project-id",
        "name": "Email Summarizer",
        "description": "Summarizes incoming emails and creates action items",
        "createdAt": "2025-01-15T10:00:00Z",
        "updatedAt": "2025-01-20T14:30:00Z",
        "__typename": "UCLAgent",
    },
    {
        "id": "sk_002",
        "projectId": "test-project-id",
        "name": "Slack Notifier",
        "description": "Posts notifications to Slack channels",
        "createdAt": "2025-02-01T09:00:00Z",
        "updatedAt": "2025-02-10T11:00:00Z",
        "__typename": "UCLAgent",
    },
]


def _mock_response(status_code: int = 200, json_data: dict = None, text: str = ""):
    """Create a mock httpx response."""
    resp = MagicMock()
    resp.status_code = status_code
    resp.json.return_value = json_data or {}
    resp.text = text or json.dumps(json_data or {})
    return resp


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestSkillsCommand:
    @patch("fastn.cli.skills_command._verbose_post")
    @patch("fastn.cli.skills_command.load_config")
    def test_skills_list_success(self, mock_load, mock_post):
        """Lists skills in a table format."""
        config = MagicMock()
        config.auth_token = "fake-token"
        config.api_key = "test-key"
        config.refresh_token = None
        config.token_expiry = None
        config.resolve_project_id.return_value = "test-project-id"
        config.get_headers.return_value = {"Authorization": "Bearer fake-token"}
        mock_load.return_value = config

        mock_post.return_value = _mock_response(
            json_data={"data": {"listUCLAgents": _SAMPLE_SKILLS}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["skills"])

        assert result.exit_code == 0
        assert "Email Summarizer" in result.output
        assert "Slack Notifier" in result.output
        assert "sk_001" in result.output
        assert "sk_002" in result.output
        assert "2 skill(s) found" in result.output

    @patch("fastn.cli.skills_command._verbose_post")
    @patch("fastn.cli.skills_command.load_config")
    def test_skills_list_empty(self, mock_load, mock_post):
        """Shows message when no skills exist."""
        config = MagicMock()
        config.auth_token = "fake-token"
        config.api_key = "test-key"
        config.refresh_token = None
        config.token_expiry = None
        config.resolve_project_id.return_value = "test-project-id"
        config.get_headers.return_value = {"Authorization": "Bearer fake-token"}
        mock_load.return_value = config

        mock_post.return_value = _mock_response(
            json_data={"data": {"listUCLAgents": []}}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["skills"])

        assert result.exit_code == 0
        assert "No skills found" in result.output

    @patch("fastn.cli.skills_command.load_config")
    def test_skills_no_auth(self, mock_load):
        """Errors when not authenticated."""
        config = MagicMock()
        config.auth_token = ""
        config.api_key = ""
        mock_load.return_value = config

        runner = CliRunner()
        result = runner.invoke(cli, ["skills"])

        assert result.exit_code != 0
        assert "Not authenticated" in result.output

    @patch("fastn.cli.skills_command._verbose_post")
    @patch("fastn.cli.skills_command.load_config")
    def test_skills_no_project(self, mock_load, mock_post):
        """Errors when no project is configured."""
        config = MagicMock()
        config.auth_token = "fake-token"
        config.api_key = "test-key"
        config.refresh_token = None
        config.token_expiry = None
        config.resolve_project_id.return_value = ""
        mock_load.return_value = config

        runner = CliRunner()
        result = runner.invoke(cli, ["skills"])

        assert result.exit_code != 0
        assert "No project configured" in result.output

    @patch("fastn.cli.skills_command._verbose_post")
    @patch("fastn.cli.skills_command.load_config")
    def test_skills_401_error(self, mock_load, mock_post):
        """Handles 401 authentication error."""
        config = MagicMock()
        config.auth_token = "expired-token"
        config.api_key = "test-key"
        config.refresh_token = None
        config.token_expiry = None
        config.resolve_project_id.return_value = "test-project-id"
        config.get_headers.return_value = {"Authorization": "Bearer expired-token"}
        mock_load.return_value = config

        mock_post.return_value = _mock_response(status_code=401, text="Unauthorized")

        runner = CliRunner()
        result = runner.invoke(cli, ["skills"])

        assert result.exit_code != 0
        assert "Authentication failed" in result.output

    @patch("fastn.cli.skills_command._verbose_post")
    @patch("fastn.cli.skills_command.load_config")
    def test_skills_500_error(self, mock_load, mock_post):
        """Handles server errors."""
        config = MagicMock()
        config.auth_token = "fake-token"
        config.api_key = "test-key"
        config.refresh_token = None
        config.token_expiry = None
        config.resolve_project_id.return_value = "test-project-id"
        config.get_headers.return_value = {"Authorization": "Bearer fake-token"}
        mock_load.return_value = config

        mock_post.return_value = _mock_response(
            status_code=500, text="Internal Server Error"
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["skills"])

        assert result.exit_code != 0
        assert "API error" in result.output

    @patch("fastn.cli.skills_command._verbose_post")
    @patch("fastn.cli.skills_command.load_config")
    def test_skills_graphql_error(self, mock_load, mock_post):
        """Handles GraphQL-level errors."""
        config = MagicMock()
        config.auth_token = "fake-token"
        config.api_key = "test-key"
        config.refresh_token = None
        config.token_expiry = None
        config.resolve_project_id.return_value = "test-project-id"
        config.get_headers.return_value = {"Authorization": "Bearer fake-token"}
        mock_load.return_value = config

        mock_post.return_value = _mock_response(
            json_data={"errors": [{"message": "Not authorized"}]}
        )

        runner = CliRunner()
        result = runner.invoke(cli, ["skills"])

        assert result.exit_code != 0
        assert "GraphQL error" in result.output

    @patch("fastn.cli.skills_command._verbose_post")
    @patch("fastn.cli.skills_command.load_config")
    def test_skills_sends_correct_payload(self, mock_load, mock_post):
        """Verifies the correct GraphQL query and variables are sent."""
        config = MagicMock()
        config.auth_token = "fake-token"
        config.api_key = "test-key"
        config.refresh_token = None
        config.token_expiry = None
        config.resolve_project_id.return_value = "my-project-123"
        config.get_headers.return_value = {"Authorization": "Bearer fake-token"}
        mock_load.return_value = config

        mock_post.return_value = _mock_response(
            json_data={"data": {"listUCLAgents": []}}
        )

        runner = CliRunner()
        runner.invoke(cli, ["skills"])

        # Check _verbose_post was called with the right payload
        call_args = mock_post.call_args
        payload = call_args[1].get("payload") or call_args[0][2]
        assert "ListUCLAgents" in payload["query"]
        assert payload["variables"] == {"input": {"projectId": "my-project-123"}}
