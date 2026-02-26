"""Fastn CommerceTools connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class CommercetoolsConnector:
    """CommerceTools connector ().

    Provides 63 tools.
    """

    def change_password_of_customer(
        self,
        currentPassword: str,
        id: str,
        newPassword: str,
        version: int,
    ) -> Dict[str, Any]:
        """Changes the password for a specific customer in the system.

        Args:
            currentPassword: The current password for authentication. (required)
            id: ID of the user to update. (required)
            newPassword: The new password for the user. (required)
            version: Version number for optimistic concurrency control. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def change_password_of_customer_in_store(
        self,
    ) -> Dict[str, Any]:
        """Changes the password for a specific customer in a store.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_a_customer(
        self,
        email: str,
        firstName: str,
        lastName: str,
        password: str,
    ) -> Dict[str, Any]:
        """Creates a new customer account in the system.

        Args:
            email: Customer's email address. (required)
            firstName: Customer's first name. (required)
            lastName: Customer's last name. (required)
            password: Customer's password. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_a_customer_in_store(
        self,
    ) -> Dict[str, Any]:
        """Creates a new customer account in a specific store.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_attribute_group(
        self,
        authToken: str,
        region: str,
        storeName: str,
    ) -> Dict[str, Any]:
        """Creates a new attribute group within the system.

        Args:
            authToken: The authentication token for the CommerceTools API. (required)
            region: The region of the CommerceTools store. (required)
            storeName: The name of the store within CommerceTools. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_cart_discount(
        self,
        cartPredicate: str,
        isActive: bool,
        name: Dict[str, Any],
        sortOrder: str,
        stores: List[Any],
        requiresDiscountCode: Optional[bool] = None,
        target: Optional[Dict[str, Any]] = None,
        value: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new cart discount in the system.

        Args:
            cartPredicate: Predicate for filtering carts. (required)
            isActive: Indicates whether the resource is active. (required)
            name: Name of the resource. (required)
            sortOrder: Sort order for the results. (required)
            stores:  (required)
            requiresDiscountCode: Indicates whether a discount code is required.
            target: Target details.
            value: Value details.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_cart_discount_in_store(
        self,
    ) -> Dict[str, Any]:
        """Creates a new cart discount for a specific store.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_category(
        self,
        name: Dict[str, Any],
        parent: Dict[str, Any],
        slug: Dict[str, Any],
        orderHint: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new category within the system.

        Args:
            name: Name of the resource. (required)
            parent: Parent resource details. (required)
            slug: Slug of the resource. (required)
            orderHint: Order hint for the resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_inventory(
        self,
        availableQuantity: int,
        quantityOnStock: int,
        sku: str,
    ) -> Dict[str, Any]:
        """Creates a new inventory entry in the system.

        Args:
            availableQuantity: The number of items currently available. (required)
            quantityOnStock: The total quantity of items in stock. (required)
            sku: The Stock Keeping Unit (SKU) identifier. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_password_reset_token_for_customer(
        self,
        email: str,
    ) -> Dict[str, Any]:
        """Creates a password reset token for a customer in the system.

        Args:
            email: Customer's email address. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product(
        self,
        masterVariant: Dict[str, Any],
        name: Dict[str, Any],
        productType: Dict[str, Any],
        slug: Dict[str, Any],
        variants: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new product within the system.

        Args:
            masterVariant: Master variant of the product. (required)
            name: Product name in different languages. (required)
            productType: Product type of the product. (required)
            slug: Product slug in different languages. (required)
            variants: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product_discount(
        self,
        name: Dict[str, Any],
        sortOrder: str,
        description: Optional[Dict[str, Any]] = None,
        isActive: Optional[bool] = None,
        predicate: Optional[str] = None,
        value: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new product discount within the system.

        Args:
            name: Name of the resource (localized). (required)
            sortOrder: Specifies the sorting order for the results. (required)
            description: Description of the resource (localized).
            isActive: Indicates whether the resource is active.
            predicate: Query predicate for filtering results.
            value: Value of the resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product_type(
        self,
        name: str,
        attributes: Optional[List[Any]] = None,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new product type within the system.

        Args:
            name: Name of the resource. (required)
            attributes: 
            description: Description of the resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_stand_alone_prices(
        self,
        Authorization: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates new stand-alone prices in the system.

        Args:
            Authorization: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_store(
        self,
        key: str,
        name: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new store within the system.

        Args:
            key: Unique key for the resource. (required)
            name: Name of the resource (localized). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_attribute_group(
        self,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified attribute group from the system.

        Args:
            version: Version of the resource in CommerceTools.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_attribute_group_by_key(
        self,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified attribute group using its unique key.

        Args:
            version: Version of the CommerceTools API.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product(
        self,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific product from the system.

        Args:
            version: The version of the API.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product_discount_by_id(
        self,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific product discount using its unique ID.

        Args:
            version: Version of the API.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product_discount_by_key(
        self,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified product discount using its unique key.

        Args:
            version: Version number for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product_type_by_id(
        self,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific product type using its unique ID.

        Args:
            version: Version of the API being used.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_stand_alone_price_by_id(
        self,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific stand-alone price using its unique ID.

        Args:
            version: Version number for the CommerceTools API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_stand_alone_price_by_key(
        self,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified stand-alone price using its unique key.

        Args:
            version: Version of the API.
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_auth_token(
        self,
    ) -> Dict[str, Any]:
        """Generates an authentication token for accessing secure endpoints in the API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_a_category_by_id(
        self,
        categoryId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific category identified by its ID.

        Args:
            categoryId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_a_category_by_key(
        self,
        categoryKey: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific category identified by its key.

        Args:
            categoryKey:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_cart_discounts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all cart discounts available in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_cart_discounts_in_store(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all cart discounts available in a specific store.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_categories(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all categories available in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_customers(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all customers currently in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_customers_in_store(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all customers associated with a specific store.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_product_discounts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all product discounts currently active.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_stand_alone_price(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all stand-alone prices available in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_stores(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all stores currently available in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_an_inventory_by_id(
        self,
        inventoryId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific inventory identified by its ID.

        Args:
            inventoryId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_an_inventory_by_key(
        self,
    ) -> Dict[str, Any]:
        """Fetches details of a specific inventory identified by its key.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_attribute_group_by_id(
        self,
        authToken: str,
        region: str,
        storeName: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of an attribute group using its unique ID.

        Args:
            authToken: Authentication token for the CommerceTools API. (required)
            region: Region of the CommerceTools store. (required)
            storeName: Name of the store in CommerceTools. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_attribute_group_by_key(
        self,
        authToken: str,
        region: str,
        storeName: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of an attribute group using its unique key.

        Args:
            authToken: Authentication token for the CommerceTools API. (required)
            region: Region of the CommerceTools store. (required)
            storeName: Name of the store in CommerceTools. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_cart_discount_by_id(
        self,
        CartDiscountId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific cart discount identified by its ID.

        Args:
            CartDiscountId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_cart_discount_in_store_by_id(
        self,
    ) -> Dict[str, Any]:
        """Fetches details of a cart discount in a specific store by its ID.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_by_id(
        self,
        customerId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific customer identified by their ID.

        Args:
            customerId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_by_key(
        self,
    ) -> Dict[str, Any]:
        """Fetches details of a specific customer identified by their key.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_by_password_token(
        self,
    ) -> Dict[str, Any]:
        """Fetches details of a customer using their password reset token.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_in_store_by_id(
        self,
    ) -> Dict[str, Any]:
        """Fetches details of a specific customer in a store identified by their ID.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customer_in_store_by_key(
        self,
    ) -> Dict[str, Any]:
        """Fetches details of a specific customer in a store identified by their key.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_inventory(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the current inventory details.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_by_id(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific product identified by its ID.

        Args:
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_by_sku(
        self,
    ) -> Dict[str, Any]:
        """Fetches details of a specific product identified by its SKU (Stock Keeping Unit).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_discount_by_id(
        self,
        productDiscountId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific product discount identified by its ID.

        Args:
            productDiscountId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_discount_by_key(
        self,
    ) -> Dict[str, Any]:
        """Fetches details of a specific product discount identified by its key.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_type_by_id(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific product type using its unique ID.

        Args:
            id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_type_by_key(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific product type using its unique key.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of products currently available in the system.

        Args:
            limit: The limit for pagination.
            offset: The offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stand_alone_price_by_id(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the details of a stand-alone price using its unique ID.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stand_alone_price_by_key(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the details of a stand-alone price using its unique key.
        Returns:
            API response as a dictionary.
        """
        ...

    def reset_password_of_customer(
        self,
        newPassword: str,
        tokenValue: str,
    ) -> Dict[str, Any]:
        """Resets the password for a specific customer in the system.

        Args:
            newPassword: New password for the CommerceTools API. (required)
            tokenValue: Token value for the CommerceTools API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_attribute_group_by_id(
        self,
        authToken: str,
        region: str,
        storeName: str,
    ) -> Dict[str, Any]:
        """Updates an existing attribute group using its unique ID.

        Args:
            authToken: The authentication token for accessing CommerceTools. (required)
            region: The region of the CommerceTools store. (required)
            storeName: The name of the CommerceTools store. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_attribute_group_by_key(
        self,
        authToken: str,
        region: str,
        storeName: str,
    ) -> Dict[str, Any]:
        """Updates an existing attribute group using its unique key.

        Args:
            authToken: The authentication token for the CommerceTools API. (required)
            region: The region of the CommerceTools store. (required)
            storeName: The name of the CommerceTools store. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_category_by_key(
        self,
    ) -> Dict[str, Any]:
        """Updates a category's information using its unique key.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_key_of_inventory_by_id(
        self,
        actions: List[Any],
        version: int,
    ) -> Dict[str, Any]:
        """Updates the key of a specified inventory using its unique ID.

        Args:
            actions:  (required)
            version: Version number. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_name_of_category_by_id(
        self,
        actions: Optional[List[Any]] = None,
        version: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates the name of a specified category using its unique ID.

        Args:
            actions: 
            version: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product_type_by_id(
        self,
        actions: List[Any],
        version: float,
    ) -> Dict[str, Any]:
        """Updates the product type information using the unique ID of the product type.

        Args:
            actions:  (required)
            version: The version number. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product_type_by_key(
        self,
        authToken: str,
        region: str,
        storeName: str,
    ) -> Dict[str, Any]:
        """Updates the product type information using the unique key of the product type.

        Args:
            authToken: Authentication token for the CommerceTools API. (required)
            region: Region of the CommerceTools store. (required)
            storeName: Name of the store in CommerceTools. (required)
        Returns:
            API response as a dictionary.
        """
        ...

