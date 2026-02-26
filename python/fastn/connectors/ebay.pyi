"""Fastn Ebay connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class EbayConnector:
    """Ebay connector ().

    Provides 34 tools.
    """

    def create_destination(
        self,
        deliveryConfig: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new destination for items within the logistics management system.

        Args:
            deliveryConfig: 
            name: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_fixed_price_item(
        self,
        AddFixedPriceItemRequest: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new fixed price item in the inventory management system.

        Args:
            AddFixedPriceItemRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_item(
        self,
        AddItemRequest: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new item in the inventory management system.

        Args:
            AddItemRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_new_inventory_item(
        self,
        availability: Optional[Dict[str, Any]] = None,
        condition: Optional[str] = None,
        packageWeightAndSize: Optional[Dict[str, Any]] = None,
        product: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new inventory item in the inventory management system.

        Args:
            availability: 
            condition: 
            packageWeightAndSize: 
            product: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_new_location(
        self,
        location: Optional[Dict[str, Any]] = None,
        locationInstructions: Optional[str] = None,
        locationTypes: Optional[List[Any]] = None,
        merchantLocationStatus: Optional[str] = None,
        name: Optional[str] = None,
        operatingHours: Optional[List[Any]] = None,
        phone: Optional[str] = None,
        specialHours: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new location within the inventory management system.

        Args:
            location: 
            locationInstructions: 
            locationTypes: 
            merchantLocationStatus: 
            name: 
            operatingHours: 
            phone: 
            specialHours: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_offer(
        self,
        availableQuantity: Optional[int] = None,
        categoryId: Optional[str] = None,
        format: Optional[str] = None,
        listingDescription: Optional[str] = None,
        listingPolicies: Optional[Dict[str, Any]] = None,
        marketplaceId: Optional[str] = None,
        merchantLocationKey: Optional[str] = None,
        pricingSummary: Optional[Dict[str, Any]] = None,
        quantityLimitPerBuyer: Optional[int] = None,
        sku: Optional[str] = None,
        tax: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new offer for products or services in the promotions management system.

        Args:
            availableQuantity: 
            categoryId: 
            format: 
            listingDescription: 
            listingPolicies: 
            marketplaceId: 
            merchantLocationKey: 
            pricingSummary: 
            quantityLimitPerBuyer: 
            sku: 
            tax: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_subscription(
        self,
        destinationId: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
        status: Optional[str] = None,
        topicId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new subscription for a user or service in the subscription management system.

        Args:
            destinationId: 
            payload: 
            status: 
            topicId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_inventory_item(
        self,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified inventory item from the inventory management system.

        Args:
            sku: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_location(
        self,
        locationName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified location from the inventory management system.

        Args:
            locationName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_offer(
        self,
        offerId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified offer from the promotions management system.

        Args:
            offerId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_subscription(
        self,
        subscriptionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified subscription from the subscription management system.

        Args:
            subscriptionId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def disable_location(
        self,
        locationName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Disables an existing location to restrict its use in the inventory management system.

        Args:
            locationName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def disable_subscription(
        self,
        subscriptionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Disables a subscription to restrict service access in the subscription management system.

        Args:
            subscriptionId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def enable_location(
        self,
        locationName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Enables an existing location to become active within the inventory management system.

        Args:
            locationName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def enable_subscription(
        self,
        subscriptionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Enables an existing subscription to allow service access in the subscription management system.

        Args:
            subscriptionId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def end_item(
        self,
        EndItemRequest: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Ends the listing of a specified item in the inventory management system.

        Args:
            EndItemRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def end_items(
        self,
        EndItemsRequest: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Ends the listings of multiple items in the inventory management system.

        Args:
            EndItemsRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_application_auth_token(
        self,
        Authorization: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates an application authentication token for use in the API integration with the specified application.

        Args:
            Authorization: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inventory_item(
        self,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific inventory item from the inventory management system.

        Args:
            sku: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inventory_location(
        self,
        locationName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific inventory location in the inventory management system.

        Args:
            locationName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inventory_locations(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all inventory locations in the inventory management system.

        Args:
            limit: 
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_item(
        self,
        GetItemRequest: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific item from the inventory management system.

        Args:
            GetItemRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_item_by_legacy_item_id(
        self,
        X_EBAY_C_MARKETPLACE_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves an item based on its legacy item ID from the inventory management system.

        Args:
            X_EBAY_C_MARKETPLACE_ID: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_merchandised_products(
        self,
        X_EBAY_C_MARKETPLACE_ID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of merchandised products from the merchandising management system.

        Args:
            X_EBAY_C_MARKETPLACE_ID: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_refresh_token(
        self,
        authToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a refresh token for re-authentication in the API integration with the specified service.

        Args:
            authToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_seller_list(
        self,
        GetSellerListRequest: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of sellers from the seller management system.

        Args:
            GetSellerListRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def list_inventory_item(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all inventory items in the specified inventory management system.

        Args:
            limit: 
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def publish_offer(
        self,
        offerId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Publishes an existing offer to make it available to customers in the promotions management system.

        Args:
            offerId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def revise_fixed_price_item(
        self,
        ReviseFixedPriceItemRequest: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Revises the details of a fixed price item in the inventory management system.

        Args:
            ReviseFixedPriceItemRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def revise_item(
        self,
        ReviseItemRequest: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Revises the details of an existing item in the inventory management system.

        Args:
            ReviseItemRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def search_products(
        self,
        X_EBAY_API_CALL_NAME: Optional[str] = None,
        X_EBAY_API_VERSION: Optional[str] = None,
        X_EBAY_C_MARKETPLACE_ID: Optional[str] = None,
        authToken: Optional[str] = None,
        base_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for products in the product catalog within the specified marketplace or store.

        Args:
            X_EBAY_API_CALL_NAME: 
            X_EBAY_API_VERSION: 
            X_EBAY_C_MARKETPLACE_ID: 
            authToken: 
            base_url: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_destination(
        self,
        deliveryConfig: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing destination in the logistics management system.

        Args:
            deliveryConfig: 
            name: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_offer(
        self,
        availableQuantity: Optional[int] = None,
        categoryId: Optional[str] = None,
        includeCatalogProductDetails: Optional[bool] = None,
        listingDescription: Optional[str] = None,
        listingPolicies: Optional[Dict[str, Any]] = None,
        pricingSummary: Optional[Dict[str, Any]] = None,
        quantityLimitPerBuyer: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing offer in the promotions management system.

        Args:
            availableQuantity: 
            categoryId: 
            includeCatalogProductDetails: 
            listingDescription: 
            listingPolicies: 
            pricingSummary: 
            quantityLimitPerBuyer: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_subscription(
        self,
        destinationId: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing subscription in the subscription management system.

        Args:
            destinationId: 
            payload: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

