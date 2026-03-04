"""Fastn Google Custom Search connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class GoogleCustomSearchConnector:
    """Google Custom Search connector ().

    Provides 1 tools.
    """

    def google_custom_search_list_links(
        self,
        cx: Optional[str] = None,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Performs a web search using the Google Custom Search API and returns a list of result links matching the specified query. Use this when you need to retrieve URLs from a configured custom search engine for a given search term. Results are scoped to the search engine configuration defined in your API credentials — it does not perform an unrestricted Google web search. Does not return page content, only URLs and result metadata.

        Args:
            cx: The custom search engine ID (cx) to use for the Google Custom Search API.
            q: The search query string for the Google Custom Search API.
        Returns:
            API response as a dictionary.
        """
        ...

