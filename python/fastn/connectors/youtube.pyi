"""Fastn Youtube connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class YoutubeConnector:
    """Youtube connector ().

    Provides 1 tools.
    """

    def get_channel_info(
        self,
        categoryId: str,
        forUsername: str,
        hl: str,
        id: str,
        key: str,
        managedByMe: str,
        maxResults: str,
        mine: str,
        mySubscribers: str,
        onBehalfOfContentOwner: str,
        pageToken: str,
        part: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific channel in the context of the platform's API.

        Args:
            categoryId: The ID of the category to filter results by. (required)
            forUsername: Retrieve resources associated with a specific username. (required)
            hl: Specifies the preferred language for the response. (required)
            id: The unique identifier of the resource. (required)
            key: API Key for authentication. (required)
            managedByMe: Filter results to only include resources managed by the authenticated user. (required)
            maxResults: The maximum number of items to return. (required)
            mine: Filter results to only include resources owned by the authenticated user. (required)
            mySubscribers: Filter results to only include subscribers of the authenticated user. (required)
            onBehalfOfContentOwner: The ID of the content owner acting on behalf of the user. (required)
            pageToken: A token identifying a specific page of results. (required)
            part: Specifies the parts of the resource to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

