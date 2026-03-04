"""Fastn Gmail connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class GmailConnector:
    """Gmail connector ().

    Provides 15 tools.
    """

    def gmail_create_draft(
        self,
        content: str,
        from: str,
        subject: str,
        to: str,
        threadId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new unsent email draft and saves it to the Drafts folder in the authenticated users Gmail account. Use this when you need to prepare a message for future review or sending without delivering it immediately. Do not use this to send an email now; use gmail_send_mail instead. Do not use this to insert an already-composed message directly into the mailbox; use gmail_create_email instead.

        Args:
            content: The body content of the email. (required)
            from: The sender's email address. (required)
            subject: The subject of the email. (required)
            to: The recipient's email address. (required)
            threadId: The ID of the thread to which the draft email belongs, if any.
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_create_email(
        self,
        content: str,
        from: str,
        subject: str,
        to: str,
        deleted: Optional[bool] = None,
        internalDateSource: Optional[str] = None,
        labelIds: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new email message in the authenticated users Gmail account without sending it. Use this to insert a raw message into the mailbox (e.g., to import an existing message or create one programmatically). Do not use this to send an email to a recipient; use gmail_send_mail instead. Do not use this to save an unsent draft for later editing; use gmail_create_draft instead. Note: this action writes a message directly to the mailbox and cannot be undone without separately deleting the message.

        Args:
            content: The body content of the email. (required)
            from: Your email address. (required)
            subject: The subject of the email. (required)
            to: The recipient's email address. (required)
            deleted: Flag indicating if the email is deleted.
            internalDateSource: Source of the internal date.
            labelIds: Labels associated with the email.
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_delete_email(
        self,
        messageId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently and irreversibly deletes a specific email from the authenticated users Gmail account by message ID. Use this only when the message must be completely and permanently removed from the account. This action cannot be undone and the message cannot be recovered after deletion. Do not use this to move a message to Trash with the option to recover it later; use gmail_trash_email instead.

        Args:
            messageId: The ID of the email to be deleted. (required)
            access_token: OAuth 2.0 access token.
            alt: Data format for the response.
            callback: JSONP callback parameter.
            fields: Selector specifying which fields to include in a partial response.
            prettyPrint: Returns response with indentations and line breaks.
            quotaUser: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
            uploadType: Legacy upload protocol for media files.
            upload_protocol: Upload protocol for media files.
            xgafv: V1 error format.
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_extract_from_email(
        self,
        message_id: Optional[str] = None,
        search_term: Optional[str] = None,
        subject: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Extracts specific information (names, dates, key data points) from email content. Use this to find and retrieve lines from an email that match a specific search term. Provide either a message_id to retrieve a specific email, or a subject and/or search_term to locate and search within emails. Do not use this to download or retrieve entire attachments; use gmail_get_mail_attachment instead. Do not use this to extract metadata (subject, sender, date headers); those are included in the email structure returned by gmail_get_mail.

        Args:
            message_id: ID of the email message (if applicable).
            search_term: Search term for filtering emails (if applicable).
            subject: Subject of the email (if applicable).
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_get_label(
        self,
        labelId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific Gmail label by its label ID from the authenticated users Gmail account, including its name, type, and visibility settings. Use this when you need the properties of a single known label. Do not use this to list all available labels; use gmail_list_labels instead.

        Args:
            labelId: The ID of the label to retrieve. (required)
            access_token: OAuth 2.0 access token.
            alt: Data format for the response.
            callback: JSONP callback function name.
            fields: Comma-separated list of fields to include in the response.
            prettyPrint: Whether to return response in a pretty-printed format.
            quotaUser: An opaque string identifying the user requesting the API call.
            uploadType: Type of upload being performed.
            upload_protocol: Upload protocol used.
            xgafv: V1 error format.
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_get_mail(
        self,
        messageId: str,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full content and metadata (subject, sender, recipients, body, headers) of a single email by its message ID from the authenticated users Gmail account. Use this to read or process a specific email. Do not use this to list multiple emails or search the inbox; use gmail_list_emails instead. Do not use this to download a file attachment from the email; use gmail_get_mail_attachment instead. Do not use this to extract specific data points from email body text; use gmail_extract_from_email instead.

        Args:
            messageId: Message ID for the My connectors API call. (required)
            format: Format of the data for My connectors.
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_get_mail_attachment(
        self,
        attachmentId: str,
        messageId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single attachment from an email by its message ID and attachment ID. Use this when you need to download or access a specific file, document, or image that was sent with an email. Do not use this to extract text or data from within an email body; use gmail_extract_from_email instead. Do not use this to list all attachments in a message; this tool retrieves a single attachment by ID.

        Args:
            attachmentId:  (required)
            messageId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_get_thread(
        self,
        threadId: str,
        format: Optional[str] = None,
        metadataHeaders: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific email thread and all its constituent messages from the authenticated users Gmail account by thread ID. Use this when you need to read the full conversation history of a thread, including all replies and their content. Do not use this to list all threads in the mailbox; use gmail_list_threads instead. Do not use this to retrieve a single standalone email by message ID; use gmail_get_mail instead.

        Args:
            threadId: The Gmail thread identifier to retrieve. (required)
            format: The level of detail to include in the response. Options are metadata, minimal, or full.
            metadataHeaders: Headers to include in the metadata portion of the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_list_drafts(
        self,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        includeSpamTrash: Optional[str] = None,
        maxResults: Optional[str] = None,
        pageToken: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        q: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all email drafts saved in the Drafts folder of the authenticated users Gmail account. Use this to enumerate drafts available for review, editing, or sending. Do not use this to retrieve the full content of a specific draft; use gmail_get_mail with the draft message ID instead. Do not use this to list sent or received emails; use gmail_list_emails instead.

        Args:
            access_token: OAuth 2.0 access token for the API request.
            alt: Data format for the response, e.g., JSON.
            callback: JSONP callback function name.
            fields: Selector specifying which fields to include in a partial response.
            includeSpamTrash: Whether to include spam and trash in the results.
            maxResults: Maximum number of drafts to return in the response.
            pageToken: Page token to retrieve the next page of results.
            prettyPrint: Returns response with indentations and line breaks for readability.
            q: Search query string to filter drafts.
            quotaUser: User to impersonate for quota purposes.
            uploadType: Type of the upload protocol.
            upload_protocol: Upload protocol for media, if applicable.
            xgafv: Error format version for the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_list_emails(
        self,
        includeSpamTrash: Optional[str] = None,
        labelIds: Optional[str] = None,
        maxResults: Optional[str] = None,
        pageToken: Optional[str] = None,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of emails in the authenticated users Gmail account, with optional filtering by label, query string, or other parameters. Use this to enumerate or search for multiple messages across the mailbox. Do not use this to retrieve the full content of a specific email; use gmail_get_mail instead. Do not use this to list email threads grouped by conversation; use gmail_list_threads instead.

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

    def gmail_list_labels(
        self,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all labels defined in the authenticated users Gmail account, including both system labels (e.g., INBOX, SENT, TRASH) and user-created labels. Use this to discover available labels for filtering, categorizing, or organizing emails. Do not use this to retrieve the full details of a single label by ID; use gmail_get_label instead.

        Args:
            access_token: OAuth 2.0 access token used for authorizing the request.
            alt: Data format for the response, such as 'json'.
            callback: JSONP callback function name.
            fields: Selector specifying which fields to include in a partial response.
            prettyPrint: Returns response with indentations and line breaks for readability.
            quotaUser: An opaque string that identifies the user making the request for quota purposes.
            uploadType: Legacy upload protocol for media resources.
            upload_protocol: Upload protocol for media resources, such as 'raw' or 'multipart'.
            xgafv: V1 error format version parameter.
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_list_threads(
        self,
        includeSpamTrash: Optional[bool] = None,
        labelIds: Optional[str] = None,
        maxResults: Optional[int] = None,
        pageToken: Optional[int] = None,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of email threads in the authenticated users Gmail account, with optional filtering by label, query, or other parameters. Use this to get an overview of conversations or to find threads matching specific criteria. Do not use this to retrieve the full content and messages of a single thread; use gmail_get_thread instead. Do not use this to list individual messages; use gmail_list_emails instead.

        Args:
            includeSpamTrash: Whether to include messages from Spam and Trash folders in the results.
            labelIds: A comma-separated list of label IDs to filter messages.
            maxResults: Maximum number of messages to return.
            pageToken: Token for retrieving the next page of results.
            q: Free-text search query to apply to messages.
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_send_mail(
        self,
        content: str,
        from: str,
        subject: str,
        to: str,
    ) -> Dict[str, Any]:
        """Sends an email immediately to one or more recipients from the authenticated users Gmail account. Use this to deliver a message now. This action is irreversible once submitted; the email is delivered and cannot be recalled. Do not use this to save a message for later sending; use gmail_create_draft instead. Do not use this to insert a message into the mailbox without sending it; use gmail_create_email instead.

        Args:
            content: The body content of the email. (required)
            from: Your email address. (required)
            subject: The subject of the email. (required)
            to: The recipient's email address. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_trash_email(
        self,
        messageId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Moves a specific email to the Trash folder in the authenticated users Gmail account by message ID. The message is not permanently deleted and can be recovered within 30 days. Use this as a reversible alternative to permanent deletion. Do not use this to permanently and immediately delete a message; use gmail_delete_email instead. Do not use this to restore a trashed message; use gmail_untrash_message instead.

        Args:
            messageId: The unique identifier for the email to be trashed. (required)
            access_token: OAuth 2.0 access token.
            alt: Data format for the response.
            callback: JSONP callback function name.
            fields: Selector specifying which fields to include in a partial response.
            prettyPrint: Returns response with indentations and line breaks.
            quotaUser: An opaque string that represents a user for quota purposes.
            uploadType: Legacy upload protocol for media files.
            upload_protocol: Upload protocol for media.
            xgafv: Version of the Google APIs to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def gmail_untrash_message(
        self,
        messageId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes a previously trashed email from the Trash folder and restores it to the authenticated users inbox in Gmail. Use this to recover a message that was moved to Trash by mistake. Do not use this to recover a permanently deleted message; permanently deleted messages cannot be restored. Do not use this to move a message to Trash; use gmail_trash_email instead.

        Args:
            messageId: The ID of the email to untrash. (required)
            access_token: OAuth 2.0 access token.
            alt: Data format for the response.
            callback: JSONP callback function name.
            fields: Selector specifying which fields to include in a partial response.
            prettyPrint: Returns response with indentations and line breaks.
            quotaUser: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
            uploadType: Legacy upload protocol for media resources.
            upload_protocol: Upload protocol for media resources.
            xgafv: V1 error format.
        Returns:
            API response as a dictionary.
        """
        ...

