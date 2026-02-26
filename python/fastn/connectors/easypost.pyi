"""Fastn EasyPost connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class EasypostConnector:
    """EasyPost connector ().

    Provides 18 tools.
    """

    def buy_shipment(
        self,
        insurance: str,
        rate: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Purchases a shipment label for shipping an item.

        Args:
            insurance: Insurance details for the shipment. (required)
            rate: Rate details for the shipment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_address(
        self,
        address: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new address in the address management system.

        Args:
            address: Address information for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_and_verify_address(
        self,
        address: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates and verifies a new address in a single operation.

        Args:
            address: Address information for the shipment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_child_user(
        self,
        user: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new child user account within the user system.

        Args:
            user: User details for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_parcel(
        self,
        parcel: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new parcel in the logistics system.

        Args:
            parcel: Dimensions and weight of the parcel. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_shipment(
        self,
        shipment: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new shipment in the logistics system.

        Args:
            shipment: Details of the shipment being created or updated. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_tracker(
        self,
        tracker: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new tracker for monitoring the shipment's progress.

        Args:
            tracker: Details of the shipment to be tracked via EasyPost. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_verified_address(
        self,
        address: Dict[str, Any],
        verify: bool,
    ) -> Dict[str, Any]:
        """Creates a verified address in the address management system.

        Args:
            address: Address information for the EasyPost API request. (required)
            verify: Flag indicating whether to verify the address with EasyPost. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Deletes a user account from the system.

        Args:
            userId: User ID for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_address(
        self,
        addressId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific address using its unique identifier.

        Args:
            addressId: ID of the address for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_addresses(
        self,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all addresses associated with the user account.

        Args:
            page_size: Specifies the number of results per page for EasyPost API pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_parcel(
        self,
        parcel_Id: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific parcel using its unique identifier.

        Args:
            parcel_Id: ID of the parcel for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_shipment(
        self,
        shipment_Id: str,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific shipment using its unique identifier.

        Args:
            shipment_Id: ID of the shipment in EasyPost. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_shipments(
        self,
        after_id: Optional[str] = None,
        before_id: Optional[str] = None,
        end_datetime: Optional[str] = None,
        include_children: Optional[bool] = None,
        page_size: Optional[float] = None,
        purchased: Optional[bool] = None,
        start_datetime: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all shipments associated with the user account.

        Args:
            after_id: Return results with IDs greater than this ID.
            before_id: Return results with IDs less than this ID.
            end_datetime: Filter results to include entries before this datetime.
            include_children: Include child records in the results.
            page_size: Number of results per page.
            purchased: Filter results to include only purchased items.
            start_datetime: Filter results to include entries after this datetime.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tracker(
        self,
        tracker_Id: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific tracker using its unique identifier.

        Args:
            tracker_Id: Tracking ID for the EasyPost request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_trackers(
        self,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all trackers associated with the user's shipments.

        Args:
            page_size: Number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific user by their unique identifier.

        Args:
            userId: User ID for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def verify_address(
        self,
        addressId: str,
    ) -> Dict[str, Any]:
        """Verifies the legitimacy of an existing address.

        Args:
            addressId: ID of the address for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

