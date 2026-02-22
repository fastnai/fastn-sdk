"""Tests for the projects namespace (fastn.projects.list)."""

from __future__ import annotations

import base64
import json
import tempfile
from pathlib import Path

import pytest
from pytest_httpx import HTTPXMock

from fastn.client import AsyncFastnClient, FastnClient, GRAPHQL_URL
from fastn.exceptions import APIError, AuthError, ConfigError


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_jwt(payload: dict) -> str:
    """Build a fake 3-part JWT with the given payload (no signature)."""
    header = base64.urlsafe_b64encode(json.dumps({"alg": "none"}).encode()).rstrip(b"=").decode()
    body = base64.urlsafe_b64encode(json.dumps(payload).encode()).rstrip(b"=").decode()
    return f"{header}.{body}.fakesig"


_SAMPLE_PROJECTS = [
    {"id": "proj_001", "name": "My Project", "packageType": "free"},
    {"id": "proj_002", "name": "Team Project", "packageType": "pro"},
]


def _create_auth_env(tmpdir: str, auth_token: str | None = None) -> str:
    """Create a .fastn dir with config containing an auth_token."""
    fastn_dir = Path(tmpdir) / ".fastn"
    fastn_dir.mkdir()

    config: dict = {
        "project_id": "test-project-id",
        "stage": "LIVE",
    }
    if auth_token:
        config["auth_token"] = auth_token

    (fastn_dir / "config.json").write_text(json.dumps(config))
    (fastn_dir / "registry.json").write_text(json.dumps({
        "version": "2025.02.14",
        "connectors": {},
    }))

    return str(fastn_dir / "config.json")


# ---------------------------------------------------------------------------
# Sync client tests
# ---------------------------------------------------------------------------

class TestProjectsSyncList:
    def test_list_success(self, httpx_mock: HTTPXMock):
        token = _make_jwt({"sub": "user123"})
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_auth_env(tmpdir, auth_token=token)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={
                    "data": {
                        "getOrganizations": _SAMPLE_PROJECTS,
                    }
                },
            )

            result = client.projects.list()
            assert result == _SAMPLE_PROJECTS
            assert len(result) == 2
            assert result[0]["id"] == "proj_001"
            client.close()

    def test_list_no_auth_token(self):
        """Client creation itself fails when no auth_token or api_key is set."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_auth_env(tmpdir, auth_token=None)
            with pytest.raises(ConfigError):
                FastnClient(config_path=config_path)

    def test_list_token_no_sub(self):
        token = _make_jwt({"aud": "some-aud"})  # no "sub" claim
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_auth_env(tmpdir, auth_token=token)
            client = FastnClient(config_path=config_path)

            with pytest.raises(AuthError, match="user ID"):
                client.projects.list()
            client.close()

    def test_list_401(self, httpx_mock: HTTPXMock):
        token = _make_jwt({"sub": "user123"})
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_auth_env(tmpdir, auth_token=token)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(url=GRAPHQL_URL, status_code=401)

            with pytest.raises(AuthError, match="Authentication failed"):
                client.projects.list()
            client.close()

    def test_list_500(self, httpx_mock: HTTPXMock):
        token = _make_jwt({"sub": "user123"})
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_auth_env(tmpdir, auth_token=token)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL, status_code=500, json={"error": "boom"},
            )

            with pytest.raises(APIError, match="500"):
                client.projects.list()
            client.close()

    def test_list_graphql_error(self, httpx_mock: HTTPXMock):
        token = _make_jwt({"sub": "user123"})
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_auth_env(tmpdir, auth_token=token)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={"errors": [{"message": "Unauthorized access"}]},
            )

            with pytest.raises(APIError, match="GraphQL error"):
                client.projects.list()
            client.close()

    def test_list_empty_result(self, httpx_mock: HTTPXMock):
        token = _make_jwt({"sub": "user123"})
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_auth_env(tmpdir, auth_token=token)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={"data": {"getOrganizations": []}},
            )

            result = client.projects.list()
            assert result == []
            client.close()


# ---------------------------------------------------------------------------
# Async client tests
# ---------------------------------------------------------------------------

class TestProjectsAsyncList:
    @pytest.mark.anyio
    async def test_list_success(self, httpx_mock: HTTPXMock):
        token = _make_jwt({"sub": "user123"})
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_auth_env(tmpdir, auth_token=token)
            client = AsyncFastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={
                    "data": {
                        "getOrganizations": _SAMPLE_PROJECTS,
                    }
                },
            )

            result = await client.projects.list()
            assert result == _SAMPLE_PROJECTS
            assert len(result) == 2
            await client.close()

    @pytest.mark.anyio
    async def test_list_no_auth_token(self):
        """Client creation itself fails when no auth_token or api_key is set."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_auth_env(tmpdir, auth_token=None)
            with pytest.raises(ConfigError):
                AsyncFastnClient(config_path=config_path)

    @pytest.mark.anyio
    async def test_list_graphql_error(self, httpx_mock: HTTPXMock):
        token = _make_jwt({"sub": "user123"})
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_auth_env(tmpdir, auth_token=token)
            client = AsyncFastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={"errors": [{"message": "Something broke"}]},
            )

            with pytest.raises(APIError, match="GraphQL error"):
                await client.projects.list()
            await client.close()
