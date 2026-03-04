"""Fastn Square connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _SquareCreateCatalogObjectObject(TypedDict, total=False):
    id: str
    item_data: Dict[str, Any]
    type: str

class _SquareCreateLocationLocation(TypedDict, total=False):
    address: Dict[str, Any]
    description: str
    name: str

class _SquareCreateOrderOrder(TypedDict, total=False):
    fulfillments: List[Any]
    line_items: List[Any]
    location_id: str
    metadata: Dict[str, Any]
    taxes: List[Any]

class _SquareSearchOrdersQuery(TypedDict, total=False):
    filter: Dict[str, Any]
    sort: Dict[str, Any]

class _SquareUpdateOrderOrder(TypedDict, total=False):
    discounts: List[Any]
    fulfillments: List[Any]
    line_items: List[Any]
    location_id: str
    metadata: Dict[str, Any]
    taxes: List[Any]

class _SquareUpsertCatalogObjectObject(TypedDict, total=False):
    id: str
    item_data: Dict[str, Any]
    type: str

class SquareConnector:
    """Square connector ().

    Provides 16 tools.
    """

    def square_adjust_inventory(
        self,
        adjustments: List[Any],
        idempotency_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Applies a quantity adjustment to the inventory of one or more catalog items in Square, increasing or decreasing stock levels. Use this to record stock changes due to receiving shipments, spoilage, theft, or manual corrections. Do not use this to set an absolute inventory count — this tool applies relative adjustments only. This operation permanently modifies inventory records and the adjustment cannot be undone.

        Args:
            adjustments:  (required)
            idempotency_key: Unique key to prevent duplicate requests.
        Returns:
            API response as a dictionary.
        """
        ...

    def square_batch_list_inventory_counts(
        self,
        catalog_object_ids: List[Any],
        location_ids: List[Any],
        updated_after: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves inventory counts for multiple catalog items in a single batch request to Square. Use this when you need current stock counts for several items at once and want to avoid making individual requests per item. Do not use this to retrieve counts for a single item — use square_get_inventory_count instead. This is a read-only operation with no side effects.

        Args:
            catalog_object_ids: Array of Catalog Object IDs for the Square API request. (required)
            location_ids: Array of location IDs for the Square API request. (required)
            updated_after: Filter for objects updated after this timestamp.
        Returns:
            API response as a dictionary.
        """
        ...

    def square_create_catalog_object(
        self,
        idempotency_key: Optional[str] = None,
        object: Optional[_SquareCreateCatalogObjectObject] = None,
    ) -> Dict[str, Any]:
        """Creates a new catalog object in Square — such as an item, item variation, category, tax, or discount — without overwriting any existing entry. Use this when you are certain the object does not already exist and want a strict create-only operation. Do not use this to update an existing catalog object — use square_upsert_catalog_object instead. The newly created object will be immediately available in the catalog.

        Args:
            idempotency_key: 
            object: 
        Returns:
            API response as a dictionary.
        """
        ...

    def square_create_location(
        self,
        location: _SquareCreateLocationLocation,
    ) -> Dict[str, Any]:
        """Creates a new business location in Square, including details such as name, address, contact information, and business hours. Use this to register a new physical or virtual location where transactions will be processed. Do not use this to update an existing locations details. Each location created in Square may affect billing and account limits depending on your Square plan.

        Args:
            location: Location details for the Square API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def square_create_order(
        self,
        idempotency_key: Optional[str] = None,
        order: Optional[_SquareCreateOrderOrder] = None,
    ) -> Dict[str, Any]:
        """Creates a new order in Square with specified line items, taxes, discounts, and fulfillment details. Use this to initiate a customer transaction or purchase. Do not use this to modify an existing order — use square_update_order instead. Creating an order does not automatically charge a payment; a separate payment step is required to complete the transaction.

        Args:
            idempotency_key: Idempotency key to prevent duplicate requests.
            order: Order details for the Square endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def square_delete_catalog_object(
        self,
        objectId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific catalog object from Square identified by its object ID. Use this to remove items, variations, categories, taxes, or discounts that are no longer needed. Do not use this if you only want to hide an item from listings — consider deactivating it instead. This action is irreversible; deleted catalog objects cannot be recovered.

        Args:
            objectId: ID of the object being accessed via the Square API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def square_get_catalog_object(
        self,
        objectId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single Square catalog object — such as an item, item variation, category, tax, or discount — identified by its object ID. Use this when you need structured data about one specific catalog entry. Do not use this to browse all catalog objects — use square_list_catalog_objects instead. This is a read-only operation with no side effects.

        Args:
            objectId: ID of the object being accessed via the Square Square API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def square_get_catalog_object_by_id(
        self,
        objectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific catalog object from Square using its catalog object ID. Use this as an alternative lookup when you have a direct object ID and need full metadata for that catalog entry. Note: square_get_catalog_object covers the same endpoint — prefer consolidating to one tool if duplication exists in your connector. This is a read-only operation with no side effects.

        Args:
            objectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def square_get_inventory_count(
        self,
        catalogObjectId: str,
        location_ids: str,
    ) -> Dict[str, Any]:
        """Retrieves the current inventory count for a single catalog object identified by its catalog object ID in Square. Use this when you need the stock level for one specific item. Do not use this for multiple items at once — use square_batch_list_inventory_counts instead. This is a read-only operation with no side effects.

        Args:
            catalogObjectId: ID of the catalog object. (required)
            location_ids: IDs of the locations. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def square_get_order(
        self,
        orderId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single Square order identified by its order ID, including line items, pricing, fulfillment status, and metadata. Use this when you need to inspect or display the contents of a known order. Do not use this to search for orders — use square_search_orders instead. This is a read-only operation with no side effects.

        Args:
            orderId: Order ID for the Square Square API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def square_list_catalog_objects(
        self,
        catalog_version: Optional[str] = None,
        cursor: Optional[str] = None,
        types: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all catalog objects in Square, including items, item variations, categories, taxes, and discounts. Use this to browse or export the full product catalog. Do not use this when you need details for a specific object by ID — use square_get_catalog_object instead. This is a read-only operation with no side effects.

        Args:
            catalog_version: Version of the catalog to use for the request.
            cursor: Cursor for pagination of results.
            types: Types of data to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def square_list_inventory(
        self,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all inventory records tracked in Square. Use this to browse or audit all inventory entries across your catalog. Do not use this when you need counts for specific items by ID — use square_get_inventory_count or square_batch_list_inventory_counts instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def square_list_locations(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all business locations associated with the Square account, including each locations ID, name, address, status, and capabilities. Use this to discover available location IDs required by other Square tools such as square_create_order or square_search_orders. Do not use this to retrieve details for a single location by ID. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def square_search_orders(
        self,
        location_ids: List[Any],
        query: _SquareSearchOrdersQuery,
        limit: Optional[int] = None,
        return_entries: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Searches for Square orders matching specified filter criteria such as location, state, date range, or customer. Use this when you do not have a specific order ID but need to find orders based on attributes. Do not use this when you already have an order ID — use square_get_order instead. This is a read-only operation with no side effects.

        Args:
            location_ids: Array of location IDs to filter results. (required)
            query: Parameters to filter and sort the results. (required)
            limit: Maximum number of results to return.
            return_entries: Whether to return the entries in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def square_update_order(
        self,
        orderId: str,
        idempotency_key: Optional[str] = None,
        order: Optional[_SquareUpdateOrderOrder] = None,
    ) -> Dict[str, Any]:
        """Updates an existing Square order identified by its order ID, allowing modifications to line items, fulfillments, state, or metadata. Use this to apply changes to an order that has already been created. Do not use this to create a new order — use square_create_order instead. Changes to orders in terminal states (e.g. completed or cancelled) may be rejected by Square.

        Args:
            orderId: ID of the order. (required)
            idempotency_key: Idempotency key for the request.
            order: Order details for the Square Square endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def square_upsert_catalog_object(
        self,
        object: _SquareUpsertCatalogObjectObject,
        idempotency_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Inserts a new catalog object or updates an existing one in Square in a single operation. If an object ID is provided and matches an existing entry, that entry is updated; otherwise a new object is created. Use this when you want to create or overwrite a catalog entry without needing to check for its existence first. Do not use this if you only want to create (never overwrite) — use square_create_catalog_object instead. This operation modifies catalog data and changes may affect item listings visible to customers.

        Args:
            object: Object data for the Square API request. (required)
            idempotency_key: Idempotency key for request.
        Returns:
            API response as a dictionary.
        """
        ...

