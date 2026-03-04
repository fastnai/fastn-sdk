"""Fastn SAP connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class SapConnector:
    """SAP connector ().

    Provides 4 tools.
    """

    def sap_create_access_token(
        self,
        authToken: str,
        grant_type: str,
        password: str,
        username: str,
        baseUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Requests and returns an OAuth access token from the SAP authorization server to authenticate subsequent API calls. Use this as a prerequisite step before calling other SAP tools that require bearer token authentication. This tool posts credentials to the OAuth token endpoint and should not be used to read or modify business data.

        Args:
            authToken:  (required)
            grant_type:  (required)
            password:  (required)
            username:  (required)
            baseUrl: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sap_list_contacts(
        self,
        api_key: str,
        count: str,
        data_ServiceVersion: str,
        pageSize: str,
    ) -> Dict[str, Any]:
        """Returns a list of business partner contacts from SAP Subscription Billing, including names, email addresses, and phone numbers. Use this when you need to retrieve or review contact records for business partners. Do not use this to fetch customer account records — use sap_list_customers for that.

        Args:
            api_key:  (required)
            count:  (required)
            data_ServiceVersion:  (required)
            pageSize:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sap_list_customers(
        self,
        api_key: str,
        count: str,
        data_ServiceVersion: str,
        pageSize: str,
    ) -> Dict[str, Any]:
        """Returns a list of customer records from SAP Subscription Billing, including customer names, contact information, and account status. Use this when you need to review or search available customer accounts. To retrieve contact-level details for business partners, use sap_list_contacts instead.

        Args:
            api_key:  (required)
            count:  (required)
            data_ServiceVersion:  (required)
            pageSize:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sap_list_products(
        self,
        api_key: str,
        count: str,
        data_ServiceVersion: str,
        pageSize: str,
    ) -> Dict[str, Any]:
        """Returns a list of products from SAP Subscription Billing, including product names, descriptions, prices, and availability. Use this when you need to browse or audit the product catalog. To retrieve details for a single product, use a dedicated get product tool if available.

        Args:
            api_key:  (required)
            count:  (required)
            data_ServiceVersion:  (required)
            pageSize:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

