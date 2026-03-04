"""Fastn Milvus connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MilvusConnector:
    """Milvus connector ().

    Provides 18 tools.
    """

    def create_backup(
        self,
        backupType: str,
        clusterId: str,
        dbCollections: List[Any],
    ) -> Dict[str, Any]:
        """Creates a backup of the current state in the specified connector.

        Args:
            backupType: The type of backup to perform. (required)
            clusterId: The ID of the Milvus cluster. (required)
            dbCollections:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_collection_milvus(
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
        """Creates a collection in Milvus, an open-source vector database built for scalable similarity search and AI applications.

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

    def get_collections_milvus(
        self,
        dbName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets the list of collections in Milvus, an open-source vector database built for scalable similarity search and AI applications.

        Args:
            dbName: Name of the target database.
        Returns:
            API response as a dictionary.
        """
        ...

    def milvus_create_backup(
        self,
        backupType: str,
        clusterId: str,
        dbCollections: List[Any],
    ) -> Dict[str, Any]:
        """Creates a backup snapshot of a specified Milvus cluster, capturing the current state of all its collections and data. Use this tool before performing high-risk operations such as dropping collections or bulk deletes, or on a scheduled basis to ensure data recoverability. Do not use this tool as a substitute for data export or migration. The backup is stored on Zilliz Cloud and can be referenced by its ID for future restoration or deletion.

        Args:
            backupType: The type of backup to perform. (required)
            clusterId: The ID of the Milvus cluster. (required)
            dbCollections:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def milvus_create_cluster(
        self,
        clusterName: str,
        projectId: str,
        regionId: str,
    ) -> Dict[str, Any]:
        """Creates a new free-tier Milvus cluster on Zilliz Cloud. Use this tool when you need to provision a new serverless Milvus environment to host collections and vector data. Do not use this tool if you already have an existing cluster and only need to create a collection within it — use milvus_create_collection instead. Note: this endpoint creates a free-tier cluster only; paid-tier clusters require a different provisioning flow.

        Args:
            clusterName: The name of the Milvus cluster. (required)
            projectId: The ID of the project associated with the Milvus cluster. (required)
            regionId: The ID of the region where the Milvus cluster is located. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def milvus_create_collection(
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
        """Creates a new collection within a specified Milvus cluster, defining its schema including fields, data types, and vector dimensions. Use this tool when you need to set up a new container for storing and searching vector entities. Do not use this tool to insert data into an existing collection — use milvus_insert_entities for that. This action creates a persistent, empty collection on the cluster.

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

    def milvus_delete_backup(
        self,
        backupId: str,
        clusterId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific backup of a Milvus cluster identified by cluster ID and backup ID. Use this tool when you need to remove an obsolete or unwanted backup to free up storage. Do not use this tool to delete the cluster itself or its live data — use milvus_drop_cluster for that. This action is irreversible; the deleted backup cannot be recovered.

        Args:
            backupId: The ID of the backup. (required)
            clusterId: The ID of the Milvus cluster. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def milvus_delete_entity(
        self,
        collectionName: str,
        filter: str,
        dbName: Optional[str] = None,
        partitionName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes one or more entities from a specified Milvus collection using a filter expression or primary key IDs. Use this tool when you need to remove specific records from a collection. Do not use this tool to drop an entire collection — use milvus_drop_collection instead. This action is irreversible; deleted entities cannot be recovered unless a backup exists.

        Args:
            collectionName: The name of the collection to search. (required)
            filter: A JSON string representing the filter expression for searching. (required)
            dbName: The name of the database containing the collection.
            partitionName: The name of the partition to search within.
        Returns:
            API response as a dictionary.
        """
        ...

    def milvus_drop_cluster(
        self,
        clusterId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified Milvus cluster from Zilliz Cloud, including all collections and data it contains. Use this tool only when you intend to completely remove a cluster and all its data. Do not use this tool if you only want to remove a single collection or entity — use milvus_drop_collection or milvus_delete_entity instead. This action is irreversible; all data in the cluster will be permanently lost.

        Args:
            clusterId: The ID of the Milvus cluster to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def milvus_drop_collection(
        self,
        collectionName: str,
        dbName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently drops (deletes) a specified collection and all its entities from a Milvus cluster. Use this tool when you need to completely remove a collection and all its data. Do not use this tool if you only want to remove specific entities — use milvus_delete_entity instead. This action is irreversible; all data in the collection will be permanently lost.

        Args:
            collectionName: The name of the collection. (required)
            dbName: The name of the database.
        Returns:
            API response as a dictionary.
        """
        ...

    def milvus_flush_collection(
        self,
        collectionName: str,
        dbName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Flushes a specified Milvus collection, persisting all buffered data in memory to storage to ensure it is searchable and durable. Use this tool after bulk insert operations when you need to guarantee that newly inserted data is immediately available for queries and searches. Do not use this tool during normal low-volume inserts, as Milvus flushes automatically. This operation may briefly impact collection performance.

        Args:
            collectionName: The name of the collection. (required)
            dbName: The name of the database.
        Returns:
            API response as a dictionary.
        """
        ...

    def milvus_get_entity(
        self,
        collectionName: str,
        id: List[Any],
        outputFields: Optional[List[Any]] = None,
        partitionNames: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves one or more specific entities from a Milvus collection by their primary key IDs. Use this tool when you know the exact entity ID(s) and need to fetch their field values directly. Do not use this tool for filter-based or vector similarity searches — use milvus_query_entities or a search tool instead. This is a read-only operation with no side effects.

        Args:
            collectionName: Name of the collection to query. (required)
            id: Array of entity IDs to retrieve. (required)
            outputFields: List of fields to be returned in the response.
            partitionNames: List of partition names to filter results.
        Returns:
            API response as a dictionary.
        """
        ...

    def milvus_insert_entities(
        self,
        collectionName: str,
        data: List[Any],
        dbName: str,
        partitionName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Inserts one or more vector entities (records) into a specified Milvus collection. Use this tool when you need to add new data points, including their vector embeddings and associated scalar fields, to a collection. Do not use this tool to update existing entities — delete and re-insert instead. This action writes data to the collection and is not reversible without a delete operation.

        Args:
            collectionName: Name of the collection. (required)
            data:  (required)
            dbName: Name of the database. (required)
            partitionName: Name of the partition to insert into (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def milvus_list_clusters(
        self,
        currentPage: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all Milvus clusters available in the Zilliz Cloud account. Use this tool when you need to discover existing clusters, retrieve their IDs, or check cluster availability before performing cluster-level operations. Do not use this tool to list collections within a cluster — use milvus_list_collections for that. This is a read-only operation with no side effects.

        Args:
            currentPage: The current page number for pagination.
            pageSize: The number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def milvus_list_collections(
        self,
        dbName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all collections within a specified Milvus cluster. Use this tool when you need to discover or enumerate available collections before performing operations on them. Do not use this tool to retrieve entity data from within a collection. This is a read-only operation with no side effects.

        Args:
            dbName: Name of the target database.
        Returns:
            API response as a dictionary.
        """
        ...

    def milvus_query_entities(
        self,
        collectionName: str,
        filter: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        outputFields: Optional[List[Any]] = None,
        partitionNames: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Queries entities from a specified Milvus collection using scalar filter expressions. Use this tool when you need to retrieve entities that match a boolean filter condition (e.g., field == value) from a collection. Do not use this tool for vector similarity search — use a dedicated search tool for that. Does not modify data.

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

