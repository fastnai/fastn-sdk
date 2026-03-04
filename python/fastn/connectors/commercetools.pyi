"""Fastn CommerceTools connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _CommercetoolsCreateAttributeGroupDescription(TypedDict, total=False):
    en: str

class _CommercetoolsCreateAttributeGroupName(TypedDict, total=False):
    en: str

class _CommercetoolsCreateCartDiscountName(TypedDict, total=False):
    en: str

class _CommercetoolsCreateCartDiscountTarget(TypedDict, total=False):
    predicate: str
    type: str

class _CommercetoolsCreateCartDiscountValue(TypedDict, total=False):
    permyriad: int
    type: str

class _CommercetoolsCreateCartDiscountInStoreName(TypedDict, total=False):
    en: str

class _CommercetoolsCreateCartDiscountInStoreTarget(TypedDict, total=False):
    predicate: str
    type: str

class _CommercetoolsCreateCartDiscountInStoreValue(TypedDict, total=False):
    permyriad: int
    type: str

class _CommercetoolsCreateCategoryName(TypedDict, total=False):
    en: str

class _CommercetoolsCreateCategoryParent(TypedDict, total=False):
    id: str
    typeId: str

class _CommercetoolsCreateCategorySlug(TypedDict, total=False):
    en: str

class _CommercetoolsCreateProductMastervariant(TypedDict, total=False):
    images: List[Any]
    prices: List[Any]
    sku: str

class _CommercetoolsCreateProductName(TypedDict, total=False):
    en: str

class _CommercetoolsCreateProductProducttype(TypedDict, total=False):
    id: str
    typeId: str

class _CommercetoolsCreateProductSlug(TypedDict, total=False):
    en: str

class _CommercetoolsCreateProductDiscountName(TypedDict, total=False):
    en: str

class _CommercetoolsCreateProductDiscountDescription(TypedDict, total=False):
    en: str

class _CommercetoolsCreateProductDiscountValue(TypedDict, total=False):
    money: List[Any]
    type: str

class _CommercetoolsCreateStandalonePriceValue(TypedDict, total=False):
    centAmount: int
    currencyCode: str

class _CommercetoolsCreateStoreName(TypedDict, total=False):
    en: str

class CommercetoolsConnector:
    """CommerceTools connector ().

    Provides 63 tools.
    """

    def commercetools_change_customer_password(
        self,
        currentPassword: str,
        id: str,
        newPassword: str,
        version: int,
    ) -> Dict[str, Any]:
        """Changes the password for a specific CommerceTools customer using their current password. Use this when the customers existing password is known and needs to be updated. Do not use this for password resets where the current password is unknown — use commercetools_reset_customer_password instead. This action permanently modifies the customers login credentials.

        Args:
            currentPassword: The current password for authentication. (required)
            id: ID of the user to update. (required)
            newPassword: The new password for the user. (required)
            version: Version number for optimistic concurrency control. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_change_customer_password_in_store(
        self,
        currentPassword: str,
        id: str,
        newPassword: str,
        storeKey: str,
        version: int,
    ) -> Dict[str, Any]:
        """Changes the password for a specific customer within a designated store context in CommerceTools. Use this when the customers current password is known and needs to be updated within a store-scoped context. Do not use this for password resets (where the current password is unknown) — use commercetools_reset_customer_password instead. This action permanently modifies the customers credentials.

        Args:
            currentPassword: The current password for authentication (for password updates). (required)
            id: The unique identifier for the user or account. (required)
            newPassword: The new password for the user or account. (required)
            storeKey: The unique identifier for the store within CommerceTools. (required)
            version: Version number for optimistic concurrency control. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_create_attribute_group(
        self,
        attributes: List[Any],
        authToken: str,
        description: _CommercetoolsCreateAttributeGroupDescription,
        key: str,
        name: _CommercetoolsCreateAttributeGroupName,
        region: str,
        storeName: str,
    ) -> Dict[str, Any]:
        """Creates a new attribute group in CommerceTools. Attribute groups define how product type attributes are organized and displayed in the Merchant Center UI. Use this when you need to introduce a new grouping of product attributes. Do not use this to update an existing group — use commercetools_update_attribute_group_by_id or commercetools_update_attribute_group_by_key instead. This action creates a persistent attribute group record.

        Args:
            attributes:  (required)
            authToken: The authentication token for the CommerceTools API. (required)
            description: Description of the product, localized by language. (required)
            key: Unique identifier for the product within CommerceTools. (required)
            name: Name of the product, localized by language. (required)
            region: The region of the CommerceTools store. (required)
            storeName: The name of the store within CommerceTools. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_create_cart_discount(
        self,
        cartPredicate: str,
        isActive: bool,
        name: _CommercetoolsCreateCartDiscountName,
        sortOrder: str,
        stores: List[Any],
        requiresDiscountCode: Optional[bool] = None,
        target: Optional[_CommercetoolsCreateCartDiscountTarget] = None,
        value: Optional[_CommercetoolsCreateCartDiscountValue] = None,
    ) -> Dict[str, Any]:
        """Creates a new global cart discount in CommerceTools. Use this when a discount should apply across all stores. Do not use this if the discount should be scoped to a specific store — use commercetools_create_cart_discount_in_store instead. This action creates a persistent discount record that will affect cart pricing.

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

    def commercetools_create_cart_discount_in_store(
        self,
        name: _CommercetoolsCreateCartDiscountInStoreName,
        stores: List[Any],
        cartPredicate: Optional[str] = None,
        isActive: Optional[bool] = None,
        requiresDiscountCode: Optional[bool] = None,
        sortOrder: Optional[str] = None,
        storeKey: Optional[str] = None,
        target: Optional[_CommercetoolsCreateCartDiscountInStoreTarget] = None,
        value: Optional[_CommercetoolsCreateCartDiscountInStoreValue] = None,
    ) -> Dict[str, Any]:
        """Creates a new cart discount scoped to a specific store in CommerceTools. Use this when a discount should apply only within a particular store context. Do not use this to create a global cart discount — use commercetools_create_cart_discount instead. This action creates a persistent discount record that will affect cart pricing within the store.

        Args:
            name: The name of the entity. (required)
            stores:  (required)
            cartPredicate: A predicate to filter carts.
            isActive: Indicates whether the entity is active.
            requiresDiscountCode: Indicates whether a discount code is required for this operation.
            sortOrder: Specifies the sort order for the results.
            storeKey: The unique identifier for the store.
            target: Specifies the target of the operation.
            value: The value of the entity.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_create_category(
        self,
        name: _CommercetoolsCreateCategoryName,
        parent: _CommercetoolsCreateCategoryParent,
        slug: _CommercetoolsCreateCategorySlug,
        orderHint: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new product category in CommerceTools. Use this to define a new category for organizing products, including setting its name, slug, and optional parent category. Do not use this to update an existing category — use commercetools_update_category_by_id or commercetools_update_category_by_key instead. This action creates a persistent category record.

        Args:
            name: Name of the resource. (required)
            parent: Parent resource details. (required)
            slug: Slug of the resource. (required)
            orderHint: Order hint for the resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_create_customer(
        self,
        email: str,
        firstName: str,
        lastName: str,
        password: str,
    ) -> Dict[str, Any]:
        """Creates a new global customer account in CommerceTools. Use this when registering a customer without a specific store scope. Do not use this if the customer should be tied to a specific store — use commercetools_create_customer_in_store instead. This action creates a persistent customer record.

        Args:
            email: Customer's email address. (required)
            firstName: Customer's first name. (required)
            lastName: Customer's last name. (required)
            password: Customer's password. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_create_customer_in_store(
        self,
        email: str,
        firstName: str,
        lastName: str,
        password: str,
        storeKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new customer account scoped to a specific store in CommerceTools. Use this when a customer should be registered within a particular store context. Do not use this to create a global customer account — use commercetools_create_customer instead. This action creates a persistent customer record.

        Args:
            email: The email address of the user. (required)
            firstName: The first name of the user. (required)
            lastName: The last name of the user. (required)
            password: The password for the user. (required)
            storeKey: The unique identifier for the store.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_create_customer_password_reset_token(
        self,
        email: str,
    ) -> Dict[str, Any]:
        """Creates a password reset token for a specific CommerceTools customer, initiating the password reset flow. Use this when a customer requests a password reset. The generated token should then be passed to commercetools_reset_customer_password to complete the reset. Do not use this to directly change a password. The token has a limited validity period.

        Args:
            email: Customer's email address. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_create_inventory(
        self,
        availableQuantity: int,
        quantityOnStock: int,
        sku: str,
    ) -> Dict[str, Any]:
        """Creates a new inventory entry for a product variant in CommerceTools. Use this to register stock availability for a specific SKU at a supply channel. Do not use this to update an existing inventory entry — use commercetools_update_inventory_by_id instead. This action creates a persistent inventory record.

        Args:
            availableQuantity: The number of items currently available. (required)
            quantityOnStock: The total quantity of items in stock. (required)
            sku: The Stock Keeping Unit (SKU) identifier. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_create_product(
        self,
        masterVariant: _CommercetoolsCreateProductMastervariant,
        name: _CommercetoolsCreateProductName,
        productType: _CommercetoolsCreateProductProducttype,
        slug: _CommercetoolsCreateProductSlug,
        variants: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the CommerceTools catalog. Use this when you need to add a brand-new product with its attributes, variants, and pricing. Do not use this to update an existing product. This action is irreversible without a subsequent delete; the product will be visible in the catalog once published.

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

    def commercetools_create_product_discount(
        self,
        name: _CommercetoolsCreateProductDiscountName,
        sortOrder: str,
        description: Optional[_CommercetoolsCreateProductDiscountDescription] = None,
        isActive: Optional[bool] = None,
        predicate: Optional[str] = None,
        value: Optional[_CommercetoolsCreateProductDiscountValue] = None,
    ) -> Dict[str, Any]:
        """Creates a new product discount in CommerceTools. Use this when you need to define a discount that applies to specific products or product variants. Do not use this for cart-level discounts — use commercetools_create_cart_discount instead. This action creates a persistent discount record that will affect product pricing.

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

    def commercetools_create_product_type(
        self,
        name: str,
        attributes: Optional[List[Any]] = None,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new product type in CommerceTools. Product types define the custom attribute schema for a group of products. Use this when you need to introduce a new set of product attributes. Do not use this to update an existing product type — use commercetools_update_product_type_by_id or commercetools_update_product_type_by_key instead. This action creates a persistent schema record.

        Args:
            name: Name of the resource. (required)
            attributes: 
            description: Description of the resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_create_standalone_price(
        self,
        sku: str,
        value: _CommercetoolsCreateStandalonePriceValue,
        Authorization: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new standalone price for a product variant in CommerceTools. Standalone prices are managed independently of embedded prices and can be scoped by country, currency, customer group, or channel. Use this to add pricing outside of the products embedded price list. This action creates a persistent price record that will affect storefront pricing.

        Args:
            sku: Stock Keeping Unit (SKU) identifier. (required)
            value: Details about the value being sent to CommerceTools. (required)
            Authorization: 
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_create_store(
        self,
        key: str,
        name: _CommercetoolsCreateStoreName,
    ) -> Dict[str, Any]:
        """Creates a new store within the CommerceTools project. Use this when setting up a new sales channel or regional store. Do not use this to update an existing store. This action creates a persistent store record that can be used to scope customers, inventory, and discounts.

        Args:
            key: Unique key for the resource. (required)
            name: Name of the resource (localized). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_delete_attribute_group_by_id(
        self,
        id: str,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific attribute group from CommerceTools using its unique ID. Attribute groups define how product attributes are organized in the Merchant Center UI. Use this only when an attribute group must be fully removed. This action is irreversible. Do not use this to delete by key — use commercetools_delete_attribute_group_by_key instead.

        Args:
            id:  (required)
            version: Version of the resource in CommerceTools.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_delete_attribute_group_by_key(
        self,
        key: str,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific attribute group from CommerceTools using its unique key. Attribute groups define how product attributes are organized in the Merchant Center UI. Use this only when an attribute group must be fully removed. This action is irreversible. Do not use this to delete by ID — use commercetools_delete_attribute_group_by_id instead.

        Args:
            key: Key identifier for the request in CommerceTools. (required)
            version: Version of the CommerceTools API.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_delete_product(
        self,
        productId: str,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific product from the CommerceTools catalog by its unique product ID. Use this only when a product must be fully removed. This action is irreversible — the product and all its variants cannot be recovered after deletion. Do not use this to unpublish or deactivate a product.

        Args:
            productId: The ID of the product. (required)
            version: The version of the API.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_delete_product_discount_by_id(
        self,
        productDiscountId: str,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific product discount from CommerceTools using its unique ID. Use this only when a product discount must be fully removed and you have the discount ID available. This action is irreversible. Do not use this to delete by key — use commercetools_delete_product_discount_by_key instead.

        Args:
            productDiscountId:  (required)
            version: Version of the API.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_delete_product_discount_by_key(
        self,
        productDiscountKey: str,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific product discount from CommerceTools using its unique key. Use this only when a product discount must be fully removed and you have the discount key available. This action is irreversible. Do not use this to delete by ID — use commercetools_delete_product_discount_by_id instead.

        Args:
            productDiscountKey: Key for the product discount. (required)
            version: Version number for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_delete_product_type_by_id(
        self,
        id: str,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific product type from CommerceTools using its unique ID. Product types define the custom attributes available to products. Use this only when a product type must be fully removed; this may impact products referencing this type. This action is irreversible. Do not use this to delete by key.

        Args:
            id:  (required)
            version: Version of the API being used.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_delete_standalone_price_by_id(
        self,
        standAlonePriceId: Optional[str] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific standalone price from CommerceTools using its unique ID. Standalone prices are product variant prices managed independently of embedded price lists. Use this only when a standalone price must be fully removed and you have the price ID. This action is irreversible. Do not use this to delete by key — use commercetools_delete_standalone_price_by_key instead.

        Args:
            standAlonePriceId: ID of the standalone price in CommerceTools.
            version: Version number for the CommerceTools API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_delete_standalone_price_by_key(
        self,
        standAlonePriceKey: Optional[str] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific standalone price from CommerceTools using its unique key. Standalone prices are product variant prices managed independently of embedded price lists. Use this only when a standalone price must be fully removed and you have the price key. This action is irreversible. Do not use this to delete by ID — use commercetools_delete_standalone_price_by_id instead.

        Args:
            standAlonePriceKey: Key for the standalone price.
            version: Version of the API.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_generate_auth_token(
        self,
        ctRegion: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates an OAuth 2.0 client-credentials authentication token for accessing secured CommerceTools API endpoints. Use this before making API calls that require authorization. The token is scoped to the permissions defined by the provided scope parameter. Do not use this for customer-facing login flows — this is for machine-to-machine API authentication only.

        Args:
            ctRegion: Specifies the CommerceTools region.
            scope: Scope of access for the API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_attribute_group_by_id(
        self,
        authToken: str,
        region: str,
        storeName: str,
        id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific attribute group in CommerceTools by its unique ID. Use this when you have the attribute group ID and need to inspect its configuration. Do not use this when you only have the group key — use commercetools_get_attribute_group_by_key instead. This tool does not modify any data.

        Args:
            authToken: Authentication token for the CommerceTools API. (required)
            region: Region of the CommerceTools store. (required)
            storeName: Name of the store in CommerceTools. (required)
            id: Identifier for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_attribute_group_by_key(
        self,
        authToken: str,
        region: str,
        storeName: str,
        key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific attribute group in CommerceTools by its unique key. Use this when you have the attribute group key and need to inspect its configuration. Do not use this when you only have the group ID — use commercetools_get_attribute_group_by_id instead. This tool does not modify any data.

        Args:
            authToken: Authentication token for the CommerceTools API. (required)
            region: Region of the CommerceTools store. (required)
            storeName: Name of the store in CommerceTools. (required)
            key: API key for accessing CommerceTools.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_cart_discount_by_id(
        self,
        CartDiscountId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific global cart discount in CommerceTools by its unique ID. Use this when you need discount configuration details and have the discount ID available. Do not use this for store-scoped discounts — use commercetools_get_cart_discount_in_store_by_id instead. This tool does not modify any data.

        Args:
            CartDiscountId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_cart_discount_in_store_by_id(
        self,
        cartDiscountId: Optional[str] = None,
        storeKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific cart discount within a designated store in CommerceTools, identified by its unique ID. Use this when you need store-scoped cart discount data and have the discount ID available. Do not use this for global (non-store-scoped) discount lookup — use commercetools_get_cart_discount_by_id instead. This tool does not modify any data.

        Args:
            cartDiscountId: 
            storeKey: The key of the store.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_category_by_id(
        self,
        categoryId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific category in CommerceTools by its unique ID. Use this when you have the category ID and need category details. Do not use this when you only have the category key — use commercetools_get_category_by_key instead. This tool does not modify any data.

        Args:
            categoryId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_category_by_key(
        self,
        categoryKey: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific category in CommerceTools by its unique key. Use this when you have the category key and need category details. Do not use this when you only have the category ID — use commercetools_get_category_by_id instead. This tool does not modify any data.

        Args:
            categoryKey:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_customer_by_id(
        self,
        customerId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details of a single CommerceTools customer by their unique customer ID. Use this when you have the customer ID and need customer profile information. Do not use this for store-scoped customer lookup — use commercetools_get_customer_in_store_by_id instead. This tool does not modify any data.

        Args:
            customerId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_customer_by_key(
        self,
        customerKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves full details of a single CommerceTools customer by their unique customer key. Use this when you have the customer key and need customer profile information. Do not use this for store-scoped customer lookup — use commercetools_get_customer_in_store_by_key instead. This tool does not modify any data.

        Args:
            customerKey: Unique identifier for the customer in CommerceTools.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_customer_by_password_token(
        self,
        passwordToken: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a CommerceTools customer using their active password reset token. Use this to identify which customer is associated with a given reset token before completing a password reset flow. Do not use this for general customer lookup — use commercetools_get_customer_by_id or commercetools_get_customer_by_key instead. This tool does not modify any data.

        Args:
            passwordToken: The password token for authentication with CommerceTools. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_customer_in_store_by_id(
        self,
        customerId: str,
        storeKey: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific customer within a designated store in CommerceTools, identified by the customers unique ID. Use this when you need store-scoped customer data and have the customer ID available. Do not use this for global (non-store-scoped) customer lookup — use commercetools_get_customer_by_id instead. This tool does not modify any data.

        Args:
            customerId:  (required)
            storeKey:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_customer_in_store_by_key(
        self,
        customerkey: str,
        storeKey: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific customer within a designated store in CommerceTools, identified by the customers unique key. Use this when you need store-scoped customer data and have the customer key available. Do not use this for global (non-store-scoped) customer lookup — use commercetools_get_customer_by_key instead. This tool does not modify any data.

        Args:
            customerkey: Unique identifier for the customer in the CommerceTools platform. (required)
            storeKey: Unique identifier for the store in the CommerceTools platform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_inventory_by_id(
        self,
        inventoryId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific inventory entry in CommerceTools by its unique ID. Use this when you have the inventory ID and need stock details. Do not use this when you only have the inventory key — use commercetools_get_inventory_by_key instead. This tool does not modify any data.

        Args:
            inventoryId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_inventory_by_key(
        self,
        inventoryKey: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific inventory entry in CommerceTools by its unique key. Use this when you have the inventory key and need stock details. Do not use this when you only have the inventory ID — use commercetools_get_inventory_by_id instead. This tool does not modify any data.

        Args:
            inventoryKey: Unique identifier for the inventory item in CommerceTools. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_product_by_id(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details of a single CommerceTools product by its unique product ID. Use this when you need to look up a specific products attributes, variants, prices, or metadata. Do not use this to search or list multiple products — use commercetools_list_products instead. This tool does not modify any data.

        Args:
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_product_by_sku(
        self,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific product variant in CommerceTools by its SKU (Stock Keeping Unit) using the GraphQL API. Use this when you have the SKU and need product or variant details. Do not use this to look up a product by ID — use commercetools_get_product_by_id instead. This tool does not modify any data.

        Args:
            sku: The SKU of the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_product_discount_by_id(
        self,
        productDiscountId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific product discount in CommerceTools by its unique ID. Use this when you have the discount ID and need discount configuration details. Do not use this when you only have the discount key — use commercetools_get_product_discount_by_key instead. This tool does not modify any data.

        Args:
            productDiscountId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_product_discount_by_key(
        self,
        productDiscountKey: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific product discount in CommerceTools by its unique key. Use this when you have the discount key and need discount configuration details. Do not use this when you only have the discount ID — use commercetools_get_product_discount_by_id instead. This tool does not modify any data.

        Args:
            productDiscountKey: Key for identifying the product discount in CommerceTools. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_product_type_by_id(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific product type in CommerceTools by its unique ID. Use this when you have the product type ID and need its attribute schema. Do not use this when you only have the product type key — use commercetools_get_product_type_by_key instead. This tool does not modify any data.

        Args:
            id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_product_type_by_key(
        self,
        key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific product type in CommerceTools by its unique key. Use this when you have the product type key and need its attribute schema. Do not use this when you only have the product type ID — use commercetools_get_product_type_by_id instead. This tool does not modify any data.

        Args:
            key: API key for accessing the CommerceTools platform.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_standalone_price_by_id(
        self,
        StandAlonePriceid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific standalone price in CommerceTools by its unique ID. Use this when you have the price ID and need pricing configuration details. Do not use this when you only have the price key — use commercetools_get_standalone_price_by_key instead. This tool does not modify any data.

        Args:
            StandAlonePriceid: The ID of the standalone price in CommerceTools.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_get_standalone_price_by_key(
        self,
        standAlonePriceKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific standalone price in CommerceTools by its unique key. Use this when you have the price key and need pricing configuration details. Do not use this when you only have the price ID — use commercetools_get_standalone_price_by_id instead. This tool does not modify any data.

        Args:
            standAlonePriceKey: The key for the standalone price.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_list_cart_discounts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all global cart discounts available in the CommerceTools project. Use this when you need to review or audit all cart discounts across all stores. Do not use this to retrieve a single discount — use commercetools_get_cart_discount_by_id instead. This tool does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_list_cart_discounts_in_store(
        self,
        storeKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all cart discounts available within a specific store in CommerceTools. Use this when you need to review or audit cart discounts scoped to a particular store. Do not use this to retrieve a single cart discount — use commercetools_get_cart_discount_in_store_by_id instead. This tool does not modify any data.

        Args:
            storeKey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_list_categories(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all product categories in the CommerceTools project. Use this when you need to enumerate or audit the category hierarchy. Do not use this to retrieve a single category — use commercetools_get_category_by_id or commercetools_get_category_by_key instead. This tool does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_list_customers(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all customers in the CommerceTools project. Use this when you need to enumerate or audit all customer accounts globally. Do not use this to retrieve a single customer — use commercetools_get_customer_by_id or commercetools_get_customer_by_key instead. This tool does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_list_customers_in_store(
        self,
        storeKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all customers associated with a specific store in CommerceTools. Use this when you need to enumerate or audit customers scoped to a particular store. Do not use this to retrieve a single customer — use commercetools_get_customer_in_store_by_id or commercetools_get_customer_in_store_by_key instead. This tool does not modify any data.

        Args:
            storeKey: The unique identifier for the store.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_list_inventory(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all inventory entries in the CommerceTools project. Use this when you need to review or audit stock levels across all product variants and supply channels. Do not use this to retrieve a single inventory entry — use commercetools_get_inventory_by_id or commercetools_get_inventory_by_key instead. This tool does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_list_product_discounts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all product discounts in the CommerceTools project. Use this when you need to review or audit all active and inactive product discounts. Do not use this to retrieve a single discount — use commercetools_get_product_discount_by_id or commercetools_get_product_discount_by_key instead. This tool does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_list_products(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all products in the CommerceTools project. Use this when you need to enumerate or audit products in the catalog. Do not use this to retrieve a single product — use commercetools_get_product_by_id or commercetools_get_product_by_sku instead. This tool does not modify any data.

        Args:
            limit: The limit for pagination.
            offset: The offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_list_standalone_prices(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all standalone prices available in the CommerceTools project. Use this when you need to review or audit standalone pricing configurations. Do not use this to retrieve a single standalone price — use commercetools_get_standalone_price_by_id or commercetools_get_standalone_price_by_key instead. This tool does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_list_stores(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all stores available in the CommerceTools project. Use this when you need to enumerate or audit all store configurations. Do not use this to retrieve a single store. This tool does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_reset_customer_password(
        self,
        newPassword: str,
        tokenValue: str,
    ) -> Dict[str, Any]:
        """Resets the password for a specific CommerceTools customer using a valid password reset token. Use this after a reset token has been generated via commercetools_create_customer_password_reset_token. Do not use this to change a known password — use commercetools_change_customer_password instead. This action modifies the customers credentials permanently.

        Args:
            newPassword: New password for the CommerceTools API. (required)
            tokenValue: Token value for the CommerceTools API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_update_attribute_group_by_id(
        self,
        actions: List[Any],
        authToken: str,
        id: str,
        region: str,
        storeName: str,
        version: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Updates an existing attribute group in CommerceTools using its unique ID. Use this to modify how product attributes are grouped and displayed in the Merchant Center when you have the group ID. Do not use this to create a new attribute group — use commercetools_create_attribute_group instead. This action permanently modifies the attribute group record.

        Args:
            actions:  (required)
            authToken: The authentication token for accessing CommerceTools. (required)
            id: The unique identifier for the request. (required)
            region: The region of the CommerceTools store. (required)
            storeName: The name of the CommerceTools store. (required)
            version: The version number.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_update_attribute_group_by_key(
        self,
        actions: List[Any],
        authToken: str,
        region: str,
        storeName: str,
        key: Optional[str] = None,
        version: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates an existing attribute group in CommerceTools using its unique key. Use this to modify how product attributes are grouped and displayed in the Merchant Center. Do not use this to create a new attribute group — use commercetools_create_attribute_group instead. This action permanently modifies the attribute group record.

        Args:
            actions:  (required)
            authToken: The authentication token for the CommerceTools API. (required)
            region: The region of the CommerceTools store. (required)
            storeName: The name of the CommerceTools store. (required)
            key: Unique identifier for the request.
            version: Version number for optimistic concurrency.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_update_category_by_id(
        self,
        categoryId: str,
        actions: Optional[List[Any]] = None,
        version: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates an existing categorys information in CommerceTools using its unique ID. Use this to modify category attributes such as name, slug, description, or parent when you have the category ID. Do not use this to create a new category — use commercetools_create_category instead. This action permanently modifies the category record.

        Args:
            categoryId:  (required)
            actions: 
            version: 
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_update_category_by_key(
        self,
        actions: List[Any],
        version: int,
        categoryKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing categorys information in CommerceTools using its unique key. Use this to modify category attributes such as name, slug, description, or parent. Do not use this to create a new category — use commercetools_create_category instead. This action permanently modifies the category record.

        Args:
            actions:  (required)
            version: Version number for optimistic concurrency control. (required)
            categoryKey: Key identifier for the category in CommerceTools.
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_update_inventory_by_id(
        self,
        actions: List[Any],
        inventoryId: str,
        version: int,
    ) -> Dict[str, Any]:
        """Updates an existing inventory entry in CommerceTools by its unique ID. Use this to modify inventory attributes such as the key, quantity on stock, or restock levels. Do not use this to create a new inventory entry — use commercetools_create_inventory instead. This action permanently modifies the inventory record.

        Args:
            actions:  (required)
            inventoryId:  (required)
            version: Version number. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_update_product_type_by_id(
        self,
        actions: List[Any],
        productId: str,
        version: float,
    ) -> Dict[str, Any]:
        """Updates an existing product type in CommerceTools using its unique ID. Use this to modify the product types attribute definitions or metadata when you have the product type ID. Do not use this to create a new product type — use commercetools_create_product_type instead. This action permanently modifies the product type record.

        Args:
            actions:  (required)
            productId: The ID of the product. (required)
            version: The version number. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def commercetools_update_product_type_by_key(
        self,
        actions: List[Any],
        authToken: str,
        region: str,
        storeName: str,
        key: Optional[str] = None,
        version: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Updates an existing product type in CommerceTools using its unique key. Use this to modify the product types attributes or metadata when you have the product type key. Note: this tool calls a GET endpoint — verify the intended behavior before use, as an update operation is expected to use POST. Do not use this to create a new product type — use commercetools_create_product_type instead.

        Args:
            actions:  (required)
            authToken: Authentication token for the CommerceTools API. (required)
            region: Region of the CommerceTools store. (required)
            storeName: Name of the store in CommerceTools. (required)
            key: Key identifier for the request.
            version: Version number for the request.
        Returns:
            API response as a dictionary.
        """
        ...

