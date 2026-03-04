"""Fastn Trackstar connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _TrackstarCreateInboundShipmentSupplierObject(TypedDict, total=False):
    supplier_id: str

class _TrackstarCreateKitProductMeasurements(TypedDict, total=False):
    height: str
    length: str
    unit: str
    weight: str
    weight_unit: str
    width: str

class _TrackstarCreateOrderChannelObject(TypedDict, total=False):
    channel_id: str

class _TrackstarCreateOrderShipToAddress(TypedDict, total=False):
    address1: str
    address2: str
    city: str
    company: str
    country: str
    full_name: str
    postal_code: str
    state: str

class _TrackstarCreateProductMeasurements(TypedDict, total=False):
    height: str
    length: str
    unit: str
    weight: str
    weight_unit: str
    width: str

class _TrackstarShipOrderMeasurements(TypedDict, total=False):
    height: str
    length: str
    unit: str
    weight: str
    weight_unit: str
    width: str

class _TrackstarUpdateInboundShipmentSupplierObject(TypedDict, total=False):
    supplier_id: str

class _TrackstarUpdateKitProductMeasurements(TypedDict, total=False):
    height: str
    length: str
    unit: str
    weight: str
    weight_unit: str
    width: str

class _TrackstarUpdateOrderChannelObject(TypedDict, total=False):
    channel_id: str

class _TrackstarUpdateOrderShipToAddress(TypedDict, total=False):
    address1: str
    address2: str
    city: str
    company: str
    country: str
    full_name: str
    postal_code: str
    state: str

class _TrackstarUpdateProductMeasurements(TypedDict, total=False):
    height: str
    length: str
    unit: str
    weight: str
    weight_unit: str
    width: str

class _TrackstarUpdateSaleFulfillmentShipmentShippingaddress(TypedDict, total=False):
    City: str
    Company: str
    Contact: str
    Country: str
    DisplayAddressLine1: str
    DisplayAddressLine2: str
    Line1: str
    Line2: str
    Postcode: str
    ShipToOther: bool
    State: str

class TrackstarConnector:
    """Trackstar connector ().

    Provides 76 tools.
    """

    def trackstar_adjust_inventory_for_product(
        self,
        adjustment_type: Optional[str] = None,
        product_id: Optional[str] = None,
        quantity: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adjusts the inventory level for a specific product in the cart system, identified by product_id, to correct stock counts or reflect changes in availability. Use this tool when you need to update the stock quantity of a cart-connected product. Do not use this tool to adjust WMS inventory items — use the adjust inventory item tool instead. This operation modifies cart product inventory levels in place.

        Args:
            adjustment_type: 
            product_id: 
            quantity: 
            warehouse_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_adjust_inventory_item(
        self,
        adjustment_type: Optional[str] = None,
        inventory_id: Optional[str] = None,
        location_id: Optional[str] = None,
        quantity: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adjusts the quantity or attributes of a specific inventory item identified by inventory_id in the WMS, such as correcting stock counts or recording shrinkage. Use this tool when you need to make a direct adjustment to an inventory record. Do not use this tool to adjust cart product inventory — use the adjust inventory for product tool instead, and do not use this tool to update Trackstar tags on inventory — use the update inventory Trackstar tags tool instead. This operation modifies inventory levels in place.

        Args:
            adjustment_type: The type of inventory adjustment.
            inventory_id: The ID of the inventory item.
            location_id: The ID of the inventory location.
            quantity: The quantity of the inventory item.
            warehouse_id: The ID of the warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_cancel_order(
        self,
        order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Cancels an existing order identified by order_id in the WMS, removing it from the active order processing workflow. Use this tool when a customer or operator needs to cancel an order before it has been fulfilled or shipped. Do not use this tool to update order details — use the update order tool instead. Cancellation may be irreversible once the order has reached certain fulfillment states, and downstream inventory or notification workflows may be triggered.

        Args:
            order_id: ID of the order.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_create_cart_order_shipment(
        self,
        carrier: Optional[str] = None,
        order_id: Optional[str] = None,
        shipping_method: Optional[str] = None,
        tracking_number: Optional[str] = None,
        tracking_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a shipment record for a specific cart order identified by order_id, initiating the delivery process for items in the cart order. Use this tool when a cart order is ready to be dispatched and a shipment needs to be logged. Do not use this tool to ship WMS orders — use the ship order tool instead. This operation creates a new shipment and may trigger downstream fulfillment and notification workflows.

        Args:
            carrier: The shipping carrier (e.g., FedEx, UPS).
            order_id: The ID of the order associated with the shipment.
            shipping_method: The shipping method used (e.g., Ground, Express).
            tracking_number: The tracking number for the shipment.
            tracking_url: URL to track the shipment online.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_create_inbound_shipment(
        self,
        expected_arrival_date: Optional[str] = None,
        line_items: Optional[List[Any]] = None,
        purchase_order_number: Optional[str] = None,
        supplier: Optional[str] = None,
        supplier_object: Optional[_TrackstarCreateInboundShipmentSupplierObject] = None,
        tracking_number: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new inbound shipment record in the WMS to track incoming inventory from a supplier, including expected items and quantities. Use this tool when you need to register a new shipment that is expected to arrive at the warehouse. Do not use this tool to update an existing inbound shipment — use the update inbound shipment tool instead, and do not use this tool to mark a shipment as received — use the receive inbound shipment tool instead. This operation creates a new inbound shipment record.

        Args:
            expected_arrival_date: Expected arrival date
            line_items: 
            purchase_order_number: Purchase order number
            supplier: Supplier name
            supplier_object: Supplier object details
            tracking_number: Tracking number
            warehouse_id: Warehouse ID
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_create_kit_product(
        self,
        gtin: Optional[str] = None,
        inventory_items: Optional[List[Any]] = None,
        measurements: Optional[_TrackstarCreateKitProductMeasurements] = None,
        name: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new kit product in the WMS by bundling multiple individual items together into a single sellable unit. Use this tool when you need to define a new product kit with its component items and quantities. Do not use this tool to update an existing kit — use the update kit product tool instead, and do not use this tool to create a standard product — use the create product tool instead. This operation creates a new kit product record in the inventory system.

        Args:
            gtin: Global Trade Item Number.
            inventory_items: 
            measurements: Measurements of the product.
            name: Name of the product.
            sku: Stock Keeping Unit.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_create_link_token(
        self,
        connection_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a short-lived link token used to initiate the Trackstar authentication and connection flow for a user. Use this tool when you need to start the OAuth or link process to connect a new integration. Do not use this tool to exchange an authorization code for an access token — use the exchange auth code tool instead. The generated token is single-use and expires after a short period.

        Args:
            connection_id: ID of the connection.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_create_order(
        self,
        channel: Optional[str] = None,
        channel_object: Optional[_TrackstarCreateOrderChannelObject] = None,
        invoice_currency_code: Optional[str] = None,
        line_items: Optional[List[Any]] = None,
        order_number: Optional[str] = None,
        reference_id: Optional[str] = None,
        ship_to_address: Optional[_TrackstarCreateOrderShipToAddress] = None,
        shipping_method: Optional[str] = None,
        total_discount: Optional[str] = None,
        total_price: Optional[str] = None,
        total_shipping: Optional[str] = None,
        total_tax: Optional[str] = None,
        trading_partner: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new order record in the WMS, capturing customer purchase details, line items, and shipping specifications. Use this tool when you need to register a new customer order for fulfillment. Do not use this tool to update an existing order — use the update order tool instead, and do not use this tool to create cart orders — use the cart order tools instead. This operation creates a new order and may trigger fulfillment workflows.

        Args:
            channel: The sales channel for the order.
            channel_object: Additional details about the sales channel.
            invoice_currency_code: The currency code for the invoice.
            line_items: 
            order_number: The order number.
            reference_id: A reference ID for the order.
            ship_to_address: The shipping address for the order.
            shipping_method: The shipping method used for the order.
            total_discount: The total discount applied to the order.
            total_price: The total price of the order.
            total_shipping: The total shipping cost for the order.
            total_tax: The total tax amount for the order.
            trading_partner: The trading partner associated with this order.
            warehouse_customer_id: The ID of the warehouse customer.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_create_order_file(
        self,
        order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads or attaches a file to a specific order identified by order_id in the WMS, such as packing slips, invoices, or supporting documents. Use this tool when you need to associate a document with an order for record-keeping or processing purposes. Do not use this tool to create the order itself — use the create order tool instead. This operation adds a file attachment to the existing order record.

        Args:
            order_id: ID of the order.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_create_product(
        self,
        gtin: Optional[str] = None,
        measurements: Optional[_TrackstarCreateProductMeasurements] = None,
        name: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new product record in the WMS inventory with details such as name, SKU, price, and description. Use this tool when you need to add a brand-new product to the catalog. Do not use this tool to update an existing product — use the update product tool instead, and do not use this tool to create a kit product — use the create kit product tool instead. This operation creates a new product entry in the inventory system.

        Args:
            gtin: Global Trade Item Number.
            measurements: Measurements of the product.
            name: Name of the product.
            sku: Stock Keeping Unit.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_create_return(
        self,
        line_items: Optional[List[Any]] = None,
        order_id: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new return record in the WMS to process the return of products from a customer back to inventory. Use this tool when you need to register an incoming return request, including the items being returned and associated order details. Do not use this tool to update an existing return — use the update return tool instead. This operation creates a new return record and may trigger downstream inventory and notification workflows.

        Args:
            line_items: 
            order_id: ID of the order.
            warehouse_id: ID of the warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_delete_connection(
        self,
    ) -> Dict[str, Any]:
        """Permanently deletes an integration connection from the Trackstar system, removing all associated configuration and integration data. Use this tool when you need to remove a connection that is no longer needed. Do not use this tool if you only want to disable or pause a connection — deletion is irreversible and all data associated with the connection will be lost. This operation cannot be undone.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_exchange_auth_code(
        self,
        auth_code: Optional[str] = None,
        customer_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exchanges an OAuth authorization code for an access token, completing the authentication flow to enable secure API access to Trackstar. Use this tool after a user has completed the OAuth consent flow and an authorization code has been returned. Do not use this tool to generate a link token — use the create link token tool instead. This operation consumes the authorization code, which can only be used once.

        Args:
            auth_code: Authorization code for the request.
            customer_id: The ID of the customer.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_generate_sandbox(
        self,
        integration_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a sandbox environment for a specific integration type, populating it with test data to support development and testing workflows without affecting live production data. Use this tool when you need to set up an isolated test environment for a given integration type. Do not use this tool in production environments. This operation creates new sandbox resources and test data that persist until the sandbox is reset or removed.

        Args:
            integration_type: Type of integration for the Trackstar API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_bill(
        self,
        bill_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific billing record identified by bill_id, including charges, line items, and payment status. Use this tool when you need to review or audit a single bill in the WMS billing system. Do not use this tool to retrieve all bills — use the list bills tool instead. This is a read-only operation.

        Args:
            bill_id: ID of the bill.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_cart_order(
        self,
        order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific order from the cart system, identified by order_id, including line items, status, and cart-specific metadata. Use this tool when you need to look up a single cart order. Do not use this tool to retrieve WMS orders — use the get order tool instead, and do not use this tool to list all cart orders — use the list cart orders tool instead. This is a read-only operation.

        Args:
            order_id: Order ID for the Trackstar API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_cart_product(
        self,
        product_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific product listed in the cart system, identified by product_id, including inventory levels and product attributes as seen by the cart integration. Use this tool when you need to look up a single product within the cart context. Do not use this tool to retrieve WMS products — use the get product tool instead, and do not use this tool to list all cart products — use the list cart products tool instead. This is a read-only operation.

        Args:
            product_id: ID of the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_cart_warehouse(
        self,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific warehouse linked to the cart system, identified by warehouse_id, including storage configuration and associated cart integration settings. Use this tool when you need to look up a single cart-connected warehouse. Do not use this tool to retrieve WMS warehouses — use the get warehouse tool instead, and do not use this tool to list all cart warehouses — use the list cart warehouses tool instead. This is a read-only operation.

        Args:
            warehouse_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_connection(
        self,
        connection_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific integration connection identified by connection_id, including its status, configuration, and associated integration metadata. Use this tool when you need to inspect or troubleshoot a single connection. Do not use this tool to retrieve all connections — use the list connections tool instead. This is a read-only operation.

        Args:
            connection_id: The ID of the connection.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_inbound_shipment(
        self,
        inbound_shipment_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific inbound shipment identified by inbound_shipment_id, including expected quantities, supplier information, and receipt status. Use this tool when you need to look up the current state or details of a single inbound shipment. Do not use this tool to retrieve all inbound shipments — use the list inbound shipments tool instead. This is a read-only operation.

        Args:
            inbound_shipment_id: ID of the inbound shipment.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_integration_info(
        self,
        integration_name: Optional[str] = None,
        integration_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves configuration and status information for a single integration identified by integration_type and integration_name. Use this tool when you need details about a specific integration such as its health, configuration, or connection status for troubleshooting or analysis. Do not use this tool to retrieve information about all integrations of a given type — use the list integration info tool instead. This is a read-only operation.

        Args:
            integration_name: Name of the integration.
            integration_type: Type of the integration.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_inventory_item(
        self,
        inventory_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific inventory item identified by inventory_id, including current stock levels, location, and associated product details. Use this tool when you need to look up a single inventory record. Do not use this tool to retrieve all inventory items — use the list inventory items tool instead. This is a read-only operation.

        Args:
            inventory_id: ID of the inventory item.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_inventory_ledger(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the inventory ledger, which is a log of all stock movements, adjustments, and transactions recorded in the WMS. Use this tool when you need to audit inventory changes, trace stock discrepancies, or review historical inventory activity. Do not use this tool to retrieve current inventory levels for specific items — use the get inventory item or list inventory items tools instead. This is a read-only operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_kit_schema_for_connection(
        self,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the JSON schema defining the required and optional fields for creating or updating a kit product for the currently active connection. Use this tool when you need to understand the data structure required by the connected system before submitting a create or update kit request. Do not use this tool to get the schema for a specific named integration — use the get kit schema for integration tool instead. This is a read-only operation.

        Args:
            method: HTTP method for the Trackstar API request (e.g., GET, POST).
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_kit_schema_for_integration(
        self,
        integration_name: Optional[str] = None,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the JSON schema defining the required and optional fields for creating or updating a kit product for a specific integration identified by integration_name. Use this tool when you need to understand the exact data structure expected by a particular integration before submitting a create or update kit request. Do not use this tool to get the schema for the active connection — use the get kit schema for connection tool instead. This is a read-only operation.

        Args:
            integration_name: Name of the integration.
            method: HTTP method for the Trackstar API request (e.g., GET, POST).
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_labor_activity(
        self,
        labor_activity_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific labor activity record identified by labor_activity_id, including activity type, duration, and associated worker information. Use this tool when you need to review a single labor activity for analysis or resource management. Do not use this tool to retrieve all labor activities — use the list labor activities tool instead. This is a read-only operation.

        Args:
            labor_activity_id: The ID of the labor activity.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_order(
        self,
        order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific order identified by order_id from the WMS, including line items, status, shipping details, and customer information. Use this tool when you need to look up the current state or details of a single order. Do not use this tool to retrieve all orders — use the list orders tool instead. This is a read-only operation.

        Args:
            order_id: The ID of the order.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_order_schema_for_connection(
        self,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the JSON schema defining the required and optional fields for creating or updating an order for the currently active connection. Use this tool when you need to understand the data structure required by the connected system before submitting a create or update order request. Do not use this tool to get the schema for a specific named integration — use the get order schema for integration tool instead. This is a read-only operation.

        Args:
            method: HTTP method for the Trackstar API request (e.g., GET, POST, PUT, DELETE).
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_order_schema_for_integration(
        self,
        integration_name: Optional[str] = None,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the JSON schema defining the required and optional fields for creating or updating an order for a specific integration identified by integration_name. Use this tool when you need to understand the exact data structure expected by a particular integration before submitting a create or update order request. Do not use this tool to get the schema for the active connection — use the get order schema for connection tool instead. This is a read-only operation.

        Args:
            integration_name: Name of the integration.
            method: HTTP method for the Trackstar API request (e.g., GET, POST, PUT, DELETE).
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_product(
        self,
        product_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific product identified by product_id from the WMS inventory, including attributes such as name, SKU, price, and description. Use this tool when you need to look up a single product record. Do not use this tool to retrieve all products — use the list products tool instead. This is a read-only operation.

        Args:
            product_id: ID of the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_product_schema_for_connection(
        self,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the JSON schema defining the required and optional fields for creating or updating a product for the currently active connection. Use this tool when you need to understand the data structure required by the connected system before submitting a create or update product request. Do not use this tool to get the schema for a specific named integration — use the get product schema for integration tool instead. This is a read-only operation.

        Args:
            method: HTTP method for the Trackstar API request (e.g., GET, POST, PUT, DELETE).
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_product_schema_for_integration(
        self,
        integration_name: Optional[str] = None,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the JSON schema defining the required and optional fields for creating or updating a product for a specific integration identified by integration_name. Use this tool when you need to understand the exact data structure expected by a particular integration before submitting a create or update product request. Do not use this tool to get the schema for the active connection — use the get product schema for connection tool instead. This is a read-only operation.

        Args:
            integration_name: Name of the integration for the Trackstar API request.
            method: HTTP method for the Trackstar API request (e.g., GET, POST, PUT, DELETE).
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_return(
        self,
        return_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific return record identified by return_id, including return status, line items, and associated order information. Use this tool when you need to look up the current state or details of a single customer return. Do not use this tool to retrieve all returns — use the list returns tool instead. This is a read-only operation.

        Args:
            return_id: ID to be returned by the Trackstar API.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_return_schema_for_connection(
        self,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the JSON schema defining the required and optional fields for creating or updating a return for the currently active connection. Use this tool when you need to understand the data structure required by the connected system before submitting a create or update return request. Do not use this tool to get the schema for a specific named integration — use the get return schema for integration tool instead. This is a read-only operation.

        Args:
            method: The HTTP method for the Trackstar API request (e.g., GET, POST, PUT, DELETE).
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_return_schema_for_integration(
        self,
        integration_name: Optional[str] = None,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the JSON schema defining the required and optional fields for creating or updating a return for a specific integration identified by integration_name. Use this tool when you need to understand the exact data structure expected by a particular integration before submitting a create or update return request. Do not use this tool to get the schema for the active connection — use the get return schema for connection tool instead. This is a read-only operation.

        Args:
            integration_name: Name of the integration for the Trackstar API request.
            method: HTTP method for the Trackstar API request (e.g., GET, POST, PUT, DELETE).
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_shipment(
        self,
        shipment_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific freight shipment identified by shipment_id, including tracking information, status, and associated order details. Use this tool when you need to look up the current state or details of a single outbound freight shipment. Do not use this tool to retrieve all shipments — use the list shipments tool instead. This is a read-only operation.

        Args:
            shipment_id: ID of the shipment.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_shipping_method(
        self,
        shipping_method_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific shipping method identified by shipping_method_id, including carrier information, delivery timeframes, and cost parameters. Use this tool when you need to review a particular shipping option before assigning it to an order. Do not use this tool to retrieve all available shipping methods — use the list shipping methods tool instead. This is a read-only operation.

        Args:
            shipping_method_id: ID of the shipping method.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_warehouse(
        self,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific warehouse identified by warehouse_id, including its attributes such as name, address, and capacity. Use this tool when you need information about a single warehouse for logistics or inventory management decisions. Do not use this tool to retrieve all warehouses — use the list warehouses tool instead. This is a read-only operation.

        Args:
            warehouse_id: ID of the warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_warehouse_customer(
        self,
        warehouse_customer_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific warehouse customer identified by warehouse_customer_id, including customer profile and associated warehouse configuration. Use this tool when you need to look up a single warehouse customer for review or management purposes. Do not use this tool to retrieve all warehouse customers — use the list warehouse customers tool instead. This is a read-only operation.

        Args:
            warehouse_customer_id: ID of the warehouse customer.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_get_warehouse_location(
        self,
        location_id: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific location within a warehouse, identified by both warehouse_id and location_id. Use this tool when you need information about a particular warehouse location such as its zone, aisle, or capacity for inventory placement decisions. Do not use this tool to retrieve all locations in a warehouse — use the list warehouse locations tool instead. This is a read-only operation.

        Args:
            location_id: ID of the location.
            warehouse_id: ID of the warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_bills(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
        warehouse_customer_idcontains: Optional[str] = None,
        warehouse_customer_ideq: Optional[str] = None,
        warehouse_customer_idin: Optional[str] = None,
        warehouse_customer_idneq: Optional[str] = None,
        warehouse_customer_idnin: Optional[str] = None,
        warehouse_customer_idnot_contains: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all billing records in the WMS, including charges, line items, and payment statuses. Use this tool when you need a financial overview of all bills for reporting or expense tracking. Do not use this tool to retrieve details of a single bill — use the get bill tool instead. This is a read-only operation.

        Args:
            created_date: 
            created_dateeq: 
            created_dategt: 
            created_dategte: 
            created_datein: 
            created_datelt: 
            created_datelte: 
            created_dateneq: 
            created_datenin: 
            idsin: 
            limit: 
            page_token: 
            updated_date: 
            updated_dateeq: 
            updated_dategt: 
            updated_dategte: 
            updated_datein: 
            updated_datelt: 
            updated_datelte: 
            updated_dateneq: 
            updated_datenin: 
            warehouse_customer_id: 
            warehouse_customer_idcontains: 
            warehouse_customer_ideq: 
            warehouse_customer_idin: 
            warehouse_customer_idneq: 
            warehouse_customer_idnin: 
            warehouse_customer_idnot_contains: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_cart_orders(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        order_number: Optional[str] = None,
        order_numbercontains: Optional[str] = None,
        order_numbereq: Optional[str] = None,
        order_numberin: Optional[str] = None,
        order_numbernin: Optional[str] = None,
        order_numbernot_contains: Optional[str] = None,
        page_token: Optional[str] = None,
        status: Optional[str] = None,
        statuscontains: Optional[str] = None,
        statuseq: Optional[str] = None,
        statusin: Optional[str] = None,
        statusneq: Optional[str] = None,
        statusnin: Optional[str] = None,
        statusnot_contains: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
        warehouse_customer_idcontains: Optional[str] = None,
        warehouse_customer_ideq: Optional[str] = None,
        warehouse_customer_idin: Optional[str] = None,
        warehouse_customer_idneq: Optional[str] = None,
        warehouse_customer_idnin: Optional[str] = None,
        warehouse_customer_idnot_contains: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all orders from the cart system, including their statuses, line items, and cart-specific metadata. Use this tool when you need an overview of all active and completed cart orders. Do not use this tool to retrieve WMS orders — use the list orders tool instead, and do not use this tool to retrieve a single cart order — use the get cart order tool instead. This is a read-only operation.

        Args:
            created_date: Filter records by created date.
            created_dateeq: Filter records where the created date is equal to a specified value.
            created_dategt: Filter records where the created date is greater than a specified value.
            created_dategte: Filter records where the created date is greater than or equal to a specified value.
            created_datein: Filter records where the created date is within a specified range.
            created_datelt: Filter records where the created date is less than a specified value.
            created_datelte: Filter records where the created date is less than or equal to a specified value.
            created_dateneq: Filter records where the created date is not equal to a specified value.
            created_datenin: Filter records where the created date is within a specified range.
            idsin: Filter records where the ID is in a specified list.
            limit: Limit the number of records returned.
            order_number: Filter records by order number.
            order_numbercontains: Filter records where the order number contains a specified substring.
            order_numbereq: Filter records where the order number is equal to a specified value.
            order_numberin: Filter records where the order number is in a specified list.
            order_numbernin: Filter records where the order number is not in a specified list.
            order_numbernot_contains: Filter records where the order number does not contain a specified substring.
            page_token: Token for pagination.
            status: Filter records by status.
            statuscontains: Filter records where the status contains a specified substring.
            statuseq: Filter records where the status is equal to a specified value.
            statusin: Filter records where the status is in a specified list.
            statusneq: Filter records where the status is not equal to a specified value.
            statusnin: Filter records where the status is not in a specified list.
            statusnot_contains: Filter records where the status does not contain a specified substring.
            updated_date: Filter records by updated date.
            updated_dateeq: Filter records where the updated date is equal to a specified value.
            updated_dategt: Filter records where the updated date is greater than a specified value.
            updated_dategte: Filter records where the updated date is greater than or equal to a specified value.
            updated_datein: Filter records where the updated date is within a specified range.
            updated_datelt: Filter records where the updated date is less than a specified value.
            updated_datelte: Filter records where the updated date is less than or equal to a specified value.
            updated_dateneq: Filter records where the updated date is not equal to a specified value.
            updated_datenin: Filter records where the updated date is within a specified range.
            warehouse_customer_id: Filter records by warehouse customer ID.
            warehouse_customer_idcontains: Filter records where the warehouse customer ID contains a specified substring.
            warehouse_customer_ideq: Filter records where the warehouse customer ID is equal to a specified value.
            warehouse_customer_idin: Filter records where the warehouse customer ID is in a specified list.
            warehouse_customer_idneq: Filter records where the warehouse customer ID is not equal to a specified value.
            warehouse_customer_idnin: Filter records where the warehouse customer ID is not in a specified list.
            warehouse_customer_idnot_contains: Filter records where the warehouse customer ID does not contain a specified substring.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_cart_products(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all products available in the cart system, including inventory levels and product attributes as seen by the cart integration. Use this tool when you need a catalog-level overview of cart-connected products. Do not use this tool to retrieve WMS products — use the list products tool instead, and do not use this tool to retrieve a single cart product — use the get cart product tool instead. This is a read-only operation.

        Args:
            created_date: Filter results by created date.
            created_dateeq: Filter results where the created date equals the specified value.
            created_dategt: Filter results where the created date is greater than the specified value.
            created_dategte: Filter results where the created date is greater than or equal to the specified value.
            created_datein: Filter results where the created date is within the specified range.
            created_datelt: Filter results where the created date is less than the specified value.
            created_datelte: Filter results where the created date is less than or equal to the specified value.
            created_dateneq: Filter results where the created date is not equal to the specified value.
            created_datenin: Filter results where the created date is not within the specified range.
            idsin: Filter results where the ID is in the specified list.
            limit: Number of results to return per page.
            page_token: Token for pagination.
            updated_date: Filter results by updated date.
            updated_dateeq: Filter results where the updated date equals the specified value.
            updated_dategt: Filter results where the updated date is greater than the specified value.
            updated_dategte: Filter results where the updated date is greater than or equal to the specified value.
            updated_datein: Filter results where the updated date is within the specified range.
            updated_datelt: Filter results where the updated date is less than the specified value.
            updated_datelte: Filter results where the updated date is less than or equal to the specified value.
            updated_dateneq: Filter results where the updated date is not equal to the specified value.
            updated_datenin: Filter results where the updated date is not within the specified range.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_cart_warehouses(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all warehouses linked to the cart system, including their storage configurations and cart integration settings. Use this tool when you need an overview of all cart-connected warehouses. Do not use this tool to retrieve WMS warehouses — use the list warehouses tool instead, and do not use this tool to retrieve a single cart warehouse — use the get cart warehouse tool instead. This is a read-only operation.

        Args:
            created_date: Filter results by created date.
            created_dateeq: Filter results where the created date equals the specified value.
            created_dategt: Filter results where the created date is greater than the specified value.
            created_dategte: Filter results where the created date is greater than or equal to the specified value.
            created_datein: Filter results where the created date is in the specified list.
            created_datelt: Filter results where the created date is less than the specified value.
            created_datelte: Filter results where the created date is less than or equal to the specified value.
            created_dateneq: Filter results where the created date is not equal to the specified value.
            created_datenin: Filter results where the created date is not in the specified list.
            idsin: Filter results where the ID is in the specified list.
            limit: Number of records to return per page.
            page_token: Token for pagination.
            updated_date: Filter results by updated date.
            updated_dateeq: Filter results where the updated date equals the specified value.
            updated_dategt: Filter results where the updated date is greater than the specified value.
            updated_dategte: Filter results where the updated date is greater than or equal to the specified value.
            updated_datein: Filter results where the updated date is in the specified list.
            updated_datelt: Filter results where the updated date is less than the specified value.
            updated_datelte: Filter results where the updated date is less than or equal to the specified value.
            updated_dateneq: Filter results where the updated date is not equal to the specified value.
            updated_datenin: Filter results where the updated date is not in the specified list.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_connections(
        self,
        page_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all integration connections currently configured in the Trackstar system, including their status and associated integration details. Use this tool when you need an overview of all active and inactive connections. Do not use this tool to retrieve details of a single connection — use the get connection tool instead. This is a read-only operation.

        Args:
            page_token: Token for retrieving the next page of results.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_inbound_shipment_suppliers(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
        warehouse_customer_idcontains: Optional[str] = None,
        warehouse_customer_ideq: Optional[str] = None,
        warehouse_customer_idin: Optional[str] = None,
        warehouse_customer_idneq: Optional[str] = None,
        warehouse_customer_idnin: Optional[str] = None,
        warehouse_customer_idnot_contains: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all suppliers associated with inbound shipments in the WMS, including supplier names and contact details. Use this tool when you need an overview of all suppliers sending inventory into the warehouse. Do not use this tool to retrieve individual inbound shipment details — use the get inbound shipment or list inbound shipments tools instead. This is a read-only operation.

        Args:
            created_date: The date the record was created.
            created_dateeq: Filter records where the created date is equal to a specified value.
            created_dategt: Filter records where the created date is greater than a specified value.
            created_dategte: Filter records where the created date is greater than or equal to a specified value.
            created_datein: Filter records where the created date is within a specified range.
            created_datelt: Filter records where the created date is less than a specified value.
            created_datelte: Filter records where the created date is less than or equal to a specified value.
            created_dateneq: Filter records where the created date is not equal to a specified value.
            created_datenin: Filter records where the created date is within a specified range.
            idsin: Filter records where the ID is within a specified range.
            limit: The maximum number of records to return.
            page_token: Token for pagination.
            updated_date: The date the record was last updated.
            updated_dateeq: Filter records where the updated date is equal to a specified value.
            updated_dategt: Filter records where the updated date is greater than a specified value.
            updated_dategte: Filter records where the updated date is greater than or equal to a specified value.
            updated_datein: Filter records where the updated date is within a specified range.
            updated_datelt: Filter records where the updated date is less than a specified value.
            updated_datelte: Filter records where the updated date is less than or equal to a specified value.
            updated_dateneq: Filter records where the updated date is not equal to a specified value.
            updated_datenin: Filter records where the updated date is not within a specified range.
            warehouse_customer_id: Filter records where the warehouse customer ID matches a specified value.
            warehouse_customer_idcontains: Filter records where the warehouse customer ID contains a specified substring.
            warehouse_customer_ideq: Filter records where the warehouse customer ID is equal to a specified value.
            warehouse_customer_idin: Filter records where the warehouse customer ID is within a specified range.
            warehouse_customer_idneq: Filter records where the warehouse customer ID is not equal to a specified value.
            warehouse_customer_idnin: Filter records where the warehouse customer ID is not within a specified range.
            warehouse_customer_idnot_contains: Filter records where the warehouse customer ID does not contain a specified substring.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_inbound_shipments(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        expected_arrival_date: Optional[str] = None,
        expected_arrival_dateeq: Optional[str] = None,
        expected_arrival_dategt: Optional[str] = None,
        expected_arrival_dategte: Optional[str] = None,
        expected_arrival_datelt: Optional[str] = None,
        expected_arrival_datelte: Optional[str] = None,
        expected_arrival_dateneq: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        purchase_order_number: Optional[str] = None,
        purchase_order_numbercontains: Optional[str] = None,
        purchase_order_numbereq: Optional[str] = None,
        purchase_order_numberin: Optional[str] = None,
        purchase_order_numberneq: Optional[str] = None,
        purchase_order_numbernin: Optional[str] = None,
        purchase_order_numbernot_contains: Optional[str] = None,
        status: Optional[str] = None,
        statuscontains: Optional[str] = None,
        statuseq: Optional[str] = None,
        statusin: Optional[str] = None,
        statusneq: Optional[str] = None,
        statusnin: Optional[str] = None,
        statusnot_contains: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
        warehouse_customer_idcontains: Optional[str] = None,
        warehouse_customer_ideq: Optional[str] = None,
        warehouse_customer_idin: Optional[str] = None,
        warehouse_customer_idneq: Optional[str] = None,
        warehouse_customer_idnin: Optional[str] = None,
        warehouse_customer_idnot_contains: Optional[str] = None,
        warehouse_id: Optional[str] = None,
        warehouse_idcontains: Optional[str] = None,
        warehouse_ideq: Optional[str] = None,
        warehouse_idnot_contains: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all inbound shipments recorded in the WMS, including their statuses, expected quantities, and supplier details. Use this tool when you need an overview of all incoming inventory shipments. Do not use this tool to retrieve details of a single inbound shipment — use the get inbound shipment tool instead. This is a read-only operation.

        Args:
            created_date: Filter results based on the created date.
            created_dateeq: Filter results where the created date is equal to this value.
            created_dategt: Filter results where the created date is greater than this value.
            created_dategte: Filter results where the created date is greater than or equal to this value.
            created_datein: Filter results where the created date is in this list (comma-separated).
            created_datelt: Filter results where the created date is less than this value.
            created_datelte: Filter results where the created date is less than or equal to this value.
            created_dateneq: Filter results where the created date is not equal to this value.
            created_datenin: Filter results where the created date is not in this list (comma-separated).
            expected_arrival_date: Filter results based on the expected arrival date.
            expected_arrival_dateeq: Filter results where the expected arrival date is equal to this value.
            expected_arrival_dategt: Filter results where the expected arrival date is greater than this value.
            expected_arrival_dategte: Filter results where the expected arrival date is greater than or equal to this value.
            expected_arrival_datelt: Filter results where the expected arrival date is less than this value.
            expected_arrival_datelte: Filter results where the expected arrival date is less than or equal to this value.
            expected_arrival_dateneq: Filter results where the expected arrival date is not equal to this value.
            idsin: Filter results where the ID is in this list (comma-separated).
            limit: Limit the number of results returned.
            page_token: Token for pagination. Use the nextPageToken from the previous response.
            purchase_order_number: Filter results based on the purchase order number.
            purchase_order_numbercontains: Filter results where the purchase order number contains this value.
            purchase_order_numbereq: Filter results where the purchase order number is equal to this value.
            purchase_order_numberin: Filter results where the purchase order number is in this list (comma-separated).
            purchase_order_numberneq: Filter results where the purchase order number is not equal to this value.
            purchase_order_numbernin: Filter results where the purchase order number is not in this list (comma-separated).
            purchase_order_numbernot_contains: Filter results where the purchase order number does not contain this value.
            status: Filter results based on the status.
            statuscontains: Filter results where the status contains this value.
            statuseq: Filter results where the status is equal to this value.
            statusin: Filter results where the status is in this list (comma-separated).
            statusneq: Filter results where the status is not equal to this value.
            statusnin: Filter results where the status is not in this list (comma-separated).
            statusnot_contains: Filter results where the status does not contain this value.
            updated_date: Filter results based on the updated date.
            updated_dateeq: Filter results where the updated date is equal to this value.
            updated_dategt: Filter results where the updated date is greater than this value.
            updated_dategte: Filter results where the updated date is greater than or equal to this value.
            updated_datein: Filter results where the updated date is in this list (comma-separated).
            updated_datelt: Filter results where the updated date is less than this value.
            updated_datelte: Filter results where the updated date is less than or equal to this value.
            updated_dateneq: Filter results where the updated date is not equal to this value.
            updated_datenin: Filter results where the updated date is not in this list (comma-separated).
            warehouse_customer_id: Filter results based on the warehouse customer ID.
            warehouse_customer_idcontains: Filter results where the warehouse customer ID contains this value.
            warehouse_customer_ideq: Filter results where the warehouse customer ID is equal to this value.
            warehouse_customer_idin: Filter results where the warehouse customer ID is in this list (comma-separated).
            warehouse_customer_idneq: Filter results where the warehouse customer ID is not equal to this value.
            warehouse_customer_idnin: Filter results where the warehouse customer ID is not in this list (comma-separated).
            warehouse_customer_idnot_contains: Filter results where the warehouse customer ID does not contain this value.
            warehouse_id: Filter results based on the warehouse ID.
            warehouse_idcontains: Filter results where the warehouse ID contains this value.
            warehouse_ideq: Filter results where the warehouse ID is equal to this value.
            warehouse_idnot_contains: Filter results where the warehouse ID does not contain this value.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_integration_info(
        self,
        integration_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves configuration and status information for all integrations of a specific integration_type. Use this tool when you need an overview of all integrations of a given type for monitoring, analytics, or troubleshooting. Do not use this tool when you need details about a single named integration — use the get integration info tool instead. This is a read-only operation.

        Args:
            integration_type: Type of integration for the Trackstar API.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_inventory_items(
        self,
        active: Optional[str] = None,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        sku: Optional[str] = None,
        skucontains: Optional[str] = None,
        skueq: Optional[str] = None,
        skuin: Optional[str] = None,
        skunin: Optional[str] = None,
        skunot_contains: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
        warehouse_customer_idcontains: Optional[str] = None,
        warehouse_customer_ideq: Optional[str] = None,
        warehouse_customer_idin: Optional[str] = None,
        warehouse_customer_idneq: Optional[str] = None,
        warehouse_customer_idnin: Optional[str] = None,
        warehouse_customer_idnot_contains: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a complete list of all inventory items recorded in the WMS, including current stock levels, locations, and associated product details. Use this tool when you need a full inventory overview for stock management or availability analysis. Do not use this tool to retrieve details of a single inventory item — use the get inventory item tool instead. This is a read-only operation.

        Args:
            active: Filter results by active status.
            created_date: Filter results by created date.
            created_dateeq: Filter results where created date equals the specified value.
            created_dategt: Filter results where created date is greater than the specified value.
            created_dategte: Filter results where created date is greater than or equal to the specified value.
            created_datein: Filter results where created date is within the specified range.
            created_datelt: Filter results where created date is less than the specified value.
            created_datelte: Filter results where created date is less than or equal to the specified value.
            created_dateneq: Filter results where created date does not equal the specified value.
            created_datenin: Filter results where created date is within the specified range.
            idsin: Filter results where ID is in the specified list.
            limit: The maximum number of results to return.
            page_token: Token for pagination.
            sku: Filter results by SKU.
            skucontains: Filter results where SKU contains the specified value.
            skueq: Filter results where SKU equals the specified value.
            skuin: Filter results where SKU is in the specified list.
            skunin: Filter results where SKU is not in the specified list.
            skunot_contains: Filter results where SKU does not contain the specified value.
            updated_date: Filter results by updated date.
            updated_dateeq: Filter results where updated date equals the specified value.
            updated_dategt: Filter results where updated date is greater than the specified value.
            updated_dategte: Filter results where updated date is greater than or equal to the specified value.
            updated_datein: Filter results where updated date is within the specified range.
            updated_datelt: Filter results where updated date is less than the specified value.
            updated_datelte: Filter results where updated date is less than or equal to the specified value.
            updated_dateneq: Filter results where updated date does not equal the specified value.
            updated_datenin: Filter results where updated date is within the specified range.
            warehouse_customer_id: Filter results by warehouse customer ID.
            warehouse_customer_idcontains: Filter results where warehouse customer ID contains the specified value.
            warehouse_customer_ideq: Filter results where warehouse customer ID equals the specified value.
            warehouse_customer_idin: Filter results where warehouse customer ID is in the specified list.
            warehouse_customer_idneq: Filter results where warehouse customer ID does not equal the specified value.
            warehouse_customer_idnin: Filter results where warehouse customer ID is not in the specified list.
            warehouse_customer_idnot_contains: Filter results where warehouse customer ID does not contain the specified value.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_labor_activities(
        self,
        activity_end_time: Optional[str] = None,
        activity_end_timeeq: Optional[str] = None,
        activity_end_timegt: Optional[str] = None,
        activity_end_timegte: Optional[str] = None,
        activity_end_timein: Optional[str] = None,
        activity_end_timelt: Optional[str] = None,
        activity_end_timelte: Optional[str] = None,
        activity_end_timeneq: Optional[str] = None,
        activity_end_timenin: Optional[str] = None,
        activity_start_time: Optional[str] = None,
        activity_start_timeeq: Optional[str] = None,
        activity_start_timegt: Optional[str] = None,
        activity_start_timegte: Optional[str] = None,
        activity_start_timein: Optional[str] = None,
        activity_start_timelt: Optional[str] = None,
        activity_start_timelte: Optional[str] = None,
        activity_start_timeneq: Optional[str] = None,
        activity_start_timenin: Optional[str] = None,
        activity_type: Optional[str] = None,
        associated_object_id: Optional[str] = None,
        associated_object_type: Optional[str] = None,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
        user_id: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
        warehouse_customer_idcontains: Optional[str] = None,
        warehouse_customer_ideq: Optional[str] = None,
        warehouse_customer_idin: Optional[str] = None,
        warehouse_customer_idneq: Optional[str] = None,
        warehouse_customer_idnin: Optional[str] = None,
        warehouse_customer_idnot_contains: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all labor activity records in the WMS, including activity types, durations, and associated worker information. Use this tool when you need an overview of all labor activities for workforce management or reporting. Do not use this tool to retrieve details of a single labor activity — use the get labor activity tool instead. This is a read-only operation.

        Args:
            activity_end_time: Filter activities by activity end time.
            activity_end_timeeq: Filter activities where the activity end time is equal to this value.
            activity_end_timegt: Filter activities where the activity end time is greater than this value.
            activity_end_timegte: Filter activities where the activity end time is greater than or equal to this value.
            activity_end_timein: Filter activities where the activity end time is in this list (comma-separated).
            activity_end_timelt: Filter activities where the activity end time is less than this value.
            activity_end_timelte: Filter activities where the activity end time is less than or equal to this value.
            activity_end_timeneq: Filter activities where the activity end time is not equal to this value.
            activity_end_timenin: Filter activities where the activity end time is in this list (comma-separated).
            activity_start_time: Filter activities by activity start time.
            activity_start_timeeq: Filter activities where the activity start time is equal to this value.
            activity_start_timegt: Filter activities that started after this time.
            activity_start_timegte: Filter activities that started at or after this time.
            activity_start_timein: Filter activities where the activity start time is in this list (comma-separated).
            activity_start_timelt: Filter activities that started before this time.
            activity_start_timelte: Filter activities that started before or at this time.
            activity_start_timeneq: Filter activities where the activity start time is not equal to this value.
            activity_start_timenin: Filter activities where the activity start time is in this list (comma-separated).
            activity_type: Filter activities by activity type.
            associated_object_id: The ID of the associated object.
            associated_object_type: The type of the associated object.
            created_date: Filter activities by created date.
            created_dateeq: Filter activities created on this date.
            created_dategt: Filter activities created after this date.
            created_dategte: Filter activities created on or after this date.
            created_datein: Filter activities created on these dates (comma-separated).
            created_datelt: Filter activities created before this date.
            created_datelte: Filter activities created before or at this date.
            created_dateneq: Filter activities where the created date is not equal to this value.
            created_datenin: Filter activities where the created date is not in this list (comma-separated).
            idsin: Filter activities where the ID is in this list (comma-separated).
            limit: The maximum number of activities to return.
            page_token: Token for pagination.
            updated_date: Filter activities by updated date.
            updated_dateeq: Filter activities updated on this date.
            updated_dategt: Filter activities updated after this date.
            updated_dategte: Filter activities updated on or after this date.
            updated_datein: Filter activities where the updated date is in this list (comma-separated).
            updated_datelt: Filter activities updated before this date.
            updated_datelte: Filter activities updated before or at this date.
            updated_dateneq: Filter activities where the updated date is not equal to this value.
            updated_datenin: Filter activities where the updated date is not in this list (comma-separated).
            user_id: Filter activities by user ID.
            warehouse_customer_id: Filter activities by warehouse customer ID.
            warehouse_customer_idcontains: Filter activities where the warehouse customer ID contains this value.
            warehouse_customer_ideq: Filter activities where the warehouse customer ID is equal to this value.
            warehouse_customer_idin: Filter activities where the warehouse customer ID is in this list (comma-separated).
            warehouse_customer_idneq: Filter activities where the warehouse customer ID is not equal to this value.
            warehouse_customer_idnin: Filter activities where the warehouse customer ID is not in this list (comma-separated).
            warehouse_customer_idnot_contains: Filter activities where the warehouse customer ID does not contain this value.
            warehouse_id: Filter activities by warehouse ID.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_order_channels(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
        warehouse_customer_idcontains: Optional[str] = None,
        warehouse_customer_ideq: Optional[str] = None,
        warehouse_customer_idin: Optional[str] = None,
        warehouse_customer_idneq: Optional[str] = None,
        warehouse_customer_idnin: Optional[str] = None,
        warehouse_customer_idnot_contains: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all order channels configured in the WMS, such as e-commerce platforms or marketplaces through which orders are received. Use this tool when you need to review available sales channels or analyze order volume by channel. Do not use this tool to retrieve individual orders — use the list orders or get order tools instead. This is a read-only operation.

        Args:
            created_date: Filter records by created date.
            created_dateeq: Filter records where the created date is equal to the specified value.
            created_dategt: Filter records where the created date is greater than the specified value.
            created_dategte: Filter records where the created date is greater than or equal to the specified value.
            created_datein: Filter records where the created date is within the specified range.
            created_datelt: Filter records where the created date is less than the specified value.
            created_datelte: Filter records where the created date is less than or equal to the specified value.
            created_dateneq: Filter records where the created date is not equal to the specified value.
            created_datenin: Filter records where the created date is within the specified range.
            idsin: Filter records where the ID is in the specified list.
            limit: The maximum number of records to return.
            page_token: Pagination token for fetching subsequent pages of results.
            updated_date: Filter records by updated date.
            updated_dateeq: Filter records where the updated date is equal to the specified value.
            updated_dategt: Filter records where the updated date is greater than the specified value.
            updated_dategte: Filter records where the updated date is greater than or equal to the specified value.
            updated_datein: Filter records where the updated date is within the specified range.
            updated_datelt: Filter records where the updated date is less than the specified value.
            updated_datelte: Filter records where the updated date is less than or equal to the specified value.
            updated_dateneq: Filter records where the updated date is not equal to the specified value.
            updated_datenin: Filter records where the updated date is not in the specified list.
            warehouse_customer_id: Filter records by warehouse customer ID.
            warehouse_customer_idcontains: Filter records where the warehouse customer ID contains the specified value.
            warehouse_customer_ideq: Filter records where the warehouse customer ID is equal to the specified value.
            warehouse_customer_idin: Filter records where the warehouse customer ID is in the specified list.
            warehouse_customer_idneq: Filter records where the warehouse customer ID is not equal to the specified value.
            warehouse_customer_idnin: Filter records where the warehouse customer ID is not in the specified list.
            warehouse_customer_idnot_contains: Filter records where the warehouse customer ID does not contain the specified value.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_order_packs(
        self,
        order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of packs associated with a specific order identified by order_id, including pack dimensions, contents, and status. Use this tool when you need to review packing details for a particular order during fulfillment or shipping review. Do not use this tool to retrieve general order details — use the get order tool instead. This is a read-only operation.

        Args:
            order_id: ID of the order.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_orders(
        self,
        channel: Optional[str] = None,
        channelcontains: Optional[str] = None,
        channeleq: Optional[str] = None,
        channelin: Optional[str] = None,
        channelneq: Optional[str] = None,
        channelnin: Optional[str] = None,
        channelnot_contains: Optional[str] = None,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        order_number: Optional[str] = None,
        order_numbercontains: Optional[str] = None,
        order_numbereq: Optional[str] = None,
        order_numberin: Optional[str] = None,
        order_numbernin: Optional[str] = None,
        order_numbernot_contains: Optional[str] = None,
        page_token: Optional[str] = None,
        reference_id: Optional[str] = None,
        reference_idcontains: Optional[str] = None,
        reference_ideq: Optional[str] = None,
        reference_idin: Optional[str] = None,
        reference_idnin: Optional[str] = None,
        reference_idnot_contains: Optional[str] = None,
        required_ship_date: Optional[str] = None,
        required_ship_dateeq: Optional[str] = None,
        required_ship_dategt: Optional[str] = None,
        required_ship_dategte: Optional[str] = None,
        required_ship_datelt: Optional[str] = None,
        required_ship_datelte: Optional[str] = None,
        required_ship_dateneq: Optional[str] = None,
        status: Optional[str] = None,
        statuscontains: Optional[str] = None,
        statuseq: Optional[str] = None,
        statusin: Optional[str] = None,
        statusneq: Optional[str] = None,
        statusnin: Optional[str] = None,
        statusnot_contains: Optional[str] = None,
        type: Optional[str] = None,
        typecontains: Optional[str] = None,
        typeeq: Optional[str] = None,
        typein: Optional[str] = None,
        typeneq: Optional[str] = None,
        typenin: Optional[str] = None,
        typenot_contains: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
        warehouse_customer_idcontains: Optional[str] = None,
        warehouse_customer_ideq: Optional[str] = None,
        warehouse_customer_idin: Optional[str] = None,
        warehouse_customer_idneq: Optional[str] = None,
        warehouse_customer_idnin: Optional[str] = None,
        warehouse_customer_idnot_contains: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all orders recorded in the WMS, including their statuses, line items, and associated customer and shipping details. Use this tool when you need an overview of all orders for management or reporting purposes. Do not use this tool to retrieve details of a single order — use the get order tool instead. This is a read-only operation.

        Args:
            channel: Channel.
            channelcontains: Channel contains this value.
            channeleq: Channel equal to this value.
            channelin: Channel in this list (comma-separated).
            channelneq: Channel not equal to this value.
            channelnin: Channel not in this list (comma-separated).
            channelnot_contains: Channel does not contain this value.
            created_date: Created date.
            created_dateeq: Created date equal to this value.
            created_dategt: Created date greater than this value.
            created_dategte: Created date greater than or equal to this value.
            created_datein: Created date in this list (comma-separated).
            created_datelt: Created date less than this value.
            created_datelte: Created date less than or equal to this value.
            created_dateneq: Created date not equal to this value.
            created_datenin: Created date in this list (comma-separated).
            idsin: IDs in this list (comma-separated).
            limit: Limit the number of results.
            order_number: Order number.
            order_numbercontains: Order number contains this value.
            order_numbereq: Order number equal to this value.
            order_numberin: Order number in this list (comma-separated).
            order_numbernin: Order number not in this list (comma-separated).
            order_numbernot_contains: Order number does not contain this value.
            page_token: Page token for pagination.
            reference_id: Reference ID.
            reference_idcontains: Reference ID contains this value.
            reference_ideq: Reference ID equal to this value.
            reference_idin: Reference ID in this list (comma-separated).
            reference_idnin: Reference ID not in this list (comma-separated).
            reference_idnot_contains: Reference ID does not contain this value.
            required_ship_date: Required ship date.
            required_ship_dateeq: Required ship date equal to this value.
            required_ship_dategt: Required ship date greater than this value.
            required_ship_dategte: Required ship date greater than or equal to this value.
            required_ship_datelt: Required ship date less than this value.
            required_ship_datelte: Required ship date less than or equal to this value.
            required_ship_dateneq: Required ship date not equal to this value.
            status: Status.
            statuscontains: Status contains this value.
            statuseq: Status equal to this value.
            statusin: Status in this list (comma-separated).
            statusneq: Status not equal to this value.
            statusnin: Status not in this list (comma-separated).
            statusnot_contains: Status does not contain this value.
            type: Type.
            typecontains: Type contains this value.
            typeeq: Type equal to this value.
            typein: Type in this list (comma-separated).
            typeneq: Type equal to this value.
            typenin: Type in this list (comma-separated).
            typenot_contains: Type does not contain this value.
            updated_date: Updated date.
            updated_dateeq: Updated date equal to this value.
            updated_dategt: Updated date greater than this value.
            updated_dategte: Updated date greater than or equal to this value.
            updated_datein: Updated date in this list (comma-separated).
            updated_datelt: Updated date less than this value.
            updated_datelte: Updated date less than or equal to this value.
            updated_dateneq: Updated date not equal to this value.
            updated_datenin: Updated date in this list (comma-separated).
            warehouse_customer_id: Warehouse customer ID.
            warehouse_customer_idcontains: Warehouse customer ID contains this value.
            warehouse_customer_ideq: Warehouse customer ID equal to this value.
            warehouse_customer_idin: Warehouse customer ID in this list (comma-separated).
            warehouse_customer_idneq: Warehouse customer ID not equal to this value.
            warehouse_customer_idnin: Warehouse customer ID not in this list (comma-separated).
            warehouse_customer_idnot_contains: Warehouse customer ID does not contain this value.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_products(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        sku: Optional[str] = None,
        skucontains: Optional[str] = None,
        skueq: Optional[str] = None,
        skuin: Optional[str] = None,
        skunin: Optional[str] = None,
        skunot_contains: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
        warehouse_customer_idcontains: Optional[str] = None,
        warehouse_customer_ideq: Optional[str] = None,
        warehouse_customer_idin: Optional[str] = None,
        warehouse_customer_idneq: Optional[str] = None,
        warehouse_customer_idnin: Optional[str] = None,
        warehouse_customer_idnot_contains: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a complete list of all products in the WMS inventory, including their names, SKUs, prices, and descriptions. Use this tool when you need a catalog-level overview of all products. Do not use this tool to retrieve details of a single product — use the get product tool instead. This is a read-only operation.

        Args:
            created_date: Creation date filter.
            created_dateeq: Specific creation date to filter results.
            created_dategt: Created date filter: results after this date.
            created_dategte: Created date filter: results on or after this date.
            created_datein: List of creation dates to include in the results.
            created_datelt: Created date filter: results before this date.
            created_datelte: Created date filter: results on or before this date.
            created_dateneq: Created date to exclude from the results.
            created_datenin: List of creation dates to include in the results.
            idsin: List of IDs to include in the results.
            limit: Maximum number of results to return.
            page_token: Token for pagination.
            sku: SKU to filter results.
            skucontains: SKU that should be contained in the results.
            skueq: Specific SKU to filter results.
            skuin: List of SKUs to include in the results.
            skunin: List of SKUs to exclude from the results.
            skunot_contains: SKU that should not be contained in the results.
            updated_date: Updated date filter.
            updated_dateeq: Specific updated date to filter results.
            updated_dategt: Updated date filter: results after this date.
            updated_dategte: Updated date filter: results on or after this date.
            updated_datein: List of updated dates to include in the results.
            updated_datelt: Updated date filter: results before this date.
            updated_datelte: Updated date filter: results on or before this date.
            updated_dateneq: Updated date to exclude from the results.
            updated_datenin: List of updated dates to include in the results.
            warehouse_customer_id: Warehouse Customer ID to filter results.
            warehouse_customer_idcontains: Warehouse Customer ID that should be contained in the results.
            warehouse_customer_ideq: Specific Warehouse Customer ID to filter results.
            warehouse_customer_idin: List of Warehouse Customer IDs to include in the results.
            warehouse_customer_idneq: Warehouse Customer ID to exclude from the results.
            warehouse_customer_idnin: List of Warehouse Customer IDs to exclude from the results.
            warehouse_customer_idnot_contains: Warehouse Customer ID that should not be contained in the results.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_returns(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        status: Optional[str] = None,
        statuscontains: Optional[str] = None,
        statuseq: Optional[str] = None,
        statusin: Optional[str] = None,
        statusneq: Optional[str] = None,
        statusnin: Optional[str] = None,
        statusnot_contains: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
        warehouse_customer_idcontains: Optional[str] = None,
        warehouse_customer_ideq: Optional[str] = None,
        warehouse_customer_idin: Optional[str] = None,
        warehouse_customer_idneq: Optional[str] = None,
        warehouse_customer_idnin: Optional[str] = None,
        warehouse_customer_idnot_contains: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all return records processed in the WMS, including return statuses, line items, and associated order references. Use this tool when you need an overview of all customer returns for tracking or analysis. Do not use this tool to retrieve details of a single return — use the get return tool instead. This is a read-only operation.

        Args:
            created_date: Filter records based on the created date.
            created_dateeq: Filter records where the created date is equal to the specified value.
            created_dategt: Filter records where the created date is greater than the specified value.
            created_dategte: Filter records where the created date is greater than or equal to the specified value.
            created_datein: Filter records where the created date is within the specified range.
            created_datelt: Filter records where the created date is less than the specified value.
            created_datelte: Filter records where the created date is less than or equal to the specified value.
            created_dateneq: Filter records where the created date is not equal to the specified value.
            created_datenin: Filter records where the created date is within the specified range.
            idsin: Filter records where the ID is in the specified list.
            limit: Specifies the maximum number of records to return.
            page_token: Token for pagination. Use the nextPageToken from previous response to get next page of results.
            status: Filter records based on the status.
            statuscontains: Filter records where the status contains the specified value.
            statuseq: Filter records where the status is equal to the specified value.
            statusin: Filter records where the status is in the specified list.
            statusneq: Filter records where the status is not equal to the specified value.
            statusnin: Filter records where the status is not in the specified list.
            statusnot_contains: Filter records where the status does not contain the specified value.
            updated_date: Filter records based on the updated date.
            updated_dateeq: Filter records where the updated date is equal to the specified value.
            updated_dategt: Filter records where the updated date is greater than the specified value.
            updated_dategte: Filter records where the updated date is greater than or equal to the specified value.
            updated_datein: Filter records where the updated date is within the specified range.
            updated_datelt: Filter records where the updated date is less than the specified value.
            updated_datelte: Filter records where the updated date is less than or equal to the specified value.
            updated_dateneq: Filter records where the updated date is not equal to the specified value.
            updated_datenin: Filter records where the updated date is not in the specified list.
            warehouse_customer_id: Filter records based on the warehouse customer ID.
            warehouse_customer_idcontains: Filter records where the warehouse customer ID contains the specified value.
            warehouse_customer_ideq: Filter records where the warehouse customer ID is equal to the specified value.
            warehouse_customer_idin: Filter records where the warehouse customer ID is in the specified list.
            warehouse_customer_idneq: Filter records where the warehouse customer ID is not equal to the specified value.
            warehouse_customer_idnin: Filter records where the warehouse customer ID is not in the specified list.
            warehouse_customer_idnot_contains: Filter records where the warehouse customer ID does not contain the specified value.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_shipments(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all freight shipments recorded in the system, including their statuses, tracking details, and associated order references. Use this tool when you need an overview of all outbound shipments for shipping and logistics management. Do not use this tool to retrieve details of a single shipment — use the get shipment tool instead. This is a read-only operation.

        Args:
            created_date: Filter results by created date.
            created_dateeq: Filter results where the created date equals the specified value.
            created_dategt: Filter results where the created date is greater than the specified value.
            created_dategte: Filter results where the created date is greater than or equal to the specified value.
            created_datein: Filter results where the created date is within the specified range.
            created_datelt: Filter results where the created date is less than the specified value.
            created_datelte: Filter results where the created date is less than or equal to the specified value.
            created_dateneq: Filter results where the created date is not equal to the specified value.
            created_datenin: Filter results where the created date is not within the specified range.
            idsin: Filter results where the ID is within the specified comma-separated list.
            limit: Maximum number of results to return.
            page_token: Token for pagination; use the nextPageToken from the previous response.
            updated_date: Filter results by updated date.
            updated_dateeq: Filter results where the updated date equals the specified value.
            updated_dategt: Filter results where the updated date is greater than the specified value.
            updated_dategte: Filter results where the updated date is greater than or equal to the specified value.
            updated_datein: Filter results where the updated date is within the specified range.
            updated_datelt: Filter results where the updated date is less than the specified value.
            updated_datelte: Filter results where the updated date is less than or equal to the specified value.
            updated_dateneq: Filter results where the updated date is not equal to the specified value.
            updated_datenin: Filter results where the updated date is not within the specified range.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_shipping_methods(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all shipping methods available in the WMS, including carrier names, delivery timeframes, and cost configurations. Use this tool when you need to review all delivery options before assigning a shipping method to an order. Do not use this tool to retrieve details of a single shipping method — use the get shipping method tool instead. This is a read-only operation.

        Args:
            created_date: Filter records based on the created date.
            created_dateeq: Filter records where the created date equals the specified value.
            created_dategt: Filter records where the created date is greater than the specified value.
            created_dategte: Filter records where the created date is greater than or equal to the specified value.
            created_datein: Filter records where the created date is within the specified range.
            created_datelt: Filter records where the created date is less than the specified value.
            created_datelte: Filter records where the created date is less than or equal to the specified value.
            created_dateneq: Filter records where the created date is not equal to the specified value.
            created_datenin: Filter records where the created date is within the specified range.
            idsin: Filter records where the ID is in the specified list.
            limit: Number of records to return per page.
            page_token: Token for pagination.
            updated_date: Filter records based on the updated date.
            updated_dateeq: Filter records where the updated date equals the specified value.
            updated_dategt: Filter records where the updated date is greater than the specified value.
            updated_dategte: Filter records where the updated date is greater than or equal to the specified value.
            updated_datein: Filter records where the updated date is within the specified range.
            updated_datelt: Filter records where the updated date is less than the specified value.
            updated_datelte: Filter records where the updated date is less than or equal to the specified value.
            updated_dateneq: Filter records where the updated date is not equal to the specified value.
            updated_datenin: Filter records where the updated date is not within the specified range.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_warehouse_customers(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all warehouse customers configured in the WMS, including their profiles and associated warehouse assignments. Use this tool when you need an overview of all customers managed within the warehouse system. Do not use this tool to retrieve details of a single warehouse customer — use the get warehouse customer tool instead. This is a read-only operation.

        Args:
            created_date: Filter records by created date.
            created_dateeq: Filter records where the created date equals the specified value.
            created_dategt: Filter records where the created date is greater than the specified value.
            created_dategte: Filter records where the created date is greater than or equal to the specified value.
            created_datein: Filter records where the created date is within the specified range.
            created_datelt: Filter records where the created date is less than the specified value.
            created_datelte: Filter records where the created date is less than or equal to the specified value.
            created_dateneq: Filter records where the created date is not equal to the specified value.
            created_datenin: Filter records where the created date is not within the specified range.
            idsin: Filter records where the ID is in the specified list.
            limit: Number of records to return per page.
            page_token: Token for pagination.
            updated_date: Filter records by updated date.
            updated_dateeq: Filter records where the updated date equals the specified value.
            updated_dategt: Filter records where the updated date is greater than the specified value.
            updated_dategte: Filter records where the updated date is greater than or equal to the specified value.
            updated_datein: Filter records where the updated date is within the specified range.
            updated_datelt: Filter records where the updated date is less than the specified value.
            updated_datelte: Filter records where the updated date is less than or equal to the specified value.
            updated_dateneq: Filter records where the updated date is not equal to the specified value.
            updated_datenin: Filter records where the updated date is not within the specified range.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_warehouse_locations(
        self,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        page_token: Optional[str] = None,
        type: Optional[str] = None,
        typecontains: Optional[str] = None,
        typeeq: Optional[str] = None,
        typein: Optional[str] = None,
        typeneq: Optional[str] = None,
        typenin: Optional[str] = None,
        typenot_contains: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all locations within a specific warehouse identified by warehouse_id, including zone, aisle, and bin information. Use this tool when you need to review all storage locations in a warehouse for inventory placement or space management. Do not use this tool to retrieve details of a single location — use the get warehouse location tool instead. This is a read-only operation.

        Args:
            created_date: 
            created_dateeq: 
            created_dategt: 
            created_dategte: 
            created_datein: 
            created_datelt: 
            created_datelte: 
            created_dateneq: 
            created_datenin: 
            idsin: 
            limit: 
            page_token: 
            type: 
            typecontains: 
            typeeq: 
            typein: 
            typeneq: 
            typenin: 
            typenot_contains: 
            updated_date: 
            updated_dateeq: 
            updated_dategt: 
            updated_dategte: 
            updated_datein: 
            updated_datelt: 
            updated_datelte: 
            updated_dateneq: 
            updated_datenin: 
            warehouse_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_list_warehouses(
        self,
        code: Optional[str] = None,
        code_contains: Optional[str] = None,
        codeeq: Optional[str] = None,
        codein: Optional[str] = None,
        codenin: Optional[str] = None,
        codenot_contains: Optional[str] = None,
        created_date: Optional[str] = None,
        created_dateeq: Optional[str] = None,
        created_dategt: Optional[str] = None,
        created_dategte: Optional[str] = None,
        created_datein: Optional[str] = None,
        created_datelt: Optional[str] = None,
        created_datelte: Optional[str] = None,
        created_dateneq: Optional[str] = None,
        created_datenin: Optional[str] = None,
        idsin: Optional[str] = None,
        limit: Optional[str] = None,
        name: Optional[str] = None,
        namecontains: Optional[str] = None,
        nameeq: Optional[str] = None,
        namein: Optional[str] = None,
        namenin: Optional[str] = None,
        namenot_contains: Optional[str] = None,
        page_token: Optional[str] = None,
        updated_date: Optional[str] = None,
        updated_dateeq: Optional[str] = None,
        updated_dategt: Optional[str] = None,
        updated_dategte: Optional[str] = None,
        updated_datein: Optional[str] = None,
        updated_datelt: Optional[str] = None,
        updated_datelte: Optional[str] = None,
        updated_dateneq: Optional[str] = None,
        updated_datenin: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all warehouses configured in the WMS, including their names, addresses, and operational details. Use this tool when you need an overview of all available warehouses for logistics or inventory planning. Do not use this tool to retrieve details of a single warehouse — use the get warehouse tool instead. This is a read-only operation.

        Args:
            code: 
            code_contains: 
            codeeq: 
            codein: 
            codenin: 
            codenot_contains: 
            created_date: Filter results by created date.
            created_dateeq: Filter results where the created date equals the specified value.
            created_dategt: Filter results where the created date is greater than the specified value.
            created_dategte: Filter results where the created date is greater than or equal to the specified value.
            created_datein: Filter results where the created date is in the specified range.
            created_datelt: Filter results where the created date is less than the specified value.
            created_datelte: Filter results where the created date is less than or equal to the specified value.
            created_dateneq: Filter results where the created date is not equal to the specified value.
            created_datenin: Filter results where the created date is not in the specified range.
            idsin: Filter results where the ID is in the specified list.
            limit: Maximum number of results to return.
            name: 
            namecontains: 
            nameeq: 
            namein: 
            namenin: 
            namenot_contains: 
            page_token: Token for pagination. Use the nextPageToken from the previous response.
            updated_date: Filter results by updated date.
            updated_dateeq: Filter results where the updated date equals the specified value.
            updated_dategt: Filter results where the updated date is greater than the specified value.
            updated_dategte: Filter results where the updated date is greater than or equal to the specified value.
            updated_datein: Filter results where the updated date is in the specified range.
            updated_datelt: Filter results where the updated date is less than the specified value.
            updated_datelte: Filter results where the updated date is less than or equal to the specified value.
            updated_dateneq: Filter results where the updated date is not equal to the specified value.
            updated_datenin: Filter results where the updated date is not in the specified range.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_receive_inbound_shipment(
        self,
        inbound_shipment_id: Optional[str] = None,
        line_items: Optional[List[Any]] = None,
        warehouse_id: Optional[str] = None,
        warehouse_location_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Marks a specific inbound shipment identified by inbound_shipment_id as received in the WMS, updating inventory levels to reflect the newly arrived stock. Use this tool when physical goods from an inbound shipment have arrived and need to be recorded in inventory. Do not use this tool to update shipment metadata — use the update inbound shipment tool instead. This operation modifies inventory levels and updates the shipment status, which may be irreversible.

        Args:
            inbound_shipment_id: The ID of the inbound shipment.
            line_items: 
            warehouse_id: The ID of the warehouse.
            warehouse_location_id: The ID of the warehouse location.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_sandbox_simulate_fulfill(
        self,
        order_id: Optional[str] = None,
        partial: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Simulates the fulfillment of a specific order identified by order_id within the Trackstar sandbox environment, triggering fulfillment state changes without affecting live production data. Use this tool during development and testing to validate fulfillment workflows. Do not use this tool in production environments — it is intended exclusively for sandbox use. This operation alters the sandbox order state and cannot be applied to live orders.

        Args:
            order_id: Order ID for the Trackstar API request.
            partial: Partial data for the Trackstar API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_ship_order(
        self,
        carrier: Optional[str] = None,
        measurements: Optional[_TrackstarShipOrderMeasurements] = None,
        order_id: Optional[str] = None,
        packages: Optional[List[Any]] = None,
        shipped_date: Optional[str] = None,
        shipping_cost: Optional[str] = None,
        shipping_method: Optional[str] = None,
        tracking_number: Optional[str] = None,
        tracking_url: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a shipment record for a specific order identified by order_id, initiating the physical delivery of order items to the customer. Use this tool when an order is ready to be dispatched and a shipment needs to be logged in the WMS. Do not use this tool to update general order details — use the update order tool instead. This operation creates a new shipment and may trigger downstream fulfillment workflows.

        Args:
            carrier: The shipping carrier (e.g., FedEx, UPS).
            measurements: Dimensions and weight of the package.
            order_id: ID of the associated order.
            packages: 
            shipped_date: The date the shipment was shipped.
            shipping_cost: The cost of shipping.
            shipping_method: The shipping method used (e.g., Ground, Express).
            tracking_number: The tracking number for the shipment.
            tracking_url: URL to track the shipment online.
            warehouse_id: ID of the warehouse the shipment originated from.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_sync_connection(
        self,
        functions_to_sync: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Triggers a synchronization of a specific integration connection to ensure data between Trackstar and the connected system is consistent and up to date. Use this tool when integration data appears stale or out of sync. Do not use this tool to create or delete connections — use the create or delete connection tools instead. This operation initiates a sync process which may take time to complete depending on data volume.

        Args:
            functions_to_sync: An array of function names to synchronize.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_update_inbound_shipment(
        self,
        expected_arrival_date: Optional[str] = None,
        inbound_shipment_id: Optional[str] = None,
        line_items: Optional[List[Any]] = None,
        purchase_order_number: Optional[str] = None,
        supplier: Optional[str] = None,
        supplier_object: Optional[_TrackstarUpdateInboundShipmentSupplierObject] = None,
        tracking_number: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing inbound shipment record identified by inbound_shipment_id in the WMS. Use this tool when you need to modify inbound shipment attributes such as expected quantities, supplier details, or scheduled dates. Do not use this tool to update Trackstar tags on an inbound shipment — use the update inbound shipment Trackstar tags tool instead, and do not use this tool to mark a shipment as received — use the receive inbound shipment tool instead. This operation modifies the inbound shipment record in place.

        Args:
            expected_arrival_date: The expected arrival date of the shipment.
            inbound_shipment_id: The ID of the inbound shipment.
            line_items: 
            purchase_order_number: The purchase order number associated with the shipment.
            supplier: The name of the supplier.
            supplier_object: Supplier object details.
            tracking_number: The tracking number for the shipment.
            warehouse_id: The ID of the warehouse where the shipment is expected to arrive.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_update_inbound_shipment_trackstar_tags(
        self,
        body: Dict[str, Any],
        inbound_shipment_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates Trackstar metadata tags on a specific inbound shipment record identified by inbound_shipment_id. Use this tool when you need to add, replace, or remove Trackstar classification tags on an inbound shipment to improve tracking, filtering, or reporting. Do not use this tool to update other inbound shipment attributes — use the update inbound shipment tool instead. This operation overwrites existing Trackstar tag values on the inbound shipment.

        Args:
            body: Body parameters for the Trackstar API request. (required)
            inbound_shipment_id: The ID of the inbound shipment.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_update_inventory_trackstar_tags(
        self,
        body: Optional[Dict[str, Any]] = None,
        inventory_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates Trackstar metadata tags on a specific inventory record identified by inventory_id. Use this tool when you need to add, replace, or remove Trackstar classification tags on an inventory item to improve tracking analytics and reporting. Do not use this tool to update inventory quantities or other attributes — use the adjust inventory item tool instead. This operation overwrites existing Trackstar tag values on the inventory record.

        Args:
            body: Request body for the Trackstar API.
            inventory_id: ID of the inventory item.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_update_kit_product(
        self,
        gtin: Optional[str] = None,
        inventory_items: Optional[List[Any]] = None,
        kit_id: Optional[str] = None,
        measurements: Optional[_TrackstarUpdateKitProductMeasurements] = None,
        name: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration or attributes of an existing kit product identified by kit_id in the WMS. Use this tool when you need to modify kit properties such as component items, quantities, or descriptions. Do not use this tool to create a new kit — use the create kit product tool instead. This operation modifies the kit product record in place.

        Args:
            gtin: Global Trade Item Number (GTIN) of the product.
            inventory_items: 
            kit_id: ID of the kit.
            measurements: Product measurements.
            name: Name of the product.
            sku: Stock Keeping Unit (SKU) of the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_update_order(
        self,
        channel: Optional[str] = None,
        channel_object: Optional[_TrackstarUpdateOrderChannelObject] = None,
        invoice_currency_code: Optional[str] = None,
        line_items: Optional[List[Any]] = None,
        order_id: Optional[str] = None,
        order_number: Optional[str] = None,
        reference_id: Optional[str] = None,
        ship_to_address: Optional[_TrackstarUpdateOrderShipToAddress] = None,
        shipping_method: Optional[str] = None,
        status: Optional[str] = None,
        total_discount: Optional[str] = None,
        total_price: Optional[str] = None,
        total_shipping: Optional[str] = None,
        total_tax: Optional[str] = None,
        trading_partner: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing order record identified by order_id in the WMS. Use this tool when you need to modify order attributes such as line items, shipping address, or processing status. Do not use this tool to update Trackstar tags on an order — use the update order Trackstar tags tool instead, and do not use this tool to cancel or ship an order — use the cancel order or ship order tools respectively. This operation modifies the order record in place.

        Args:
            channel: The sales channel for the order.
            channel_object: Details about the sales channel.
            invoice_currency_code: The currency code for the invoice.
            line_items: 
            order_id: The ID of the order.
            order_number: The order number.
            reference_id: A reference ID for the order.
            ship_to_address: The shipping address for the order.
            shipping_method: The shipping method used for the order.
            status: The current status of the order.
            total_discount: The total discount applied to the order.
            total_price: The total price of the order.
            total_shipping: The total shipping cost for the order.
            total_tax: The total tax amount for the order.
            trading_partner: The trading partner associated with the order.
            warehouse_customer_id: The ID of the warehouse customer.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_update_order_trackstar_tags(
        self,
        body: Optional[Dict[str, Any]] = None,
        order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates Trackstar metadata tags on a specific order record identified by order_id. Use this tool when you need to add, replace, or remove Trackstar classification tags on an order to improve tracking, filtering, or reporting. Do not use this tool to update other order attributes such as line items or shipping details — use the update order tool instead. This operation overwrites existing Trackstar tag values on the order.

        Args:
            body: Body parameters for the Trackstar API request.
            order_id: The ID of the order.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_update_product(
        self,
        gtin: Optional[str] = None,
        measurements: Optional[_TrackstarUpdateProductMeasurements] = None,
        name: Optional[str] = None,
        product_id: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing product record identified by product_id in the WMS inventory. Use this tool when you need to modify product attributes such as name, price, description, or SKU. Do not use this tool to update Trackstar tags on a product — use the update product Trackstar tags tool instead. This operation modifies the product record in place.

        Args:
            gtin: 
            measurements: 
            name: 
            product_id: 
            sku: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_update_product_trackstar_tags(
        self,
        body: Optional[Dict[str, Any]] = None,
        product_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates Trackstar metadata tags on a specific product record identified by product_id. Use this tool when you need to add, replace, or remove Trackstar classification tags on a product to improve tracking, categorization, or reporting. Do not use this tool to update other product attributes such as name, price, or SKU — use the update product tool instead. This operation overwrites existing Trackstar tag values on the product.

        Args:
            body: Request body for the Trackstar API.
            product_id: ID of the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_update_return(
        self,
        line_items: Optional[List[Any]] = None,
        order_id: Optional[str] = None,
        return_id: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing return record identified by return_id in the WMS. Use this tool when you need to modify return attributes such as status, line items, or associated notes. Do not use this tool to update Trackstar tags on a return — use the update return Trackstar tags tool instead. This operation modifies the return record in place.

        Args:
            line_items: 
            order_id: ID of the order.
            return_id: Return ID.
            warehouse_id: ID of the warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_update_return_trackstar_tags(
        self,
        body: Dict[str, Any],
        return_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates Trackstar metadata tags on a specific return record identified by return_id. Use this tool when you need to add, replace, or remove Trackstar classification tags on a return to improve tracking, filtering, or reporting. Do not use this tool to update other return attributes such as status or line items — use the update return tool instead. This operation overwrites existing Trackstar tag values on the return.

        Args:
            body: Request body for the Trackstar API. (required)
            return_id: ID to be returned by the Trackstar API.
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_update_sale_fulfillment_shipment(
        self,
        Lines: Optional[List[Any]] = None,
        RequireBy: Optional[str] = None,
        ShippingAddress: Optional[_TrackstarUpdateSaleFulfillmentShipmentShippingaddress] = None,
        ShippingNotes: Optional[str] = None,
        Status: Optional[str] = None,
        TaskID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the shipment details for a sale fulfillment record in the DEAR Inventory external API, such as tracking numbers, carrier information, or shipment status. Use this tool when you need to modify shipping information associated with a sale fulfillment in DEAR Inventory. Do not use this tool to update WMS order shipments — use the ship order or update order tools instead. This operation modifies the sale fulfillment shipment record in place.

        Args:
            Lines: 
            RequireBy: 
            ShippingAddress: 
            ShippingNotes: 
            Status: 
            TaskID: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trackstar_update_warehouse_trackstar_tags(
        self,
        body: Dict[str, Any],
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates Trackstar metadata tags on a specific warehouse record identified by warehouse_id. Use this tool when you need to add, replace, or remove Trackstar classification tags on a warehouse to improve tracking, filtering, or reporting. Do not use this tool to update other warehouse attributes such as name, address, or capacity — use the update warehouse tool instead. This operation overwrites existing Trackstar tag values on the warehouse.

        Args:
            body: Request body for the Trackstar API. (required)
            warehouse_id: ID of the warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

