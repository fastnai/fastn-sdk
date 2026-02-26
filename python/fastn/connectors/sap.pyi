"""Fastn SAP connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SapConnector:
    """SAP connector ().

    Provides 4 tools.
    """

    def access_token(
        self,
    ) -> Dict[str, Any]:
        """Retrieves an access token for authentication purposes from the specified connector, allowing secure access to APIs and services.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
        api_key: str,
        data_ServiceVersion: str,
    ) -> Dict[str, Any]:
        """Obtains contact information from the specified connector, including names, email addresses, phone numbers, and other relevant data.

        Args:
            api_key:  (required)
            data_ServiceVersion:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customers(
        self,
        api_key: str,
        data_ServiceVersion: str,
    ) -> Dict[str, Any]:
        """Fetches a list of customers from the designated connector, providing details such as names, contact information, and account status.

        Args:
            api_key:  (required)
            data_ServiceVersion:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
        api_key: str,
        data_ServiceVersion: str,
    ) -> Dict[str, Any]:
        """Retrieves product information from the designated connector, including product names, descriptions, prices, and availability.

        Args:
            api_key:  (required)
            data_ServiceVersion:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

