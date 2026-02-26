"""Fastn Algolia connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AlgoliaConnector:
    """Algolia connector ().

    Provides 16 tools.
    """

    def browse_index(
        self,
        indexName: str,
    ) -> Dict[str, Any]:
        """Browses through the index in the specified data storage or database, retrieving a list of entries or objects present in it.

        Args:
            indexName: The name of the Algolia index to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clear_objects(
        self,
        indexName: str,
    ) -> Dict[str, Any]:
        """Clears all objects from the specified data storage or database, removing all entries completely.

        Args:
            indexName: Name of the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def copy_or_move_index(
        self,
        destination: str,
        operation: str,
    ) -> Dict[str, Any]:
        """Copies or moves an index within the specified data storage or database, allowing for data migration or duplication.

        Args:
            destination: The destination for the Algolia operation. (required)
            operation: The type of operation to perform on Algolia. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_object(
        self,
    ) -> Dict[str, Any]:
        """Creates a new object in the specified data storage or database, allowing you to store new information.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_index(
        self,
        indexName: str,
    ) -> Dict[str, Any]:
        """Deletes the entire index from the specified data storage or database, removing all associated data and configurations.

        Args:
            indexName: The name of the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_object(
        self,
        indexName: str,
        objectId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific object from the specified data storage or database, permanently removing it from the system.

        Args:
            indexName: The name of the Algolia index. (required)
            objectId: The ID of the object within the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_dictionary_entries(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all entries from the specified dictionary in the database, providing a complete list of available data.

        Args:
            query: The search query string.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_index_settings(
        self,
        indexName: str,
    ) -> Dict[str, Any]:
        """Retrieves the current settings of the specified index in the data storage or database, allowing you to examine configuration options.

        Args:
            indexName: Name of the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_indexes(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all indexes available within the specified data storage or database, providing an overview of data organization.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_object(
        self,
        indexName: str,
        objectId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific object from the specified data storage or database based on a unique identifier.

        Args:
            indexName: Name of the Algolia index. (required)
            objectId: ID of the object within the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_objects(
        self,
        indexName: str,
    ) -> Dict[str, Any]:
        """Retrieves multiple objects from the specified data storage or database based on a set of criteria or filters.

        Args:
            indexName: The name of the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def partially_update_objects(
        self,
    ) -> Dict[str, Any]:
        """Partially updates existing objects in the specified data storage or database, allowing certain attributes to be modified without changing the entire object.
        Returns:
            API response as a dictionary.
        """
        ...

    def search_dictionary_entries(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for entries in the specified dictionary within the database, returning results that match the search criteria.

        Args:
            query: Search query string for the Algolia API.
        Returns:
            API response as a dictionary.
        """
        ...

    def searchindex(
        self,
    ) -> Dict[str, Any]:
        """Performs a search operation within the specified index in the data storage or database, returning results that match the search criteria.
        Returns:
            API response as a dictionary.
        """
        ...

    def set_index_settings(
        self,
        customRanking: Optional[List[Any]] = None,
        hitsPerPage: Optional[int] = None,
        searchableAttributes: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Sets or updates the settings of the specified index in the data storage or database, allowing customization of its behavior.

        Args:
            customRanking: Custom ranking criteria for Algolia search results.
            hitsPerPage: Number of hits per page for Algolia search results.
            searchableAttributes: Attributes to be used for Algolia search.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_object(
        self,
    ) -> Dict[str, Any]:
        """Updates an existing object in the specified data storage or database, allowing you to modify its attributes or values.
        Returns:
            API response as a dictionary.
        """
        ...

