"""Fastn Restdb connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class RestdbConnector:
    """Restdb connector ().

    Provides 8 tools.
    """

    def create_document(
        self,
    ) -> Dict[str, Any]:
        """Creates a new document in the database using the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_document(
        self,
        collectionId: str,
        collectionName: str,
    ) -> Dict[str, Any]:
        """Deletes a specific document from the database using the specified connector.

        Args:
            collectionId: The ID of the collection to access. (required)
            collectionName: The name of the collection to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_documents(
        self,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes multiple documents from the database based on given criteria using the specified connector.

        Args:
            q: A query string to filter the results (e.g., `name=John`). This allows you to filter the results based on the field names and values within your collection.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_collection_metadata(
        self,
        collectionName: str,
    ) -> Dict[str, Any]:
        """Retrieves metadata about a specific collection within the database using the specified connector.

        Args:
            collectionName: The name of the collection to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_database_metadata(
        self,
    ) -> Dict[str, Any]:
        """Retrieves metadata about the database structure and settings using the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_document(
        self,
        h: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a single document from the database using the specified connector.

        Args:
            h: Description of the 'h' parameter.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_documents(
        self,
        h: Optional[str] = None,
        p: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of documents from the database using the specified connector.

        Args:
            h: Description of the 'h' parameter (if available).
            p: Description of the 'p' parameter (if available).
        Returns:
            API response as a dictionary.
        """
        ...

    def update_document(
        self,
    ) -> Dict[str, Any]:
        """Updates an existing document in the database with new information using the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

