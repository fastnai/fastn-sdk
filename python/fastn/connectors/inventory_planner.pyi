"""Fastn Inventory Planner connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _InventoryPlannerClosePurchaseOrderPurchaseOrder(TypedDict, total=False):
    status: str

class _InventoryPlannerCreateAssemblyOrderPurchaseOrder(TypedDict, total=False):
    expected_date: str
    items: List[Any]
    reference: str
    source_warehouse: str
    status: str
    type: str
    warehouse: str

class _InventoryPlannerCreateConnectionConnection(TypedDict, total=False):
    auth: Dict[str, Any]
    authorize_at: str
    authorized: str
    authorized_at: str
    checked_at: str
    config: Dict[str, Any]
    message: str
    platform: str
    ready_at: str

class _InventoryPlannerCreatePurchaseOrderPurchaseOrder(TypedDict, total=False):
    expected_date: str
    reference: str
    status: str
    variants_filter: Dict[str, Any]
    vendor: str
    warehouse: str

class _InventoryPlannerCreateTransferPurchaseOrder(TypedDict, total=False):
    connections: List[Any]
    expected_date: str
    source_warehouse: str
    status: str
    variants_filter: Dict[str, Any]
    warehouse: str

class _InventoryPlannerCreateWebhookWebhook(TypedDict, total=False):
    address: str
    fields: str
    filter: Dict[str, Any]
    topic: str

class _InventoryPlannerPushStockUpdateStockUpdate(TypedDict, total=False):
    items: List[Any]

class _InventoryPlannerSavePurchaseOrderToConnectionConnection(TypedDict, total=False):
    save_po: bool

class _InventoryPlannerUpdateOrderPurchaseOrder(TypedDict, total=False):
    billing_address: str
    currency: str
    discount_enabled: bool
    expected_date: str
    notes: str
    reference: str
    replenishment_type: str
    shipping_address: str
    source_type: str
    source_warehouse: str
    status: str
    type: str
    uom_ordering: bool
    uom_round: str
    useTitlesAsVendorName: bool
    warehouse: str

class _InventoryPlannerUpdateReceivedQuantitySingleItemItem(TypedDict, total=False):
    id: str
    received: int

class _InventoryPlannerUpdateWebhookWebhook(TypedDict, total=False):
    address: str
    fields: str
    filter: Dict[str, Any]
    topic: str

class InventoryPlannerConnector:
    """Inventory Planner connector ().

    Provides 28 tools.
    """

    def inventory_planner_close_purchase_order(
        self,
        purchase_order: _InventoryPlannerClosePurchaseOrderPurchaseOrder,
        purchase_order_id: str,
    ) -> Dict[str, Any]:
        """Marks a specific purchase order as closed in Inventory Planner, finalizing all associated transactions and indicating that the order is complete. Use this tool when all items on a purchase order have been received and no further changes are expected. Do not use this tool to update item quantities or order details — use inventory_planner_update_received_quantity_single_item or inventory_planner_update_order instead. Closing a purchase order is a significant state change; it may not be reversible and will prevent further modifications to the order.

        Args:
            purchase_order: Purchase order object containing status. (required)
            purchase_order_id: ID of the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_create_assembly_order(
        self,
        purchase_order: _InventoryPlannerCreateAssemblyOrderPurchaseOrder,
    ) -> Dict[str, Any]:
        """Creates a new assembly order in Inventory Planner for manufacturing or kitting processes, specifying the component items and quantities required to build or assemble a finished product. Use this tool when you need to initiate production or assembly of inventory items from their components. Do not use this tool to create a standard purchase order from a supplier — use inventory_planner_create_purchase_order instead. Do not use this tool to create a warehouse transfer — use inventory_planner_create_transfer instead. This action creates a new record in the system and cannot be undone without explicitly closing or deleting the resulting order.

        Args:
            purchase_order: Information about the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_create_connection(
        self,
        connection: Optional[_InventoryPlannerCreateConnectionConnection] = None,
    ) -> Dict[str, Any]:
        """Creates a new connection in Inventory Planner to integrate with an external inventory source or system, enabling data synchronization between Inventory Planner and a third-party platform. Use this tool when you need to establish a new integration link with an external system. Do not use this tool to link a purchase order to an existing connection — use inventory_planner_save_purchase_order_to_connection instead. This action creates a persistent integration record in the system.

        Args:
            connection: 
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_create_purchase_order(
        self,
        purchase_order: _InventoryPlannerCreatePurchaseOrderPurchaseOrder,
    ) -> Dict[str, Any]:
        """Creates a new purchase order in Inventory Planner for acquiring goods from a supplier, specifying the items, quantities, and supplier details. Use this tool when you need to place a new order with a vendor to replenish inventory. Do not use this tool to create a stock transfer between warehouses — use inventory_planner_create_transfer instead. Do not use this tool to create an assembly order — use inventory_planner_create_assembly_order instead. This action creates a new record in the system and cannot be undone without explicitly closing or deleting the resulting order.

        Args:
            purchase_order: Represents a purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_create_transfer(
        self,
        purchase_order: _InventoryPlannerCreateTransferPurchaseOrder,
    ) -> Dict[str, Any]:
        """Creates a new stock transfer order in Inventory Planner to move inventory between warehouses, specifying the items and quantities to be transferred. Use this tool when you need to initiate a transfer of goods between locations. Do not use this tool to create a standard purchase order from a supplier — use inventory_planner_create_purchase_order instead. Do not use this tool to create an assembly order — use inventory_planner_create_assembly_order instead. This action creates a new record in the system and cannot be undone without explicitly closing or deleting the resulting order.

        Args:
            purchase_order: The purchase order object. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_create_webhook(
        self,
        webhook: _InventoryPlannerCreateWebhookWebhook,
    ) -> Dict[str, Any]:
        """Creates a new webhook in Inventory Planner that sends real-time HTTP event notifications to a specified URL when configured events occur (e.g., purchase order updates, stock changes). Use this tool when you need to set up a new event-driven integration with an external system. Do not use this tool to modify an existing webhook — use inventory_planner_update_webhook instead. The webhook becomes active immediately upon creation and will begin dispatching event notifications.

        Args:
            webhook: The detailed configuration of the webhook to be created. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_delete_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific webhook from Inventory Planner using its unique identifier, immediately stopping all future event notifications to the webhooks configured URL. Use this tool when a webhook integration is no longer needed and should be fully removed. Do not use this tool if you only want to modify the webhook — use inventory_planner_update_webhook instead. This action is irreversible; the deleted webhook cannot be recovered and must be recreated using inventory_planner_create_webhook if needed again.

        Args:
            webhookId: The unique identifier of the webhook to be deleted. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_get_item_by_sku(
        self,
        sku: str,
    ) -> Dict[str, Any]:
        """Retrieves inventory item details from Inventory Planner by searching for a specific SKU (Stock Keeping Unit), returning information such as price, available quantity, and item description. Use this tool when you have a SKU and need to look up the corresponding inventory items details. Do not use this tool to retrieve a full list of all variants — use inventory_planner_list_variants instead. This is a read-only operation and has no side effects.

        Args:
            sku: Stock Keeping Unit identifier. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_get_purchase_order_by_id(
        self,
        purchase_order_id: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a specific purchase order in Inventory Planner using its unique identifier, including the list of line items, order status, supplier information, and totals. Use this tool when you know the purchase order ID and need its complete details. Do not use this tool to retrieve a list of all purchase orders — use inventory_planner_list_purchase_orders instead. This is a read-only operation and has no side effects.

        Args:
            purchase_order_id: ID of the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_get_purchase_order_item_by_id(
        self,
        item_id: str,
        purchase_order_id: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single line item within a specific purchase order in Inventory Planner using the items unique identifier, including pricing, ordered quantity, and received quantity. Use this tool when you need precise details about one specific item in a purchase order and you have its item ID. Do not use this tool to retrieve all items on a purchase order — use inventory_planner_list_purchase_order_items instead. This is a read-only operation and has no side effects.

        Args:
            item_id: The unique identifier for the item. (required)
            purchase_order_id: The unique identifier for the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_get_stock_update(
        self,
        forDst: str,
        purchase_order_id: str,
    ) -> Dict[str, Any]:
        """Retrieves the stock update record associated with a specific purchase order in Inventory Planner, providing details on inventory changes such as adjustments or post-delivery corrections. Use this tool when you need to review the stock update history or current stock adjustment data tied to a particular purchase order. Do not use this tool to submit or push new stock changes — use inventory_planner_push_stock_update instead. This is a read-only operation and has no side effects.

        Args:
            forDst: Destination for the Inventory Planner operation. (required)
            purchase_order_id: ID of the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_get_warehouse(
        self,
        warehouseId: str,
        field_groups: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific warehouse in Inventory Planner using its unique identifier, including location, capacity, and current stock levels. Use this tool when you know the warehouse ID and need its specific configuration or stock details. Do not use this tool to retrieve a list of all warehouses — use inventory_planner_list_warehouses instead. This is a read-only operation and has no side effects.

        Args:
            warehouseId: The identifier of the warehouse associated with the inventory data. (required)
            field_groups: Groups of fields to be included or used for filtering.
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_get_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Retrieves the configuration details of a specific webhook in Inventory Planner using its unique identifier, including its target URL, event subscriptions, and current status. Use this tool when you know the webhook ID and need to inspect its configuration. Do not use this tool to list all webhooks — use inventory_planner_list_webhooks instead. This is a read-only operation and has no side effects.

        Args:
            webhookId: Identifier of the webhook to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_list_purchase_order_connections(
        self,
        purchase_order_id: str,
    ) -> Dict[str, Any]:
        """Retrieves all connections linked to a specific purchase order in Inventory Planner, showing associated external systems, documents, or related orders. Use this tool when you need to review which connections are associated with a given purchase order. Do not use this tool to link a purchase order to a connection — use inventory_planner_save_purchase_order_to_connection instead. This is a read-only operation and has no side effects.

        Args:
            purchase_order_id: ID of the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_list_purchase_order_items(
        self,
        purchase_order_id: str,
    ) -> Dict[str, Any]:
        """Retrieves all line items associated with a specific purchase order in Inventory Planner, including each items status, quantity ordered, and quantity received. Use this tool when you need a full list of items on a particular purchase order. Do not use this tool to retrieve a single item by its ID — use inventory_planner_get_purchase_order_item_by_id instead. This is a read-only operation and has no side effects.

        Args:
            purchase_order_id: The ID of the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_list_purchase_orders(
        self,
        created_date: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        reference: Optional[str] = None,
        reference2: Optional[str] = None,
        source_warehouse: Optional[str] = None,
        status: Optional[str] = None,
        type: Optional[str] = None,
        warehouse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all purchase orders in Inventory Planner, providing an overview of each orders status, supplier, and associated details. Use this tool when you need to browse or enumerate all purchase orders in the system. Do not use this tool to retrieve the details of a single purchase order by ID — use inventory_planner_get_purchase_order_by_id instead. This is a read-only operation and has no side effects.

        Args:
            created_date: Filter records by creation date.
            limit: Number of records to return per page.
            page: Page number for pagination.
            reference: reference
            reference2: Extra Reference
            source_warehouse: Filter results by the identifier of the source warehouse.
            status: Order Status
            type: Filter records by inventory type.
            warehouse: Filter results by the destination warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_list_variants(
        self,
        created_at_time: Optional[str] = None,
        field_groups: Optional[str] = None,
        limit: Optional[str] = None,
        noTotalCount: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all product variants in Inventory Planner, representing different versions or configurations of inventory items (e.g., size, color, SKU). Use this tool when you need to browse all product variants in the inventory. Do not use this tool to look up a specific variant by SKU — use inventory_planner_get_item_by_sku instead. This is a read-only operation and has no side effects.

        Args:
            created_at_time: 
            field_groups: Specify the groups of fields to include in the response.
            limit: Maximum number of records to return.
            noTotalCount: Flag to specify whether to include total count in response.
            page: Page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_list_warehouses(
        self,
        name: str,
        display_name: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all warehouses configured in Inventory Planner, including details such as location and available storage facilities. Use this tool when you need an overview of all warehouses in the system or to identify a warehouse ID for subsequent operations. Do not use this tool to retrieve details of a single warehouse by ID — use inventory_planner_get_warehouse instead. This is a read-only operation and has no side effects.

        Args:
            name: The name or identifier of the IP resource to retrieve or filter by. (required)
            display_name: Human-readable display name for the IP resource.
            limit: Maximum number of items to return (pagination limit).
            page: Page number for paginated results.
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_list_webhooks(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all webhooks currently configured in Inventory Planner, including their target URLs, subscribed event types, and statuses. Use this tool when you need an overview of all active webhook integrations or to find a specific webhook ID for subsequent operations. Do not use this tool to retrieve details of a single webhook — use inventory_planner_get_webhook instead. This is a read-only operation and has no side effects.

        Args:
            limit: The maximum number of webhooks to retrieve.
            page: The page number of webhooks to retrieve for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_push_stock_update(
        self,
        forDst: bool,
        purchase_order_id: str,
        stock_update: _InventoryPlannerPushStockUpdateStockUpdate,
    ) -> Dict[str, Any]:
        """Manually submits a stock update for a specific purchase order in Inventory Planner, recording inventory changes such as adjustments or corrections to stock levels. Use this tool when you need to push a manual inventory change associated with a purchase order to the system. Do not use this tool to retrieve stock update history — use inventory_planner_get_stock_update instead. This action writes data to the inventory system and the effect persists until overridden by a subsequent update.

        Args:
            forDst: Indicates if the update is for Daylight Saving Time. (required)
            purchase_order_id: ID of the related purchase order. (required)
            stock_update: Information about the stock update. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_save_purchase_order_to_connection(
        self,
        connection_id: str,
        purchase_order_id: str,
        connection: Optional[_InventoryPlannerSavePurchaseOrderToConnectionConnection] = None,
    ) -> Dict[str, Any]:
        """Links a purchase order to a specific connection in Inventory Planner, enabling organized tracking and cross-referencing of related documents or external integrations. Use this tool when you need to associate an existing purchase order with a named connection (e.g., a linked external system or document group). Do not use this tool to create a new purchase order or connection — use the respective create tools for those actions. This action overwrites any existing link between the purchase order and the specified connection.

        Args:
            connection_id: The ID of the connection. (required)
            purchase_order_id: The ID of the purchase order. (required)
            connection: Settings related to the connection.
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_update_order(
        self,
        orderId: str,
        purchase_order: Optional[_InventoryPlannerUpdateOrderPurchaseOrder] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing purchase order in Inventory Planner, allowing modifications to line items, quantities, statuses, or other order fields. Use this tool when you need to amend an open purchase order with new or corrected information. Do not use this tool to close a purchase order — use inventory_planner_close_purchase_order instead. Do not use this tool to update received quantities after delivery — use inventory_planner_update_received_quantity_single_item or inventory_planner_update_received_quantities_multiple_items instead. This action modifies an existing record and changes persist immediately.

        Args:
            orderId: Identifier of the order associated with this request. (required)
            purchase_order: Details of the purchase order to be created or updated.
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_update_received_quantities_multiple_items(
        self,
        items: List[Any],
        purchase_order_id: str,
    ) -> Dict[str, Any]:
        """Updates the received quantities of multiple line items within a specific purchase order in Inventory Planner in a single request, ensuring accurate inventory records after a bulk delivery. Use this tool when multiple items from a purchase order have been received and you need to record their actual received quantities at once. Do not use this tool if only a single item needs updating — use inventory_planner_update_received_quantity_single_item instead. This action modifies inventory records and cannot be undone without subsequent corrective updates.

        Args:
            items:  (required)
            purchase_order_id: ID of the purchase order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_update_received_quantity_single_item(
        self,
        item: _InventoryPlannerUpdateReceivedQuantitySingleItemItem,
        item_id: str,
        purchase_order_id: str,
    ) -> Dict[str, Any]:
        """Updates the received quantity of a single line item within a specific purchase order in Inventory Planner, reflecting accurate inventory counts after a delivery is processed. Use this tool when a delivery has been received and you need to record the actual quantity received for one specific item in a purchase order. Do not use this tool to update multiple items at once — use inventory_planner_update_received_quantities_multiple_items instead. This action modifies inventory records and cannot be undone without a subsequent corrective update.

        Args:
            item: Information about the item. (required)
            item_id: Unique identifier for the item in the URL. (required)
            purchase_order_id: Purchase order ID associated with the item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_update_webhook(
        self,
        webhookId: str,
        webhook: Optional[_InventoryPlannerUpdateWebhookWebhook] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing webhook in Inventory Planner, allowing changes to the target URL, subscribed event types, or other webhook settings. Use this tool when you need to modify an already-configured webhook. Do not use this tool to create a new webhook — use inventory_planner_create_webhook instead. Do not use this tool to delete a webhook — use inventory_planner_delete_webhook instead. Changes take effect immediately and will alter which events trigger notifications to the configured URL.

        Args:
            webhookId: The unique identifier of the webhook to update. (required)
            webhook: Details of the webhook to be updated.
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_upload_variant_data(
        self,
        fileName: Optional[str] = None,
        variants: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Uploads or imports bulk variant data into Inventory Planner to create or update product variant records, enabling accurate tracking of different item versions in inventory. Use this tool when you need to onboard or refresh a large set of product variant records. Do not use this tool to update a single variant — use inventory_planner_update_order or the appropriate update tool instead. This action writes data to the system; uploads may overwrite existing variant records depending on matching logic.

        Args:
            fileName: 
            variants: 
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_upload_vendor_data(
        self,
        fileName: Optional[str] = None,
        vendors: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Uploads or imports bulk vendor (supplier) data into Inventory Planner to create or update supplier records, ensuring accurate and up-to-date supplier information for inventory and purchasing workflows. Use this tool when you need to onboard or refresh a large set of vendor records. Do not use this tool to update a single purchase order or connection — use the appropriate update tools instead. This action writes data to the system; uploads may overwrite existing vendor records depending on matching logic.

        Args:
            fileName: 
            vendors: 
        Returns:
            API response as a dictionary.
        """
        ...

    def inventory_planner_upload_warehouse_data(
        self,
        fileName: Optional[str] = None,
        warehouses: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Uploads or imports bulk warehouse data into Inventory Planner to create or update warehouse records, ensuring accurate storage and location information for inventory management. Use this tool when you need to onboard or refresh a large set of warehouse records. Do not use this tool to retrieve warehouse details — use inventory_planner_list_warehouses or inventory_planner_get_warehouse instead. This action writes data to the system; uploads may overwrite existing warehouse records depending on matching logic.

        Args:
            fileName: 
            warehouses: 
        Returns:
            API response as a dictionary.
        """
        ...

