"""Fastn Etsy connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class EtsyConnector:
    """Etsy connector ().

    Provides 8 tools.
    """

    def etsy_create_draft_listing(
        self,
        description: Optional[str] = None,
        image_ids: Optional[List[Any]] = None,
        is_customizable: Optional[bool] = None,
        is_personalizable: Optional[bool] = None,
        is_supply: Optional[bool] = None,
        is_taxable: Optional[bool] = None,
        item_dimensions_unit: Optional[str] = None,
        item_height: Optional[float] = None,
        item_length: Optional[float] = None,
        item_weight: Optional[float] = None,
        item_weight_unit: Optional[str] = None,
        item_width: Optional[float] = None,
        materials: Optional[List[Any]] = None,
        personalization_char_count_max: Optional[int] = None,
        personalization_instructions: Optional[str] = None,
        personalization_is_required: Optional[bool] = None,
        price: Optional[float] = None,
        processing_max: Optional[int] = None,
        processing_min: Optional[int] = None,
        production_partner_ids: Optional[List[Any]] = None,
        quantity: Optional[int] = None,
        return_policy_id: Optional[int] = None,
        shipping_profile_id: Optional[int] = None,
        shop_id: Optional[str] = None,
        shop_section_id: Optional[int] = None,
        should_auto_renew: Optional[bool] = None,
        styles: Optional[List[Any]] = None,
        tags: Optional[List[Any]] = None,
        taxonomy_id: Optional[int] = None,
        title: Optional[str] = None,
        type: Optional[str] = None,
        when_made: Optional[str] = None,
        who_made: Optional[str] = None,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new draft listing in a specified Etsy shop (POST /v3/application/shops/{shop_id}/listings). The listing is saved in draft state and is not publicly visible until explicitly published. Use this when you want to prepare and review a listing before making it live. Do not use this to update an existing listing. This operation creates a new record in the shop and can be reversed by deleting the draft listing.

        Args:
            description: 
            image_ids: 
            is_customizable: 
            is_personalizable: 
            is_supply: 
            is_taxable: 
            item_dimensions_unit: 
            item_height: 
            item_length: 
            item_weight: 
            item_weight_unit: 
            item_width: 
            materials: 
            personalization_char_count_max: 
            personalization_instructions: 
            personalization_is_required: 
            price: 
            processing_max: 
            processing_min: 
            production_partner_ids: 
            quantity: 
            return_policy_id: 
            shipping_profile_id: 
            shop_id: 
            shop_section_id: 
            should_auto_renew: 
            styles: 
            tags: 
            taxonomy_id: 
            title: 
            type: 
            when_made: 
            who_made: 
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def etsy_delete_listing(
        self,
        listing_id: str,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific listing from an Etsy shop (DELETE /v3/application/listings/{listing_id}), removing it from public view and all shop inventory. Use this when a listing needs to be fully removed and is no longer needed. Do not use this to temporarily hide a listing — consider updating its state instead. This operation is irreversible; the listing and its data cannot be recovered after deletion.

        Args:
            listing_id:  (required)
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def etsy_delete_listing_image(
        self,
        listing_id: Optional[str] = None,
        listing_image_id: Optional[str] = None,
        shop_id: Optional[str] = None,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific image from an Etsy listing (DELETE /v3/application/shops/{shop_id}/listings/{listing_id}/images/{listing_image_id}). Use this when you need to remove an outdated or incorrect image from a listing. Do not use this to replace an image — delete the old one and then upload a new one using etsy_upload_listing_image. This operation is irreversible; the deleted image cannot be recovered.

        Args:
            listing_id: 
            listing_image_id: 
            shop_id: 
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def etsy_get_listing(
        self,
        listing_id: Optional[str] = None,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Etsy listing by its listing ID (GET /v3/application/listings/{listing_id}), including title, description, price, tags, and categorization. Use this when you need full details about a single known listing. Do not use this to browse or search multiple listings at once. This is a read-only operation with no side effects.

        Args:
            listing_id: 
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def etsy_get_listing_image(
        self,
        listing_id: str,
        listing_image_id: str,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific image associated with an Etsy listing by its listing ID and image ID (GET /v3/application/listings/{listing_id}/images/{listing_image_id}), returning image metadata and URL. Use this when you need details or the URL for a single known listing image. Do not use this to upload or delete images — use etsy_upload_listing_image or etsy_delete_listing_image instead. This is a read-only operation with no side effects.

        Args:
            listing_id:  (required)
            listing_image_id:  (required)
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def etsy_get_listing_inventory(
        self,
        listing_id: Optional[str] = None,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves inventory details for a specific Etsy listing (GET /v3/application/listings/{listing_id}/inventory), including stock quantities, product offerings, and availability by variation. Use this when you need to check or display current stock levels for a listing. Do not use this to retrieve general listing metadata — use etsy_get_listing instead. This is a read-only operation with no side effects.

        Args:
            listing_id: 
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

    def etsy_get_listing_product(
        self,
        x_Api_Key: str,
        listing_id: Optional[str] = None,
        product_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details for a specific product variant within an Etsy listings inventory (GET /v3/application/listings/{listing_id}/inventory/products/{product_id}), including pricing, SKU, and availability for that variation. Use this when you need precise details about a single product variant rather than the full inventory. Do not use this to retrieve all inventory variants at once — use etsy_get_listing_inventory instead. This is a read-only operation with no side effects.

        Args:
            x_Api_Key:  (required)
            listing_id: 
            product_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def etsy_upload_listing_image(
        self,
        listing_id: str,
        shop_id: str,
        alt_text: Optional[str] = None,
        image: Optional[str] = None,
        is_watermarked: Optional[str] = None,
        listing_image_id: Optional[str] = None,
        overwrite: Optional[str] = None,
        rank: Optional[str] = None,
        x_Api_Key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a new image to a specific Etsy listing (POST /v3/application/shops/{shop_id}/listings/{listing_id}/images), associating it with the listing for display in the marketplace. Use this when you need to add or replace visual content for a listing. Ensure the image meets Etsys format and size requirements before uploading. Do not use this to retrieve or delete existing images — use etsy_get_listing_image or etsy_delete_listing_image instead. This operation creates a new image record on the listing.

        Args:
            listing_id:  (required)
            shop_id:  (required)
            alt_text: 
            image: 
            is_watermarked: 
            listing_image_id: 
            overwrite: 
            rank: 
            x_Api_Key: 
        Returns:
            API response as a dictionary.
        """
        ...

