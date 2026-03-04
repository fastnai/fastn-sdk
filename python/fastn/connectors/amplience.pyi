"""Fastn Amplience connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AmplienceConnector:
    """Amplience connector ().

    Provides 3 tools.
    """

    def amplience_generate_access_token(
        self,
        client_credentials: str,
        client_id: str,
        client_secret: str,
    ) -> Dict[str, Any]:
        """Generates an OAuth 2.0 access token from Ampliences authorization service for authenticating subsequent Amplience API requests. Use this tool to obtain or refresh an access token before making API calls that require authorization. Do not use this tool to retrieve or manage content items.

        Args:
            client_credentials:  (required)
            client_id:  (required)
            client_secret:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def amplience_get_content_item(
        self,
        access_Token: str,
        contentItemId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single content item from Amplience by its content item ID, including its metadata, schema, and content fields. Use this tool when you need to inspect or work with a specific content item. Do not use this tool to retrieve multiple content items — use amplience_list_content_items instead.

        Args:
            access_Token:  (required)
            contentItemId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def amplience_list_content_items(
        self,
        access_Token: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of content items from Amplience, returning their metadata and content fields. Use this tool when you need to browse or enumerate multiple content items across the platform. Do not use this tool to retrieve a single content item by ID — use amplience_get_content_item instead.

        Args:
            access_Token:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

