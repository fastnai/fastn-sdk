"""Fastn Walmart connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class WalmartConnector:
    """Walmart connector ().

    Provides 28 tools.
    """

    def bulk_item_inventory_update(
        self,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the inventory levels of multiple items in bulk within the inventory management system.

        Args:
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cancel_inbound_shipment(
        self,
        inboundOrderId: str,
    ) -> Dict[str, Any]:
        """Cancels an inbound shipment record in the logistics system, halting its processing.

        Args:
            inboundOrderId: The identifier of the inbound order to be accessed or manipulated on My data sources. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def catalog_search_items(
        self,
    ) -> Dict[str, Any]:
        """Searches for items in the catalog based on specified criteria, returning matching results from the catalog management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_inbound_shipment(
        self,
        inboundOrderId: str,
        orderItems: List[Any],
        inboundServices: Optional[Dict[str, Any]] = None,
        returnAddress: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new inbound shipment record in the logistics system for tracking incoming products.

        Args:
            inboundOrderId: Unique identifier for the inbound order. (required)
            orderItems:  (required)
            inboundServices: Inbound service options available for the order.
            returnAddress: Return address details for the inbound order.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_repricer_strategy(
        self,
        ContentType: Optional[str] = None,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new repricer strategy in the pricing management system to adjust item prices based on defined rules.

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

    def create_subscription(
        self,
        WM_QOSCORRELATION_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new subscription in the subscription management system, allowing for recurring transactions or access.

        Args:
            WM_QOSCORRELATION_ID: Correlation ID used for tracking the request through Walmart services.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_repricer_strategy(
        self,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a repricer strategy in the pricing management system, removing price adjustment rules.

        Args:
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_subscription(
        self,
        WM_QOSCORRELATION_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing subscription in the subscription management system, ceasing all future transactions.

        Args:
            WM_QOSCORRELATION_ID: Unique identifier for tracking the quality of service of the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_access_token(
        self,
        WM_SVCNAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains an access token for authenticated requests within the application ecosystem.

        Args:
            WM_SVCNAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_items(
        self,
        WM_QOS_CORRELATION_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a comprehensive list of all items in the inventory management system.

        Args:
            WM_QOS_CORRELATION_ID: Correlation identifier for tracing requests through the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_subscriptions(
        self,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all active subscriptions within the subscription management system.

        Args:
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_event_types(
        self,
        WM_QOSCORRELATION_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of available event types within the event management system.

        Args:
            WM_QOSCORRELATION_ID: Correlation ID used for tracing the quality of service of the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inbound_shipment_items(
        self,
        shipmentId: str,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of items that are part of an existing inbound shipment in the logistics system.

        Args:
            shipmentId: Identifier of the shipment to retrieve. (required)
            limit: Maximum number of items to return.
            offset: Starting position for results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inventory(
        self,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the current inventory levels and details for all tracked items in the inventory management system.

        Args:
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_item(
        self,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific item in the inventory management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_item_count_by_groups(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the count of items categorized under specific groups in the inventory system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_item_count_by_status(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the count of items filtered by their current status (e.g., in stock, sold out) in the inventory system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_list_of_incentive_items(
        self,
        ContentType: Optional[str] = None,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of items eligible for incentives in the inventory system.

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

    def get_orders(
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
        """Fetches orders placed by customers, providing details on each transaction within the order management system.

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

    def get_shipments(
        self,
        fromCreateDate: Optional[str] = None,
        inboundOrderId: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        shipmentId: Optional[str] = None,
        status: Optional[str] = None,
        toCreateDate: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves shipment details for processed orders in the shipping management system.

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

    def get_subscriptions(
        self,
        WM_QOSCORRELATION_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all subscriptions associated with the user's account in the subscription management system.

        Args:
            WM_QOSCORRELATION_ID: Unique identifier for quality of service correlation.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_taxonomy(
        self,
        WM_CONSUMER_CHANNEL_TYPE: Optional[str] = None,
        WM_QOS_CORRELATION_ID: Optional[str] = None,
        WM_SEC_ACCESS_TOKEN: Optional[str] = None,
        WM_SVC_NAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the taxonomy structure of categories used for items in the inventory management system.

        Args:
            WM_CONSUMER_CHANNEL_TYPE: 
            WM_QOS_CORRELATION_ID: 
            WM_SEC_ACCESS_TOKEN: 
            WM_SVC_NAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def retire_item(
        self,
        WM_CONSUMER_CHANNEL_TYPE: Optional[str] = None,
        WM_QOS_CORRELATION_ID: Optional[str] = None,
        WM_SEC_ACCESS_TOKEN: Optional[str] = None,
        WM_SVC_NAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retires an item from inventory, marking it as no longer available in the system.

        Args:
            WM_CONSUMER_CHANNEL_TYPE: 
            WM_QOS_CORRELATION_ID: 
            WM_SEC_ACCESS_TOKEN: 
            WM_SVC_NAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def search_item(
        self,
        WM_CONSUMER_CHANNEL_TYPE: Optional[str] = None,
        WM_QOS_CORRELATION_ID: Optional[str] = None,
        WM_SEC_ACCESS_TOKEN: Optional[str] = None,
        WM_SVC_NAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for a specific item in the inventory management system based on provided criteria.

        Args:
            WM_CONSUMER_CHANNEL_TYPE: 
            WM_QOS_CORRELATION_ID: 
            WM_SEC_ACCESS_TOKEN: 
            WM_SVC_NAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def test_subscription(
        self,
        WM_QOSCORRELATION_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Tests an existing subscription for functionality within the subscription management system.

        Args:
            WM_QOSCORRELATION_ID: Correlation ID for tracking request quality of service.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_inventory(
        self,
        WM_CONSUMERCHANNELTYPE: Optional[str] = None,
        WM_QOSCORRELATION_ID: Optional[str] = None,
        WM_SECACCESS_TOKEN: Optional[str] = None,
        WM_SVCNAME: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the inventory details for a specific item in the inventory management system.

        Args:
            WM_CONSUMERCHANNELTYPE: 
            WM_QOSCORRELATION_ID: 
            WM_SECACCESS_TOKEN: 
            WM_SVCNAME: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_repricer_strategy(
        self,
    ) -> Dict[str, Any]:
        """Updates an existing repricer strategy in the pricing management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_subscription(
        self,
        WM_QOSCORRELATION_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing subscription in the subscription management system.

        Args:
            WM_QOSCORRELATION_ID: Correlation identifier for tracking the quality of service.
        Returns:
            API response as a dictionary.
        """
        ...

