"""Fastn Restdb connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class RestdbConnector:
    """Restdb connector ().

    Provides 8 tools.
    """

    def restdb_create_document(
        self,
        collectionName: str,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new document in a specified restdb.io collection. Use this when you need to insert a new record into a collection. Do not use this to update an existing document (use restdb_update_document instead). This operation writes a new entry to the database and cannot be undone without explicitly deleting the created document.

        Args:
            collectionName: The name of the collection to interact with. (required)
            body: Data to be sent to Restdb.
        Returns:
            API response as a dictionary.
        """
        ...

    def restdb_delete_document(
        self,
        collectionId: str,
        collectionName: str,
    ) -> Dict[str, Any]:
        """Deletes a single specific document from a restdb.io collection by its document ID. Use this when you need to permanently remove one known document. Do not use this to delete multiple documents at once (use restdb_delete_documents instead) or to update a document (use restdb_update_document instead). This operation is irreversible — the deleted document cannot be recovered.

        Args:
            collectionId: The ID of the collection to access. (required)
            collectionName: The name of the collection to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def restdb_delete_documents(
        self,
        collectionName: str,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes all documents in a restdb.io collection that match the specified criteria in bulk. Use this when you need to remove multiple documents from a collection at once based on a query or wildcard match. Do not use this to delete a single known document by ID (use restdb_delete_document instead). This operation is irreversible — deleted documents cannot be recovered.

        Args:
            collectionName: The name of the collection to interact with. (required)
            q: A query string to filter the results (e.g., `name=John`). This allows you to filter the results based on the field names and values within your collection.
        Returns:
            API response as a dictionary.
        """
        ...

    def restdb_get_collection_metadata(
        self,
        collectionName: str,
    ) -> Dict[str, Any]:
        """Retrieves metadata about a specific restdb.io collection, including its schema, field definitions, and configuration. Use this when you need to inspect the structure or settings of a named collection before querying or modifying its documents. Do not use this to retrieve actual document data (use restdb_list_documents or restdb_get_document instead) or to get database-level metadata (use restdb_get_database_metadata instead).

        Args:
            collectionName: The name of the collection to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def restdb_get_database_metadata(
        self,
    ) -> Dict[str, Any]:
        """Retrieves top-level metadata about the entire restdb.io database, including its collections, structure, and settings. Use this when you need an overview of the database schema or to discover which collections exist. Do not use this to retrieve metadata about a specific collection (use restdb_get_collection_metadata instead) or to read document data.
        Returns:
            API response as a dictionary.
        """
        ...

    def restdb_get_document(
        self,
        collectionId: str,
        collectionName: str,
        h: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a single document from a restdb.io collection by its document ID. Use this when you know the exact document ID and need to fetch that specific record. Do not use this to retrieve multiple documents or search by criteria (use restdb_list_documents instead), or to inspect collection structure (use restdb_get_collection_metadata instead).

        Args:
            collectionId: The ID of the collection to access. (required)
            collectionName: The name of the collection to access. (required)
            h: Description of the 'h' parameter.
        Returns:
            API response as a dictionary.
        """
        ...

    def restdb_list_documents(
        self,
        collectionName: str,
        h: Optional[str] = None,
        p: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of documents from a specified restdb.io collection, optionally filtered by query parameters. Use this when you need to fetch multiple records from a collection. Do not use this to retrieve a single known document by ID (use restdb_get_document instead) or to inspect collection schema (use restdb_get_collection_metadata instead).

        Args:
            collectionName: The name of the collection to interact with. (required)
            h: Description of the 'h' parameter (if available).
            p: Description of the 'p' parameter (if available).
        Returns:
            API response as a dictionary.
        """
        ...

    def restdb_update_document(
        self,
        body: Dict[str, Any],
        collectionId: str,
        collectionName: str,
    ) -> Dict[str, Any]:
        """Updates an existing document in a restdb.io collection by its document ID using a partial PATCH update. Use this when you need to modify one or more fields of a specific, known document without replacing the entire record. Do not use this to create new documents (use restdb_create_document instead) or to update multiple documents at once (use restdb_delete_documents and recreate, or query first). This operation overwrites only the fields provided and cannot be undone without a prior backup.

        Args:
            body: The data to be sent in the request body.  This may be empty for certain operations. (required)
            collectionId: The ID of the collection. (required)
            collectionName: The name of the collection. (required)
        Returns:
            API response as a dictionary.
        """
        ...

