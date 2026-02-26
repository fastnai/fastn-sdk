"""Fastn PayPal connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class PaypalConnector:
    """PayPal connector ().

    Provides 10 tools.
    """

    def cancel_unclaimed_payout_item(
        self,
        enviroment: str,
        payoutItemId: str,
    ) -> Dict[str, Any]:
        """Cancels a payout item that has not been claimed in the payment processing system.

        Args:
            enviroment: Specifies the environment (e.g., sandbox, production). (required)
            payoutItemId: Identifier for the payout item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def capture_payment_for_order(
        self,
        PayPalRequestId: str,
        Prefer: str,
    ) -> Dict[str, Any]:
        """Captures the payment for a specific order within the e-commerce platform.

        Args:
            PayPalRequestId: Unique identifier for the PayPal request. (required)
            Prefer: HTTP header to specify preferences for the PayPal request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def confirm_payment_source(
        self,
        PayPalRequestId: str,
        Prefer: str,
    ) -> Dict[str, Any]:
        """Confirms the payment source associated with a user in the payment processing system.

        Args:
            PayPalRequestId: Unique identifier for the PayPal request. (required)
            Prefer: HTTP Prefer header for controlling response format. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_batch_payout(
        self,
        PayPalRequestId: str,
    ) -> Dict[str, Any]:
        """Creates a batch payout request in the payment processing system to distribute funds.

        Args:
            PayPalRequestId: Unique request ID for the PayPal transaction. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_order(
        self,
        PayPalRequestId: str,
        Prefer: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new order in the e-commerce platform using the provided order details.

        Args:
            PayPalRequestId: Unique identifier for the PayPal request. (required)
            Prefer: Header indicating preferred response format.
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_access_token(
        self,
        grant_type: str,
        ignoreCache: str,
        return_authn_schemes: str,
        return_client_metadata: str,
        return_unconsented_scopes: str,
    ) -> Dict[str, Any]:
        """Generates an access token for authentication in the API system.

        Args:
            grant_type: The type of grant for the OAuth 2.0 flow. (required)
            ignoreCache: Flag to ignore cached data (if applicable). (required)
            return_authn_schemes: Flag to return authentication schemes (if applicable). (required)
            return_client_metadata: Flag to return client metadata (if applicable). (required)
            return_unconsented_scopes: Flag to return unconsented scopes (if applicable). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order_detail(
        self,
        enviroment: str,
        orderId: str,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific order in the e-commerce platform using the order ID.

        Args:
            enviroment: The environment for the PayPal API request (e.g., sandbox, production). (required)
            orderId: The order ID for the PayPal API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_payout_batch_details(
        self,
        fields: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        total_required: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific payout batch in the payment processing system using the batch ID.

        Args:
            fields: Specifies the fields to be returned in the response.
            page: Specifies the page number for pagination.
            page_size: Specifies the number of records per page.
            total_required: Indicates whether the total number of records is required.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_payout_item_details(
        self,
        enviroment: str,
        payoutItemId: str,
    ) -> Dict[str, Any]:
        """Gets detailed information about an individual payout item in the payout batch.

        Args:
            enviroment: The environment for the PayPal API call (e.g., sandbox, production). (required)
            payoutItemId: The ID of the payout item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_info(
        self,
        schema: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves user information based on the authenticated session within the API.

        Args:
            schema: Schema identifier for the PayPal API request.
        Returns:
            API response as a dictionary.
        """
        ...

