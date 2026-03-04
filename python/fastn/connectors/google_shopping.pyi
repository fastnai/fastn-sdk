"""Fastn Google Shopping connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _GoogleShoppingCreateProductPrice(TypedDict, total=False):
    currency: str
    value: str

class _GoogleShoppingCreateProductSaleprice(TypedDict, total=False):
    currency: str
    value: str

class _GoogleShoppingCreateProductShippingheight(TypedDict, total=False):
    unit: str
    value: int

class _GoogleShoppingCreateProductShippinglength(TypedDict, total=False):
    unit: str
    value: int

class _GoogleShoppingCreateProductShippingweight(TypedDict, total=False):
    unit: str
    value: int

class _GoogleShoppingCreateProductShippingwidth(TypedDict, total=False):
    unit: str
    value: int

class _GoogleShoppingUpdateProductPrice(TypedDict, total=False):
    currency: str
    value: str

class _GoogleShoppingUpdateProductSaleprice(TypedDict, total=False):
    currency: str
    value: str

class _GoogleShoppingUpdateProductShippingheight(TypedDict, total=False):
    unit: str
    value: int

class _GoogleShoppingUpdateProductShippinglength(TypedDict, total=False):
    unit: str
    value: int

class _GoogleShoppingUpdateProductShippingweight(TypedDict, total=False):
    unit: str
    value: int

class _GoogleShoppingUpdateProductShippingwidth(TypedDict, total=False):
    unit: str
    value: int

class GoogleShoppingConnector:
    """Google Shopping connector ().

    Provides 5 tools.
    """

    def google_shopping_create_product(
        self,
        availability: str,
        channel: str,
        condition: str,
        contentLanguage: str,
        description: str,
        feedLabel: str,
        id: str,
        imageLink: str,
        link: str,
        merchantId: str,
        offerId: str,
        price: _GoogleShoppingCreateProductPrice,
        targetCountry: str,
        title: str,
        ageGroup: Optional[str] = None,
        brand: Optional[str] = None,
        color: Optional[str] = None,
        customAttributes: Optional[List[Any]] = None,
        gender: Optional[str] = None,
        identifierExists: Optional[bool] = None,
        kind: Optional[str] = None,
        material: Optional[str] = None,
        maxHandlingTime: Optional[str] = None,
        minHandlingTime: Optional[str] = None,
        pattern: Optional[str] = None,
        productTypes: Optional[List[Any]] = None,
        salePrice: Optional[_GoogleShoppingCreateProductSaleprice] = None,
        salePriceEffectiveDate: Optional[str] = None,
        shipping: Optional[List[Any]] = None,
        shippingHeight: Optional[_GoogleShoppingCreateProductShippingheight] = None,
        shippingLength: Optional[_GoogleShoppingCreateProductShippinglength] = None,
        shippingWeight: Optional[_GoogleShoppingCreateProductShippingweight] = None,
        shippingWidth: Optional[_GoogleShoppingCreateProductShippingwidth] = None,
        sizeSystem: Optional[str] = None,
        sizeType: Optional[str] = None,
        sizes: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new product listing in the Google Merchant Center for a specified merchant. Use this to add a product to the merchants catalog so it can appear in Google Shopping results. To update an existing product, use google_shopping_update_product. Submitting a product triggers Googles review and approval process before it appears in listings.

        Args:
            availability: Availability status of the product. (required)
            channel: Sales channel for the product. (required)
            condition: Condition of the product. (required)
            contentLanguage: Content language for the product. (required)
            description: Description of the product. (required)
            feedLabel: Label for the product feed. (required)
            id: Unique identifier for the product. (required)
            imageLink: Link to the product image. (required)
            link: Link to the product page. (required)
            merchantId: Merchant ID. (required)
            offerId: Offer ID for the product. (required)
            price: Price of the product. (required)
            targetCountry: Target country for the product. (required)
            title: Title of the product. (required)
            ageGroup: Age group the product is targeted towards.
            brand: Brand of the product.
            color: Color of the product.
            customAttributes: 
            gender: Gender the product is targeted towards.
            identifierExists: Indicates if a product identifier exists.
            kind: Kind of product.
            material: Material of the product.
            maxHandlingTime: Maximum handling time for the product.
            minHandlingTime: Minimum handling time for the product.
            pattern: Pattern of the product.
            productTypes: Types of product.
            salePrice: Sale price of the product.
            salePriceEffectiveDate: Effective date for the sale price.
            shipping: 
            shippingHeight: Height of the product for shipping.
            shippingLength: Length of the product for shipping.
            shippingWeight: Weight of the product for shipping.
            shippingWidth: Width of the product for shipping.
            sizeSystem: Size system used for the product.
            sizeType: Type of size system used.
            sizes: Available sizes for the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_shopping_delete_product(
        self,
        merchantId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Permanently removes a product listing from the Google Merchant Center for a specified merchant by product ID. Use this to delist a product from Google Shopping. This action is irreversible — the product will be removed from the merchants catalog and will no longer appear in Google Shopping results. To temporarily suppress a product, consider updating its availability instead.

        Args:
            merchantId: ID of the merchant. (required)
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_shopping_get_product(
        self,
        merchantId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a specific product listing from the Google Merchant Center by merchant ID and product ID. Returns attributes such as title, price, availability, description, and status. Use this to inspect a single known product. To browse multiple products, use google_shopping_list_products. Read-only operation with no side effects.

        Args:
            merchantId: Merchant ID associated with the product on Google Shopping. (required)
            productId: ID of the product on Google Shopping. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_shopping_list_products(
        self,
        merchantId: str,
    ) -> Dict[str, Any]:
        """Lists all product listings in the Google Merchant Center for a specified merchant. Use this to browse or audit the full product catalog. To retrieve details for a single specific product, use google_shopping_get_product. Read-only operation with no side effects.

        Args:
            merchantId: Merchant ID for the Google Shopping API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_shopping_update_product(
        self,
        availability: str,
        condition: str,
        contentLanguage: str,
        merchantId: str,
        offerId: str,
        price: _GoogleShoppingUpdateProductPrice,
        productId: str,
        targetCountry: str,
        title: str,
        ageGroup: Optional[str] = None,
        brand: Optional[str] = None,
        channel: Optional[str] = None,
        color: Optional[str] = None,
        customAttributes: Optional[List[Any]] = None,
        description: Optional[str] = None,
        feedLabel: Optional[str] = None,
        gender: Optional[str] = None,
        id: Optional[str] = None,
        identifierExists: Optional[bool] = None,
        imageLink: Optional[str] = None,
        kind: Optional[str] = None,
        link: Optional[str] = None,
        material: Optional[str] = None,
        maxHandlingTime: Optional[str] = None,
        minHandlingTime: Optional[str] = None,
        pattern: Optional[str] = None,
        productTypes: Optional[List[Any]] = None,
        salePrice: Optional[_GoogleShoppingUpdateProductSaleprice] = None,
        salePriceEffectiveDate: Optional[str] = None,
        shipping: Optional[List[Any]] = None,
        shippingHeight: Optional[_GoogleShoppingUpdateProductShippingheight] = None,
        shippingLength: Optional[_GoogleShoppingUpdateProductShippinglength] = None,
        shippingWeight: Optional[_GoogleShoppingUpdateProductShippingweight] = None,
        shippingWidth: Optional[_GoogleShoppingUpdateProductShippingwidth] = None,
        sizeSystem: Optional[str] = None,
        sizeType: Optional[str] = None,
        sizes: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing product listing in the Google Merchant Center for a specified merchant, using a partial PATCH update. Use this to modify attributes such as price, availability, title, or description of a product that already exists. To create a new product, use google_shopping_create_product. This operation modifies the product record and the changes will be reflected in Google Shopping listings.

        Args:
            availability: Availability status of the product. (required)
            condition: Condition of the product. (required)
            contentLanguage: Language of the product content. (required)
            merchantId: Merchant ID from the URL. (required)
            offerId: Offer ID for the product. (required)
            price: Price of the product. (required)
            productId: Product ID from the URL. (required)
            targetCountry: Target country for the product. (required)
            title: Title of the product. (required)
            ageGroup: Age group the product is targeted towards.
            brand: Brand of the product.
            channel: Sales channel of the product.
            color: Color of the product.
            customAttributes: 
            description: Description of the product.
            feedLabel: Label for the product feed.
            gender: Gender the product is targeted towards.
            id: Unique identifier of the product.
            identifierExists: Indicates if the product identifier exists.
            imageLink: Link to the product image.
            kind: Kind of product.
            link: Link to the product.
            material: Material of the product.
            maxHandlingTime: Maximum handling time for the product.
            minHandlingTime: Minimum handling time for the product.
            pattern: Pattern of the product.
            productTypes: Types of product.
            salePrice: Sale price of the product.
            salePriceEffectiveDate: Effective date of the sale price.
            shipping: 
            shippingHeight: Height of the product for shipping.
            shippingLength: Length of the product for shipping.
            shippingWeight: Weight of the product for shipping.
            shippingWidth: Width of the product for shipping.
            sizeSystem: System used for sizing.
            sizeType: Type of size system used.
            sizes: Available sizes for the product.
        Returns:
            API response as a dictionary.
        """
        ...

