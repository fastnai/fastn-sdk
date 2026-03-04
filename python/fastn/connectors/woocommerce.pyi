"""Fastn WooCommerce connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class WoocommerceConnector:
    """WooCommerce connector ().

    Provides 4 tools.
    """

    def woocommerce_create_product(
        self,
        name: str,
        regular_price: str,
        type: str,
        categories: Optional[List[Any]] = None,
        description: Optional[str] = None,
        images: Optional[List[Any]] = None,
        short_description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the WooCommerce store with the specified attributes such as name, price, description, and stock details. Use this tool when you need to add a new item to the product catalog. The product will be published or drafted depending on the status field provided. Do not use this tool to update an existing product; use the appropriate update tool for that. This operation creates a persistent resource.

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

    def woocommerce_delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific product from the WooCommerce store by its product ID. Use this tool when a product needs to be fully removed from the catalog. This action is irreversible; the product cannot be recovered after deletion. Do not use this tool to temporarily hide or draft a product; use woocommerce_update_product to change status instead.

        Args:
            productId: Unique identifier for the WooCommerce product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def woocommerce_get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific WooCommerce product by its product ID, including name, price, description, stock status, and attributes. Use this tool when you need to inspect a single products full details. Do not use this tool to retrieve multiple products; use woocommerce_list_products for that. This operation is read-only and has no side effects.

        Args:
            productId: ID of the product in WooCommerce. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def woocommerce_list_products(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all products available in the WooCommerce store, including their IDs, names, prices, and statuses. Use this tool when you need to browse or enumerate the product catalog. Do not use this tool to retrieve detailed information about a single product; use woocommerce_get_product with a specific product ID for that. This operation is read-only and has no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

