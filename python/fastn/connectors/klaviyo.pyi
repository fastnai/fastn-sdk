"""Fastn Klaviyo connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _KlaviyoAssignCampaignMessageTemplateData(TypedDict, total=False):
    relationships: Dict[str, Any]
    type: str

class _KlaviyoCreateCampaignData(TypedDict, total=False):
    attributes: Dict[str, Any]
    type: str

class _KlaviyoCreateCampaignRecipientEstimationJobData(TypedDict, total=False):
    id: str
    type: str

class _KlaviyoCreateCampaignSendJobData(TypedDict, total=False):
    id: str
    type: str

class _KlaviyoCreateListData(TypedDict, total=False):
    attributes: Dict[str, Any]
    type: str

class _KlaviyoUpdateCampaignData(TypedDict, total=False):
    attributes: Dict[str, Any]
    id: str
    type: str

class _KlaviyoUpdateCampaignMessageData(TypedDict, total=False):
    attributes: Dict[str, Any]
    type: str

class _KlaviyoUpdateCampaignSendJobData(TypedDict, total=False):
    attributes: Dict[str, Any]
    id: str
    type: str

class _KlaviyoUpdateListData(TypedDict, total=False):
    attributes: Dict[str, Any]
    id: str
    type: str

class _KlaviyoUpdateSegmentData(TypedDict, total=False):
    attributes: Dict[str, Any]
    id: str
    type: str

class KlaviyoConnector:
    """Klaviyo connector ().

    Provides 24 tools.
    """

    def klaviyo_assign_campaign_message_template(
        self,
        data: _KlaviyoAssignCampaignMessageTemplateData,
    ) -> Dict[str, Any]:
        """Assigns an existing template to a specific Klaviyo campaign message, replacing any previously assigned template. Use this to link a pre-built email template to a campaign message before sending. This overwrites the current template assignment for the target message.

        Args:
            data: Data payload for the Klaviyo API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_create_campaign(
        self,
        data: _KlaviyoCreateCampaignData,
    ) -> Dict[str, Any]:
        """Creates a new campaign in Klaviyo with the specified configuration, such as name, audience, and channel. Use this to set up a new email or SMS campaign before adding messages and scheduling a send. Do not use this to send the campaign; use create_campaign_send_job after the campaign is fully configured.

        Args:
            data: Campaign data. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_create_campaign_recipient_estimation_job(
        self,
        data: _KlaviyoCreateCampaignRecipientEstimationJobData,
    ) -> Dict[str, Any]:
        """Creates a recipient estimation job for a specific Klaviyo campaign to calculate how many recipients will receive the campaign. Use this before sending a campaign to get a projected audience size. This triggers an asynchronous background job; use the corresponding get tool to poll for results. Does not send the campaign.

        Args:
            data: The main data object for the Klaviyo API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_create_campaign_send_job(
        self,
        data: _KlaviyoCreateCampaignSendJobData,
    ) -> Dict[str, Any]:
        """Creates a send job that queues a specific Klaviyo campaign for delivery to its recipients. Use this to initiate the sending process for a campaign that has been fully configured. This triggers an asynchronous send operation; the campaign will be dispatched to all targeted recipients. This action is irreversible once the send job is underway.

        Args:
            data: Data payload for the Klaviyo API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_create_list(
        self,
        data: _KlaviyoCreateListData,
    ) -> Dict[str, Any]:
        """Creates a new contact list in Klaviyo with the specified name and configuration. Use this to set up a new list for organizing profiles or targeting campaigns. Do not use this to update an existing list; use update_list instead. The new list will initially have no members.

        Args:
            data: Main data object for the Klaviyo API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_delete_campaign(
        self,
        campaignId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific Klaviyo campaign, identified by its campaign ID. Use this only when the campaign is no longer needed. This action is irreversible — the campaign and all associated configuration will be permanently removed. Do not use this on campaigns that have already been sent or are currently sending.

        Args:
            campaignId: The ID of the Klaviyo campaign. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_delete_list(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific Klaviyo contact list, identified by its list ID. Use this only when the list is no longer needed. This action is irreversible — the list and its membership data will be permanently removed. This does not delete the profiles within the list, only the list itself.

        Args:
            listId: The ID of the list to target. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_get_account(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Klaviyo account, identified by its account ID, including settings and configuration. Use this to inspect a single accounts details. Do not use this to list all accounts; use list_accounts instead.

        Args:
            accountId: Your Klaviyo account ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_get_campaign(
        self,
        campaignId: str,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Klaviyo campaign, identified by its campaign ID, with optional filtering parameters. Use this to inspect the configuration, status, and metadata of a single campaign. Do not use this to list multiple campaigns; use list_campaigns instead.

        Args:
            campaignId: The ID of the Klaviyo campaign. (required)
            filter: Filter criteria for the Klaviyo API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_get_campaign_message(
        self,
        messagesId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific message associated with a Klaviyo campaign, including its content, template, and configuration, identified by the message ID. Use this to inspect a single campaign message. Do not use this to list all messages for a campaign; use list_campaign_messages instead.

        Args:
            messagesId: ID of the message. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_get_campaign_recipient_estimation_job(
        self,
        messagesId: str,
    ) -> Dict[str, Any]:
        """Retrieves the status and results of a recipient estimation job for a specific Klaviyo campaign, identified by its job ID. Use this to poll an estimation job created via the create_campaign_recipient_estimation_job tool and retrieve the projected recipient count once the job completes. Do not use this to retrieve send job status; use get_campaign_send_job instead.

        Args:
            messagesId: ID of the message to retrieve. Required for this endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_get_campaign_send_job(
        self,
        messagesId: str,
    ) -> Dict[str, Any]:
        """Retrieves the current status and details of a specific Klaviyo campaign send job, identified by its job ID. Use this to monitor the progress or outcome of a send job initiated via create_campaign_send_job. Do not use this to retrieve recipient estimation job status; use get_campaign_recipient_estimation_job instead.

        Args:
            messagesId: ID of the message to retrieve from Klaviyo. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_get_segment(
        self,
        segmentId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Klaviyo segment, identified by its segment ID, including its definition and metadata. Use this to inspect a single segments configuration. Do not use this to list all segments; use list_segments instead.

        Args:
            segmentId: The ID of the Klaviyo segment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_list_accounts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all Klaviyo accounts accessible with the current API credentials. Use this to enumerate available accounts. Do not use this to retrieve details about a specific account; use get_account instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_list_campaign_messages(
        self,
        campaignId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all messages associated with a specific Klaviyo campaign, identified by the campaign ID. Use this to enumerate messages within a campaign. Do not use this to retrieve details about a single message; use get_campaign_message instead.

        Args:
            campaignId: ID of the Klaviyo campaign. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_list_campaign_tags(
        self,
        campaignId: str,
    ) -> Dict[str, Any]:
        """Retrieves all tags associated with a specific Klaviyo campaign, identified by the campaign ID. Use this to inspect the tags applied to a campaign for filtering or organizational purposes. Do not use this to retrieve campaign details; use get_campaign instead.

        Args:
            campaignId: The ID of the Klaviyo campaign. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_list_campaigns(
        self,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of Klaviyo campaigns, with support for filtering by status, channel, or other criteria via the filter parameter. Use this to enumerate campaigns for review or management. Do not use this to retrieve details about a single campaign; use get_campaign instead.

        Args:
            filter: Filter parameters for the Klaviyo API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_list_lists(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all contact lists defined in Klaviyo. Use this to enumerate available lists for targeting, review, or management. Do not use this to retrieve details about a single list or to list segments; use get_segment or list_segments for segments.
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_list_segments(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all segments defined in Klaviyo. Use this to enumerate available segments for targeting or review. Do not use this to retrieve details about a single segment; use get_segment instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_update_campaign(
        self,
        campaignId: str,
        data: _KlaviyoUpdateCampaignData,
    ) -> Dict[str, Any]:
        """Updates the configuration or metadata of an existing Klaviyo campaign, identified by its campaign ID. Use this to modify campaign name, audience, scheduling, or other settings before the campaign is sent. Do not use this to send the campaign; use create_campaign_send_job instead.

        Args:
            campaignId: ID of the campaign. (required)
            data: Campaign data. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_update_campaign_message(
        self,
        data: _KlaviyoUpdateCampaignMessageData,
        messagesId: str,
    ) -> Dict[str, Any]:
        """Updates the content or configuration of a specific Klaviyo campaign message, identified by its message ID. Use this to modify subject lines, preview text, or other message-level properties before a campaign is sent. Do not use this to assign or swap templates; use assign_campaign_message_template instead.

        Args:
            data: Data payload for the Klaviyo API request. (required)
            messagesId: ID of the message. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_update_campaign_send_job(
        self,
        data: _KlaviyoUpdateCampaignSendJobData,
        messagesId: str,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing Klaviyo campaign send job, such as cancelling a scheduled send. Use this to modify or cancel a send job that has not yet completed. Do not use this to create a new send job; use create_campaign_send_job instead. Changes to an in-progress send may not be reversible.

        Args:
            data: Data payload for the Klaviyo API request. (required)
            messagesId: ID of the message. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_update_list(
        self,
        data: _KlaviyoUpdateListData,
        listId: str,
    ) -> Dict[str, Any]:
        """Updates the properties of an existing Klaviyo contact list, such as its name, identified by its list ID. Use this to rename or reconfigure a list. Do not use this to add or remove members from a list. Does not affect profiles already subscribed to the list.

        Args:
            data: The main data object for the request. (required)
            listId: ID of the Klaviyo list. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def klaviyo_update_segment(
        self,
        data: _KlaviyoUpdateSegmentData,
        segmentId: str,
    ) -> Dict[str, Any]:
        """Updates the configuration or metadata of an existing Klaviyo segment, identified by its segment ID. Use this to rename a segment or modify its definition. Do not use this to create a new segment. Changes to a segments definition will affect all campaigns and flows that reference it.

        Args:
            data: Data payload for the Klaviyo API. (required)
            segmentId: ID of the Klaviyo segment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

