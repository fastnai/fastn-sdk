"""Fastn Instagram connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class InstagramConnector:
    """Instagram connector ().

    Provides 2 tools.
    """

    def convert_short_lived_token_to_long_lived_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        fb_exchange_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Converts a short-lived authentication token into a long-lived token within the designated authentication system, enabling extended user sessions without needing to re-authenticate frequently.

        Args:
            client_id: 
            client_secret: 
            fb_exchange_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves user information from the specified system to provide detailed data about the user's profile and settings.
        Returns:
            API response as a dictionary.
        """
        ...

