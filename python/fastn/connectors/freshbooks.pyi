"""Fastn FreshBooks connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _FreshbooksCreateClientClient(TypedDict, total=False):
    contacts: List[Any]
    currency_code: str
    email: str
    face: str
    fname: str
    highlight_string: str
    home_phone: str
    language: str
    last_activity: str
    late_fee: str
    late_reminders: List[Any]
    lname: str
    note: str
    organization: str
    p_city: str
    p_code: str
    p_country: str
    p_province: str
    p_street: str
    p_street2: str
    source: str
    status: str
    userid: str
    vat_name: str
    vat_number: str

class _FreshbooksUpdateClientClient(TypedDict, total=False):
    fname: str

class FreshbooksConnector:
    """FreshBooks connector ().

    Provides 11 tools.
    """

    def freshbooks_create_account(
        self,
        businessUuid: str,
        name: str,
        number: str,
        parent_account: float,
        sub_type: str,
        auto_created: Optional[bool] = None,
        description: Optional[str] = None,
        system_account_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new ledger account within a FreshBooks business. Use this tool when you need to add a new account to the chart of accounts, such as a new expense, income, or asset account. Do not use this tool to update an existing account; use freshbooks_update_account instead. This operation permanently adds a new ledger account to the business and affects financial structure and reporting.

        Args:
            businessUuid: The UUID of the business. (required)
            name: The name of the entity. (required)
            number: The number associated with the entity. (required)
            parent_account: The ID of the parent account. (required)
            sub_type: The sub type of the entity. (required)
            auto_created: Indicates whether the entity was auto-created.
            description: A description of the entity.
            system_account_name: The system account name for the entity.
        Returns:
            API response as a dictionary.
        """
        ...

    def freshbooks_create_client(
        self,
        accountId: str,
        client: _FreshbooksCreateClientClient,
    ) -> Dict[str, Any]:
        """Creates a new client record in FreshBooks. Use this tool when you need to add a new client to your FreshBooks account, providing details such as name, email, and billing address. Do not use this tool to update an existing client; use freshbooks_update_client instead. This operation permanently creates a new client record in FreshBooks.

        Args:
            accountId: Account ID. (required)
            client: Client information. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def freshbooks_get_account(
        self,
        accountUid: str,
        businessUid: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific ledger account within a FreshBooks business, identified by its account UID. Use this tool when you need full details for a single known ledger account, such as its type, balance, or description. Do not use this tool to retrieve all accounts; use freshbooks_list_accounts instead. This is a read-only operation with no side effects.

        Args:
            accountUid:  (required)
            businessUid:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def freshbooks_get_client(
        self,
        accountId: str,
        customerId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full profile details of a single, specific client from FreshBooks, identified by their customer ID. Use this tool when you need detailed information about one client, such as contact info, currency, or billing address. Do not use this tool to retrieve a list of multiple clients; use freshbooks_list_clients instead. This is a read-only operation with no side effects.

        Args:
            accountId: Account ID for the FreshBooks API request. (required)
            customerId: Customer ID for the FreshBooks API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def freshbooks_get_user(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the profile details of the currently authenticated FreshBooks user, including name, email, and account information. Use this tool when you need to identify who is logged in or obtain the authenticated users profile data. Do not use this tool to retrieve client profiles; use freshbooks_get_client instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def freshbooks_list_account_types(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all available ledger account types in FreshBooks. Use this tool when you need to understand which account type categories exist before creating or categorizing a ledger account. Do not use this tool to retrieve individual account details; use freshbooks_get_account instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def freshbooks_list_accounts(
        self,
        businessUuid: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all ledger accounts associated with a FreshBooks business. Use this tool when you need an overview of all ledger accounts, such as for financial reporting, chart of accounts review, or account selection. Do not use this tool to retrieve a single accounts details; use freshbooks_get_account instead. This is a read-only operation with no side effects.

        Args:
            businessUuid: UUID of the FreshBooks business. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def freshbooks_list_clients(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all clients associated with a FreshBooks account. Use this tool when you need to browse or search across all clients, such as for reporting, bulk operations, or client lookup by name. Do not use this tool to fetch a single clients details; use freshbooks_get_client instead. This is a read-only operation with no side effects.

        Args:
            accountId: Account ID for FreshBooks. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def freshbooks_list_payments(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all payments recorded in FreshBooks for a given account. Use this tool when you need an overview of payment transactions, such as for financial reporting or reconciliation. Do not use this tool to retrieve details of a single specific payment by ID. This is a read-only operation with no side effects.

        Args:
            accountId: The account ID for the FreshBooks account. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def freshbooks_update_account(
        self,
        businessUuid: str,
        name: str,
        number: str,
        parent_account: str,
        sub_type: str,
        auto_created: Optional[bool] = None,
        description: Optional[str] = None,
        system_account_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing ledger account within a FreshBooks business. Use this tool when you need to modify the details of a ledger account, such as its name, type, or description, for a specified business. Do not use this tool to create a new ledger account; use freshbooks_create_account instead. Note: this endpoint uses POST but performs an update operation. Changes to ledger accounts affect financial reporting and cannot be easily reversed.

        Args:
            businessUuid: The UUID of the business. (required)
            name: The name of the account. (required)
            number: The account number. (required)
            parent_account: The ID of the parent account, if applicable. (required)
            sub_type: The sub-type of the account. (required)
            auto_created: Indicates if the account was auto-created.
            description: A description of the account.
            system_account_name: The system account name.
        Returns:
            API response as a dictionary.
        """
        ...

    def freshbooks_update_client(
        self,
        accountId: str,
        client: _FreshbooksUpdateClientClient,
        customerId: str,
    ) -> Dict[str, Any]:
        """Updates the information of an existing client in FreshBooks. Use this tool when you need to modify a clients details such as name, email, address, or other profile fields for a known client identified by their customer ID. Do not use this tool to create a new client or to retrieve client information. This operation overwrites the specified clients existing data and cannot be undone without a subsequent update.

        Args:
            accountId: Account ID for the FreshBooks API request. (required)
            client: Client information for the FreshBooks API request. (required)
            customerId: Customer ID for the FreshBooks API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

