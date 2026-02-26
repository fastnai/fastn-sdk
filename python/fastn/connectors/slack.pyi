"""Fastn Slack connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SlackConnector:
    """Slack connector ().

    Provides 2 tools.
    """

    def list_channels(
        self,
    ) -> Dict[str, Any]:
        """List all channels
        Returns:
            API response as a dictionary.
        """
        ...

    def send_message(
        self,
        channel: str,
        text: str,
    ) -> Dict[str, Any]:
        """Send a message to a channel

        Args:
            channel: Channel name (required)
            text: Message text (required)
        Returns:
            API response as a dictionary.
        """
        ...

