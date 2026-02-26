"""Fastn Klaviyo connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class KlaviyoConnector:
    """Klaviyo connector ().

    Provides 24 tools.
    """

    def assign_campaign_message_template(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Assigns a message template to a specified campaign message in the marketing platform.

        Args:
            data: Data payload for the Klaviyo API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_campaign_recipient_estimation_job(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new recipient estimation job for a specific campaign in the marketing platform.

        Args:
            data: The main data object for the Klaviyo API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_campaign_send_job(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new send job for a specific campaign in the marketing platform.

        Args:
            data: Data payload for the Klaviyo API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_compaigns(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new campaign in the marketing platform.

        Args:
            data: Campaign data. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_list(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new contact list in the marketing platform.

        Args:
            data: Main data object for the Klaviyo API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_campaign(
        self,
        campaignId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified campaign from the marketing platform.

        Args:
            campaignId: The ID of the Klaviyo campaign. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_list(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified contact list from the marketing platform.

        Args:
            listId: The ID of the list to target. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_account(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific account in the marketing platform.

        Args:
            accountId: Your Klaviyo account ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_accounts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of accounts associated with the marketing platform.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_campaign(
        self,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific campaign in the marketing platform.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_campaign_message(
        self,
        messagesId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific message associated with a campaign in the marketing platform.

        Args:
            messagesId: ID of the message. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_campaign_messages(
        self,
        campaignId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of messages associated with a specific campaign in the marketing platform.

        Args:
            campaignId: ID of the Klaviyo campaign. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_campaign_recipient_estimation_job(
        self,
        messagesId: str,
    ) -> Dict[str, Any]:
        """Retrieves information about a campaign's recipient estimation job in the marketing platform.

        Args:
            messagesId: ID of the message to retrieve. Required for this endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_campaign_send_job(
        self,
        messagesId: str,
    ) -> Dict[str, Any]:
        """Retrieves details about a campaign's send job in the marketing platform.

        Args:
            messagesId: ID of the message to retrieve from Klaviyo. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_campaign_tag(
        self,
        campaignId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific tag associated with a campaign in the marketing platform.

        Args:
            campaignId: The ID of the Klaviyo campaign. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_campaigns(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of campaigns from the marketing platform.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_lists(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of contact lists from the marketing platform.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_segment(
        self,
        segmentId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific segment in the marketing platform.

        Args:
            segmentId: The ID of the Klaviyo segment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_segments(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of segments from the marketing platform.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_campaign(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates an existing campaign in the marketing platform.

        Args:
            data: Campaign data. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_campaign_message(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates a specific message associated with a campaign in the marketing platform.

        Args:
            data: Data payload for the Klaviyo API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_campaign_send_job(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates the information for a specific campaign send job in the marketing platform.

        Args:
            data: Data payload for the Klaviyo API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_list(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates an existing contact list in the marketing platform.

        Args:
            data: The main data object for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_segment(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates a specified segment in the marketing platform.

        Args:
            data: Data payload for the Klaviyo API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

