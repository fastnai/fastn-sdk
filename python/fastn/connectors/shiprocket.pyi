"""Fastn ShipRocket connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _ShiprocketCreateForwardShipmentVendorDetails(TypedDict, total=False):
    address: str
    address_2: str
    city: str
    country: str
    email: str
    name: str
    phone: int
    pickup_location: str
    pin_code: str
    state: str

class ShiprocketConnector:
    """ShipRocket connector ().

    Provides 12 tools.
    """

    def shiprocket__cancel_shipment(
        self,
        awbs: Optional[List[Any]] = None,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Cancels one or more scheduled ShipRocket shipments using their AWB numbers, stopping all further courier processing and status updates. Use this tool only when a shipment must be definitively stopped before pickup or dispatch. Do not use this tool if you only need to modify shipment details; cancellation may be irreversible once the courier has accepted the parcel. This operation modifies shipment state and cannot always be undone.

        Args:
            awbs: 
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shiprocket__create_forward_shipment(
        self,
        billing_address: Optional[str] = None,
        billing_city: Optional[str] = None,
        billing_country: Optional[str] = None,
        billing_customer_name: Optional[str] = None,
        billing_email: Optional[str] = None,
        billing_last_name: Optional[str] = None,
        billing_phone: Optional[str] = None,
        billing_pincode: Optional[str] = None,
        billing_state: Optional[str] = None,
        breadth: Optional[int] = None,
        channel_id: Optional[str] = None,
        height: Optional[int] = None,
        length: Optional[int] = None,
        order_date: Optional[str] = None,
        order_id: Optional[str] = None,
        order_items: Optional[List[Any]] = None,
        payment_method: Optional[str] = None,
        pickup_location: Optional[str] = None,
        shipping_is_billing: Optional[bool] = None,
        sub_total: Optional[int] = None,
        token: Optional[str] = None,
        vendor_details: Optional[_ShiprocketCreateForwardShipmentVendorDetails] = None,
        weight: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Creates a forward shipment in ShipRocket, initiating the logistics process for dispatching goods from the seller to the customer. Use this tool when a new order needs to be shipped outbound. Do not use this tool for return shipments; use shiprocket__create_return_shipment instead. This operation creates a new shipment record and triggers logistics workflows.

        Args:
            billing_address: 
            billing_city: 
            billing_country: 
            billing_customer_name: 
            billing_email: 
            billing_last_name: 
            billing_phone: 
            billing_pincode: 
            billing_state: 
            breadth: 
            channel_id: 
            height: 
            length: 
            order_date: 
            order_id: 
            order_items: 
            payment_method: 
            pickup_location: 
            shipping_is_billing: 
            sub_total: 
            token: 
            vendor_details: 
            weight: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shiprocket__create_return_shipment(
        self,
        breadth: Optional[int] = None,
        channel_id: Optional[str] = None,
        company_name: Optional[str] = None,
        height: Optional[int] = None,
        length: Optional[int] = None,
        order_date: Optional[str] = None,
        order_id: Optional[str] = None,
        order_items: Optional[List[Any]] = None,
        payment_method: Optional[str] = None,
        pickup_address: Optional[str] = None,
        pickup_address_2: Optional[str] = None,
        pickup_city: Optional[str] = None,
        pickup_country: Optional[str] = None,
        pickup_customer_name: Optional[str] = None,
        pickup_email: Optional[str] = None,
        pickup_isd_code: Optional[str] = None,
        pickup_last_name: Optional[str] = None,
        pickup_phone: Optional[str] = None,
        pickup_pincode: Optional[int] = None,
        pickup_state: Optional[str] = None,
        request_pickup: Optional[bool] = None,
        shipping_address: Optional[str] = None,
        shipping_address_2: Optional[str] = None,
        shipping_city: Optional[str] = None,
        shipping_country: Optional[str] = None,
        shipping_customer_name: Optional[str] = None,
        shipping_email: Optional[str] = None,
        shipping_isd_code: Optional[str] = None,
        shipping_last_name: Optional[str] = None,
        shipping_phone: Optional[int] = None,
        shipping_pincode: Optional[int] = None,
        shipping_state: Optional[str] = None,
        sub_total: Optional[int] = None,
        token: Optional[str] = None,
        total_discount: Optional[str] = None,
        weight: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Creates a return shipment in ShipRocket, initiating the logistics process for sending goods back to the seller or origin. Use this tool when a customer has requested a return and you need to generate a return shipping label and tracking. Do not use this tool for new outbound deliveries; use shiprocket__create_forward_shipment instead. This operation creates a new shipment record and triggers logistics workflows.

        Args:
            breadth: 
            channel_id: 
            company_name: 
            height: 
            length: 
            order_date: 
            order_id: 
            order_items: 
            payment_method: 
            pickup_address: 
            pickup_address_2: 
            pickup_city: 
            pickup_country: 
            pickup_customer_name: 
            pickup_email: 
            pickup_isd_code: 
            pickup_last_name: 
            pickup_phone: 
            pickup_pincode: 
            pickup_state: 
            request_pickup: 
            shipping_address: 
            shipping_address_2: 
            shipping_city: 
            shipping_country: 
            shipping_customer_name: 
            shipping_email: 
            shipping_isd_code: 
            shipping_last_name: 
            shipping_phone: 
            shipping_pincode: 
            shipping_state: 
            sub_total: 
            token: 
            total_discount: 
            weight: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shiprocket__generate_token(
        self,
        email: Optional[str] = None,
        password: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Authenticates with the ShipRocket API using login credentials and returns a bearer token required for all subsequent API calls. Use this tool before calling any other ShipRocket tool if a valid token is not already available. Tokens may expire and need to be refreshed. This operation does not create or modify any shipment or order data.

        Args:
            email: 
            password: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shiprocket__get_shipment(
        self,
        shipmentId: str,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific ShipRocket shipment using its unique shipment ID, including status, courier, and recipient details. Use this tool when you need full shipment metadata for a known shipment ID. To list all shipments, use shiprocket__list_shipments instead. Read-only; no data is modified.

        Args:
            shipmentId:  (required)
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shiprocket__get_tracking_by_awb(
        self,
        awb_code: Optional[str] = None,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves real-time tracking information for a single shipment using its Air Waybill (AWB) number. Use this tool when you have a specific AWB code and need courier or delivery status updates. For tracking multiple AWBs at once, use shiprocket__list_tracking_by_awbs. For tracking by order or shipment ID, use the corresponding tools. Read-only; no data is modified.

        Args:
            awb_code: 
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shiprocket__get_tracking_by_order_id(
        self,
        channel_id: Optional[str] = None,
        order_id: Optional[str] = None,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves real-time tracking information for a shipment using its associated ShipRocket order ID. Use this tool when you have an order ID and need to check delivery status or courier updates. If you have a shipment ID or AWB number instead, use shiprocket__get_tracking_by_shipment_id or shiprocket__get_tracking_by_awb. Read-only; no data is modified.

        Args:
            channel_id: 
            order_id: 
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shiprocket__get_tracking_by_shipment_id(
        self,
        shipment_id: str,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves real-time tracking information for a shipment using its unique ShipRocket shipment ID. Use this tool when you have a shipment ID and need courier or delivery status updates. If you have an order ID or AWB number instead, use shiprocket__get_tracking_by_order_id or shiprocket__get_tracking_by_awb. Read-only; no data is modified.

        Args:
            shipment_id:  (required)
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shiprocket__get_wallet_balance(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the current ShipRocket wallet balance for the authenticated account, showing available funds for shipping charges. Use this tool when you need to verify sufficient funds before creating shipments or to display the account balance to users. Read-only; no data is modified.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shiprocket__list_channels(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all sales or distribution channels connected to your ShipRocket account, such as marketplaces or storefronts. Use this tool when you need to discover available channels or retrieve channel IDs for use in order or shipment operations. Read-only; no data is modified.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shiprocket__list_shipments(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all shipments available in your ShipRocket account, providing an overview of current and past shipments with their statuses. Use this tool when you need a broad view of all shipments or want to find a specific shipment without knowing its ID. For detailed information on a single shipment, use shiprocket__get_shipment instead. Read-only; no data is modified.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def shiprocket__list_tracking_by_awbs(
        self,
        awbs: Optional[List[Any]] = None,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves tracking information for multiple shipments in a single request using a list of Air Waybill (AWB) numbers. Use this tool when you need to check the status of several shipments at once to avoid making repeated individual calls. For a single AWB, use shiprocket__get_tracking_by_awb instead. This is a POST request but is read-only; no data is modified.

        Args:
            awbs: 
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

