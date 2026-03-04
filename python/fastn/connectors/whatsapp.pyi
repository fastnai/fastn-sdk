"""Fastn Whatsapp connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _WhatsappCreateTemplateTypes(TypedDict, total=False):
    twilio_quick_reply: Dict[str, Any]
    twilio_text: Dict[str, Any]

class _WhatsappCreateTemplateVariables(TypedDict, total=False):
    _1: str

class WhatsappConnector:
    """Whatsapp connector ().

    Provides 6 tools.
    """

    def whatsapp_create_template(
        self,
        friendly_name: str,
        language: str,
        types: _WhatsappCreateTemplateTypes,
        variables: Optional[_WhatsappCreateTemplateVariables] = None,
    ) -> Dict[str, Any]:
        """Creates a new WhatsApp message template in Twilio Content API for use in future messaging campaigns or automated notifications. Use this tool when you need to define a reusable message structure before submitting it for WhatsApp approval. Note: the template must be submitted for approval via whatsapp_submit_approval before it can be used in business-initiated messages. This operation creates a persistent resource.

        Args:
            friendly_name: A user-friendly name for the message. (required)
            language: Language of the message. (required)
            types: Different types of messages supported. (required)
            variables: Variables to be used within the message.
        Returns:
            API response as a dictionary.
        """
        ...

    def whatsapp_get_approval_status(
        self,
        twilioContentSid: str,
    ) -> Dict[str, Any]:
        """Retrieves the current approval status of a WhatsApp template submission identified by its Twilio Content SID. Use this tool to check whether a previously submitted template is pending, approved, or rejected by WhatsApp. Do not use this tool to submit a new approval request; use whatsapp_submit_approval for that. This operation is read-only and has no side effects.

        Args:
            twilioContentSid: The Twilio Content SID for the Whatsapp message. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def whatsapp_get_template(
        self,
        twilioContentSid: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of an existing WhatsApp message template from the Twilio Content API by its Content SID. Use this tool to inspect a templates structure, variables, and metadata before using or submitting it. Do not use this tool to list all templates or to check approval status; use dedicated tools for those purposes. This operation is read-only and has no side effects.

        Args:
            twilioContentSid: Twilio Content SID for identifying the message. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def whatsapp_send_business_initiated_message(
        self,
        ContentSid: str,
        ContentVariables: Dict[str, Any],
        From: str,
        To: str,
        twilioAccountSid: str,
        MediaUrl: Optional[str] = None,
        StatusCallback: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a proactive WhatsApp message from the business to a user via the Twilio Messaging API, using a pre-approved message template. Use this tool for automated notifications, alerts, or marketing messages initiated outside of a user-started conversation. Requires a WhatsApp-approved template; do not use this tool for free-form replies within an active user session — use whatsapp_send_user_initiated_message for that. Sending a message is irreversible.

        Args:
            ContentSid: Content SID for tracking the message (optional). (required)
            ContentVariables: Variables for personalized messages (optional). (required)
            From: Whatsapp number sending the message. (required)
            To: Whatsapp number receiving the message. (required)
            twilioAccountSid: Twilio Account SID. (required)
            MediaUrl: URL of the media to be sent (optional).
            StatusCallback: URL for status callbacks (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def whatsapp_send_user_initiated_message(
        self,
        body: str,
        from: str,
        to: str,
        twilioAccountSid: str,
        MediaUrl: Optional[str] = None,
        StatusCallback: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a WhatsApp message in reply to a user-initiated conversation via the Twilio Messaging API. Use this tool when responding to an inbound message from a user within the active 24-hour WhatsApp messaging window. Do not use this tool to send outbound messages outside of an active user session; use whatsapp_send_business_initiated_message for proactive outreach instead. Sending a message is irreversible.

        Args:
            body: Text content of the message. (required)
            from: Whatsapp phone number of the sender. (required)
            to: Whatsapp phone number of the recipient. (required)
            twilioAccountSid: Twilio Account SID if using Twilio for Whatsapp integration. (required)
            MediaUrl: URL of the media to be sent (optional).
            StatusCallback: URL to receive message status updates (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def whatsapp_submit_approval(
        self,
        category: str,
        name: str,
        twilioContentSid: str,
    ) -> Dict[str, Any]:
        """Submits a WhatsApp template approval request to Meta via Twilio for a content item identified by its Twilio Content SID. Use this tool when a newly created message template needs to go through WhatsApps compliance review before it can be used in business-initiated messages. This action initiates a review process; approval is not immediate. Do not use this tool to check the status of an existing submission; use whatsapp_get_approval_status for that.

        Args:
            category: Category of the message. (required)
            name: Recipient's name. (required)
            twilioContentSid: Twilio Content SID for the message. (required)
        Returns:
            API response as a dictionary.
        """
        ...

