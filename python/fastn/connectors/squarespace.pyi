"""Fastn Squarespace connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _SquarespaceCreateOrderGrandtotal(TypedDict, total=False):
    currency: str
    value: str

class _SquarespaceCreateOrderSubtotal(TypedDict, total=False):
    currency: str
    value: str

class _SquarespaceCreateOrderBillingaddress(TypedDict, total=False):
    address1: str
    address2: str
    city: str
    countryCode: str
    firstName: str
    lastName: str
    phone: str
    postalCode: str
    state: str

class _SquarespaceCreateOrderDiscounttotal(TypedDict, total=False):
    currency: str
    value: str

class _SquarespaceCreateOrderShippingaddress(TypedDict, total=False):
    address1: str
    address2: str
    city: str
    countryCode: str
    firstName: str
    lastName: str
    phone: str
    postalCode: str
    state: str

class _SquarespaceCreateOrderShippingtotal(TypedDict, total=False):
    currency: str
    value: str

class _SquarespaceCreateOrderTaxtotal(TypedDict, total=False):
    currency: str
    value: str

class SquarespaceConnector:
    """Squarespace connector ().

    Provides 11 tools.
    """

    def squarespace_create_order(
        self,
        channelName: str,
        createdOn: str,
        externalOrderReference: str,
        fulfillmentStatus: str,
        grandTotal: _SquarespaceCreateOrderGrandtotal,
        lineItems: List[Any],
        priceTaxInterpretation: str,
        subtotal: _SquarespaceCreateOrderSubtotal,
        billingAddress: Optional[_SquarespaceCreateOrderBillingaddress] = None,
        customerEmail: Optional[str] = None,
        discountLines: Optional[List[Any]] = None,
        discountTotal: Optional[_SquarespaceCreateOrderDiscounttotal] = None,
        fulfilledOn: Optional[str] = None,
        fulfillments: Optional[List[Any]] = None,
        inventoryBehavior: Optional[str] = None,
        shippingAddress: Optional[_SquarespaceCreateOrderShippingaddress] = None,
        shippingLines: Optional[List[Any]] = None,
        shippingTotal: Optional[_SquarespaceCreateOrderShippingtotal] = None,
        shopperFulfillmentNotificationBehavior: Optional[str] = None,
        taxTotal: Optional[_SquarespaceCreateOrderTaxtotal] = None,
    ) -> Dict[str, Any]:
        """Creates a new order in your Squarespace eCommerce store with the specified parameters such as line items, customer information, and pricing. Use this when you need to programmatically place an order. This action creates a permanent record in the platform; use with care as created orders may require manual cancellation to undo.

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

    def squarespace_create_product(
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
        """Creates a new product in your Squarespace store inventory, adding it to the online store with the specified attributes such as name, description, price, and variants. Use this when you need to add a new item for sale. Use squarespace_update_product to modify an existing product instead. This action creates a permanent record in the store.

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

    def squarespace_delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific product from your Squarespace store inventory by productId. Use this when you need to remove a product entirely from the store. This action is irreversible — the product and its associated data cannot be recovered after deletion. Use squarespace_update_product instead if you only want to hide or modify the product.

        Args:
            productId: The ID of the product for the Squarespace API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def squarespace_get_order(
        self,
        orderId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single order in Squarespace by order ID, including line items, status, pricing, and customer details. Use this when you have a specific orderId and need full order details. Use squarespace_list_orders instead when you need to browse or process multiple orders. Does not modify any data.

        Args:
            orderId: The ID of the order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def squarespace_get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single product in your Squarespace store by productId, including name, description, pricing, and inventory data. Use this when you have a specific productId and need full product details. Use squarespace_list_products instead when you need to browse multiple products. Does not modify any data.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def squarespace_get_profile(
        self,
        profileId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single customer profile in Squarespace by profile ID, including contact details and account data. Use this when you have a specific profileId and need full profile details. Use squarespace_list_profiles instead when you need to browse or search across multiple profiles. Does not modify any data.

        Args:
            profileId: The ID of the profile to access on Squarespace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def squarespace_list_orders(
        self,
        modifiedAfter: Optional[str] = None,
        modifiedBefore: Optional[str] = None,
        nextPageCursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all orders in your Squarespace eCommerce store. Use this when you need a full collection of orders, such as for reporting, auditing, or bulk processing. Use squarespace_get_order instead when you need details for a single known order by ID. Does not modify any data.

        Args:
            modifiedAfter: Filter results modified after this timestamp.
            modifiedBefore: Filter results modified before this timestamp.
            nextPageCursor: 
        Returns:
            API response as a dictionary.
        """
        ...

    def squarespace_list_products(
        self,
        nextPageCursor: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all products available in your Squarespace store inventory. Use this when you need to browse, audit, or process multiple products at once. Use squarespace_get_product instead when you need full details for a single known product by ID. Does not modify any data.

        Args:
            nextPageCursor: 
            type: Type parameter for the Squarespace API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def squarespace_list_profiles(
        self,
        nextPageCursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all customer profiles registered in your Squarespace eCommerce platform. Use this when you need to browse, audit, or process multiple customer profiles at once. Use squarespace_get_profile instead when you need details for a single known profile by ID. Does not modify any data.

        Args:
            nextPageCursor: Cursor for retrieving the next page of results from the Squarespace API.
        Returns:
            API response as a dictionary.
        """
        ...

    def squarespace_list_store_pages(
        self,
        nextPageCursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all store pages configured in your Squarespace website, providing the page structure and metadata for the online store. Use this when you need to view or audit the stores page layout and organization. Does not modify any data.

        Args:
            nextPageCursor: Cursor for pagination; used to retrieve the next page of results.
        Returns:
            API response as a dictionary.
        """
        ...

    def squarespace_update_product(
        self,
        productId: str,
        isVisible: Optional[bool] = None,
        name: Optional[str] = None,
        tags: Optional[List[Any]] = None,
        urlSlug: Optional[str] = None,
        variantAttributes: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing product in your Squarespace store inventory, such as name, description, price, or availability, identified by productId. Use this when you need to modify an existing products attributes. Use squarespace_create_product to add a new product instead. This action overwrites existing product data.

        Args:
            productId: ID of the product. (required)
            isVisible: Indicates whether the resource is visible.
            name: Name of the resource.
            tags: Array of tags for the resource.
            urlSlug: URL slug for the resource.
            variantAttributes: Array of variant attributes.
        Returns:
            API response as a dictionary.
        """
        ...

