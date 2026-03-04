"""Fastn Google Ads connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _GoogleAdsSearchSearchsettings(TypedDict, total=False):
    omitResults: bool
    returnSummaryRow: bool
    returnTotalResultsCount: bool

class GoogleAdsConnector:
    """Google Ads connector ().

    Provides 2 tools.
    """

    def google_ads_list_customers(
        self,
    ) -> Dict[str, Any]:
        """Lists all Google Ads customer accounts accessible to the authenticated user by calling the listAccessibleCustomers endpoint. Use this tool when you need to discover which customer account IDs are available before performing account-specific operations such as running reports or managing campaigns. Do not use this tool to retrieve detailed campaign, ad group, or billing information — use a search or reporting tool for those needs. Returns a list of resource names for accessible customer accounts.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_ads_search(
        self,
        customerId: Optional[str] = None,
        pageToken: Optional[str] = None,
        query: Optional[str] = None,
        searchSettings: Optional[_GoogleAdsSearchSearchsettings] = None,
        validateOnly: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Executes a Google Ads Query Language (GAQL) search request against a specific Google Ads customer account to retrieve campaign, ad group, ad, keyword, or performance data. Use this tool when you need to query structured advertising data for a known customer account (customerId). Do not use this tool to list accessible customers — use google_ads_list_customers for that. Requires a valid GAQL query string in the request body. This is a read-only operation and does not modify any advertising data.

        Args:
            customerId: 
            pageToken: 
            query: 
            searchSettings: 
            validateOnly: 
        Returns:
            API response as a dictionary.
        """
        ...

