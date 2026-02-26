"""Fastn Google Chat connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GoogleChatConnector:
    """Google Chat connector ().

    Provides 3 tools.
    """

    def get_space(
        self,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific space from the workspace connector, providing information about its configuration and settings.

        Args:
            spaceId: ID of the Google Chat space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_spaces(
        self,
        pageSize: Optional[str] = None,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all available spaces through the workspace connector, enabling users to view and select from multiple workspaces.

        Args:
            pageSize: Number of results to return per page in the Google Chat API.
            pageToken: Token for retrieving the next page of results in the Google Chat API.
        Returns:
            API response as a dictionary.
        """
        ...

    def send_message(
        self,
        messageId: Optional[str] = None,
        requestId: Optional[str] = None,
        threadKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a message using the messaging connector, allowing users to communicate directly within the application.

        Args:
            messageId: Identifier for the message.
            requestId: Unique identifier for the request.
            threadKey: Key identifying the conversation thread.
        Returns:
            API response as a dictionary.
        """
        ...

