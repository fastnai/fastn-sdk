"""Fastn Checkout connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _CheckoutCreateInstrumentCustomer(TypedDict, total=False):
    default: bool
    email: str
    id: str
    name: str
    phone: Dict[str, Any]

class _CheckoutCreatePaymentSource(TypedDict, total=False):
    cvv: str
    expiry_month: int
    expiry_year: int
    number: str
    type: str

class _CheckoutRefundPaymentDestination(TypedDict, total=False):
    account_holder: Dict[str, Any]
    account_number: str
    account_type: str
    bank: Dict[str, Any]
    bank_code: str
    bban: str
    branch_code: str
    country: str
    iban: str
    swift_bic: str

class _CheckoutRefundPaymentMetadata(TypedDict, total=False):
    coupon_code: str
    partner_id: int

class _CheckoutReversePaymentMetadata(TypedDict, total=False):
    coupon_code: str
    partner_id: int

class CheckoutConnector:
    """Checkout connector ().

    Provides 12 tools.
    """

    def checkout_create_instrument(
        self,
        country: str,
        currency: str,
        customer: _CheckoutCreateInstrumentCustomer,
        cvv: str,
        env: str,
        expiry_month: int,
        expiry_year: int,
        number: str,
        processing_channel_id: str,
        type: str,
    ) -> Dict[str, Any]:
        """Creates and saves a new payment instrument (e.g., a tokenized credit card or bank account) in Checkout.com. Use this to store a customers payment method for future use. Do not use this to process an immediate payment — use checkout_create_payment instead.

        Args:
            country: Cardholder's country. (required)
            currency: Transaction currency. (required)
            customer: Details about the customer. (required)
            cvv: Card verification value (CVV). (required)
            env: Environment (e.g., sandbox, production). (required)
            expiry_month: Card expiry month (numerical). (required)
            expiry_year: Card expiry year (numerical). (required)
            number: Card number. (required)
            processing_channel_id: ID of the processing channel. (required)
            type: Type of card. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def checkout_create_payment(
        self,
        amount: int,
        currency: str,
        env: str,
        processing_channel_id: str,
        reference: str,
        source: _CheckoutCreatePaymentSource,
    ) -> Dict[str, Any]:
        """Initiates and processes a new payment transaction in Checkout.com. Use this to charge a customer via card, token, or other supported payment source. This action has financial side effects — funds will be captured or authorized depending on the request parameters. To refund a payment, use checkout_refund_payment.

        Args:
            amount: Transaction amount. (required)
            currency: Transaction currency. (required)
            env: Environment (e.g., sandbox, production). (required)
            processing_channel_id: ID of the processing channel. (required)
            reference: Reference for the transaction. (required)
            source: Payment source details. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def checkout_create_workflow(
        self,
        actions: List[Any],
        active: bool,
        conditions: List[Any],
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new automation workflow in Checkout.com that triggers actions based on payment events (e.g., send a webhook when a payment is captured). Use this to configure event-driven automation rules. Do not use this to list existing workflows — use checkout_list_workflows instead.

        Args:
            actions:  (required)
            active: Indicates if the entity is active. (required)
            conditions:  (required)
            name: Name of the entity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def checkout_delete_instrument(
        self,
        env: str,
        instrumentId: str,
    ) -> Dict[str, Any]:
        """Permanently removes a saved payment instrument (e.g., a tokenized card or bank account) from Checkout.com by instrument ID. Use this when a customer removes a saved payment method. This action is irreversible — the instrument token will no longer be usable for future payments.

        Args:
            env: Environment for the API request (e.g., sandbox, production). (required)
            instrumentId: ID of the payment instrument. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def checkout_get_instrument(
        self,
        env: str,
        instrumentId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific saved payment instrument from Checkout.com by instrument ID, such as card type, expiry, and billing details. Use this to inspect or verify a stored payment method before charging. Do not use this to list all instruments.

        Args:
            env: Environment for the checkout.com API request (e.g., sandbox, production). (required)
            instrumentId: ID of the payment instrument. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def checkout_get_payment(
        self,
        env: str,
        paymentId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single payment in Checkout.com by payment ID, including its status, amount, currency, and customer details. Use this to inspect or verify the state of a known transaction. To list all payment actions on a transaction, use checkout_list_payment_actions instead.

        Args:
            env: Environment for the checkout.com API (e.g., sandbox, production). (required)
            paymentId: Payment ID for the checkout.com API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def checkout_list_disputes(
        self,
        entity_ids: Optional[str] = None,
        from: Optional[str] = None,
        id: Optional[str] = None,
        limit: Optional[str] = None,
        payment_arn: Optional[str] = None,
        payment_id: Optional[str] = None,
        payment_mcc: Optional[str] = None,
        payment_reference: Optional[str] = None,
        processing_channel_ids: Optional[str] = None,
        skip: Optional[str] = None,
        statuses: Optional[str] = None,
        sub_entity_ids: Optional[str] = None,
        this_channel_only: Optional[str] = None,
        to: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of payment disputes (chargebacks and retrievals) filed against transactions in Checkout.com. Use this to monitor and manage dispute cases. Does not resolve or respond to disputes — this is a read-only operation.

        Args:
            entity_ids: Comma-separated list of entity IDs.
            from: Start date for filtering payments (timestamp).
            id: ID of the entity.
            limit: Maximum number of records to return.
            payment_arn: Amazon Resource Name (ARN) of the payment.
            payment_id: ID of the payment.
            payment_mcc: Merchant Category Code (MCC) of the payment.
            payment_reference: Reference ID of the payment.
            processing_channel_ids: Comma-separated list of processing channel IDs.
            skip: Number of records to skip for pagination.
            statuses: Comma-separated list of payment statuses to filter by.
            sub_entity_ids: Comma-separated list of sub-entity IDs.
            this_channel_only: Filter payments to only include those processed through the current channel.
            to: End date for filtering payments (timestamp).
        Returns:
            API response as a dictionary.
        """
        ...

    def checkout_list_payment_actions(
        self,
        env: str,
        paymentId: str,
    ) -> Dict[str, Any]:
        """Returns the list of actions (e.g., authorization, capture, refund, void) that have been performed on a specific payment in Checkout.com, identified by payment ID. Use this to audit the full lifecycle of a payment transaction. This is a read-only operation with no side effects. Note: despite the tool name getPaymentOptions, this endpoint retrieves payment actions, not checkout options.

        Args:
            env: Environment (e.g., sandbox, production). (required)
            paymentId: ID of the payment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def checkout_list_payment_methods(
        self,
        env: str,
        processing_channel_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns the list of payment methods (e.g., Visa, Mastercard, PayPal) accepted by your Checkout.com account configuration. Use this to present available options to customers before checkout. This is a read-only operation with no side effects.

        Args:
            env: Environment for the API request (e.g., sandbox, production). (required)
            processing_channel_id: ID of the processing channel.
        Returns:
            API response as a dictionary.
        """
        ...

    def checkout_list_workflows(
        self,
        env: str,
    ) -> Dict[str, Any]:
        """Returns a list of all automation workflows configured in Checkout.com, including their trigger events and associated actions. Use this to review or audit existing payment automation rules. This is a read-only operation with no side effects.

        Args:
            env: Environment setting for the Checkout.com API (e.g., sandbox, production). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def checkout_refund_payment(
        self,
        CkoIdempotencyKey: str,
        amount: int,
        destination: _CheckoutRefundPaymentDestination,
        env: str,
        paymentId: str,
        reference: str,
        amount_allocations: Optional[List[Any]] = None,
        capture_action_id: Optional[str] = None,
        items: Optional[List[Any]] = None,
        metadata: Optional[_CheckoutRefundPaymentMetadata] = None,
    ) -> Dict[str, Any]:
        """Initiates a full or partial refund for a captured payment in Checkout.com by payment ID. Use this after a payment has already been settled and funds need to be returned to the customer. This action has financial side effects. For pre-settlement cancellations, use checkout_reverse_payment instead.

        Args:
            CkoIdempotencyKey: Idempotency key for the request. (required)
            amount: Amount of the payment. (required)
            destination: Destination account details for the payment. (required)
            env: Environment. (required)
            paymentId: Payment ID. (required)
            reference: Reference for the payment. (required)
            amount_allocations: 
            capture_action_id: Capture action ID.
            items: 
            metadata: Metadata associated with the payment.
        Returns:
            API response as a dictionary.
        """
        ...

    def checkout_reverse_payment(
        self,
        CkoIdempotencyKey: str,
        env: str,
        metadata: _CheckoutReversePaymentMetadata,
        paymentId: str,
        reference: str,
    ) -> Dict[str, Any]:
        """Reverses a previously authorized or captured payment in Checkout.com by payment ID, voiding the transaction. Use this to cancel a payment before settlement. This action is irreversible and has financial side effects — funds will be returned to the payer. For post-settlement cancellations, use checkout_refund_payment instead.

        Args:
            CkoIdempotencyKey: Idempotency key for the request. (required)
            env: Environment (e.g., sandbox, production). (required)
            metadata: Metadata associated with the transaction. (required)
            paymentId: Payment ID. (required)
            reference: Reference for the transaction. (required)
        Returns:
            API response as a dictionary.
        """
        ...

