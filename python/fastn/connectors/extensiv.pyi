"""Fastn Extensiv connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _ExtensivCreateCartExtraParams(TypedDict, total=False):
    item_field: str
    prime_ship_code: str
    refund_delay: str

class _ExtensivCreateCartSchedules(TypedDict, total=False):
    confirm: str
    inventory: str
    order: str

class _ExtensivUpdateCartExtraParams(TypedDict, total=False):
    item_field: str
    prime_ship_code: str
    refund_delay: str

class _ExtensivUpdateCartSchedules(TypedDict, total=False):
    confirm: str
    inventory: str
    order: str

class _ExtensivUpdateMerchantWmsParams(TypedDict, total=False):
    ownerCode: str

class _ExtensivUpdateWmsWmsParams(TypedDict, total=False):
    ownerCode: str

class ExtensivConnector:
    """Extensiv connector ().

    Provides 31 tools.
    """

    def extensiv_batch_update_order_status(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Batch updates the status of multiple orders simultaneously in the Extensiv platform. Use this when you need to update order statuses in bulk rather than one at a time. Do not use this to update a single orders status — use extensiv_update_order_status_wms instead. Batch status changes are applied immediately and affect all specified orders.

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_cancel_order_in_cart(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Cancels an order within the sales channel cart in the Extensiv platform. Use this to request cancellation of an order at the cart or sales channel level. Do not use this to cancel an order in the WMS — use extensiv_cancel_order_in_wms instead. Order cancellation is irreversible and will notify the relevant sales channel.

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_cancel_order_in_wms(
        self,
        custRef: str,
    ) -> Dict[str, Any]:
        """Cancels an order in the Warehouse Management System (WMS) identified by its customer reference number. Use this to halt fulfillment processing for a specific order within the WMS. Do not use this to cancel an order at the sales channel level — use extensiv_cancel_order_in_cart instead. Order cancellation in the WMS is irreversible and may affect downstream fulfillment workflows.

        Args:
            custRef: Customer reference ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_create_cart(
        self,
        cart_id: str,
        user_key: str,
        description: Optional[str] = None,
        extra_params: Optional[_ExtensivCreateCartExtraParams] = None,
        password: Optional[str] = None,
        schedules: Optional[_ExtensivCreateCartSchedules] = None,
    ) -> Dict[str, Any]:
        """Creates a new sales channel cart integration in the Extensiv platform. Use this when connecting a new sales channel or order source to the system. Do not use this to update an existing cart — use extensiv_update_cart instead. This action permanently creates a cart record.

        Args:
            cart_id: Identifier for the shopping cart. (required)
            user_key: Unique identifier for the user. (required)
            description: Description of the request.
            extra_params: Additional parameters for the request.
            password: Password associated with the request.
            schedules: Scheduling related information.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_create_merchant(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new merchant account in the Extensiv platform. Use this when onboarding a new merchant to the system. Do not use this to update an existing merchant — use extensiv_update_merchant instead. This action permanently creates a merchant record and cannot be undone without a separate delete operation.

        Args:
            name: Name field for the Extensiv API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_dismiss_alerts(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Dismisses one or more active alerts in the Extensiv platform for the merchant. Use this to clear notifications after they have been reviewed or resolved. Do not use this to view alerts — use extensiv_list_alerts instead. Dismissal is permanent and cannot be undone.

        Args:
            body: Array of integers representing the request body for the Extensiv Extensiv endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_get_available_cart(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieves details about a specific available (unconfigured) cart integration type identified by its ID from the Extensiv platform. Use this to inspect a single available cart type before setting it up. Do not use this to list all available cart types — use extensiv_list_available_carts instead. Do not use this for already configured carts — use extensiv_get_cart instead.

        Args:
            id: ID of the URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_get_cart(
        self,
        orderSource: str,
    ) -> Dict[str, Any]:
        """Retrieves configuration and details for a specific sales channel cart integration identified by its order source. Use this to inspect the settings of a single configured cart. Do not use this to list all carts — use extensiv_list_setup_carts or extensiv_list_available_carts instead.

        Args:
            orderSource: Source of the order for the Extensiv Extensiv endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_get_order(
        self,
        custRef: str,
    ) -> Dict[str, Any]:
        """Retrieves full details of a specific order identified by its customer reference number, including line items, shipping information, and fulfillment data. Use this to inspect a single order in depth. Do not use this to check only the order status — use extensiv_get_order_status instead. Do not use this to list multiple orders — use extensiv_list_orders_by_status instead.

        Args:
            custRef: Customer reference for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_get_order_status(
        self,
        custRef: str,
    ) -> Dict[str, Any]:
        """Retrieves the current processing status of a specific order identified by its customer reference number. Use this to check where an order stands in the fulfillment pipeline. Do not use this to retrieve full order details — use extensiv_get_order instead. Do not use this to list orders by status — use extensiv_list_orders_by_status instead.

        Args:
            custRef: Customer reference for the URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_get_product_info(
        self,
        sku: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed product information for a specific SKU from the Extensiv platform. Use this to look up product attributes such as description, dimensions, and configuration for a single product. Do not use this to retrieve inventory levels — use extensiv_get_product_inventory instead.

        Args:
            sku: Product SKU for the Extensiv API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_get_product_inventory(
        self,
        sku: str,
    ) -> Dict[str, Any]:
        """Retrieves current inventory levels and details for a specific product identified by its SKU. Use this to check stock quantities and inventory status for a single product. Do not use this to retrieve general product details — use extensiv_get_product_info instead. Do not use this to list all inventory — use extensiv_list_inventory instead.

        Args:
            sku: SKU identifier for the Extensiv API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_list_alerts(
        self,
    ) -> Dict[str, Any]:
        """Lists all active alerts for the merchant in the Extensiv platform. Use this to review pending warehouse management notifications and warnings. Do not use this to dismiss alerts — use extensiv_dismiss_alerts instead. Returns a collection of alert records.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_list_available_carts(
        self,
    ) -> Dict[str, Any]:
        """Lists all available sales channel cart integration types supported by the Extensiv platform. Use this to discover which cart or sales channel types can be connected. Do not use this to list already configured carts — use extensiv_list_setup_carts instead. Returns a collection of available cart type records.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_list_cart_inventory(
        self,
        orderSource: str,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all inventory items associated with a specific sales channel cart integration identified by its order source. Use this to review inventory data at the cart or sales channel level. Do not use this to list all merchant-level inventory — use extensiv_list_inventory instead. Returns a collection of cart inventory records.

        Args:
            orderSource: Specify the order source. (required)
            limit: Limit the number of results.
            page: Specify the page number.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_list_cart_ship_methods(
        self,
        custRef: str,
    ) -> Dict[str, Any]:
        """Lists all shipping methods available for a specific sales channel cart integration identified by its customer reference. Use this to retrieve cart-level shipping options for mapping or configuration. Do not use this to list WMS-level shipping methods — use extensiv_list_wms_ship_methods instead. Returns a collection of cart shipping method records.

        Args:
            custRef: Customer reference for the Extensiv Extensiv endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_list_inventory(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all inventory items for the merchant in the Extensiv platform. Use this to get a complete view of stock across all products. Do not use this for inventory scoped to a specific cart — use extensiv_list_cart_inventory instead. Do not use this for a single product — use extensiv_get_product_inventory instead. Returns a collection of inventory records.

        Args:
            limit: Number of records to retrieve from the Extensiv API.
            page: Page number for pagination of results from the Extensiv API.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_list_merchant_wms_ship_methods(
        self,
    ) -> Dict[str, Any]:
        """Lists all shipping methods available in the Warehouse Management System (WMS) within the merchant context. Use this to retrieve WMS shipping options scoped to a merchant. Do not use this to list cart-level shipping methods — use extensiv_list_cart_ship_methods instead. Returns a collection of shipping method records.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_list_orders_by_status(
        self,
        status: str,
    ) -> Dict[str, Any]:
        """Lists all orders matching a specific fulfillment status in the Extensiv platform. Use this to retrieve a filtered collection of orders by their current processing state (e.g., pending, shipped, cancelled). Do not use this to retrieve details of a single order — use extensiv_get_order instead. Returns a collection of order records matching the specified status.

        Args:
            status: Status of the URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_list_setup_carts(
        self,
    ) -> Dict[str, Any]:
        """Lists all sales channel cart integrations that have been configured and set up in the Extensiv platform. Use this to see which sales channels are actively connected. Do not use this to list all available cart types — use extensiv_list_available_carts instead. Do not use this to retrieve a specific carts details — use extensiv_get_cart instead. Returns a collection of configured cart records.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_list_skipped_orders(
        self,
    ) -> Dict[str, Any]:
        """Lists all orders that were skipped during processing for the merchant in the Extensiv platform. Use this to identify and review orders that failed to import or were intentionally bypassed. Do not use this to list all orders by status — use extensiv_list_orders_by_status instead. Returns a collection of skipped order records.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_list_warehouses(
        self,
    ) -> Dict[str, Any]:
        """Lists all warehouses associated with the merchant in the Extensiv platform. Use this to retrieve available warehouse locations and their identifiers. Do not use this to update a warehouse — use extensiv_update_warehouse instead. Returns a collection of warehouse records.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_list_wms_params(
        self,
    ) -> Dict[str, Any]:
        """Lists all configuration parameters associated with the Warehouse Management System (WMS). Use this to inspect available WMS settings and parameter values. Do not use this to modify WMS parameters — use extensiv_update_wms instead. Returns a collection of parameter key-value records.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_list_wms_ship_methods(
        self,
    ) -> Dict[str, Any]:
        """Lists all shipping methods configured in the Warehouse Management System (WMS). Use this to retrieve available WMS shipping options for order fulfillment configuration. Do not use this to list shipping methods for a specific sales channel cart — use extensiv_list_cart_ship_methods instead. Returns a collection of shipping method records.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_update_cart(
        self,
        orderSource: str,
        password: str,
        description: Optional[str] = None,
        extra_params: Optional[_ExtensivUpdateCartExtraParams] = None,
        schedules: Optional[_ExtensivUpdateCartSchedules] = None,
        user_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration or details of an existing sales channel cart integration identified by its order source. Use this to modify cart settings after the cart has been created. Do not use this to create a new cart — use extensiv_create_cart instead. Changes may affect order routing and fulfillment for the specified sales channel.

        Args:
            orderSource: Source of the order. (required)
            password: Password for the request body. (required)
            description: Description of the request.
            extra_params: Additional parameters for the request.
            schedules: Scheduling information.
            user_key: User key identifier.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_update_inventory(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Updates inventory details for one or more products in the Extensiv platform. Use this to adjust stock quantities or inventory attributes. Do not use this to retrieve inventory data — use extensiv_get_product_inventory or extensiv_list_inventory instead. Inventory changes take effect immediately and may impact order fulfillment.

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_update_merchant(
        self,
        name: str,
        wms_params: Optional[_ExtensivUpdateMerchantWmsParams] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration and details of an existing merchant in the Extensiv platform. Use this to modify merchant settings after the merchant has been created. Do not use this to create a new merchant — use extensiv_create_merchant instead. Changes take effect immediately.

        Args:
            name: Name parameter for the Extensiv API. (required)
            wms_params: Warehouse Management System (WMS) parameters.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_update_order_status_shipped(
        self,
        custRef: str,
        order_status: str,
        shipments: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Marks a specific order as Shipped in the Extensiv platform, identified by its customer reference number. Use this when fulfillment is complete and the order has been dispatched to the customer. Do not use this to apply other order status changes — use extensiv_update_order_status_wms instead. This status change is typically irreversible in downstream systems.

        Args:
            custRef: Customer reference ID. (required)
            order_status: Status of the order. (required)
            shipments: 
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_update_order_status_wms(
        self,
        custRef: str,
        order_status: str,
    ) -> Dict[str, Any]:
        """Updates the status of a specific order in the Warehouse Management System (WMS), identified by its customer reference number. Use this to reflect changes in order processing state within the WMS. Do not use this for bulk updates — use extensiv_batch_update_order_status instead. Do not use this specifically to mark an order as shipped — use extensiv_update_order_status_shipped instead. Status changes take effect immediately.

        Args:
            custRef: Reference to the customer. (required)
            order_status: Status of the order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_update_warehouse(
        self,
        inventory_warehouse: str,
        wasehousePk: str,
        default: Optional[bool] = None,
        wms_warehouse_id: Optional[str] = None,
        wms_warehouse_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration and details of a specific warehouse identified by its warehouse primary key. Use this to modify warehouse settings such as address, operational parameters, or name. Do not use this to list warehouses — use extensiv_list_warehouses instead. Changes take effect immediately and may affect order routing.

        Args:
            inventory_warehouse: Name of the inventory warehouse. (required)
            wasehousePk: Primary key of the warehouse. (required)
            default: Indicates a default setting.
            wms_warehouse_id: ID of the warehouse in the WMS system.
            wms_warehouse_name: Name of the warehouse in the WMS system.
        Returns:
            API response as a dictionary.
        """
        ...

    def extensiv_update_wms(
        self,
        wms_name: str,
        wms_params: _ExtensivUpdateWmsWmsParams,
    ) -> Dict[str, Any]:
        """Updates the configuration details of the Warehouse Management System (WMS). Use this to modify existing WMS settings such as connection parameters or operational configuration. Do not use this to create a new WMS configuration. Changes take effect immediately and may impact active warehouse operations.

        Args:
            wms_name: Name of the Warehouse Management System. (required)
            wms_params: Parameters specific to the Warehouse Management System. (required)
        Returns:
            API response as a dictionary.
        """
        ...

