"""Fastn Autom connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AutomConnector:
    """Autom connector ().

    Provides 6 tools.
    """

    def autom_bing_search(
        self,
        query: str,
        cc: Optional[str] = None,
        lat: Optional[int] = None,
        location: Optional[str] = None,
        lon: Optional[int] = None,
        mkt: Optional[str] = None,
        num: Optional[int] = None,
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Performs a web search using the Bing search engine and returns diverse search results including web pages, news, and other content. Use this tool when you need to retrieve search results specifically from Bing. Do not use this tool when you need Google-specific results, image search, or search autocomplete suggestions.

        Args:
            query: Search query. (required)
            cc: Carbon copy recipients.
            lat: Latitude coordinate.
            location: Location parameter.
            lon: Longitude coordinate.
            mkt: Market identifier.
            num: Numerical parameter.
            page: Pagination parameter.
        Returns:
            API response as a dictionary.
        """
        ...

    def autom_brave_search(
        self,
        query: str,
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Performs a privacy-focused web search using the Brave search engine and returns search results. Use this tool when you need web search results from Braves independent index, especially when privacy is a priority. Do not use this tool when you need results from Google or Bing specifically, or when you need image search or autocomplete suggestions.

        Args:
            query: The search query for the Autom API. (required)
            page: The page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def autom_get_usage(
        self,
    ) -> Dict[str, Any]:
        """Retrieves current API usage statistics for the authenticated Autom.dev account, including request counts and consumption metrics. Use this tool when you need to monitor API quota consumption or audit usage. Do not use this tool to perform searches or retrieve external content.
        Returns:
            API response as a dictionary.
        """
        ...

    def autom_google_images_search(
        self,
        query: str,
        gl: Optional[str] = None,
        hl: Optional[str] = None,
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Searches for and retrieves image results from Google Images based on a provided query. Returns image URLs and metadata for visually relevant content. Use this tool when you need to find images matching a search query. Do not use this tool for general web searches, news searches, or autocomplete suggestions.

        Args:
            query: The search query string. (required)
            gl: Geo location code for search results.
            hl: Language code for search results.
            page: Page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def autom_google_search(
        self,
        gl: Optional[str] = None,
        hl: Optional[str] = None,
        location: Optional[str] = None,
        num: Optional[int] = None,
        page: Optional[int] = None,
        query: Optional[str] = None,
        uule: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Performs a web search using Google Search and returns relevant results including web pages, snippets, and links. Use this tool when you need to retrieve general search results from Google. Do not use this tool when you need image results (use autom_google_images_search), autocomplete suggestions (use autom_google_search_autocomplete), or results from Bing or Brave.

        Args:
            gl: Geographic location code (country code).
            hl: Language code for localized results.
            location: Geographic location to filter results.
            num: Number of results to return per page.
            page: Page number for pagination.
            query: The search term or phrase.
            uule: User's location for personalized results.
        Returns:
            API response as a dictionary.
        """
        ...

    def autom_google_search_autocomplete(
        self,
        query: str,
        cp: Optional[int] = None,
        gl: Optional[str] = None,
        hl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates autocomplete query suggestions from Google Search based on a partial search query. Use this tool when you need to discover popular or predicted search terms related to a topic, or to enhance a search interface with suggestions. Do not use this tool to retrieve full search results or images.

        Args:
            query: The search query to be executed. (required)
            cp: Number of results per page.
            gl: Country code for the response (e.g., 'US').
            hl: Language code for the response (e.g., 'en').
        Returns:
            API response as a dictionary.
        """
        ...

