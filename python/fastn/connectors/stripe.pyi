"""Fastn Stripe connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class StripeConnector:
    """Stripe connector ().

    Provides 40 tools.
    """

    def capture_charge(
        self,
        chargeId: str,
    ) -> Dict[str, Any]:
        """Captures funds for a given charge in the payment processing system.

        Args:
            chargeId: Charge ID for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_charge(
        self,
        amount: str,
        currency: str,
        source: str,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new charge for a customer in the payment processing system.

        Args:
            amount: Amount of the payment in the smallest currency unit. (required)
            currency: Three-letter ISO currency code. (required)
            source: Identifier of the payment source (e.g., credit card token). (required)
            description: Description of the payment.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_customer(
        self,
        balance: Optional[str] = None,
        cash_balance: Optional[str] = None,
        coupon: Optional[str] = None,
        description: Optional[str] = None,
        email: Optional[str] = None,
        invoice_prefix: Optional[str] = None,
        invoice_settings: Optional[str] = None,
        metadata: Optional[str] = None,
        name: Optional[str] = None,
        next_invoice_sequence: Optional[str] = None,
        payment_method: Optional[str] = None,
        phone: Optional[str] = None,
        preferred_locales: Optional[str] = None,
        promotion_code: Optional[str] = None,
        shipping: Optional[str] = None,
        source: Optional[str] = None,
        tax_exempt: Optional[str] = None,
        test_clock: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new customer in the customer management system.

        Args:
            balance: Customer's balance.
            cash_balance: Customer's cash balance.
            coupon: Coupon code to apply.
            description: Description of the request.
            email: Customer's email address.
            invoice_prefix: Prefix for invoice numbers.
            invoice_settings: Settings related to invoices.
            metadata: Additional metadata for the request.
            name: Customer's name.
            next_invoice_sequence: Sequence number for the next invoice.
            payment_method: Customer's payment method.
            phone: Customer's phone number.
            preferred_locales: Customer's preferred locales.
            promotion_code: Promotion code to apply.
            shipping: Shipping information.
            source: Payment source details.
            tax_exempt: Indicates if the customer is tax-exempt.
            test_clock: Test clock settings.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_invoice(
        self,
        account_tax_ids: Optional[str] = None,
        application_fee_amount: Optional[str] = None,
        automatic_tax: Optional[str] = None,
        collection_method: Optional[str] = None,
        currency: Optional[str] = None,
        custom_fields: Optional[str] = None,
        customer: Optional[str] = None,
        days_until_due: Optional[str] = None,
        default_source: Optional[str] = None,
        default_tax_rates: Optional[str] = None,
        description: Optional[str] = None,
        discounts: Optional[str] = None,
        due_date: Optional[str] = None,
        effective_at: Optional[str] = None,
        footer: Optional[str] = None,
        from_invoice: Optional[str] = None,
        metadata: Optional[str] = None,
        on_behalf_of: Optional[str] = None,
        payment_settings: Optional[str] = None,
        pending_invoice_items_behaviour: Optional[str] = None,
        rendering: Optional[str] = None,
        shipping_cost: Optional[str] = None,
        shipping_details: Optional[str] = None,
        statement_descriptor: Optional[str] = None,
        subscription: Optional[str] = None,
        transfer_data: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new invoice in the billing system.

        Args:
            account_tax_ids: Tax IDs for the account.
            application_fee_amount: Amount of application fee.
            automatic_tax: Settings for automatic tax calculation.
            collection_method: Method for collecting payment.
            currency: Three-letter ISO currency code.
            custom_fields: Custom fields for the invoice.
            customer: ID of the customer.
            days_until_due: Number of days until the invoice is due.
            default_source: Default payment source for the invoice.
            default_tax_rates: Default tax rates for the invoice.
            description: Description of the invoice.
            discounts: Discounts applied to the invoice.
            due_date: Due date of the invoice.
            effective_at: Date and time when the invoice becomes effective.
            footer: Text to appear in the footer of the invoice.
            from_invoice: ID of the invoice to clone.
            metadata: Arbitrary metadata related to the invoice.
            on_behalf_of: ID of the connected account to create the invoice on behalf of.
            payment_settings: Payment settings for the invoice.
            pending_invoice_items_behaviour: How to handle pending invoice items.
            rendering: Rendering options for the invoice.
            shipping_cost: Shipping cost for the invoice.
            shipping_details: Shipping details for the invoice.
            statement_descriptor: Text that appears on the customer's statement.
            subscription: ID of the subscription this invoice is for.
            transfer_data: Data for transferring funds to a connected account.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_invoice_item(
        self,
        amount: str,
        currency: str,
        customer: str,
        invoice: str,
        price: str,
        quantity: str,
        unit_amount: str,
        unit_amount_decimal: str,
    ) -> Dict[str, Any]:
        """Creates an itemized entry for an invoice in the billing system.

        Args:
            amount: Amount for the Stripe transaction. (required)
            currency: Currency for the Stripe transaction. (required)
            customer: Customer ID associated with the Stripe transaction. (required)
            invoice: Invoice ID associated with the Stripe transaction. (required)
            price: Price of the item for the Stripe transaction. (required)
            quantity: Quantity of items for the Stripe transaction. (required)
            unit_amount: Unit amount for the Stripe transaction. (required)
            unit_amount_decimal: Unit amount in decimal format for the Stripe transaction. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_invoice_with_customer_id(
        self,
        customer: str,
    ) -> Dict[str, Any]:
        """Creates a new invoice associated with a specific customer in the billing system.

        Args:
            customer: Identifier for the customer in the Stripe system. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_price(
        self,
        currency: str,
        product: str,
        recurringinterval: str,
        unit_amount: str,
    ) -> Dict[str, Any]:
        """Creates a new pricing structure for a product in the system.

        Args:
            currency: Currency code (e.g., USD). (required)
            product: Product identifier. (required)
            recurringinterval: Recurring interval for subscription. (required)
            unit_amount: Unit amount for the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new product in the system for sale.

        Args:
            name: Name field for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_subscription_single_item(
        self,
        customer: Optional[str] = None,
        items0price: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a single item subscription for a customer in the subscription management system.

        Args:
            customer: Identifier for the customer.
            items0price: Price of the first item.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_webhook(
        self,
        enabled_events: List[Any],
        url: str,
        api_version: Optional[str] = None,
        description: Optional[str] = None,
        metadata: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook for receiving notifications from the system.

        Args:
            enabled_events:  (required)
            url: URL to send webhook events to. (required)
            api_version: 
            description: 
            metadata: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_draft_invoice(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Deletes a draft invoice in the billing system.

        Args:
            invoiceId: ID of the invoice. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing webhook from the system.

        Args:
            webhookId: Webhook ID for the Stripe API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def finalize_invoice(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Finalizes an invoice, making it ready for payment in the billing system.

        Args:
            invoiceId: ID of the invoice for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_account(
        self,
    ) -> Dict[str, Any]:
        """Retrieves account information associated with a customer in the account management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_balance(
        self,
    ) -> Dict[str, Any]:
        """Checks the balance of the account within the payment processing system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_charge(
        self,
        chargeId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific charge in the payment processing system.

        Args:
            chargeId: ID of the charge for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_charges(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all charges made in the payment processing system.

        Args:
            limit: Limit parameter for the Stripe API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_checkout_session(
        self,
        checkoutSessionId: str,
    ) -> Dict[str, Any]:
        """Fetches details about a specific checkout session in the e-commerce platform.

        Args:
            checkoutSessionId: Checkout Session ID for Stripe. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer(
        self,
        customerId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific customer in the system.

        Args:
            customerId: Customer ID for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customers(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of all customers registered in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_invoice(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific invoice in the billing system.

        Args:
            invoiceId: ID of the invoice for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_invoice_line_items(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of line items included in a specific invoice in the billing system.

        Args:
            limit: Limit for the Stripe API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_invoices(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all invoices in the billing system.

        Args:
            limit: Limit parameter for the Stripe API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific product in the system.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all products available in the system.

        Args:
            limit: Limit for the Stripe API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tax_code(
        self,
        taxCode: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific tax code in the tax management system.

        Args:
            taxCode: Tax code associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tax_codes(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all tax codes available in the tax management system.

        Args:
            limit: Limit the number of results returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_upcoming_invoice(
        self,
        customer: Optional[str] = None,
        schedule: Optional[str] = None,
        subscription: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details about an upcoming invoice for a customer in the billing system.

        Args:
            customer: Customer related parameter.
            schedule: Schedule related parameter.
            subscription: Subscription related parameter.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_upcoming_invoices_line_items(
        self,
        customer: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves line items from the upcoming invoices in the billing system.

        Args:
            customer: Customer ID for the Stripe API request.
            limit: Limit for the Stripe API request (e.g., number of records).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Retrieves details about a specific webhook in the system.

        Args:
            webhookId: Webhook ID for the Stripe Stripe endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhooks(
        self,
        ending_before: Optional[str] = None,
        limit: Optional[str] = None,
        starting_after: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all webhooks registered in the system.

        Args:
            ending_before: 
            limit: Limit parameter for the Stripe API request.
            starting_after: 
        Returns:
            API response as a dictionary.
        """
        ...

    def mark_invoice_uncollectible(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Marks an invoice as uncollectible in the billing system.

        Args:
            invoiceId: Invoice ID for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def pay_invoice(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Processes payment for an invoice in the billing system.

        Args:
            invoiceId: ID of the invoice for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def search_charges(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Searches for specific charges in the payment processing system based on query parameters.

        Args:
            query: Query string for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def search_customers(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for customers based on specific criteria in the system.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

    def search_invoices(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Searches for specific invoices in the billing system based on query parameters.

        Args:
            query: Query string parameters for the Stripe Stripe API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def send_invoice_for_manual_payment(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Sends an invoice for manual payment review in the billing system.

        Args:
            invoiceId: ID of the invoice for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_charge(
        self,
    ) -> Dict[str, Any]:
        """Updates the details of an existing charge in the payment processing system.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_webhook(
        self,
        enabled_events: str,
        url: str,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing webhook in the system.

        Args:
            enabled_events: List of events to receive webhook notifications for. (required)
            url: URL to receive webhook notifications. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def void_an_invoice(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Voids an existing invoice, marking it as canceled in the billing system.

        Args:
            invoiceId: ID of the invoice for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

