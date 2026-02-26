"""Fastn Extensiv connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ExtensivConnector:
    """Extensiv connector ().

    Provides 30 tools.
    """

    def batch_update_order_status(
        self,
    ) -> Dict[str, Any]:
        """Batch updates the statuses of multiple orders in the current system context.
        Returns:
            API response as a dictionary.
        """
        ...

    def cancel_order_in_cart(
        self,
    ) -> Dict[str, Any]:
        """Cancels an order in the cart in the current system context.
        Returns:
            API response as a dictionary.
        """
        ...

    def cancel_order_in_wms(
        self,
        custRef: str,
    ) -> Dict[str, Any]:
        """Cancels an order in the WMS in the current system context.

        Args:
            custRef: Customer reference ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def dismiss_alerts(
        self,
    ) -> Dict[str, Any]:
        """Dismisses alerts in the current system context.
        Returns:
            API response as a dictionary.
        """
        ...

    def edit_merchant(
        self,
        name: str,
        wms_params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Edits the details of a merchant in the current system context.

        Args:
            name: Name parameter for the Extensiv API. (required)
            wms_params: Warehouse Management System (WMS) parameters.
        Returns:
            API response as a dictionary.
        """
        ...

    def edit_warehouse(
        self,
        inventory_warehouse: str,
        default: Optional[bool] = None,
        wms_warehouse_id: Optional[str] = None,
        wms_warehouse_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Edits the details of a specific warehouse in the current system context.

        Args:
            inventory_warehouse: Name of the inventory warehouse. (required)
            default: Indicates a default setting.
            wms_warehouse_id: ID of the warehouse in the WMS system.
            wms_warehouse_name: Name of the warehouse in the WMS system.
        Returns:
            API response as a dictionary.
        """
        ...

    def edit_wms(
        self,
        wms_name: str,
        wms_params: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Edits WMS configuration details in the current system context.

        Args:
            wms_name: Name of the Warehouse Management System. (required)
            wms_params: Parameters specific to the Warehouse Management System. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_cart(
        self,
        orderSource: str,
    ) -> Dict[str, Any]:
        """Retrieves details about a specific cart in the current system context.

        Args:
            orderSource: Source of the order for the Extensiv Extensiv endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_info(
        self,
        sku: str,
    ) -> Dict[str, Any]:
        """Gets detailed product information in the current system context.

        Args:
            sku: Product SKU for the Extensiv API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_inventory(
        self,
        sku: str,
    ) -> Dict[str, Any]:
        """Retrieves inventory information for a specific product in the current system context.

        Args:
            sku: SKU identifier for the Extensiv API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def list_alerts(
        self,
    ) -> Dict[str, Any]:
        """Lists all alerts related to the current system context.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_available_cart(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieves details about a specific available cart in the current system context.

        Args:
            id: ID of the URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def list_available_carts(
        self,
    ) -> Dict[str, Any]:
        """Lists all available carts in the current system context.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_cart_inventory(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists inventory items specific to a cart in the current system context.

        Args:
            limit: Limit the number of results.
            page: Specify the page number.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_cart_ship_methods(
        self,
        custRef: str,
    ) -> Dict[str, Any]:
        """Lists all shipping methods available for the cart in the current system context.

        Args:
            custRef: Customer reference for the Extensiv Extensiv endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def list_inventory(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all inventory items in the current system context.

        Args:
            limit: Number of records to retrieve from the Extensiv API.
            page: Page number for pagination of results from the Extensiv API.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_orders_by_status(
        self,
        status: str,
    ) -> Dict[str, Any]:
        """Lists all orders by their current status in the current system context.

        Args:
            status: Status of the URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def list_setup_carts(
        self,
    ) -> Dict[str, Any]:
        """Lists all setup carts in the current system context.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_skipped_orders(
        self,
    ) -> Dict[str, Any]:
        """Lists orders that were skipped in the current system context.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_warehouses(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all warehouses in the current system context.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_wms_params(
        self,
    ) -> Dict[str, Any]:
        """Lists parameters related to the WMS in the current system context.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_wms_ship_methods(
        self,
    ) -> Dict[str, Any]:
        """Lists all shipping methods available in the WMS in the current system context.
        Returns:
            API response as a dictionary.
        """
        ...

    def new_cart(
        self,
        cart_id: str,
        user_key: str,
        description: Optional[str] = None,
        extra_params: Optional[Dict[str, Any]] = None,
        password: Optional[str] = None,
        schedules: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new cart in the current system context.

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

    def new_merchant(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new merchant in the current system context.

        Args:
            name: Name field for the Extensiv API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_cart(
        self,
        password: str,
        description: Optional[str] = None,
        extra_params: Optional[Dict[str, Any]] = None,
        schedules: Optional[Dict[str, Any]] = None,
        user_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the information of an existing cart in the current system context.

        Args:
            password: Password for the request body. (required)
            description: Description of the request.
            extra_params: Additional parameters for the request.
            schedules: Scheduling information.
            user_key: User key identifier.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_inventory(
        self,
    ) -> Dict[str, Any]:
        """Updates inventory details in the current system context.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_order_status_shipped(
        self,
        order_status: str,
        shipments: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the status of an order to 'Shipped' in the current system context.

        Args:
            order_status: Status of the order. (required)
            shipments: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_order_status_wms(
        self,
        order_status: str,
    ) -> Dict[str, Any]:
        """Updates the order status in the WMS (Warehouse Management System) in the current system context.

        Args:
            order_status: Status of the order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def view_order(
        self,
        custRef: str,
    ) -> Dict[str, Any]:
        """Views detailed information about a specific order in the current system context.

        Args:
            custRef: Customer reference for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def view_order_status(
        self,
        custRef: str,
    ) -> Dict[str, Any]:
        """Checks the status of a specific order in the current system context.

        Args:
            custRef: Customer reference for the URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

