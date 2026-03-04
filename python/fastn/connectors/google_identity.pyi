"""Fastn Google Identity connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class GoogleIdentityConnector:
    """Google Identity connector ().

    Provides 2 tools.
    """

    def google_identity_get_openid_configuration(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the OpenID Connect discovery document from Google Identity, which contains essential provider metadata including the issuer URL, authorization endpoint, token endpoint, JWKS URI, and supported scopes. Use this to configure an OpenID Connect client or validate Google as an identity provider. This is a public, unauthenticated endpoint. Read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_identity_get_user_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves profile information for the currently authenticated user from Google Identity using an OAuth 2.0 access token. Returns user attributes such as name, email address, profile picture URL, and subject identifier. Use this after a user has authenticated via Google OAuth to obtain their identity details. Requires a valid Bearer token with the openid scope. Read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

