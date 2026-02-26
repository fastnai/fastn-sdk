"""Fastn Typeform connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TypeformConnector:
    """Typeform connector ().

    Provides 12 tools.
    """

    def create_form(
        self,
        fields: List[Any],
        settings: Dict[str, Any],
        title: str,
    ) -> Dict[str, Any]:
        """Creates a new form for data collection in the system.

        Args:
            fields:  (required)
            settings: Settings for the Typeform. (required)
            title: Title of the Typeform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_or_update_webhook(
        self,
        enabled: bool,
        event: str,
        url: str,
    ) -> Dict[str, Any]:
        """Creates or updates a webhook to listen for specific events in the system.

        Args:
            enabled: Indicates whether the webhook is enabled or disabled. (required)
            event: Type of event being sent to Typeform. (required)
            url: URL to receive webhook notifications from Typeform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_form(
        self,
        form_id: str,
    ) -> Dict[str, Any]:
        """Deletes a specified form from the system.

        Args:
            form_id: The ID of the Typeform form to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_responses(
        self,
        included_response_ids: str,
    ) -> Dict[str, Any]:
        """Deletes specified responses from a form in the system.

        Args:
            included_response_ids: Comma-separated list of response IDs to include in the results. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        form_id: str,
        tag: str,
    ) -> Dict[str, Any]:
        """Deletes a specified webhook from the system.

        Args:
            form_id: The unique identifier of the Typeform form. (required)
            tag: A tag associated with the Typeform form. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_form(
        self,
        form_id: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific form in the system.

        Args:
            form_id: The unique identifier of the Typeform form. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_forms(
        self,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all forms available in the system.

        Args:
            page: The page number to retrieve.
            page_size: The number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_responses(
        self,
        form_id: str,
    ) -> Dict[str, Any]:
        """Fetches all responses submitted for a particular form in the system.

        Args:
            form_id: The ID of the Typeform form. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_single_webhook(
        self,
        form_id: str,
        my_webhook_tag: str,
    ) -> Dict[str, Any]:
        """Retrieves information about a single webhook in the system.

        Args:
            form_id: ID of the Typeform form associated with this webhook. (required)
            my_webhook_tag: Unique identifier for the webhook within Typeform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves user information from the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhooks(
        self,
        form_id: str,
    ) -> Dict[str, Any]:
        """Fetches a list of all webhooks set up in the system.

        Args:
            form_id: ID of the Typeform form to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_form(
        self,
        fields: List[Any],
        settings: Dict[str, Any],
        title: str,
    ) -> Dict[str, Any]:
        """Updates an existing form with new details in the system.

        Args:
            fields:  (required)
            settings: Form settings for the Typeform. (required)
            title: Title of the Typeform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

