"""Fastn ShipRocket  connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ShiprocketConnector:
    """ShipRocket  connector ().

    Provides 12 tools.
    """

    def cancel_shipment(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Cancels a shipment that has been scheduled in the shipping management system, ceasing all further processing and updates.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_forward_shipment(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a forward shipment in the shipping management system, initiating the process for dispatching goods to the destination.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_return_shipment(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a return shipment in the shipping management system, initiating the process for returning goods back to the sender.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token(
        self,
        email: Optional[str] = None,
        password: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates an authentication token in the security management system for user access to the shipping services.

        Args:
            email: 
            password: 
        Returns:
            API response as a dictionary.
        """
        ...

    def list_shipment(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all shipments currently available in the shipping management system for easy overview and tracking.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def retrieve_channels_(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of channels available in the distribution or logistics management system for shipment and communication.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def retrieve_shipment(
        self,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific shipment by its unique shipment ID in the shipping management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def retrieve_tracking_by_awb_(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves tracking information for a specific shipment using the Air Waybill (AWB) number in the shipping tracking system.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def retrieve_tracking_by_order_id(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves tracking information for a shipment using its associated order ID in the shipping tracking system.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def retrieve_tracking_by_shipment_id(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves tracking information for a shipment using its unique shipment ID in the shipping tracking system.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def retrieve_tracking_multiple_awbs(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves tracking information for multiple shipments using their respective AWB numbers in the shipping tracking system.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def retrieve_wallet_balance(
        self,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the current wallet balance in the payment or transaction management system for the user to see available funds.

        Args:
            token: 
        Returns:
            API response as a dictionary.
        """
        ...

