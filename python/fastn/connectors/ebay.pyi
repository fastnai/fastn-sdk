"""Fastn Ebay connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _EbayCreateDestinationDeliveryconfig(TypedDict, total=False):
    endpoint: str
    verificationToken: str

class _EbayCreateFixedPriceItemAddfixedpriceitemrequest(TypedDict, total=False):
    _xmlns: str
    ErrorLanguage: str
    Item: Dict[str, Any]
    MessageID: str
    Version: str
    WarningLevel: str

class _EbayCreateInventoryItemAvailability(TypedDict, total=False):
    shipToLocationAvailability: Dict[str, Any]

class _EbayCreateInventoryItemPackageweightandsize(TypedDict, total=False):
    dimensions: Dict[str, Any]
    weight: Dict[str, Any]

class _EbayCreateInventoryItemProduct(TypedDict, total=False):
    aspects: Dict[str, Any]
    description: str
    imageUrls: List[Any]
    title: str
    upc: List[Any]

class _EbayCreateItemAdditemrequest(TypedDict, total=False):
    _xmlns: str
    ErrorHandling: str
    ErrorLanguage: str
    Item: Dict[str, Any]
    MessageID: str
    Version: str
    WarningLevel: str

class _EbayCreateLocationLocation(TypedDict, total=False):
    address: Dict[str, Any]

class _EbayCreateOfferListingpolicies(TypedDict, total=False):
    fulfillmentPolicyId: str
    paymentPolicyId: str
    returnPolicyId: str

class _EbayCreateOfferPricingsummary(TypedDict, total=False):
    price: Dict[str, Any]

class _EbayCreateOfferTax(TypedDict, total=False):
    applyTax: bool
    thirdPartyTaxCategory: str
    vatPercentage: float

class _EbayCreateSubscriptionPayload(TypedDict, total=False):
    deliveryProtocol: str
    format: str
    schemaVersion: str

class _EbayEndItemEnditemrequest(TypedDict, total=False):
    _comment: str
    _xmlns: str
    EndingReason: str
    ErrorLanguage: str
    ItemID: str
    WarningLevel: str

class _EbayEndItemsEnditemsrequest(TypedDict, total=False):
    _xmlns: str
    EndItemRequestContainer: List[Any]
    ErrorLanguage: str
    WarningLevel: str

class _EbayGetItemGetitemrequest(TypedDict, total=False):
    _comment: str
    _xmlns: str
    ErrorLanguage: str
    ItemID: str
    WarningLevel: str

class _EbayListSellersGetsellerlistrequest(TypedDict, total=False):
    _xmlns: str
    AdminEndedItemsOnly: str
    CategoryID: str
    DetailLevel: str
    EndTimeFrom: str
    EndTimeTo: str
    ErrorLanguage: str
    GranularityLevel: str
    IncludeVariations: str
    IncludeWatchCount: str
    MessageID: str
    MotorsDealerUsers: Dict[str, Any]
    OutputSelector: str
    Pagination: Dict[str, Any]
    SKUArray: Dict[str, Any]
    Sort: str
    StartTimeFrom: str
    StartTimeTo: str
    Version: str
    WarningLevel: str

class _EbayReviseFixedPriceItemRevisefixedpriceitemrequest(TypedDict, total=False):
    _xmlns: str
    DeletedField: str
    ErrorLanguage: str
    Item: Dict[str, Any]
    MessageID: str
    Version: str
    WarningLevel: str

class _EbayReviseItemReviseitemrequest(TypedDict, total=False):
    _xmlns: str
    DeletedField: str
    ErrorHandling: str
    ErrorLanguage: str
    InvocationID: str
    Item: Dict[str, Any]
    MessageID: str
    VerifyOnly: str
    Version: str
    WarningLevel: str

class _EbayUpdateDestinationDeliveryconfig(TypedDict, total=False):
    endpoint: str
    verificationToken: str

class _EbayUpdateOfferListingpolicies(TypedDict, total=False):
    fulfillmentPolicyId: str
    paymentPolicyId: str
    returnPolicyId: str

class _EbayUpdateOfferPricingsummary(TypedDict, total=False):
    price: Dict[str, Any]

class _EbayUpdateSubscriptionPayload(TypedDict, total=False):
    deliveryProtocol: str
    format: str
    schemaVersion: str

class EbayConnector:
    """Ebay connector ().

    Provides 34 tools.
    """

    def ebay_create_destination(
        self,
        deliveryConfig: Optional[_EbayCreateDestinationDeliveryconfig] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new notification destination in the eBay Commerce Notification system, defining a delivery endpoint (e.g., a webhook URL) where eBay will send event notifications. Use this before creating subscriptions that require a destination to receive notifications. This action creates a persistent resource; do not call it repeatedly for the same endpoint. Do not use this to update an existing destination — use ebay_update_destination instead.

        Args:
            deliveryConfig: 
            name: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_create_fixed_price_item(
        self,
        AddFixedPriceItemRequest: Optional[_EbayCreateFixedPriceItemAddfixedpriceitemrequest] = None,
    ) -> Dict[str, Any]:
        """Creates a new fixed-price eBay listing via the eBay Trading API. Use this to list an item at a set Buy It Now price without an auction component. Prefer this over ebay_create_item when the listing format is strictly fixed-price and you are using the Trading API. Do not use this to create auction-style listings — use ebay_create_item instead. Do not use this to manage inventory via the Sell Inventory API — use ebay_create_new_inventory_item and ebay_create_offer instead.

        Args:
            AddFixedPriceItemRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_create_inventory_item(
        self,
        availability: Optional[_EbayCreateInventoryItemAvailability] = None,
        condition: Optional[str] = None,
        packageWeightAndSize: Optional[_EbayCreateInventoryItemPackageweightandsize] = None,
        product: Optional[_EbayCreateInventoryItemProduct] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates or replaces an inventory item record in the eBay Sell Inventory API identified by its seller-defined SKU, defining product details such as title, description, condition, and availability. Use this as the first step before creating an offer with ebay_create_offer. If an inventory item with the given SKU already exists, this call will overwrite it. Do not use this to update only partial fields of an existing inventory item — this call replaces the full record. Do not use this to create a listing directly — publish an offer using ebay_publish_offer after creating the inventory item.

        Args:
            availability: 
            condition: 
            packageWeightAndSize: 
            product: 
            sku: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_create_item(
        self,
        AddItemRequest: Optional[_EbayCreateItemAdditemrequest] = None,
    ) -> Dict[str, Any]:
        """Creates a new eBay listing (auction or fixed-price) via the eBay Trading API. Use this to list a new item for sale on eBay, providing details such as title, description, category, price, condition, and shipping options. This action creates an active listing visible to buyers. Do not use this to update an existing listing — use ebay_revise_item instead. Do not use this to create a fixed-price listing using the Sell Inventory API — use ebay_create_new_inventory_item and ebay_create_offer instead.

        Args:
            AddItemRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_create_location(
        self,
        location: Optional[_EbayCreateLocationLocation] = None,
        locationInstructions: Optional[str] = None,
        locationName: Optional[str] = None,
        locationTypes: Optional[List[Any]] = None,
        merchantLocationStatus: Optional[str] = None,
        name: Optional[str] = None,
        operatingHours: Optional[List[Any]] = None,
        phone: Optional[str] = None,
        specialHours: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new inventory location (warehouse, store, or fulfillment center) in the sellers eBay account via the Sell Inventory API, identified by a merchant-defined location name. Use this to register a physical location where inventory is stored or fulfilled from before associating inventory items with it. Do not use this to update an existing location — use ebay_update_destination or the appropriate location update tool instead. Do not use this to enable a disabled location — use ebay_enable_location instead.

        Args:
            location: 
            locationInstructions: 
            locationName: 
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

    def ebay_create_offer(
        self,
        availableQuantity: Optional[int] = None,
        categoryId: Optional[str] = None,
        format: Optional[str] = None,
        listingDescription: Optional[str] = None,
        listingPolicies: Optional[_EbayCreateOfferListingpolicies] = None,
        marketplaceId: Optional[str] = None,
        merchantLocationKey: Optional[str] = None,
        pricingSummary: Optional[_EbayCreateOfferPricingsummary] = None,
        quantityLimitPerBuyer: Optional[int] = None,
        sku: Optional[str] = None,
        tax: Optional[_EbayCreateOfferTax] = None,
    ) -> Dict[str, Any]:
        """Creates a new offer for an inventory item in the eBay Sell Inventory API, defining listing details such as price, marketplace, listing category, and fulfillment policy. An offer must be published using ebay_publish_offer before it becomes a live eBay listing visible to buyers. Use this as the second step after creating an inventory item with ebay_create_new_inventory_item. Do not use this to update an existing offer — use ebay_update_offer instead.

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

    def ebay_create_subscription(
        self,
        destinationId: Optional[str] = None,
        payload: Optional[_EbayCreateSubscriptionPayload] = None,
        status: Optional[str] = None,
        topicId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new eBay notification subscription in the Commerce Notification API, registering interest in a specific event topic and linking it to a notification destination. Use this to start receiving eBay event notifications (e.g., order updates, item sold) at a configured destination endpoint. A destination must exist before creating a subscription — use ebay_create_destination first if needed. Do not use this to update an existing subscription — use ebay_update_subscription instead.

        Args:
            destinationId: 
            payload: 
            status: 
            topicId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_delete_inventory_item(
        self,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an inventory item from the sellers eBay Sell Inventory API identified by its SKU, removing all associated product data. Use this when an item is permanently discontinued and should be removed from inventory management. This action is irreversible — the inventory item record cannot be recovered. Note: deleting an inventory item with active offers may affect live listings. Do not use this to simply end a listing — use ebay_end_item instead.

        Args:
            sku: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_delete_location(
        self,
        locationName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an inventory location from the sellers eBay account identified by its location name. Use this only when a location is no longer needed and has no active inventory items associated with it. This action is irreversible — the location and its configuration cannot be recovered after deletion. Do not use this to temporarily deactivate a location — use ebay_disable_location instead.

        Args:
            locationName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_delete_offer(
        self,
        offerId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an unpublished offer from the eBay Sell Inventory API identified by its offer ID. Use this to remove an offer that was created but never published, or to clean up stale draft offers. This action is irreversible — the offer cannot be recovered after deletion. Note: published offers that have active listings must be withdrawn before deletion. Do not use this to update an offer — use ebay_update_offer instead.

        Args:
            offerId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_delete_subscription(
        self,
        subscriptionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an eBay notification subscription identified by its subscription ID via the Commerce Notification API, stopping all event notifications associated with it. Use this when a subscription is no longer needed. This action is irreversible — the subscription must be recreated with ebay_create_subscription if needed again. Do not use this to temporarily stop notifications — use ebay_disable_subscription instead.

        Args:
            subscriptionId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_disable_location(
        self,
        locationName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Disables an active eBay inventory location, preventing it from being used for new inventory operations while retaining its configuration. Use this to temporarily suspend a location without permanently deleting it. The location can be re-enabled later using ebay_enable_location. Do not use this if you intend to permanently remove the location — use ebay_delete_location instead.

        Args:
            locationName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_disable_subscription(
        self,
        subscriptionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Disables an active eBay notification subscription, pausing the delivery of event notifications without permanently deleting the subscription configuration. Use this to temporarily suspend notifications for a subscription. The subscription can be re-enabled using ebay_enable_subscription. Do not use this to permanently remove a subscription — use ebay_delete_subscription instead.

        Args:
            subscriptionId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_enable_location(
        self,
        locationName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Enables a previously disabled eBay inventory location, making it active and available for inventory operations again. Use this to reactivate a location that was suspended using ebay_disable_location. Do not use this to create a new location — use ebay_create_new_location instead.

        Args:
            locationName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_enable_subscription(
        self,
        subscriptionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Enables a previously disabled eBay notification subscription, resuming delivery of event notifications to the configured destination. Use this to reactivate a subscription that was paused using ebay_disable_subscription. Do not use this to create a new subscription — use ebay_create_subscription instead.

        Args:
            subscriptionId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_end_item(
        self,
        EndItemRequest: Optional[_EbayEndItemEnditemrequest] = None,
    ) -> Dict[str, Any]:
        """Ends the active listing of a single eBay item via the eBay Trading API, immediately removing it from eBay search results and making it unavailable for purchase. Use this when a specific item is sold, out of stock, or needs to be removed from sale. Ending a listing is not easily reversible — the item must be relisted to become active again. Do not use this to end multiple items at once — use ebay_end_items instead.

        Args:
            EndItemRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_end_items(
        self,
        EndItemsRequest: Optional[_EbayEndItemsEnditemsrequest] = None,
    ) -> Dict[str, Any]:
        """Ends the active listings of multiple eBay items in a single batch call via the eBay Trading API. Use this to immediately terminate several listings at once, for example when items sell out or are being discontinued. Ending a listing removes it from eBay search results and makes it unavailable for purchase. This action is not easily reversible — ended listings must be relisted to become active again. Do not use this to end a single item — use ebay_end_item instead.

        Args:
            EndItemsRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_generate_application_auth_token(
        self,
        Authorization: Optional[str] = None,
        grant_type: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates an OAuth application access token (client credentials grant) for the eBay production environment, authorizing server-to-server API calls that do not require user consent. Use this to obtain a bearer token for calling eBay APIs that support application-level authentication. This targets the eBay production environment. Do not use this for user-specific OAuth flows — use ebay_get_refresh_token instead. Do not use this for sandbox testing — use the sandbox-specific token endpoint.

        Args:
            Authorization: 
            grant_type: 
            scope: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_get_inventory_item(
        self,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single inventory item from the eBay Sell Inventory API identified by its SKU, including product title, description, condition, and availability. Use this when you need complete information about one specific inventory item. Do not use this to retrieve all inventory items — use ebay_list_inventory_items instead.

        Args:
            sku: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_get_inventory_location(
        self,
        locationName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single eBay inventory location identified by its location name (merchant location key), including address, operating hours, and status. Use this when you need detailed information about one specific location. Do not use this to retrieve all locations — use ebay_list_inventory_locations instead.

        Args:
            locationName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_get_item(
        self,
        GetItemRequest: Optional[_EbayGetItemGetitemrequest] = None,
    ) -> Dict[str, Any]:
        """Retrieves full details of a specific eBay item from the eBay Trading API, including listing information, price, quantity, seller details, and item condition. Use this when you have a known item ID and need comprehensive listing data from the Trading API. Do not use this to search for items by keyword — use ebay_search_products instead. Do not use this to look up an item using a legacy item ID via the Browse API — use ebay_get_item_by_legacy_item_id instead.

        Args:
            GetItemRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_get_item_by_legacy_item_id(
        self,
        X_EBAY_C_MARKETPLACE_ID: Optional[str] = None,
        legacyItemId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves full details of a single eBay listing using its legacy item ID (the numeric ID visible in classic eBay URLs). Use this when you have a specific legacy item ID and need complete listing details such as price, condition, seller, images, and shipping options. Do not use this to search by keyword or to look up items using the newer RESTful item ID format — use ebay_search_products for keyword searches.

        Args:
            X_EBAY_C_MARKETPLACE_ID: 
            legacyItemId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_get_refresh_token(
        self,
        authToken: Optional[str] = None,
        code: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exchanges an authorization code or existing credentials for a new OAuth refresh token using the eBay sandbox identity service. Use this during the OAuth authorization flow to obtain a refresh token that can later be used to generate new access tokens without user re-authentication. This call targets the eBay sandbox environment and should not be used in production. Do not use this to generate an application-level (client credentials) token — use ebay_generate_application_auth_token instead.

        Args:
            authToken: 
            code: 
            redirect_uri: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_list_inventory_items(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all inventory items in the sellers eBay Sell Inventory account, returning SKUs, product details, conditions, and availability for each item. Use this to get a full overview of all inventory records managed via the Sell Inventory API. Do not use this to retrieve a single inventory item by SKU — use ebay_get_inventory_item instead.

        Args:
            limit: 
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_list_inventory_locations(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all inventory locations configured under the sellers eBay account via the Sell Inventory API. Use this to retrieve a full list of warehouses, stores, or fulfillment centers where inventory is tracked. Returns location keys, addresses, and status for each location. Do not use this to retrieve details of a single specific location — use ebay_get_inventory_location instead.

        Args:
            limit: 
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_list_merchandised_products(
        self,
        X_EBAY_C_MARKETPLACE_ID: Optional[str] = None,
        categoryId: Optional[str] = None,
        metricName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists merchandised products from the eBay Buy Marketing API for a given category and ranking metric. Use this to discover trending or top-selling products within a specific eBay category (e.g., most-watched, most-purchased). Requires a valid category_id and metric_name. Do not use this to search for a specific item by keyword or ID — use ebay_search_products or ebay_get_item_by_legacy_item_id instead.

        Args:
            X_EBAY_C_MARKETPLACE_ID: 
            categoryId: 
            metricName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_list_sellers(
        self,
        GetSellerListRequest: Optional[_EbayListSellersGetsellerlistrequest] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of sellers from the eBay Trading API. Use this to obtain seller account information and listings associated with a seller account. Returns seller identifiers and related metadata. Do not use this to retrieve a single item — use ebay_get_item instead.

        Args:
            GetSellerListRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_publish_offer(
        self,
        offerId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Publishes an existing eBay offer to create or update a live eBay listing, making the item available for purchase by buyers. Use this after creating or updating an offer via ebay_create_offer or ebay_update_offer to activate it on the eBay marketplace. Publishing an offer that is already live will update the existing listing. Do not use this to create the offer itself — use ebay_create_offer first.

        Args:
            offerId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_revise_fixed_price_item(
        self,
        ReviseFixedPriceItemRequest: Optional[_EbayReviseFixedPriceItemRevisefixedpriceitemrequest] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing fixed-price eBay listing via the eBay Trading API, such as price, quantity, title, description, or item specifics. Use this to modify an active fixed-price listing without ending and relisting it. Do not use this to revise auction-style listings — use ebay_revise_item instead. Do not use this to create a new fixed-price listing — use ebay_create_fixed_price_item instead.

        Args:
            ReviseFixedPriceItemRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_revise_item(
        self,
        ReviseItemRequest: Optional[_EbayReviseItemReviseitemrequest] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing eBay listing (including auction-style listings) via the eBay Trading API, such as price, title, description, item specifics, or shipping options. Use this to modify an active listing without ending and relisting it. Do not use this to revise fixed-price listings — use ebay_revise_fixed_price_item instead. Do not use this to create a new listing — use ebay_create_item or ebay_create_fixed_price_item instead.

        Args:
            ReviseItemRequest: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_search_products(
        self,
        X_EBAY_API_CALL_NAME: Optional[str] = None,
        X_EBAY_API_VERSION: Optional[str] = None,
        X_EBAY_C_MARKETPLACE_ID: Optional[str] = None,
        authToken: Optional[str] = None,
        base_url: Optional[str] = None,
        product_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches eBay listings by keyword and returns up to 5 matching product summaries from the Buy Browse API. Use this to find active eBay listings matching a product name or description. Returns summary data including title, price, condition, and item URL. Do not use this to look up a specific item by ID — use ebay_get_item_by_legacy_item_id instead. Do not use this to browse trending products by category — use ebay_list_merchandised_products instead.

        Args:
            X_EBAY_API_CALL_NAME: 
            X_EBAY_API_VERSION: 
            X_EBAY_C_MARKETPLACE_ID: 
            authToken: 
            base_url: 
            product_name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_update_destination(
        self,
        deliveryConfig: Optional[_EbayUpdateDestinationDeliveryconfig] = None,
        destinationId: Optional[str] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing eBay notification destination (e.g., webhook endpoint URL or delivery details) identified by its destination ID. Use this when a notification endpoint URL or its settings have changed and need to be kept in sync. This operation overwrites existing destination details. Do not use this to create a new destination — use ebay_create_destination instead.

        Args:
            deliveryConfig: 
            destinationId: 
            name: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_update_offer(
        self,
        availableQuantity: Optional[int] = None,
        categoryId: Optional[str] = None,
        includeCatalogProductDetails: Optional[bool] = None,
        listingDescription: Optional[str] = None,
        listingPolicies: Optional[_EbayUpdateOfferListingpolicies] = None,
        offerId: Optional[str] = None,
        pricingSummary: Optional[_EbayUpdateOfferPricingsummary] = None,
        quantityLimitPerBuyer: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing eBay offer (such as price, quantity, listing policies, or fulfillment settings) identified by its offer ID via the Sell Inventory API. Use this to modify offer details before or after publishing. Changes to a published offer may require republishing to take effect on the live listing. Do not use this to create a new offer — use ebay_create_offer instead. Do not use this to delete an offer — use ebay_delete_offer instead.

        Args:
            availableQuantity: 
            categoryId: 
            includeCatalogProductDetails: 
            listingDescription: 
            listingPolicies: 
            offerId: 
            pricingSummary: 
            quantityLimitPerBuyer: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ebay_update_subscription(
        self,
        destinationId: Optional[str] = None,
        payload: Optional[_EbayUpdateSubscriptionPayload] = None,
        status: Optional[str] = None,
        subscriptionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing eBay notification subscription identified by its subscription ID via the Commerce Notification API, such as changing the associated destination or topic. Use this when subscription settings need to be modified without deleting and recreating the subscription. Do not use this to create a new subscription — use ebay_create_subscription instead. Do not use this to enable or disable a subscription — use ebay_enable_subscription or ebay_disable_subscription instead.

        Args:
            destinationId: 
            payload: 
            status: 
            subscriptionId: 
        Returns:
            API response as a dictionary.
        """
        ...

