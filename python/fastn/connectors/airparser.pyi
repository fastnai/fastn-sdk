"""Fastn Airparser connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AirparserConnector:
    """Airparser connector ().

    Provides 8 tools.
    """

    def airparser_clone_extraction_schema(
        self,
        destination_inbox_id: str,
        inboxId: str,
    ) -> Dict[str, Any]:
        """Duplicates the extraction schema of an existing Airparser inbox into a new or target inbox. Use this when you want to reuse an existing schema as a starting point without recreating it from scratch. Do not use this to create a completely new schema from scratch — use airparser_create_extraction_schema instead. This action modifies the target inbox configuration.

        Args:
            destination_inbox_id: The ID of the destination inbox. (required)
            inboxId: The ID of the inbox. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def airparser_create_extraction_schema(
        self,
        fields: List[Any],
        inboxId: str,
    ) -> Dict[str, Any]:
        """Creates a new extraction schema for a specific Airparser inbox, defining which fields and data points should be extracted from incoming documents. Use this when setting up a new inbox or changing the extraction structure. Do not use this to update an existing schema — use the clone or update endpoint instead. This action modifies the inbox configuration.

        Args:
            fields:  (required)
            inboxId: The ID of the inbox to process. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def airparser_delete_inbox(
        self,
        inboxId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific Airparser inbox and all documents associated with it. Use this only when you intend to fully remove an inbox and its contents. This action is irreversible — deleted inboxes and their documents cannot be recovered. Do not use this if you only want to remove individual documents.

        Args:
            inboxId: The ID of the inbox to process. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def airparser_get_document(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single document from Airparser by its unique document ID. Use this to inspect document metadata or status for a known document. Do not use this to list multiple documents — use airparser_list_documents instead. This action is read-only and has no side effects.

        Args:
            docId: The ID of the document to parse. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def airparser_get_parsed_data(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Retrieves the fully parsed and extracted field data for a specific document in Airparser, including all structured values defined by the inboxs extraction schema. Use this after a document has been processed to access its extracted content. Do not use this to get basic document metadata — use airparser_get_document instead. This action is read-only and has no side effects.

        Args:
            docId: The ID of the document to be processed by Airparser. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def airparser_list_documents(
        self,
        inboxId: str,
        from: Optional[str] = None,
        page: Optional[str] = None,
        q: Optional[str] = None,
        statuses: Optional[List[Any]] = None,
        to: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all documents stored in a specific Airparser inbox. Use this to browse or audit documents that have been submitted for parsing. Do not use this to retrieve a single documents details — use airparser_get_document instead, or to get parsed field data use airparser_get_parsed_data. This action is read-only and has no side effects.

        Args:
            inboxId: The ID of the inbox to retrieve messages from. (required)
            from: Filter messages from this date.
            page: Specifies the page number for pagination.
            q: The search query string.
            statuses: An array of message statuses to filter by.
            to: Filter messages to this date.
        Returns:
            API response as a dictionary.
        """
        ...

    def airparser_list_inboxes(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all inboxes available in your Airparser account. Use this to discover existing inboxes and their IDs before performing operations such as uploading documents or managing schemas. Do not use this to retrieve documents inside an inbox — use airparser_list_documents instead. This action is read-only and has no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def airparser_upload_document(
        self,
        file: str,
        inboxId: str,
        meta: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a document file to a specific Airparser inbox to be queued for parsing and data extraction. Use this to submit new documents for processing. The document will be parsed according to the inboxs extraction schema. This action creates a new document record and triggers the parsing pipeline — it cannot be undone without explicitly deleting the document afterward.

        Args:
            file: Details about the file to be processed (likely a URL or ID). (required)
            inboxId: The ID of the inbox to process. (required)
            meta: Additional metadata related to the file or request.
        Returns:
            API response as a dictionary.
        """
        ...

