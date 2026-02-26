"""Fastn Power Automate connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class PowerAutomateConnector:
    """Power Automate connector ().

    Provides 3 tools.
    """

    def create_custom_connector(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a custom connector in the specified integration system by providing a name and description for the connector.

        Args:
            expand: Expansion parameters for related data.
            filter: Filter criteria for data retrieval.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_access_token(
        self,
        client_id: str,
        client_secret: str,
        password: str,
        username: str,
    ) -> Dict[str, Any]:
        """Fetches an access token for authenticating requests to the specified integration system, enabling secure API interactions.

        Args:
            client_id: Client ID for Power Automate OAuth 2.0 flow. (required)
            client_secret: Client secret for Power Automate OAuth 2.0 flow. (required)
            password: User's password for Power Automate authentication. (required)
            username: Username for Power Automate authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_enviornment(
        self,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the environment details for the specified integration system, providing information on the current operational context.

        Args:
            expand: Expansion parameters for the Power Automate request.
            filter: Filter criteria for the Power Automate request.
        Returns:
            API response as a dictionary.
        """
        ...

