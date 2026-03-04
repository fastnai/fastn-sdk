"""Fastn Microsoft Outlook connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _MicrosoftOutlookSendEmailMessage(TypedDict, total=False):
    body: Dict[str, Any]
    ccRecipients: List[Any]
    subject: str
    toRecipients: List[Any]

class MicrosoftOutlookConnector:
    """Microsoft Outlook connector ().

    Provides 3 tools.
    """

    def microsoft_outlook_get_email(
        self,
        mailId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single email by its ID, including full content and metadata such as sender, subject, date, body, and attachments. Use this when the user asks to view a specific email, read email details, or when you have an email ID and need its complete information. Do not use this to list or retrieve multiple emails; use microsoft_outlook_list_emails instead.

        Args:
            mailId: Mail ID for the My connectors API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_outlook_list_emails(
        self,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of emails from the authenticated users mailbox, including basic metadata such as sender, subject, date, and a preview of the message body. Use this when the user asks to see their emails, view the inbox, check recent messages, or browse all emails in the mailbox. Do not use this to retrieve a single email by ID; use microsoft_outlook_get_email instead.

        Args:
            select: Specifies the fields to select in the Microsoft Outlook API response.
            skip: Specifies the number of records to skip in the Microsoft Outlook API response.
            top: Specifies the number of records to return in the Microsoft Outlook API response.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_outlook_send_email(
        self,
        message: Optional[_MicrosoftOutlookSendEmailMessage] = None,
        saveToSentItems: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends an email to one or more recipients with a specified subject and body content. Use this when the user wants to send, compose, or dispatch a new email. This action immediately delivers the email to all specified recipients and cannot be undone once sent. Do not use this to retrieve, list, or read existing emails; use microsoft_outlook_get_email or microsoft_outlook_list_emails instead.

        Args:
            message: Email message details.
            saveToSentItems: Specifies whether to save the sent email to the Sent Items folder.
        Returns:
            API response as a dictionary.
        """
        ...

