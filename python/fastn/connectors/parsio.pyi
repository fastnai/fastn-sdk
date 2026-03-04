"""Fastn Parsio connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class ParsioConnector:
    """Parsio connector ().

    Provides 17 tools.
    """

    def parsio_create_doc(
        self,
        html: str,
        mailboxId: str,
        name: str,
        from: Optional[str] = None,
        text: Optional[str] = None,
        to: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads and creates a new document in a specific Parsio mailbox for parsing. Use this tool when you need to submit a new email, PDF, or attachment to Parsio for structured data extraction. Do not use this tool to trigger parsing on an already-uploaded document; use the parse document tool instead. This operation stores the document in Parsio and may automatically trigger parsing if a matching template exists.

        Args:
            html: The HTML content of the email. (required)
            mailboxId: The ID of the mailbox. (required)
            name: Name of the email. (required)
            from: The sender's email address.
            text: The plain text content of the email.
            to: The recipient's email address.
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_create_mailbox(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new Parsio mailbox to receive and parse incoming emails or documents. Use this tool when setting up a new parsing pipeline in Parsio. Do not use this tool to modify an existing mailbox; use the update mailbox tool instead. This operation creates a persistent mailbox resource in Parsio.

        Args:
            name: Name field. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_create_webhook(
        self,
        mailbox_id: str,
        url: str,
        enabled: Optional[bool] = None,
        event: Optional[str] = None,
        table_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook for a specific Parsio mailbox, enabling Parsio to send parsed data notifications to a target URL when documents are processed. Use this tool when setting up automated data delivery from Parsio to an external system. Do not use this tool to modify an existing webhook; use the update webhook tool instead. This operation registers a persistent webhook that will deliver events until explicitly deleted.

        Args:
            mailbox_id: The ID of the mailbox. (required)
            url: The target URL. (required)
            enabled: Indicates whether the request is enabled.
            event: The event associated with the request.
            table_id: The ID of the table.
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_delete_mailbox(
        self,
        mailbox_id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified Parsio mailbox and its associated configuration. Use this tool when a mailbox is no longer needed. Do not use this tool if you only want to update mailbox settings; use the update mailbox tool instead. This action is irreversible — all templates, documents, and webhooks associated with the mailbox may be permanently lost.

        Args:
            mailbox_id: The ID of the mailbox. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_delete_webhook(
        self,
        ids: List[Any],
    ) -> Dict[str, Any]:
        """Permanently deletes a specified webhook from Parsio, stopping all future event deliveries to its configured endpoint. Use this tool when a webhook is no longer needed or must be replaced. Do not use this tool if you only want to pause delivery; instead, update the webhook configuration. This action is irreversible — the webhook cannot be recovered after deletion.

        Args:
            ids: An array of IDs to be processed by the Parsio API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_disable_template(
        self,
        ids: List[Any],
    ) -> Dict[str, Any]:
        """Disables one or more parsing templates in Parsio, preventing them from being applied to incoming documents. Use this tool when you want to deactivate a template without permanently deleting it, for example during template maintenance or A/B testing. Do not use this tool to delete a template. Disabled templates can be re-enabled using the enable template tool.

        Args:
            ids: An array of IDs to process. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_enable_template(
        self,
        ids: List[Any],
    ) -> Dict[str, Any]:
        """Re-enables one or more previously disabled parsing templates in Parsio so they are applied to incoming documents again. Use this tool to restore a template that was deactivated using the disable template tool. Do not use this tool to create a new template. Changes take effect immediately for subsequent document parsing.

        Args:
            ids: An array of IDs to be processed by the Parsio API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_get_doc(
        self,
        documentId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details and parsed data of a specific document in Parsio by its document ID. Use this tool to check the extraction results, parsing status, or metadata of a single document after it has been processed. Do not use this tool to list all documents in a mailbox; use the list documents tool instead. This is a read-only operation with no side effects.

        Args:
            documentId: The unique identifier for the document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_get_mailbox(
        self,
        mailbox_id: str,
    ) -> Dict[str, Any]:
        """Retrieves the details and configuration of a specific Parsio mailbox by its mailbox ID. Use this tool to inspect mailbox settings or obtain its ID for use in document and template operations. Do not use this tool to list all mailboxes; use the list mailboxes tool instead. This is a read-only operation with no side effects.

        Args:
            mailbox_id: The ID of the mailbox. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_get_template(
        self,
        template_id: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific Parsio parsing template by its template ID, including its field extraction rules and configuration. Use this tool when you need to inspect or verify a single templates settings. Do not use this tool to list all templates; use the list templates tool instead. This is a read-only operation with no side effects.

        Args:
            template_id: The ID of the template to use for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_list_docs(
        self,
        mailboxId: str,
        from: Optional[str] = None,
        page: Optional[str] = None,
        q: Optional[str] = None,
        status: Optional[str] = None,
        to: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns all documents stored in a specific Parsio mailbox, identified by its mailbox ID, along with their parsing status and metadata. Use this tool to browse or audit documents that have been submitted for parsing. Do not use this tool to retrieve a single document by ID; use the get document tool instead. This is a read-only operation with no side effects.

        Args:
            mailboxId: The ID of the mailbox. (required)
            from: Filter results from a specific date.
            page: Specify the page number for pagination.
            q: Search query string to filter results.
            status: Filter results by status.
            to: Filter results to a specific date.
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_list_mailboxes(
        self,
    ) -> Dict[str, Any]:
        """Returns all Parsio mailboxes configured for the authenticated account. Use this tool to discover available mailboxes, find mailbox IDs needed for document and template operations, or audit mailbox configurations. Do not use this tool to retrieve a single mailbox by ID; use the get mailbox tool instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_list_templates(
        self,
        mailbox_id: str,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns all parsing templates configured for a specific Parsio mailbox, identified by its mailbox ID. Use this tool to discover available templates, find template IDs for use in other operations, or audit template configurations. Do not use this tool to retrieve a single template by ID; use the get template tool instead. This is a read-only operation with no side effects.

        Args:
            mailbox_id: The ID of the mailbox. (required)
            page: Specifies the page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_list_webhooks(
        self,
        mailbox_id: str,
    ) -> Dict[str, Any]:
        """Returns all webhooks configured for a specific Parsio mailbox, identified by its mailbox ID. Use this tool to audit webhook endpoints, verify event subscriptions, or find webhook IDs needed for update or delete operations. This is a read-only operation with no side effects.

        Args:
            mailbox_id: The unique identifier for the mailbox. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_parse_doc(
        self,
        documentId: str,
    ) -> Dict[str, Any]:
        """Triggers the parsing of a specific document in Parsio using the matched template, extracting structured data fields from its content. Use this tool when a document has already been uploaded to Parsio and you need to initiate or re-trigger its data extraction. Do not use this tool to upload a new document; use the create document tool instead. Parsing results are stored in Parsio and may be delivered via webhook if one is configured.

        Args:
            documentId: The unique identifier for the document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_update_mailbox(
        self,
        mailbox_id: str,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the settings or attributes of an existing Parsio mailbox, such as its name or configuration options. Use this tool when you need to modify a mailbox that has already been created. Do not use this tool to create a new mailbox; use the create mailbox tool instead. Changes take effect immediately.

        Args:
            mailbox_id: The ID of the mailbox. (required)
            name: The name. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def parsio_update_webhook(
        self,
        _id: str,
        enabled: bool,
        event: str,
        url: str,
        table_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing webhook in Parsio, such as its target URL or event triggers. Use this tool when you need to modify where or how Parsio delivers parsed data notifications. Do not use this tool to create a new webhook; use the create webhook tool instead. This operation overwrites the existing webhook configuration and takes effect immediately.

        Args:
            _id: Unique identifier for the webhook. (required)
            enabled: Indicates whether the webhook is active. (required)
            event: The type of event that triggers the webhook. (required)
            url: The URL where Parsio will send webhook events. (required)
            table_id: The ID of the table associated with this webhook.
        Returns:
            API response as a dictionary.
        """
        ...

