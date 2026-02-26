"""Fastn Swell connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SwellConnector:
    """Swell connector ().

    Provides 5 tools.
    """

    def create_product(
        self,
        active: Optional[bool] = None,
        name: Optional[str] = None,
        options: Optional[List[Any]] = None,
        price: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the inventory system.

        Args:
            active: Indicates if the product is active in the Swell API request.
            name: Name of the product in the Swell API request.
            options: 
            price: Price of the product in the Swell API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Deletes a product from the inventory system by its unique ID.

        Args:
            productId: Product ID for the Swell API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_products(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of all products available in the inventory system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_by_id(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific product by its unique ID in the inventory system.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product(
        self,
        active: Optional[bool] = None,
        attributes: Optional[Dict[str, Any]] = None,
        currency: Optional[str] = None,
        delivery: Optional[str] = None,
        name: Optional[str] = None,
        options: Optional[List[Any]] = None,
        price: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Updates the information of an existing product in the inventory system.

        Args:
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

