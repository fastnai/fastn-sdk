"""Fastn Nuclia connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class NucliaConnector:
    """Nuclia connector ().

    Provides 6 tools.
    """

    def ask_knowledge(
        self,
        query: str,
        audit_metadata: Optional[Dict[str, Any]] = None,
        autofilter: Optional[bool] = None,
        chat_history: Optional[List[Any]] = None,
        citations: Optional[bool] = None,
        debug: Optional[bool] = None,
        extra_context: Optional[List[Any]] = None,
        features: Optional[List[Any]] = None,
        field_type_filter: Optional[List[Any]] = None,
        fields: Optional[List[Any]] = None,
        filter_expression: Optional[Dict[str, Any]] = None,
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
        """Asks a question to the knowledge base connected via the specified connector.

        Args:
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

    def delete_resource(
        self,
        kbId: str,
        resourceId: str,
    ) -> Dict[str, Any]:
        """Deletes a resource from the system using the specified connector.

        Args:
            kbId: The ID of the knowledge base. (required)
            resourceId: The ID of the specific resource within the knowledge base. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_resource(
        self,
        extracted: Optional[str] = None,
        field_type: Optional[str] = None,
        show: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific resource using the connector.

        Args:
            extracted: Specifies which fields to extract.
            field_type: Specifies the type of field.
            show: Specifies the fields to include in the search results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_resources(
        self,
        page: Optional[str] = None,
        size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of resources from the specified connector.

        Args:
            page: The page number for pagination.
            size: The number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def search_knowledge(
        self,
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
        """Searches for information in the knowledge base using the specified connector.

        Args:
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

    def update_resource(
        self,
        title: str,
        conversations: Optional[Dict[str, Any]] = None,
        extra: Optional[Dict[str, Any]] = None,
        fieldmetadata: Optional[List[Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        hidden: Optional[bool] = None,
        links: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        origin: Optional[Dict[str, Any]] = None,
        processing_options: Optional[Dict[str, Any]] = None,
        security: Optional[Dict[str, Any]] = None,
        slug: Optional[str] = None,
        summary: Optional[str] = None,
        texts: Optional[Dict[str, Any]] = None,
        thumbnail: Optional[str] = None,
        usermetadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the properties of an existing resource in the specified connector.

        Args:
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

