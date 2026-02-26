"""Fastn Trackstar connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TrackstarConnector:
    """Trackstar connector ().

    Provides 76 tools.
    """

    def adjust_inventory_for_product(
        self,
        adjustment_type: Optional[str] = None,
        quantity: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adjusts the inventory levels for a specified product, allowing for accurate stock tracking and management.

        Args:
            adjustment_type: 
            quantity: 
            warehouse_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def adjust_inventory_item(
        self,
        adjustment_type: Optional[str] = None,
        location_id: Optional[str] = None,
        quantity: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Modifies details of an existing inventory item, enabling updates to attributes such as quantity or description.

        Args:
            adjustment_type: The type of inventory adjustment.
            location_id: The ID of the inventory location.
            quantity: The quantity of the inventory item.
            warehouse_id: The ID of the warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def cancel_order(
        self,
        order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Cancels an existing order, removing it from the order processing workflow.

        Args:
            order_id: ID of the order.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_a_kit_product(
        self,
        gtin: Optional[str] = None,
        inventory_items: Optional[List[Any]] = None,
        measurements: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new kit product that bundles multiple items together for sale, streamlining inventory management and sales efforts.

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

    def create_cart_order_shipment(
        self,
        carrier: Optional[str] = None,
        shipping_method: Optional[str] = None,
        tracking_number: Optional[str] = None,
        tracking_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Initiates the shipment process for a cart order, preparing items for delivery to the customer.

        Args:
            carrier: The shipping carrier (e.g., FedEx, UPS).
            shipping_method: The shipping method used (e.g., Ground, Express).
            tracking_number: The tracking number for the shipment.
            tracking_url: URL to track the shipment online.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_inbound_shipment(
        self,
        expected_arrival_date: Optional[str] = None,
        line_items: Optional[List[Any]] = None,
        purchase_order_number: Optional[str] = None,
        supplier: Optional[str] = None,
        supplier_object: Optional[Dict[str, Any]] = None,
        tracking_number: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new inbound shipment in the system, tracking incoming inventory from suppliers.

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

    def create_link_token(
        self,
        connection_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a unique link token for payment processing or authentication purposes in the system.

        Args:
            connection_id: ID of the connection.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_order(
        self,
        channel: Optional[str] = None,
        channel_object: Optional[Dict[str, Any]] = None,
        invoice_currency_code: Optional[str] = None,
        line_items: Optional[List[Any]] = None,
        order_number: Optional[str] = None,
        reference_id: Optional[str] = None,
        ship_to_address: Optional[Dict[str, Any]] = None,
        shipping_method: Optional[str] = None,
        total_discount: Optional[str] = None,
        total_price: Optional[str] = None,
        total_shipping: Optional[str] = None,
        total_tax: Optional[str] = None,
        trading_partner: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new order in the system, capturing customer purchase details and item specifications.

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

    def create_order_file(
        self,
        order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates an order file that compiles important data related to a specific order for record-keeping and processing.

        Args:
            order_id: ID of the order.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product(
        self,
        gtin: Optional[str] = None,
        measurements: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new product entry in the inventory, adding details such as name, price, and description.

        Args:
            gtin: Global Trade Item Number.
            measurements: Measurements of the product.
            name: Name of the product.
            sku: Stock Keeping Unit.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_return(
        self,
        line_items: Optional[List[Any]] = None,
        order_id: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Processes a return request, facilitating the return of products from customers back to inventory.

        Args:
            line_items: 
            order_id: ID of the order.
            warehouse_id: ID of the warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_connection(
        self,
    ) -> Dict[str, Any]:
        """Deletes a specific connection in the system, removing integration points or APIs as needed.
        Returns:
            API response as a dictionary.
        """
        ...

    def exchange_auth_code(
        self,
        auth_code: Optional[str] = None,
        customer_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exchanges an authorization code for token generation in the authentication process, enabling secure API access.

        Args:
            auth_code: Authorization code for the request.
            customer_id: The ID of the customer.
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_sandbox(
        self,
        integration_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a sandbox environment for testing and development purposes without affecting live data.

        Args:
            integration_type: Type of integration for the Trackstar API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_bills(
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
        """Retrieves all bills in the system for review, providing financial tracking and expense insights.

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

    def get_all_cart_orders(
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
        """Fetches all cart orders, showing active and completed orders within the cart management system.

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

    def get_all_cart_products(
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
        """Retrieves all products currently in the cart, helping to review inventory for customer orders.

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

    def get_all_cart_warehouses(
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
        """Gets the details of all warehouses linked to the cart system, allowing for management of inventory storage locations.

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

    def get_all_inbound_shipment_suppliers(
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
        """Retrieves information about all inbound shipment suppliers, aiding in supplier management and logistics.

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

    def get_all_inbound_shipments(
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
        """Fetches information on all inbound shipments, providing visibility into incoming inventory.

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

    def get_all_inventory_items(
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
        """Retrieves a complete list of all inventory items, essential for managing stock levels and product availability.

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

    def get_all_labor_activities(
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
        """Gets a comprehensive overview of all labor activities within the system, aiding labor management.

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

    def get_all_order_channels(
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
        """Fetches the list of all order channels used within the system, providing insights into sales performance across platforms.

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

    def get_all_orders(
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
        """Retrieves all orders processed in the system, enabling order management and tracking.

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

    def get_all_products(
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
        """Gets a complete listing of all products in the inventory system, useful for catalog management.

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

    def get_all_returns(
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
        """Retrieves a list of all returns processed in the system for tracking and analysis.

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

    def get_all_shipments(
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
        """Gets details for all shipments handled in the system, aiding in shipping and tracking management.

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

    def get_all_shipping_methods(
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
        """Retrieves information on all available shipping methods for orders, facilitating delivery decision-making.

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

    def get_all_warehouse_customers(
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
        """Gets a comprehensive list of all warehouse customers, streamlining customer management processes.

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

    def get_all_warehouse_locations(
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
    ) -> Dict[str, Any]:
        """Retrieves details of all warehouse locations for effective space management and inventory control.

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
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_warehouses(
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
        """Gets a complete list of all warehouses in the system for logistics and inventory management.

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

    def get_bill(
        self,
        bill_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific bill for review and financial tracking within the system.

        Args:
            bill_id: ID of the bill.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_cart_order(
        self,
        order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific cart order, allowing for individualized order review and management.

        Args:
            order_id: Order ID for the Trackstar API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_cart_product(
        self,
        product_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves information on a specific cart product, aiding in inventory management and product details.

        Args:
            product_id: ID of the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_cart_warehouse(
        self,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets details of a specific cart warehouse to manage storage and logistics efficiently.

        Args:
            warehouse_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connection(
        self,
        connection_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific connection in the system, allowing for management of integrations.

        Args:
            connection_id: The ID of the connection.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connections(
        self,
        page_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all current connections in the system for tracking and management purposes.

        Args:
            page_token: Token for retrieving the next page of results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inbound_shipment(
        self,
        inbound_shipment_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific inbound shipment, providing visibility into inventory coming into the system.

        Args:
            inbound_shipment_id: ID of the inbound shipment.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inventory_item(
        self,
        inventory_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets detailed information about a specific inventory item, facilitating inventory management and tracking.

        Args:
            inventory_id: ID of the inventory item.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inventory_ledger(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the inventory ledger to help track stock movements and adjustments over time.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_kit_create_update_schema_for_connection(
        self,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the kit create update schema for the connection, aiding in integration and data mapping.

        Args:
            method: HTTP method for the Trackstar API request (e.g., GET, POST).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_kit_create_update_schema_for_integration(
        self,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets the kit create update schema for integration, assisting in syncing product kit data.

        Args:
            method: HTTP method for the Trackstar API request (e.g., GET, POST).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_labor_activity(
        self,
        labor_activity_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific labor activity for detailed analysis and resource management.

        Args:
            labor_activity_id: The ID of the labor activity.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order(
        self,
        order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets details of a specific order, enabling thorough review and management of customer purchases.

        Args:
            order_id: The ID of the order.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order_create_update_schema_for_connection(
        self,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the order create update schema for the connection for integration purposes.

        Args:
            method: HTTP method for the Trackstar API request (e.g., GET, POST, PUT, DELETE).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order_create_update_schema_for_integration(
        self,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets the order create update schema for integration, aiding in standardizing order processing.

        Args:
            method: HTTP method for the Trackstar API request (e.g., GET, POST, PUT, DELETE).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order_packs(
        self,
        order_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the order packs associated with a specific order, streamlining order fulfillment processes.

        Args:
            order_id: ID of the order.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product(
        self,
        product_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets detailed information about a specific product, helping with inventory management and sales.

        Args:
            product_id: ID of the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_create_update_schema_for_connection(
        self,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the product create update schema for the connection for effective inventory management integration.

        Args:
            method: HTTP method for the Trackstar API request (e.g., GET, POST, PUT, DELETE).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_create_update_schema_for_integration(
        self,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets the product create update schema for integration, ensuring consistent data handling.

        Args:
            method: HTTP method for the Trackstar API request (e.g., GET, POST, PUT, DELETE).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_return(
        self,
        return_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific return, allowing for tracking and analysis of customer returns.

        Args:
            return_id: ID to be returned by the Trackstar API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_return_create_update_schema_for_connection(
        self,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the return create update schema for the connection, facilitating integration of return processing.

        Args:
            method: The HTTP method for the Trackstar API request (e.g., GET, POST, PUT, DELETE).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_return_create_update_schema_for_integration(
        self,
        method: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets the return create update schema for integration, ensuring efficient handling of returns.

        Args:
            method: HTTP method for the Trackstar API request (e.g., GET, POST, PUT, DELETE).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_shipment(
        self,
        shipment_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific shipment, providing details for tracking and management.

        Args:
            shipment_id: ID of the shipment.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_shipping_method(
        self,
        shipping_method_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets detailed information about a specific shipping method, helping to choose the right delivery options.

        Args:
            shipping_method_id: ID of the shipping method.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_warehouse(
        self,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific warehouse for effective inventory and logistics management.

        Args:
            warehouse_id: ID of the warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_warehouse_customer(
        self,
        warehouse_customer_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets details of a specific warehouse customer, aiding in customer relationship management.

        Args:
            warehouse_customer_id: ID of the warehouse customer.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_warehouse_location(
        self,
        location_id: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific warehouse location for managing inventory placement.

        Args:
            location_id: ID of the location.
            warehouse_id: ID of the warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def integration_info(
        self,
        integration_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches integration information for overall system analytics and performance metrics.

        Args:
            integration_type: Type of integration for the Trackstar API.
        Returns:
            API response as a dictionary.
        """
        ...

    def integration_info_for_single_integration(
        self,
        integration_name: Optional[str] = None,
        integration_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets integration info for a single integration to facilitate targeted analysis and troubleshooting.

        Args:
            integration_name: Name of the integration.
            integration_type: Type of the integration.
        Returns:
            API response as a dictionary.
        """
        ...

    def receive_inbound_shipment(
        self,
        line_items: Optional[List[Any]] = None,
        warehouse_id: Optional[str] = None,
        warehouse_location_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Processes the receiving of an inbound shipment, updating inventory levels accordingly.

        Args:
            line_items: 
            warehouse_id: The ID of the warehouse.
            warehouse_location_id: The ID of the warehouse location.
        Returns:
            API response as a dictionary.
        """
        ...

    def sandbox_simulate_fulfill(
        self,
        partial: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Simulates order fulfillment in a sandbox environment for testing and development purposes.

        Args:
            partial: Partial data for the Trackstar API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def ship_order(
        self,
        carrier: Optional[str] = None,
        measurements: Optional[Dict[str, Any]] = None,
        packages: Optional[List[Any]] = None,
        shipped_date: Optional[str] = None,
        shipping_cost: Optional[str] = None,
        shipping_method: Optional[str] = None,
        tracking_number: Optional[str] = None,
        tracking_url: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Ships a specific order, managing the logistics of delivering products to the customer.

        Args:
            carrier: The shipping carrier (e.g., FedEx, UPS).
            measurements: Dimensions and weight of the package.
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

    def sync_connection(
        self,
        functions_to_sync: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Synchronizes a specific connection in the system, ensuring that integrations are consistent and up-to-date.

        Args:
            functions_to_sync: An array of function names to synchronize.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_a_kit_product(
        self,
        gtin: Optional[str] = None,
        inventory_items: Optional[List[Any]] = None,
        measurements: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing kit product to reflect new configurations or inventory changes.

        Args:
            gtin: Global Trade Item Number (GTIN) of the product.
            inventory_items: 
            measurements: Product measurements.
            name: Name of the product.
            sku: Stock Keeping Unit (SKU) of the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_inbound_shipment(
        self,
        expected_arrival_date: Optional[str] = None,
        line_items: Optional[List[Any]] = None,
        purchase_order_number: Optional[str] = None,
        supplier: Optional[str] = None,
        supplier_object: Optional[Dict[str, Any]] = None,
        tracking_number: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates details of an existing inbound shipment, ensuring accurate tracking and inventory management.

        Args:
            expected_arrival_date: The expected arrival date of the shipment.
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

    def update_inbound_shipment_trackstar_tags(
        self,
    ) -> Dict[str, Any]:
        """Modifies Trackstar tags associated with an inbound shipment for better tracking capabilities.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_inventory_trackstar_tags(
        self,
    ) -> Dict[str, Any]:
        """Updates Trackstar tags associated with inventory items for improved tracking analytics.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_order(
        self,
        channel: Optional[str] = None,
        channel_object: Optional[Dict[str, Any]] = None,
        invoice_currency_code: Optional[str] = None,
        line_items: Optional[List[Any]] = None,
        order_number: Optional[str] = None,
        reference_id: Optional[str] = None,
        ship_to_address: Optional[Dict[str, Any]] = None,
        shipping_method: Optional[str] = None,
        status: Optional[str] = None,
        total_discount: Optional[str] = None,
        total_price: Optional[str] = None,
        total_shipping: Optional[str] = None,
        total_tax: Optional[str] = None,
        trading_partner: Optional[str] = None,
        warehouse_customer_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing order with new information or changes to ensure accuracy in processing.

        Args:
            channel: The sales channel for the order.
            channel_object: Details about the sales channel.
            invoice_currency_code: The currency code for the invoice.
            line_items: 
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

    def update_order_trackstar_tags(
        self,
    ) -> Dict[str, Any]:
        """Modifies Trackstar tags for a specific order to enhance tracking and reporting capabilities.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product(
        self,
        gtin: Optional[str] = None,
        measurements: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates details of an existing product inventory, ensuring that attributes remain current.

        Args:
            gtin: 
            measurements: 
            name: 
            sku: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product_trackstar_tags(
        self,
    ) -> Dict[str, Any]:
        """Modifies Trackstar tags for products to improve tracking performance and categorization.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_return(
        self,
        line_items: Optional[List[Any]] = None,
        order_id: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates information for a specific return, ensuring that data stays relevant and accurate.

        Args:
            line_items: 
            order_id: ID of the order.
            warehouse_id: ID of the warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_return_trackstar_tags(
        self,
    ) -> Dict[str, Any]:
        """Modifies Trackstar tags associated with a specific return for enhanced tracking and reporting.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_sale_fulfillment_ship_(
        self,
        Lines: Optional[List[Any]] = None,
        RequireBy: Optional[str] = None,
        ShippingAddress: Optional[Dict[str, Any]] = None,
        ShippingNotes: Optional[str] = None,
        Status: Optional[str] = None,
        TaskID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the fulfillment ship information for a sale, ensuring that shipment details are accurate in the system.

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

    def update_warehouse_trackstar_tags(
        self,
    ) -> Dict[str, Any]:
        """Updates Trackstar tags for warehouses to improve tracking and management insights.
        Returns:
            API response as a dictionary.
        """
        ...

