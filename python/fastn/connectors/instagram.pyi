"""Fastn Instagram connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class InstagramConnector:
    """Instagram connector ().

    Provides 2 tools.
    """

    def instagram_convert_short_lived_token_to_long_lived_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        fb_exchange_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exchanges a short-lived Instagram OAuth access token (valid for ~1 hour) for a long-lived access token (valid for up to 60 days) via the Facebook Graph API. Use this immediately after initial OAuth authorization to extend the session and avoid frequent re-authentication. Do not use this if you already have a valid long-lived token.

        Args:
            client_id: 
            client_secret: 
            fb_exchange_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def instagram_get_user_info(
        self,
        comma_seperated_fields: Optional[str] = None,
        userId: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves profile information for a specific Instagram user by their user ID via the Facebook Graph API, including fields such as name, biography, and account details. Use this to fetch user profile metadata. Requires a valid access token with appropriate permissions. Do not use this to retrieve media, insights, or account metrics.

        Args:
            comma_seperated_fields: 
            userId: 
            username: 
        Returns:
            API response as a dictionary.
        """
        ...

