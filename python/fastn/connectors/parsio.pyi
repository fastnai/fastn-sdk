"""Fastn Parsio connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ParsioConnector:
    """Parsio connector ().

    Provides 17 tools.
    """

    def create_doc(
        self,
        html: str,
        name: str,
        from: Optional[str] = None,
        text: Optional[str] = None,
        to: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new document in the specified document management system.

        Args:
            html: The HTML content of the email. (required)
            name: Name of the email. (required)
            from: The sender's email address.
            text: The plain text content of the email.
            to: The recipient's email address.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_mailbox(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new mailbox in the specified email service.

        Args:
            name: Name field. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_webhook(
        self,
        url: str,
        enabled: Optional[bool] = None,
        event: Optional[str] = None,
        table_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the specified webhook service.

        Args:
            url: The target URL. (required)
            enabled: Indicates whether the request is enabled.
            event: The event associated with the request.
            table_id: The ID of the table.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_mailbox(
        self,
        mailbox_id: str,
    ) -> Dict[str, Any]:
        """Deletes a specified mailbox from the email service.

        Args:
            mailbox_id: The ID of the mailbox. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        ids: List[Any],
    ) -> Dict[str, Any]:
        """Deletes a specified webhook from the webhook service.

        Args:
            ids: An array of IDs to be processed by the Parsio API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def disable_template(
        self,
        ids: List[Any],
    ) -> Dict[str, Any]:
        """Disables a specified template in the template management system.

        Args:
            ids: An array of IDs to process. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def enable_template(
        self,
        ids: List[Any],
    ) -> Dict[str, Any]:
        """Enables a specified template in the template management system.

        Args:
            ids: An array of IDs to be processed by the Parsio API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_doc(
        self,
        documentId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific document in the specified document management system.

        Args:
            documentId: The unique identifier for the document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_docs(
        self,
        from: Optional[str] = None,
        page: Optional[str] = None,
        q: Optional[str] = None,
        status: Optional[str] = None,
        to: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of documents from the specified document management system.

        Args:
            from: Filter results from a specific date.
            page: Specify the page number for pagination.
            q: Search query string to filter results.
            status: Filter results by status.
            to: Filter results to a specific date.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_mailbox(
        self,
        mailbox_id: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific mailbox in the specified email service.

        Args:
            mailbox_id: The ID of the mailbox. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_mailboxes(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of mailboxes in the specified email service.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_template(
        self,
        template_id: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific template from the specified template management system.

        Args:
            template_id: The ID of the template to use for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_templates(
        self,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of templates from the specified template management system.

        Args:
            page: Specifies the page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_webhooks(
        self,
        mailbox_id: str,
    ) -> Dict[str, Any]:
        """Lists all webhooks configured in the specified webhook service.

        Args:
            mailbox_id: The unique identifier for the mailbox. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def parse_doc(
        self,
        documentId: str,
    ) -> Dict[str, Any]:
        """Parses the content of a document in the specified document management system.

        Args:
            documentId: The unique identifier for the document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_mailbox(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the settings or attributes of an existing mailbox in the specified email service.

        Args:
            name: The name. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_webhook(
        self,
        _id: str,
        enabled: bool,
        event: str,
        url: str,
        table_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing webhook in the specified webhook service.

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

