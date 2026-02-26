"""Fastn Qdrant connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class QdrantConnector:
    """Qdrant connector ().

    Provides 11 tools.
    """

    def create_collection(
        self,
        timeout: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new collection in the specified database or data storage system.

        Args:
            timeout: Timeout for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_collection(
        self,
        timeout: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes a specific collection from the specified database or data storage system.

        Args:
            timeout: Timeout for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_points(
        self,
        ordering: Optional[str] = None,
        wait: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes specific data points from the specified database or data storage system.

        Args:
            ordering: 
            wait: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_vectors(
        self,
        ordering: Optional[str] = None,
        wait: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes vector data associated with specific points in the specified database or data storage system.

        Args:
            ordering: Specifies the ordering of results.
            wait: Specifies whether to wait for asynchronous operations.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_collection(
        self,
        collectionName: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific collection from the specified database or data storage system.

        Args:
            collectionName: The name of the collection to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_collections(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all collections from the specified database or data storage system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_point(
        self,
        consistency: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific data point from the specified database or data storage system.

        Args:
            consistency: Specifies the consistency level for the operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_points(
        self,
        consistency: Optional[str] = None,
        timeout: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all data points from the specified database or data storage system.

        Args:
            consistency: Consistency level for the request.
            timeout: Timeout for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_collection(
        self,
        timeout: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing collection in the specified database or data storage system.

        Args:
            timeout: Request timeout.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_vectors(
        self,
        ordering: Optional[str] = None,
        wait: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the vector data associated with points in the specified database or data storage system.

        Args:
            ordering: Specifies the ordering of results.
            wait: Specifies whether to wait for asynchronous operations to complete.
        Returns:
            API response as a dictionary.
        """
        ...

    def upsert_points(
        self,
        ordering: Optional[str] = None,
        wait: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Inserts or updates data points in the specified database or data storage system, ensuring the points are either added or modified as needed.

        Args:
            ordering: Specify the ordering of results.
            wait: Wait for operation completion.
        Returns:
            API response as a dictionary.
        """
        ...

