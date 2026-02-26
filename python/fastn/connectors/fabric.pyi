"""Fastn Fabric connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FabricConnector:
    """Fabric connector ().

    Provides 35 tools.
    """

    def create_app_v3(
        self,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new app in the system using the App Connector.

        Args:
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_event_subscription(
        self,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new event subscription in the system via the Event Subscription Connector.

        Args:
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_inventory_v3(
        self,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new inventory entry in the system using the Inventory Connector.

        Args:
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_location_v2(
        self,
        authToken: Optional[str] = None,
        env: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new location in the system using the Location Connector.

        Args:
            authToken: 
            env: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product_in_product_catalog_v3(
        self,
        locale: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new product entry in the product catalog using the Product Catalog Connector (v3).

        Args:
            locale: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product_v3(
        self,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the system using the Product Connector (v3).

        Args:
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_shipment_v2(
        self,
        authToken: Optional[str] = None,
        env: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new shipment in the system via the Shipment Connector.

        Args:
            authToken: 
            env: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_app(
        self,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific app in the system via the App Connector.

        Args:
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_location_v2(
        self,
        authToken: str,
        env: str,
        x_fabric_tenant_id: str,
    ) -> Dict[str, Any]:
        """Deletes a specific location from the system using the Location Connector.

        Args:
            authToken:  (required)
            env:  (required)
            x_fabric_tenant_id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_self_service_webhooks(
        self,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes self-service webhooks from the Webhook Connector.

        Args:
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook_v3(
        self,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific webhook from the Webhook Connector.

        Args:
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_auth_token(
        self,
    ) -> Dict[str, Any]:
        """Generates an authentication token using the Authentication Connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_access_token(
        self,
        grant_type: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains an access token using the Authentication Connector.

        Args:
            grant_type: 
            scope: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_locations_v2(
        self,
    ) -> Dict[str, Any]:
        """Fetches all locations from the Location Connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_allocation_v2(
        self,
        authToken: str,
        env: str,
        x_fabric_tenant_id: str,
    ) -> Dict[str, Any]:
        """Retrieves allocation details from the Allocation Connector.

        Args:
            authToken:  (required)
            env:  (required)
            x_fabric_tenant_id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_apps(
        self,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all applications in the system using the App Connector.

        Args:
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_catalog_connector_product_by_sku_v3(
        self,
        locale: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product details by SKU from the Catalog Connector (v3).

        Args:
            locale: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_event_subscriptions(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves event subscription details from the Event Subscription Connector.

        Args:
            limit: 
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_events(
        self,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches events using the Events Connector.

        Args:
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_locations_v3(
        self,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all locations using the Location Connector (v3).

        Args:
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order_v2(
        self,
    ) -> Dict[str, Any]:
        """Retrieves order details from the Order Connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order_v3(
        self,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves order details from the Order Connector (v3).

        Args:
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_by_id_v3(
        self,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product details by ID from the Product Connector (v3).

        Args:
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_by_sku_v3(
        self,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves product details by SKU from the Product Connector (v3).

        Args:
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products_v3(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all products from the Product Connector (v3).

        Args:
            limit: 
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_specific_location_v2(
        self,
        authToken: str,
        env: str,
        x_fabric_tenant_id: str,
    ) -> Dict[str, Any]:
        """Retrieves details for a specific location from the Location Connector.

        Args:
            authToken:  (required)
            env:  (required)
            x_fabric_tenant_id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user(
        self,
        baseUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches user details from the User Connector.

        Args:
            baseUrl: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_variant_by_id_v3(
        self,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves variant details by ID from the Product Variant Connector (v3).

        Args:
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_variants_v3(
        self,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all variants from the Product Variant Connector (v3).

        Args:
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhooks_v3(
        self,
        xfabricchannelid: Optional[str] = None,
        xfabrictenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves webhook configurations from the Webhook Connector.

        Args:
            xfabricchannelid: 
            xfabrictenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def patch_update_location_v2(
        self,
        authToken: str,
        env: str,
        x_fabric_tenant_id: str,
    ) -> Dict[str, Any]:
        """Partially updates a location in the system via the Location Connector.

        Args:
            authToken:  (required)
            env:  (required)
            x_fabric_tenant_id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def put_update_location_v2(
        self,
        authToken: Optional[str] = None,
        env: Optional[str] = None,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing location in the system via the Location Connector.

        Args:
            authToken: 
            env: 
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def search_catalog_connectors_v3(
        self,
        locale: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for catalog connectors using the Catalog Connector.

        Args:
            locale: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_allocation_v2(
        self,
        authToken: str,
        env: str,
        x_fabric_tenant_id: str,
    ) -> Dict[str, Any]:
        """Updates the allocation of resources within the system using the Allocation Connector.

        Args:
            authToken:  (required)
            env:  (required)
            x_fabric_tenant_id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product_attributes_by_id_v3(
        self,
        x_fabric_tenant_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates product attributes by ID using the Product Connector (v3).

        Args:
            x_fabric_tenant_id: 
        Returns:
            API response as a dictionary.
        """
        ...

