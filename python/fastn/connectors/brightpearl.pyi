"""Fastn Brightpearl connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class BrightpearlConnector:
    """Brightpearl connector ().

    Provides 9 tools.
    """

    def brightpearl_create_webhook(
        self,
        bodyTemplate: Optional[str] = None,
        contentType: Optional[str] = None,
        httpMethod: Optional[str] = None,
        idSetAccepted: Optional[bool] = None,
        qualityOfService: Optional[int] = None,
        subscribeTo: Optional[str] = None,
        uriTemplate: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook subscription in Brightpearl so that your system receives real-time HTTP callbacks when specific platform events occur (e.g. order created, stock updated). Use this when you want to set up event-driven integrations with Brightpearl. Do not use this to retrieve or update existing webhooks. Note: creating a webhook is a persistent configuration change in Brightpearl that must be explicitly deleted to remove.

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

    def brightpearl_get_category(
        self,
        catId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single Brightpearl product category by its category ID, including its name and hierarchy information. Use this when you need metadata for a specific category. Do not use this to browse all categories or to search for products within a category — use brightpearl_search_products for product discovery.

        Args:
            catId: Identifier for the category. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def brightpearl_get_price_list(
        self,
        priceListId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves the price for a specific product from a named price list in Brightpearl, identified by product ID and price list ID. Use this when you need the price of a product under a particular pricing tier, customer group, or currency. Do not use this to retrieve all prices for a product across all lists — use brightpearl_list_product_prices for that.

        Args:
            priceListId: ID of the price list. (required)
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def brightpearl_get_price_options(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the allowed request options (e.g. supported HTTP methods, headers, and parameters) for the Brightpearl product-price endpoint. Use this to discover what operations and fields are available before making pricing requests. Do not use this to fetch actual product prices — use brightpearl_get_product_prices or brightpearl_get_price_list for that.
        Returns:
            API response as a dictionary.
        """
        ...

    def brightpearl_get_product(
        self,
        productIds: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information for one or more Brightpearl products by their product IDs, including descriptions, specifications, availability, and attributes. Use this when you have specific product IDs and need full product records. Do not use this to search for products by keyword or filter — use brightpearl_search_products for that.

        Args:
            productIds: Comma-separated list of product IDs. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def brightpearl_get_product_options(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the allowed request options (e.g. supported HTTP methods, headers, and parameters) for the Brightpearl product endpoint. Use this to discover what operations and fields are supported before making product requests. Do not use this to fetch product details or variations — use brightpearl_get_product for that.
        Returns:
            API response as a dictionary.
        """
        ...

    def brightpearl_list_product_prices(
        self,
        productIds: str,
    ) -> Dict[str, Any]:
        """Retrieves all current pricing information for one or more products in Brightpearl by their product IDs, covering all configured price lists. Use this when you need a full pricing overview for specific products. Do not use this to fetch prices from a single named price list — use brightpearl_get_price_list for that.

        Args:
            productIds: Comma-separated list of product IDs. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def brightpearl_list_webhooks(
        self,
        id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the configuration details of all webhooks registered in Brightpearl, including endpoint URLs, subscribed events, and status for each webhook. Use this to review all configured webhooks. Do not use this to create new webhooks or to retrieve details of a single webhook by ID.

        Args:
            id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def brightpearl_search_products(
        self,
        columns: Optional[str] = None,
        firstResult: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches the Brightpearl product catalogue using query parameters such as name, SKU, or category to return matching products. Use this when you need to find products by keyword or filter criteria rather than by a known product ID. Do not use this when you already have specific product IDs — use brightpearl_get_product for direct lookups.

        Args:
            columns: Specifies the columns to be returned in the response.
            firstResult: Index of the first record to be returned.
            pageSize: Number of records to return per page.
        Returns:
            API response as a dictionary.
        """
        ...

