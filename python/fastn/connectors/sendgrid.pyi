"""Fastn SendGrid connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _SendgridCreateSenderIdentityFrom(TypedDict, total=False):
    email: str
    name: str

class _SendgridCreateSenderIdentityReplyTo(TypedDict, total=False):
    email: str
    name: str

class _SendgridSendEmailFrom(TypedDict, total=False):
    email: str
    name: str

class _SendgridUpdateSenderIdentityFrom(TypedDict, total=False):
    email: str
    name: str

class _SendgridUpdateSenderIdentityReplyTo(TypedDict, total=False):
    email: str
    name: str

class SendgridConnector:
    """SendGrid connector ().

    Provides 15 tools.
    """

    def sendgrid_cancel_or_pause_scheduled_send(
        self,
        batch_id: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Cancels or pauses a scheduled email send in SendGrid by associating a pause or cancel status with a batch ID. Use this tool before the scheduled send time to prevent or delay delivery. This action creates a scheduled send modification record. Do not use this tool to resume a send or to delete an existing pause/cancellation.

        Args:
            batch_id: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_create_batch(
        self,
    ) -> Dict[str, Any]:
        """Generates a new batch ID in SendGrid that can be assigned to a scheduled email send. Use this tool to obtain a batch ID before scheduling an email so that the send can later be paused or cancelled using that ID. Do not use this tool to send an email directly or to list existing batches.
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_create_sender_identity(
        self,
        Api_key: Optional[str] = None,
        address: Optional[str] = None,
        address_2: Optional[str] = None,
        city: Optional[str] = None,
        country: Optional[str] = None,
        from: Optional[_SendgridCreateSenderIdentityFrom] = None,
        nickname: Optional[str] = None,
        reply_to: Optional[_SendgridCreateSenderIdentityReplyTo] = None,
        state: Optional[str] = None,
        zip: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new sender identity in SendGrid with a specified from name and email address. Use this tool to register a new sender before using it in email campaigns. A verification email will be sent to the provided address. Do not use this tool to update an existing sender identity.

        Args:
            Api_key: 
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

    def sendgrid_delete_scheduled_send_cancellation(
        self,
        batchId: Optional[str] = None,
        scheduled_sends: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing cancellation or pause instruction from a scheduled email send in SendGrid, identified by its batch ID. Use this tool when you want to lift a previously applied pause or cancellation so the email send resumes as originally planned. This action is irreversible for the deleted instruction. Do not use this tool to cancel or pause a send.

        Args:
            batchId: 
            scheduled_sends: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_delete_sender_identity(
        self,
        senderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a sender identity from SendGrid, identified by its sender ID. Use this tool only when a sender identity must be fully removed from the account. This action is irreversible. Do not use this tool to update or temporarily disable a sender identity.

        Args:
            senderId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_filter_messages(
        self,
        messageId: str,
    ) -> Dict[str, Any]:
        """Filters messages based on specified criteria within SendGrid. Use this tool to search and retrieve email messages matching particular conditions such as status, date range, recipient, or sender. Returns matching message details including delivery status and metadata. Do not use this tool to retrieve a single message by ID.

        Args:
            messageId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_get_global_email_statistics(
        self,
        start_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves aggregated global email statistics from SendGrid for a specified date range, starting from the required start_date parameter. Use this tool to review account-wide metrics such as delivered, opened, clicked, bounced, and unsubscribed counts. Do not use this tool to retrieve statistics scoped to a specific category, subuser, or IP pool.

        Args:
            start_date: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_get_sender_identity(
        self,
        senderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific sender identity in SendGrid, identified by its sender ID. Use this tool to view the from name, reply-to address, verification status, and other fields for a single sender. Do not use this tool to retrieve all sender identities.

        Args:
            senderId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_list_scheduled_sends(
        self,
    ) -> Dict[str, Any]:
        """Lists all scheduled email sends that have an active pause or cancellation instruction in SendGrid. Use this tool to review which batch IDs have pending scheduled send modifications. Do not use this tool to retrieve general email send history or statistics.
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_list_sender_identities(
        self,
    ) -> Dict[str, Any]:
        """Lists all sender identities configured in SendGrid. Use this tool to retrieve sender names, email addresses, verification statuses, and IDs for all senders on the account. Do not use this tool to retrieve a single sender identity by ID.
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_resend_sender_identity_verification(
        self,
        senderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Resends the verification email for a specific sender identity in SendGrid, identified by its sender ID. Use this tool when a sender has not received or has lost the original verification email and needs it resent before the identity can be used to send mail. Do not use this tool to update or delete a sender identity.

        Args:
            senderId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_send_email(
        self,
        content: Optional[List[Any]] = None,
        from: Optional[_SendgridSendEmailFrom] = None,
        personalizations: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Sends a transactional or marketing email through SendGrid to one or more recipients. Use this tool to deliver a single email with specified subject, body, from address, and recipients. Supports dynamic template IDs, attachments, and scheduled sending via a batch ID. This action immediately queues the email for delivery and cannot be undone unless a batch ID with a scheduled send is used.

        Args:
            content: 
            from: 
            personalizations: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_update_scheduled_send(
        self,
        status: str,
        batchId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the cancellation or pause status of a scheduled email send in SendGrid, identified by its batch ID. Use this tool to modify an existing scheduled send pause or cancellation instruction. Do not use this tool to create a new scheduled send or to delete a pause/cancellation.

        Args:
            status:  (required)
            batchId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_update_sender_identity(
        self,
        address: Optional[str] = None,
        address_2: Optional[str] = None,
        city: Optional[str] = None,
        country: Optional[str] = None,
        from: Optional[_SendgridUpdateSenderIdentityFrom] = None,
        nickname: Optional[str] = None,
        reply_to: Optional[_SendgridUpdateSenderIdentityReplyTo] = None,
        senderId: Optional[str] = None,
        state: Optional[str] = None,
        zip: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing sender identity in SendGrid, identified by its sender ID. Use this tool to modify the from name, reply-to address, or other fields of a sender. Updating certain fields may require re-verification of the sender identity. Do not use this tool to create a new sender identity.

        Args:
            address: 
            address_2: 
            city: 
            country: 
            from: 
            nickname: 
            reply_to: 
            senderId: 
            state: 
            zip: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sendgrid_validate_batch_id(
        self,
        batchId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Validates that a SendGrid batch ID is valid and active. Use this tool to confirm a batch ID exists and is eligible for use in scheduled email sends before assigning it to a message. Do not use this tool to create a new batch ID or cancel a scheduled send.

        Args:
            batchId: 
        Returns:
            API response as a dictionary.
        """
        ...

