"""Fastn Airparser connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AirparserConnector:
    """Airparser connector ().

    Provides 8 tools.
    """

    def clone_extraction_schema(
        self,
        destination_inbox_id: str,
    ) -> Dict[str, Any]:
        """Duplicates an existing extraction schema within the connector for reuse or modification.

        Args:
            destination_inbox_id: The ID of the destination inbox. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_extraction_schema(
        self,
        fields: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new extraction schema in the connector to define how data will be extracted from documents.

        Args:
            fields:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_inbox(
        self,
        inboxId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific inbox within the connector, removing all associated documents.

        Args:
            inboxId: The ID of the inbox to process. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_document(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific document from the connector by its identifier.

        Args:
            docId: The ID of the document to parse. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_documents(
        self,
        from: Optional[str] = None,
        page: Optional[str] = None,
        q: Optional[str] = None,
        statuses: Optional[List[Any]] = None,
        to: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of documents stored in the specified connector.

        Args:
            from: Filter messages from this date.
            page: Specifies the page number for pagination.
            q: The search query string.
            statuses: An array of message statuses to filter by.
            to: Filter messages to this date.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inboxes(
        self,
    ) -> Dict[str, Any]:
        """Obtains a list of available inboxes within the connector to manage incoming documents.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_parsed_data(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Retrieves and parses data from documents stored in the connector for analysis and extraction.

        Args:
            docId: The ID of the document to be processed by Airparser. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_document(
        self,
        file: str,
        meta: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a document to the specified connector for further processing.

        Args:
            file: Details about the file to be processed (likely a URL or ID). (required)
            meta: Additional metadata related to the file or request.
        Returns:
            API response as a dictionary.
        """
        ...

