"""Fastn Xero connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class XeroConnector:
    """Xero connector ().

    Provides 11 tools.
    """

    def get_accounts_xero(
        self,
        Xerotenantid: str,
        order: Optional[str] = None,
        where: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all accounts in Xero accounting software, allowing for management and synchronization of financial data.

        Args:
            Xerotenantid: Tenant ID for Xero. (required)
            order: Order by clause for sorting results.
            where: Where clause for filtering results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_bank_transactions_xero(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Provides access to bank transactions recorded in Xero accounting software, aiding in reconciliation and financial tracking.

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

    def get_contacts_xero(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Gathers contact information stored in Xero accounting software, essential for managing client and supplier relationships.

        Args:
            Xerotenantid: Tenant ID for Xero authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_credit_notes_xero(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Obtains credit notes from Xero accounting software, necessary for managing customer returns and adjustments to invoiced amounts.

        Args:
            Xerotenantid: Tenant ID for Xero. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_invoices_xero(
        self,
        Xerotenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains invoices from Xero accounting software, facilitating the review and management of outstanding payments and client billing.

        Args:
            Xerotenantid: Tenant ID for Xero authentication.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_items_xero(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Fetches inventory items listed in Xero accounting software, assisting in stock management and sales processing.

        Args:
            Xerotenantid: Tenant ID for Xero authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_journals_xero(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Retrieves journal entries from Xero accounting software, which are crucial for maintaining accurate financial records.

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

    def get_report_xero(
        self,
        Xerotenantid: str,
    ) -> Dict[str, Any]:
        """Generates financial reports in Xero accounting software, allowing for insightful analysis of your business performance.

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

