"""Fastn Google Ads connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GoogleAdsConnector:
    """Google Ads connector ().

    Provides 2 tools.
    """

    def get_customers(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of customers from the customer management system for review or processing.
        Returns:
            API response as a dictionary.
        """
        ...

    def search(
        self,
        pageToken: Optional[str] = None,
        query: Optional[str] = None,
        searchSettings: Optional[Dict[str, Any]] = None,
        validateOnly: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Searches for specific information or data across various sources within the system.

        Args:
            pageToken: 
            query: 
            searchSettings: 
            validateOnly: 
        Returns:
            API response as a dictionary.
        """
        ...

