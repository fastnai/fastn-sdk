"""Fastn Amazon connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AmazonConnector:
    """Amazon connector ().

    Provides 12 tools.
    """

    def create_destination(
        self,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new destination for data or workflow integration in the context of the messaging service.

        Args:
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_or_update_listing(
        self,
    ) -> Dict[str, Any]:
        """Creates a new listing or updates an existing listing in the e-commerce platform.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_subscription(
        self,
        region: Optional[str] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new subscription to a service or data feed in the context of the subscription management system.

        Args:
            region: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_destination(
        self,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific destination in the context of the messaging service.

        Args:
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_listing_item(
        self,
    ) -> Dict[str, Any]:
        """Deletes a specific listing item from the database in the context of the e-commerce platform.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_subscription(
        self,
        region: Optional[str] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing subscription in the context of the subscription management system.

        Args:
            region: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        refresh_token: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a new token for API authentication in the context of the service's security framework.

        Args:
            client_id: 
            client_secret: 
            grant_type: 
            refresh_token: 
            scope: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_destination(
        self,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific destination in the context of the messaging service.

        Args:
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_listing_item(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a specific listing item from the database in the context of the e-commerce platform.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_subscription(
        self,
        region: Optional[str] = None,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific subscription in the context of the subscription management system.

        Args:
            region: 
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def list_destinations(
        self,
        x_amz_access_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all available destinations for data or workflow integration in the context of the messaging service.

        Args:
            x_amz_access_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def partially_update_listing(
        self,
    ) -> Dict[str, Any]:
        """Partially updates an existing listing in the e-commerce platform with the provided details.
        Returns:
            API response as a dictionary.
        """
        ...

