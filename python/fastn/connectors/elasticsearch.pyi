"""Fastn Elasticsearch connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ElasticsearchConnector:
    """Elasticsearch connector ().

    Provides 8 tools.
    """

    def bulk_index(
        self,
        create: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Submit multiple documents for indexing in the connector, facilitating batch processing for improved efficiency.

        Args:
            create: Parameters for creating a new document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cat_indices(
        self,
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
        """List all indices available in the connector, offering a comprehensive overview of the data structure.

        Args:
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

    def create_document(
        self,
    ) -> Dict[str, Any]:
        """Add a new document to the specified connector, ensuring it adheres to the defined structure of the index.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_index(
        self,
        mappings: Optional[Dict[str, Any]] = None,
        settings: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Create a new index within the specified connector, enabling the organization and storage of related documents.

        Args:
            mappings: Mappings for the Elasticsearch index.
            settings: Settings for the Elasticsearch index.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_index(
        self,
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
        """Retrieve details about a specific index in the connector, providing information such as mapping and settings.

        Args:
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

    def search(
        self,
        allow_no_indices: Optional[str] = None,
        allow_partial_search_results: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Search for documents in the specified connector context, allowing for filtering and retrieval of relevant data.

        Args:
            allow_no_indices: 
            allow_partial_search_results: 
        Returns:
            API response as a dictionary.
        """
        ...

    def search_index(
        self,
        pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Perform a search operation within a specified index in the connector, returning documents that match the search criteria.

        Args:
            pretty: Format the Elasticsearch response to be more human-readable.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_document(
        self,
        doc: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Update an existing document in the specified connector, ensuring that the most current information is reflected in the index.

        Args:
            doc: The document to be indexed in Elasticsearch.
        Returns:
            API response as a dictionary.
        """
        ...

