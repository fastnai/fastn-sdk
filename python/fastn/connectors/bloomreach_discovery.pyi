"""Fastn Bloomreach Discovery connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class BloomreachDiscoveryConnector:
    """Bloomreach Discovery connector ().

    Provides 4 tools.
    """

    def bloomreach_discovery_get_category_recommendations(
        self,
        _br_uid_2: Optional[str] = None,
        account_id: Optional[str] = None,
        cat_id: Optional[str] = None,
        domain_key: Optional[str] = None,
        facet: Optional[bool] = None,
        recs_pathways_host: Optional[str] = None,
        url: Optional[str] = None,
        widget_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns AI-driven product recommendations for a specific category using a configured Bloomreach Discovery recommendations widget. Use this tool when you need to surface relevant products to a user who is browsing or has shown affinity toward a particular category. Requires a widget ID that must be pre-configured in Bloomreach Discovery. Does not modify any data. Do not use this tool for keyword-based product search — use bloomreach_discovery_search_product instead.

        Args:
            _br_uid_2: 
            account_id: 
            cat_id: 
            domain_key: 
            facet: 
            recs_pathways_host: 
            url: 
            widget_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_discovery_search_category(
        self,
        account_id: str,
        domain_key: str,
        request_type: str,
        rows: str,
        search_type: str,
        start: str,
        url: str,
        auth_key: Optional[str] = None,
        efq: Optional[str] = None,
        fl: Optional[str] = None,
        fq: Optional[str] = None,
        q: Optional[str] = None,
        ref_url: Optional[str] = None,
        request_id: Optional[str] = None,
        search_host: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for product categories in the Bloomreach Discovery index based on specified query criteria, returning matching category names, IDs, and metadata. Use this tool when you need to find relevant categories for navigation, filtering, or merchandising purposes. Does not modify any data. Do not use this tool to search for individual products — use bloomreach_discovery_search_product instead.

        Args:
            account_id:  (required)
            domain_key:  (required)
            request_type:  (required)
            rows:  (required)
            search_type:  (required)
            start:  (required)
            url:  (required)
            auth_key: 
            efq: 
            fl: 
            fq: 
            q: 
            ref_url: 
            request_id: 
            search_host: 
            sort: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_discovery_search_content(
        self,
        account_id: str,
        domain_key: str,
        fl: str,
        q: str,
        rows: str,
        search_host: str,
        search_type: str,
        _br_uid_2: Optional[str] = None,
        auth_key: Optional[str] = None,
        catalog_name: Optional[str] = None,
        ref_url: Optional[str] = None,
        request_type: Optional[str] = None,
        start: Optional[str] = None,
        url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for content items such as articles, blog posts, or multimedia assets in the Bloomreach Discovery index based on a user-provided query or criteria. Use this tool when you need to find and retrieve non-product content by keyword or relevance. Does not modify any data. Do not use this tool to search for products or categories — use bloomreach_discovery_search_product or bloomreach_discovery_search_category instead.

        Args:
            account_id:  (required)
            domain_key:  (required)
            fl:  (required)
            q:  (required)
            rows:  (required)
            search_host:  (required)
            search_type:  (required)
            _br_uid_2: 
            auth_key: 
            catalog_name: 
            ref_url: 
            request_type: 
            start: 
            url: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_discovery_search_product(
        self,
        account_id: str,
        domain_key: str,
        ref_url: str,
        request_type: str,
        rows: str,
        search_type: str,
        start: str,
        url: str,
        _br_uid_2: Optional[str] = None,
        auth_key: Optional[str] = None,
        efq: Optional[str] = None,
        fl: Optional[str] = None,
        fq: Optional[str] = None,
        q: Optional[str] = None,
        request_id: Optional[str] = None,
        search_host: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for products in the Bloomreach Discovery index based on a user query, returning ranked product results with details such as name, price, and attributes. Use this tool when you need to retrieve products matching a keyword search or user intent. Does not modify any data. Do not use this tool to search for content or categories — use bloomreach_discovery_search_content or bloomreach_discovery_search_category instead.

        Args:
            account_id:  (required)
            domain_key:  (required)
            ref_url:  (required)
            request_type:  (required)
            rows:  (required)
            search_type:  (required)
            start:  (required)
            url:  (required)
            _br_uid_2: 
            auth_key: 
            efq: 
            fl: 
            fq: 
            q: 
            request_id: 
            search_host: 
            sort: 
        Returns:
            API response as a dictionary.
        """
        ...

