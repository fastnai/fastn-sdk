"""Fastn Microsoft Dynamics 365 Sales Hub connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MicrosoftDynamics365SalesHubConnector:
    """Microsoft Dynamics 365 Sales Hub connector ().

    Provides 2 tools.
    """

    def create_contact(
        self,
        allow_duplicates: bool,
    ) -> Dict[str, Any]:
        """Creates a new contact in the contacts management connector.

        Args:
            allow_duplicates: Flag indicating whether duplicate entries are allowed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_auth_token_with_password_credentials(
        self,
        clientId: str,
        client_id: str,
        password: str,
        scope: str,
        username: str,
    ) -> Dict[str, Any]:
        """Generates an authentication token using password credentials in the authentication connector.

        Args:
            clientId: The client ID associated with the application making the request. (required)
            client_id: The identifier for the client application requesting authentication. (required)
            password: The password of the user for authentication. (required)
            scope: The scope of the authorization request, defining access levels. (required)
            username: The username of the user for authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

