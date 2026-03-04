"""Fastn PackageX connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _PackagexCreateFulfillmentMetadata(TypedDict, total=False):
    fabricAllocation: Dict[str, Any]

class _PackagexCreateFulfillmentRecipient(TypedDict, total=False):
    address: Dict[str, Any]
    business: str
    contact_id: str
    email: str
    name: str
    phone: str

class _PackagexCreateFulfillmentSender(TypedDict, total=False):
    address: Dict[str, Any]
    business: str
    contact_id: str
    email: str
    name: str
    phone: str

class _PackagexCreateFulfillmentShipmentOptions(TypedDict, total=False):
    checkout_total: int
    lead_time_mins: int
    max_delivery_days: str
    provider_instructions: str
    provider_timeout: int
    providers: List[Any]
    rate_types: List[Any]
    request_provider_pickup: bool
    same_day_tip_amount: str
    service_levels: List[Any]
    verify_addresses: bool

class PackagexConnector:
    """PackageX connector ().

    Provides 1 tools.
    """

    def packagex_create_fulfillment(
        self,
        complete_at: Optional[int] = None,
        id: Optional[str] = None,
        inventory: Optional[List[Any]] = None,
        location_id: Optional[str] = None,
        metadata: Optional[_PackagexCreateFulfillmentMetadata] = None,
        order_number: Optional[str] = None,
        organization_id: Optional[str] = None,
        recipient: Optional[_PackagexCreateFulfillmentRecipient] = None,
        sender: Optional[_PackagexCreateFulfillmentSender] = None,
        shipment_options: Optional[_PackagexCreateFulfillmentShipmentOptions] = None,
    ) -> Dict[str, Any]:
        """Creates a new fulfillment record in PackageX to initiate a shipping or logistics operation. Use this tool when you need to register a new outbound shipment, assign a carrier, and begin tracking for an order. Do not use this tool to update or cancel an existing fulfillment. This operation creates a persistent fulfillment record in PackageX and may trigger carrier label generation and tracking assignments, which may incur shipping costs.

        Args:
            complete_at: 
            id: 
            inventory: 
            location_id: 
            metadata: 
            order_number: 
            organization_id: 
            recipient: 
            sender: 
            shipment_options: 
        Returns:
            API response as a dictionary.
        """
        ...

