"""Fastn FreshBooks connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FreshbooksConnector:
    """FreshBooks connector ().

    Provides 11 tools.
    """

    def create_account(
        self,
        name: str,
        number: str,
        parent_account: float,
        sub_type: str,
        auto_created: Optional[bool] = None,
        description: Optional[str] = None,
        system_account_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new account in the user management system.

        Args:
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

    def create_client(
        self,
        client: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new client in the client management system.

        Args:
            client: Client information. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_account(
        self,
        accountUid: str,
        businessUid: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific account from the user management system.

        Args:
            accountUid:  (required)
            businessUid:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_accounts(
        self,
        businessUuid: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all accounts from the user management system.

        Args:
            businessUuid: UUID of the FreshBooks business. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_client(
        self,
        accountId: str,
        customerId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific client from the client management system.

        Args:
            accountId: Account ID for the FreshBooks API request. (required)
            customerId: Customer ID for the FreshBooks API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_clients(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all clients from the client management system.

        Args:
            accountId: Account ID for FreshBooks. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_payments(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all payments from the payment processing system.

        Args:
            accountId: The account ID for the FreshBooks account. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user(
        self,
    ) -> Dict[str, Any]:
        """Retrieves user details from the user management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_account_types(
        self,
    ) -> Dict[str, Any]:
        """Lists all available account types in the user management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_account(
        self,
        name: str,
        number: str,
        parent_account: str,
        sub_type: str,
        auto_created: Optional[bool] = None,
        description: Optional[str] = None,
        system_account_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the information of an existing account in the user management system.

        Args:
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

    def update_client(
        self,
        client: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates the information of an existing client in the client management system.

        Args:
            client: Client information for the FreshBooks API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

