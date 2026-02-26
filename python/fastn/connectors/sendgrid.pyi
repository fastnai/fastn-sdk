"""Fastn SendGrid connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SendgridConnector:
    """SendGrid connector ().

    Provides 15 tools.
    """

    def cancel_or_pause_scheduled_send(
        self,
        batch_id: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Cancels or pauses a scheduled email send operation using the scheduling connector.

        Args:
            batch_id: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_batch(
        self,
    ) -> Dict[str, Any]:
        """Creates a batch of messages for processing using the batch management connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sender_identity(
        self,
    ) -> Dict[str, Any]:
        """Creates a new sender identity within the email connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_cancellation_pause_from_scheduled_send(
        self,
    ) -> Dict[str, Any]:
        """Deletes the cancellation or pause from a scheduled send using the scheduling connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_sender_identity(
        self,
        senderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified sender identity from the email connector.

        Args:
            senderId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def filter_messages(
        self,
        messageId: str,
    ) -> Dict[str, Any]:
        """Filters messages based on specified criteria within the messaging connector.

        Args:
            messageId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_sender_identities(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all sender identities associated with the email connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_scheduled_sends(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of scheduled sends within the scheduling connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def resend_sender_identitiy_verification(
        self,
        senderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Resends the verification request for a sender identity in the email connector.

        Args:
            senderId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def retrieve_global_email_statistics(
        self,
        start_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves global email statistics using the statistics reporting connector.

        Args:
            start_date: 
        Returns:
            API response as a dictionary.
        """
        ...

    def send_email(
        self,
        content: Optional[List[Any]] = None,
        from: Optional[Dict[str, Any]] = None,
        personalizations: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Sends an email to a specified recipient using the email connector.

        Args:
            content: 
            from: 
            personalizations: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_scheduled_send(
        self,
        batchId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates parameters of a scheduled send in the scheduling connector.

        Args:
            batchId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_sender_identity(
        self,
        address: Optional[str] = None,
        address_2: Optional[str] = None,
        city: Optional[str] = None,
        country: Optional[str] = None,
        from: Optional[Dict[str, Any]] = None,
        nickname: Optional[str] = None,
        reply_to: Optional[Dict[str, Any]] = None,
        state: Optional[str] = None,
        zip: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the sender identity information in the email connector.

        Args:
            address: 
            address_2: 
            city: 
            country: 
            from: 
            nickname: 
            reply_to: 
            state: 
            zip: 
        Returns:
            API response as a dictionary.
        """
        ...

    def validate_batch_id(
        self,
        batchId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Validates a batch ID within the batch management connector.

        Args:
            batchId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def view_sender_identity(
        self,
        senderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Views details of a specific sender identity in the email connector.

        Args:
            senderId: 
        Returns:
            API response as a dictionary.
        """
        ...

