"""Fastn Nuclia connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _NucliaAskKnowledgeAuditMetadata(TypedDict, total=False):
    environment: str
    user: str

class _NucliaAskKnowledgeFilterExpression(TypedDict, total=False):
    field: Dict[str, Any]
    operator: str
    paragraph: Dict[str, Any]

class _NucliaUpdateResourceExtra(TypedDict, total=False):
    metadata: Dict[str, Any]

class _NucliaUpdateResourceMetadata(TypedDict, total=False):
    language: str
    languages: List[Any]
    metadata: Dict[str, Any]

class _NucliaUpdateResourceOrigin(TypedDict, total=False):
    collaborators: List[Any]
    created: str
    filename: str
    metadata: Dict[str, Any]
    modified: str
    path: str
    related: List[Any]
    source_id: str
    tags: List[Any]
    url: str

class _NucliaUpdateResourceProcessingOptions(TypedDict, total=False):
    ml_text: bool

class _NucliaUpdateResourceSecurity(TypedDict, total=False):
    access_groups: List[Any]

class _NucliaUpdateResourceUsermetadata(TypedDict, total=False):
    classifications: List[Any]
    relations: List[Any]

class NucliaConnector:
    """Nuclia connector ().

    Provides 6 tools.
    """

    def nuclia_ask_knowledge(
        self,
        kbId: str,
        query: str,
        audit_metadata: Optional[_NucliaAskKnowledgeAuditMetadata] = None,
        autofilter: Optional[bool] = None,
        chat_history: Optional[List[Any]] = None,
        citations: Optional[bool] = None,
        debug: Optional[bool] = None,
        extra_context: Optional[List[Any]] = None,
        features: Optional[List[Any]] = None,
        field_type_filter: Optional[List[Any]] = None,
        fields: Optional[List[Any]] = None,
        filter_expression: Optional[_NucliaAskKnowledgeFilterExpression] = None,
        filters: Optional[List[Any]] = None,
        generate_answer: Optional[bool] = None,
        generative_model: Optional[str] = None,
        highlight: Optional[bool] = None,
        keyword_filters: Optional[List[Any]] = None,
        max_tokens: Optional[int] = None,
        min_score: Optional[int] = None,
        prefer_markdown: Optional[bool] = None,
        prompt: Optional[str] = None,
        rag_strategies: Optional[List[Any]] = None,
        range_creation_end: Optional[str] = None,
        range_creation_start: Optional[str] = None,
        range_modification_end: Optional[str] = None,
        range_modification_start: Optional[str] = None,
        rank_fusion: Optional[str] = None,
        reranker: Optional[str] = None,
        show: Optional[List[Any]] = None,
        show_hidden: Optional[bool] = None,
        top_k: Optional[int] = None,
        vectorset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Submits a natural-language question to the Nuclia knowledge base and returns a generative AI answer grounded in the stored content. Use this tool when you need a synthesized, conversational response rather than raw search results. For raw document search, use nuclia_search_knowledge instead. Does not modify any data.

        Args:
            kbId: The ID of the knowledge base to search. (required)
            query: The search query string. (required)
            audit_metadata: Metadata for auditing purposes.
            autofilter: Enable automatic filtering.
            chat_history: 
            citations: Include citations in the response.
            debug: Enable debug mode.
            extra_context: Array of extra context strings.
            features: List of features to include in the results.
            field_type_filter: Filter by field type.
            fields: List of fields to return in the results.
            filter_expression: A structured filter expression for refining the search.
            filters: Array of additional filters.
            generate_answer: Generate a summarized answer.
            generative_model: Generative model to use.
            highlight: Enable highlighting of search terms.
            keyword_filters: Array of keyword filters.
            max_tokens: Maximum number of tokens for the generative model.
            min_score: Minimum score threshold for results.
            prefer_markdown: Prefer markdown format for the response.
            prompt: The prompt for the generative model.
            rag_strategies: 
            range_creation_end: End date for range filtering (creation).
            range_creation_start: Start date for range filtering (creation).
            range_modification_end: End date for range filtering (modification).
            range_modification_start: Start date for range filtering (modification).
            rank_fusion: Rank fusion strategy.
            reranker: Reranker model to use.
            show: List of fields to show in the response.
            show_hidden: Show hidden results.
            top_k: The number of top results to return.
            vectorset: The name of the vectorset to use for similarity search.
        Returns:
            API response as a dictionary.
        """
        ...

    def nuclia_delete_resource(
        self,
        kbId: str,
        resourceId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific resource from the Nuclia knowledge base by its resource ID. Use this tool only when a resource must be removed entirely. This action is irreversible—the resource cannot be recovered after deletion. Do not use this tool if you only need to update or deactivate a resource; use nuclia_update_resource instead.

        Args:
            kbId: The ID of the knowledge base. (required)
            resourceId: The ID of the specific resource within the knowledge base. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def nuclia_get_resource(
        self,
        kbId: str,
        resourceId: str,
        extracted: Optional[str] = None,
        field_type: Optional[str] = None,
        show: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single resource from the Nuclia knowledge base by its resource ID. Use this tool when you need full metadata and content details for one specific resource. To retrieve a list of multiple resources, use nuclia_list_resources instead. Does not modify any data.

        Args:
            kbId: The ID of the knowledge base to search. (required)
            resourceId: The ID of the resource to search within the knowledge base. (required)
            extracted: Specifies which fields to extract.
            field_type: Specifies the type of field.
            show: Specifies the fields to include in the search results.
        Returns:
            API response as a dictionary.
        """
        ...

    def nuclia_list_resources(
        self,
        kbId: str,
        page: Optional[str] = None,
        size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all resources stored in the Nuclia knowledge base. Use this tool when you need an overview of available resources. For detailed information about a single resource, use nuclia_get_resource instead. Does not modify any data.

        Args:
            kbId: The ID of the knowledge base. (required)
            page: The page number for pagination.
            size: The number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def nuclia_search_knowledge(
        self,
        kbId: str,
        query: str,
        autofilter: Optional[str] = None,
        debug: Optional[str] = None,
        features: Optional[str] = None,
        field_type: Optional[str] = None,
        filter_expression: Optional[str] = None,
        highlight: Optional[str] = None,
        min_score: Optional[str] = None,
        min_score_bm25: Optional[str] = None,
        min_score_semantic: Optional[str] = None,
        range_creation_end: Optional[str] = None,
        range_creation_start: Optional[str] = None,
        range_modification_end: Optional[str] = None,
        range_modification_start: Optional[str] = None,
        show: Optional[str] = None,
        show_hidden: Optional[str] = None,
        sort_field: Optional[str] = None,
        sort_limit: Optional[str] = None,
        sort_order: Optional[str] = None,
        top_k: Optional[str] = None,
        vectorset: Optional[str] = None,
        with_duplicates: Optional[str] = None,
        with_synonyms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for information across the Nuclia knowledge base using a query string. Use this tool when you need to retrieve relevant documents, passages, or resources matching a search query. Returns ranked results from the knowledge base. Does not generate a conversational answer—use nuclia_ask_knowledge for generative responses. Does not modify any data.

        Args:
            kbId: The ID of the knowledge base to search. (required)
            query: The search query string. (required)
            autofilter: Enable or disable automatic filtering.
            debug: Enable debug mode for detailed logging.
            features: Specify features to include in the search.
            field_type: Specify the type of field to search.
            filter_expression: A filter expression to refine search results.
            highlight: Enable or disable highlighting of search terms.
            min_score: The minimum score for a result to be returned.
            min_score_bm25: Minimum score using BM25 algorithm.
            min_score_semantic: Minimum score using semantic search algorithm.
            range_creation_end: End of the range for creation date filtering.
            range_creation_start: Start of the range for creation date filtering.
            range_modification_end: End of the range for modification date filtering.
            range_modification_start: Start of the range for modification date filtering.
            show: Specify fields to include in the results.
            show_hidden: Show hidden documents in results.
            sort_field: Field to sort results by.
            sort_limit: Limit the number of sorted results.
            sort_order: Order of sorting (asc or desc).
            top_k: Return only the top K results.
            vectorset: Specify the vector set to use for semantic search.
            with_duplicates: Include duplicate results.
            with_synonyms: Include results matching synonyms.
        Returns:
            API response as a dictionary.
        """
        ...

    def nuclia_update_resource(
        self,
        kbId: str,
        resourceId: str,
        title: str,
        conversations: Optional[Dict[str, Any]] = None,
        extra: Optional[_NucliaUpdateResourceExtra] = None,
        fieldmetadata: Optional[List[Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        hidden: Optional[bool] = None,
        links: Optional[Dict[str, Any]] = None,
        metadata: Optional[_NucliaUpdateResourceMetadata] = None,
        origin: Optional[_NucliaUpdateResourceOrigin] = None,
        processing_options: Optional[_NucliaUpdateResourceProcessingOptions] = None,
        security: Optional[_NucliaUpdateResourceSecurity] = None,
        slug: Optional[str] = None,
        summary: Optional[str] = None,
        texts: Optional[Dict[str, Any]] = None,
        thumbnail: Optional[str] = None,
        usermetadata: Optional[_NucliaUpdateResourceUsermetadata] = None,
    ) -> Dict[str, Any]:
        """Updates the properties of an existing resource in the Nuclia knowledge base using a partial PATCH request. Use this tool to modify metadata, content, or other fields of a resource identified by its resource ID. Only the fields provided will be updated; unspecified fields remain unchanged. To remove a resource entirely, use nuclia_delete_resource instead.

        Args:
            kbId: The ID of the knowledge base. (required)
            resourceId: The ID of the resource within the knowledge base. (required)
            title: The title of the resource. (required)
            conversations: Conversations associated with the resource.
            extra: Additional metadata.
            fieldmetadata: 
            files: Associated files.
            hidden: Whether the resource is hidden.
            links: Links associated with the resource.
            metadata: Additional metadata associated with the resource.
            origin: Metadata about the source of the resource.
            processing_options: Options for processing the resource.
            security: Security settings for the resource.
            slug: A URL-friendly identifier for the resource.
            summary: A brief summary of the resource.
            texts: Text content associated with the resource.
            thumbnail: URL of the resource's thumbnail image.
            usermetadata: User-defined metadata for the resource.
        Returns:
            API response as a dictionary.
        """
        ...

