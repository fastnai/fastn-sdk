"""Fastn Etsy connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class EtsyConnector:
    """Etsy connector ().

    Provides 8 tools.
    """

    def create_draft_listing(
        self,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a draft version of a new listing in the marketplace, enabling preparation and review before it goes live.

        Args:
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_listing(
        self,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific listing from the marketplace, removing it from public view and availability.

        Args:
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_listing_image(
        self,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an image associated with a specific listing in the marketplace, helping to maintain and update the visual assets of the product.

        Args:
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_listing(
        self,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific listing in the marketplace, including its descriptions, pricing, and categorization.

        Args:
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_listing_image(
        self,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves an image from a specific listing in the marketplace, providing access to the visual representation of the product.

        Args:
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_listing_inventory(
        self,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets inventory information for a specific listing in the marketplace, offering insights into stock levels and availability.

        Args:
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_listing_product(
        self,
        x_Api_Key: str,
    ) -> Dict[str, Any]:
        """Retrieves product details for a given listing in the marketplace, allowing for insights into pricing, availability, and specifications.

        Args:
            x_Api_Key:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_listing_image(
        self,
    ) -> Dict[str, Any]:
        """Uploads an image to a specific listing in the marketplace, enabling the enhancement of product presentation through visual content.
        Returns:
            API response as a dictionary.
        """
        ...

