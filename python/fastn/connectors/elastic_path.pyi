"""Fastn Elastic Path connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _ElasticPathCreateCatalogData(TypedDict, total=False):
    attributes: Dict[str, Any]
    type: str

class _ElasticPathCreateCustomerData(TypedDict, total=False):
    email: str
    external_ref: str
    name: str
    password: str
    type: str

class _ElasticPathCreateInventoryData(TypedDict, total=False):
    quantity: int

class _ElasticPathUpdateCatalogData(TypedDict, total=False):
    attributes: Dict[str, Any]
    id: str
    type: str

class _ElasticPathUpdateInventoryData(TypedDict, total=False):
    action: str
    quantity: int
    type: str

class ElasticPathConnector:
    """Elastic Path connector ().

    Provides 18 tools.
    """

    def elastic_path_create_catalog(
        self,
        data: _ElasticPathCreateCatalogData,
    ) -> Dict[str, Any]:
        """Creates a new catalog in Elastic Path. Use this tool to define a new catalog with its associated hierarchies, price books, and other configuration. Do not use this tool to update an existing catalog — use elastic_path_update_catalog instead.

        Args:
            data: Main data object for the Elastic Path request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_create_customer(
        self,
        data: _ElasticPathCreateCustomerData,
    ) -> Dict[str, Any]:
        """Creates a new customer record in Elastic Path. Use this tool to register a new customer with their name, email, and other profile details. Do not use this tool to update an existing customers information — use elastic_path_update_customer instead.

        Args:
            data: Data payload for Elastic Path. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_create_inventory(
        self,
        data: _ElasticPathCreateInventoryData,
        productId: str,
    ) -> Dict[str, Any]:
        """Creates a new inventory record for a specific product in Elastic Path by its product ID. Use this tool to initialize inventory tracking for a product that does not yet have an inventory record. Do not use this tool to adjust existing stock levels — use elastic_path_update_inventory instead.

        Args:
            data: Details about the product. (required)
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_create_product(
        self,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the Elastic Path product catalog (PCM). Use this tool when you need to add a brand-new product with its attributes, pricing, and metadata. Do not use this tool to modify an existing product — use elastic_path_update_product instead.

        Args:
            body: Request body for the Elastic Path endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_delete_catalog(
        self,
        catalogId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific catalog from Elastic Path by its catalog ID. Use this tool only when a catalog must be fully removed from the system. This action is irreversible — the catalog and its configuration cannot be recovered after deletion. Do not use this tool to modify a catalog — use elastic_path_update_catalog instead.

        Args:
            catalogId: ID of the catalog. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_delete_customer(
        self,
        customerId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific customer record from Elastic Path by their customer ID. Use this tool only when a customer account must be fully removed from the system. This action is irreversible — all customer data associated with this record will be deleted and cannot be recovered. Do not use this tool to update customer details — use elastic_path_update_customer instead.

        Args:
            customerId: ID of the customer. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific product from the Elastic Path product catalog (PCM) by its product ID. Use this tool only when a product must be fully removed from the catalog. This action is irreversible — the product cannot be recovered after deletion. Do not use this tool if you only want to update or deactivate a product — use elastic_path_update_product instead.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_generate_access_token(
        self,
        clientId: str,
        clientSecret: str,
        region: str,
    ) -> Dict[str, Any]:
        """Generates a new OAuth access token for authenticating subsequent requests to the Elastic Path API. Use this tool to obtain a token before making API calls that require authorization. The region parameter determines which Elastic Path API endpoint is used. Do not use this tool for operations unrelated to authentication setup.

        Args:
            clientId: Client ID for authentication with Elastic Path. (required)
            clientSecret: Client secret for authentication with Elastic Path. (required)
            region: Region specification for the Elastic Path API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_get_catalog(
        self,
        catalogId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single catalog in Elastic Path by its catalog ID. Use this tool when you need full details — such as hierarchies, price books, and metadata — for one specific catalog. Do not use this tool to retrieve multiple catalogs — use elastic_path_list_catalogs instead.

        Args:
            catalogId: ID of the catalog. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single product in the Elastic Path product catalog (PCM) by its product ID. Use this tool when you need full details — such as attributes, pricing, or metadata — for one specific product. Do not use this tool to retrieve multiple products at once — use elastic_path_list_products instead.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_list_carts(
        self,
    ) -> Dict[str, Any]:
        """Lists all shopping carts in Elastic Path. Use this tool when you need an overview of active or existing carts across the system, such as for auditing or cart management workflows. Do not use this tool when you need details about a single specific cart.
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_list_catalogs(
        self,
    ) -> Dict[str, Any]:
        """Lists all catalogs in Elastic Path. Use this tool when you need to retrieve a collection of catalogs, such as for browsing or selecting a catalog for further operations. Do not use this tool when you need detailed information about a single specific catalog — use elastic_path_get_catalog instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_list_customers(
        self,
    ) -> Dict[str, Any]:
        """Lists all customers registered in Elastic Path. Use this tool when you need to retrieve a collection of customer records, such as for browsing, filtering, or reporting. Do not use this tool when you need detailed information about a single specific customer — retrieve by customer ID using the appropriate get tool.
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_list_inventories(
        self,
    ) -> Dict[str, Any]:
        """Lists all inventory records in Elastic Path. Use this tool when you need an overview of stock levels across all products. Do not use this tool when you need inventory details for a single specific product — filter results by product ID after retrieval or use the appropriate product-scoped endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_list_products(
        self,
    ) -> Dict[str, Any]:
        """Lists all products in the Elastic Path product catalog (PCM). Use this tool when you need to retrieve a collection of products, such as for browsing, filtering, or displaying a product index. Do not use this tool when you need detailed information about a single specific product — use elastic_path_get_product instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_update_catalog(
        self,
        catalogId: str,
        data: _ElasticPathUpdateCatalogData,
    ) -> Dict[str, Any]:
        """Updates the details of an existing catalog in Elastic Path by its catalog ID. Use this tool to modify catalog properties such as name, description, or associated price books and hierarchies. Do not use this tool to create a new catalog — use elastic_path_create_catalog instead.

        Args:
            catalogId: ID of the catalog. (required)
            data: Data object for the Elastic Path API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_update_inventory(
        self,
        data: _ElasticPathUpdateInventoryData,
        productId: str,
    ) -> Dict[str, Any]:
        """Records an inventory transaction (such as an increment, decrement, or allocation) for a specific product in Elastic Path by its product ID. Use this tool to adjust stock levels or record inventory movements. Note: this creates a transaction against the inventory record and will permanently affect stock counts. Do not use this tool to create a new inventory record — use elastic_path_create_inventory instead.

        Args:
            data: Details about the product. (required)
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elastic_path_update_product(
        self,
        productId: str,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing product in the Elastic Path product catalog (PCM) by its product ID. Use this tool to modify product attributes such as name, description, pricing, or status. Do not use this tool to create a new product — use elastic_path_create_product instead.

        Args:
            productId: ID of the product. (required)
            body: Request body for the Elastic Path API.
        Returns:
            API response as a dictionary.
        """
        ...

