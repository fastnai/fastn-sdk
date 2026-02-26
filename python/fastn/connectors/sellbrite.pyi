"""Fastn Sellbrite connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SellbriteConnector:
    """Sellbrite connector ().

    Provides 9 tools.
    """

    def create_warehouse(
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
        """Creates a new warehouse for storing products using the Warehouses connector.

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

    def delete_product(
        self,
        productSku: str,
    ) -> Dict[str, Any]:
        """Removes a product from the inventory via the Products connector.

        Args:
            productSku: Product SKU for Sellbrite API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inventory(
        self,
    ) -> Dict[str, Any]:
        """Fetches the current inventory levels for products from the Inventory connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_orders(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of orders placed using the Orders connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product(
        self,
        productSku: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific product using the Products connector.

        Args:
            productSku: Product SKU for the Sellbrite API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of products in the inventory using the Products connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_warehouses(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of warehouses where products are stored using the Warehouses connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def updatewarehouses(
        self,
        name: str,
        address_line_1: Optional[str] = None,
        city: Optional[str] = None,
        country: Optional[str] = None,
        phone: Optional[str] = None,
        postal_code: Optional[str] = None,
        state: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates information for existing warehouses using the Warehouses connector.

        Args:
            name: The name. (required)
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

    def upsert_product(
        self,
        category_name: str,
        name: str,
        price: str,
        asin: Optional[str] = None,
        brand: Optional[str] = None,
        condition: Optional[str] = None,
        condition_note: Optional[str] = None,
        custom_attributes: Optional[Dict[str, Any]] = None,
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
        """Adds or updates a product in the inventory through the Products connector.

        Args:
            category_name: Name of the product category. (required)
            name: Name of the product. (required)
            price: Price of the product. (required)
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

