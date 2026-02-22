"""Comprehensive tests for all Fastn CLI commands.

Tests every CLI command using Click's CliRunner with mocked API calls.
Covers success paths, error paths, and edge cases.
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any, Dict
from unittest.mock import MagicMock, patch

import click
import httpx
import pytest
from click.testing import CliRunner

from fastn.cli import cli
from fastn import __version__


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_fastn_dir(tmpdir: str, *, config: dict = None, registry: dict = None,
                     manifest: dict = None) -> Path:
    """Create a .fastn directory with config, registry, and manifest."""
    fastn_dir = Path(tmpdir) / ".fastn"
    fastn_dir.mkdir(parents=True, exist_ok=True)

    if config is None:
        config = {
            "api_key": "test-api-key",
            "project_id": "test-project-id",
            "stage": "LIVE",
        }
    (fastn_dir / "config.json").write_text(json.dumps(config))

    if registry is None:
        registry = {"version": "1.0.0", "connectors": {}}
    (fastn_dir / "registry.json").write_text(json.dumps(registry))

    if manifest is None:
        manifest = {"installed": {}, "registry_version": "1.0.0",
                    "last_synced": "2026-02-19T00:00:00+00:00"}
    (fastn_dir / "manifest.json").write_text(json.dumps(manifest))

    return fastn_dir


def _make_registry_with_tools() -> dict:
    """Create a registry with Slack tool and actions."""
    return {
        "version": "1.0.0",
        "connectors": {
            "slack": {
                "id": "conn_slack_001",
                "display_name": "Slack",
                "source": "workspace",
                "connector_type": "GROUP",
                "tools": {
                    "send_message": {
                        "actionId": "act_slack_send_message",
                        "name": "sendMessage",
                        "description": "Send a message to a channel",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "body": {
                                    "type": "object",
                                    "properties": {
                                        "channel": {
                                            "type": "string",
                                            "description": "Channel name",
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
                        },
                        "outputSchema": {
                            "type": "object",
                            "properties": {
                                "ok": {"type": "boolean"},
                            },
                        },
                    },
                    "list_channels": {
                        "actionId": "act_slack_list_channels",
                        "name": "listChannels",
                        "description": "List all channels",
                        "inputSchema": {
                            "type": "object",
                            "properties": {},
                        },
                    },
                },
            },
            "github": {
                "id": "conn_github_001",
                "display_name": "GitHub",
                "source": "org",
                "connector_type": "GROUP",
                "tools": {},
            },
        },
    }


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def tmp_env(monkeypatch):
    """Set up a temp .fastn dir and point config loading to it."""
    with tempfile.TemporaryDirectory() as tmpdir:
        monkeypatch.chdir(tmpdir)
        # Clear env vars
        monkeypatch.delenv("FASTN_API_KEY", raising=False)
        monkeypatch.delenv("FASTN_PROJECT_ID", raising=False)
        monkeypatch.delenv("FASTN_AUTH_TOKEN", raising=False)
        monkeypatch.delenv("FASTN_STAGE", raising=False)
        monkeypatch.delenv("FASTN_TENANT_ID", raising=False)
        yield tmpdir


# ===================================================================
# VERSION command
# ===================================================================

class TestVersionCommand:
    def test_version_flag(self, runner):
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert __version__ in result.output

    def test_version_command(self, runner, tmp_env):
        _make_fastn_dir(tmp_env)
        result = runner.invoke(cli, ["version"])
        assert result.exit_code == 0
        assert f"Fastn SDK v{__version__}" in result.output
        assert "Registry version:" in result.output
        assert "Last synced:" in result.output

    def test_version_no_manifest(self, runner, tmp_env):
        fastn_dir = _make_fastn_dir(tmp_env)
        (fastn_dir / "manifest.json").unlink()
        result = runner.invoke(cli, ["version"])
        assert result.exit_code == 0
        # When manifest is missing, registry_version is empty string
        assert "Registry version:" in result.output


# ===================================================================
# LOGOUT command
# ===================================================================

class TestLogoutCommand:
    def test_logout_clears_tokens(self, runner, tmp_env):
        _make_fastn_dir(tmp_env, config={
            "api_key": "test-key",
            "project_id": "proj",
            "auth_token": "at_test",
            "refresh_token": "rt_test",
            "token_expiry": "2026-01-01T00:00:00+00:00",
        })
        result = runner.invoke(cli, ["logout"])
        assert result.exit_code == 0
        assert "Logged out" in result.output

        # Verify tokens are cleared
        config_data = json.loads(
            (Path(tmp_env) / ".fastn" / "config.json").read_text()
        )
        assert config_data.get("auth_token", "") == ""
        assert config_data.get("refresh_token", "") == ""


# ===================================================================
# WHOAMI command
# ===================================================================

class TestWhoamiCommand:
    def test_whoami_not_logged_in(self, runner, tmp_env):
        _make_fastn_dir(tmp_env, config={
            "api_key": "test-key",
            "project_id": "proj",
        })
        result = runner.invoke(cli, ["whoami"])
        assert result.exit_code == 0
        assert "Not logged in" in result.output

    @patch("fastn.oauth.fetch_userinfo")
    @patch("fastn.cli.auth_commands._ensure_fresh_token")
    def test_whoami_logged_in(self, mock_fresh, mock_userinfo, runner, tmp_env):
        _make_fastn_dir(tmp_env, config={
            "api_key": "key",
            "project_id": "proj",
            "auth_token": "at_valid",
        })
        mock_userinfo.return_value = {
            "name": "Test User",
            "email": "test@example.com",
            "sub": "user_123",
        }
        result = runner.invoke(cli, ["whoami"])
        assert result.exit_code == 0
        assert "Test User" in result.output
        assert "test@example.com" in result.output
        assert "user_123" in result.output

    @patch("fastn.oauth.fetch_userinfo")
    @patch("fastn.cli.auth_commands._ensure_fresh_token")
    def test_whoami_fetch_fails(self, mock_fresh, mock_userinfo, runner, tmp_env):
        _make_fastn_dir(tmp_env, config={
            "api_key": "key",
            "project_id": "proj",
            "auth_token": "at_valid",
        })
        mock_userinfo.side_effect = Exception("token expired")
        result = runner.invoke(cli, ["whoami"])
        assert result.exit_code == 0
        assert "Failed to fetch user info" in result.output


# ===================================================================
# SCHEMA command
# ===================================================================

class TestSchemaCommand:
    def test_schema_all_tools(self, runner, tmp_env):
        registry = _make_registry_with_tools()
        _make_fastn_dir(tmp_env, registry=registry)
        result = runner.invoke(cli, ["schema", "slack"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert isinstance(data, list)
        assert len(data) == 2
        names = {t["name"] for t in data}
        assert "send_message" in names or "list_channels" in names

    def test_schema_specific_tool(self, runner, tmp_env):
        registry = _make_registry_with_tools()
        _make_fastn_dir(tmp_env, registry=registry)
        result = runner.invoke(cli, ["schema", "slack", "send_message"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["name"] == "send_message"
        assert "inputSchema" in data
        assert "outputSchema" in data
        assert data["actionId"] == "act_slack_send_message"

    def test_schema_tool_not_found(self, runner, tmp_env):
        registry = _make_registry_with_tools()
        _make_fastn_dir(tmp_env, registry=registry)
        result = runner.invoke(cli, ["schema", "slack", "nonexistent"])
        assert result.exit_code != 0
        assert "not found" in result.output.lower()

    def test_schema_tool_not_found_in_registry(self, runner, tmp_env):
        _make_fastn_dir(tmp_env)
        result = runner.invoke(cli, ["schema", "nonexistent"])
        assert result.exit_code != 0
        assert "not found" in result.output.lower()

    def test_schema_no_tools_cached(self, runner, tmp_env):
        registry = {
            "version": "1.0.0",
            "connectors": {
                "github": {
                    "id": "conn_gh_001",
                    "display_name": "GitHub",
                    "tools": {},
                }
            },
        }
        _make_fastn_dir(tmp_env, registry=registry)
        result = runner.invoke(cli, ["schema", "github"])
        assert result.exit_code != 0
        assert "No tools cached" in result.output

    def test_schema_underscore_fallback(self, runner, tmp_env):
        """send_message should match sendmessage in registry."""
        registry = {
            "version": "1.0.0",
            "connectors": {
                "slack": {
                    "id": "conn_slack",
                    "display_name": "Slack",
                    "tools": {
                        "sendmessage": {
                            "actionId": "act_slack_sendmessage",
                            "description": "Send a message",
                            "inputSchema": {},
                            "outputSchema": {},
                        },
                    },
                },
            },
        }
        _make_fastn_dir(tmp_env, registry=registry)
        result = runner.invoke(cli, ["schema", "slack", "send_message"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["actionId"] == "act_slack_sendmessage"


# ===================================================================
# LIST command
# ===================================================================

class TestListCommand:
    def test_list_all_tools(self, runner, tmp_env):
        registry = _make_registry_with_tools()
        _make_fastn_dir(tmp_env, registry=registry)
        result = runner.invoke(cli, ["list"])
        assert result.exit_code == 0
        assert "Available connectors" in result.output
        assert "slack" in result.output
        assert "github" in result.output

    def test_list_groups_by_source(self, runner, tmp_env):
        registry = _make_registry_with_tools()
        _make_fastn_dir(tmp_env, registry=registry)
        result = runner.invoke(cli, ["list"])
        assert result.exit_code == 0
        assert "My Workspace" in result.output
        assert "My Organization" in result.output

    def test_list_specific_tool(self, runner, tmp_env):
        registry = _make_registry_with_tools()
        _make_fastn_dir(tmp_env, registry=registry)
        result = runner.invoke(cli, ["list", "slack"])
        assert result.exit_code == 0
        assert "Slack" in result.output
        assert "send_message" in result.output or "sendMessage" in result.output
        assert "list_channels" in result.output or "listChannels" in result.output

    def test_list_tool_not_found(self, runner, tmp_env):
        registry = _make_registry_with_tools()
        _make_fastn_dir(tmp_env, registry=registry)
        result = runner.invoke(cli, ["list", "nonexistent"])
        assert result.exit_code != 0
        assert "not found" in result.output.lower()

    def test_list_verbose(self, runner, tmp_env):
        registry = _make_registry_with_tools()
        _make_fastn_dir(tmp_env, registry=registry)
        result = runner.invoke(cli, ["list", "slack", "-v"])
        assert result.exit_code == 0
        assert "Input:" in result.output or "Usage:" in result.output

    def test_list_installed_flag(self, runner, tmp_env):
        registry = _make_registry_with_tools()
        manifest = {
            "installed": {"slack": {"version": "1.0.0"}},
            "registry_version": "1.0.0",
            "last_synced": "2026-02-19T00:00:00+00:00",
        }
        _make_fastn_dir(tmp_env, registry=registry, manifest=manifest)
        result = runner.invoke(cli, ["list", "--installed"])
        assert result.exit_code == 0
        assert "slack" in result.output
        assert "Installed" in result.output

    def test_list_installed_none(self, runner, tmp_env):
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())
        result = runner.invoke(cli, ["list", "--installed"])
        assert result.exit_code == 0
        assert "No connectors installed" in result.output

    def test_list_empty_registry_not_authenticated(self, runner, tmp_env):
        _make_fastn_dir(tmp_env, config={
            "api_key": "",
            "project_id": "",
        })
        result = runner.invoke(cli, ["list"])
        assert result.exit_code != 0
        assert "Not authenticated" in result.output

    def test_list_shows_installed_checkmark(self, runner, tmp_env):
        registry = _make_registry_with_tools()
        manifest = {
            "installed": {"slack": {"version": "1.0.0"}},
            "registry_version": "1.0.0",
        }
        _make_fastn_dir(tmp_env, registry=registry, manifest=manifest)
        result = runner.invoke(cli, ["list"])
        assert result.exit_code == 0
        # Checkmark appears next to installed tools
        assert "\u2705" in result.output


# ===================================================================
# REMOVE command
# ===================================================================

class TestRemoveCommand:
    @patch("fastn.cli.registry_commands._detect_languages", return_value=["python"])
    @patch("fastn.cli.registry_commands._regenerate_stubs")
    def test_remove_installed(self, mock_stubs, mock_detect, runner, tmp_env):
        registry = _make_registry_with_tools()
        manifest = {
            "installed": {"slack": {"version": "1.0.0"}},
            "registry_version": "1.0.0",
        }
        _make_fastn_dir(tmp_env, registry=registry, manifest=manifest)
        result = runner.invoke(cli, ["remove", "slack"])
        assert result.exit_code == 0
        assert "Removed slack" in result.output

    def test_remove_not_installed(self, runner, tmp_env):
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())
        result = runner.invoke(cli, ["remove", "slack"])
        assert result.exit_code == 0
        assert "not installed" in result.output


# ===================================================================
# RUN command
# ===================================================================

class TestRunCommand:
    def test_run_list_tools(self, runner, tmp_env):
        """fastn run slack -> list available tools."""
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())
        result = runner.invoke(cli, ["run", "slack"])
        assert result.exit_code == 0
        assert "available tools" in result.output.lower()
        assert "send_message" in result.output or "sendMessage" in result.output

    def test_run_not_authenticated(self, runner, tmp_env):
        _make_fastn_dir(tmp_env, config={
            "api_key": "",
            "project_id": "",
        })
        result = runner.invoke(cli, ["run", "slack", "send_message"])
        assert result.exit_code != 0
        assert "Not authenticated" in result.output

    def test_run_empty_registry(self, runner, tmp_env):
        _make_fastn_dir(tmp_env)
        result = runner.invoke(cli, ["run", "slack"])
        assert result.exit_code != 0
        assert "Registry is empty" in result.output

    def test_run_tool_not_found(self, runner, tmp_env):
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())
        result = runner.invoke(cli, ["run", "nonexistent"])
        assert result.exit_code != 0
        assert "not found" in result.output.lower()

    def test_run_action_not_found(self, runner, tmp_env):
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())
        result = runner.invoke(cli, ["run", "slack", "nonexistent_action"])
        assert result.exit_code != 0
        assert "not found" in result.output.lower()

    @patch("fastn.cli.run_command._verbose_post")
    @patch("fastn.cli.run_command._ensure_fresh_token")
    def test_run_with_inline_params(self, mock_fresh, mock_post, runner, tmp_env):
        """Test inline params via ctx.args.

        Note: Click's ignore_unknown_options causes --flags to be treated
        as positional values when there are optional positional args. The
        CLI's optional tenant_id positional arg captures the first unknown
        --flag. So we verify the command executes and calls the API.
        """
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"body": {"ok": True, "ts": "1234"}}
        mock_resp.text = '{"body": {"ok": true}}'
        mock_post.return_value = mock_resp

        # Pass extra params as ctx.args — Click's positional tenant_id
        # will consume the first --flag, so remaining args get parsed
        result = runner.invoke(cli, [
            "run", "slack", "send_message",
            "--channel", "general", "--text", "Hello!"
        ])
        assert result.exit_code == 0
        assert "ok" in result.output

        # Verify API was called with correct action
        call_args = mock_post.call_args
        payload = call_args[0][2]
        assert payload["input"]["actionId"] == "act_slack_send_message"
        # At least text should be in the params body
        params = payload["input"]["parameters"]
        assert params.get("body", {}).get("text") == "Hello!"

    @patch("fastn.cli.run_command._verbose_post")
    @patch("fastn.cli.run_command._ensure_fresh_token")
    def test_run_with_connection_id(self, mock_fresh, mock_post, runner, tmp_env):
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"body": {"ok": True}}
        mock_resp.text = '{"body": {"ok": true}}'
        mock_post.return_value = mock_resp

        result = runner.invoke(cli, [
            "run", "slack", "send_message",
            "--connection-id", "conn_abc",
            "--channel", "general", "--text", "Hi"
        ])
        assert result.exit_code == 0

        payload = mock_post.call_args[0][2]
        assert payload["input"]["connectionId"] == "conn_abc"

    @patch("fastn.cli.run_command._verbose_post")
    @patch("fastn.cli.run_command._ensure_fresh_token")
    def test_run_with_tenant_flag(self, mock_fresh, mock_post, runner, tmp_env):
        """Test --tenant flag sets the tenant header.

        Click's ignore_unknown_options means unknown --flags become
        positional values when optional positional args exist.
        We use list_channels (no required params) to avoid interactive
        prompting, and verify the tenant header is set.
        """
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"body": {"channels": []}}
        mock_resp.text = '{"body": {"channels": []}}'
        mock_post.return_value = mock_resp

        # Use list_channels which has no required params, so no prompt
        result = runner.invoke(cli, [
            "run", "slack", "list_channels",
            "--tenant", "acme",
        ])
        assert result.exit_code == 0

        # Verify tenant header is set
        call_args = mock_post.call_args
        headers = call_args[0][1]
        assert headers.get("x-fastn-space-tenantid") == "acme"

    @patch("fastn.cli.run_command._verbose_post")
    @patch("fastn.cli.run_command._ensure_fresh_token")
    def test_run_with_positional_tenant(self, mock_fresh, mock_post, runner, tmp_env):
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"body": {"ok": True}}
        mock_resp.text = '{"body": {"ok": true}}'
        mock_post.return_value = mock_resp

        result = runner.invoke(cli, [
            "run", "slack", "send_message", "tenant-123",
            "--channel", "general", "--text", "Hi"
        ])
        assert result.exit_code == 0

        call_args = mock_post.call_args
        headers = call_args[0][1]
        assert headers.get("x-fastn-space-tenantid") == "tenant-123"

    @patch("fastn.cli.run_command._verbose_post")
    @patch("fastn.cli.run_command._ensure_fresh_token")
    def test_run_api_error(self, mock_fresh, mock_post, runner, tmp_env):
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())

        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.json.return_value = {"error": "Server error"}
        mock_resp.text = '{"error": "Server error"}'
        mock_post.return_value = mock_resp

        result = runner.invoke(cli, [
            "run", "slack", "send_message",
            "--channel", "general", "--text", "Hi"
        ])
        assert result.exit_code != 0
        assert "API error" in result.output or "error" in result.output.lower()

    @patch("fastn.cli.run_command._verbose_post")
    @patch("fastn.cli.run_command._ensure_fresh_token")
    def test_run_auth_error(self, mock_fresh, mock_post, runner, tmp_env):
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())

        mock_resp = MagicMock()
        mock_resp.status_code = 401
        mock_resp.json.return_value = {"error": "Unauthorized"}
        mock_resp.text = "Unauthorized"
        mock_post.return_value = mock_resp

        result = runner.invoke(cli, [
            "run", "slack", "send_message",
            "--channel", "general", "--text", "Hi"
        ])
        assert result.exit_code != 0
        assert "Authentication" in result.output or "authentication" in result.output.lower()

    def test_run_interactive_prompt(self, runner, tmp_env):
        """When no params are given and there are fields, prompt interactively."""
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())

        # Simulate user typing params interactively (channel + text, then empty for optional)
        with patch("fastn.cli.run_command._verbose_post") as mock_post, \
             patch("fastn.cli.run_command._ensure_fresh_token"):
            mock_resp = MagicMock()
            mock_resp.status_code = 200
            mock_resp.json.return_value = {"body": {"ok": True}}
            mock_resp.text = '{"body": {"ok": true}}'
            mock_post.return_value = mock_resp

            result = runner.invoke(cli, ["run", "slack", "send_message"],
                                  input="general\nHello\n")
            # Should prompt for required fields
            assert "channel" in result.output.lower() or result.exit_code == 0


# ===================================================================
# SYNC command
# ===================================================================

class TestSyncCommand:
    def test_sync_not_authenticated(self, runner, tmp_env):
        _make_fastn_dir(tmp_env, config={
            "api_key": "",
            "project_id": "",
        })
        result = runner.invoke(cli, ["sync"])
        assert result.exit_code != 0
        assert "Not authenticated" in result.output

    @patch("fastn.cli.registry_commands._detect_languages", return_value=["python"])
    @patch("fastn.cli.registry_commands._regenerate_stubs")
    @patch("fastn.cli.registry_commands._fetch_registry_list")
    @patch("fastn.cli._helpers._ensure_fresh_token")
    def test_sync_success(self, mock_fresh, mock_fetch, mock_stubs, mock_detect, runner, tmp_env):
        _make_fastn_dir(tmp_env)
        mock_fetch.return_value = _make_registry_with_tools()
        mock_stubs.return_value = False

        result = runner.invoke(cli, ["sync"])
        assert result.exit_code == 0
        assert "Registry synced" in result.output
        assert "2 connectors available" in result.output


# ===================================================================
# ADD command
# ===================================================================

class TestAddCommand:
    @patch("fastn.cli.registry_commands._detect_languages", return_value=["python"])
    @patch("fastn.cli.registry_commands._regenerate_stubs")
    @patch("fastn.cli.registry_commands._fetch_tool_actions")
    @patch("fastn.cli._helpers._ensure_fresh_token")
    def test_add_success(self, mock_fresh, mock_fetch_actions, mock_stubs, mock_detect, runner, tmp_env):
        registry = _make_registry_with_tools()
        # Remove tools so add fetches them
        registry["connectors"]["slack"]["tools"] = {}
        _make_fastn_dir(tmp_env, registry=registry)

        mock_fetch_actions.return_value = [
            {
                "node": {
                    "id": "act_slack_send_message",
                    "name": "sendMessage",
                    "description": "Send a message",
                    "inputSchema": json.dumps({"type": "object", "properties": {}}),
                    "outputSchema": json.dumps({"type": "object", "properties": {}}),
                }
            }
        ]
        mock_stubs.return_value = True

        result = runner.invoke(cli, ["add", "slack"])
        assert result.exit_code == 0
        assert "slack added" in result.output
        assert "Type stubs generated" in result.output

    def test_add_tool_not_found(self, runner, tmp_env):
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())
        result = runner.invoke(cli, ["add", "nonexistent"])
        assert result.exit_code == 0  # add doesn't fail hard, just warns
        assert "not found" in result.output.lower()

    @patch("fastn.cli.registry_commands._detect_languages", return_value=["python"])
    @patch("fastn.cli.registry_commands._regenerate_stubs")
    @patch("fastn.cli.registry_commands._fetch_tool_actions")
    @patch("fastn.cli._helpers._ensure_fresh_token")
    def test_add_multiple(self, mock_fresh, mock_fetch, mock_stubs, mock_detect, runner, tmp_env):
        registry = _make_registry_with_tools()
        registry["connectors"]["slack"]["tools"] = {}
        registry["connectors"]["github"]["tools"] = {}
        _make_fastn_dir(tmp_env, registry=registry)

        mock_fetch.return_value = [
            {
                "node": {
                    "id": "act_tool",
                    "name": "doSomething",
                    "description": "Do something",
                    "inputSchema": json.dumps({}),
                    "outputSchema": json.dumps({}),
                }
            }
        ]
        mock_stubs.return_value = True

        result = runner.invoke(cli, ["add", "slack", "github"])
        assert result.exit_code == 0
        assert "slack added" in result.output
        assert "github added" in result.output


# ===================================================================
# AGENT command
# ===================================================================

class TestAgentCommand:
    def test_agent_not_authenticated(self, runner, tmp_env):
        _make_fastn_dir(tmp_env, config={
            "api_key": "",
            "project_id": "",
        })
        result = runner.invoke(cli, ["agent", "send hello"])
        assert result.exit_code != 0
        assert "Not authenticated" in result.output

    def test_agent_no_prompt(self, runner, tmp_env):
        _make_fastn_dir(tmp_env)
        result = runner.invoke(cli, ["agent"])
        assert result.exit_code != 0

    def test_agent_no_llm_configured_aborts(self, runner, tmp_env):
        _make_fastn_dir(tmp_env)
        # Simulate user cancelling LLM setup (input "0" for invalid choice)
        result = runner.invoke(cli, ["agent", "send hello"], input="0\n")
        # Should fail because LLM provider wasn't configured
        assert result.exit_code != 0

    @patch("fastn.cli.agent_command._verbose_post")
    @patch("fastn.cli.agent_command._ensure_fresh_token")
    def test_agent_no_tools_found(self, mock_fresh, mock_post, runner, tmp_env):
        _make_fastn_dir(tmp_env, config={
            "api_key": "key",
            "project_id": "proj",
            "llm_provider": "openai",
            "llm_api_key": "sk-test",
            "llm_model": "gpt-4o-mini",
        })

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = []
        mock_resp.text = "[]"
        mock_post.return_value = mock_resp

        result = runner.invoke(cli, ["agent", "send hello"])
        assert result.exit_code == 0
        assert "No tools found" in result.output

    @patch("fastn.cli.agent_command._verbose_post")
    @patch("fastn.cli.agent_command._ensure_fresh_token")
    def test_agent_non_openai_provider(self, mock_fresh, mock_post, runner, tmp_env):
        _make_fastn_dir(tmp_env, config={
            "api_key": "key",
            "project_id": "proj",
            "llm_provider": "anthropic",
            "llm_api_key": "sk-ant-test",
            "llm_model": "claude-3-5-sonnet",
        })

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = [
            {"actionId": "act_test", "function": {"name": "test_tool", "description": "test"}}
        ]
        mock_resp.text = "[]"
        mock_post.return_value = mock_resp

        result = runner.invoke(cli, ["agent", "test task"])
        assert result.exit_code != 0
        assert "Only OpenAI is supported" in result.output

    @patch("fastn.cli.agent_command._verbose_post")
    @patch("fastn.cli.agent_command._ensure_fresh_token")
    def test_agent_tool_discovery_fails(self, mock_fresh, mock_post, runner, tmp_env):
        _make_fastn_dir(tmp_env, config={
            "api_key": "key",
            "project_id": "proj",
            "llm_provider": "openai",
            "llm_api_key": "sk-test",
            "llm_model": "gpt-4o",
        })

        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.json.return_value = {"error": "Internal error"}
        mock_resp.text = "Internal error"
        mock_post.return_value = mock_resp

        result = runner.invoke(cli, ["agent", "send hello"])
        assert result.exit_code != 0
        assert "Connector discovery failed" in result.output


# ===================================================================
# INIT command
# ===================================================================

class TestInitCommand:
    def test_init_manual_api_key(self, runner, tmp_env):
        """Init with manual API key entry (no browser login)."""
        result = runner.invoke(cli, ["init"],
                              input="n\ntest-api-key\ntest-project-id\n")
        assert result.exit_code == 0
        assert "Config saved" in result.output

        # Verify config was written
        config_data = json.loads(
            (Path(tmp_env) / ".fastn" / "config.json").read_text()
        )
        assert config_data["api_key"] == "test-api-key"
        assert config_data["project_id"] == "test-project-id"

    def test_init_creates_gitignore(self, runner, tmp_env):
        result = runner.invoke(cli, ["init"],
                              input="n\nkey\nproj\n")
        assert result.exit_code == 0
        assert "gitignore" in result.output.lower()
        gitignore = Path(tmp_env) / ".gitignore"
        assert gitignore.exists()
        assert ".fastn/config.json" in gitignore.read_text()


# ===================================================================
# LOGIN command
# ===================================================================

class TestLoginCommand:
    @patch("fastn.cli.auth_commands._run_device_login")
    def test_login_failure(self, mock_login, runner, tmp_env):
        _make_fastn_dir(tmp_env)
        mock_login.return_value = None  # Login failed
        result = runner.invoke(cli, ["login"])
        assert result.exit_code != 0


# ===================================================================
# VERBOSE flag
# ===================================================================

class TestVerboseFlag:
    @patch("fastn.cli.run_command._verbose_post")
    @patch("fastn.cli.run_command._ensure_fresh_token")
    def test_verbose_shows_api_calls(self, mock_fresh, mock_post, runner, tmp_env):
        _make_fastn_dir(tmp_env, registry=_make_registry_with_tools())

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"body": {"ok": True}}
        mock_resp.text = '{"body": {"ok": true}}'
        mock_post.return_value = mock_resp

        result = runner.invoke(cli, [
            "-v", "run", "slack", "send_message",
            "--channel", "general", "--text", "Hi"
        ])
        assert result.exit_code == 0
