"""Fastn Elastic Path connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ElasticPathConnector:
    """Elastic Path connector ().

    Provides 18 tools.
    """

    def add_product(
        self,
    ) -> Dict[str, Any]:
        """Adds a new product to the catalog in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_catalog(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new catalog in the system.

        Args:
            data: Main data object for the Elastic Path request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_customer(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new customer in the system.

        Args:
            data: Data payload for Elastic Path. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_inventory(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new inventory record in the system.

        Args:
            data: Details about the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_catalog(
        self,
        catalogId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified catalog from the system.

        Args:
            catalogId: ID of the catalog. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_customer(
        self,
        customerId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified customer from the system.

        Args:
            customerId: ID of the customer. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified product from the catalog.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_access_token(
        self,
        clientId: str,
        clientSecret: str,
    ) -> Dict[str, Any]:
        """Generates a new access token for authentication in the system.

        Args:
            clientId: Client ID for authentication with Elastic Path. (required)
            clientSecret: Client secret for authentication with Elastic Path. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_carts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of shopping carts in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_catalog(
        self,
        catalogId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific catalog.

        Args:
            catalogId: ID of the catalog. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_catalogs(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of catalogs in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customers(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of customers registered in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inventories(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of inventories in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific product.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of products in the catalog.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_catalog(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates the details of an existing catalog.

        Args:
            data: Data object for the Elastic Path API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_inventory(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates an existing inventory record in the system.

        Args:
            data: Details about the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product(
        self,
    ) -> Dict[str, Any]:
        """Updates the details of an existing product in the catalog.
        Returns:
            API response as a dictionary.
        """
        ...

