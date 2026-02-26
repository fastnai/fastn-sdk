"""Fastn Milvus connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MilvusConnector:
    """Milvus connector ().

    Provides 13 tools.
    """

    def create_backup(
        self,
        backupType: str,
        dbCollections: List[Any],
    ) -> Dict[str, Any]:
        """Creates a backup of the current state in the specified connector.

        Args:
            backupType: The type of backup to perform. (required)
            dbCollections:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_cluster(
        self,
        clusterName: str,
        projectId: str,
        regionId: str,
    ) -> Dict[str, Any]:
        """Creates a new cluster in the specified connector environment.

        Args:
            clusterName: The name of the Milvus cluster. (required)
            projectId: The ID of the project associated with the Milvus cluster. (required)
            regionId: The ID of the region where the Milvus cluster is located. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_collection(
        self,
        collectionName: str,
        dimension: int,
        autoID: Optional[str] = None,
        dbName: Optional[str] = None,
        idType: Optional[str] = None,
        metricType: Optional[str] = None,
        primaryFieldName: Optional[str] = None,
        vectorFieldName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new collection within a cluster in the specified connector.

        Args:
            collectionName: The name of the collection to be created. (required)
            dimension: The dimension of the vector. (required)
            autoID: Specifies whether to automatically generate IDs.
            dbName: The name of the database.
            idType: The data type of the primary key.
            metricType: The metric type used for similarity search.
            primaryFieldName: The name of the primary key field.
            vectorFieldName: The name of the vector field.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete(
        self,
        collectionName: str,
        filter: str,
        dbName: Optional[str] = None,
        partitionName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified item or record in the specified connector.

        Args:
            collectionName: The name of the collection to search. (required)
            filter: A JSON string representing the filter expression for searching. (required)
            dbName: The name of the database containing the collection.
            partitionName: The name of the partition to search within.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_backup(
        self,
        backupId: str,
        clusterId: str,
    ) -> Dict[str, Any]:
        """Deletes a backup from the specified connector.

        Args:
            backupId: The ID of the backup. (required)
            clusterId: The ID of the Milvus cluster. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def drop_cluster(
        self,
        clusterId: str,
    ) -> Dict[str, Any]:
        """Drops an existing cluster from the specified connector.

        Args:
            clusterId: The ID of the Milvus cluster to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def drop_collection(
        self,
        collectionName: str,
        dbName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Drops an existing collection from a cluster in the specified connector.

        Args:
            collectionName: The name of the collection. (required)
            dbName: The name of the database.
        Returns:
            API response as a dictionary.
        """
        ...

    def flush_collection(
        self,
        collectionName: str,
        dbName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Flushes the data from a specified collection in the connector.

        Args:
            collectionName: The name of the collection. (required)
            dbName: The name of the database.
        Returns:
            API response as a dictionary.
        """
        ...

    def get(
        self,
        collectionName: str,
        id: List[Any],
        outputFields: Optional[List[Any]] = None,
        partitionNames: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specified item or record from the connector.

        Args:
            collectionName: Name of the collection to query. (required)
            id: Array of entity IDs to retrieve. (required)
            outputFields: List of fields to be returned in the response.
            partitionNames: List of partition names to filter results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_clusters(
        self,
        currentPage: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all clusters in the specified connector.

        Args:
            currentPage: The current page number for pagination.
            pageSize: The number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_collections(
        self,
        dbName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all collections within a cluster in the specified connector.

        Args:
            dbName: Name of the target database.
        Returns:
            API response as a dictionary.
        """
        ...

    def insert(
        self,
        collectionName: str,
        data: List[Any],
        dbName: str,
        partitionName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Inserts a new item or record into a specified collection in the connector.

        Args:
            collectionName: Name of the collection. (required)
            data:  (required)
            dbName: Name of the database. (required)
            partitionName: Name of the partition to insert into (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def query(
        self,
        collectionName: str,
        filter: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        outputFields: Optional[List[Any]] = None,
        partitionNames: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Queries the data within a specified collection in the connector.

        Args:
            collectionName: The name of the collection to search. (required)
            filter: A JSON string representing the filter expression for the search. (required)
            limit: The maximum number of results to return.
            offset: The starting offset for pagination of search results.
            outputFields: An array of field names to retrieve in the search results.
            partitionNames: An array of partition names to limit the search.
        Returns:
            API response as a dictionary.
        """
        ...

