"""Fastn Walmart connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _WalmartBulkItemInventoryUpdateInventoryheader(TypedDict, total=False):
    version: str

class _WalmartCreateInboundShipmentInboundservices(TypedDict, total=False):
    inventoryTransferService: str

class _WalmartCreateInboundShipmentReturnaddress(TypedDict, total=False):
    addressLine1: str
    addressLine2: str
    city: str
    countryCode: str
    postalCode: str
    stateCode: str

class _WalmartTestSubscriptionAuthdetails(TypedDict, total=False):
    authHeaderName: str
    authMethod: str
    authUrl: str
    clientId: str
    clientSecret: str
    password: str
    userName: str

class _WalmartTestSubscriptionHeaders(TypedDict, total=False):
    content_type: str

class _WalmartUpdateInventoryQuantity(TypedDict, total=False):
    amount: int
    unit: str

class _WalmartUpdateInventoryMarketplaceQuantity(TypedDict, total=False):
    amount: int
    unit: str

class _WalmartUpdatePricesMpitemfeedheader(TypedDict, total=False):
    businessUnit: str
    locale: str
    version: str

class _WalmartUpdateSubscriptionAuthdetails(TypedDict, total=False):
    authHeaderName: str
    authMethod: str
    authUrl: str
    clientId: str
    clientSecret: str
    password: str
    userName: str

class _WalmartUpdateSubscriptionHeaders(TypedDict, total=False):
    content_type: str

class _WalmartUpdateSubscriptionMarketplaceAuthdetails(TypedDict, total=False):
    authHeaderName: str
    authMethod: str
    password: str
    userName: str

class WalmartConnector:
    """Walmart connector ().

    Provides 35 tools.
    """

    def walmart_bulk_item_inventory_update(
        self,
        Inventory: Optional[List[Any]] = None,
        InventoryHeader: Optional[_WalmartBulkItemInventoryUpdateInventoryheader] = None,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
        shipNode: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Submits a bulk feed to update inventory levels for multiple Walmart Marketplace items simultaneously via the feeds API. Use this when inventory changes affect many items at once. Do not use this for a single item update — use walmart_update_inventory_marketplace instead. Triggers asynchronous feed processing; inventory updates are not applied instantly.

        Args:
            Inventory: 
            InventoryHeader: 
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
            shipNode: 
            sku: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_cancel_inbound_shipment(
        self,
        inboundOrderId: str,
    ) -> Dict[str, Any]:
        """Cancels an existing Walmart inbound shipment identified by its inbound order ID, halting all further processing of that shipment. Use this only when a shipment needs to be stopped before it is received. This action is irreversible — a cancelled shipment cannot be reactivated.

        Args:
            inboundOrderId: The identifier of the inbound order to be accessed or manipulated on My data sources. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_catalog_search_items(
        self,
        body: str,
        limit: str,
        next_cursor: str,
        WM_CONSUMER_CHANNEL_TYPE: Optional[str] = None,
        WM_QOS_CORRELATION_ID: Optional[str] = None,
        WM_SEC_ACCESS_TOKEN: Optional[str] = None,
        WM_SVC_NAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches the Walmart Marketplace catalog for items matching specified criteria using a POST request, supporting pagination via limit and nextCursor parameters. Use this for broad catalog discovery or when searching by multiple attributes simultaneously. Do not use this to look up a single item by a known ID — use walmart_get_item or walmart_search_item instead. Does not modify any data.

        Args:
            body: You can search by Query, Filter and Sort or by all of them collectively. (required)
            limit:  (required)
            next_cursor: Please do not apply nextCursor when you do the search for the first time. (required)
            WM_CONSUMER_CHANNEL_TYPE: 
            WM_QOS_CORRELATION_ID: 
            WM_SEC_ACCESS_TOKEN: 
            WM_SVC_NAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_create_inbound_shipment(
        self,
        inboundOrderId: str,
        orderItems: List[Any],
        inboundServices: Optional[_WalmartCreateInboundShipmentInboundservices] = None,
        returnAddress: Optional[_WalmartCreateInboundShipmentReturnaddress] = None,
    ) -> Dict[str, Any]:
        """Creates a new inbound shipment record in the Walmart fulfillment system to track incoming products sent to a Walmart fulfillment center. Use this when initiating a new inbound logistics workflow. Do not use this to update an existing shipment — use walmart_update_shipment_quantities instead. Creates a persistent shipment record.

        Args:
            inboundOrderId: Unique identifier for the inbound order. (required)
            orderItems:  (required)
            inboundServices: Inbound service options available for the order.
            returnAddress: Return address details for the inbound order.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_create_repricer_strategy(
        self,
        ContentType: Optional[str] = None,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
        enableRepricerForPromotion: Optional[bool] = None,
        enabled: Optional[bool] = None,
        repricerStrategy: Optional[str] = None,
        strategies: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new repricer strategy in the Walmart Marketplace pricing management system to automatically adjust item prices based on defined rules and competitive signals. Use this when setting up automated pricing for the first time or adding a new strategy. Do not use this to modify an existing strategy — use walmart_update_repricer_strategy instead. Creates a persistent repricer strategy resource.

        Args:
            ContentType: 
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
            enableRepricerForPromotion: 
            enabled: 
            repricerStrategy: 
            strategies: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_create_subscription(
        self,
        events: List[Any],
        WM_QOSCORRELATION_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Walmart webhook subscription to receive event notifications at a specified callback URL for one or more event types. Use this when you need to start receiving real-time Walmart Marketplace events. Do not use this to modify an existing subscription — use walmart_update_subscription instead. Creates a persistent subscription resource.

        Args:
            events: List of events to subscribe to. (required)
            WM_QOSCORRELATION_ID: Correlation ID used for tracking the request through Walmart services.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_create_subscription_marketplace(
        self,
        ContentType: Optional[str] = None,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
        events: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new Walmart webhook subscription via the marketplace API endpoint to receive event notifications at a specified callback URL for one or more event types. Use this when you need to start receiving real-time Walmart Marketplace events via the marketplace.walmartapis.com endpoint. Do not use this to modify an existing subscription — use walmart_update_subscription_marketplace instead. Creates a persistent subscription resource.

        Args:
            ContentType: 
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
            events: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_delete_repricer_strategy(
        self,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a repricer strategy identified by its strategy collection ID from the Walmart Marketplace pricing management system, removing all associated automated price adjustment rules. Use this only when a repricer strategy is no longer needed. This action is irreversible — deleted strategies cannot be recovered.

        Args:
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_delete_subscription(
        self,
        subscriptionId: str,
        WM_QOSCORRELATION_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing Walmart webhook subscription identified by its subscription ID, stopping all future event deliveries to its endpoint. Use this only when a webhook subscription is no longer needed. This action is irreversible — the subscription cannot be recovered after deletion.

        Args:
            subscriptionId: Unique identifier of the subscription to be deleted. (required)
            WM_QOSCORRELATION_ID: Unique identifier for tracking the quality of service of the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_delete_subscription_marketplace(
        self,
        ContentType: Optional[str] = None,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
        subscriptionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing Walmart webhook subscription via the marketplace API endpoint, identified by its subscription ID, stopping all future event deliveries. Use this only when a webhook subscription on the marketplace.walmartapis.com endpoint is no longer needed. This action is irreversible — the subscription cannot be recovered after deletion.

        Args:
            ContentType: 
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
            subscriptionId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_get_access_token(
        self,
        WM_SVCNAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains a short-lived OAuth access token for authenticating subsequent Walmart Marketplace API requests. Use this before making API calls that require authorization. Do not use this to retrieve business data — it is an authentication utility only. The returned token should be passed as a bearer token in subsequent requests.

        Args:
            WM_SVCNAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_get_inventory(
        self,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
        shipNode: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the current inventory levels and stock details for tracked items on the Walmart Marketplace. Use this to check available stock quantities for one or more items. Do not use this to update inventory — use walmart_update_inventory_marketplace or walmart_bulk_item_inventory_update instead. Does not modify any data.

        Args:
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
            shipNode: 
            sku: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_get_item(
        self,
        item_id: str,
        item_id_type: str,
        WM_CONSUMER_CHANNEL_TYPE: Optional[str] = None,
        WM_QOS_CORRELATION_ID: Optional[str] = None,
        WM_SEC_ACCESS_TOKEN: Optional[str] = None,
        WM_SVC_NAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single Walmart Marketplace item by its item ID and product ID type. Use this when you need attributes, status, or metadata for one specific item. Do not use this to search for items by keyword or criteria — use walmart_search_item instead. Does not modify any data.

        Args:
            item_id:  (required)
            item_id_type:  (required)
            WM_CONSUMER_CHANNEL_TYPE: 
            WM_QOS_CORRELATION_ID: 
            WM_SEC_ACCESS_TOKEN: 
            WM_SVC_NAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_get_item_count_by_groups(
        self,
        WM_CONSUMER_CHANNEL_TYPE: Optional[str] = None,
        WM_QOS_CORRELATION_ID: Optional[str] = None,
        WM_SEC_ACCESS_TOKEN: Optional[str] = None,
        WM_SVC_NAME: Optional[str] = None,
        variant_group_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the count of Walmart Marketplace items grouped under a specific variant group, identified by variant group ID. Use this to understand the size of a variant group before performing bulk operations. Do not use this to filter items by status — use walmart_get_item_count_by_status instead. Does not modify any data.

        Args:
            WM_CONSUMER_CHANNEL_TYPE: 
            WM_QOS_CORRELATION_ID: 
            WM_SEC_ACCESS_TOKEN: 
            WM_SVC_NAME: 
            variant_group_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_get_item_count_by_status(
        self,
        group_status: str,
        WM_CONSUMER_CHANNEL_TYPE: Optional[str] = None,
        WM_QOS_CORRELATION_ID: Optional[str] = None,
        WM_SEC_ACCESS_TOKEN: Optional[str] = None,
        WM_SVC_NAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the count of Walmart Marketplace items filtered by a specific status (e.g., PUBLISHED, UNPUBLISHED, IN_PROGRESS). Use this to audit item counts by lifecycle status. Do not use this to count items by variant group — use walmart_get_item_count_by_groups instead. Does not modify any data.

        Args:
            group_status:  (required)
            WM_CONSUMER_CHANNEL_TYPE: 
            WM_QOS_CORRELATION_ID: 
            WM_SEC_ACCESS_TOKEN: 
            WM_SVC_NAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_get_taxonomy(
        self,
        WM_CONSUMER_CHANNEL_TYPE: Optional[str] = None,
        WM_QOS_CORRELATION_ID: Optional[str] = None,
        WM_SEC_ACCESS_TOKEN: Optional[str] = None,
        WM_SVC_NAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full Walmart Marketplace item category taxonomy structure. Use this to discover valid category paths and attributes required when listing or classifying items. Do not use this to retrieve item data — use walmart_get_item or walmart_search_item instead. Does not modify any data.

        Args:
            WM_CONSUMER_CHANNEL_TYPE: 
            WM_QOS_CORRELATION_ID: 
            WM_SEC_ACCESS_TOKEN: 
            WM_SVC_NAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_list_all_subscriptions(
        self,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all active Walmart webhook subscriptions via the marketplace API endpoint. Use this to audit or enumerate all webhook configurations on the marketplace.walmartapis.com endpoint. Do not use this if you need subscriptions from the base URL endpoint — use walmart_list_subscriptions instead. Does not modify any data.

        Args:
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_list_event_types(
        self,
        WM_QOSCORRELATION_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all available Walmart webhook event types that can be subscribed to. Use this to discover valid event type values before creating or updating a webhook subscription. Does not modify any data.

        Args:
            WM_QOSCORRELATION_ID: Correlation ID used for tracing the quality of service of the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_list_inbound_shipment_items(
        self,
        shipmentId: str,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of items associated with an existing Walmart inbound shipment. Use this to review item-level details such as quantities and SKUs within an inbound shipment. Do not use this to retrieve shipment-level summaries — use walmart_list_shipments instead. Does not modify any data.

        Args:
            shipmentId: Identifier of the shipment to retrieve. (required)
            limit: Maximum number of items to return.
            offset: Starting position for results.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_list_incentive_items(
        self,
        ContentType: Optional[str] = None,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of Walmart Marketplace items that are currently eligible for repricer incentives. Use this to identify items that qualify for incentive-based pricing adjustments before configuring or applying repricer strategies. Does not modify any data.

        Args:
            ContentType: 
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_list_items(
        self,
        WM_QOS_CORRELATION_ID: Optional[str] = None,
        availability: Optional[str] = None,
        condition: Optional[str] = None,
        gtin: Optional[str] = None,
        includeCustomerFavoritesStatus: Optional[str] = None,
        lifecycleStatus: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        publishedStatus: Optional[str] = None,
        showDuplicateItemInfo: Optional[str] = None,
        sku: Optional[str] = None,
        variantGroupId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a comprehensive list of all items in the Walmart Marketplace inventory catalog for the authenticated account. Use this for bulk review, auditing, or syncing all items. Do not use this to retrieve a single item — use walmart_get_item instead. Does not modify any data.

        Args:
            WM_QOS_CORRELATION_ID: Correlation identifier for tracing requests through the system.
            availability: Filter by product availability status.
            condition: Filter by item condition (e.g., new, refurbished).
            gtin: Global Trade Item Number to filter by a specific product.
            includeCustomerFavoritesStatus: Whether to include information about customer favorites status in results.
            lifecycleStatus: Lifecycle status of the item (e.g., Active, Inactive).
            limit: Maximum number of results to return.
            offset: Offset for paginated results.
            publishedStatus: Filter by publication status of the item.
            showDuplicateItemInfo: Flag to include information about duplicate items in results.
            sku: Stock Keeping Unit to filter by a specific item.
            variantGroupId: Identifier for a group of item variants to filter results.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_list_orders(
        self,
        createdEndDate: Optional[str] = None,
        createdStartDate: Optional[str] = None,
        customerOrderId: Optional[str] = None,
        fromExpectedShipDate: Optional[str] = None,
        lastModifiedEndDate: Optional[str] = None,
        lastModifiedStartDate: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        orderType: Optional[str] = None,
        productInfo: Optional[str] = None,
        purchaseOrderId: Optional[str] = None,
        replacementInfo: Optional[str] = None,
        shipNodeType: Optional[str] = None,
        shippingProgramType: Optional[str] = None,
        sku: Optional[str] = None,
        status: Optional[str] = None,
        toExpectedShipDate: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of customer orders from the Walmart Marketplace order management system, including transaction details for each order. Use this to review, process, or audit orders placed by customers. Do not use this to retrieve shipment details — use walmart_list_shipments instead. Does not modify any data.

        Args:
            createdEndDate: End date filter for order creation time.
            createdStartDate: Start date filter for order creation (ISO 8601).
            customerOrderId: Customer order identifier to filter by.
            fromExpectedShipDate: Lower bound for the expected ship date window.
            lastModifiedEndDate: End date filter for last modification time.
            lastModifiedStartDate: Start date filter for last modification time.
            limit: Maximum number of records to return.
            offset: Pagination offset indicating the starting point of results.
            orderType: Filter by the type of orders.
            productInfo: Product information or SKU to filter by.
            purchaseOrderId: Purchase order identifier.
            replacementInfo: Replacement order information if applicable.
            shipNodeType: Type of shipping node used for fulfillment.
            shippingProgramType: Type of Walmart shipping program to apply.
            sku: Product Stock Keeping Unit to filter by.
            status: Order status filter.
            toExpectedShipDate: Upper bound for the expected ship date window.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_list_shipment_items(
        self,
        shipmentId: str,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of items contained within a specific Walmart fulfillment inbound shipment. Use this to inspect the contents of a shipment during the inbound fulfillment process. Do not use this to retrieve shipment-level details — use walmart_list_shipments instead. Does not modify any data.

        Args:
            shipmentId: Identifier of the shipment to retrieve or operate on. (required)
            limit: Maximum number of items to return for pagination.
            offset: Pagination offset indicating the starting position of the returned items.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_list_shipments(
        self,
        fromCreateDate: Optional[str] = None,
        inboundOrderId: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        shipmentId: Optional[str] = None,
        status: Optional[str] = None,
        toCreateDate: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of inbound shipments and their summary details from the Walmart fulfillment system. Use this to get an overview of all inbound shipments or to find a specific shipment to act on. Do not use this to retrieve item-level details within a shipment — use walmart_list_inbound_shipment_items instead. Does not modify any data.

        Args:
            fromCreateDate: Lower bound creation date to filter inbound orders.
            inboundOrderId: Identifier for a specific inbound order.
            limit: Maximum number of results to return.
            offset: Pagination offset to start returning results from.
            shipmentId: Identifier for a specific shipment.
            status: Filter by the current status of the inbound order.
            toCreateDate: Upper bound creation date to filter inbound orders.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_list_subscriptions(
        self,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        eventType: Optional[str] = None,
        resourceName: Optional[str] = None,
        status: Optional[str] = None,
        subscriptionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all webhook subscriptions associated with the authenticated Walmart Marketplace account. Use this to audit, review, or enumerate existing webhook configurations. Do not use this to retrieve a single subscription by ID. Does not modify any data.

        Args:
            WM_QOSCORRELATION_ID: Unique identifier for quality of service correlation.
            eventType: Type of event to filter the subscriptions.
            resourceName: Name of the resource for which to get webhook subscriptions.
            status: Status filter to retrieve subscriptions by their status.
            subscriptionId: Unique identifier of the subscription to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_retire_item(
        self,
        SKU: Optional[str] = None,
        WM_CONSUMER_CHANNEL_TYPE: Optional[str] = None,
        WM_QOS_CORRELATION_ID: Optional[str] = None,
        WM_SEC_ACCESS_TOKEN: Optional[str] = None,
        WM_SVC_NAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently retires a Walmart Marketplace item identified by its SKU, marking it as no longer available for sale and removing it from active listings. Use this when an item should no longer appear on Walmart Marketplace. This action is irreversible — a retired item cannot be reinstated through this endpoint.

        Args:
            SKU: 
            WM_CONSUMER_CHANNEL_TYPE: 
            WM_QOS_CORRELATION_ID: 
            WM_SEC_ACCESS_TOKEN: 
            WM_SVC_NAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_search_item(
        self,
        WM_CONSUMER_CHANNEL_TYPE: Optional[str] = None,
        WM_QOS_CORRELATION_ID: Optional[str] = None,
        WM_SEC_ACCESS_TOKEN: Optional[str] = None,
        WM_SVC_NAME: Optional[str] = None,
        seacrch_type: Optional[str] = None,
        search_type_value: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for Walmart Marketplace items using a specified search type and value (e.g., SKU, GTIN, UPC). Use this when you need to look up one or more items by a known identifier or attribute. Do not use this for free-text catalog searches — use walmart_catalog_search_items for that. Does not modify any data.

        Args:
            WM_CONSUMER_CHANNEL_TYPE: 
            WM_QOS_CORRELATION_ID: 
            WM_SEC_ACCESS_TOKEN: 
            WM_SVC_NAME: 
            seacrch_type: query for a keyword search, upc for Universal Product Code search or gtin to get the Global Trade Item Number.
            search_type_value: to search for a keyword, enter text with the query search type. or specify the number with the upc search type. 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_test_subscription(
        self,
        eventType: str,
        eventUrl: str,
        eventVersion: str,
        resourceName: str,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        authDetails: Optional[_WalmartTestSubscriptionAuthdetails] = None,
        headers: Optional[_WalmartTestSubscriptionHeaders] = None,
    ) -> Dict[str, Any]:
        """Sends a test event to a Walmart webhook subscription endpoint to verify that the subscription is correctly configured and receiving events. Use this to validate a webhook before relying on it for live events. Does not modify subscription configuration, but does trigger an outbound HTTP request to the subscribed URL.

        Args:
            eventType: Type of event triggering the subscription. (required)
            eventUrl: The URL endpoint where the event is sent. (required)
            eventVersion: Version identifier for the event message. (required)
            resourceName: The name of the resource associated with the event. (required)
            WM_QOSCORRELATION_ID: Correlation ID for tracking request quality of service.
            authDetails: Optional authentication details for event delivery.
            headers: HTTP headers to include in the notification request.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_update_inventory(
        self,
        inventoryAvailableDate: Optional[str] = None,
        quantity: Optional[_WalmartUpdateInventoryQuantity] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the inventory quantity for a specific Walmart Marketplace item to reflect current stock levels. Use this when stock levels change for a single item. Do not use this for bulk inventory updates across multiple items — use walmart_bulk_item_inventory_update instead. Overwrites the existing inventory record for the specified item.

        Args:
            inventoryAvailableDate: The date when the inventory will be available (ISO 8601 date string).
            quantity: Object describing the quantity to set or update for the given SKU.
            sku: The Stock Keeping Unit identifier for the item in the request body.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_update_inventory_marketplace(
        self,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
        quantity: Optional[_WalmartUpdateInventoryMarketplaceQuantity] = None,
        shipNode: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the inventory quantity for a specific item on the Walmart Marketplace (marketplace.walmartapis.com endpoint). Use this when stock levels change for a single item via the marketplace API. Do not use this for bulk updates — use walmart_bulk_item_inventory_update instead. Overwrites the existing inventory record for the specified item.

        Args:
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
            quantity: 
            shipNode: 
            sku: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_update_prices(
        self,
        MPItem: Optional[List[Any]] = None,
        MPItemFeedHeader: Optional[_WalmartUpdatePricesMpitemfeedheader] = None,
        feedType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Submits a bulk feed to update prices for one or more items listed on Walmart Marketplace. Use this when current market conditions require price adjustments. Do not use this to update a single items inventory — use walmart_update_inventory instead. Triggers an asynchronous feed processing job; price changes are not applied instantly.

        Args:
            MPItem: 
            MPItemFeedHeader: Header information for the marketplace item feed.
            feedType: The type of feed being submitted (for example: item, inventory, price).
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_update_repricer_strategy(
        self,
        strategyCollectionId: str,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
        enableRepricerForPromotion: Optional[bool] = None,
        enabled: Optional[bool] = None,
        repricerStrategy: Optional[str] = None,
        strategies: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing Walmart Marketplace repricer strategy identified by its strategy collection ID, modifying its pricing rules or parameters. Use this to adjust how automated repricing operates for a set of items. Do not use this to create a new strategy — use walmart_create_repricer_strategy instead. Overwrites the existing strategy configuration.

        Args:
            strategyCollectionId:  (required)
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
            enableRepricerForPromotion: 
            enabled: 
            repricerStrategy: 
            strategies: 
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_update_shipment_quantities(
        self,
        inboundOrderId: str,
        orderItems: List[Any],
        shipmentId: str,
    ) -> Dict[str, Any]:
        """Updates the item quantities within one or more active Walmart inbound shipments. Use this when the expected quantities of items in a shipment change before the shipment is received. Do not use this on completed or cancelled shipments. Overwrites existing quantity records for the specified shipment.

        Args:
            inboundOrderId: Unique identifier for the inbound order associated with this request. (required)
            orderItems:  (required)
            shipmentId: Identifier for the shipment that this update pertains to. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_update_subscription(
        self,
        eventType: str,
        eventUrl: str,
        resourceName: str,
        status: str,
        subscriptionId: str,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        authDetails: Optional[_WalmartUpdateSubscriptionAuthdetails] = None,
        eventVersion: Optional[str] = None,
        headers: Optional[_WalmartUpdateSubscriptionHeaders] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing Walmart webhook subscription identified by its subscription ID. Use this to change the event types, callback URL, or other properties of a webhook subscription. Do not use this to create a new subscription — use walmart_create_subscription instead. Modifies an existing subscription in place.

        Args:
            eventType: Type of event that the subscription listens to. (required)
            eventUrl: URL endpoint where the webhook events are sent. (required)
            resourceName: Name of the resource associated with the webhook event. (required)
            status: Current status of the subscription. (required)
            subscriptionId: Identifier of the subscription to update. (required)
            WM_QOSCORRELATION_ID: Correlation identifier for tracking the quality of service.
            authDetails: Authentication related details for the webhook events.
            eventVersion: Version of the event notification schema.
            headers: Headers included as part of the webhook notification.
        Returns:
            API response as a dictionary.
        """
        ...

    def walmart_update_subscription_marketplace(
        self,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
        authDetails: Optional[_WalmartUpdateSubscriptionMarketplaceAuthdetails] = None,
        eventUrl: Optional[str] = None,
        status: Optional[str] = None,
        subscriptionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing Walmart webhook subscription via the marketplace API endpoint, identified by its subscription ID. Use this to change callback URL, event types, or other properties of a webhook subscription on the marketplace.walmartapis.com endpoint. Do not use this to create a new subscription — use walmart_create_subscription instead. Modifies an existing subscription in place.

        Args:
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
            authDetails: 
            eventUrl: 
            status: 
            subscriptionId: 
        Returns:
            API response as a dictionary.
        """
        ...

