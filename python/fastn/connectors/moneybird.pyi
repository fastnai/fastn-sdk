"""Fastn Moneybird connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MoneybirdConnector:
    """Moneybird connector ().

    Provides 10 tools.
    """

    def create_contact(
        self,
        contact: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new contact in the system.

        Args:
            contact: Contact details for the Moneybird API endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sales_invoice(
        self,
        sales_invoice: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generates a new sales invoice in the system.

        Args:
            sales_invoice: Details of the sales invoice. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def createproduct(
        self,
        product: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new product in the system.

        Args:
            product: Product details for the Moneybird API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_update(
        self,
        administrationId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Deletes or updates an entry in the system.

        Args:
            administrationId: ID of the administration. (required)
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_administrations(
        self,
    ) -> Dict[str, Any]:
        """Fetches the list of administrations within the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contact(
        self,
        administrationId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific contact from the system.

        Args:
            administrationId: ID of the administration in Moneybird. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_documents(
        self,
        administrationId: str,
    ) -> Dict[str, Any]:
        """Fetches documents available in the system.

        Args:
            administrationId: The ID of the administration to access via the Moneybird API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
        administrationId: str,
    ) -> Dict[str, Any]:
        """Retrieves the list of products available in the system.

        Args:
            administrationId: ID of the administration for the Moneybird API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sales_invoices(
        self,
        administrationId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all sales invoices from the system.

        Args:
            administrationId: ID of the administration. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product(
        self,
        product: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates the details of an existing product in the system.

        Args:
            product: Product information. (required)
        Returns:
            API response as a dictionary.
        """
        ...

