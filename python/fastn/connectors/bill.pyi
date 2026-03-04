"""Fastn Bill connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _BillCreateBillClassifications(TypedDict, total=False):
    chartOfAccountId: str

class _BillCreateBillInvoice(TypedDict, total=False):
    invoiceDate: str
    invoiceNumber: str

class _BillCreateCustomerBillingaddress(TypedDict, total=False):
    city: str
    country: str
    line1: str
    stateOrProvince: str
    zipOrPostalCode: str

class _BillCreateCustomerContact(TypedDict, total=False):
    firstName: str
    lastName: str

class _BillCreateInvoiceCustomer(TypedDict, total=False):
    email: str
    name: str

class _BillCreateSubscriptionStatus(TypedDict, total=False):
    enabled: bool

class _BillInviteCustomerToNetworkRppsinformation(TypedDict, total=False):
    accountNumber: str
    addressId: str

class _BillSendInvoiceRecipient(TypedDict, total=False):
    to: List[Any]

class _BillSendInvoiceReplyto(TypedDict, total=False):
    userId: str

class _BillUpdateBillClassifications(TypedDict, total=False):
    chartOfAccountId: str

class _BillUpdateBillInvoice(TypedDict, total=False):
    invoiceDate: str
    invoiceNumber: str

class _BillUpdateInvoiceCustomer(TypedDict, total=False):
    email: str
    name: str

class _BillUpdateSubscriptionStatus(TypedDict, total=False):
    enabled: bool

class BillConnector:
    """Bill connector ().

    Provides 27 tools.
    """

    def bill_create_bill(
        self,
        billLineItems: Optional[List[Any]] = None,
        classifications: Optional[_BillCreateBillClassifications] = None,
        description: Optional[str] = None,
        dueDate: Optional[str] = None,
        invoice: Optional[_BillCreateBillInvoice] = None,
        payFromChartOfAccountId: Optional[str] = None,
        vendorId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new bill (accounts payable record) in Bill.com representing an amount owed to a vendor. Use this tool when you need to record a new payable. Do not use this tool to update an existing bill; use bill_update_bill instead.

        Args:
            billLineItems: 
            classifications: Account classifications for the bill.
            description: Description of the bill.
            dueDate: Due date of the bill.
            invoice: Details of the related invoice.
            payFromChartOfAccountId: ID of the account to pay from.
            vendorId: ID of the vendor.
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_create_customer(
        self,
        accountType: Optional[str] = None,
        billingAddress: Optional[_BillCreateCustomerBillingaddress] = None,
        companyName: Optional[str] = None,
        contact: Optional[_BillCreateCustomerContact] = None,
        email: Optional[str] = None,
        name: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new customer record in Bill.com with contact information and payment terms. Use this tool when you need to add a new customer before creating invoices or sending invitations. Do not use this tool to update an existing customer. Note: after creating a customer, use bill_invite_customer_to_network to onboard them to the Bill.com network.

        Args:
            accountType: 
            billingAddress: 
            companyName: 
            contact: 
            email: 
            name: 
            phone: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_create_invoice(
        self,
        customer: Optional[_BillCreateInvoiceCustomer] = None,
        invoiceLineItems: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new invoice in Bill.com for a specified customer, including line items, amounts, and due date. Use this tool when you need to generate a new receivables invoice. Do not use this tool to update an existing invoice; use bill_update_invoice instead. Note: creating an invoice does not automatically send it to the customer; use bill_send_invoice for that.

        Args:
            customer: Customer details for the invoice.
            invoiceLineItems: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_create_invoice_payment_link(
        self,
        customerId: str,
        email: str,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Generates a shareable payment link for a specific invoice in Bill.com, identified by its invoiceId, allowing the customer to pay online. Use this tool when you need to provide a customer with a direct URL to pay an invoice. Do not use this tool to send the invoice via email; use bill_send_invoice instead. Note: bill_get_payment_link calls the same endpoint and should not be used alongside this tool for the same invoice.

        Args:
            customerId:  (required)
            email:  (required)
            invoiceId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_create_payment_link(
        self,
        customerId: Optional[str] = None,
        email: Optional[str] = None,
        invoiceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a shareable payment link for a specific invoice in Bill.com, identified by its invoiceId. Use this tool when you need a standalone payment URL for an invoice. Note: this tool calls the same endpoint as bill_create_invoice_payment_link; prefer using bill_create_invoice_payment_link for invoice-specific payment link generation to avoid duplication.

        Args:
            customerId: 
            email: 
            invoiceId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_create_subscription(
        self,
        XIdempotentKey: str,
        events: Optional[List[Any]] = None,
        name: Optional[str] = None,
        notificationUrl: Optional[str] = None,
        status: Optional[_BillCreateSubscriptionStatus] = None,
    ) -> Dict[str, Any]:
        """Creates a new event subscription in Bill.com to receive webhook notifications for specified event types. Use this tool when you want to register a new endpoint to listen for Bill.com events. Do not use this tool to update an existing subscription; use bill_update_subscription instead.

        Args:
            XIdempotentKey: Idempotent key for request deduplication. (required)
            events: 
            name: Name for the webhook.
            notificationUrl: URL to receive notifications.
            status: Status of the webhook.
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_delete_subscription(
        self,
        subscriptionId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing event subscription in Bill.com, identified by its subscriptionId. Use this tool when you need to stop receiving event notifications for a specific subscription. Do not use this tool to temporarily pause a subscription; use bill_update_subscription to modify it instead. This action is irreversible — the subscription cannot be recovered after deletion.

        Args:
            subscriptionId: Subscription ID for identifying the Bill.com account. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_get_bill_details(
        self,
        billId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific bill in Bill.com, identified by its billId, including vendor, amounts, due date, and payment status. Use this tool when you need the full record of a single bill. Do not use this tool to list all bills; use bill_list_bills instead.

        Args:
            billId: ID of the bill. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_get_customer(
        self,
        customerId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of an existing customer in Bill.com, identified by their customerId, including contact information, payment terms, and status. Use this tool when you need the full profile of a single customer. Do not use this tool to create a customer; use bill_create_customer instead.

        Args:
            customerId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_get_events_catalog(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the catalog of all available event types in Bill.com that can be subscribed to via webhooks or event subscriptions. Use this tool to discover which events are supported before creating a subscription. Do not use this tool to retrieve existing subscriptions; use bill_list_subscriptions instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_get_invoice_details(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific invoice in Bill.com, identified by its invoiceId, including line items, amounts, status, and customer details. Use this tool when you need the full record of a single invoice. Do not use this tool to list all invoices; use bill_list_invoices instead.

        Args:
            invoiceId: The ID of the invoice. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_get_organization(
        self,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about the authenticated organization in Bill.com, including name, address, and configuration. Use this tool when you need to inspect the current organizations profile. Do not use this tool to search for other organizations; use bill_search_organizations instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_get_session_detail(
        self,
    ) -> Dict[str, Any]:
        """Retrieves details about the current authenticated session in Bill.com, including session status and associated user or organization context. Use this tool to inspect or validate an active session. Do not use this tool to create a new session or log in; use the login tool instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_get_subscription_details(
        self,
        subscriptionId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific event subscription in Bill.com, identified by its subscriptionId. Use this tool when you need the configuration or status of a single subscription. Do not use this tool to list all subscriptions; use bill_list_subscriptions instead.

        Args:
            subscriptionId: Your Bill.com subscription ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_get_vendor_payment_options(
        self,
        amount: Optional[str] = None,
        vendorId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the available payment options (e.g., ACH, check, virtual card) that can be used to pay vendors in Bill.com. Use this tool before initiating a vendor payment to determine which payment methods are available. Do not use this tool to execute a payment or to retrieve customer payment options.

        Args:
            amount: Amount for the Bill.com API request.
            vendorId: Vendor ID for the Bill.com API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_invite_customer_to_network(
        self,
        customerId: str,
        networkId: str,
        networkType: str,
        rppsInformation: Optional[_BillInviteCustomerToNetworkRppsinformation] = None,
    ) -> Dict[str, Any]:
        """Sends an invitation to an existing customer in Bill.com to join the Bill.com network, enabling electronic payments and collaboration. Use this tool when a customer has been created and you want to onboard them to the network. Do not use this tool to invite vendors or to create a new customer; use bill_create_customer first. This action triggers an outbound invitation email to the customer.

        Args:
            customerId: ID of the customer. (required)
            networkId: Identifier for the network. (required)
            networkType: Type of the network. (required)
            rppsInformation: Information related to RPPS.
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_list_bills(
        self,
        filters: Optional[str] = None,
        max: Optional[str] = None,
        page: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all bills (accounts payable records) in Bill.com. Use this tool when you need a summary or full listing of bills across vendors. Do not use this tool to retrieve details of a single bill; use bill_get_bill_details instead.

        Args:
            filters: 
            max: 
            page: 
            sort: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_list_invoices(
        self,
        filters: Optional[str] = None,
        max: Optional[str] = None,
        page: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all invoices in Bill.com. Use this tool when you need a summary or full listing of invoices across customers. Do not use this tool to retrieve details of a single invoice; use bill_get_invoice_details instead.

        Args:
            filters: Filters for the Bill.com API request.
            max: Maximum number of results to return.
            page: Page number for pagination.
            sort: Sort order for the results.
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_list_subscriptions(
        self,
        max: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all event subscriptions registered in Bill.com. Use this tool when you need an overview of all active or inactive subscriptions. Do not use this tool to retrieve details of a single subscription; use bill_get_subscription_details instead.

        Args:
            max: The maximum number of results to return.
            page: The page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_login(
        self,
        devKey: str,
        organizationId: str,
        password: str,
        stage: str,
        username: str,
    ) -> Dict[str, Any]:
        """Authenticates a user and establishes a new session in Bill.com, returning a session token required for subsequent API calls. Use this tool before calling any other Bill.com tool that requires authentication. Do not use this tool if a valid session is already active; use bill_get_session_detail to verify an existing session. Note: credentials are transmitted securely but ensure sessions are terminated using bill_logout when no longer needed.

        Args:
            devKey:  (required)
            organizationId:  (required)
            password:  (required)
            stage:  (required)
            username:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_logout(
        self,
    ) -> Dict[str, Any]:
        """Logs out the currently authenticated user from Bill.com, terminating the active session. Use this tool when you need to end a session explicitly. Do not use this tool to switch users or to start a new session; use the login tool for authentication. This action is irreversible — the current session token will be invalidated immediately.
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_search_organizations(
        self,
        accountNumber: Optional[str] = None,
        name: Optional[str] = None,
        scope: Optional[str] = None,
        zipOrPostalCode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for organizations in the Bill.com network based on specified criteria such as name or contact details. Use this tool to find and identify external organizations before sending invitations or initiating transactions. Do not use this tool to retrieve details of your own organization; use bill_get_organization instead.

        Args:
            accountNumber: Account number.
            name: Name parameter.
            scope: Scope of the request.
            zipOrPostalCode: Zip or postal code.
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_send_invoice(
        self,
        invoiceId: str,
        recipient: _BillSendInvoiceRecipient,
        replyTo: _BillSendInvoiceReplyto,
    ) -> Dict[str, Any]:
        """Sends an existing invoice to a customer via email in Bill.com, identified by its invoiceId. Use this tool after creating an invoice when you are ready to deliver it to the customer. Do not use this tool to create a new invoice; use bill_create_invoice first. This action triggers an outbound email to the customer and cannot be unsent.

        Args:
            invoiceId: ID of the invoice. (required)
            recipient: Details of the recipient(s). (required)
            replyTo: Details of the reply-to recipient. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_update_bill(
        self,
        billId: Optional[str] = None,
        billLineItems: Optional[List[Any]] = None,
        classifications: Optional[_BillUpdateBillClassifications] = None,
        description: Optional[str] = None,
        dueDate: Optional[str] = None,
        invoice: Optional[_BillUpdateBillInvoice] = None,
        payFromChartOfAccountId: Optional[str] = None,
        vendorId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing bill (accounts payable record) in Bill.com, identified by its billId, such as amounts, due date, or vendor information. Use this tool when you need to modify a previously created bill. Do not use this tool to create a new bill; use bill_create_bill instead. This operation partially overwrites existing bill fields.

        Args:
            billId: 
            billLineItems: 
            classifications: 
            description: 
            dueDate: 
            invoice: 
            payFromChartOfAccountId: 
            vendorId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_update_invoice(
        self,
        customer: Optional[_BillUpdateInvoiceCustomer] = None,
        invoiceId: Optional[str] = None,
        invoiceLineItems: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing invoice in Bill.com, such as line items, due date, or customer information. Use this tool when you need to modify a previously created invoice identified by its invoiceId. Do not use this tool to create a new invoice or to send an invoice to a customer. This operation partially overwrites existing invoice fields and cannot be undone without a subsequent update.

        Args:
            customer: 
            invoiceId: 
            invoiceLineItems: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bill_update_subscription(
        self,
        events: Optional[List[Any]] = None,
        name: Optional[str] = None,
        notificationUrl: Optional[str] = None,
        status: Optional[_BillUpdateSubscriptionStatus] = None,
        subscriptionId: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing event subscription in Bill.com, identified by its subscriptionId, such as the endpoint URL or subscribed event types. Use this tool when you need to modify a subscription without deleting and recreating it. Do not use this tool to create a new subscription; use bill_create_subscription instead.

        Args:
            events: 
            name: 
            notificationUrl: 
            status: 
            subscriptionId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of users in the system.
        Returns:
            API response as a dictionary.
        """
        ...

