"""Fastn Stripe connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class StripeConnector:
    """Stripe connector ().

    Provides 40 tools.
    """

    def stripe_capture_charge(
        self,
        chargeId: str,
    ) -> Dict[str, Any]:
        """Captures a previously authorized but uncaptured Stripe charge, completing the payment and transferring funds. Only charges with capture_method set to manual can be captured. Use this tool to finalize a payment after an authorization hold. This action triggers an actual funds transfer and is irreversible. Do not use this tool on charges that have already been captured or on charges created with automatic capture.

        Args:
            chargeId: Charge ID for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_create_charge(
        self,
        amount: str,
        currency: str,
        source: str,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Stripe charge to collect payment from a customer using a payment source such as a card token or payment method ID. Requires an amount, currency, and payment source. This immediately attempts to collect payment and is irreversible once captured. Use this tool for one-time payments. Do not use this tool for subscription-based billing — use stripe_create_subscription_single_item instead.

        Args:
            amount: Amount of the payment in the smallest currency unit. (required)
            currency: Three-letter ISO currency code. (required)
            source: Identifier of the payment source (e.g., credit card token). (required)
            description: Description of the payment.
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_create_customer(
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
        """Creates a new customer record in Stripe with details such as name, email, phone, and billing address. Use this tool when onboarding a new customer who will be billed, subscribed, or invoiced through Stripe. Creating a customer enables attaching payment methods and generating invoices. Do not use this tool to update an existing customer — use stripe_update_customer instead.

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

    def stripe_create_invoice(
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
        """Creates a new draft invoice in Stripe. A customer ID must be provided. The invoice is created in draft status and can have line items added before being finalized. Use this tool as the starting point for generating a new invoice for a customer. Do not use this tool to add charges to the invoice — use stripe_create_invoice_item after creating the invoice.

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

    def stripe_create_invoice_item(
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
        """Adds a line item to a Stripe customers pending invoice or to a specific draft invoice. Requires a customer ID and amount. Invoice items are accumulated and included in the next invoice created for the customer, or can be explicitly attached to a draft invoice. Use this tool before finalizing an invoice when you need to add individual charges. Do not use this tool to create the invoice itself — use stripe_create_invoice instead.

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

    def stripe_create_invoice_with_customer_id(
        self,
        customer: str,
    ) -> Dict[str, Any]:
        """Creates a new draft Stripe invoice explicitly linked to a specific customer by their customer ID. Use this tool when you need to ensure the invoice is associated with a known customer ID at creation time. The invoice is created in draft status. Do not use this tool to add line items — use stripe_create_invoice_item after creating the invoice. Note: if stripe_create_invoice already accepts a customer ID, prefer using that tool to avoid duplication.

        Args:
            customer: Identifier for the customer in the Stripe system. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_create_price(
        self,
        currency: str,
        product: str,
        recurringinterval: str,
        unit_amount: str,
    ) -> Dict[str, Any]:
        """Creates a new price for an existing Stripe product, defining the currency, unit amount, and billing interval (one-time or recurring). Use this tool when setting up pricing for a product to be used in subscriptions, checkout sessions, or invoices. A product must exist before creating a price. Do not use this tool to create the product itself — use stripe_create_product first.

        Args:
            currency: Currency code (e.g., USD). (required)
            product: Product identifier. (required)
            recurringinterval: Recurring interval for subscription. (required)
            unit_amount: Unit amount for the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_create_product(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new product in your Stripe account with a name, description, and optional metadata. Products represent the goods or services you sell and must exist before creating associated prices. Use this tool when introducing a new item to your catalog. Do not use this tool to create pricing — use stripe_create_price after creating the product.

        Args:
            name: Name field for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_create_subscription_single_item(
        self,
        customer: Optional[str] = None,
        items0price: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Stripe subscription for a customer with a single price item. Requires an existing customer ID and a price ID. Use this tool when enrolling a customer in a single-plan recurring billing subscription. This immediately starts the subscription and may trigger an initial charge depending on the billing settings. Do not use this tool for subscriptions with multiple line items.

        Args:
            customer: Identifier for the customer.
            items0price: Price of the first item.
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_create_webhook(
        self,
        enabled_events: List[Any],
        url: str,
        api_version: Optional[str] = None,
        description: Optional[str] = None,
        metadata: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Registers a new webhook endpoint in your Stripe account to receive event notifications at a specified URL. You must provide the destination URL and the list of Stripe event types to subscribe to. Use this tool when setting up a new integration that needs to listen to Stripe events. Do not use this tool to modify an existing webhook — use stripe_update_webhook instead.

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

    def stripe_delete_draft_invoice(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a Stripe invoice that is still in draft status. Only draft invoices can be deleted. Once deleted, the invoice cannot be recovered. Use this tool when a draft invoice was created in error or is no longer needed. Do not use this tool on finalized invoices — use stripe_void_invoice to cancel those instead.

        Args:
            invoiceId: ID of the invoice. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_delete_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a Stripe webhook endpoint by its ID. Once deleted, Stripe will stop sending event notifications to that endpoint. This action is irreversible. Use this tool only when you intend to permanently remove a webhook. Do not use this tool to temporarily disable a webhook — use stripe_update_webhook to deactivate it instead.

        Args:
            webhookId: Webhook ID for the Stripe API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_finalize_invoice(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Finalizes a Stripe draft invoice, locking its contents and making it ready for payment. Once finalized, the invoice can no longer be edited and transitions from draft to open status. Use this tool after all line items have been added to a draft invoice. Do not use this tool if you still need to modify the invoice — finalization is irreversible.

        Args:
            invoiceId: ID of the invoice for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_get_account(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the details of the authenticated Stripe account, including business profile, settings, capabilities, and payout configuration. Use this tool to inspect the current accounts configuration or verify account status. This returns the account associated with the API key in use, not a specific customer account.
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_get_balance(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the current balance of the authenticated Stripe account, including available funds, pending amounts, and currency breakdowns. Use this tool to check how much money is available for payouts or to monitor funds in transit. This reflects the balance for the account associated with the API key in use.
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_get_charge(
        self,
        chargeId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Stripe charge by its ID, including amount, currency, status, payment method details, and any associated refunds. Use this tool when you need to inspect a single known charge. Do not use this tool to browse multiple charges — use stripe_list_charges or stripe_search_charges instead.

        Args:
            chargeId: ID of the charge for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_get_checkout_session(
        self,
        checkoutSessionId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific Stripe Checkout session by its ID, including payment status, line items, customer information, and mode (payment, subscription, or setup). Use this tool to verify the outcome of a checkout flow or inspect session metadata. Do not use this tool to create a new checkout session.

        Args:
            checkoutSessionId: Checkout Session ID for Stripe. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_get_customer(
        self,
        customerId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Stripe customer by their customer ID, including name, email, phone, billing address, and attached payment methods. Use this tool when you need to inspect or display a single known customers profile. Do not use this tool to browse all customers — use stripe_list_customers instead.

        Args:
            customerId: Customer ID for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_get_invoice(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Stripe invoice by its ID, including status, line items, customer, due date, and payment details. Use this tool when you need to inspect or display a single known invoice. Do not use this tool to browse multiple invoices — use stripe_list_invoices or stripe_search_invoices instead.

        Args:
            invoiceId: ID of the invoice for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Stripe product by its product ID, including name, description, active status, and metadata. Use this tool when you need to inspect a single known product. Do not use this tool to browse all products — use stripe_list_products instead.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_get_tax_code(
        self,
        taxCode: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Stripe tax code by its ID, including its name and description of the tax treatment it represents. Use this tool when you need to confirm the details of a particular tax classification. Do not use this tool to browse all available tax codes — use stripe_list_tax_codes instead.

        Args:
            taxCode: Tax code associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_get_upcoming_invoice(
        self,
        customer: Optional[str] = None,
        schedule: Optional[str] = None,
        subscription: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a preview of the next upcoming invoice for a specific customer, including the total amount due, billing period, and applied discounts or credits. This does not create or finalize an invoice — it is a read-only preview. Use this tool to show customers what they will be charged at the next billing cycle. Do not use this tool to list individual line items — use stripe_list_upcoming_invoice_line_items instead.

        Args:
            customer: Customer related parameter.
            schedule: Schedule related parameter.
            subscription: Subscription related parameter.
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_get_webhook(
        self,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific Stripe webhook endpoint by its ID, including its URL, subscribed events, and enabled status. Use this tool when you need to inspect a single webhook configuration. Do not use this tool to list all webhooks — use stripe_list_webhooks instead.

        Args:
            webhookId: Webhook ID for the Stripe Stripe endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_list_charges(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists charges made in your Stripe account, with an optional limit on the number of results returned. Returns a paginated collection of charge records including amounts, statuses, and associated customers. Use this tool when you need to browse or audit charges in bulk. Do not use this tool to retrieve a single charge — use stripe_get_charge instead.

        Args:
            limit: Limit parameter for the Stripe API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_list_customers(
        self,
    ) -> Dict[str, Any]:
        """Lists all customers registered in your Stripe account, returning a paginated collection of customer records including name, email, and account details. Use this tool when you need to browse or audit customers in bulk. Do not use this tool to retrieve a single customer — use stripe_get_customer instead, or use stripe_search_customers to find customers matching specific criteria.
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_list_invoice_line_items(
        self,
        invoiceId: str,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all line items included in a specific Stripe invoice, identified by its invoice ID. Returns individual charge entries with amounts, descriptions, and quantities. Use this tool when you need the detailed breakdown of charges within a known invoice. Do not use this tool to retrieve the invoice summary — use stripe_get_invoice for that.

        Args:
            invoiceId: Invoice ID for the Stripe API request. (required)
            limit: Limit for the Stripe API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_list_invoices(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all invoices in your Stripe account, optionally filtered by customer, status, or date range. Returns a paginated collection of invoice records. Use this tool when you need to browse or audit invoices in bulk. Do not use this tool to retrieve a single invoice by ID — use stripe_get_invoice instead.

        Args:
            limit: Limit parameter for the Stripe API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_list_products(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all products defined in your Stripe account. Use this tool when you need to retrieve the full catalog of products, including their names, descriptions, active status, and metadata. Returns a paginated collection. Do not use this tool to retrieve a single product by ID — use stripe_get_product instead.

        Args:
            limit: Limit for the Stripe API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_list_tax_codes(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all tax codes available in Stripes tax classification system. Tax codes are used to assign the correct tax treatment to products and services. Use this tool when you need to find the appropriate tax code to assign to a product. Returns a paginated collection. Do not use this tool to retrieve a single tax code by ID — use stripe_get_tax_code instead.

        Args:
            limit: Limit the number of results returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_list_upcoming_invoice_line_items(
        self,
        customer: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists the individual line items that will appear on a customers next upcoming invoice before it is finalized. Use this tool when you need to preview the detailed breakdown of charges on an upcoming invoice. Requires identifying the customer. Do not use this tool to view the upcoming invoice summary — use stripe_get_upcoming_invoice for that.

        Args:
            customer: Customer ID for the Stripe API request.
            limit: Limit for the Stripe API request (e.g., number of records).
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_list_webhooks(
        self,
        ending_before: Optional[str] = None,
        limit: Optional[str] = None,
        starting_after: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all webhook endpoints registered in your Stripe account, including their URLs, subscribed events, and status. Use this tool when you need to audit or review all configured webhooks. Returns a paginated collection. Do not use this tool to retrieve a single webhook by ID — use stripe_get_webhook instead.

        Args:
            ending_before: 
            limit: Limit parameter for the Stripe API request.
            starting_after: 
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_mark_invoice_uncollectible(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Marks a finalized Stripe invoice as uncollectible, indicating that payment is not expected. This changes the invoice status to uncollectible and stops further collection attempts. Use this tool for invoices related to bad debt or customers who cannot pay. This action is difficult to reverse. Do not use this tool to cancel an invoice — use stripe_void_invoice instead.

        Args:
            invoiceId: Invoice ID for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_pay_invoice(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Triggers immediate payment of a finalized Stripe invoice using the customers default payment method or a specified payment method. Use this tool to programmatically collect payment without waiting for the customer to pay manually. The invoice must be finalized before payment can be attempted. This action initiates a real charge. Do not use this tool to send the invoice to the customer for self-service payment — use stripe_send_invoice_for_manual_payment instead.

        Args:
            invoiceId: ID of the invoice for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_search_charges(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Searches for Stripe charges matching a specific query using Stripes search syntax, such as filtering by amount, currency, customer, or metadata. Use this tool when you need to find charges that meet particular conditions. Do not use this tool to list all charges without filters — use stripe_list_charges instead.

        Args:
            query: Query string for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_search_customers(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for Stripe customers matching specific criteria using Stripes search query syntax, such as filtering by email, name, or metadata fields. Use this tool when you need to find customers that match particular conditions rather than browsing all customers. Do not use this tool to list all customers without filters — use stripe_list_customers instead.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_search_invoices(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Searches for Stripe invoices matching specific criteria using Stripes search query syntax, such as filtering by customer, status, or metadata. Use this tool when you need to locate invoices that match particular conditions. Do not use this tool to list all invoices without filters — use stripe_list_invoices instead.

        Args:
            query: Query string parameters for the Stripe Stripe API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_send_invoice_for_manual_payment(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Sends a finalized Stripe invoice to the customer via email, prompting them to complete payment manually through the hosted invoice page. Use this tool when the customer needs to pay via a link rather than through automatic charge. The invoice must be finalized before sending. This triggers an email notification to the customer. Do not use this tool to automatically charge the customer — use stripe_pay_invoice instead.

        Args:
            invoiceId: ID of the invoice for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_update_charge(
        self,
        body: Dict[str, Any],
        chargeId: str,
    ) -> Dict[str, Any]:
        """Updates mutable properties of an existing Stripe charge by its ID, such as its description, metadata, or receipt email. Use this tool when you need to modify charge details after it has been created. Not all fields can be changed after creation. Do not use this tool to capture a charge — use stripe_capture_charge instead.

        Args:
            body: Request body for the Stripe API endpoint. (required)
            chargeId: ID of the charge. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_update_webhook(
        self,
        enabled_events: str,
        url: str,
        webhookId: str,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing Stripe webhook endpoint, such as its URL, enabled events, or active status. Requires the webhook endpoint ID. Use this tool when you need to modify a previously registered webhook. This operation overwrites the specified fields and takes effect immediately. Do not use this tool to create a new webhook — use stripe_create_webhook instead.

        Args:
            enabled_events: List of events to receive webhook notifications for. (required)
            url: URL to receive webhook notifications. (required)
            webhookId: Unique identifier for the webhook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stripe_void_invoice(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Voids a finalized Stripe invoice, permanently canceling it so it can no longer be paid. The invoice status is set to void and the customer is not charged. This action is irreversible. Use this tool when a finalized invoice was created in error or is no longer valid. Do not use this tool on draft invoices — use stripe_delete_draft_invoice instead.

        Args:
            invoiceId: ID of the invoice for the Stripe API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

