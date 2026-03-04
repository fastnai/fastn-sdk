"""Fastn Swell connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class SwellConnector:
    """Swell connector ().

    Provides 5 tools.
    """

    def swell_create_product(
        self,
        active: Optional[bool] = None,
        name: Optional[str] = None,
        options: Optional[List[Any]] = None,
        price: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the Swell store and adds it to the product catalog. Use this when adding a brand-new product that does not yet exist. This action creates a persistent product record in the store. Do not use this to modify an existing product; use swell_update_product instead.

        Args:
            active: Indicates if the product is active in the Swell API request.
            name: Name of the product in the Swell API request.
            options: 
            price: Price of the product in the Swell API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def swell_delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a product from the Swell store by its unique product ID. Use this when a product must be fully removed from the catalog. This action is irreversible — the product and all its associated data will be permanently deleted and cannot be recovered. Do not use this to temporarily hide or disable a product; use updateProduct instead.

        Args:
            productId: Product ID for the Swell API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def swell_get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Returns the full details of a single product in the Swell store by its unique product ID. Use this when you need complete information about a specific product, such as price, description, stock level, and attributes. Do not use this to list all products; use swell_list_products instead.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def swell_list_products(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all products available in the Swell store. Use this to browse or enumerate the full product catalog. Do not use this to retrieve a single product by ID; use swell_get_product instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def swell_update_product(
        self,
        productId: str,
        active: Optional[bool] = None,
        attributes: Optional[Dict[str, Any]] = None,
        currency: Optional[str] = None,
        delivery: Optional[str] = None,
        name: Optional[str] = None,
        options: Optional[List[Any]] = None,
        price: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields of an existing product in the Swell store by its unique product ID. Use this to modify product details such as name, price, description, stock, or other attributes. Only the fields provided in the request body will be updated. Do not use this to create a new product; use swell_create_product instead.

        Args:
            productId: The ID of the product. (required)
            active: Indicates if the product is active.
            attributes: Additional attributes for the product.
            currency: The currency of the product price.
            delivery: The delivery method for the product.
            name: The name of the product.
            options: 
            price: The price of the product.
        Returns:
            API response as a dictionary.
        """
        ...

