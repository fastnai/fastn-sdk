"""Fastn Google Chat connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _GoogleChatSendMessageThread(TypedDict, total=False):
    threadKey: str

class GoogleChatConnector:
    """Google Chat connector ().

    Provides 3 tools.
    """

    def google_chat_get_space(
        self,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Google Chat space identified by spaceId, including its display name, type, and configuration settings. Use this tool when you need metadata about a single known space. Do not use this tool to list all available spaces — use google_chat_list_spaces for that. This is a read-only operation and does not modify the space.

        Args:
            spaceId: ID of the Google Chat space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_chat_list_spaces(
        self,
        pageSize: Optional[str] = None,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all Google Chat spaces (rooms and direct messages) accessible to the authenticated user or service account. Use this tool when you need to discover available spaces before sending messages or retrieving space details. Do not use this tool to retrieve details of a single space — use google_chat_get_space for that. This is a read-only operation and does not modify any spaces.

        Args:
            pageSize: Number of results to return per page in the Google Chat API.
            pageToken: Token for retrieving the next page of results in the Google Chat API.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_chat_send_message(
        self,
        spaceId: str,
        text: str,
        cardsV2: Optional[List[Any]] = None,
        messageId: Optional[str] = None,
        requestId: Optional[str] = None,
        thread: Optional[_GoogleChatSendMessageThread] = None,
        threadKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a text or card message to a specific Google Chat space or conversation identified by spaceId. Use this tool when you need to post a notification, alert, or conversational message to a Google Chat space. Do not use this tool to retrieve messages or list spaces — use google_chat_list_spaces or google_chat_get_space for those. Sending a message is a write operation and will be visible to all members of the target space.

        Args:
            spaceId: Unique identifier for the Google Chat space. (required)
            text: Plain text message content. (required)
            cardsV2: 
            messageId: Identifier for the message.
            requestId: Unique identifier for the request.
            thread: Thread information for the message.
            threadKey: Key identifying the conversation thread.
        Returns:
            API response as a dictionary.
        """
        ...

