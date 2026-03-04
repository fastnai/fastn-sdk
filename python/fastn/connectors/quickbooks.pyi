"""Fastn QuickBooks connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _QuickbooksCreateAccountCurrencyref(TypedDict, total=False):
    name: str
    value: str

class _QuickbooksCreateCustomerBilladdr(TypedDict, total=False):
    City: str
    CountrySubDivisionCode: str
    Line1: str
    PostalCode: str

class _QuickbooksCreateCustomerPrimaryemailaddr(TypedDict, total=False):
    Address: str

class _QuickbooksCreateCustomerPrimaryphone(TypedDict, total=False):
    FreeFormNumber: str

class _QuickbooksCreatePaymentCustomerref(TypedDict, total=False):
    value: str

class _QuickbooksCreatePaymentPaymentmethodref(TypedDict, total=False):
    value: str

class _QuickbooksUpdateAccountCurrencyref(TypedDict, total=False):
    value: str

class QuickbooksConnector:
    """QuickBooks connector ().

    Provides 12 tools.
    """

    def quickbooks_create_account(
        self,
        AccountType: str,
        Name: str,
        companyId: str,
        environment: str,
        AccountSubType: Optional[str] = None,
        Active: Optional[bool] = None,
        CurrencyRef: Optional[_QuickbooksCreateAccountCurrencyref] = None,
        Description: Optional[str] = None,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new account record in QuickBooks for a specified company, with details such as account name, type, and classification. Use this tool when you need to add a new chart-of-accounts entry. Do not use this tool to update an existing account — use the update account tool instead. Creating accounts affects the chart of accounts and financial reporting.

        Args:
            AccountType: Type of the account (e.g., Bank, Asset). (required)
            Name: Name of the account. (required)
            companyId: ID of the QuickBooks company. (required)
            environment: QuickBooks API environment (e.g., production, sandbox). (required)
            AccountSubType: Subtype of the account (if applicable).
            Active: Indicates whether the account is active.
            CurrencyRef: Reference to the currency of the account.
            Description: Description of the account.
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def quickbooks_create_customer(
        self,
        companyId: str,
        environment: str,
        BillAddr: Optional[_QuickbooksCreateCustomerBilladdr] = None,
        DisplayName: Optional[str] = None,
        PrimaryEmailAddr: Optional[_QuickbooksCreateCustomerPrimaryemailaddr] = None,
        PrimaryPhone: Optional[_QuickbooksCreateCustomerPrimaryphone] = None,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new customer record in QuickBooks for a specified company, including details such as name, email, phone number, and billing address. Use this tool when you need to add a new customer to QuickBooks. Do not use this tool to update an existing customer record — use the updateCustomer tool instead.

        Args:
            companyId: The ID of the QuickBooks company. (required)
            environment: QuickBooks API environment (e.g., production, sandbox). (required)
            BillAddr: Billing address details.
            DisplayName: Display name of the entity.
            PrimaryEmailAddr: Primary email address details.
            PrimaryPhone: Primary phone number details.
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def quickbooks_create_payment(
        self,
        baseUrl: str,
        companyId: str,
        CustomerRef: Optional[_QuickbooksCreatePaymentCustomerref] = None,
        Line: Optional[List[Any]] = None,
        PaymentMethodRef: Optional[_QuickbooksCreatePaymentPaymentmethodref] = None,
        TotalAmt: Optional[float] = None,
        TxnDate: Optional[str] = None,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates and records a new payment transaction in QuickBooks for a specified company, including details such as amount, customer, and linked invoices. Use this tool when you need to record a payment received from a customer. Do not use this tool to update an existing payment record. This action posts a financial transaction and may affect account balances.

        Args:
            baseUrl: The base URL for the QuickBooks API request. (required)
            companyId: ID of the company. (required)
            CustomerRef: Reference to the customer involved in the transaction.
            Line: 
            PaymentMethodRef: Reference to the payment method used.
            TotalAmt: Total amount of the transaction.
            TxnDate: Date of the transaction.
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def quickbooks_get_account(
        self,
        accountId: str,
        companyId: str,
        environment: str,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single account record in QuickBooks, identified by its account ID, including name, type, balance, and status. Use this tool when you need to inspect a specific account. Do not use this tool to retrieve a list of all accounts — use the list accounts tool instead.

        Args:
            accountId: Account ID for the QuickBooks request. (required)
            companyId: Company ID for the QuickBooks request. (required)
            environment: Environment for the QuickBooks request (e.g., production, sandbox). (required)
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def quickbooks_get_company_info(
        self,
        companyId: str,
        environment: str,
        realmId: str,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves profile and configuration information for a specific QuickBooks company, including its name, address, contact details, and fiscal year settings. Use this tool when you need to look up company-level metadata for a given company ID and realm ID. Do not use this tool to retrieve financial data such as accounts or payments.

        Args:
            companyId: Company ID for the QuickBooks company. (required)
            environment: Environment for the QuickBooks API request (e.g., production, sandbox). (required)
            realmId: Realm ID for the QuickBooks company. (required)
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def quickbooks_get_customer(
        self,
        companyId: str,
        customerId: str,
        environment: str,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single customer record in QuickBooks, identified by their customer ID, including name, contact information, and billing details. Use this tool when you need to look up a specific customer. Do not use this tool to retrieve a list of all customers — use the list customers tool instead.

        Args:
            companyId: The ID of the QuickBooks company. (required)
            customerId: The ID of the customer in QuickBooks. (required)
            environment: The QuickBooks environment (e.g., sandbox, production). (required)
            minorversion: Minor version of the QuickBooks API being used.
        Returns:
            API response as a dictionary.
        """
        ...

    def quickbooks_get_payment(
        self,
        companyId: str,
        environment: str,
        paymentId: str,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single payment record in QuickBooks, identified by its payment ID, including amount, date, customer, and associated invoices. Use this tool when you need to inspect a specific payment. Do not use this tool to retrieve a list of multiple payments — use the list payments tool instead.

        Args:
            companyId: The ID of the company. (required)
            environment: The environment of the QuickBooks API request (e.g., production, sandbox). (required)
            paymentId: The ID of the payment. (required)
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def quickbooks_list_account_detail(
        self,
        companyId: str,
        environment: str,
        name: str,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a detailed Account List report from QuickBooks for a specified company, including account names, types, balances, and other financial details. Use this tool when you need a comprehensive report of all accounts for accounting or auditing purposes. Do not use this tool to retrieve or modify individual account records — use the account management tools instead.

        Args:
            companyId: The ID of the QuickBooks company. (required)
            environment: The QuickBooks environment (e.g., production, sandbox). (required)
            name: Name parameter for the QuickBooks API request. (required)
            minorversion: The minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def quickbooks_list_accounts(
        self,
        companyId: str,
        environment: str,
        query: str,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of account records from QuickBooks for a specified company by querying the QuickBooks data service. Use this tool when you need to browse or filter multiple accounts. Do not use this tool to retrieve details of a single account — use the get account tool instead.

        Args:
            companyId: Company ID for the QuickBooks QuickBooks API request. (required)
            environment: Environment for the QuickBooks QuickBooks API request. (required)
            query: Query string for the QuickBooks QuickBooks API request. (required)
            minorversion: Minor version for the QuickBooks QuickBooks API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def quickbooks_list_customers(
        self,
        companyId: str,
        environment: str,
        query: str,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of customer records from QuickBooks for a specified company by querying the QuickBooks data service. Use this tool when you need to browse or filter multiple customers. Do not use this tool to retrieve details of a single customer — use the get customer tool instead.

        Args:
            companyId: The ID of the QuickBooks company. (required)
            environment: The QuickBooks environment (e.g., sandbox, production). (required)
            query: Query string for the QuickBooks API request. (required)
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def quickbooks_list_payments(
        self,
        companyId: str,
        environment: str,
        query: str,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of payment records from QuickBooks for a specified company by querying the QuickBooks data service. Use this tool when you need to browse or filter multiple payments. Do not use this tool to retrieve details of a single payment — use the get payment tool instead.

        Args:
            companyId: Company ID for the QuickBooks API request. (required)
            environment: Environment for the QuickBooks API request (e.g., production, sandbox). (required)
            query: Query string for the QuickBooks API request. (required)
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def quickbooks_update_account(
        self,
        AccountType: str,
        Id: str,
        companyId: str,
        environment: str,
        AccountSubType: Optional[str] = None,
        AcctNum: Optional[str] = None,
        Active: Optional[bool] = None,
        Classification: Optional[str] = None,
        CurrencyRef: Optional[_QuickbooksUpdateAccountCurrencyref] = None,
        Description: Optional[str] = None,
        FullyQualifiedName: Optional[str] = None,
        Name: Optional[str] = None,
        SyncToken: Optional[str] = None,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing account record in QuickBooks for a specified company, such as its name, type, or description. Use this tool when you need to modify the properties of an account that already exists. Do not use this tool to create a new account — use the create account tool instead. Changes to account definitions may affect financial reporting.

        Args:
            AccountType: Type of the account. (required)
            Id: Unique identifier for the account. (required)
            companyId: ID of the company. (required)
            environment: QuickBooks environment (e.g., production, sandbox). (required)
            AccountSubType: Subtype of the account.
            AcctNum: Account number for the account.
            Active: Indicates if the account is active.
            Classification: Classification of the account.
            CurrencyRef: Reference to the currency used for the account.
            Description: Description of the account.
            FullyQualifiedName: Fully qualified name of the account.
            Name: Name of the account.
            SyncToken: Synchronization token for the account.
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

