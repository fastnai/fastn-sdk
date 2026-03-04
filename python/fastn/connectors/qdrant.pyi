"""Fastn Qdrant connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _QdrantCreateCollectionVectors(TypedDict, total=False):
    datatype: str
    distance: str
    hnsw_config: Dict[str, Any]
    multivector_config: Dict[str, Any]
    on_disk: bool
    quantization_config: Dict[str, Any]
    size: int

class _QdrantCreateCollectionHnswConfig(TypedDict, total=False):
    ef_construct: int
    full_scan_threshold: int
    m: int
    max_indexing_threads: int
    on_disk: bool
    payload_m: int

class _QdrantCreateCollectionInitFrom(TypedDict, total=False):
    collection: str

class _QdrantCreateCollectionOptimizersConfig(TypedDict, total=False):
    default_segment_number: int
    deleted_threshold: float
    flush_interval_sec: int
    indexing_threshold: int
    max_optimization_threads: str
    max_segment_size: int
    memmap_threshold: int
    vacuum_min_vector_number: int

class _QdrantCreateCollectionQuantizationConfig(TypedDict, total=False):
    scalar: Dict[str, Any]

class _QdrantCreateCollectionSparseVectors(TypedDict, total=False):
    key_0: Dict[str, Any]
    key_1: Dict[str, Any]

class _QdrantCreateCollectionStrictModeConfig(TypedDict, total=False):
    condition_max_size: int
    enabled: bool
    filter_max_conditions: int
    max_collection_payload_size_bytes: int
    max_collection_vector_size_bytes: int
    max_points_count: int
    max_query_limit: int
    max_timeout: int
    multivector_config: Dict[str, Any]
    read_rate_limit: int
    search_allow_exact: bool
    search_max_hnsw_ef: int
    search_max_oversampling: float
    sparse_config: Dict[str, Any]
    unindexed_filtering_retrieve: bool
    unindexed_filtering_update: bool
    upsert_max_batchsize: int
    write_rate_limit: int

class _QdrantCreateCollectionWalConfig(TypedDict, total=False):
    wal_capacity_mb: int
    wal_retain_closed: int
    wal_segments_ahead: int

class _QdrantDeleteVectorsFilter(TypedDict, total=False):
    min_should: Dict[str, Any]
    must: List[Any]
    must_not: List[Any]
    should: List[Any]

class _QdrantUpdateCollectionHnswConfig(TypedDict, total=False):
    ef_construct: int
    full_scan_threshold: int
    m: int
    max_indexing_threads: int
    on_disk: bool
    payload_m: int

class _QdrantUpdateCollectionOptimizersConfig(TypedDict, total=False):
    default_segment_number: int
    deleted_threshold: float
    flush_interval_sec: int
    indexing_threshold: int
    max_optimization_threads: str
    max_segment_size: int
    memmap_threshold: int
    vacuum_min_vector_number: int

class _QdrantUpdateCollectionParams(TypedDict, total=False):
    on_disk_payload: str
    read_fan_out_factor: int
    replication_factor: int
    write_consistency_factor: int

class _QdrantUpdateCollectionQuantizationConfig(TypedDict, total=False):
    scalar: Dict[str, Any]

class _QdrantUpdateCollectionSparseVectors(TypedDict, total=False):
    key_0: Dict[str, Any]

class _QdrantUpdateCollectionStrictModeConfig(TypedDict, total=False):
    condition_max_size: int
    enabled: bool
    filter_max_conditions: int
    max_collection_payload_size_bytes: int
    max_collection_vector_size_bytes: int
    max_points_count: int
    max_query_limit: int
    max_timeout: int
    multivector_config: Dict[str, Any]
    read_rate_limit: int
    search_allow_exact: bool
    search_max_hnsw_ef: int
    search_max_oversampling: float
    sparse_config: Dict[str, Any]
    unindexed_filtering_retrieve: bool
    unindexed_filtering_update: bool
    upsert_max_batchsize: int
    write_rate_limit: int

class _QdrantUpdateCollectionVectors(TypedDict, total=False):
    key_0: Dict[str, Any]
    key_1: Dict[str, Any]
    key_2: Dict[str, Any]
    key_3: Dict[str, Any]

class QdrantConnector:
    """Qdrant connector ().

    Provides 11 tools.
    """

    def qdrant_create_collection(
        self,
        collectionName: str,
        vectors: _QdrantCreateCollectionVectors,
        hnsw_config: Optional[_QdrantCreateCollectionHnswConfig] = None,
        init_from: Optional[_QdrantCreateCollectionInitFrom] = None,
        on_disk_payload: Optional[str] = None,
        optimizers_config: Optional[_QdrantCreateCollectionOptimizersConfig] = None,
        quantization_config: Optional[_QdrantCreateCollectionQuantizationConfig] = None,
        replication_factor: Optional[str] = None,
        shard_number: Optional[str] = None,
        sharding_method: Optional[str] = None,
        sparse_vectors: Optional[_QdrantCreateCollectionSparseVectors] = None,
        strict_mode_config: Optional[_QdrantCreateCollectionStrictModeConfig] = None,
        timeout: Optional[str] = None,
        wal_config: Optional[_QdrantCreateCollectionWalConfig] = None,
        write_consistency_factor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new collection in Qdrant with a specified name and vector configuration, such as vector size and distance metric. Use this tool when setting up a new namespace for storing embeddings before upserting points. Do not use this tool if the collection already exists; use the update collection tool to modify an existing collections configuration. This operation provisions a new collection resource and cannot be undone without explicitly deleting the collection.

        Args:
            collectionName: Name of the collection to create. (required)
            vectors: Configuration for the vector field. (required)
            hnsw_config: Configuration for HNSW index.
            init_from: Initialize collection from another collection.
            on_disk_payload: Whether to store payloads on disk.
            optimizers_config: Configuration for collection optimizers.
            quantization_config: Configuration for vector quantization.
            replication_factor: Replication factor for the collection.
            shard_number: Number of shards for the collection.
            sharding_method: Sharding method to use.
            sparse_vectors: Configuration for sparse vectors.
            strict_mode_config: Configuration for strict mode.
            timeout: Timeout for the request.
            wal_config: Configuration for Write-Ahead Log.
            write_consistency_factor: Write consistency factor for the collection.
        Returns:
            API response as a dictionary.
        """
        ...

    def qdrant_delete_collection(
        self,
        collectionName: str,
        timeout: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an entire collection from Qdrant, including all of its points, vectors, and configuration. Use this tool only when a collection and all its data are no longer needed. Do not use this tool to remove individual points or vectors; use the delete points or delete vectors tools instead. This operation is irreversible — all data within the collection is permanently destroyed and cannot be recovered.

        Args:
            collectionName: The name of the collection to interact with. (required)
            timeout: Timeout for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def qdrant_delete_points(
        self,
        collectionName: str,
        points: List[Any],
        ordering: Optional[str] = None,
        shard_key: Optional[str] = None,
        wait: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently removes specific points from a named Qdrant collection by their point IDs or filter conditions. Use this tool when stored data points are no longer needed or must be purged. Do not use this tool to remove only the vector values while keeping the point; use the delete vectors tool instead. This operation is irreversible — deleted points and their payloads cannot be recovered.

        Args:
            collectionName:  (required)
            points:  (required)
            ordering: 
            shard_key: 
            wait: 
        Returns:
            API response as a dictionary.
        """
        ...

    def qdrant_delete_vectors(
        self,
        collectionName: str,
        points: List[Any],
        vectors: List[Any],
        filter: Optional[_QdrantDeleteVectorsFilter] = None,
        ordering: Optional[str] = None,
        shard_key: Optional[str] = None,
        wait: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes specific named vectors from points in a Qdrant collection without removing the points themselves. Use this tool when you need to clear vector data for particular vector names on existing points, for example when updating embedding models. Do not use this tool if you intend to remove the entire point record; use the delete points tool instead. This operation is irreversible — deleted vectors cannot be recovered.

        Args:
            collectionName: The name of the collection to interact with. (required)
            points: An array of point IDs. (required)
            vectors: An array of vectors representing the points. (required)
            filter: Filtering criteria for point selection.
            ordering: Specifies the ordering of results.
            shard_key: Key used for sharding.
            wait: Specifies whether to wait for asynchronous operations.
        Returns:
            API response as a dictionary.
        """
        ...

    def qdrant_get_collection(
        self,
        collectionName: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed configuration and status information for a single named Qdrant collection, including vector parameters, point count, and indexing status. Use this tool to inspect a collections settings or verify it exists before performing operations on it. Do not use this tool to list all available collections; use the list collections tool instead. This is a read-only operation with no side effects.

        Args:
            collectionName: The name of the collection to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def qdrant_get_point(
        self,
        collectionName: str,
        pointId: str,
        consistency: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a single point by its ID from a named Qdrant collection, including its vector and payload data. Use this tool when you need the full record for one specific point. Do not use this tool to retrieve multiple points at once; use the get points tool for batch retrieval. This is a read-only operation with no side effects.

        Args:
            collectionName: The name of the collection. (required)
            pointId: The ID of the point. (required)
            consistency: Specifies the consistency level for the operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def qdrant_get_points(
        self,
        collectionName: str,
        ids: List[Any],
        consistency: Optional[str] = None,
        shard_key: Optional[str] = None,
        timeout: Optional[str] = None,
        with_payload: Optional[bool] = None,
        with_vector: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves a batch of points from a named Qdrant collection by their IDs, returned in a single response. Use this tool when you need to fetch multiple specific points and their payloads or vectors by ID. Do not use this tool for similarity or semantic search; use a search tool for nearest-neighbor queries. Note: despite using HTTP POST, this is a read-only retrieval operation with no side effects.

        Args:
            collectionName: Name of the collection. (required)
            ids: List of IDs to retrieve. (required)
            consistency: Consistency level for the request.
            shard_key: Shard key for the request.
            timeout: Timeout for the request.
            with_payload: Include payload in the response.
            with_vector: Include vector in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def qdrant_list_collections(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all collections available in the Qdrant instance. Use this tool to discover what collections exist before performing collection-level operations such as get, update, or delete. Do not use this tool to retrieve the details or configuration of a specific collection; use the get collection tool instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def qdrant_update_collection(
        self,
        collectionName: str,
        hnsw_config: Optional[_QdrantUpdateCollectionHnswConfig] = None,
        optimizers_config: Optional[_QdrantUpdateCollectionOptimizersConfig] = None,
        params: Optional[_QdrantUpdateCollectionParams] = None,
        quantization_config: Optional[_QdrantUpdateCollectionQuantizationConfig] = None,
        sparse_vectors: Optional[_QdrantUpdateCollectionSparseVectors] = None,
        strict_mode_config: Optional[_QdrantUpdateCollectionStrictModeConfig] = None,
        timeout: Optional[str] = None,
        vectors: Optional[_QdrantUpdateCollectionVectors] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration parameters of an existing Qdrant collection, such as optimizer settings, replication factor, or indexing thresholds. Use this tool when you need to tune collection-level settings without recreating the collection. Do not use this tool to modify point data or vector values; use the upsert points or update vectors tools instead. Configuration changes may trigger background reindexing operations that affect query performance temporarily.

        Args:
            collectionName: Name of the collection to interact with. (required)
            hnsw_config: HNSW index configuration.
            optimizers_config: Configuration for optimizers.
            params: Collection parameters.
            quantization_config: Quantization configuration.
            sparse_vectors: Sparse vectors configuration.
            strict_mode_config: Configuration for strict mode.
            timeout: Request timeout.
            vectors: Vectors data for the points.
        Returns:
            API response as a dictionary.
        """
        ...

    def qdrant_update_vectors(
        self,
        collectionName: str,
        points: List[Any],
        ordering: Optional[str] = None,
        shard_key: Optional[str] = None,
        wait: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the vector values for existing points in a specified Qdrant collection. Use this tool when embeddings need to be refreshed or corrected for points that already exist in the collection. Do not use this tool to add new points or update payload metadata; use the upsert points tool for inserting new points or updating payloads. This operation overwrites the existing vector values for the specified points.

        Args:
            collectionName: The name of the collection to operate on. (required)
            points:  (required)
            ordering: Specifies the ordering of results.
            shard_key: Shard key for sharded collections.
            wait: Specifies whether to wait for asynchronous operations to complete.
        Returns:
            API response as a dictionary.
        """
        ...

    def qdrant_upsert_points(
        self,
        collectionName: str,
        points: List[Any],
        ordering: Optional[str] = None,
        shard_key: Optional[str] = None,
        wait: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Inserts new points or updates existing points in a named Qdrant collection. If a point with the given ID already exists, it is overwritten; otherwise, a new point is created. Use this tool when ingesting embeddings and associated payload data into a collection. Do not use this tool to update only the vector without touching the payload, as it will overwrite the entire point record. This operation modifies stored data and overwrites existing points with matching IDs.

        Args:
            collectionName: The name of the collection. (required)
            points:  (required)
            ordering: Specify the ordering of results.
            shard_key: Shard key for sharded collections.
            wait: Wait for operation completion.
        Returns:
            API response as a dictionary.
        """
        ...

