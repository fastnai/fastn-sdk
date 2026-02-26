"""Fastn MongoDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MongodbConnector:
    """MongoDB connector ().

    Provides 12 tools.
    """

    def create_collection(
        self,
        collection_name: Optional[str] = None,
        db_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new collection within a specified database using the createCollection tool.

        Args:
            collection_name: 
            db_name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_database(
        self,
        db_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new database in the specified environment using the createDatabase tool.

        Args:
            db_name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_document_(
        self,
        collection: Optional[str] = None,
        dataSource: Optional[str] = None,
        database: Optional[str] = None,
        document: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new document in the specified database using the createDocument tool.

        Args:
            collection: 
            dataSource: 
            database: 
            document: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete(
        self,
        collection_name: str,
        db_name: str,
        query: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Removes a resource from the specified server using the delete tool.

        Args:
            collection_name: The name of the collection to access. (required)
            db_name: The name of the database to target. (required)
            query: Query parameters for filtering documents. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_document(
        self,
        collection: Optional[str] = None,
        dataSource: Optional[str] = None,
        database: Optional[str] = None,
        filter: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Deletes a document by its ID from the specified database using the deleteDocument tool.

        Args:
            collection: 
            dataSource: 
            database: 
            filter: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get(
        self,
        collection_name: str,
        db_name: str,
        limit: int,
        projection: Dict[str, Any],
        query: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Retrieves a resource or data from the specified server using the get tool.

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

    def get_collections(
        self,
        db_name: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all collections within the specified database using the getCollections tool.

        Args:
            db_name: The name of the MongoDB database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_document(
        self,
        collection: Optional[str] = None,
        dataSource: Optional[str] = None,
        database: Optional[str] = None,
        filter: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Fetches a specific document by its ID from the specified database using the getDocument tool.

        Args:
            collection: 
            dataSource: 
            database: 
            filter: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_documents(
        self,
        collection: Optional[str] = None,
        dataSource: Optional[str] = None,
        database: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all documents from the specified database using the getDocuments tool.

        Args:
            collection: 
            dataSource: 
            database: 
        Returns:
            API response as a dictionary.
        """
        ...

    def patch(
        self,
        collection_name: str,
        data: Dict[str, Any],
        query: Dict[str, Any],
        db_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Applies partial modifications to an existing resource on the specified server using the patch tool.

        Args:
            collection_name: The name of the collection to interact with. (required)
            data: Data to be inserted or updated in the MongoDB collection. (required)
            query: Query parameters for filtering documents in the MongoDB collection. (required)
            db_name: The name of the database.
        Returns:
            API response as a dictionary.
        """
        ...

    def post(
        self,
        collection_name: str,
        data: Dict[str, Any],
        db_name: str,
    ) -> Dict[str, Any]:
        """Submits data to the specified server to create a new resource using the post tool.

        Args:
            collection_name: Name of the collection. (required)
            data: Data to be inserted, updated, or queried. (required)
            db_name: Name of the database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_document(
        self,
        collection: Optional[str] = None,
        dataSource: Optional[str] = None,
        database: Optional[str] = None,
        filter: Optional[Dict[str, Any]] = None,
        update: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing document in the specified database using the updateDocument tool.

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

