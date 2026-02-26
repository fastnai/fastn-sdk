"""Fastn Zapier connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ZapierConnector:
    """Zapier connector ().

    Provides 11 tools.
    """

    def get_actions(
        self,
        action_type: Optional[str] = None,
        app: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the available actions that can be performed within a specific application in your Zapier integration, guiding users in setting up Zaps effectively.

        Args:
            action_type: 
            app: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_apps_v1(
        self,
        client_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains a list of applications available in the legacy version of the Zapier integration, allowing users to access older application options.

        Args:
            client_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_apps_v2(
        self,
    ) -> Dict[str, Any]:
        """Obtains a list of available applications that can be integrated within your Zapier account, allowing you to explore potential automation options through Zapier.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_categories(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of categories available for applications within the Zapier ecosystem, helping you to navigate and organize integrations.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_choices(
        self,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of choices available for specific inputs in your Zapier integration, helping users make informed selections during Zap setup.

        Args:
            data: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_input_fields(
        self,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Fetches the input fields necessary for setting up actions in your Zapier integration, ensuring that all required data is captured.

        Args:
            data: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_profile(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the user profile information for the connected account in your Zapier integration, providing insights into the account details.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_zaps_v1(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of Zaps configured in your Zapier account for the Zapier integration.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_zaps_v2(
        self,
    ) -> Dict[str, Any]:
        """Fetches updated Zaps in your Zapier account, providing the latest information and settings for the Zapier integration.
        Returns:
            API response as a dictionary.
        """
        ...

    def guess_zap_beta(
        self,
        client_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Attempts to guess the Zap configuration based on the inputs provided, utilizing the Zapier integration to streamline your automation process.

        Args:
            client_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_zap(
        self,
    ) -> Dict[str, Any]:
        """Triggers a specific Zap to run immediately in your Zapier integration, initiating the predefined automation process.
        Returns:
            API response as a dictionary.
        """
        ...

