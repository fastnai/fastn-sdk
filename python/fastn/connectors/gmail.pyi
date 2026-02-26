"""Fastn Gmail connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GmailConnector:
    """Gmail connector ().

    Provides 5 tools.
    """

    def extract_from_email(
        self,
        message_id: Optional[str] = None,
        search_term: Optional[str] = None,
        subject: Optional[str] = None,
    ) -> Dict[str, Any]:
        """The extractFromEmail tool analyzes the content of an email to extract specific information such as names, dates, or key data points using the email connector, streamlining data processing.

        Args:
            message_id: ID of the email message (if applicable).
            search_term: Search term for filtering emails (if applicable).
            subject: Subject of the email (if applicable).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_mail(
        self,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """The getMail tool fetches the content and details of a specific email from the inbox using the email connector, allowing you to read or process the individual email.

        Args:
            format: Format of the data for My connectors.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_mail_attachments(
        self,
        attachmentId: str,
        messageId: str,
    ) -> Dict[str, Any]:
        """The getMailAttachments tool extracts and retrieves any attachments associated with a specific email using the email connector, enabling access to documents, images, or files sent with the email.

        Args:
            attachmentId:  (required)
            messageId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_mails(
        self,
        includeSpamTrash: Optional[str] = None,
        labelIds: Optional[str] = None,
        maxResults: Optional[str] = None,
        pageToken: Optional[str] = None,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """The getMails tool retrieves a list of emails from the inbox using the designated email connector, providing details about each email for further actions.

        Args:
            includeSpamTrash: Include spam and trash items.
            labelIds: Comma-separated list of label IDs.
            maxResults: Maximum number of results to return.
            pageToken: Token for pagination.
            q: Search query.
        Returns:
            API response as a dictionary.
        """
        ...

    def send_mail(
        self,
        content: str,
        from: str,
        subject: str,
        to: str,
    ) -> Dict[str, Any]:
        """The sendMail tool allows you to send emails through the specified email connector, enabling communication with recipients via their email addresses.

        Args:
            content: The body content of the email. (required)
            from: Your email address. (required)
            subject: The subject of the email. (required)
            to: The recipient's email address. (required)
        Returns:
            API response as a dictionary.
        """
        ...

