"""Fastn Elasticsearch connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _CreateIndexMappings(TypedDict, total=False):
    properties: Dict[str, Any]

class _CreateIndexSettings(TypedDict, total=False):
    index: Dict[str, Any]

class _ElasticsearchBulkIndexCreate(TypedDict, total=False):
    _id: str

class _ElasticsearchSearchQuery(TypedDict, total=False):
    match: Dict[str, Any]
    term: Dict[str, Any]

class _ElasticsearchUpdateDocumentDoc(TypedDict, total=False):
    field_name: str

class ElasticsearchConnector:
    """Elasticsearch connector ().

    Provides 8 tools.
    """

    def create_index(
        self,
        indexName: str,
        mappings: Optional[_CreateIndexMappings] = None,
        settings: Optional[_CreateIndexSettings] = None,
    ) -> Dict[str, Any]:
        """Create a new index within the specified connector, enabling the organization and storage of related documents.

        Args:
            indexName: The name of the Elasticsearch index. (required)
            mappings: Mappings for the Elasticsearch index.
            settings: Settings for the Elasticsearch index.
        Returns:
            API response as a dictionary.
        """
        ...

    def elasticsearch_bulk_index(
        self,
        create: _ElasticsearchBulkIndexCreate,
        indexName: str,
    ) -> Dict[str, Any]:
        """Submits multiple documents for indexing in a single batch request to a specified Elasticsearch index (POST /_bulk). Use this when you need to index, update, or delete large numbers of documents efficiently in one API call. Prefer this over calling elasticsearch_create_document or elasticsearch_update_document repeatedly for bulk operations. This operation mutates index data; deletions within the bulk request are irreversible.

        Args:
            create: Parameters for creating a new document. (required)
            indexName: Name of the Elasticsearch index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elasticsearch_create_document(
        self,
        body: Dict[str, Any],
        indexName: str,
    ) -> Dict[str, Any]:
        """Adds a new document to a specified Elasticsearch index (POST /{indexName}/_doc), automatically assigning a document ID. Use this when you need to insert a single new document into an index. Do not use this for bulk insertions — use elasticsearch_bulk_index instead. Do not use this to update an existing document — use elasticsearch_update_document instead. This operation mutates index data and adds a new record.

        Args:
            body: Request body for the Elasticsearch API.  This may vary depending on the specific Elasticsearch endpoint. (required)
            indexName: Name of the Elasticsearch index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elasticsearch_get_index(
        self,
        indexName: str,
        all: Optional[str] = None,
        allow_no_indices: Optional[str] = None,
        closed: Optional[str] = None,
        expand_wildcards: Optional[str] = None,
        flat_settings: Optional[str] = None,
        hidden: Optional[str] = None,
        ignore_unavailable: Optional[str] = None,
        include_defaults: Optional[str] = None,
        include_type_name: Optional[str] = None,
        local: Optional[str] = None,
        master_timeout: Optional[str] = None,
        none: Optional[str] = None,
        open: Optional[str] = None,
        pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed configuration for a specific Elasticsearch index (GET /{indexName}), including its mappings, settings, and aliases. Use this when you need to inspect an indexs field types, analyzers, or configuration before indexing documents or building queries. Do not use this to list all available indices — use elasticsearch_list_indices instead. This is a read-only operation with no side effects.

        Args:
            indexName: The name of the Elasticsearch index. (required)
            all: Return all indices.
            allow_no_indices: Allow the request to proceed even if no indices match.
            closed: Include closed indices in the response.
            expand_wildcards: Whether to expand wildcard expressions.
            flat_settings: Return settings in a flattened format.
            hidden: Include hidden indices in the response.
            ignore_unavailable: Ignore unavailable indices.
            include_defaults: Include default settings in the response.
            include_type_name: Include the type name in the response.
            local: Return only local indices.
            master_timeout: Timeout for connecting to the master node.
            none: No specific indices.
            open: Include open indices in the response.
            pretty: Return a formatted JSON response.
        Returns:
            API response as a dictionary.
        """
        ...

    def elasticsearch_list_indices(
        self,
        indexName: str,
        bytes: Optional[str] = None,
        expand_wildcards: Optional[str] = None,
        format: Optional[str] = None,
        h: Optional[str] = None,
        health: Optional[str] = None,
        help: Optional[str] = None,
        include_unloaded_segments: Optional[str] = None,
        local: Optional[str] = None,
        master_timeout: Optional[str] = None,
        pri: Optional[str] = None,
        s: Optional[str] = None,
        time: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all indices available in the Elasticsearch cluster using the CAT indices API (GET /_cat/indices). Returns a summary overview of each index including health status, document count, and storage size. Use this when you need to discover what indices exist before performing index-level operations. Do not use this to retrieve detailed index mappings or settings — use elasticsearch_get_index instead. This is a read-only operation with no side effects.

        Args:
            indexName: Name of the Elasticsearch index. (required)
            bytes: Bytes parameter for the request.
            expand_wildcards: Expand wildcards option.
            format: Format of the response.
            h: h parameter for the request.
            health: Health parameter for the request.
            help: Help parameter for the request.
            include_unloaded_segments: Include unloaded segments option.
            local: Local parameter for the request.
            master_timeout: Master timeout for the request.
            pri: Primary shard parameter.
            s: s parameter for the request.
            time: Time parameter for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def elasticsearch_search(
        self,
        query: _ElasticsearchSearchQuery,
        allow_no_indices: Optional[str] = None,
        allow_partial_search_results: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for documents in the specified connector context, allowing for filtering and retrieval of relevant data using Elasticsearch query DSL. Use this for general search operations across the cluster or multiple indices. Do not use this if you need to search within a single known index with explicit index specification — use elasticsearch_search_index instead. This is a read-only operation with no side effects.

        Args:
            query:  (required)
            allow_no_indices: 
            allow_partial_search_results: 
        Returns:
            API response as a dictionary.
        """
        ...

    def elasticsearch_search_index(
        self,
        indexName: str,
        pretty: Optional[str] = None,
        size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a search query against a specific Elasticsearch index (POST /{indexName}/_search) and returns documents matching the specified criteria. Use this when you need to search within a known, single index using query DSL (e.g., match, term, range filters). Do not use this for cross-index searches — use elasticsearch_search instead. This is a read-only operation with no side effects.

        Args:
            indexName: Name of the Elasticsearch index to query. (required)
            pretty: Format the Elasticsearch response to be more human-readable.
            size: Number of results to return in the Elasticsearch query.
        Returns:
            API response as a dictionary.
        """
        ...

    def elasticsearch_update_document(
        self,
        groupId: str,
        indexName: str,
        doc: Optional[_ElasticsearchUpdateDocumentDoc] = None,
    ) -> Dict[str, Any]:
        """Updates an existing document within a specified Elasticsearch index using a partial update (POST /_update). Use this when you need to modify one or more fields of an already-indexed document without replacing it entirely. Requires the index name and document ID. Do not use this to create a new document or to replace a document in full — use elasticsearch_create_document or a full index operation instead. This operation mutates data in the index and cannot be undone automatically.

        Args:
            groupId: Group ID for the Elasticsearch request (if applicable). (required)
            indexName: Name of the Elasticsearch index. (required)
            doc: The document to be indexed in Elasticsearch.
        Returns:
            API response as a dictionary.
        """
        ...

