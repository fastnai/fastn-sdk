"""Fastn Zapier connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _GetChoicesZapierData(TypedDict, total=False):
    authentication: str
    inputs: Dict[str, Any]

class _GetInputFieldsZapierData(TypedDict, total=False):
    authentication: str
    inputs: Dict[str, Any]
    limit: int
    offset: int

class ZapierConnector:
    """Zapier connector ().

    Provides 11 tools.
    """

    def get_actions_zapier(
        self,
        action_type: Optional[str] = None,
        app: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the actions available for selected apps in Zapier. Use this to define what automated tasks can be performed in your workflows.

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

    def get_apps_v2_zapier(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of apps available in your Zapier account for automating workflows. Use this to discover new integrations within Zapier.
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

    def get_choices_zapier(
        self,
        actionId: Optional[str] = None,
        data: Optional[_GetChoicesZapierData] = None,
        inputId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves available choices for input fields when configuring actions in Zapier. Use this to ensure correct selections in your automated workflows.

        Args:
            actionId: 
            data: 
            inputId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_input_fields_zapier(
        self,
        actionId: Optional[str] = None,
        data: Optional[_GetInputFieldsZapierData] = None,
    ) -> Dict[str, Any]:
        """Fetches the input fields required for actions in Zapier. This helps in setting up the necessary information for automated workflows.

        Args:
            actionId: 
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
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Attempts to guess the Zap configuration based on the inputs provided, utilizing the Zapier integration to streamline your automation process.

        Args:
            client_id: 
            description: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_zap(
        self,
        body: Dict[str, Any],
        zapHook: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Triggers a specific Zap to run immediately in your Zapier integration, initiating the predefined automation process.

        Args:
            body:  (required)
            zapHook: 
        Returns:
            API response as a dictionary.
        """
        ...

