"""Fastn Shopify connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ShopifyConnector:
    """Shopify connector ().

    Provides 31 tools.
    """

    def bulk_create_products(
        self,
    ) -> Dict[str, Any]:
        """Bulk creates multiple products in the inventory management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_basic_product(
        self,
        product: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a basic product entry in the inventory management system.

        Args:
            product: Details of the Shopify product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_fulfillment(
        self,
        lineItemsByFulfillmentOrder: List[Any],
        notifyCustomer: Optional[bool] = None,
        trackingInfo: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new fulfillment entry in the inventory management system to process orders.

        Args:
            lineItemsByFulfillmentOrder:  (required)
            notifyCustomer: Whether to notify the customer about the shipment.
            trackingInfo: Tracking information for the shipment.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product(
        self,
        product: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new product entry in the inventory management system.

        Args:
            product: Represents a Shopify product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_staged_upload_url(
        self,
    ) -> Dict[str, Any]:
        """Creates a staged upload URL in the inventory management system for file uploads.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_variant(
        self,
        variant: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new variant for an existing product in the inventory management system.

        Args:
            variant: Details of the variant.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_webhook(
        self,
        url: str,
        entity: Optional[str] = None,
        operation: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the inventory management system to listen for specific events.

        Args:
            url: The URL endpoint for the Shopify API call. (required)
            entity: The type of Shopify entity being manipulated (e.g., product, order, customer).
            operation: The type of operation to be performed (e.g., create, update, delete).
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified product from the inventory management system.

        Args:
            productId: The ID of the Shopify product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified webhook from the inventory management system.

        Args:
            webhookId: The ID of the webhook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
    ) -> Dict[str, Any]:
        """Fetches an access token needed for authorization in the inventory management system.

        Args:
            client_id: Client ID for Shopify API authentication. (required)
            client_secret: Client secret for Shopify API authentication. (required)
            code: Authorization code for Shopify. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_bulk_inventory(
        self,
    ) -> Dict[str, Any]:
        """Fetches bulk inventory information from the inventory management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_fulfillment_order(
        self,
        orderId: str,
    ) -> Dict[str, Any]:
        """Retrieves details about a specific fulfillment order in the inventory management system.

        Args:
            orderId: The ID of the order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inventory_items(
        self,
        ids: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of inventory items from the inventory management system.

        Args:
            ids: IDs required for the Shopify API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inventory_levels(
        self,
        location_ids: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the inventory levels for various items in the inventory management system.

        Args:
            location_ids: Comma-separated list of location IDs.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_locations(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of locations from the inventory management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_orders(
        self,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of orders from the inventory management system.

        Args:
            name: A parameter name.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific product in the inventory management system.

        Args:
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_by_handle(
        self,
        handle: str,
    ) -> Dict[str, Any]:
        """Fetches a product by its handle from the inventory management system.

        Args:
            handle: Handle of the Shopify resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
        created_at_min: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of products from the inventory management system.

        Args:
            created_at_min: Minimum creation date for filtering results (ISO 8601 format).
            limit: test the flow Description
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products_count(
        self,
    ) -> Dict[str, Any]:
        """Fetches the count of products available in the inventory management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products_graph_ql(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of products using GraphQL from the inventory management system.

        Args:
            query: The query string for the Shopify API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_variant(
        self,
        variantId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific variant from the inventory management system.

        Args:
            variantId: The ID of the product variant. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhooks(
        self,
        address: Optional[str] = None,
        topic: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all registered webhooks in the inventory management system.

        Args:
            address: Address related to the request.
            topic: Topic of the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def move_fulfillment_order(
        self,
        fulfillmentOrderId: str,
        newLocationId: str,
        lineitems: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Moves a fulfillment order to a new location within the inventory management system.

        Args:
            fulfillmentOrderId: The ID of the fulfillment order. (required)
            newLocationId: The ID of the new location for the fulfillment. (required)
            lineitems: 
        Returns:
            API response as a dictionary.
        """
        ...

    def register_webhook(
        self,
        url: str,
        entity: Optional[str] = None,
        operation: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Registers an existing webhook in the inventory management system for event notifications.

        Args:
            url: Specific URL for the Shopify API endpoint. (required)
            entity: Shopify entity to interact with (e.g., products, orders, customers).
            operation: Type of operation to perform (e.g., create, update, delete).
        Returns:
            API response as a dictionary.
        """
        ...

    def set_inventory_level(
        self,
        available: Optional[int] = None,
        inventory_item_id: Optional[int] = None,
        location_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Sets the inventory level for a specific item in the inventory management system.

        Args:
            available: 
            inventory_item_id: 
            location_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_basic_product(
        self,
        product: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates an existing basic product in the inventory management system.

        Args:
            product: Details of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_inventory_item(
        self,
        inventory_item: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates a specific inventory item in the inventory management system.

        Args:
            inventory_item: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_order(
        self,
        order: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing order in the inventory management system.

        Args:
            order: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product(
        self,
        product: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing product in the inventory management system.

        Args:
            product: Details of the Shopify product.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_variants(
        self,
        variant: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates the variants of a product in the inventory management system.

        Args:
            variant: Details about the product variant. (required)
        Returns:
            API response as a dictionary.
        """
        ...

