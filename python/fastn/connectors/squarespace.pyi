"""Fastn Squarespace connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SquarespaceConnector:
    """Squarespace connector ().

    Provides 11 tools.
    """

    def create_order(
        self,
        channelName: str,
        createdOn: str,
        externalOrderReference: str,
        fulfillmentStatus: str,
        grandTotal: Dict[str, Any],
        lineItems: List[Any],
        priceTaxInterpretation: str,
        subtotal: Dict[str, Any],
        billingAddress: Optional[Dict[str, Any]] = None,
        customerEmail: Optional[str] = None,
        discountLines: Optional[List[Any]] = None,
        discountTotal: Optional[Dict[str, Any]] = None,
        fulfilledOn: Optional[str] = None,
        fulfillments: Optional[List[Any]] = None,
        inventoryBehavior: Optional[str] = None,
        shippingAddress: Optional[Dict[str, Any]] = None,
        shippingLines: Optional[List[Any]] = None,
        shippingTotal: Optional[Dict[str, Any]] = None,
        shopperFulfillmentNotificationBehavior: Optional[str] = None,
        taxTotal: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new order in the eCommerce platform based on the specified parameters.

        Args:
            channelName: Name of the sales channel (e.g., online store). (required)
            createdOn: Date and time when the order was created. (required)
            externalOrderReference: Reference ID from an external system. (required)
            fulfillmentStatus: Current fulfillment status of the order. (required)
            grandTotal: Total amount of the order. (required)
            lineItems:  (required)
            priceTaxInterpretation: How taxes are interpreted for pricing. (required)
            subtotal: Subtotal of the order before tax and shipping. (required)
            billingAddress: Billing address details.
            customerEmail: Email address of the customer.
            discountLines: 
            discountTotal: Total discount amount.
            fulfilledOn: Date and time when the order was fulfilled.
            fulfillments: 
            inventoryBehavior: How inventory is handled for this order.
            shippingAddress: Shipping address details.
            shippingLines: 
            shippingTotal: Total shipping cost.
            shopperFulfillmentNotificationBehavior: How shopper fulfillment notifications are handled.
            taxTotal: Total tax amount.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product(
        self,
        storePageId: str,
        type: str,
        variants: List[Any],
        isVisible: Optional[bool] = None,
        name: Optional[str] = None,
        tags: Optional[List[Any]] = None,
        urlSlug: Optional[str] = None,
        variantAttributes: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the inventory of the eCommerce platform.

        Args:
            storePageId: ID of the store page where the product will be displayed. (required)
            type: Type of product. (required)
            variants:  (required)
            isVisible: Indicates whether the product is visible on the storefront.
            name: Name of the product.
            tags: Array of tags for the product.
            urlSlug: URL slug for the product.
            variantAttributes: Array of variant attributes (e.g., color, size).
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific product from the inventory of the eCommerce platform.

        Args:
            productId: The ID of the product for the Squarespace API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order(
        self,
        orderId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific order from the eCommerce platform.

        Args:
            orderId: The ID of the order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_orders(
        self,
        modifiedAfter: Optional[str] = None,
        modifiedBefore: Optional[str] = None,
        nextPageCursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all orders in the eCommerce platform.

        Args:
            modifiedAfter: Filter results modified after this timestamp.
            modifiedBefore: Filter results modified before this timestamp.
            nextPageCursor: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific product from the eCommerce platform.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
        nextPageCursor: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of products available in the eCommerce platform.

        Args:
            nextPageCursor: 
            type: Type parameter for the Squarespace API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_profile(
        self,
        profileId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific customer profile from the eCommerce platform.

        Args:
            profileId: The ID of the profile to access on Squarespace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_profiles(
        self,
        nextPageCursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of customer profiles from the eCommerce platform.

        Args:
            nextPageCursor: Cursor for retrieving the next page of results from the Squarespace API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_store_pages(
        self,
        nextPageCursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the store pages in the context of the eCommerce platform.

        Args:
            nextPageCursor: Cursor for pagination; used to retrieve the next page of results.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product(
        self,
        isVisible: Optional[bool] = None,
        name: Optional[str] = None,
        tags: Optional[List[Any]] = None,
        urlSlug: Optional[str] = None,
        variantAttributes: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing product in the inventory of the eCommerce platform.

        Args:
            isVisible: Indicates whether the resource is visible.
            name: Name of the resource.
            tags: Array of tags for the resource.
            urlSlug: URL slug for the resource.
            variantAttributes: Array of variant attributes.
        Returns:
            API response as a dictionary.
        """
        ...

