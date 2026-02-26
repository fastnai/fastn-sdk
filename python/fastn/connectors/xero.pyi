"""Fastn Xero connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class XeroConnector:
    """Xero connector ().

    Provides 11 tools.
    """

    def get_accounts(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of accounts in the accounting software.

        Args:
            Xerotenantid: Tenant ID for Xero. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_bank_transactions(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Retrieves bank transactions from the accounting software.

        Args:
            Xerotenantid: Xero Tenant ID for authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connections(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of connections between accounts in the accounting software.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Accesses contact information stored in the accounting software.

        Args:
            Xerotenantid: Tenant ID for Xero authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_credit_notes(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Retrieves credit notes issued in the accounting software.

        Args:
            Xerotenantid: Tenant ID for Xero. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_invoices(
        self,
        Xerotenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains a detailed list of invoices from the accounting software.

        Args:
            Xerotenantid: Tenant ID for Xero authentication.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_items(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Fetches a list of items or products in the accounting software.

        Args:
            Xerotenantid: Tenant ID for Xero authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_journals(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Retrieves journal entries from the accounting software.

        Args:
            Xerotenantid: Xero tenant identifier. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_payments(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Obtains payment information related to transactions in the accounting software.

        Args:
            Xerotenantid: Xero tenant ID for authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_report(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Generates and fetches a specific report from the accounting software.

        Args:
            Xerotenantid: Tenant ID for Xero. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Accesses a list of users in the accounting software.

        Args:
            Xerotenantid: Xero tenant identifier. (required)
        Returns:
            API response as a dictionary.
        """
        ...

