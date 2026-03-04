"""Fastn Shopify connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _ShopifyCreateBasicProductProduct(TypedDict, total=False):
    body_html: str
    handle: str
    images: List[Any]
    status: str
    title: str
    variants: List[Any]

class _ShopifyCreateFulfillmentTrackinginfo(TypedDict, total=False):
    company: str
    number: str
    url: str

class _ShopifyCreateProductProduct(TypedDict, total=False):
    admin_graphql_api_id: str
    body_html: str
    created_at: str
    handle: str
    images: List[Any]
    product_type: str
    published_at: str
    published_scope: str
    status: str
    tags: str
    template_suffix: Any
    title: str
    updated_at: str
    variants: List[Any]
    vendor: str

class _ShopifyCreateVariantVariant(TypedDict, total=False):
    barcode: str
    compare_at_price: str
    created_at: str
    fulfillment_service: str
    grams: int
    id: int
    image_id: Any
    inventory_item_id: int
    inventory_management: str
    inventory_policy: str
    old_inventory_quantity: int
    option1: str
    position: int
    price: str
    product_id: int
    requires_shipping: bool
    sku: str
    tax_code: str
    taxable: bool
    title: str
    updated_at: str
    weight: int
    weight_unit: str

class _ShopifyUpdateBasicProductProduct(TypedDict, total=False):
    body_html: str
    handle: str
    images: List[Any]
    status: str
    title: str
    variants: List[Any]

class _ShopifyUpdateInventoryItemInventoryItem(TypedDict, total=False):
    sku: str

class _ShopifyUpdateOrderOrder(TypedDict, total=False):
    admin_graphql_api_id: str
    app_id: int
    billing_address: str
    browser_ip: str
    buyer_accepts_marketing: bool
    cancel_reason: str
    cancelled_at: str
    cart_token: str
    checkout_id: str
    checkout_token: str
    client_details: str
    closed_at: str
    company: str
    confirmation_number: str
    confirmed: bool
    contact_email: str
    created_at: str
    currency: str
    current_subtotal_price: str
    current_subtotal_price_set: Dict[str, Any]
    current_total_additional_fees_set: str
    current_total_discounts: str
    current_total_discounts_set: Dict[str, Any]
    current_total_duties_set: str
    current_total_price: str
    current_total_price_set: Dict[str, Any]
    current_total_tax: str
    current_total_tax_set: Dict[str, Any]
    customer: str
    customer_locale: str
    device_id: str
    discount_applications: List[Any]
    discount_codes: List[Any]
    email: str
    estimated_taxes: bool
    financial_status: str
    fulfillment_status: str
    fulfillments: List[Any]
    id: int
    landing_site: str
    landing_site_ref: str
    line_items: List[Any]
    location_id: str
    merchant_of_record_app_id: str
    name: str
    note: str
    note_attributes: List[Any]
    number: int
    order_number: int
    order_status_url: str
    original_total_additional_fees_set: str
    original_total_duties_set: str
    payment_gateway_names: List[Any]
    payment_terms: str
    phone: str
    po_number: str
    presentment_currency: str
    processed_at: str
    reference: str
    referring_site: str
    refunds: List[Any]
    shipping_lines: List[Any]
    source_identifier: str
    source_name: str
    source_url: str
    subtotal_price: str
    subtotal_price_set: Dict[str, Any]
    tags: str
    tax_exempt: bool
    tax_lines: List[Any]
    taxes_included: bool
    test: bool
    token: str
    total_discounts: str
    total_discounts_set: Dict[str, Any]
    total_line_items_price: str
    total_line_items_price_set: Dict[str, Any]
    total_outstanding: str
    total_price: str
    total_price_set: Dict[str, Any]
    total_shipping_price_set: Dict[str, Any]
    total_tax: str
    total_tax_set: Dict[str, Any]
    total_tip_received: str
    total_weight: int
    updated_at: str
    user_id: str

class _ShopifyUpdateProductProduct(TypedDict, total=False):
    admin_graphql_api_id: str
    body_html: str
    created_at: str
    handle: str
    id: int
    images: List[Any]
    options: List[Any]
    product_type: str
    published_at: str
    published_scope: str
    status: str
    tags: str
    template_suffix: Any
    title: str
    updated_at: str
    variants: List[Any]
    vendor: str

class _ShopifyUpdateVariantVariant(TypedDict, total=False):
    admin_graphql_api_id: str
    barcode: Any
    compare_at_price: Any
    created_at: str
    fulfillment_service: str
    grams: int
    image_id: int
    inventory_item_id: int
    inventory_management: Any
    inventory_policy: str
    old_inventory_quantity: int
    option1: str
    option2: Any
    option3: Any
    position: int
    presentment_prices: List[Any]
    price: str
    requires_shipping: bool
    sku: str
    taxable: bool
    title: str
    updated_at: str
    weight: float
    weight_unit: str

class ShopifyConnector:
    """Shopify connector ().

    Provides 31 tools.
    """

    def shopify_bulk_create_products(
        self,
        fileUrl: str,
    ) -> Dict[str, Any]:
        """Creates multiple Shopify products in a single batch operation using the GraphQL API. Use this when you need to add many products to the store at once more efficiently than creating them one at a time. Do not use this to create a single product — use shopify_create_product instead. Bulk operations may run asynchronously; check operation status separately.

        Args:
            fileUrl:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_create_basic_product(
        self,
        product: _ShopifyCreateBasicProductProduct,
    ) -> Dict[str, Any]:
        """Creates a new product in the Shopify store with a minimal set of fields (such as title and vendor) using the REST API. Use this for simple product creation where only basic attributes are needed. For creating a product with full details including variants, images, and tags, use shopify_create_product instead.

        Args:
            product: Details of the Shopify product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_create_fulfillment(
        self,
        lineItemsByFulfillmentOrder: List[Any],
        notifyCustomer: Optional[bool] = None,
        trackingInfo: Optional[_ShopifyCreateFulfillmentTrackinginfo] = None,
    ) -> Dict[str, Any]:
        """Creates a fulfillment record for one or more line items in a Shopify order via the GraphQL API, marking them as shipped or processed. Use this when you are ready to fulfill items in an order and want to record tracking information. Do not use this to move a fulfillment to a different location — use shopify_move_fulfillment_order instead.

        Args:
            lineItemsByFulfillmentOrder:  (required)
            notifyCustomer: Whether to notify the customer about the shipment.
            trackingInfo: Tracking information for the shipment.
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_create_product(
        self,
        product: _ShopifyCreateProductProduct,
    ) -> Dict[str, Any]:
        """Creates a new product in the Shopify store, including its title, description, variants, images, tags, and status. Use this when adding a single new product to the catalog. Do not use this to update an existing product — use shopify_update_product instead. For creating many products at once, use shopify_bulk_create_products.

        Args:
            product: Represents a Shopify product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_create_staged_upload_url(
        self,
        filename: str,
        httpMethod: str,
        mimeType: str,
        resource: str,
    ) -> Dict[str, Any]:
        """Generates a temporary staged upload URL via the Shopify GraphQL API that allows you to upload a file (such as a product image or video) to Shopifys servers before attaching it to a resource. Use this as the first step before associating uploaded media with a product or other Shopify object. The returned URL is time-limited and single-use.

        Args:
            filename: Name of the file being uploaded or processed. (required)
            httpMethod: HTTP method used for the request (e.g., GET, POST, PUT, DELETE). (required)
            mimeType: MIME type of the file (e.g., application/json, image/jpeg). (required)
            resource: The Shopify API resource being accessed (e.g., products, orders). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_create_variant(
        self,
        productId: str,
        variant: Optional[_ShopifyCreateVariantVariant] = None,
    ) -> Dict[str, Any]:
        """Creates a new variant (e.g. a specific size, color, or material option) for an existing Shopify product identified by its product ID. Use this when a product needs an additional purchasable option added to it. Do not use this to update an existing variant — use shopify_update_variants instead.

        Args:
            productId: ID of the product the variant belongs to. (required)
            variant: Details of the variant.
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_create_webhook(
        self,
        url: str,
        entity: Optional[str] = None,
        operation: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook subscription in the Shopify store that sends HTTP POST notifications to a specified callback URL whenever a given event topic occurs (e.g. orders/paid, inventory_levels/update). Use this to initiate event-driven workflows. Note: this tool and shopify_register_webhook share the same endpoint — confirm with your implementation which payload format each expects before choosing one.

        Args:
            url: The URL endpoint for the Shopify API call. (required)
            entity: The type of Shopify entity being manipulated (e.g., product, order, customer).
            operation: The type of operation to be performed (e.g., create, update, delete).
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific product from the Shopify store by its product ID. This action is irreversible — the product record, along with all its variants and images, will be removed and cannot be recovered. Use this only when you intend to permanently remove a product. Do not use this to temporarily hide a product — use shopify_update_product to set status to draft instead.

        Args:
            productId: The ID of the Shopify product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_delete_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a registered webhook from the Shopify store by its webhook ID, stopping all future event notifications to that endpoint. This action is irreversible. Use this when a webhook subscription is no longer needed. Do not use this to temporarily pause notifications — there is no pause feature; you must delete and re-create the webhook.

        Args:
            webhookId: The ID of the webhook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_get_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        storeName: str,
    ) -> Dict[str, Any]:
        """Exchanges an OAuth authorization code for a permanent Shopify API access token for a given store. Use this during the OAuth installation flow to complete authentication and obtain credentials for subsequent API calls. Do not use this for routine API calls — the access token should be stored securely and reused. Exposing or logging this token is a security risk.

        Args:
            client_id: Client ID for Shopify API authentication. (required)
            client_secret: Client secret for Shopify API authentication. (required)
            code: Authorization code for Shopify. (required)
            storeName: Name of the Shopify store. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single Shopify product by its product ID, including title, description, variants, images, tags, and status. Use this when you need full details for one specific product. Do not use this to list multiple products — use shopify_list_products instead.

        Args:
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_get_product_by_handle(
        self,
        handle: str,
    ) -> Dict[str, Any]:
        """Retrieves a single Shopify product by its URL handle (the human-readable slug used in the storefront URL, e.g. blue-sneakers). Use this when you know the product handle but not the product ID. Do not use this to search by title or other attributes — use shopify_list_products instead.

        Args:
            handle: Handle of the Shopify resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_get_products_count(
        self,
    ) -> Dict[str, Any]:
        """Returns the total count of products in the Shopify store, optionally filtered by status, vendor, or product type. Use this to determine catalog size for pagination planning or reporting without fetching full product records. Do not use this to retrieve product details — use shopify_list_products for that.
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_get_variant(
        self,
        variantId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific product variant in the Shopify store by its variant ID, including price, SKU, inventory quantity, weight, and option values. Use this when you need full details for one variant. Do not use this to list all variants of a product — query the parent product via shopify_get_product instead.

        Args:
            variantId: The ID of the product variant. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_list_bulk_inventory(
        self,
    ) -> Dict[str, Any]:
        """Retrieves bulk inventory data across multiple items or locations from the Shopify store using the GraphQL API. Use this for large-scale inventory audits or synchronization tasks where querying items individually would be inefficient. Do not use this to retrieve inventory for a single item — use shopify_list_inventory_items instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_list_fulfillment_orders(
        self,
        orderId: str,
    ) -> Dict[str, Any]:
        """Retrieves all fulfillment orders associated with a specific Shopify order by its order ID. Fulfillment orders represent groups of line items that will be fulfilled together from a particular location. Use this to inspect the fulfillment breakdown of an order before processing. Do not confuse this with retrieving order details — use shopify_list_orders for that.

        Args:
            orderId: The ID of the order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_list_inventory_items(
        self,
        ids: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of inventory items from the Shopify store, optionally filtered by IDs. Each inventory item corresponds to a product variant and contains cost and tracking information. Use this to look up inventory item IDs needed for setting or adjusting stock levels. Do not use this to get stock quantities — use shopify_list_inventory_levels for that.

        Args:
            ids: IDs required for the Shopify API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_list_inventory_levels(
        self,
        location_ids: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the available stock quantities for inventory items across one or more Shopify locations. Use this to check current stock levels before making inventory adjustments or fulfillment decisions. Do not use this to update stock quantities — use shopify_set_inventory_level instead.

        Args:
            location_ids: Comma-separated list of location IDs.
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_list_locations(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all active fulfillment locations (warehouses, stores, or third-party logistics providers) configured in the Shopify store. Use this to obtain location IDs required when setting inventory levels or moving fulfillment orders. Do not use this to retrieve inventory at a location — use shopify_list_inventory_levels instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_list_orders(
        self,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of orders from the Shopify store, with optional filters for status, date range, customer, and fulfillment state. Use this to browse or process multiple orders. Do not use this to retrieve a single specific order by ID — use a dedicated get order tool if available.

        Args:
            name: A parameter name.
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_list_products(
        self,
        created_at_min: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of products from the Shopify store via the REST API, with optional filters for title, vendor, product type, status, and creation date. Use this to browse or export the product catalog. Do not use this to retrieve a single product — use shopify_get_product instead. For advanced field selection, use shopify_list_products_graphql.

        Args:
            created_at_min: Minimum creation date for filtering results (ISO 8601 format).
            limit: test the flow Description
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_list_products_graphql(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of Shopify products using the GraphQL API, supporting advanced filtering, cursor-based pagination, and field selection not available in the REST API. Use this when you need granular control over the fields returned or when working with large product catalogs. Do not use this for simple single-product lookups — use shopify_get_product instead.

        Args:
            query: The query string for the Shopify API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_list_webhooks(
        self,
        address: Optional[str] = None,
        topic: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all webhooks currently registered in the Shopify store, including their IDs, topics, and callback URLs. Use this to audit existing webhook subscriptions or to find a webhook ID before updating or deleting it. Do not use this to create a webhook — use shopify_create_webhook instead.

        Args:
            address: Address related to the request.
            topic: Topic of the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_move_fulfillment_order(
        self,
        fulfillmentOrderId: str,
        newLocationId: str,
        lineitems: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Moves an existing fulfillment order to a different fulfillment location via the Shopify GraphQL API. Use this when the originally assigned fulfillment location cannot fulfill the order and it needs to be reassigned. Do not use this to create a new fulfillment — use shopify_create_fulfillment instead.

        Args:
            fulfillmentOrderId: The ID of the fulfillment order. (required)
            newLocationId: The ID of the new location for the fulfillment. (required)
            lineitems: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_register_webhook(
        self,
        url: str,
        entity: Optional[str] = None,
        operation: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Registers a webhook subscription in the Shopify store to receive event notifications at a specified callback URL for a given topic (e.g. orders/create, products/update). Use this to set up event-driven integrations. Note: this tool and shopify_create_webhook share the same endpoint — confirm with your implementation which payload format each expects before choosing one.

        Args:
            url: Specific URL for the Shopify API endpoint. (required)
            entity: Shopify entity to interact with (e.g., products, orders, customers).
            operation: Type of operation to perform (e.g., create, update, delete).
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_set_inventory_level(
        self,
        available: Optional[int] = None,
        inventory_item_id: Optional[int] = None,
        location_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Sets the exact available inventory quantity for a specific inventory item at a specific location in the Shopify store. Use this to override the current stock count with a precise value. Do not use this to adjust inventory by a relative amount (increment/decrement) — use the inventory adjust endpoint instead. This action immediately overwrites the existing quantity.

        Args:
            available: 
            inventory_item_id: 
            location_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_update_basic_product(
        self,
        product: _ShopifyUpdateBasicProductProduct,
        productId: str,
    ) -> Dict[str, Any]:
        """Updates a limited set of basic fields (such as title, vendor, or product type) for an existing Shopify product identified by its product ID, using the REST API. Use this for lightweight product edits that do not require updating variants or media. For comprehensive product updates including variants and images, use shopify_update_product instead.

        Args:
            product: Details of the product. (required)
            productId: ID of the product to be updated. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_update_inventory_item(
        self,
        inventoryItemId: Optional[str] = None,
        inventory_item: Optional[_ShopifyUpdateInventoryItemInventoryItem] = None,
    ) -> Dict[str, Any]:
        """Updates the properties of a specific inventory item in the Shopify store by its inventory item ID. Editable fields include cost, country of origin, harmonized system code, and tracking settings. Use this to manage inventory item metadata. Do not use this to change stock quantities — use shopify_set_inventory_level instead.

        Args:
            inventoryItemId: 
            inventory_item: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_update_order(
        self,
        orderId: str,
        order: Optional[_ShopifyUpdateOrderOrder] = None,
    ) -> Dict[str, Any]:
        """Updates editable fields of an existing Shopify order identified by its order ID, such as note, tags, email, and shipping address. Use this to correct or annotate order information after it has been placed. Do not use this to fulfill an order — use shopify_create_fulfillment instead. Changes are applied immediately.

        Args:
            orderId:  (required)
            order: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_update_product(
        self,
        productId: str,
        product: Optional[_ShopifyUpdateProductProduct] = None,
    ) -> Dict[str, Any]:
        """Updates the fields of an existing Shopify product identified by its product ID. Editable fields include title, description, status, tags, images, and vendor. Use this when you need to modify a products core attributes. Do not use this to update product variants — use shopify_update_variants instead. This action overwrites only the fields provided; omitted fields are left unchanged.

        Args:
            productId: ID of the product. (required)
            product: Details of the Shopify product.
        Returns:
            API response as a dictionary.
        """
        ...

    def shopify_update_variant(
        self,
        variant: _ShopifyUpdateVariantVariant,
        variantId: str,
    ) -> Dict[str, Any]:
        """Updates the fields of a specific product variant in the Shopify store by its variant ID, including price, SKU, weight, option values, and inventory policy. Use this to modify an individual variant. Do not use this to create a new variant — use shopify_create_variant instead. Changes are applied immediately and affect the live storefront.

        Args:
            variant: Details about the product variant. (required)
            variantId: The ID of the variant. (required)
        Returns:
            API response as a dictionary.
        """
        ...

