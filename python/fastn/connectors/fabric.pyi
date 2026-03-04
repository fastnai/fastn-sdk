"""Fastn Fabric connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _FabricCreateEventSubscriptionAuthorizationdetails(TypedDict, total=False):
    config: Dict[str, Any]
    type: str

class _FabricCreateInventoryV3Counters(TypedDict, total=False):
    allocated: int
    onHand: int
    shipped: int

class _FabricCreateInventoryV3Customattributes(TypedDict, total=False):
    isBopis: bool

class _FabricCreateInventoryV3Virtualcountersstatus(TypedDict, total=False):
    availableBackorder: str
    availablePreorder: str
    availableToPurchase: str

class _FabricCreateLocationV2Address(TypedDict, total=False):
    addressLine1: str
    addressLine2: str
    addressLine3: str
    addressLine4: str
    city: str
    contact: List[Any]
    country: str
    postalCode: int
    state: str
    type: str

class _FabricCreateLocationV2Attributes(TypedDict, total=False):
    isReturns: bool

class _FabricCreateLocationV2Coordinates(TypedDict, total=False):
    coordinates: List[Any]
    type: str

class _FabricCreateLocationV2Services(TypedDict, total=False):
    isCurbsidePickUp: bool

class _FabricCreateShipmentV2Shiptoaddress(TypedDict, total=False):
    addressLine1: str
    addressLine2: str
    addressLine3: str
    addressLine4: str
    city: str
    country: str
    latitude: str
    longitude: str
    postalCode: str
    state: str
    type: str

class _FabricPatchLocationV2Address(TypedDict, total=False):
    addressLine1: str
    addressLine2: str
    addressLine3: str
    addressLine4: str
    city: str
    contact: List[Any]
    country: str
    postalCode: int
    state: str
    type: str

class _FabricPatchLocationV2Attributes(TypedDict, total=False):
    isReturns: bool

class _FabricPatchLocationV2Coordinates(TypedDict, total=False):
    coordinates: List[Any]
    type: str

class _FabricPatchLocationV2Services(TypedDict, total=False):
    isCurbsidePickUp: bool

class _FabricPutLocationV2Address(TypedDict, total=False):
    addressLine1: str
    addressLine2: str
    addressLine3: str
    addressLine4: str
    city: str
    contact: List[Any]
    country: str
    postalCode: int
    state: str
    type: str

class _FabricPutLocationV2Attributes(TypedDict, total=False):
    isReturns: bool

class _FabricPutLocationV2Coordinates(TypedDict, total=False):
    coordinates: List[Any]
    type: str

class _FabricPutLocationV2Services(TypedDict, total=False):
    isCurbsidePickUp: bool

class _FabricSearchCatalogConnectorsV3Search(TypedDict, total=False):
    attributeIds: Dict[str, Any]
    attributeTypes: Dict[str, Any]
    attributes: List[Any]
    bundleProductCount: Dict[str, Any]
    bundleProductId: Dict[str, Any]
    bundleProductName: Dict[str, Any]
    bundleProductSku: Dict[str, Any]
    categoryId: Dict[str, Any]
    categoryName: Dict[str, Any]
    collectionName: Dict[str, Any]
    createdAt: Dict[str, Any]
    id: Dict[str, Any]
    image: Dict[str, Any]
    itemId: Dict[str, Any]
    keyword: Dict[str, Any]
    parentId: Dict[str, Any]
    parentSku: Dict[str, Any]
    productName: Dict[str, Any]
    sku: Dict[str, Any]
    type: Dict[str, Any]
    updatedAt: Dict[str, Any]

class FabricConnector:
    """Fabric connector ().

    Provides 35 tools.
    """

    def fabric_create_event_subscription(
        self,
        authorizationDetails: Optional[_FabricCreateEventSubscriptionAuthorizationdetails] = None,
        deliveryType: Optional[str] = None,
        events: Optional[List[Any]] = None,
        name: Optional[str] = None,
        targetUrl: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new event subscription in Fabrics self-service events system. Use this tool to register a new endpoint to receive notifications for specific Fabric platform events. Do not use this tool to list or retrieve existing subscriptions — use fabric_list_event_subscriptions instead. Submits a POST request to the event-subscriptions endpoint. This operation creates a persistent subscription that will begin delivering events immediately upon creation.

        Args:
            authorizationDetails: 
            deliveryType: 
            events: 
            name: 
            targetUrl: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_create_inventory_v3(
        self,
        backorderLimit: Optional[int] = None,
        backorderShipmentAt: Optional[str] = None,
        counters: Optional[_FabricCreateInventoryV3Counters] = None,
        customAttributes: Optional[_FabricCreateInventoryV3Customattributes] = None,
        hasInfiniteInventory: Optional[bool] = None,
        itemId: Optional[int] = None,
        leadTime: Optional[str] = None,
        locationNumber: Optional[int] = None,
        lowStock: Optional[int] = None,
        networkCode: Optional[str] = None,
        preorderLimit: Optional[int] = None,
        preorderShipmentAt: Optional[str] = None,
        region: Optional[str] = None,
        safetyStock: Optional[int] = None,
        sku: Optional[str] = None,
        status: Optional[str] = None,
        type: Optional[str] = None,
        vendorId: Optional[str] = None,
        virtualCountersStatus: Optional[_FabricCreateInventoryV3Virtualcountersstatus] = None,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new inventory entry in Fabric using the Inventory Connector. Use this tool to register inventory quantities for a product or location for the first time. Do not use this tool to update existing inventory records. Submits a POST request to the inventories endpoint. This operation creates a persistent inventory record; removal requires a separate delete operation.

        Args:
            backorderLimit: 
            backorderShipmentAt: 
            counters: 
            customAttributes: 
            hasInfiniteInventory: 
            itemId: 
            leadTime: 
            locationNumber: 
            lowStock: 
            networkCode: 
            preorderLimit: 
            preorderShipmentAt: 
            region: 
            safetyStock: 
            sku: 
            status: 
            type: 
            vendorId: 
            virtualCountersStatus: 
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_create_location_v2(
        self,
        address: Optional[_FabricCreateLocationV2Address] = None,
        attributes: Optional[_FabricCreateLocationV2Attributes] = None,
        authToken: Optional[str] = None,
        coordinates: Optional[_FabricCreateLocationV2Coordinates] = None,
        env: Optional[str] = None,
        isActive: Optional[bool] = None,
        locationNum: Optional[int] = None,
        name: Optional[str] = None,
        operatingHours: Optional[List[Any]] = None,
        services: Optional[_FabricCreateLocationV2Services] = None,
        type: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new location record in Fabrics OMS Location Connector (v2). Use this tool to add a new physical or logical location such as a warehouse, store, or distribution center. Do not use this tool to update an existing location — use fabric_put_location_v2 or fabric_patch_location_v2 instead. Submits a POST request to the OMS location endpoint. This operation creates a persistent location record; removal requires fabric_delete_location_v2.

        Args:
            address: 
            attributes: 
            authToken: 
            coordinates: 
            env: 
            isActive: 
            locationNum: 
            name: 
            operatingHours: 
            services: 
            type: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_create_product_in_catalog_v3(
        self,
        attributes: Optional[List[Any]] = None,
        categories: Optional[List[Any]] = None,
        categoryId: Optional[str] = None,
        categoryName: Optional[str] = None,
        collections: Optional[List[Any]] = None,
        images: Optional[List[Any]] = None,
        locale: Optional[str] = None,
        productName: Optional[str] = None,
        sku: Optional[str] = None,
        type: Optional[str] = None,
        variants: Optional[List[Any]] = None,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new product entry in the Fabric product catalog using the Catalog Connector (v3). Use this tool to add a product directly to the catalog connector, separate from the core product batch creation flow. Do not use this tool to create products via the core product API — use fabric_create_product_v3 instead. Submits a POST request to the catalog-connector products endpoint. This operation is irreversible without a subsequent delete.

        Args:
            attributes: 
            categories: 
            categoryId: 
            categoryName: 
            collections: 
            images: 
            locale: 
            productName: 
            sku: 
            type: 
            variants: 
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_create_product_v3(
        self,
        products: Optional[List[Any]] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates one or more new products in Fabric using the Product Connector (v3) batch endpoint. Use this tool to add new products to the Fabric catalog in bulk. Do not use this tool to update existing products — use fabric_update_product_attributes_by_id_v3 instead. Submits a POST request to the /v3/products/batch endpoint. This operation is irreversible; created products must be individually deleted or updated if changes are needed.

        Args:
            products: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_create_shipment_v2(
        self,
        allocationId: Optional[str] = None,
        attributes: Optional[Dict[str, Any]] = None,
        auditLogs: Optional[List[Any]] = None,
        authToken: Optional[str] = None,
        cartons: Optional[List[Any]] = None,
        env: Optional[str] = None,
        invoiceId: Optional[str] = None,
        locationNum: Optional[str] = None,
        locationType: Optional[str] = None,
        masterTrackingNumber: Optional[str] = None,
        poNumber: Optional[str] = None,
        recipient: Optional[List[Any]] = None,
        reshipmentReasonCode: Optional[str] = None,
        scratchedItems: Optional[List[Any]] = None,
        shipDate: Optional[str] = None,
        shipToAddress: Optional[_FabricCreateShipmentV2Shiptoaddress] = None,
        shipToId: Optional[str] = None,
        shipmentNum: Optional[str] = None,
        statusCode: Optional[str] = None,
        totalCartons: Optional[str] = None,
        type: Optional[str] = None,
        vendorId: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new shipment record in Fabrics OMS Shipment Connector (v2). Use this tool to initiate a shipment for an order or allocation. Do not use this tool to update or cancel an existing shipment. Submits a POST request to the OMS shipment endpoint. This operation creates a persistent shipment record and may trigger downstream fulfillment processes; it cannot be undone without a separate cancellation or update.

        Args:
            allocationId: 
            attributes: 
            auditLogs: 
            authToken: 
            cartons: 
            env: 
            invoiceId: 
            locationNum: 
            locationType: 
            masterTrackingNumber: 
            poNumber: 
            recipient: 
            reshipmentReasonCode: 
            scratchedItems: 
            shipDate: 
            shipToAddress: 
            shipToId: 
            shipmentNum: 
            statusCode: 
            totalCartons: 
            type: 
            vendorId: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_delete_app(
        self,
        appId: Optional[str] = None,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific application by its ID from Fabrics identity management system (UMS v2). Use this tool to remove an app registration that is no longer needed. Do not use this tool to delete other resource types such as webhooks or locations. Requires an appId URL parameter. This operation is irreversible; the deleted app and its credentials cannot be recovered.

        Args:
            appId: 
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_delete_location_v2(
        self,
        authToken: str,
        env: str,
        locationNum: str,
        x_fabric_tenant_id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific location by its location number from Fabrics OMS Location Connector (v2). Use this tool to remove a location record that is no longer needed. Do not use this tool to update a location — use fabric_patch_location_v2 or fabric_put_location_v2 instead. Requires a locationNum URL parameter. This operation is irreversible; the deleted location cannot be recovered.

        Args:
            authToken:  (required)
            env:  (required)
            locationNum:  (required)
            x_fabric_tenant_id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_delete_self_service_webhook(
        self,
        webhookId: Optional[str] = None,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific self-service event subscription webhook by its ID from Fabrics self-service events system. Use this tool to permanently remove a webhook subscription that is no longer needed. Do not use this tool to delete OMS webhooks — use fabric_delete_webhook_v3 instead. Requires a webhookId URL parameter. This operation is irreversible; the deleted webhook cannot be recovered.

        Args:
            webhookId: 
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_delete_webhook_v3(
        self,
        webhookId: Optional[str] = None,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific OMS webhook by its ID from the Fabric Webhook Connector (v3). Use this tool to remove an OMS webhook registration that is no longer needed. Do not use this tool to delete self-service event webhooks — use fabric_delete_self_service_webhook instead. Requires a webhookId URL parameter. This operation is irreversible; the deleted webhook cannot be recovered.

        Args:
            webhookId: 
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_generate_auth_token(
        self,
        base_url: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates an authentication token using Fabrics Authentication Connector by submitting client credentials and grant type. Use this tool to obtain a new token for authorizing subsequent API requests. Do not use this tool to retrieve an existing access token — use fabric_get_access_token instead. Requires client_id, client_secret, and grant_type parameters. This operation creates a new token and may invalidate or supersede previous tokens.

        Args:
            base_url: 
            client_id: 
            client_secret: 
            grant_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_get_access_token(
        self,
        baseUrl: Optional[str] = None,
        grant_type: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves an access token from Fabrics authentication service to authorize API requests. Use this tool to obtain a bearer token before making authenticated calls to Fabric APIs. Do not use this tool to generate a new token from scratch using client credentials — use fabric_generate_auth_token instead. Submits a POST request to the token endpoint. This operation may create or refresh a session token.

        Args:
            baseUrl: 
            grant_type: 
            scope: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_get_allocation_v2(
        self,
        authToken: str,
        env: str,
        x_fabric_tenant_id: str,
        allocationId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details for a specific inventory allocation by its ID from Fabrics OMS Allocation Connector (v2). Use this tool to look up allocation status and resource details for a known allocation ID. Do not use this tool to update an allocation — use fabric_update_allocation_v2 instead. Requires an allocationId URL parameter. This is a read-only operation with no side effects.

        Args:
            authToken:  (required)
            env:  (required)
            x_fabric_tenant_id:  (required)
            allocationId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_get_catalog_product_by_sku_v3(
        self,
        locale: Optional[str] = None,
        skuId: Optional[str] = None,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product details by SKU ID from the Fabric Catalog Connector (v3). Use this tool when you need catalog-specific product data for a known SKU, as opposed to core product data. Do not use this tool to search or list catalog products — use fabric_search_catalog_connectors_v3 instead. Requires a skuId URL parameter. This is a read-only operation with no side effects.

        Args:
            locale: 
            skuId: 
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_get_location_v2(
        self,
        authToken: str,
        env: str,
        locationNum: str,
        x_fabric_tenant_id: str,
    ) -> Dict[str, Any]:
        """Retrieves details for a specific location by its location number from Fabrics OMS Location Connector (v2). Use this tool when you have a known location number and need its full record. Do not use this tool to list all locations — use fabric_list_locations_v2 instead. Requires a locationNum URL parameter. This is a read-only operation with no side effects.

        Args:
            authToken:  (required)
            env:  (required)
            locationNum:  (required)
            x_fabric_tenant_id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_get_order_v2(
        self,
        authToken: Optional[str] = None,
        env: Optional[str] = None,
        orderId: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details for a specific order by its order ID from Fabrics OMS (v2). Use this tool to look up order status, line items, and fulfillment information for a known order ID using the v2 API. Do not use this tool to retrieve orders via the v3 API — use fabric_get_order_v3 instead. Requires an orderId query parameter. This is a read-only operation with no side effects.

        Args:
            authToken: 
            env: 
            orderId: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_get_order_v3(
        self,
        orderId: Optional[str] = None,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details for a specific order by its ID from the Fabric Order Connector (v3). Use this tool to look up order status, line items, and fulfillment details for a known order ID. Do not use this tool to retrieve orders using the v2 API — use fabric_get_order_v2 instead. Requires an orderId URL parameter. This is a read-only operation with no side effects.

        Args:
            orderId: 
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_get_product_by_id_v3(
        self,
        product_id: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves full details for a single product by its ID from the Fabric Product Connector (v3). Use this tool when you have a specific product ID and need its complete record. Do not use this tool to look up a product by SKU — use fabric_get_product_by_sku_v3 instead. Requires a product_id URL parameter. This is a read-only operation with no side effects.

        Args:
            product_id: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_get_product_by_sku_v3(
        self,
        sku: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves full details for a single product by its SKU from the Fabric Product Connector (v3). Use this tool when you have a SKU identifier and need the associated product record. Do not use this tool to look up a product by internal ID — use fabric_get_product_by_id_v3 instead. Requires a sku URL parameter. This is a read-only operation with no side effects.

        Args:
            sku: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_get_user(
        self,
        baseUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves profile and identity details for the currently authenticated user from the configured Fabric base URL. Use this tool to fetch user information after authentication has been established. Do not use this tool to manage tokens or perform authentication flows — use fabric_get_access_token or fabric_generate_auth_token instead. This is a read-only operation with no side effects.

        Args:
            baseUrl: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_get_variant_by_id_v3(
        self,
        variant_id: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details for a single product variant by its ID from the Fabric Product Variant Connector (v3). Use this tool when you have a specific variant ID and need its full details. Do not use this tool to list all variants for a product — use fabric_list_variants_v3 instead. Requires a variant_id URL parameter. This is a read-only operation with no side effects.

        Args:
            variant_id: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_list_apps(
        self,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all registered applications from Fabrics identity management system (UMS v2). Use this tool to retrieve all app registrations and their configurations. Do not use this tool to retrieve a single app or to manage tokens — use fabric_get_access_token for authentication. This is a read-only operation with no side effects.

        Args:
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_list_event_subscriptions(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all event subscriptions from Fabrics self-service events system. Use this tool to retrieve all registered webhook subscriptions and their configuration details. Do not use this tool to list raw events — use fabric_list_events instead. This is a read-only operation with no side effects.

        Args:
            limit: 
            offset: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_list_events(
        self,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all available events from Fabrics self-service events system. Use this tool to discover what event types are available for subscription in the Fabric platform. Do not use this tool to retrieve event subscriptions — use fabric_list_event_subscriptions instead. This is a read-only operation with no side effects.

        Args:
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_list_locations_v2(
        self,
        authToken: str,
        env: str,
        limit: str,
        offset: str,
        x_fabric_tenant_id: str,
    ) -> Dict[str, Any]:
        """Lists all locations from Fabrics OMS Location Connector (v2) with support for pagination via offset and limit parameters. Use this tool to retrieve a full or paginated list of location records. Do not use this tool to retrieve a single specific location — use fabric_get_specific_location_v2 instead. This is a read-only operation with no side effects.

        Args:
            authToken:  (required)
            env:  (required)
            limit:  (required)
            offset:  (required)
            x_fabric_tenant_id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_list_products_v3(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all products from the Fabric Product Connector (v3). Use this tool to retrieve a full collection of products from the Fabric catalog. Do not use this tool to retrieve a single product by ID or SKU — use fabric_get_product_by_id_v3 or fabric_get_product_by_sku_v3 instead. Returns a paginated list of product records. This is a read-only operation with no side effects.

        Args:
            limit: 
            offset: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_list_variants_v3(
        self,
        product_id: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all variants for a specific product from the Fabric Product Variant Connector (v3). Use this tool when you need all variants associated with a given product ID. Do not use this tool to retrieve a single variant by ID — use fabric_get_variant_by_id_v3 instead. Requires a product_id URL parameter. This is a read-only operation with no side effects.

        Args:
            product_id: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_patch_location_v2(
        self,
        authToken: str,
        env: str,
        x_fabric_tenant_id: str,
        address: Optional[_FabricPatchLocationV2Address] = None,
        attributes: Optional[_FabricPatchLocationV2Attributes] = None,
        coordinates: Optional[_FabricPatchLocationV2Coordinates] = None,
        isActive: Optional[bool] = None,
        locationNum: Optional[int] = None,
        name: Optional[str] = None,
        operatingHours: Optional[List[Any]] = None,
        services: Optional[_FabricPatchLocationV2Services] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Partially updates a specific location by its location number in Fabrics OMS (v2) using a PATCH request. Use this tool to modify only specific fields of an existing location without overwriting all fields. Do not use this tool for full location replacement — use fabric_put_location_v2 instead. Requires a locationNum URL parameter and a partial location payload. This operation modifies existing location data and cannot be undone without a subsequent update.

        Args:
            authToken:  (required)
            env:  (required)
            x_fabric_tenant_id:  (required)
            address: 
            attributes: 
            coordinates: 
            isActive: 
            locationNum: 
            name: 
            operatingHours: 
            services: 
            type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_put_location_v2(
        self,
        address: Optional[_FabricPutLocationV2Address] = None,
        attributes: Optional[_FabricPutLocationV2Attributes] = None,
        authToken: Optional[str] = None,
        coordinates: Optional[_FabricPutLocationV2Coordinates] = None,
        env: Optional[str] = None,
        isActive: Optional[bool] = None,
        locationNum: Optional[int] = None,
        name: Optional[str] = None,
        operatingHours: Optional[List[Any]] = None,
        services: Optional[_FabricPutLocationV2Services] = None,
        type: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fully replaces an existing location by its location number in Fabrics OMS Location Connector (v2) using a PUT request. Use this tool to overwrite all fields of a location record with new values. Do not use this tool for partial updates — use fabric_patch_location_v2 instead. Requires a locationNum URL parameter and a complete location payload. This operation overwrites all existing location data and cannot be undone without a subsequent update.

        Args:
            address: 
            attributes: 
            authToken: 
            coordinates: 
            env: 
            isActive: 
            locationNum: 
            name: 
            operatingHours: 
            services: 
            type: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_search_catalog_connectors_v3(
        self,
        limit: Optional[int] = None,
        locale: Optional[str] = None,
        offset: Optional[int] = None,
        search: Optional[_FabricSearchCatalogConnectorsV3Search] = None,
        sort: Optional[str] = None,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for products within the Fabric Catalog Connector (v3) using a POST-based search query. Use this tool to find catalog products matching specific criteria such as filters, attributes, or keywords. Do not use this tool to retrieve a single product by SKU — use fabric_get_catalog_product_by_sku_v3 instead. Accepts a search payload in the request body. This is a read-only operation with no side effects.

        Args:
            limit: 
            locale: 
            offset: 
            search: 
            sort: 
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_search_locations_v3(
        self,
        filters: Optional[List[Any]] = None,
        sort: Optional[str] = None,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for locations in Fabric using the Location Connector (v3) via a POST-based search request. Use this tool to find locations matching specific criteria. Note: despite being a search/list operation, this tool uses a POST request body to specify search parameters. Do not use this tool to retrieve a single specific location — use fabric_get_specific_location_v2 instead. This is a read-only operation with no side effects.

        Args:
            filters: 
            sort: 
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_search_webhooks_v3(
        self,
        filters: Optional[List[Any]] = None,
        sort: Optional[str] = None,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for and retrieves OMS webhook configurations from the Fabric Webhook Connector (v3) using a POST-based search request. Use this tool to find and review existing OMS webhook registrations. Note: despite being a retrieval operation, this tool uses a POST request body to specify search parameters. Do not use this tool to manage self-service event subscriptions — use fabric_list_event_subscriptions instead. This is a read-only operation with no side effects.

        Args:
            filters: 
            sort: 
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_update_allocation_v2(
        self,
        authToken: str,
        env: str,
        x_fabric_tenant_id: str,
        allocationDate: Optional[str] = None,
        allocationId: Optional[str] = None,
        allocationNum: Optional[str] = None,
        allocationRequestId: Optional[str] = None,
        auditLogs: Optional[List[Any]] = None,
        items: Optional[List[Any]] = None,
        itemsType: Optional[str] = None,
        locationNum: Optional[str] = None,
        locationType: Optional[str] = None,
        orderSubType: Optional[str] = None,
        parentAllocationId: Optional[str] = None,
        poNumber: Optional[str] = None,
        previousAllocationLocationNum: Optional[str] = None,
        recipient: Optional[List[Any]] = None,
        sentToPPSDate: Optional[str] = None,
        shipDate: Optional[str] = None,
        shipMethod: Optional[str] = None,
        shipToAddress: Optional[Dict[str, Any]] = None,
        shipToId: Optional[str] = None,
        shipType: Optional[str] = None,
        statusCode: Optional[str] = None,
        type: Optional[str] = None,
        updatedAt: Optional[str] = None,
        vendorId: Optional[str] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fully updates an existing inventory allocation by its ID in Fabrics OMS Allocation Connector (v2) using a PUT request. Use this tool to replace all fields of an allocation record with new values. Do not use this tool to retrieve allocation details — use fabric_get_allocation_v2 instead. Requires an allocationId URL parameter and a complete allocation payload. This operation overwrites all existing allocation data and cannot be undone without a subsequent update.

        Args:
            authToken:  (required)
            env:  (required)
            x_fabric_tenant_id:  (required)
            allocationDate: 
            allocationId: 
            allocationNum: 
            allocationRequestId: 
            auditLogs: 
            items: 
            itemsType: 
            locationNum: 
            locationType: 
            orderSubType: 
            parentAllocationId: 
            poNumber: 
            previousAllocationLocationNum: 
            recipient: 
            sentToPPSDate: 
            shipDate: 
            shipMethod: 
            shipToAddress: 
            shipToId: 
            shipType: 
            statusCode: 
            type: 
            updatedAt: 
            vendorId: 
            version: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fabric_update_product_attributes_by_id_v3(
        self,
        attributes: Optional[List[Any]] = None,
        productId: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the attributes of a specific product by its ID using the Fabric Product Connector (v3). Use this tool to modify product attribute values such as name, description, or custom fields for a known product. Do not use this tool to update other product fields outside of attributes, or to create a new product — use fabric_create_product_v3 instead. Requires a productId URL parameter and an attributes payload. This operation overwrites existing attribute values and cannot be undone without a subsequent update.

        Args:
            attributes: 
            productId: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_create_app_v3(
        self,
        description: Optional[str] = None,
        name: Optional[str] = None,
        roles: Optional[List[Any]] = None,
        type: Optional[str] = None,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new application in the Fastn platform using the V3 App Connector via the Identity Management API. Use this tool when you need to register a new app with V3-level capabilities. This is a write operation that persists a new app entry. Do not use this tool to create V1 or V2 widgets — use fastn_create_widget or fastn_create_widget_v2 instead.

        Args:
            description: 
            name: 
            roles: 
            type: 
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

