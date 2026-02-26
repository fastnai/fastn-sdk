"""Fastn checkout connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class CheckoutConnector:
    """checkout connector ().

    Provides 12 tools.
    """

    def create_instruments(
        self,
        country: str,
        currency: str,
        customer: Dict[str, Any],
        cvv: str,
        expiry_month: int,
        expiry_year: int,
        number: str,
        processing_channel_id: str,
        type: str,
    ) -> Dict[str, Any]:
        """Creates new instruments for handling payments, such as credit cards or bank accounts, in the payment processing system.

        Args:
            country: Cardholder's country. (required)
            currency: Transaction currency. (required)
            customer: Details about the customer. (required)
            cvv: Card verification value (CVV). (required)
            expiry_month: Card expiry month (numerical). (required)
            expiry_year: Card expiry year (numerical). (required)
            number: Card number. (required)
            processing_channel_id: ID of the processing channel. (required)
            type: Type of card. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_payment(
        self,
        amount: int,
        currency: str,
        processing_channel_id: str,
        reference: str,
        source: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Processes a new payment transaction in the payment processing system.

        Args:
            amount: Transaction amount. (required)
            currency: Transaction currency. (required)
            processing_channel_id: ID of the processing channel. (required)
            reference: Reference for the transaction. (required)
            source: Payment source details. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_workflow(
        self,
        actions: List[Any],
        active: bool,
        conditions: List[Any],
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new workflow for automating tasks related to payment processing in the system.

        Args:
            actions:  (required)
            active: Indicates if the entity is active. (required)
            conditions:  (required)
            name: Name of the entity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_instrument(
        self,
        env: str,
        instrumentId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified payment instrument from the payment processing system.

        Args:
            env: Environment for the API request (e.g., sandbox, production). (required)
            instrumentId: ID of the payment instrument. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_disputes(
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
        """Retrieves information about any disputes related to payment transactions in the payment processing system.

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

    def get_instrument(
        self,
        env: str,
        instrumentId: str,
    ) -> Dict[str, Any]:
        """Gets detailed information about a specific payment instrument in the payment processing system.

        Args:
            env: Environment for the checkout.com API request (e.g., sandbox, production). (required)
            instrumentId: ID of the payment instrument. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_payment_details(
        self,
        env: str,
        paymentId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific payment in the payment processing system.

        Args:
            env: Environment for the checkout.com API (e.g., sandbox, production). (required)
            paymentId: Payment ID for the checkout.com API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_payment_methods(
        self,
        processing_channel_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains a list of accepted payment methods within the payment processing system.

        Args:
            processing_channel_id: ID of the processing channel.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_payment_options(
        self,
        env: str,
        paymentId: str,
    ) -> Dict[str, Any]:
        """Fetches the available payment options offered to customers during the checkout process in the payment platform.

        Args:
            env: Environment (e.g., sandbox, production). (required)
            paymentId: ID of the payment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workflows(
        self,
        env: str,
    ) -> Dict[str, Any]:
        """Fetches a list of workflows related to payment processing that have been set up in the system.

        Args:
            env: Environment setting for the Checkout.com API (e.g., sandbox, production). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def refund_payment(
        self,
        CkoIdempotencyKey: str,
    ) -> Dict[str, Any]:
        """Initiates a refund for a specific payment transaction in the payment processing system.

        Args:
            CkoIdempotencyKey: Idempotency key for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def reverse_payment(
        self,
        CkoIdempotencyKey: str,
    ) -> Dict[str, Any]:
        """Reverses a completed payment transaction, effectively canceling it in the payment processing system.

        Args:
            CkoIdempotencyKey: Idempotency key for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

