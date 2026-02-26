"""Fastn Inventory Planner connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class InventoryPlannerConnector:
    """Inventory Planner connector ().

    Provides 22 tools.
    """

    def close_purchase_order(
        self,
        purchase_order: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Closes a purchase order in the system, indicating that the order is complete and finalizing all associated transactions.

        Args:
            purchase_order: Purchase order object containing status. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_assembly_order(
        self,
        purchase_order: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new assembly order for manufacturing or assembly processes, specifying the components and quantities needed.

        Args:
            purchase_order: Information about the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_purchase_order(
        self,
        purchase_order: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new purchase order in the system for acquiring goods or services from suppliers, specifying items and quantities required.

        Args:
            purchase_order: Represents a purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_transfer(
        self,
        purchase_order: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Initiates the transfer of stock between warehouses, specifying the items and quantities being moved.

        Args:
            purchase_order: The purchase order object. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_webhook(
        self,
        webhook: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new webhook in the application, allowing the system to send real-time updates to a specified URL based on certain events.

        Args:
            webhook: The detailed configuration of the webhook to be created. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing webhook from the application, stopping it from sending future notifications and updates.

        Args:
            webhookId: The unique identifier of the webhook to be deleted. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_orders(
        self,
        created_date: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        reference: Optional[str] = None,
        source_warehouse: Optional[str] = None,
        status: Optional[str] = None,
        type: Optional[str] = None,
        warehouse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a comprehensive list of all orders in the system, providing an overview of order statuses and details.

        Args:
            created_date: Filter records by creation date.
            limit: Number of records to return per page.
            page: Page number for pagination.
            reference: reference
            source_warehouse: Filter results by the identifier of the source warehouse.
            status: Order Status
            type: Filter records by inventory type.
            warehouse: Filter results by the destination warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_item_by_sku(
        self,
        sku: str,
    ) -> Dict[str, Any]:
        """Retrieves item details from the inventory by its unique SKU (Stock Keeping Unit) number, providing information like price, quantity, and description.

        Args:
            sku: Stock Keeping Unit identifier. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_purchase_order_by_id(
        self,
        purchase_order_id: str,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific purchase order using its unique identifier, including item list and order status.

        Args:
            purchase_order_id: ID of the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_purchase_order_connections(
        self,
        purchase_order_id: str,
    ) -> Dict[str, Any]:
        """Retrieves connections related to a specific purchase order, showing associated documents or related orders within the system.

        Args:
            purchase_order_id: ID of the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_purchase_order_item_by_id(
        self,
        item_id: str,
        purchase_order_id: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific item within a purchase order using its unique identifier, including pricing and quantities.

        Args:
            item_id: The unique identifier for the item. (required)
            purchase_order_id: The unique identifier for the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_purchase_order_items(
        self,
        purchase_order_id: str,
    ) -> Dict[str, Any]:
        """Retrieves all items associated with a specific purchase order, providing detailed information on each item's status and quantity.

        Args:
            purchase_order_id: The ID of the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stock_updates(
        self,
        forDst: str,
    ) -> Dict[str, Any]:
        """Fetches the latest stock updates across the inventory, providing insights into current stock levels and changes.

        Args:
            forDst: Destination for the Inventory Planner operation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_warehouse(
        self,
        field_groups: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of the specified warehouse, including its location, capacity, and current stock levels of items.

        Args:
            field_groups: Groups of fields to be included or used for filtering.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific webhook set up in the application, providing information such as its configuration and status.

        Args:
            webhookId: Identifier of the webhook to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhooks(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all webhooks currently configured in the application, along with their details for review and management.

        Args:
            limit: The maximum number of webhooks to retrieve.
            page: The page number of webhooks to retrieve for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def push_stock_updates(
        self,
        forDst: bool,
        stock_update: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Pushes stock updates to the system, allowing the manual entry of inventory changes for enhanced accuracy.

        Args:
            forDst: Indicates if the update is for Daylight Saving Time. (required)
            stock_update: Information about the stock update. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def save_po_into_connection(
        self,
        connection: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Saves a purchase order into a connection, allowing for organized tracking and referencing of related documents.

        Args:
            connection: Settings related to the connection.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_order(
        self,
        purchase_order: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing order in the system, allowing modifications to items, quantities, or statuses as needed.

        Args:
            purchase_order: Details of the purchase order to be created or updated.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_received_quantities__multiple_items_(
        self,
        items: List[Any],
    ) -> Dict[str, Any]:
        """Updates the received quantities of multiple items in a purchase order, ensuring accurate inventory records post-receipt.

        Args:
            items:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_received_quantities__single_item_(
        self,
        item: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates the received quantity of a single item in a purchase order, reflecting accurate inventory count after delivery.

        Args:
            item: Information about the item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_webhook(
        self,
        webhook: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing webhook in the application, allowing adjustments to the URL, event types, or other settings.

        Args:
            webhook: Details of the webhook to be updated.
        Returns:
            API response as a dictionary.
        """
        ...

