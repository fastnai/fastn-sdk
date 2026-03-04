"""Fastn Bonsai Elasticsearch connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _BonsaiElasticsearchSearchIndicesQuery(TypedDict, total=False):
    match_all: Dict[str, Any]

class BonsaiElasticsearchConnector:
    """Bonsai Elasticsearch connector ().

    Provides 5 tools.
    """

    def bonsai_elasticsearch_add_index_document(
        self,
        body: Dict[str, Any],
        id: str,
        indexName: str,
    ) -> Dict[str, Any]:
        """Adds a single document to an existing Elasticsearch index on Bonsai. Use this to store a new document under a specified index and document ID so it becomes available for future search and retrieval. Do not use this to create an index (use bonsai_elasticsearch_create_index instead) or to update an existing document in bulk. This operation writes data to the index and cannot be undone without a separate delete call.

        Args:
            body: Body of the request for Bonsai Elasticsearch. (required)
            id: ID of the document within the Elasticsearch index. (required)
            indexName: Name of the Elasticsearch index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bonsai_elasticsearch_create_index(
        self,
        index: str,
    ) -> Dict[str, Any]:
        """Creates a new Elasticsearch index on Bonsai with the specified name and optional configuration. Use this before adding documents to an index that does not yet exist. Do not use this to add documents to an existing index (use bonsai_elasticsearch_add_index_document instead). Creating an index with the same name as an existing one will return an error.

        Args:
            index: Name of the Elasticsearch index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bonsai_elasticsearch_delete_indices(
        self,
        index: str,
    ) -> Dict[str, Any]:
        """Permanently deletes one or more Elasticsearch indices on Bonsai, removing all documents and configuration stored within them. Use this when indices are no longer needed and must be fully removed. Do not use this to remove individual documents (use a document-level delete instead). This action is irreversible — all data in the deleted indices cannot be recovered.

        Args:
            index: Name of the Elasticsearch index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bonsai_elasticsearch_get_index(
        self,
        index: str,
    ) -> Dict[str, Any]:
        """Retrieves configuration and metadata details for a specific Elasticsearch index on Bonsai, such as mappings, settings, and aliases. Use this to inspect an index before querying or modifying it. Do not use this to search for documents within an index (use bonsai_elasticsearch_search_indices instead). This is a read-only operation with no side effects.

        Args:
            index: Index name in Bonsai Elasticsearch. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bonsai_elasticsearch_search_indices(
        self,
        index: str,
        query: Optional[_BonsaiElasticsearchSearchIndicesQuery] = None,
    ) -> Dict[str, Any]:
        """Executes a search query across one or more Elasticsearch indices on Bonsai and returns matching documents based on the specified criteria. Use this to find documents within known indices. Do not use this to list all indices (use bonsai_elasticsearch_get_index instead) or to add data. This is a read-only operation with no side effects.

        Args:
            index: Name of the Elasticsearch index to query. (required)
            query: Elasticsearch query parameters.
        Returns:
            API response as a dictionary.
        """
        ...

