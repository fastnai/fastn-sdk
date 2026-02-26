"""Fastn SDK — auto-generated type stubs.

This file provides IDE autocomplete for all connectors.
Do not edit manually. Regenerate with `fastn sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from .connectors.github import GithubConnector
from .connectors.slack import SlackConnector


class FastnClient:
    """Fastn SDK client with typed connector access."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        project_id: Optional[str] = None,
        timeout: Optional[float] = None,
        config_path: Optional[str] = None,
        auth_token: Optional[str] = None,
        agent_id: Optional[str] = None,
        max_retries: int = 3,
        verbose: bool = False,
    ) -> None: ...

    @property
    def github(self) -> GithubConnector:
        """GitHub () — run `fastn connector add github` to fetch tools"""
        ...
    @property
    def slack(self) -> SlackConnector:
        """Slack ()"""
        ...

    def get_tools(self, connector_name: str) -> List[str]:
        """List available tool names for a connector."""
        ...

    def get_tool(self, connector_name: str, tool_name: str) -> Dict[str, Any]:
        """Get schema info for a specific tool."""
        ...


class AsyncFastnClient:
    """Async Fastn SDK client with typed connector access."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        project_id: Optional[str] = None,
        timeout: Optional[float] = None,
        config_path: Optional[str] = None,
        auth_token: Optional[str] = None,
        agent_id: Optional[str] = None,
        max_retries: int = 3,
        verbose: bool = False,
    ) -> None: ...

    @property
    def github(self) -> GithubConnector:
        """GitHub () — run `fastn connector add github` to fetch tools"""
        ...
    @property
    def slack(self) -> SlackConnector:
        """Slack ()"""
        ...

    async def get_tools(self, connector_name: str) -> List[str]:
        """List available tool names for a connector."""
        ...

    async def get_tool(self, connector_name: str, tool_name: str) -> Dict[str, Any]:
        """Get schema info for a specific tool."""
        ...
