"""Fastn Ampliance connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AmplianceConnector:
    """Ampliance connector ().

    Provides 3 tools.
    """

    def access_token(
        self,
        client_credentials: str,
        client_id: str,
        client_secret: str,
    ) -> Dict[str, Any]:
        """Retrieves an access token for authorization in integrations requiring secure API access.

        Args:
            client_credentials:  (required)
            client_id:  (required)
            client_secret:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_content_items(
        self,
        access_Token: str,
    ) -> Dict[str, Any]:
        """Fetches a collection of content items from the specified content management system or database.

        Args:
            access_Token:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_single_content_item(
        self,
        access_Token: str,
        contentItemId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single content item from the content management system or database.

        Args:
            access_Token:  (required)
            contentItemId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

