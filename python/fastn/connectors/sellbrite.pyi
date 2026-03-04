"""Fastn Sellbrite connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _SellbriteUpsertProductCustomAttributes(TypedDict, total=False):
    attribute1: str
    attribute2: str

class SellbriteConnector:
    """Sellbrite connector ().

    Provides 9 tools.
    """

    def sellbrite_create_warehouse(
        self,
        address_line_1: str,
        city: str,
        country: str,
        name: str,
        postal_code: str,
        state: str,
        address_line_2: Optional[str] = None,
        phone: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new warehouse in Sellbrite for storing and managing product inventory. Use this tool when adding a new physical or virtual warehouse location to your Sellbrite account. Do not use this tool to update an existing warehouse.

        Args:
            address_line_1: First line of the customer's address. (required)
            city: Customer's city. (required)
            country: Customer's country. (required)
            name: Customer's full name. (required)
            postal_code: Customer's postal code or zip code. (required)
            state: Customer's state or province. (required)
            address_line_2: Second line of the customer's address (optional).
            phone: Customer's phone number.
        Returns:
            API response as a dictionary.
        """
        ...

    def sellbrite_delete_product(
        self,
        productSku: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a product from Sellbrite, identified by its SKU. Use this tool only when a product must be fully removed from the catalog. This action is irreversible and cannot be undone. Do not use this tool to simply update or deactivate a product.

        Args:
            productSku: Product SKU for Sellbrite API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sellbrite_get_product(
        self,
        productSku: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single product in Sellbrite, identified by its SKU. Use this tool to fetch product title, description, pricing, and attributes for a specific SKU. Do not use this tool to retrieve a list of all products.

        Args:
            productSku: Product SKU for the Sellbrite API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sellbrite_list_inventory(
        self,
    ) -> Dict[str, Any]:
        """Lists current inventory levels for all products in Sellbrite. Use this tool to retrieve stock quantities, warehouse allocations, and inventory details across all SKUs. Do not use this tool to update inventory levels or retrieve details for a single product.
        Returns:
            API response as a dictionary.
        """
        ...

    def sellbrite_list_orders(
        self,
    ) -> Dict[str, Any]:
        """Lists all orders in Sellbrite. Use this tool to retrieve a collection of orders, optionally filtered by status or date range. Returns order details including line items, quantities, shipping information, and fulfillment status. Do not use this tool to retrieve a single order by ID.
        Returns:
            API response as a dictionary.
        """
        ...

    def sellbrite_list_products(
        self,
    ) -> Dict[str, Any]:
        """Lists all products in the Sellbrite catalog. Use this tool to retrieve a collection of products including their SKUs, titles, pricing, and inventory details. Do not use this tool to retrieve a single product by SKU.
        Returns:
            API response as a dictionary.
        """
        ...

    def sellbrite_list_warehouses(
        self,
    ) -> Dict[str, Any]:
        """Lists all warehouses configured in Sellbrite. Use this tool to retrieve warehouse names, addresses, and identifiers. Do not use this tool to retrieve, update, or create a single warehouse.
        Returns:
            API response as a dictionary.
        """
        ...

    def sellbrite_update_warehouse(
        self,
        name: str,
        warehouseId: str,
        address_line_1: Optional[str] = None,
        city: Optional[str] = None,
        country: Optional[str] = None,
        phone: Optional[str] = None,
        postal_code: Optional[str] = None,
        state: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing warehouse in Sellbrite, identified by its warehouse ID. Use this tool to modify warehouse name, address, or other configuration fields. This operation overwrites the existing warehouse record. Do not use this tool to create a new warehouse.

        Args:
            name: The name. (required)
            warehouseId: The ID of the warehouse. (required)
            address_line_1: The first line of the address.
            city: The city.
            country: The country.
            phone: The phone number.
            postal_code: The postal code.
            state: The state or province.
        Returns:
            API response as a dictionary.
        """
        ...

    def sellbrite_upsert_product(
        self,
        category_name: str,
        name: str,
        price: str,
        productSku: str,
        asin: Optional[str] = None,
        brand: Optional[str] = None,
        condition: Optional[str] = None,
        condition_note: Optional[str] = None,
        custom_attributes: Optional[_SellbriteUpsertProductCustomAttributes] = None,
        description: Optional[str] = None,
        ean: Optional[str] = None,
        epid: Optional[str] = None,
        features: Optional[List[Any]] = None,
        gtin: Optional[str] = None,
        image_list: Optional[List[Any]] = None,
        isbn: Optional[str] = None,
        manufacturer: Optional[str] = None,
        manufacturer_model_number: Optional[str] = None,
        msrp: Optional[float] = None,
        notes: Optional[str] = None,
        package_height: Optional[float] = None,
        package_length: Optional[float] = None,
        package_unit_of_length: Optional[str] = None,
        package_unit_of_weight: Optional[str] = None,
        package_weight: Optional[float] = None,
        package_width: Optional[float] = None,
        upc: Optional[str] = None,
        warranty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new product or updates an existing product in Sellbrite, identified by its SKU. Use this tool when you need to insert a product that may or may not already exist, or when updating product details such as title, price, or description. If the SKU already exists, the existing record will be overwritten. Do not use this tool for partial updates to a single field.

        Args:
            category_name: Name of the product category. (required)
            name: Name of the product. (required)
            price: Price of the product. (required)
            productSku: SKU of the product to be updated.  Required for updates. (required)
            asin: ASIN of the product.
            brand: Brand of the product.
            condition: Condition of the product (e.g., new, used).
            condition_note: Notes about the product's condition.
            custom_attributes: Custom attributes associated with the product.
            description: Detailed description of the product.
            ean: EAN of the product.
            epid: Epid of the product.
            features: List of product features.
            gtin: GTIN of the product.
            image_list: List of URLs for product images.
            isbn: ISBN of the product.
            manufacturer: Name of the product manufacturer.
            manufacturer_model_number: Manufacturer's model number for the product.
            msrp: Manufacturer's Suggested Retail Price.
            notes: Internal notes about the product.
            package_height: Height of the product's package.
            package_length: Length of the product's package.
            package_unit_of_length: Unit of measurement for package length (e.g., inches, centimeters).
            package_unit_of_weight: Unit of measurement for package weight (e.g., pounds, kilograms).
            package_weight: Weight of the product's package.
            package_width: Width of the product's package.
            upc: UPC of the product.
            warranty: Warranty information for the product.
        Returns:
            API response as a dictionary.
        """
        ...

