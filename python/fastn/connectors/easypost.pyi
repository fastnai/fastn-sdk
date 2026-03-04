"""Fastn EasyPost connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _EasyPostBuyShipmentRate(TypedDict, total=False):
    id: str

class _EasyPostCreateAddressAddress(TypedDict, total=False):
    city: str
    company: str
    country: str
    phone: str
    state: str
    street1: str
    street2: str
    zip: str

class _EasyPostCreateAndVerifyAddressAddress(TypedDict, total=False):
    city: str
    company: str
    country: str
    phone: str
    state: str
    street1: str
    street2: str
    zip: str

class _EasyPostCreateChildUserUser(TypedDict, total=False):
    name: str

class _EasyPostCreateParcelParcel(TypedDict, total=False):
    height: str
    length: str
    weight: str
    width: str

class _EasyPostCreateShipmentShipment(TypedDict, total=False):
    customs_info: Dict[str, Any]
    from_address: Dict[str, Any]
    parcel: Dict[str, Any]
    to_address: Dict[str, Any]

class _EasyPostCreateTrackerTracker(TypedDict, total=False):
    carrier: str
    tracking_code: str

class _EasyPostCreateVerifiedAddressAddress(TypedDict, total=False):
    city: str
    company: str
    country: str
    phone: str
    state: str
    street1: str
    street2: str
    zip: str

class EasypostConnector:
    """EasyPost connector ().

    Provides 18 tools.
    """

    def easy_post_buy_shipment(
        self,
        insurance: str,
        rate: _EasyPostBuyShipmentRate,
        shipment_Id: str,
    ) -> Dict[str, Any]:
        """Purchases a shipping label for an existing EasyPost shipment by its unique shipment ID. Use this after creating a shipment and selecting a rate to finalize the purchase and generate a printable label. This action charges the account and is not reversible without a separate refund request. Do not use this to create a new shipment — use easy_post_create_shipment first.

        Args:
            insurance: Insurance details for the shipment. (required)
            rate: Rate details for the shipment. (required)
            shipment_Id: ID of the shipment in EasyPost. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_create_address(
        self,
        address: _EasyPostCreateAddressAddress,
    ) -> Dict[str, Any]:
        """Creates a new unverified address record in EasyPost. Use this when you need to store an address without immediately validating it. Do not use this if you also need postal verification at creation time — use easy_post_create_verified_address or easy_post_create_and_verify_address instead. This action persists a new address record.

        Args:
            address: Address information for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_create_and_verify_address(
        self,
        address: _EasyPostCreateAndVerifyAddressAddress,
    ) -> Dict[str, Any]:
        """Creates and verifies a new address in EasyPost in a single operation using the dedicated /create_and_verify endpoint. Use this when you need both address creation and postal validation confirmed in one call. Do not use this if you only need to create an address without verification — use easy_post_create_address instead. This action persists a new address record.

        Args:
            address: Address information for the shipment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_create_child_user(
        self,
        user: _EasyPostCreateChildUserUser,
    ) -> Dict[str, Any]:
        """Creates a new child user account under the authenticated EasyPost parent account. Use this to provision sub-accounts for separate billing or access control within the same organization. Do not use this to create top-level accounts or to modify existing users. This action persists a new user record.

        Args:
            user: User details for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_create_parcel(
        self,
        parcel: _EasyPostCreateParcelParcel,
    ) -> Dict[str, Any]:
        """Creates a new EasyPost parcel record with physical dimensions and weight. Use this before creating a shipment when you need to define the package characteristics. Do not use this to retrieve an existing parcel — use easy_post_get_parcel instead. This action persists a new parcel record.

        Args:
            parcel: Dimensions and weight of the parcel. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_create_shipment(
        self,
        shipment: _EasyPostCreateShipmentShipment,
    ) -> Dict[str, Any]:
        """Creates a new EasyPost shipment with origin, destination, and parcel details, and returns available carrier rates. Use this as the first step before purchasing a label with easy_post_buy_shipment. Do not use this to purchase a label — that requires a separate call to easy_post_buy_shipment after selecting a rate. This action persists a new shipment record.

        Args:
            shipment: Details of the shipment being created or updated. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_create_tracker(
        self,
        tracker: _EasyPostCreateTrackerTracker,
    ) -> Dict[str, Any]:
        """Creates a new EasyPost tracker to monitor the progress of a shipment by carrier and tracking number. Use this when you have a tracking number from a carrier and want to receive tracking events via EasyPost. Do not use this to track shipments already created through EasyPost — those receive trackers automatically. This action persists a new tracker record.

        Args:
            tracker: Details of the shipment to be tracked via EasyPost. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_create_verified_address(
        self,
        address: _EasyPostCreateVerifiedAddressAddress,
        verify: bool,
    ) -> Dict[str, Any]:
        """Creates a new address in EasyPost and immediately marks it as verified. Use this when you want to store an address and confirm its validity in a single step using the standard address creation endpoint with verification flags. Do not use this if you only need to create an unverified address — use easy_post_create_address instead. Do not use this if you want to use the dedicated verify endpoint — use easy_post_create_and_verify_address instead. This action persists a new address record.

        Args:
            address: Address information for the EasyPost API request. (required)
            verify: Flag indicating whether to verify the address with EasyPost. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_delete_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an EasyPost user account by its unique user ID. Use this only when a user account must be fully removed from the system. This action is irreversible — the user and all associated data will be permanently deleted. Do not use this to deactivate or modify a user — use easy_post_get_user to inspect the account first.

        Args:
            userId: User ID for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_get_address(
        self,
        addressId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single EasyPost address by its unique address ID. Use this when you need to look up a specific, known address record. Do not use this to browse or list multiple addresses — use easy_post_list_addresses instead. No data is modified by this call.

        Args:
            addressId: ID of the address for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_get_parcel(
        self,
        parcel_Id: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific EasyPost parcel by its unique parcel ID, including dimensions and weight. Use this to inspect a known parcel record. Do not use this to create a new parcel — use easy_post_create_parcel instead. No data is modified by this call.

        Args:
            parcel_Id: ID of the parcel for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_get_shipment(
        self,
        shipment_Id: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific EasyPost shipment by its unique shipment ID, including its status, rates, tracking code, and label URL. Use this to inspect a known shipment. Do not use this to list all shipments — use easy_post_list_shipments instead. No data is modified by this call.

        Args:
            shipment_Id: ID of the shipment in EasyPost. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_get_tracker(
        self,
        tracker_Id: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed tracking information for a specific EasyPost tracker by its unique tracker ID, including carrier events and current status. Use this when you have a known tracker ID and need its full details. Do not use this to browse all trackers — use easy_post_list_trackers instead. No data is modified by this call.

        Args:
            tracker_Id: Tracking ID for the EasyPost request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_get_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific EasyPost user account by its unique user ID. Use this to inspect user profile information for a known user. Do not use this to list multiple users or manage child users — use easy_post_create_child_user for child account creation. No data is modified by this call.

        Args:
            userId: User ID for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_list_addresses(
        self,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all address records associated with the authenticated EasyPost user account. Use this to browse or enumerate saved addresses. Do not use this to retrieve a single specific address — use easy_post_get_address instead. No data is modified by this call.

        Args:
            page_size: Specifies the number of results per page for EasyPost API pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_list_shipments(
        self,
        after_id: Optional[str] = None,
        before_id: Optional[str] = None,
        end_datetime: Optional[str] = None,
        include_children: Optional[bool] = None,
        page_size: Optional[float] = None,
        purchased: Optional[bool] = None,
        start_datetime: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all EasyPost shipments associated with the authenticated user account. Use this to browse, filter, or audit shipment history. Do not use this to retrieve a single shipment — use easy_post_get_shipment instead. No data is modified by this call.

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

    def easy_post_list_trackers(
        self,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all EasyPost trackers associated with the authenticated users shipments. Use this to enumerate or filter tracking records across multiple shipments. Do not use this to retrieve a single tracker — use easy_post_get_tracker instead. No data is modified by this call.

        Args:
            page_size: Number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def easy_post_verify_address(
        self,
        addressId: str,
    ) -> Dict[str, Any]:
        """Verifies whether an existing EasyPost address is valid and deliverable by its unique address ID. Use this to confirm the legitimacy of an already-stored address before using it in a shipment. Do not use this to create a new address — use easy_post_create_address or easy_post_create_and_verify_address instead. No data is permanently modified by this call.

        Args:
            addressId: ID of the address for the EasyPost API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

