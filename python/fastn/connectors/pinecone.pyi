"""Fastn Pinecone connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _PineconeCreateIndexSpec(TypedDict, total=False):
    serverless: Dict[str, Any]

class _PineconeCreateIndexTags(TypedDict, total=False):
    environment: str
    example: str

class _PineconeEmbedDataParameters(TypedDict, total=False):
    input_type: str
    truncate: str

class _PineconeQueryVectorsFilter(TypedDict, total=False):
    genre: Dict[str, Any]

class _PineconeRerankDocumentsParameters(TypedDict, total=False):
    truncate: str

class _PineconeStartImportErrormode(TypedDict, total=False):
    onError: str

class _PineconeUpdateVectorSetmetadata(TypedDict, total=False):
    type: str

class PineconeConnector:
    """Pinecone connector ().

    Provides 36 tools.
    """

    def pinecone_cancel_import(
        self,
        XPineconeAPIVersion: str,
        indexHost: str,
    ) -> Dict[str, Any]:
        """Cancels an in-progress bulk import operation on a Pinecone index by import ID. Use this to stop an import that was started in error or is no longer needed. Vectors already written before cancellation may persist in the index. Do not use this to cancel a completed import — only active imports can be cancelled. This operation cannot be undone.

        Args:
            XPineconeAPIVersion: The Pinecone API version. (required)
            indexHost: The Pinecone index host. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_chat_prompt(
        self,
        assistantName: str,
        messages: List[Any],
        model: str,
        stream: bool,
    ) -> Dict[str, Any]:
        """Sends a chat message to a named Pinecone assistant and retrieves its response. Use this as the primary way to converse with a Pinecone assistant, asking questions or issuing prompts grounded in the assistants uploaded files. Do not use this when an OpenAI-compatible response schema is required — use pinecone_open_ai_compatible_chat instead. Returns the assistants generated reply.

        Args:
            assistantName: Name of the Pinecone assistant. (required)
            messages:  (required)
            model: Specifies the Pinecone model to use. (required)
            stream: Indicates whether to stream the response. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_create_assistant(
        self,
        instructions: str,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new Pinecone assistant with the specified name and configuration. Use this to provision a fresh assistant instance that can be loaded with files and used for grounded chat interactions. Do not use this to modify an existing assistant — use pinecone_update_assistant for that. Returns the newly created assistant object including its name and initial status.

        Args:
            instructions: Instructions for the Pinecone operation. (required)
            name: Name for the Pinecone operation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_create_collection(
        self,
        XPineconeAPIVersion: str,
        name: str,
        source: str,
    ) -> Dict[str, Any]:
        """Creates a new Pinecone collection as a static snapshot from an existing index. Use this to archive an index state or prepare data for index migration. Do not use this to create a queryable index — use pinecone_create_index for that. Returns the newly created collection object including its name and initial status.

        Args:
            XPineconeAPIVersion: The Pinecone API version. (required)
            name: Name of the entity. (required)
            source: Source of the data. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_create_index(
        self,
        XPineconeAPIVersion: str,
        name: str,
        deletion_protection: Optional[str] = None,
        dimension: Optional[int] = None,
        metric: Optional[str] = None,
        spec: Optional[_PineconeCreateIndexSpec] = None,
        tags: Optional[_PineconeCreateIndexTags] = None,
    ) -> Dict[str, Any]:
        """Creates a new Pinecone index with the specified name, dimension, and similarity metric. Use this to provision a vector index before upserting or querying data. Do not use this to update an existing index — use pinecone_update_index for that. Returns the newly created index object including its host and status.

        Args:
            XPineconeAPIVersion: The version of the Pinecone API being used. (required)
            name: The name of the Pinecone index. (required)
            deletion_protection: Specifies whether deletion protection is enabled for the index.
            dimension: The dimensionality of the vectors in the index.
            metric: The metric to use for the index.
            spec: Specifications for the Pinecone index.
            tags: Tags associated with the index.
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_delete_assistant(
        self,
        NameAssistant: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a named Pinecone assistant and all associated data. Use this to remove an assistant that is no longer needed. This action is irreversible — the assistant, its configuration, and all indexed file data will be permanently destroyed. Do not use this if you only want to update assistant properties — use pinecone_update_assistant instead.

        Args:
            NameAssistant: Name of the assistant  in the Pinecone API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_delete_assistant_file(
        self,
        assistantName: str,
        fileId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific file from a named Pinecone assistant by file ID. Use this to remove a file that is no longer needed or was uploaded in error. This action is irreversible — the file and its indexed content will be permanently removed from the assistant. Do not use this if you only want to update file metadata — delete and re-upload instead.

        Args:
            assistantName: Name of the assistant. (required)
            fileId: Identifier of the file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_delete_assistant_file_v2(
        self,
        assistantName: str,
        fileId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific file from a named Pinecone assistant by file ID (duplicate endpoint variant). Use this to remove a file that is no longer needed or was uploaded in error. This action is irreversible — the file and its indexed content will be permanently removed from the assistant. Prefer pinecone_delete_assistant_file unless this variant is explicitly required.

        Args:
            assistantName: Name of the assistant. (required)
            fileId: ID of the file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_delete_collection(
        self,
        XPineconeAPIVersion: str,
        collectionName: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a named Pinecone collection. Use this to remove a static snapshot of an index that is no longer needed. This action is irreversible — the collection and all its stored vector data will be permanently destroyed. Do not use this to delete an active index — use pinecone_delete_index for that.

        Args:
            XPineconeAPIVersion: The Pinecone API version to use. (required)
            collectionName: The name of the Pinecone collection. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_delete_index(
        self,
        XPineconeAPIVersion: str,
        indexName: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a Pinecone index and all vectors stored within it. Use this to decommission an index that is no longer needed. This action is irreversible — all vector data in the index will be permanently destroyed. Do not use this to remove a collection snapshot — use pinecone_delete_collection for that.

        Args:
            XPineconeAPIVersion: The Pinecone API version to use. (required)
            indexName: The name of the Pinecone index to use. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_delete_vectors(
        self,
        XPineconeAPIVersion: str,
        ids: List[Any],
        indexHost: str,
        namespace: str,
    ) -> Dict[str, Any]:
        """Permanently deletes one or more vectors from a Pinecone index by ID, or deletes all vectors in a namespace. Use this to remove stale or incorrect vectors from an index. This action is irreversible — deleted vectors cannot be recovered. Do not use this to remove an entire index — use pinecone_delete_index for that.

        Args:
            XPineconeAPIVersion: Specifies the version of the Pinecone API to use. (required)
            ids: An array of IDs for the vectors. (required)
            indexHost: The hostname of the Pinecone index. (required)
            namespace: The namespace for the Pinecone index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_embed_data(
        self,
        XPineconeAPIVersion: str,
        inputs: Optional[List[Any]] = None,
        model: Optional[str] = None,
        parameters: Optional[_PineconeEmbedDataParameters] = None,
    ) -> Dict[str, Any]:
        """Generates vector embeddings for provided text or data using Pinecones hosted embedding model. Use this to convert raw text into dense vector representations before upserting them into a Pinecone index. Do not use this to store the resulting vectors — use pinecone_upsert_vectors for that. Returns an array of embedding vectors corresponding to the input data.

        Args:
            XPineconeAPIVersion: Specifies the version of the Pinecone API. (required)
            inputs: 
            model: Specifies the Pinecone model to use.
            parameters: Additional parameters for the Pinecone API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_evaluate_answer(
        self,
        answer: str,
        ground_truth_answer: str,
        question: str,
    ) -> Dict[str, Any]:
        """Evaluates the alignment of a generated answer against expected criteria using Pinecones evaluation metrics API. Use this to measure answer quality, factual alignment, or relevance scores for a given response. Do not use this to generate answers — use pinecone_chat_prompt for that. Returns alignment metrics indicating how well the answer matches the expected criteria.

        Args:
            answer: The provided answer to the question. (required)
            ground_truth_answer: The correct answer to the question. (required)
            question: The question to be processed by the Pinecone API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_get_assistant(
        self,
        assistantName: str,
    ) -> Dict[str, Any]:
        """Retrieves the current status and configuration details of a specific Pinecone assistant identified by name. Use this to check whether an assistant is ready, view its settings, or confirm it exists before performing operations. Do not use this to list all assistants — use pinecone_list_assistants for that. Returns assistant metadata including status and configuration.

        Args:
            assistantName: Name of the assistant for the Pinecone API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_get_assistant_context(
        self,
        assistantName: str,
        query: str,
    ) -> Dict[str, Any]:
        """Retrieves the context chunks used by a named Pinecone assistant to answer questions. Use this when you need to inspect the source passages or documents that underpin an assistants knowledge for a given query. Do not use this to send a chat message or generate a response — use pinecone_chat_prompt or pinecone_open_ai_compatible_chat for that. Returns retrieved context segments associated with the specified assistant.

        Args:
            assistantName: Name of the Pinecone assistant. (required)
            query: The search query to be executed on Pinecone. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_get_assistant_file(
        self,
        assistantName: str,
        fileId: str,
    ) -> Dict[str, Any]:
        """Retrieves metadata and status details for a specific file uploaded to a named Pinecone assistant, identified by file ID. Use this to check a files processing status, name, size, or other properties. Do not use this to list all files — use pinecone_list_assistant_files for that. Returns file metadata including status and identifiers.

        Args:
            assistantName: Name of the Pinecone assistant. (required)
            fileId: ID of the file to process in the Pinecone API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_get_collection(
        self,
        XPineconeAPIVersion: str,
        collectionName: str,
    ) -> Dict[str, Any]:
        """Retrieves the description, status, and specifications of a specific Pinecone collection identified by name. Use this to inspect a collections size, dimension, vector count, or readiness before creating an index from it. Do not use this to list all collections — use pinecone_list_collections for that. Returns collection metadata.

        Args:
            XPineconeAPIVersion: Specifies the version of the Pinecone API. (required)
            collectionName: The name of the Pinecone collection. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_get_import(
        self,
        XPineconeAPIVersion: str,
        indexHost: str,
    ) -> Dict[str, Any]:
        """Retrieves the status and details of a specific bulk import operation on a Pinecone index by import ID. Use this to monitor import progress, check for errors, or confirm completion. Do not use this to list all imports — use pinecone_list_imports for that. Returns import metadata including status and record counts.

        Args:
            XPineconeAPIVersion: The Pinecone API version. (required)
            indexHost: The hostname of your Pinecone index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_get_index(
        self,
        XPineconeAPIVersion: str,
        indexName: str,
    ) -> Dict[str, Any]:
        """Retrieves the configuration and status of a specific Pinecone index identified by name. Use this to inspect index settings such as dimension, metric, pod type, and readiness state before querying or writing data. Do not use this to list all indexes — use pinecone_list_indexes for that. Returns full index metadata.

        Args:
            XPineconeAPIVersion: Pinecone API version. (required)
            indexName: Name of the Pinecone index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_get_index_stats(
        self,
        XPineconeAPIVersion: str,
        indexHost: str,
    ) -> Dict[str, Any]:
        """Retrieves statistics for a Pinecone index including total vector count, namespace breakdown, and dimensionality. Use this to monitor index usage, verify upsert operations, or check namespace-level vector counts. Do not use this to retrieve index configuration — use pinecone_get_index for that. Returns statistical metadata about the index.

        Args:
            XPineconeAPIVersion: Pinecone API version. (required)
            indexHost: Hostname of the Pinecone index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_get_vectors(
        self,
        XPineconeAPIVersion: str,
        indexHost: str,
        ids: Optional[List[Any]] = None,
        namespace: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches one or more vectors from a Pinecone index by their IDs, returning their full vector values and metadata. Use this when you know specific vector IDs and need their complete data. Do not use this to search for similar vectors — use pinecone_query_vectors for similarity search. Returns a map of vector IDs to vector objects.

        Args:
            XPineconeAPIVersion: The version of the Pinecone API being used. (required)
            indexHost: The host of the Pinecone index. (required)
            ids: 
            namespace: 
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_list_assistant_files(
        self,
        assistantName: str,
    ) -> Dict[str, Any]:
        """Lists all files uploaded to a named Pinecone assistant. Use this to enumerate available files, check their processing statuses, or find a specific file ID before performing operations like deletion or retrieval. Do not use this to retrieve metadata for a single file — use pinecone_get_assistant_file for that. Returns an array of file metadata objects.

        Args:
            assistantName: Name of the assistant for the Pinecone API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_list_assistants(
        self,
    ) -> Dict[str, Any]:
        """Lists all Pinecone assistants available in the current project. Use this to discover existing assistants, find their names, or verify an assistant exists before interacting with it. Do not use this to retrieve details for a single assistant — use pinecone_get_assistant for that. Returns an array of assistant metadata objects.
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_list_collections(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Lists all Pinecone collections available in the current project. Use this to discover existing collection snapshots, check their statuses, or find a collection name before creating an index from it. Do not use this to retrieve details for a single collection — use pinecone_get_collection for that. Returns an array of collection metadata objects.

        Args:
            XPineconeAPIVersion: Specifies the version of the Pinecone API being used. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_list_imports(
        self,
        XPineconeAPIVersion: Optional[str] = None,
        indexHost: Optional[str] = None,
        paginationToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all bulk import operations for a Pinecone index, including their statuses and details. Use this to monitor ongoing or historical import jobs, or to find a specific import ID. Do not use this to get details of a single import — use pinecone_get_import for that. Returns an array of import metadata objects.

        Args:
            XPineconeAPIVersion: 
            indexHost: 
            paginationToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_list_indexes(
        self,
    ) -> Dict[str, Any]:
        """Lists all Pinecone indexes available in the current project. Use this to discover existing indexes, retrieve their names and hosts, or verify an index exists before performing operations on it. Do not use this to retrieve details for a single index — use pinecone_get_index for that. Returns an array of index metadata objects.
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_list_vector_ids(
        self,
        XPineconeAPIVersion: str,
        indexHost: str,
        namespace: Optional[str] = None,
        prefix: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists the IDs of vectors stored in a Pinecone index, optionally filtered by namespace or prefix. Use this to enumerate vector IDs before fetching, updating, or deleting specific vectors. Do not use this to retrieve full vector values or metadata — use pinecone_get_vectors for that. Returns a paginated list of vector ID strings.

        Args:
            XPineconeAPIVersion: Pinecone API version. (required)
            indexHost: Host for the Pinecone index. (required)
            namespace: Namespace for the Pinecone index.
            prefix: Prefix for the Pinecone index.
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_open_ai_compatible_chat(
        self,
        assistantName: str,
        messages: List[Any],
    ) -> Dict[str, Any]:
        """Sends a chat completion request to a named Pinecone assistant using an OpenAI-compatible API format. Use this when the calling application expects an OpenAI-style chat completions response schema from a Pinecone assistant. Do not use this for non-OpenAI-compatible interactions — use pinecone_chat_prompt instead. Streams or returns a chat completion response from the specified assistant.

        Args:
            assistantName: Name of the Pinecone assistant to use. (required)
            messages:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_query_vectors(
        self,
        XPineconeAPIVersion: str,
        indexHost: str,
        filter: Optional[_PineconeQueryVectorsFilter] = None,
        includeValues: Optional[bool] = None,
        namespace: Optional[str] = None,
        topK: Optional[int] = None,
        vector: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Performs a similarity search on a Pinecone index by submitting a query vector and retrieving the nearest neighbors by score. Use this as the primary tool for semantic or nearest-neighbor search over indexed vectors. Do not use this to retrieve vectors by exact ID — use pinecone_get_vectors for that. Returns the top-k most similar vectors with their scores and optional metadata.

        Args:
            XPineconeAPIVersion: The version of the Pinecone API. (required)
            indexHost: The host of the Pinecone index. (required)
            filter: Filter criteria for the Pinecone query.
            includeValues: Whether to include vector values in the results.
            namespace: The namespace to query.
            topK: Number of top results to return.
            vector: The query vector.
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_rerank_documents(
        self,
        XPineconeAPIVersion: str,
        documents: Optional[List[Any]] = None,
        model: Optional[str] = None,
        parameters: Optional[_PineconeRerankDocumentsParameters] = None,
        query: Optional[str] = None,
        return_documents: Optional[bool] = None,
        top_n: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Re-scores and reorders a list of documents or passages relative to a query using Pinecones reranking model. Use this after an initial retrieval step to improve result relevance before presenting documents to a user or downstream model. Do not use this as a primary search or retrieval tool — it requires a pre-fetched candidate list. Returns documents sorted by their relevance scores.

        Args:
            XPineconeAPIVersion: Specifies the version of the Pinecone API. (required)
            documents: 
            model: Name of the Pinecone model to use.
            parameters: Additional parameters for the query.
            query: The search query string.
            return_documents: Whether to return the full documents in the results.
            top_n: The number of top results to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_start_import(
        self,
        XPineconeAPIVersion: str,
        indexHost: str,
        errorMode: Optional[_PineconeStartImportErrormode] = None,
        integrationId: Optional[str] = None,
        uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Starts a bulk import job to ingest vectors into a Pinecone index from an external data source. Use this to efficiently load large volumes of vector data without individual upsert calls. Do not use this for small or incremental vector writes — use pinecone_upsert_vectors instead. Returns the new import job ID and initial status, which can be monitored with pinecone_get_import.

        Args:
            XPineconeAPIVersion: Specify the Pinecone API version. (required)
            indexHost: Hostname of the Pinecone index. (required)
            errorMode: Specifies how errors are handled.
            integrationId: Identifier for the integration.
            uri: Uniform Resource Identifier.
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_update_assistant(
        self,
        assistantName: str,
        instructions: str,
    ) -> Dict[str, Any]:
        """Updates the configuration or metadata properties of an existing Pinecone assistant identified by name. Use this to modify assistant settings such as instructions or metadata without recreating it. Do not use this to delete an assistant — use pinecone_delete_assistant for that. Returns the updated assistant object.

        Args:
            assistantName: Name of the assistant for the Pinecone API request. (required)
            instructions: Instructions for the Pinecone API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_update_index(
        self,
        XPineconeAPIVersion: str,
        deletion_protection: str,
        indexName: str,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing Pinecone index, such as pod size or replicas, identified by index name. Use this to scale or reconfigure an index without deleting it. Do not use this to modify vector data — use pinecone_upsert_vectors or pinecone_update_vector for that. Returns the updated index configuration.

        Args:
            XPineconeAPIVersion: The Pinecone API version. (required)
            deletion_protection: Specifies deletion protection settings. (required)
            indexName: The name of the Pinecone index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_update_vector(
        self,
        XPineconeAPIVersion: str,
        id: str,
        indexHost: str,
        namespace: str,
        setMetadata: Optional[_PineconeUpdateVectorSetmetadata] = None,
        values: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the values or metadata of a specific vector in a Pinecone index, identified by its vector ID. Use this to correct or enrich an existing vector without deleting and re-upserting it. Do not use this to insert new vectors — use pinecone_upsert_vectors for that. Returns a confirmation of the update operation.

        Args:
            XPineconeAPIVersion: The version of the Pinecone API being used. (required)
            id: Unique identifier for the vector. (required)
            indexHost: The hostname of the Pinecone index. (required)
            namespace: The namespace for the index. (required)
            setMetadata: Metadata associated with the vector data.
            values: Array of numerical values representing the vector.
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_upload_assistant_file(
        self,
        assistantName: str,
        file: str,
    ) -> Dict[str, Any]:
        """Uploads a file to a named Pinecone assistant so it can be indexed and used as a knowledge source for chat interactions. Use this when you need to add new documents or data files to an assistants knowledge base. Do not use this to update an existing files content — delete the old file first, then upload the new version. Returns metadata for the newly uploaded file including its assigned file ID.

        Args:
            assistantName: Name of the assistant for the Pinecone API. (required)
            file: File data for the Pinecone API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pinecone_upsert_vectors(
        self,
        XPineconeAPIVersion: str,
        indexHost: str,
        namespace: Optional[str] = None,
        vectors: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Inserts new vectors or updates existing vectors in a Pinecone index. If a vector with the given ID already exists it will be overwritten; otherwise a new vector will be created. Use this for incremental or real-time vector writes. For large-scale bulk ingestion, prefer pinecone_start_import. Returns the number of vectors upserted.

        Args:
            XPineconeAPIVersion: Specify the Pinecone API version. (required)
            indexHost: Host for the Pinecone index. (required)
            namespace: Namespace for the index.
            vectors: 
        Returns:
            API response as a dictionary.
        """
        ...

