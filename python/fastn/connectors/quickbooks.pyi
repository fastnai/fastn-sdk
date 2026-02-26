"""Fastn QuickBooks connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class QuickbooksConnector:
    """QuickBooks connector ().

    Provides 12 tools.
    """

    def account_list_detail(
        self,
        name: str,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Provides detailed information about the account list in the specified system.

        Args:
            name: Name parameter for the QuickBooks API request. (required)
            minorversion: The minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_account(
        self,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new account in the specified system.

        Args:
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_customer(
        self,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new customer within the specified system.

        Args:
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_payment(
        self,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Processes a new payment in the specified system.

        Args:
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_account(
        self,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific account in the specified system.

        Args:
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_accounts(
        self,
        query: str,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all accounts from the specified system.

        Args:
            query: Query string for the QuickBooks QuickBooks API request. (required)
            minorversion: Minor version for the QuickBooks QuickBooks API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_company_info(
        self,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves company information from the specified system.

        Args:
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer(
        self,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific customer in the specified system.

        Args:
            minorversion: Minor version of the QuickBooks API being used.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customers(
        self,
        query: str,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all customers from the specified system.

        Args:
            query: Query string for the QuickBooks API request. (required)
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_payment(
        self,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific payment in the specified system.

        Args:
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_payments(
        self,
        query: str,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all payments made within the specified system.

        Args:
            query: Query string for the QuickBooks API request. (required)
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_account(
        self,
        minorversion: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing account in the specified system.

        Args:
            minorversion: Minor version of the QuickBooks API.
        Returns:
            API response as a dictionary.
        """
        ...

