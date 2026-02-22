"""Tests for the skills namespace (fastn.skills.list)."""

from __future__ import annotations

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

_SAMPLE_SKILLS = [
    {
        "id": "sk_001",
        "projectId": "proj_abc",
        "name": "Email Summarizer",
        "description": "Summarizes incoming emails and creates action items",
        "createdAt": "2025-01-15T10:00:00Z",
        "updatedAt": "2025-01-20T14:30:00Z",
        "__typename": "UCLAgent",
    },
    {
        "id": "sk_002",
        "projectId": "proj_abc",
        "name": "Slack Notifier",
        "description": "Posts notifications to Slack channels based on triggers",
        "createdAt": "2025-02-01T09:00:00Z",
        "updatedAt": "2025-02-10T11:00:00Z",
        "__typename": "UCLAgent",
    },
]


def _create_config_env(
    tmpdir: str,
    api_key: str | None = "test-api-key",
    project_id: str = "proj_abc",
) -> str:
    """Create a .fastn dir with config containing an api_key."""
    fastn_dir = Path(tmpdir) / ".fastn"
    fastn_dir.mkdir()

    config: dict = {
        "project_id": project_id,
        "stage": "LIVE",
    }
    if api_key:
        config["api_key"] = api_key

    (fastn_dir / "config.json").write_text(json.dumps(config))
    (fastn_dir / "registry.json").write_text(
        json.dumps({"version": "2025.02.14", "connectors": {}})
    )

    return str(fastn_dir / "config.json")


# ---------------------------------------------------------------------------
# Sync client tests
# ---------------------------------------------------------------------------


class TestSkillsSyncList:
    def test_list_success(self, httpx_mock: HTTPXMock):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_config_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={"data": {"listUCLAgents": _SAMPLE_SKILLS}},
            )

            result = client.skills.list()
            assert result == _SAMPLE_SKILLS
            assert len(result) == 2
            assert result[0]["id"] == "sk_001"
            assert result[0]["name"] == "Email Summarizer"
            assert result[1]["name"] == "Slack Notifier"
            client.close()

    def test_list_empty(self, httpx_mock: HTTPXMock):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_config_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={"data": {"listUCLAgents": []}},
            )

            result = client.skills.list()
            assert result == []
            client.close()

    def test_list_null_result(self, httpx_mock: HTTPXMock):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_config_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={"data": {"listUCLAgents": None}},
            )

            result = client.skills.list()
            assert result == []
            client.close()

    def test_list_no_credentials(self):
        """Client creation fails when no api_key or auth_token is set."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_config_env(tmpdir, api_key=None)
            with pytest.raises(ConfigError):
                FastnClient(config_path=config_path)

    def test_list_401(self, httpx_mock: HTTPXMock):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_config_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(url=GRAPHQL_URL, status_code=401)

            with pytest.raises(AuthError, match="Authentication failed"):
                client.skills.list()
            client.close()

    def test_list_500(self, httpx_mock: HTTPXMock):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_config_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                status_code=500,
                json={"error": "internal server error"},
            )

            with pytest.raises(APIError, match="500"):
                client.skills.list()
            client.close()

    def test_list_graphql_error(self, httpx_mock: HTTPXMock):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_config_env(tmpdir)
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={"errors": [{"message": "Unauthorized access"}]},
            )

            with pytest.raises(APIError, match="GraphQL error"):
                client.skills.list()
            client.close()

    def test_list_sends_correct_query(self, httpx_mock: HTTPXMock):
        """Verify the SDK sends the correct GraphQL query and variables."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_config_env(tmpdir, project_id="proj_xyz")
            client = FastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={"data": {"listUCLAgents": []}},
            )

            client.skills.list()

            request = httpx_mock.get_request()
            body = json.loads(request.content)
            assert "ListUCLAgents" in body["query"]
            assert body["variables"] == {"input": {"projectId": "proj_xyz"}}
            client.close()


# ---------------------------------------------------------------------------
# Async client tests
# ---------------------------------------------------------------------------


class TestSkillsAsyncList:
    @pytest.mark.anyio
    async def test_list_success(self, httpx_mock: HTTPXMock):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_config_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={"data": {"listUCLAgents": _SAMPLE_SKILLS}},
            )

            result = await client.skills.list()
            assert result == _SAMPLE_SKILLS
            assert len(result) == 2
            await client.close()

    @pytest.mark.anyio
    async def test_list_empty(self, httpx_mock: HTTPXMock):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_config_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={"data": {"listUCLAgents": []}},
            )

            result = await client.skills.list()
            assert result == []
            await client.close()

    @pytest.mark.anyio
    async def test_list_graphql_error(self, httpx_mock: HTTPXMock):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = _create_config_env(tmpdir)
            client = AsyncFastnClient(config_path=config_path)

            httpx_mock.add_response(
                url=GRAPHQL_URL,
                json={"errors": [{"message": "Something broke"}]},
            )

            with pytest.raises(APIError, match="GraphQL error"):
                await client.skills.list()
            await client.close()
