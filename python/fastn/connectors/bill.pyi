"""Fastn Bill connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BillConnector:
    """Bill connector ().

    Provides 27 tools.
    """

    def create_bill(
        self,
        billLineItems: Optional[List[Any]] = None,
        classifications: Optional[Dict[str, Any]] = None,
        description: Optional[str] = None,
        dueDate: Optional[str] = None,
        invoice: Optional[Dict[str, Any]] = None,
        payFromChartOfAccountId: Optional[str] = None,
        vendorId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new bill in the system.

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

    def create_customer(
        self,
        accountType: Optional[str] = None,
        billingAddress: Optional[Dict[str, Any]] = None,
        companyName: Optional[str] = None,
        contact: Optional[Dict[str, Any]] = None,
        email: Optional[str] = None,
        name: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new customer in the system.

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

    def create_invoice(
        self,
        customer: Optional[Dict[str, Any]] = None,
        invoiceLineItems: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Generates a new invoice for a customer.

        Args:
            customer: Customer details for the invoice.
            invoiceLineItems: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_subscription(
        self,
        XIdempotentKey: str,
    ) -> Dict[str, Any]:
        """Establishes a new subscription for a customer.

        Args:
            XIdempotentKey: Idempotent key for request deduplication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_subscription(
        self,
        subscriptionId: str,
    ) -> Dict[str, Any]:
        """Removes an existing subscription from the system.

        Args:
            subscriptionId: Subscription ID for identifying the Bill.com account. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_bill_details(
        self,
        billId: str,
    ) -> Dict[str, Any]:
        """Fetches the details of a specified bill.

        Args:
            billId: ID of the bill. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_bills(
        self,
        filters: Optional[str] = None,
        max: Optional[str] = None,
        page: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all bills in the system.

        Args:
            filters: 
            max: 
            page: 
            sort: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer(
        self,
        customerId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of an existing customer.

        Args:
            customerId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_events_catalog(
        self,
    ) -> Dict[str, Any]:
        """Fetches the catalog of available events.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_invoice_details(
        self,
        invoiceId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific invoice.

        Args:
            invoiceId: The ID of the invoice. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_invoice_payment_link(
        self,
        customerId: str,
        email: str,
    ) -> Dict[str, Any]:
        """Creates a payment link for an invoice.

        Args:
            customerId:  (required)
            email:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_invoices(
        self,
        filters: Optional[str] = None,
        max: Optional[str] = None,
        page: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all invoices in the system.

        Args:
            filters: Filters for the Bill.com API request.
            max: Maximum number of results to return.
            page: Page number for pagination.
            sort: Sort order for the results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organization(
        self,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific organization.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_payment_link(
        self,
        customerId: Optional[str] = None,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a payment link for a specific transaction.

        Args:
            customerId: 
            email: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_subscription_details(
        self,
        subscriptionId: str,
    ) -> Dict[str, Any]:
        """Retrieves subscription details for a customer.

        Args:
            subscriptionId: Your Bill.com subscription ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_subscriptions(
        self,
        max: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all subscriptions in the system.

        Args:
            max: The maximum number of results to return.
            page: The page number for pagination.
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

    def get_vendor_payment_options(
        self,
        amount: Optional[str] = None,
        vendorId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the available payment options for the vendor.

        Args:
            amount: Amount for the Bill.com API request.
            vendorId: Vendor ID for the Bill.com API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def invite_customer_to_network(
        self,
        networkId: str,
        networkType: str,
        rppsInformation: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Sends an invitation to a customer to join the network.

        Args:
            networkId: Identifier for the network. (required)
            networkType: Type of the network. (required)
            rppsInformation: Information related to RPPS.
        Returns:
            API response as a dictionary.
        """
        ...

    def login(
        self,
        devKey: str,
        organizationId: str,
        password: str,
        username: str,
    ) -> Dict[str, Any]:
        """Logs a user into the system securely.

        Args:
            devKey:  (required)
            organizationId:  (required)
            password:  (required)
            username:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def logout(
        self,
    ) -> Dict[str, Any]:
        """Logs a user out of the system securely.
        Returns:
            API response as a dictionary.
        """
        ...

    def search_organizations(
        self,
        accountNumber: Optional[str] = None,
        name: Optional[str] = None,
        scope: Optional[str] = None,
        zipOrPostalCode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for organizations based on specified criteria.

        Args:
            accountNumber: Account number.
            name: Name parameter.
            scope: Scope of the request.
            zipOrPostalCode: Zip or postal code.
        Returns:
            API response as a dictionary.
        """
        ...

    def send_invoice(
        self,
        recipient: Dict[str, Any],
        replyTo: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Sends an invoice to a customer via email.

        Args:
            recipient: Details of the recipient(s). (required)
            replyTo: Details of the reply-to recipient. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def session_detail(
        self,
    ) -> Dict[str, Any]:
        """Retrieves details of the current user session.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_bill(
        self,
        billLineItems: Optional[List[Any]] = None,
        classifications: Optional[Dict[str, Any]] = None,
        description: Optional[str] = None,
        dueDate: Optional[str] = None,
        invoice: Optional[Dict[str, Any]] = None,
        payFromChartOfAccountId: Optional[str] = None,
        vendorId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Changes the billing details for an existing invoice.

        Args:
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

    def update_invoice(
        self,
        customer: Optional[Dict[str, Any]] = None,
        invoiceLineItems: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing invoice.

        Args:
            customer: 
            invoiceLineItems: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_subscription(
        self,
        events: Optional[List[Any]] = None,
        name: Optional[str] = None,
        notificationUrl: Optional[str] = None,
        status: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the subscription details for a customer.

        Args:
            events: 
            name: 
            notificationUrl: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

