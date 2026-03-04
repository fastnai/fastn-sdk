"""Fastn PayPal connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _PaypalConfirmPaymentSourcePaymentSource(TypedDict, total=False):
    card: Dict[str, Any]

class _PaypalCreateBatchPayoutSenderBatchHeader(TypedDict, total=False):
    email_message: str
    email_subject: str
    sender_batch_id: str

class PaypalConnector:
    """PayPal connector ().

    Provides 10 tools.
    """

    def paypal_cancel_unclaimed_payout_item(
        self,
        enviroment: str,
        payoutItemId: str,
    ) -> Dict[str, Any]:
        """Cancels a payout item that has not yet been claimed by the recipient in PayPal. Use this when a sent payout item is still in an unclaimed state and you need to reverse it and return the funds to the sender. This action is irreversible once processed — the cancellation cannot be undone, though a new payout can be issued afterward. Do not use this for payout items that have already been claimed or processed.

        Args:
            enviroment: Specifies the environment (e.g., sandbox, production). (required)
            payoutItemId: Identifier for the payout item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def paypal_capture_payment_for_order(
        self,
        PayPalRequestId: str,
        Prefer: str,
        enviroment: str,
        orderId: str,
    ) -> Dict[str, Any]:
        """Captures an authorized payment for a specific PayPal checkout order identified by its order ID, completing the fund transfer from buyer to seller. Use this after an order has been approved by the buyer to finalize the transaction. This action is financially irreversible — once captured, funds are transferred and cannot be automatically reversed. Do not use this if the order has not yet been approved or if you only want to authorize without capturing.

        Args:
            PayPalRequestId: Unique identifier for the PayPal request. (required)
            Prefer: HTTP header to specify preferences for the PayPal request. (required)
            enviroment: The environment for the PayPal API request (e.g., sandbox, production). (required)
            orderId: The ID of the order being processed via the PayPal API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def paypal_confirm_payment_source(
        self,
        PayPalRequestId: str,
        Prefer: str,
        enviroment: str,
        orderId: str,
        payment_source: _PaypalConfirmPaymentSourcePaymentSource,
    ) -> Dict[str, Any]:
        """Confirms the payment source for a specific PayPal checkout order, allowing the payer to explicitly verify their selected payment method before the order is processed. Use this during the checkout flow when the payment source needs to be confirmed prior to authorization or capture. Do not use this to capture payment — use paypal_capture_payment_for_order after confirmation.

        Args:
            PayPalRequestId: Unique identifier for the PayPal request. (required)
            Prefer: HTTP Prefer header for controlling response format. (required)
            enviroment: PayPal API environment (e.g., sandbox, production). (required)
            orderId: Identifier for the order being processed. (required)
            payment_source: Details of the payment source. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def paypal_create_batch_payout(
        self,
        PayPalRequestId: str,
        enviroment: str,
        items: Optional[List[Any]] = None,
        sender_batch_header: Optional[_PaypalCreateBatchPayoutSenderBatchHeader] = None,
    ) -> Dict[str, Any]:
        """Creates a batch payout request in PayPal to distribute funds to multiple recipients in a single operation. Use this when you need to send payments to one or more recipients simultaneously, such as for payroll, rewards, or refunds. This action initiates fund transfers and has financial side effects — funds will be debited from the senders PayPal account. Do not use this for single-order captures; use paypal_capture_payment_for_order instead.

        Args:
            PayPalRequestId: Unique request ID for the PayPal transaction. (required)
            enviroment: Environment the request is targeted to (e.g., sandbox, production). (required)
            items: 
            sender_batch_header: Header information for the sender batch.
        Returns:
            API response as a dictionary.
        """
        ...

    def paypal_create_order(
        self,
        PayPalRequestId: str,
        enviroment: str,
        purchase_units: List[Any],
        Prefer: Optional[str] = None,
        intent: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new PayPal checkout order with the provided order details such as amount, currency, and purchase units. Use this to initiate the checkout flow before the buyer approves and payment is captured. This does not charge the buyer — it only sets up the order. Do not use this to capture payment; use paypal_capture_payment_for_order after the buyer approves the order.

        Args:
            PayPalRequestId: Unique identifier for the PayPal request. (required)
            enviroment: Specifies the environment (e.g., 'sandbox', 'live'). (required)
            purchase_units:  (required)
            Prefer: Header indicating preferred response format.
            intent: Intent of the transaction (e.g., 'sale', 'authorize').
        Returns:
            API response as a dictionary.
        """
        ...

    def paypal_generate_access_token(
        self,
        enviroment: str,
        grant_type: str,
        ignoreCache: str,
        return_authn_schemes: str,
        return_client_metadata: str,
        return_unconsented_scopes: str,
    ) -> Dict[str, Any]:
        """Generates an OAuth2 access token for authenticating subsequent PayPal API requests using client credentials. Use this before making any PayPal API calls that require authorization. The token is time-limited and should be cached for its validity period rather than regenerated on every request. Do not use this for user-level authentication flows — it is intended for server-to-server API access.

        Args:
            enviroment: The PayPal environment (e.g., sandbox, production). (required)
            grant_type: The type of grant for the OAuth 2.0 flow. (required)
            ignoreCache: Flag to ignore cached data (if applicable). (required)
            return_authn_schemes: Flag to return authentication schemes (if applicable). (required)
            return_client_metadata: Flag to return client metadata (if applicable). (required)
            return_unconsented_scopes: Flag to return unconsented scopes (if applicable). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def paypal_get_order_detail(
        self,
        enviroment: str,
        orderId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a specific PayPal checkout order identified by its order ID, including status, amount, payer information, and purchase units. Use this to inspect or verify an order before or after processing. Do not use this to list multiple orders; this tool is for fetching a single order by ID only.

        Args:
            enviroment: The environment for the PayPal API request (e.g., sandbox, production). (required)
            orderId: The order ID for the PayPal API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def paypal_get_payout_batch_details(
        self,
        enviroment: str,
        payoutBatchId: str,
        fields: Optional[str] = None,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
        total_required: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific PayPal payout batch identified by its batch ID, including batch status, total amount, and individual payout item summaries. Use this to monitor or audit an entire payout batch after it has been created. Do not use this to retrieve details about a single payout item — use paypal_get_payout_item_details instead.

        Args:
            enviroment: Specifies the API environment (e.g., sandbox, production). (required)
            payoutBatchId: The ID of the payout batch. (required)
            fields: Specifies the fields to be returned in the response.
            page: Specifies the page number for pagination.
            page_size: Specifies the number of records per page.
            total_required: Indicates whether the total number of records is required.
        Returns:
            API response as a dictionary.
        """
        ...

    def paypal_get_payout_item_details(
        self,
        enviroment: str,
        payoutItemId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single payout item within a PayPal payout batch, identified by its payout item ID. Use this to check the status, amount, recipient, and transaction details of a specific payout item. Do not use this to retrieve details about an entire payout batch — use paypal_get_payout_batch_details instead.

        Args:
            enviroment: The environment for the PayPal API call (e.g., sandbox, production). (required)
            payoutItemId: The ID of the payout item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def paypal_get_user_info(
        self,
        enviroment: str,
        schema: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves profile information of the currently authenticated PayPal user based on their OAuth2 session, including name, email, and account details. Use this to identify the logged-in user after OAuth2 authentication. Do not use this to look up arbitrary users by ID — it only returns information for the authenticated session user.

        Args:
            enviroment: Specifies the environment (e.g., sandbox, production) for the PayPal API request. (required)
            schema: Schema identifier for the PayPal API request.
        Returns:
            API response as a dictionary.
        """
        ...

