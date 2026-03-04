"""Fastn Wix connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _WixCreateProductProduct(TypedDict, total=False):
    brand: str
    costAndProfitData: Dict[str, Any]
    description: str
    discount: Dict[str, Any]
    manageVariants: bool
    name: str
    priceData: Dict[str, Any]
    productOptions: List[Any]
    productType: str
    ribbon: str
    sku: str
    visible: bool
    weight: float

class _WixUpdateProductProduct(TypedDict, total=False):
    brand: str
    description: str
    discount: Dict[str, Any]
    name: str
    priceData: Dict[str, Any]
    productOptions: List[Any]
    productType: str
    ribbon: str
    sku: str
    visible: bool
    weight: float

class WixConnector:
    """Wix connector ().

    Provides 4 tools.
    """

    def wix_create_product(
        self,
        product: _WixCreateProductProduct,
    ) -> Dict[str, Any]:
        """Creates a new product in the Wix Stores catalog. Use this tool when you need to add a new item to the store, including its name, price, description, and other attributes. The product will be immediately visible in the store upon creation unless explicitly set to hidden. Do not use this tool to update an existing product; use wix_update_product for that.

        Args:
            product: Represents a single product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def wix_delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a product from the Wix Stores catalog by its product ID. Use this tool when a product needs to be fully removed from the store. This action is irreversible; the product cannot be recovered after deletion. Do not use this tool to temporarily hide or unpublish a product; use wix_update_product to change visibility instead.

        Args:
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def wix_get_product(
        self,
        productId: str,
        includeMerchantSpecificData: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Wix Stores product by its unique product ID. Use this tool when you need to inspect a single products name, description, price, inventory, or other attributes. Do not use this tool to browse or list multiple products. This operation is read-only and has no side effects.

        Args:
            productId: ID of the product. (required)
            includeMerchantSpecificData: Flag to include merchant-specific data in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def wix_update_product(
        self,
        product: _WixUpdateProductProduct,
        productId: str,
    ) -> Dict[str, Any]:
        """Updates one or more fields of an existing product in the Wix Stores catalog by its product ID. Use this tool to modify product details such as name, price, description, or visibility. Only the fields provided in the request body will be updated (partial update). Do not use this tool to create a new product; use wix_create_product for that. Changes take effect immediately in the live store.

        Args:
            product: Represents a single product. (required)
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

