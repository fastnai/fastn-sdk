"""Fastn Algolia connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AlgoliaConnector:
    """Algolia connector ().

    Provides 16 tools.
    """

    def algolia_browse_index(
        self,
        indexName: str,
    ) -> Dict[str, Any]:
        """Iterates through all records in a specified Algolia index, returning them in paginated batches without relevance ranking. Use this when you need to export or process all records in an index. Do not use this for relevance-ranked search queries; use algolia_search_index instead. This is a read-only operation with no side effects.

        Args:
            indexName: The name of the Algolia index to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_clear_objects(
        self,
        indexName: str,
    ) -> Dict[str, Any]:
        """Removes all records (objects) from a specified Algolia index while preserving the index itself along with its settings, synonyms, and rules. Use this when you need to empty an index without deleting it entirely. This operation is irreversible—all records will be permanently deleted. Do not use this if you want to delete the index entirely; use algolia_delete_index instead. Do not use this to remove a single record; use algolia_delete_object instead.

        Args:
            indexName: Name of the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_copy_or_move_index(
        self,
        destination: str,
        indexName: str,
        operation: str,
    ) -> Dict[str, Any]:
        """Copies or moves an existing Algolia index to a new destination index name. Use copy to duplicate an index (records, settings, synonyms, and rules) or move to rename it. A move operation replaces any existing destination index and is irreversible—the source index is deleted after a move. A copy will overwrite any existing destination index with the same name. Do not use this to create a blank new index; use algolia_create_object to add records to a new index instead.

        Args:
            destination: The destination for the Algolia operation. (required)
            indexName: The name of the Algolia index. (required)
            operation: The type of operation to perform on Algolia. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_create_object(
        self,
        body: Dict[str, Any],
        indexName: str,
    ) -> Dict[str, Any]:
        """Creates a new record (object) in a specified Algolia index. If the index does not yet exist, Algolia will create it automatically. Use this when you need to add a new record to an index. Do not use this to update an existing record; use algolia_update_object for a full replacement or algolia_partially_update_objects for a partial update. The new record becomes immediately available for search after indexing.

        Args:
            body: Request body for the Algolia API.  This may vary depending on the specific Algolia endpoint. (required)
            indexName: The name of the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_delete_index(
        self,
        indexName: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified Algolia index, including all its records, settings, synonyms, and rules. Use this only when the entire index and all its data are no longer needed. This operation is irreversible—deleted indexes and their data cannot be recovered. Do not use this to remove individual records; use algolia_delete_object instead. Do not use this to clear records while keeping the index; use algolia_clear_objects instead.

        Args:
            indexName: The name of the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_delete_object(
        self,
        indexName: str,
        objectId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a single record (object) from a specified Algolia index by its unique objectID. Use this when you need to remove a specific record. This operation is irreversible—the deleted record cannot be recovered. Do not use this to remove all records; use algolia_clear_objects instead. Do not use this to delete the entire index; use algolia_delete_index instead.

        Args:
            indexName: The name of the Algolia index. (required)
            objectId: The ID of the object within the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_get_index_settings(
        self,
        indexName: str,
    ) -> Dict[str, Any]:
        """Retrieves the current configuration settings of a specified Algolia index, including searchable attributes, ranking, faceting, and highlighting options. Use this to inspect an indexs configuration before making changes. Do not use this to retrieve records from the index; use algolia_browse_index or algolia_search_index instead. This is a read-only operation with no side effects.

        Args:
            indexName: Name of the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_get_object(
        self,
        indexName: str,
        objectId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single record (object) from a specified Algolia index by its unique objectID. Use this when you know the exact objectID and need the full record details. Do not use this to retrieve multiple records at once; use algolia_list_objects or algolia_search_index instead. This is a read-only operation with no side effects.

        Args:
            indexName: Name of the Algolia index. (required)
            objectId: ID of the object within the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_list_dictionary_entries(
        self,
        dictionaryName: str,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all entries in a specified Algolia dictionary (e.g., stopwords, plurals, or compounds). Use this when you need a complete view of every entry stored in a given dictionary. Do not use this for keyword-based filtering; use algolia_search_dictionary_entries instead. This is a read-only operation with no side effects.

        Args:
            dictionaryName: The name of the Algolia dictionary. (required)
            query: The search query string.
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_list_indexes(
        self,
    ) -> Dict[str, Any]:
        """Lists all Algolia indexes available in the application, including metadata such as record count, size, and last update time. Use this to get an overview of all indexes before performing operations on a specific one. Do not use this to retrieve records or settings from a specific index. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_list_objects(
        self,
        indexName: str,
    ) -> Dict[str, Any]:
        """Retrieves all records (objects) stored in a specified Algolia index. Use this when you need a full listing of index records without applying a search query. Do not use this to search for records using a query string; use algolia_search_index instead. Do not use this to retrieve a single record by ID; use algolia_get_object instead. This is a read-only operation with no side effects.

        Args:
            indexName: The name of the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_partially_update_objects(
        self,
        body: Dict[str, Any],
        indexName: str,
        objectId: str,
    ) -> Dict[str, Any]:
        """Partially updates one or more existing records (objects) in a specified Algolia index by modifying only the provided attributes, leaving all other attributes unchanged. Use this when you need to update specific fields without overwriting the entire record. Do not use this to replace a full record; use algolia_update_object for a full replacement. This operation modifies records in place.

        Args:
            body: Request body for the Algolia API.  This may vary depending on the specific Algolia endpoint. (required)
            indexName: The name of the Algolia index. (required)
            objectId: The ID of the object within the Algolia index. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_search_dictionary_entries(
        self,
        dictionaryName: str,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for entries in a specified Algolia dictionary (e.g., stopwords, plurals, or compounds) using a query string or filter criteria. Use this when you need to find specific dictionary entries by keyword rather than retrieving all entries. Do not use this to list all entries; use algolia_list_dictionary_entries instead. This is a read-only operation with no side effects.

        Args:
            dictionaryName: Name of the dictionary to query in the Algolia API. (required)
            query: Search query string for the Algolia API.
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_search_index(
        self,
        body: Dict[str, Any],
        indexName: str,
    ) -> Dict[str, Any]:
        """Performs a relevance-ranked search query against a specified Algolia index, returning records that match the search criteria along with ranking metadata. Use this when you need to retrieve records based on a user query or filter expression. Do not use this to retrieve all records without a query; use algolia_browse_index instead. This is a read-only operation with no side effects.

        Args:
            body: Body of the request for Algolia API.  May be empty depending on the specific Algolia endpoint. (required)
            indexName: The name of the Algolia index (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_set_index_settings(
        self,
        indexName: str,
        customRanking: Optional[List[Any]] = None,
        forwardToReplicas: Optional[str] = None,
        hitsPerPage: Optional[int] = None,
        searchableAttributes: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration settings of a specified Algolia index, such as searchable attributes, ranking criteria, faceting, and highlighting options. Use this when you need to change how an index behaves during search or indexing. Settings changes apply immediately and affect all subsequent queries on the index. Do not use this to update individual records; use algolia_update_object or algolia_partially_update_objects instead.

        Args:
            indexName: The name of the Algolia index. (required)
            customRanking: Custom ranking criteria for Algolia search results.
            forwardToReplicas: Whether to forward the request to replicas.
            hitsPerPage: Number of hits per page for Algolia search results.
            searchableAttributes: Attributes to be used for Algolia search.
        Returns:
            API response as a dictionary.
        """
        ...

    def algolia_update_object(
        self,
        indexName: str,
        objectId: str,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Fully replaces an existing record (object) in a specified Algolia index with a new set of attributes, identified by its unique objectID. Use this when you need to overwrite all attributes of a record. Do not use this for partial updates to specific fields; use algolia_partially_update_objects instead. This operation overwrites all existing attributes not included in the new payload.

        Args:
            indexName: The name of the Algolia index. (required)
            objectId: The ID of the object within the Algolia index. (required)
            body: Request body for the Algolia API.  This may vary depending on the specific endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

