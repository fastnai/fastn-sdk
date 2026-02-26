"""Fastn Bloomreach Discovery connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BloomreachDiscoveryConnector:
    """Bloomreach Discovery connector ().

    Provides 4 tools.
    """

    def category_based_recommendation(
        self,
    ) -> Dict[str, Any]:
        """Generates product recommendations based on category preferences using the categoryBasedRecommendation tool in the recommendation engine connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def search_category(
        self,
    ) -> Dict[str, Any]:
        """Utilizes the searchCategory tool in the e-commerce connector to find and list categories of products based on specified criteria.
        Returns:
            API response as a dictionary.
        """
        ...

    def search_content(
        self,
    ) -> Dict[str, Any]:
        """Employs the searchContent tool in the content management connector to search for specific articles, blog posts, or multimedia based on user indications.
        Returns:
            API response as a dictionary.
        """
        ...

    def search_product(
        self,
    ) -> Dict[str, Any]:
        """Searches for a product using the searchProduct tool in the e-commerce connector to retrieve product information based on user queries.
        Returns:
            API response as a dictionary.
        """
        ...

