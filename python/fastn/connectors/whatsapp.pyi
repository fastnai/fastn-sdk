"""Fastn Whatsapp connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class WhatsappConnector:
    """Whatsapp connector ().

    Provides 6 tools.
    """

    def business_initiated_message(
        self,
        ContentSid: str,
        ContentVariables: Dict[str, Any],
        From: str,
        To: str,
        MediaUrl: Optional[str] = None,
        StatusCallback: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a message initiated by the business using the specified messaging platform, allowing for automated notifications or marketing communication.

        Args:
            ContentSid: Content SID for tracking the message (optional). (required)
            ContentVariables: Variables for personalized messages (optional). (required)
            From: Whatsapp number sending the message. (required)
            To: Whatsapp number receiving the message. (required)
            MediaUrl: URL of the media to be sent (optional).
            StatusCallback: URL for status callbacks (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def create_template(
        self,
        friendly_name: str,
        language: str,
        types: Dict[str, Any],
        variables: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new message template in the specified messaging platform, enabling customization for future messages.

        Args:
            friendly_name: A user-friendly name for the message. (required)
            language: Language of the message. (required)
            types: Different types of messages supported. (required)
            variables: Variables to be used within the message.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_approval_status(
        self,
        twilioContentSid: str,
    ) -> Dict[str, Any]:
        """Checks the status of an approval request in the specified messaging platform, providing insights into whether the request is pending, approved, or rejected.

        Args:
            twilioContentSid: The Twilio Content SID for the Whatsapp message. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_template(
        self,
        twilioContentSid: str,
    ) -> Dict[str, Any]:
        """Retrieves a pre-existing message template from the specified messaging platform, allowing for consistent communication formats.

        Args:
            twilioContentSid: Twilio Content SID for identifying the message. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def user_initiated_message(
        self,
        body: str,
        from: str,
        to: str,
        MediaUrl: Optional[str] = None,
        StatusCallback: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a message that is initiated by a user through the specified messaging platform, enabling user interactions and responses.

        Args:
            body: Text content of the message. (required)
            from: Whatsapp phone number of the sender. (required)
            to: Whatsapp phone number of the recipient. (required)
            MediaUrl: URL of the media to be sent (optional).
            StatusCallback: URL to receive message status updates (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def whatsapp_approval_submission(
        self,
        category: str,
        name: str,
    ) -> Dict[str, Any]:
        """Submits a request for approval regarding a template or message in the specified messaging platform, facilitating the compliance process.

        Args:
            category: Category of the message. (required)
            name: Recipient's name. (required)
        Returns:
            API response as a dictionary.
        """
        ...

