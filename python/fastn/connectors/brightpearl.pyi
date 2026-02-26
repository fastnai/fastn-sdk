"""Fastn Brightpearl connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BrightpearlConnector:
    """Brightpearl connector ().

    Provides 9 tools.
    """

    def create_webhook(
        self,
        bodyTemplate: Optional[str] = None,
        contentType: Optional[str] = None,
        httpMethod: Optional[str] = None,
        idSetAccepted: Optional[bool] = None,
        qualityOfService: Optional[int] = None,
        subscribeTo: Optional[str] = None,
        uriTemplate: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the e-commerce system to allow users to receive real-time notifications for specific events.

        Args:
            bodyTemplate: 
            contentType: 
            httpMethod: 
            idSetAccepted: 
            qualityOfService: 
            subscribeTo: 
            uriTemplate: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_category(
        self,
        catId: str,
    ) -> Dict[str, Any]:
        """Fetches product categories from the e-commerce platform to help users navigate and find products in organized groups.

        Args:
            catId: Identifier for the category. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_price_list(
        self,
        priceListId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Fetches a list of prices for various products in the e-commerce database to enable users to see price variations.

        Args:
            priceListId: ID of the price list. (required)
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product(
        self,
        productIds: str,
    ) -> Dict[str, Any]:
        """Provides detailed information about a specific product in the e-commerce system, including descriptions, specifications, and availability.

        Args:
            productIds: Comma-separated list of product IDs. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_prices(
        self,
        productIds: str,
    ) -> Dict[str, Any]:
        """Retrieves current pricing information for a specific product from the e-commerce platform to assist users in comparing costs.

        Args:
            productIds: Comma-separated list of product IDs. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhooks(
        self,
        id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the currently configured webhooks from the e-commerce platform to inform users about system events they can subscribe to.

        Args:
            id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def price_options(
        self,
    ) -> Dict[str, Any]:
        """Fetches pricing options for products, allowing users to view different plans, discounts, or subscription types in the e-commerce system.
        Returns:
            API response as a dictionary.
        """
        ...

    def product_options(
        self,
    ) -> Dict[str, Any]:
        """Retrieves available options for a specific product, such as sizes, colors, or variations, within the e-commerce store.
        Returns:
            API response as a dictionary.
        """
        ...

    def product_search(
        self,
        columns: Optional[str] = None,
        firstResult: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for products in the specified e-commerce database to help users find items that match their query.

        Args:
            columns: Specifies the columns to be returned in the response.
            firstResult: Index of the first record to be returned.
            pageSize: Number of records to return per page.
        Returns:
            API response as a dictionary.
        """
        ...

