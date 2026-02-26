"""Fastn Wix connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class WixConnector:
    """Wix connector ().

    Provides 4 tools.
    """

    def create_product(
        self,
        product: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new product in the inventory management system.

        Args:
            product: Represents a single product. (required)
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
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_by_id(
        self,
        includeMerchantSpecificData: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product information by its unique identifier from the inventory management system.

        Args:
            includeMerchantSpecificData: Flag to include merchant-specific data in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product(
        self,
        product: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates an existing product's details in the inventory management system.

        Args:
            product: Represents a single product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

