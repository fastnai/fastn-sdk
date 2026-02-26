"""Fastn PackageX connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class PackagexConnector:
    """PackageX connector ().

    Provides 1 tools.
    """

    def create_fulfillments(
        self,
        complete_at: Optional[int] = None,
        id: Optional[str] = None,
        inventory: Optional[List[Any]] = None,
        location_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        order_number: Optional[str] = None,
        organization_id: Optional[str] = None,
        recipient: Optional[Dict[str, Any]] = None,
        sender: Optional[Dict[str, Any]] = None,
        shipment_options: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates fulfillments in the specified eCommerce connector context.

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

