"""Fastn Google Custom Search connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GoogleCustomSearchConnector:
    """Google Custom Search connector ().

    Provides 1 tools.
    """

    def get_links_of_query(
        self,
        cx: Optional[str] = None,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of links related to a specific query using the getLinksOfQuery endpoint.

        Args:
            cx: The custom search engine ID (cx) to use for the Google Custom Search API.
            q: The search query string for the Google Custom Search API.
        Returns:
            API response as a dictionary.
        """
        ...

