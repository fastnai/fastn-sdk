"""Tests for Fastn SDK configuration."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

import pytest

from fastn.config import (
    FastnConfig,
    add_connector_to_manifest,
    ensure_gitignore,
    get_installed_connectors,
    load_config,
    load_manifest,
    load_registry,
    remove_connector_from_manifest,
    save_config,
    save_manifest,
    save_registry,
)
from fastn.exceptions import ConfigError


class TestFastnConfig:
    def test_validate_success(self) -> None:
        config = FastnConfig(
            api_key="test-key",
            project_id="test-project",
        )
        config.validate()  # Should not raise

    def test_validate_missing_fields(self) -> None:
        config = FastnConfig()
        with pytest.raises(ConfigError, match="Missing required config fields"):
            config.validate()

    def test_validate_partial(self) -> None:
        config = FastnConfig(api_key="test")
        with pytest.raises(ConfigError, match="project_id"):
            config.validate()

    def test_to_dict(self) -> None:
        config = FastnConfig(
            api_key="key",
            project_id="project",
        )
        d = config.to_dict()
        assert d["api_key"] == "key"
        assert d["project_id"] == "project"

    def test_get_headers(self) -> None:
        config = FastnConfig(
            api_key="key",
            project_id="project",
        )
        headers = config.get_headers()
        assert headers["x-fastn-api-key"] == "key"
        assert headers["x-fastn-space-id"] == "project"
        assert headers["Content-Type"] == "application/json"
        assert headers["realm"] == "fastn"

    def test_validate_with_auth_token_instead_of_api_key(self) -> None:
        config = FastnConfig(
            auth_token="jwt-token",
        )
        config.validate()  # Should not raise — auth_token replaces api_key + project_id

    def test_validate_neither_api_key_nor_auth_token(self) -> None:
        config = FastnConfig(
            project_id="test-project",
        )
        with pytest.raises(ConfigError, match="api_key"):
            config.validate()

    def test_to_dict_includes_tokens(self) -> None:
        config = FastnConfig(
            api_key="key",
            project_id="project",
            auth_token="at_123",
            refresh_token="rt_456",
            token_expiry="2026-01-01T00:00:00+00:00",
        )
        d = config.to_dict()
        assert d["auth_token"] == "at_123"
        assert d["refresh_token"] == "rt_456"
        assert d["token_expiry"] == "2026-01-01T00:00:00+00:00"

    def test_to_dict_omits_empty_tokens(self) -> None:
        config = FastnConfig(api_key="key", project_id="project")
        d = config.to_dict()
        assert "auth_token" not in d
        assert "refresh_token" not in d
        assert "token_expiry" not in d

    def test_get_headers_with_auth_token(self) -> None:
        config = FastnConfig(
            api_key="key",
            project_id="project",
            auth_token="jwt-token-123",
        )
        headers = config.get_headers()
        assert headers["Authorization"] == "Bearer jwt-token-123"

    def test_get_headers_without_auth_token(self) -> None:
        config = FastnConfig(
            api_key="key",
            project_id="project",
        )
        headers = config.get_headers()
        assert "Authorization" not in headers


class TestEnvVarConfig:
    def test_env_vars_override_file(self, monkeypatch) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            fastn_dir = Path(tmpdir) / ".fastn"
            fastn_dir.mkdir()
            file_config = {
                "api_key": "file-key",
                "project_id": "file-project",
            }
            (fastn_dir / "config.json").write_text(json.dumps(file_config))

            monkeypatch.setenv("FASTN_API_KEY", "env-key")
            monkeypatch.setenv("FASTN_PROJECT_ID", "env-project")

            loaded = load_config(str(fastn_dir / "config.json"))
            assert loaded.api_key == "env-key"
            assert loaded.project_id == "env-project"

    def test_env_auth_token(self, monkeypatch) -> None:
        monkeypatch.setenv("FASTN_AUTH_TOKEN", "my-jwt")
        loaded = load_config("/nonexistent/path/config.json")
        assert loaded.auth_token == "my-jwt"

    def test_env_stage(self, monkeypatch) -> None:
        monkeypatch.setenv("FASTN_STAGE", "DEV")
        loaded = load_config("/nonexistent/path/config.json")
        assert loaded.stage == "DEV"

    def test_env_stage_overrides_file(self, monkeypatch) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            fastn_dir = Path(tmpdir) / ".fastn"
            fastn_dir.mkdir()
            file_config = {
                "api_key": "key",
                "project_id": "project",
                "stage": "STAGING",
            }
            (fastn_dir / "config.json").write_text(json.dumps(file_config))

            monkeypatch.setenv("FASTN_STAGE", "DEV")
            loaded = load_config(str(fastn_dir / "config.json"))
            assert loaded.stage == "DEV"

    def test_stage_defaults_to_live(self) -> None:
        loaded = load_config("/nonexistent/path/config.json")
        assert loaded.stage == "LIVE"


class TestConfigTokenRoundtrip:
    def test_save_and_load_with_tokens(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config = FastnConfig(
                api_key="key",
                project_id="project",
                auth_token="at_saved",
                refresh_token="rt_saved",
                token_expiry="2026-06-01T12:00:00+00:00",
            )
            save_config(config, tmpdir)

            loaded = load_config(str(Path(tmpdir) / ".fastn" / "config.json"))
            assert loaded.auth_token == "at_saved"
            assert loaded.refresh_token == "rt_saved"
            assert loaded.token_expiry == "2026-06-01T12:00:00+00:00"


class TestConfigIO:
    def test_save_and_load(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config = FastnConfig(
                api_key="test-key",
                project_id="test-project",
            )
            save_config(config, tmpdir)

            loaded = load_config(str(Path(tmpdir) / ".fastn" / "config.json"))
            assert loaded.api_key == "test-key"
            assert loaded.project_id == "test-project"

    def test_load_nonexistent(self) -> None:
        config = load_config("/nonexistent/path/config.json")
        assert config.api_key == ""

    def test_save_creates_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            config = FastnConfig(api_key="test")
            filepath = save_config(config, tmpdir)
            assert filepath.exists()

    def test_save_restricts_permissions(self) -> None:
        """Config file should be owner-only (0o600) to protect secrets."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = FastnConfig(api_key="secret-key")
            filepath = save_config(config, tmpdir)
            mode = os.stat(filepath).st_mode & 0o777
            assert mode == 0o600


class TestManifest:
    def test_save_and_load(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            fastn_dir = Path(tmpdir) / ".fastn"
            fastn_dir.mkdir()
            manifest = {
                "registry_version": "2025.02.14",
                "last_synced": "2025-02-14T10:00:00Z",
                "sdk": "python",
                "installed": {},
            }
            save_manifest(manifest, fastn_dir)
            loaded = load_manifest(fastn_dir)
            assert loaded["registry_version"] == "2025.02.14"

    def test_load_nonexistent(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            fastn_dir = Path(tmpdir) / ".fastn"
            fastn_dir.mkdir()
            loaded = load_manifest(fastn_dir)
            assert loaded["installed"] == {}

    def test_add_connector(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            fastn_dir = Path(tmpdir) / ".fastn"
            fastn_dir.mkdir()
            add_connector_to_manifest("slack", "2025.02.14", fastn_dir)
            installed = get_installed_connectors(fastn_dir)
            assert "slack" in installed

    def test_remove_connector(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            fastn_dir = Path(tmpdir) / ".fastn"
            fastn_dir.mkdir()
            add_connector_to_manifest("slack", "2025.02.14", fastn_dir)
            assert remove_connector_from_manifest("slack", fastn_dir) is True
            assert "slack" not in get_installed_connectors(fastn_dir)

    def test_remove_nonexistent(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            fastn_dir = Path(tmpdir) / ".fastn"
            fastn_dir.mkdir()
            assert remove_connector_from_manifest("slack", fastn_dir) is False


class TestRegistry:
    def test_save_and_load(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            fastn_dir = Path(tmpdir) / ".fastn"
            fastn_dir.mkdir()
            registry = {
                "version": "2025.02.14",
                "connectors": {
                    "slack": {
                        "display_name": "Slack",
                        "category": "communication",
                        "tools": {
                            "send_message": {
                                "actionId": "act_slack_send_message",
                            }
                        },
                    }
                },
            }
            save_registry(registry, fastn_dir)
            loaded = load_registry(fastn_dir)
            assert "slack" in loaded["connectors"]

    def test_load_nonexistent(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            fastn_dir = Path(tmpdir) / ".fastn"
            fastn_dir.mkdir()
            loaded = load_registry(fastn_dir)
            assert loaded["connectors"] == {}


class TestGitignore:
    def test_creates_gitignore(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            ensure_gitignore(tmpdir)
            gitignore = Path(tmpdir) / ".gitignore"
            assert gitignore.exists()
            assert ".fastn/config.json" in gitignore.read_text()

    def test_appends_to_existing(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            gitignore = Path(tmpdir) / ".gitignore"
            gitignore.write_text("node_modules/\n")
            ensure_gitignore(tmpdir)
            content = gitignore.read_text()
            assert "node_modules/" in content
            assert ".fastn/config.json" in content

    def test_no_duplicate(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            gitignore = Path(tmpdir) / ".gitignore"
            gitignore.write_text(".fastn/config.json\n")
            ensure_gitignore(tmpdir)
            content = gitignore.read_text()
            assert content.count(".fastn/config.json") == 1
