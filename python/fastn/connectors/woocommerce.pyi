"""Fastn WooCommerce connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class WoocommerceConnector:
    """WooCommerce connector ().

    Provides 4 tools.
    """

    def create_product(
        self,
        name: str,
        regular_price: str,
        type: str,
        categories: Optional[List[Any]] = None,
        description: Optional[str] = None,
        images: Optional[List[Any]] = None,
        short_description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the inventory management system.

        Args:
            name: Name of the product. (required)
            regular_price: Regular price of the product. (required)
            type: Type of product (e.g., 'simple', 'variable'). (required)
            categories: 
            description: Detailed description of the product.
            images: 
            short_description: Short description of the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified product from the inventory management system.

        Args:
            productId: Unique identifier for the WooCommerce product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific product from the inventory management system.

        Args:
            productId: ID of the product in WooCommerce. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all products from the inventory management system.
        Returns:
            API response as a dictionary.
        """
        ...

