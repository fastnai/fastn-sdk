"""Fastn Square connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SquareConnector:
    """Square connector ().

    Provides 16 tools.
    """

    def adjust_inventory(
        self,
        adjustments: List[Any],
        idempotency_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adjusts inventory levels for specific items in the system using the inventory management connector.

        Args:
            adjustments:  (required)
            idempotency_key: Unique key to prevent duplicate requests.
        Returns:
            API response as a dictionary.
        """
        ...

    def batch_retrieve_inventory_count(
        self,
        catalog_object_ids: List[Any],
        location_ids: List[Any],
        updated_after: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Batch retrieves inventory counts for multiple items in the system using the inventory management connector.

        Args:
            catalog_object_ids: Array of Catalog Object IDs for the Square API request. (required)
            location_ids: Array of location IDs for the Square API request. (required)
            updated_after: Filter for objects updated after this timestamp.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_catalog_object(
        self,
        idempotency_key: Optional[str] = None,
        object: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new catalog object in the system using the catalog management connector.

        Args:
            idempotency_key: 
            object: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_location(
        self,
        location: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new location in the system using the locations management connector.

        Args:
            location: Location details for the Square API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_order(
        self,
        idempotency_key: Optional[str] = None,
        order: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new order in the system using the order management connector.

        Args:
            idempotency_key: Idempotency key to prevent duplicate requests.
            order: Order details for the Square endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_catalog_object(
        self,
        objectId: str,
    ) -> Dict[str, Any]:
        """Deletes a catalog object from the system via the catalog management connector.

        Args:
            objectId: ID of the object being accessed via the Square API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_catalog_object(
        self,
        objectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific catalog object from the system using the catalog management connector.

        Args:
            objectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_locations(
        self,
    ) -> Dict[str, Any]:
        """Obtains a list of locations from the system using the locations management connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_catalog_objects(
        self,
        catalog_version: Optional[str] = None,
        cursor: Optional[str] = None,
        types: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all catalog objects available in the system using the catalog management connector.

        Args:
            catalog_version: Version of the catalog to use for the request.
            cursor: Cursor for pagination of results.
            types: Types of data to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_inventory(
        self,
    ) -> Dict[str, Any]:
        """Lists inventory items in the system using the inventory management connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def retrieve_catalog_object(
        self,
        objectId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific catalog object from the system using the catalog management connector.

        Args:
            objectId: ID of the object being accessed via the Square Square API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def retrieve_inventory_count(
        self,
        location_ids: str,
    ) -> Dict[str, Any]:
        """Retrieves the current inventory count for a specific item in the system using the inventory management connector.

        Args:
            location_ids: IDs of the locations. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def retrieve_order__(
        self,
        orderId: str,
    ) -> Dict[str, Any]:
        """Retrieves specific order details from the system using the order management connector.

        Args:
            orderId: Order ID for the Square Square API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def search_orders(
        self,
        location_ids: List[Any],
        query: Dict[str, Any],
        limit: Optional[int] = None,
        return_entries: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Searches for orders in the system using the order management connector.

        Args:
            location_ids: Array of location IDs to filter results. (required)
            query: Parameters to filter and sort the results. (required)
            limit: Maximum number of results to return.
            return_entries: Whether to return the entries in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_order_(
        self,
        idempotency_key: Optional[str] = None,
        order: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing order in the system using the order management connector.

        Args:
            idempotency_key: Idempotency key for the request.
            order: Order details for the Square Square endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def upsert_catalog_object(
        self,
        object: Dict[str, Any],
        idempotency_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates or inserts a catalog object in the system using the catalog management connector.

        Args:
            object: Object data for the Square API request. (required)
            idempotency_key: Idempotency key for request.
        Returns:
            API response as a dictionary.
        """
        ...

