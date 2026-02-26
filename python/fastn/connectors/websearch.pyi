"""Fastn Websearch connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class WebsearchConnector:
    """Websearch connector ().

    Provides 1 tools.
    """

    def web_search(
        self,
        country: str,
        includeContent: bool,
        language: str,
        maxResults: int,
        query: str,
    ) -> Dict[str, Any]:
        """Performs a comprehensive web search to gather relevant information from online sources.

        Args:
            country: Country code (ISO 3166-1 alpha-2) to localize the search results (e.g., 'us', 'gb'). (required)
            includeContent: Whether to include the full content of the search results in the response. (required)
            language: Language code (ISO 639-1) to filter search results by language (e.g., 'en', 'es'). (required)
            maxResults: Maximum number of search results to return. (required)
            query: The search query string to be processed by the AI-powered search engine. (required)
        Returns:
            API response as a dictionary.
        """
        ...

