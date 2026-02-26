"""Fastn Bonsai Elasticsearch connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BonsaiElasticsearchConnector:
    """Bonsai Elasticsearch connector ().

    Provides 5 tools.
    """

    def add_index_data(
        self,
    ) -> Dict[str, Any]:
        """Adds data to an existing index in the specified connector context, facilitating data storage and future retrieval.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_indices(
        self,
        index: str,
    ) -> Dict[str, Any]:
        """Creates new indices in the specified connector context for data organization and retrieval.

        Args:
            index: Name of the Elasticsearch index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_indices(
        self,
        index: str,
    ) -> Dict[str, Any]:
        """Deletes specified indices in the connector context to remove unwanted data organization structures.

        Args:
            index: Name of the Elasticsearch index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_index(
        self,
        index: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of an existing index in the specified connector context.

        Args:
            index: Index name in Bonsai Elasticsearch. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def search_indices_(
        self,
        query: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Searches through existing indices in the specified connector context to find relevant data based on specified criteria.

        Args:
            query: Elasticsearch query parameters.
        Returns:
            API response as a dictionary.
        """
        ...

