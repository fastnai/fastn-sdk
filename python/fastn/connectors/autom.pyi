"""Fastn Autom connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AutomConnector:
    """Autom connector ().

    Provides 6 tools.
    """

    def bing_search(
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
        """Executes a web search utilizing the Bing Search connector to gather diverse results from the Bing search engine.

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

    def brave_search(
        self,
        query: str,
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Conducts a web search through the Brave Search connector, allowing users to access information while prioritizing privacy.

        Args:
            query: The search query for the Autom API. (required)
            page: The page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_usage(
        self,
    ) -> Dict[str, Any]:
        """Retrieves usage statistics from the getUsage connector to analyze and report on system or application performance.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_images(
        self,
        query: str,
        gl: Optional[str] = None,
        hl: Optional[str] = None,
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Searches for and retrieves images using the Google Images connector to find relevant visual content based on user queries.

        Args:
            query: The search query string. (required)
            gl: Geo location code for search results.
            hl: Language code for search results.
            page: Page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_search(
        self,
        gl: Optional[str] = None,
        hl: Optional[str] = None,
        location: Optional[str] = None,
        num: Optional[int] = None,
        page: Optional[int] = None,
        query: Optional[str] = None,
        uule: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Performs a web search using the Google Search connector to retrieve relevant information from the internet.

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

    def google_search_autocomplete(
        self,
        query: str,
        cp: Optional[int] = None,
        gl: Optional[str] = None,
        hl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates autocomplete suggestions for search queries with the Google Search Autocomplete connector to enhance user search experiences.

        Args:
            query: The search query to be executed. (required)
            cp: Number of results per page.
            gl: Country code for the response (e.g., 'US').
            hl: Language code for the response (e.g., 'en').
        Returns:
            API response as a dictionary.
        """
        ...

