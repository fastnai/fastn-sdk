"""Fastn MongoDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _MongodbDeleteDocumentFilter(TypedDict, total=False):
    _id: Dict[str, Any]

class _MongodbUpdateDocumentFilter(TypedDict, total=False):
    _id: Dict[str, Any]

class _MongodbUpdateDocumentUpdate(TypedDict, total=False):
    _set: Dict[str, Any]

class MongodbConnector:
    """MongoDB connector ().

    Provides 12 tools.
    """

    def mongodb_create_collection(
        self,
        collection_name: Optional[str] = None,
        db_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new collection within a specified MongoDB database. Use this tool when you need to initialize a new collection before inserting documents. Note: In MongoDB, collections are also created implicitly on first document insert; use this tool when explicit creation with options (e.g., validation rules, capped size) is required. This operation is reversible by dropping the collection afterward.

        Args:
            collection_name: 
            db_name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def mongodb_create_database(
        self,
        db_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new database in the connected MongoDB environment. Use this tool when you need to provision a new database. Note: In MongoDB, a database is not physically created until at least one collection is added; this tool initializes the database context. Do not use this tool if the target database already exists.

        Args:
            db_name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def mongodb_create_document(
        self,
        collection: Optional[str] = None,
        dataSource: Optional[str] = None,
        database: Optional[str] = None,
        document: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Inserts a new document into a specified MongoDB collection and database. Use this tool when you need to add a single new record to a collection. Do not use this tool for updating existing documents — use mongodb_update_document instead. Uses the MongoDB Data API insertOne action. This operation creates a new document and is not reversible without a separate delete.

        Args:
            collection: 
            dataSource: 
            database: 
            document: 
        Returns:
            API response as a dictionary.
        """
        ...

    def mongodb_delete_document(
        self,
        collection: Optional[str] = None,
        dataSource: Optional[str] = None,
        database: Optional[str] = None,
        filter: Optional[_MongodbDeleteDocumentFilter] = None,
    ) -> Dict[str, Any]:
        """Deletes a single document by its ID from a specified MongoDB collection and database. Use this tool when you need to permanently remove a specific document. This operation is irreversible — the deleted document cannot be recovered. Do not use this tool for bulk deletions; use a bulk delete operation if available.

        Args:
            collection: 
            dataSource: 
            database: 
            filter: 
        Returns:
            API response as a dictionary.
        """
        ...

    def mongodb_delete_resource(
        self,
        collection_name: str,
        db_name: str,
        query: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Removes a resource from the connected MongoDB server. Use this tool when you need to delete a generic resource by specifying the target. Do not use this tool for deleting specific documents by ID — use mongodb_delete_document instead. This operation is irreversible; the deleted resource cannot be recovered.

        Args:
            collection_name: The name of the collection to access. (required)
            db_name: The name of the database to target. (required)
            query: Query parameters for filtering documents. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def mongodb_get_document(
        self,
        collection: Optional[str] = None,
        dataSource: Optional[str] = None,
        database: Optional[str] = None,
        filter: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves a single document matching specified filter criteria from a MongoDB collection and database. Use this tool when you need to fetch one specific document. Do not use this tool when you need multiple documents — use mongodb_list_documents instead. Uses the MongoDB Data API findOne action.

        Args:
            collection: 
            dataSource: 
            database: 
            filter: 
        Returns:
            API response as a dictionary.
        """
        ...

    def mongodb_get_resource(
        self,
        collection_name: str,
        db_name: str,
        limit: int,
        projection: Dict[str, Any],
        query: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Retrieves a resource or data from the connected MongoDB server via a raw GET request. Use this tool when you need to fetch a generic resource by specifying the target endpoint. Do not use this tool to retrieve specific documents — use mongodb_get_document or mongodb_list_documents instead.

        Args:
            collection_name: Name of the collection. (required)
            db_name: Name of the database. (required)
            limit: Number of documents to return. (required)
            projection: Fields to include or exclude in the result. (required)
            query: Query parameters for the MongoDB database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def mongodb_list_collections(
        self,
        db_name: str,
    ) -> Dict[str, Any]:
        """Lists all collections within a specified MongoDB database. Use this tool when you need to enumerate available collections in a database, for example before querying or managing documents. Do not use this tool to retrieve documents; use mongodb_list_documents or mongodb_get_document instead.

        Args:
            db_name: The name of the MongoDB database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def mongodb_list_documents(
        self,
        collection: Optional[str] = None,
        dataSource: Optional[str] = None,
        database: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of documents from a specified MongoDB collection and database, optionally filtered by query criteria. Use this tool when you need to fetch multiple documents at once. Do not use this tool when you need a single specific document — use mongodb_get_document instead. Uses the MongoDB Data API find action.

        Args:
            collection: 
            dataSource: 
            database: 
        Returns:
            API response as a dictionary.
        """
        ...

    def mongodb_patch_resource(
        self,
        collection_name: str,
        data: Dict[str, Any],
        query: Dict[str, Any],
        db_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Applies partial modifications to an existing resource on the connected MongoDB server. Use this tool when you need to update only specific fields of a resource without replacing it entirely. Do not use this tool for full document replacements — use mongodb_update_document instead. This operation modifies data in place.

        Args:
            collection_name: The name of the collection to interact with. (required)
            data: Data to be inserted or updated in the MongoDB collection. (required)
            query: Query parameters for filtering documents in the MongoDB collection. (required)
            db_name: The name of the database.
        Returns:
            API response as a dictionary.
        """
        ...

    def mongodb_post_resource(
        self,
        collection_name: str,
        data: Dict[str, Any],
        db_name: str,
    ) -> Dict[str, Any]:
        """Submits data to the connected MongoDB server to create a new resource. Use this tool when you need to send a raw POST request to create a generic resource. Do not use this tool for inserting specific documents — use mongodb_create_document instead. This operation creates new data on the server.

        Args:
            collection_name: Name of the collection. (required)
            data: Data to be inserted, updated, or queried. (required)
            db_name: Name of the database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def mongodb_update_document(
        self,
        collection: Optional[str] = None,
        dataSource: Optional[str] = None,
        database: Optional[str] = None,
        filter: Optional[_MongodbUpdateDocumentFilter] = None,
        update: Optional[_MongodbUpdateDocumentUpdate] = None,
    ) -> Dict[str, Any]:
        """Updates an existing document in a specified MongoDB collection and database. Use this tool when you need to modify one or more fields of an existing document identified by its filter criteria. Do not use this tool for bulk updates or for creating new documents — use mongodb_create_document instead. This operation modifies existing data in place.

        Args:
            collection: 
            dataSource: 
            database: 
            filter: 
            update: 
        Returns:
            API response as a dictionary.
        """
        ...

