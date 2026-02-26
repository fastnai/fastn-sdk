"""Fastn Google Shopping connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GoogleShoppingConnector:
    """Google Shopping connector ().

    Provides 5 tools.
    """

    def create_product(
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
        offerId: str,
        price: Dict[str, Any],
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
        salePrice: Optional[Dict[str, Any]] = None,
        salePriceEffectiveDate: Optional[str] = None,
        shipping: Optional[List[Any]] = None,
        shippingHeight: Optional[Dict[str, Any]] = None,
        shippingLength: Optional[Dict[str, Any]] = None,
        shippingWeight: Optional[Dict[str, Any]] = None,
        shippingWidth: Optional[Dict[str, Any]] = None,
        sizeSystem: Optional[str] = None,
        sizeType: Optional[str] = None,
        sizes: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the inventory management system.

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

    def delete_product(
        self,
        merchantId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Removes a product from the inventory management system.

        Args:
            merchantId: ID of the merchant. (required)
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product(
        self,
        merchantId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific product from the inventory management system.

        Args:
            merchantId: Merchant ID associated with the product on Google Shopping. (required)
            productId: ID of the product on Google Shopping. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
        merchantId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of products from the inventory management system.

        Args:
            merchantId: Merchant ID for the Google Shopping API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product(
        self,
        availability: str,
        condition: str,
        contentLanguage: str,
        offerId: str,
        price: Dict[str, Any],
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
        salePrice: Optional[Dict[str, Any]] = None,
        salePriceEffectiveDate: Optional[str] = None,
        shipping: Optional[List[Any]] = None,
        shippingHeight: Optional[Dict[str, Any]] = None,
        shippingLength: Optional[Dict[str, Any]] = None,
        shippingWeight: Optional[Dict[str, Any]] = None,
        shippingWidth: Optional[Dict[str, Any]] = None,
        sizeSystem: Optional[str] = None,
        sizeType: Optional[str] = None,
        sizes: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates details of an existing product in the inventory management system.

        Args:
            availability: Availability status of the product. (required)
            condition: Condition of the product. (required)
            contentLanguage: Language of the product content. (required)
            offerId: Offer ID for the product. (required)
            price: Price of the product. (required)
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

