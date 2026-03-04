"""Fastn Bigcommerce connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _BigcommerceAddProductOptionValuesValueData(TypedDict, total=False):
    colors: List[Any]

class _BigcommerceCreateBrandCustomUrl(TypedDict, total=False):
    is_customized: bool
    url: str

class _BigcommerceCreateProductCustomUrl(TypedDict, total=False):
    is_customized: bool
    url: str

class _BigcommerceUpdateBrandCustomUrl(TypedDict, total=False):
    is_customized: bool
    url: str

class _BigcommerceUpdateCartLineItemLineItem(TypedDict, total=False):
    gift_wrapping: Dict[str, Any]
    list_price: int
    name: str
    product_id: int
    quantity: int
    variant_id: int

class _BigcommerceUpdateCategoryCustomUrl(TypedDict, total=False):
    is_customized: bool
    url: str

class _BigcommerceUpdateChannelConfigMeta(TypedDict, total=False):
    app: Dict[str, Any]

class _BigcommerceUpdateCustomerGroupCategoryAccess(TypedDict, total=False):
    categories: List[Any]
    type: str

class _BigcommerceUpdateProductData(TypedDict, total=False):
    availability: str
    availability_description: str
    base_variant_id: int
    bin_picking_number: str
    brand_id: int
    calculated_price: int
    categories: List[Any]
    condition: str
    cost_price: int
    custom_url: Dict[str, Any]
    date_created: str
    date_modified: str
    depth: int
    description: str
    fixed_cost_shipping_price: int
    gift_wrapping_options_list: List[Any]
    gift_wrapping_options_type: str
    gtin: str
    height: int
    id: int
    inventory_level: int
    inventory_tracking: str
    inventory_warning_level: int
    is_condition_shown: bool
    is_featured: bool
    is_free_shipping: bool
    is_preorder_only: bool
    is_price_hidden: bool
    is_visible: bool
    layout_file: str
    map_price: int
    meta_description: str
    meta_keywords: List[Any]
    mpn: str
    name: str
    open_graph_description: str
    open_graph_title: str
    open_graph_type: str
    open_graph_use_image: bool
    open_graph_use_meta_description: bool
    open_graph_use_product_name: bool
    option_set_display: str
    option_set_id: str
    order_quantity_maximum: int
    order_quantity_minimum: int
    page_title: str
    preorder_message: str
    preorder_release_date: str
    price: int
    price_hidden_label: str
    product_tax_code: str
    related_products: List[Any]
    retail_price: int
    reviews_count: int
    reviews_rating_sum: int
    sale_price: int
    search_keywords: str
    sku: str
    sort_order: int
    tax_class_id: int
    total_sold: int
    type: str
    upc: str
    view_count: int
    warranty: str
    weight: int
    width: int

class BigcommerceConnector:
    """Bigcommerce connector ().

    Provides 95 tools.
    """

    def bigcommerce_add_product_image_by_file(
        self,
        image_file: str,
        productId: str,
        description: Optional[str] = None,
        is_thumbnail: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads and adds an image to a specific product in BigCommerce via a file upload, identified by product ID. Use this when you have a local image file to attach to a product. Do not use this to add an image via URL (use bigcommerce_add_product_image_by_url) or to add an image to a variant (use bigcommerce_add_variant_image).

        Args:
            image_file: The image file to upload. (required)
            productId: The BigCommerce product identifier. (required)
            description: Description for the product image.
            is_thumbnail: Flag to indicate whether the image should be set as the product's thumbnail.
            sort_order: The display order of the image.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_add_product_image_by_url(
        self,
        description: Optional[str] = None,
        image_url: Optional[str] = None,
        is_thumbnail: Optional[bool] = None,
        productId: Optional[str] = None,
        sort_order: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Adds an image to a specific product in BigCommerce by providing a publicly accessible URL, identified by product ID. Use this when the image is hosted remotely and accessible via URL. Do not use this to upload an image from a local file (use bigcommerce_add_product_image_by_file) or to add an image to a variant (use bigcommerce_add_variant_image).

        Args:
            description: 
            image_url: 
            is_thumbnail: 
            productId: 
            sort_order: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_add_product_option_values(
        self,
        label: Optional[str] = None,
        optionId: Optional[str] = None,
        productId: Optional[str] = None,
        sort_order: Optional[int] = None,
        value_data: Optional[_BigcommerceAddProductOptionValuesValueData] = None,
    ) -> Dict[str, Any]:
        """Adds one or more new values to an existing product option in BigCommerce, identified by product ID and option ID. Use this when you need to extend an option with additional choices (e.g. adding a new color or size). Do not use this to create the option itself (use bigcommerce_create_product_options) or to update an existing option value.

        Args:
            label: 
            optionId: 
            productId: 
            sort_order: 
            value_data: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_add_variant_image(
        self,
        image_url: Optional[str] = None,
        productId: Optional[str] = None,
        variantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads and attaches an image to a specific product variant in BigCommerce, identified by product ID and variant ID. Use this when you need to associate a visual representation with a variant. Do not use this to add an image to the parent product (use bigcommerce_add_product_image_by_url or bigcommerce_add_product_image_by_file).

        Args:
            image_url: 
            productId: 
            variantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_add_variant_meta_fields(
        self,
        description: Optional[str] = None,
        key: Optional[str] = None,
        namespace: Optional[str] = None,
        permission_set: Optional[str] = None,
        productId: Optional[str] = None,
        value: Optional[str] = None,
        variantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates and adds new metafields to a specific product variant in BigCommerce, identified by product ID and variant ID. Use this to attach custom key-value metadata to a variant. Do not use this to update an existing variant metafield (use bigcommerce_update_variant_meta_fields) or to create variant metafields in batch (use bigcommerce_batch_create_variants_metafields).

        Args:
            description: 
            key: 
            namespace: 
            permission_set: 
            productId: 
            value: 
            variantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_assign_product_to_channel(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Assigns one or more products to a sales channel in BigCommerce, making them available for sale on that channel. Use this when you need to publish or expose products to a specific storefront or channel. This is a PUT operation and will overwrite existing channel assignments for the specified products. Do not use this to remove a product from a channel (use bigcommerce_unassign_product_from_channel).

        Args:
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_batch_create_metafields(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates multiple product-level metafields in a single batch operation in the BigCommerce catalog. Use this when you need to add custom metadata to several products at once for efficiency. Do not use this to create metafields for a single product (use bigcommerce_create_product_meta_fields) or to create variant metafields in batch (use bigcommerce_batch_create_variants_metafields).

        Args:
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_batch_create_variants_metafields(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates multiple variant metafields in a single batch operation across the BigCommerce catalog. Use this when you need to add custom metadata to several variants at once. Do not use this to create metafields for a single variant (use bigcommerce_add_variant_meta_fields) or to create product-level metafields in batch (use bigcommerce_batch_create_metafields).

        Args:
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_batch_delete_variant_metafields(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes multiple variant metafields in a single batch operation across the BigCommerce catalog. Use this when you need to remove several variant metafields at once for efficiency. This action is irreversible — all specified metafields will be deleted. Do not use this to delete a single variant metafield (use bigcommerce_delete_variant_meta_field) or to delete product-level metafields (use bigcommerce_delete_batch_meta_fields).

        Args:
            body: Array of integer IDs or values relevant to the Bigcommerce endpoint operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_brand(
        self,
        name: str,
        custom_url: Optional[_BigcommerceCreateBrandCustomUrl] = None,
        image_url: Optional[str] = None,
        meta_description: Optional[str] = None,
        meta_keywords: Optional[List[Any]] = None,
        page_title: Optional[str] = None,
        search_keywords: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new brand in the BigCommerce catalog. Use this when you need to add a brand that products can be associated with. Do not use this to update an existing brand (use bigcommerce_update_brand) or to upload a brand image (use bigcommerce_create_brand_image).

        Args:
            name: Name of the product or resource. (required)
            custom_url: Custom URL settings for the resource.
            image_url: URL of the main image.
            meta_description: Meta description for the product or resource.
            meta_keywords: Array of meta keywords for SEO.
            page_title: Title of the page or resource.
            search_keywords: Keywords for internal search functionality.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_brand_image(
        self,
        brandId: str,
        image: str,
    ) -> Dict[str, Any]:
        """Uploads and attaches an image to a specific brand in the BigCommerce catalog, identified by its brand ID. Use this when you need to associate a logo or visual asset with a brand. Do not use this to add images to products (use bigcommerce_add_product_image_by_url or bigcommerce_add_product_image_by_file) or to update brand details (use bigcommerce_update_brand).

        Args:
            brandId: The ID of the brand for which the request is targeted. (required)
            image: The image data or URL to be used by the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_categories(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Creates multiple new categories within BigCommerce category trees in a single batch operation. Use this when you need to add several categories at once. Do not use this to create a single standalone category (use bigcommerce_create_category) or to create categories in a specific tree context (use bigcommerce_create_category_in_tree).

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_category(
        self,
        name: str,
        parent_id: int,
    ) -> Dict[str, Any]:
        """Creates a new standalone category in the BigCommerce catalog. Use this when you need to add a category outside of a tree hierarchy, or as a top-level category. Do not use this to create categories within a tree structure (use bigcommerce_create_category_in_tree) or to create multiple categories at once (use bigcommerce_create_categories).

        Args:
            name: The name of the resource being created or updated. (required)
            parent_id: The identifier of the parent resource under which the new item will be created. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_category_in_tree(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates one or more new categories within a category tree in the BigCommerce catalog. Use this when you need to add categories in the context of a hierarchical tree structure. Do not use this to create a standalone category (use bigcommerce_create_category) or to update an existing category in a tree (use bigcommerce_update_category_in_tree).

        Args:
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_channel(
        self,
        name: str,
        platform: str,
        status: str,
        type: str,
    ) -> Dict[str, Any]:
        """Creates a new sales channel in BigCommerce (e.g. a storefront, POS, or marketplace). Use this when you need to establish a new channel for selling products. Note: a second tool with the same action name exists (ActionID _knexa_2bdE4nRzxd3L2rFroa60UxgIYUT) — verify which is intended. Do not use this to update an existing channel (use bigcommerce_update_channel).

        Args:
            name: The resource name. (required)
            platform: The target platform; for this schema, BigCommerce. (required)
            status: The desired status of the resource. (required)
            type: The type category of the resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_customer(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new customer account in the BigCommerce store. Use this when you need to register a new customer with their details such as name, email, and password. Do not use this to update an existing customer (use bigcommerce_update_customer) or to manage customer attribute values (use bigcommerce_upsert_customer_attribute_values).

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_customer_attribute(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new customer attribute definition in BigCommerce. Use this when you need to define a new custom data field that can be assigned values across customers. Do not use this to assign values to the attribute (use bigcommerce_upsert_customer_attribute_values) or to update an existing attribute (use bigcommerce_update_customer_attribute).

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_product(
        self,
        name: str,
        price: float,
        type: str,
        weight: int,
        availability: Optional[str] = None,
        availability_description: Optional[str] = None,
        base_variant_id: Optional[int] = None,
        bin_picking_number: Optional[str] = None,
        brand_id: Optional[int] = None,
        bulk_pricing_rules: Optional[List[Any]] = None,
        calculated_price: Optional[float] = None,
        categories: Optional[List[Any]] = None,
        condition: Optional[str] = None,
        cost_price: Optional[int] = None,
        custom_fields: Optional[List[Any]] = None,
        custom_url: Optional[_BigcommerceCreateProductCustomUrl] = None,
        date_created: Optional[str] = None,
        date_modified: Optional[str] = None,
        depth: Optional[int] = None,
        description: Optional[str] = None,
        fixed_cost_shipping_price: Optional[int] = None,
        gift_wrapping_options_list: Optional[List[Any]] = None,
        gift_wrapping_options_type: Optional[str] = None,
        gtin: Optional[str] = None,
        height: Optional[int] = None,
        images: Optional[List[Any]] = None,
        inventory_level: Optional[int] = None,
        inventory_tracking: Optional[str] = None,
        inventory_warning_level: Optional[int] = None,
        is_condition_shown: Optional[bool] = None,
        is_featured: Optional[bool] = None,
        is_free_shipping: Optional[bool] = None,
        is_preorder_only: Optional[bool] = None,
        is_price_hidden: Optional[bool] = None,
        is_visible: Optional[bool] = None,
        layout_file: Optional[str] = None,
        map_price: Optional[int] = None,
        meta_description: Optional[str] = None,
        meta_keywords: Optional[List[Any]] = None,
        modifiers: Optional[List[Any]] = None,
        mpn: Optional[str] = None,
        open_graph_description: Optional[str] = None,
        open_graph_title: Optional[str] = None,
        open_graph_type: Optional[str] = None,
        open_graph_use_image: Optional[bool] = None,
        open_graph_use_meta_description: Optional[bool] = None,
        open_graph_use_product_name: Optional[bool] = None,
        option_set_display: Optional[str] = None,
        option_set_id: Optional[str] = None,
        options: Optional[List[Any]] = None,
        order_quantity_maximum: Optional[int] = None,
        order_quantity_minimum: Optional[int] = None,
        page_title: Optional[str] = None,
        parent_relations: Optional[List[Any]] = None,
        preorder_message: Optional[str] = None,
        preorder_release_date: Optional[str] = None,
        price_hidden_label: Optional[str] = None,
        primary_image: Optional[str] = None,
        product_tax_code: Optional[str] = None,
        related_products: Optional[List[Any]] = None,
        retail_price: Optional[int] = None,
        reviews: Optional[List[Any]] = None,
        reviews_count: Optional[int] = None,
        reviews_rating_sum: Optional[int] = None,
        sale_price: Optional[int] = None,
        search_keywords: Optional[str] = None,
        sku: Optional[str] = None,
        sort_order: Optional[int] = None,
        tax_class_id: Optional[int] = None,
        total_sold: Optional[int] = None,
        upc: Optional[str] = None,
        variants: Optional[List[Any]] = None,
        videos: Optional[List[Any]] = None,
        view_count: Optional[int] = None,
        warranty: Optional[str] = None,
        width: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the BigCommerce catalog. Use this when you need to add a new product with its core details such as name, price, type, and description. Do not use this to create product variants (use bigcommerce_create_variant), add images (use bigcommerce_add_product_image_by_url), or update an existing product (use bigcommerce_update_product).

        Args:
            name: Name of the product. (required)
            price: Price of the product. (required)
            type: Type of the product. (required)
            weight: Weight of the product. (required)
            availability: Availability of the product.
            availability_description: Description of the product availability.
            base_variant_id: ID of the base variant.
            bin_picking_number: Bin picking number for the product.
            brand_id: ID of the brand.
            bulk_pricing_rules: List of bulk pricing rules for the product.
            calculated_price: Calculated price of the product.
            categories: List of product categories.
            condition: Condition of the product.
            cost_price: Cost price of the product.
            custom_fields: List of custom fields for the product.
            custom_url: Custom URL details for the product.
            date_created: Date the product was created.
            date_modified: Date the product was modified.
            depth: Depth of the product.
            description: Description of the product.
            fixed_cost_shipping_price: Fixed cost shipping price for the product.
            gift_wrapping_options_list: List of gift wrapping options.
            gift_wrapping_options_type: Type of gift wrapping options.
            gtin: GTIN of the product.
            height: Height of the product.
            images: List of product images.
            inventory_level: Inventory level of the product.
            inventory_tracking: Inventory tracking method.
            inventory_warning_level: Inventory warning level for the product.
            is_condition_shown: Indicates whether the condition is shown.
            is_featured: Indicates whether the product is featured.
            is_free_shipping: Indicates whether shipping is free for the product.
            is_preorder_only: Indicates whether the product is preorder only.
            is_price_hidden: Indicates whether the price is hidden.
            is_visible: Indicates whether the product is visible.
            layout_file: Layout file for the product.
            map_price: MAP price of the product.
            meta_description: Meta description for the product.
            meta_keywords: List of meta keywords for the product.
            modifiers: List of modifiers for the product.
            mpn: MPN of the product.
            open_graph_description: Open Graph description for the product.
            open_graph_title: Open Graph title for the product.
            open_graph_type: Open Graph type for the product.
            open_graph_use_image: Indicates whether to use image for Open Graph.
            open_graph_use_meta_description: Indicates whether to use meta description for Open Graph.
            open_graph_use_product_name: Indicates whether to use product name for Open Graph.
            option_set_display: Display of the option set.
            option_set_id: ID of the option set.
            options: List of product options.
            order_quantity_maximum: Maximum order quantity.
            order_quantity_minimum: Minimum order quantity.
            page_title: Title of the product page.
            parent_relations: List of parent relations.
            preorder_message: Preorder message for the product.
            preorder_release_date: Preorder release date.
            price_hidden_label: Label for hidden price.
            primary_image: URL of the primary image.
            product_tax_code: Product tax code.
            related_products: List of related product IDs.
            retail_price: Retail price of the product.
            reviews: List of product reviews.
            reviews_count: Number of reviews.
            reviews_rating_sum: Sum of reviews ratings.
            sale_price: Sale price of the product.
            search_keywords: Search keywords for the product.
            sku: SKU of the product.
            sort_order: Sort order for the product.
            tax_class_id: ID of the tax class.
            total_sold: Total number of products sold.
            upc: UPC of the product.
            variants: 
            videos: List of product videos.
            view_count: Number of times the product was viewed.
            warranty: Warranty information for the product.
            width: Width of the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_product_custom_fields(
        self,
        name: str,
        product_id: str,
        value: str,
    ) -> Dict[str, Any]:
        """Creates one or more new custom fields for a specific product in BigCommerce, identified by product ID. Use this to attach additional custom data to a product beyond its standard fields. Do not use this to update existing custom fields (use bigcommerce_update_product_custom_field) or to create metafields (use bigcommerce_create_product_meta_fields).

        Args:
            name: The name of the item. (required)
            product_id: The ID of the product. (required)
            value: The value of the item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_product_meta_fields(
        self,
        key: str,
        namespace: str,
        productId: str,
        value: str,
        description: Optional[str] = None,
        permission_set: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates new metafields for a specific product in BigCommerce, identified by product ID. Use this to attach custom key-value metadata to a product. Do not use this to create metafields in bulk (use bigcommerce_batch_create_metafields) or to create metafields for a variant (use bigcommerce_add_variant_meta_fields).

        Args:
            key: The key for the configuration setting. (required)
            namespace: The namespace for the configuration entry. (required)
            productId: The product identifier used in the API call URL. (required)
            value: The value for the configuration entry. (required)
            description: Description of the configuration entry.
            permission_set: Permissions associated with this configuration.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_product_options(
        self,
        display_name: Optional[str] = None,
        name: Optional[str] = None,
        option_values: Optional[List[Any]] = None,
        productId: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates one or more new configurable options (e.g. size, color) for a specific product in BigCommerce, identified by product ID. Use this when setting up new option types for a product. Do not use this to add values to an existing option (use bigcommerce_add_product_option_values) or to create variants (use bigcommerce_create_variant).

        Args:
            display_name: 
            name: 
            option_values: 
            productId: 
            type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_shipment(
        self,
        orderId: str,
        comments: Optional[str] = None,
        items: Optional[List[Any]] = None,
        order_address_id: Optional[int] = None,
        tracking_number: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new shipment record for a specific order in BigCommerce, identified by order ID. Use this when fulfilling an order and you need to record that items have been shipped, including tracking number and shipping method. Do not use this to list existing shipments for an order (use bigcommerce_list_order_shipments) or to retrieve order details (use bigcommerce_get_order).

        Args:
            orderId: The ID of the order to update. (required)
            comments: Any comments related to the order update.
            items: 
            order_address_id: The ID of the order address.
            tracking_number: The tracking number for the shipment.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_variant(
        self,
        productId: str,
        inventory_level: Optional[int] = None,
        option_values: Optional[List[Any]] = None,
        price: Optional[float] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new variant for an existing product in BigCommerce, identified by product ID. Use this when you need to add a new SKU combination (e.g. a new size/color pair) to a product. Do not use this to update an existing variant (use bigcommerce_update_variant) or to create the parent product (use bigcommerce_create_product).

        Args:
            productId: The ID of the product to retrieve or update. (required)
            inventory_level: Current inventory level for the product.
            option_values: 
            price: Price of the product.
            sku: Stock Keeping Unit for the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_create_webhook(
        self,
        destination: str,
        is_active: bool,
        scope: str,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the BigCommerce store to receive real-time event notifications at a specified endpoint URL. Use this when you need to subscribe to store events such as order creation or product updates. Do not use this to retrieve existing webhooks (use bigcommerce_list_webhooks) or to delete a webhook (use bigcommerce_delete_webhook).

        Args:
            destination: Destination or target of the Bigcommerce API request. (required)
            is_active: Indicates whether the item is active in Bigcommerce. (required)
            scope: Scope or context of the Bigcommerce API request. (required)
            headers: Optional headers for the Bigcommerce API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_batch_meta_fields(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes multiple product-level metafields in a single batch operation in the BigCommerce catalog. Use this when you need to remove several product metafields at once for efficiency. This action is irreversible. Do not use this to delete a single product metafield or to delete variant metafields in batch (use bigcommerce_batch_delete_variant_metafields).

        Args:
            body: Array payload containing integers for the request to the BigCommerce API.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_categories(
        self,
    ) -> Dict[str, Any]:
        """Permanently deletes one or more categories from BigCommerce category trees. This action is irreversible. Use this when you need to remove categories from the tree structure. Do not use this to delete an entire category tree (use bigcommerce_delete_category_tree) or to update categories (use bigcommerce_update_categories).
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_category_tree(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Permanently deletes a category tree from BigCommerce. This action is irreversible — the tree and its associated structure will be removed. Use this when you need to remove an entire category tree. Do not use this to delete individual categories within a tree (use bigcommerce_delete_categories) or to update a tree (use bigcommerce_upsert_category_tree).

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_customer_attribute(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a customer attribute definition from the BigCommerce store. This action is irreversible and will also remove associated attribute values. Do not use this to delete specific attribute values only (use bigcommerce_delete_customer_attribute_values) or to update an attribute (use bigcommerce_update_customer_attribute).

        Args:
            id: ID parameter for the BigCommerce2 API endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_customer_attribute_values(
        self,
        idin: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes specific customer attribute values in BigCommerce. Use this when you need to remove custom attribute data from customers. This action is irreversible. Do not use this to delete the attribute definition itself (use bigcommerce_delete_customer_attribute) or to update attribute values (use bigcommerce_upsert_customer_attribute_values).

        Args:
            idin: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_option_value(
        self,
        productId: str,
        optionId: Optional[str] = None,
        valueId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific option value from a product option in the BigCommerce catalog. Requires the product ID, option ID, and value ID. This action is irreversible — the option value will be removed from the option and any variants using it may be affected. Do not use this to delete the entire option (use bigcommerce_delete_variant_option) or to delete a variant (use bigcommerce_delete_variant).

        Args:
            productId: The identifier of the product relevant to the request. (required)
            optionId: Identifier of an option associated with the product, if applicable.
            valueId: Identifier for a specific value relevant to the request (for example, an option value ID).
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific product from the BigCommerce catalog by its numeric product ID. This action is irreversible — the product, its variants, images, metafields, and associated data will be removed. Use this only when you intend to fully remove a product. Do not use this to simply unpublish or hide a product (use bigcommerce_update_product instead).

        Args:
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_product_custom_field(
        self,
        customFieldId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific custom field from a product in BigCommerce, identified by product ID and custom field ID. This action is irreversible. Do not use this to delete metafields (use bigcommerce_delete_batch_meta_fields) or to update a custom field (use bigcommerce_update_product_custom_field).

        Args:
            customFieldId: The ID of the custom field. (required)
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_product_image(
        self,
        imageId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific image from a product in BigCommerce, identified by product ID and image ID. This action is irreversible — the image will be removed from the product. Do not use this to delete a brand image or to update an image (use bigcommerce_update_product to modify product details).

        Args:
            imageId: The image identifier associated with the product. (required)
            productId: The product identifier related to the image. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_variant(
        self,
        productId: str,
        variantId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific variant from a product in the BigCommerce catalog, identified by product ID and variant ID. This action is irreversible — the variant and its associated data will be removed. Do not use this to delete an entire product (use bigcommerce_delete_product) or to delete a variant option (use bigcommerce_delete_variant_option).

        Args:
            productId: The identifier of the product in Bigcommerce to target with this request. (required)
            variantId: The identifier of the specific product variant in Bigcommerce (if applicable). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_variant_meta_field(
        self,
        metaFieldId: str,
        productId: str,
        variantId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific metafield from a product variant in BigCommerce, identified by product ID, variant ID, and metafield ID. This action is irreversible. Do not use this to delete multiple variant metafields at once (use bigcommerce_batch_delete_variant_metafields) or to delete a product-level metafield.

        Args:
            metaFieldId: The identifier of the metafield to operate on. (required)
            productId: The identifier of the product associated with the request. (required)
            variantId: The identifier of the product variant associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_variant_option(
        self,
        optionId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific product option (and its associated values) from a product in BigCommerce, identified by product ID and option ID. This action is irreversible — the option and all its values will be removed. Do not use this to delete only a specific option value (use bigcommerce_delete_option_value) or to delete a variant (use bigcommerce_delete_variant).

        Args:
            optionId: The ID of the option for the product. (required)
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_delete_webhook(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific webhook from the BigCommerce store, identified by its webhook ID. This action is irreversible — the webhook will stop receiving events immediately. Do not use this to list webhooks (use bigcommerce_list_webhooks) or to update a webhook.

        Args:
            id: The ID of the URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_get_a_category_tree(
        self,
        categoryTreeId: str,
    ) -> Dict[str, Any]:
        """Retrieves all categories within a specific category tree in BigCommerce, identified by its category tree ID. Use this when you need the full hierarchical structure of a particular tree. Do not use this to retrieve all categories across all trees (use bigcommerce_list_all_categories) or to list all category trees (use bigcommerce_list_category_trees).

        Args:
            categoryTreeId: The ID of the category tree. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_get_brand(
        self,
        brandId: str,
        exclude_fields: Optional[List[Any]] = None,
        include_fields: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific brand in the BigCommerce catalog, identified by its brand ID. Use this when you need the full details of one brand. Do not use this to list all brands (use bigcommerce_list_brands) or to create or update a brand.

        Args:
            brandId: The Brand ID for the Bigcommerce store. (required)
            exclude_fields: List of field names to exclude from the API response.
            include_fields: List of field names to explicitly include in the API response.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_get_cart(
        self,
        cartId: str,
        include: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the current state of a specific shopping cart in BigCommerce, identified by cart ID. Returns cart contents including line items, totals, and applied coupons. Use this to inspect cart details. Do not use this to update a cart line item (use bigcommerce_update_cart_line_item) or to retrieve order information (use bigcommerce_get_order).

        Args:
            cartId: The ID of the shopping cart. (required)
            include: Specifies additional data to include in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_get_category(
        self,
        categoryId: str,
        exclude_fields: Optional[List[Any]] = None,
        include_fields: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single category from the BigCommerce catalog, identified by its category ID. Use this when you need specific information about one category. Do not use this to list all categories (use bigcommerce_list_all_categories or bigcommerce_list_categories) or to retrieve a category tree (use bigcommerce_list_category_trees).

        Args:
            categoryId: The ID of the category to retrieve. (required)
            exclude_fields: Fields to exclude from the response.
            include_fields: Fields to include in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_get_channel(
        self,
        channelId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific sales channel in BigCommerce, identified by its channel ID. Use this to inspect a channels configuration, status, and type. Do not use this to list all channels (use bigcommerce_list_channels) or to update a channel (use bigcommerce_update_channel).

        Args:
            channelId: The channel ID for the Bigcommerce API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_get_channel_active_theme(
        self,
        channelId: str,
    ) -> Dict[str, Any]:
        """Retrieves the currently active storefront theme for a specific sales channel in BigCommerce, identified by channel ID. Use this to determine which theme is live on a channel. Do not use this to retrieve channel metadata (use bigcommerce_get_channel) or to update channel settings (use bigcommerce_update_channel).

        Args:
            channelId: The channel ID for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_get_order(
        self,
        orderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific order in BigCommerce, identified by its order ID. Returns order metadata including status, totals, billing details, and dates. Do not use this to retrieve the line items of the order (use bigcommerce_list_order_products), shipments (use bigcommerce_list_order_shipments), or a list of orders (use bigcommerce_list_orders).

        Args:
            orderId: The order ID.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details of a single product from the BigCommerce catalog by its numeric product ID. Use this when you know the product ID and need its complete data including pricing, inventory levels, images, and variants. Do not use this to search by SKU (use bigcommerce_get_product_by_sku) or to retrieve a list of products (use bigcommerce_list_products).

        Args:
            productId: The ID of the product being accessed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_get_product_by_sku(
        self,
        sku: str,
    ) -> Dict[str, Any]:
        """Retrieves a single product from the BigCommerce catalog by its SKU (Stock Keeping Unit). Use this when you need to look up a specific product using its SKU identifier rather than its numeric product ID. Returns full product details including pricing, inventory, and attributes. Do not use this to retrieve a product by its numeric product ID (use bigcommerce_get_product instead) or to list multiple products (use bigcommerce_list_products instead).

        Args:
            sku: The Stock Keeping Unit (SKU) identifier. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_get_product_custom_field(
        self,
        customFieldId: str,
        productId: str,
        exclude_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific custom field on a product in BigCommerce, identified by product ID and custom field ID. Use this when you need the data for one specific custom field. Do not use this to list all custom fields on a product (use bigcommerce_list_product_custom_fields) or to update a custom field (use bigcommerce_update_product_custom_field).

        Args:
            customFieldId: ID of the custom field. (required)
            productId: ID of the product. (required)
            exclude_fields: Comma-separated list of fields to exclude from the response.
            include_fields: Comma-separated list of fields to include in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_get_webhook(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific webhook configured in BigCommerce, identified by its webhook ID. Use this to inspect a webhooks endpoint URL, scope, and status. Do not use this to list all webhooks (use bigcommerce_list_webhooks) or to create a new webhook (use bigcommerce_create_webhook).

        Args:
            id: The ID of the URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_all_categories(
        self,
        category_idin: Optional[str] = None,
        category_idnot_in: Optional[str] = None,
        category_uuidin: Optional[str] = None,
        category_uuidnot_in: Optional[str] = None,
        exclude_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
        is_visible: Optional[str] = None,
        keyword: Optional[str] = None,
        limit: Optional[str] = None,
        name: Optional[str] = None,
        namelike: Optional[str] = None,
        page: Optional[str] = None,
        page_title: Optional[str] = None,
        page_titlelike: Optional[str] = None,
        parent_idin: Optional[str] = None,
        parent_idnot_in: Optional[str] = None,
        tree_idin: Optional[str] = None,
        tree_idnot_in: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a flat list of all categories across all category trees in the BigCommerce catalog. Use this when you need a complete enumeration of every category regardless of tree structure. Do not use this to retrieve a single category (use bigcommerce_get_category) or to retrieve categories scoped to a specific tree (use bigcommerce_list_categories or bigcommerce_get_a_category_tree).

        Args:
            category_idin: 
            category_idnot_in: 
            category_uuidin: 
            category_uuidnot_in: 
            exclude_fields: 
            include_fields: 
            is_visible: 
            keyword: 
            limit: 
            name: 
            namelike: 
            page: 
            page_title: 
            page_titlelike: 
            parent_idin: 
            parent_idnot_in: 
            tree_idin: 
            tree_idnot_in: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_all_customer_attribute_values(
        self,
        attribute_idin: Optional[str] = None,
        customer_idin: Optional[str] = None,
        date_created: Optional[str] = None,
        date_createdmax: Optional[str] = None,
        date_createdmin: Optional[str] = None,
        date_modified: Optional[str] = None,
        date_modifiedmax: Optional[str] = None,
        date_modifiedmin: Optional[str] = None,
        limit: Optional[str] = None,
        name: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all customer attribute values stored in BigCommerce. Use this when you need to enumerate the custom data values assigned to customers across all attributes. Do not use this to retrieve the attribute definitions themselves (use bigcommerce_list_all_customer_attributes) or to update values (use bigcommerce_upsert_customer_attribute_values).

        Args:
            attribute_idin: 
            customer_idin: 
            date_created: 
            date_createdmax: 
            date_createdmin: 
            date_modified: 
            date_modifiedmax: 
            date_modifiedmin: 
            limit: 
            name: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_all_customer_attributes(
        self,
        date_created: Optional[str] = None,
        date_createdmax: Optional[str] = None,
        date_createdmin: Optional[str] = None,
        date_modifiedmax: Optional[str] = None,
        date_modifiedmin: Optional[str] = None,
        limit: Optional[str] = None,
        name: Optional[str] = None,
        namelike: Optional[str] = None,
        page: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all customer attribute definitions available in the BigCommerce store. Use this to discover what custom attributes can be assigned to customers. Do not use this to retrieve the values assigned to customers (use bigcommerce_list_all_customer_attribute_values) or to create a new attribute (use bigcommerce_create_customer_attribute).

        Args:
            date_created: Filter by creation date.
            date_createdmax: Filter by maximum creation date.
            date_createdmin: Filter by minimum creation date.
            date_modifiedmax: Filter by maximum modification date.
            date_modifiedmin: Filter by minimum modification date.
            limit: The maximum number of results to return.
            name: Filter by name.
            namelike: Filter by name (using LIKE operator).
            page: The page number for pagination.
            type: Filter by type.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_all_products(
        self,
        availability: Optional[str] = None,
        brand_id: Optional[str] = None,
        categories: Optional[str] = None,
        categoriesin: Optional[str] = None,
        channel_idin: Optional[str] = None,
        condition: Optional[str] = None,
        date_last_imported: Optional[str] = None,
        date_last_importedmax: Optional[str] = None,
        date_last_importedmin: Optional[str] = None,
        date_last_importednot: Optional[str] = None,
        date_modified: Optional[str] = None,
        date_modifiedmax: Optional[str] = None,
        date_modifiedmin: Optional[str] = None,
        direction: Optional[str] = None,
        exclude_fields: Optional[str] = None,
        id: Optional[str] = None,
        idgreater: Optional[str] = None,
        idin: Optional[str] = None,
        idless: Optional[str] = None,
        idmax: Optional[str] = None,
        idmin: Optional[str] = None,
        idnot_in: Optional[str] = None,
        include: Optional[str] = None,
        include_fields: Optional[str] = None,
        inventory_level: Optional[str] = None,
        inventory_levelgreater: Optional[str] = None,
        inventory_levelin: Optional[str] = None,
        inventory_levelless: Optional[str] = None,
        inventory_levelmax: Optional[str] = None,
        inventory_levelmin: Optional[str] = None,
        inventory_levelnot_in: Optional[str] = None,
        inventory_low: Optional[str] = None,
        is_featured: Optional[str] = None,
        is_free_shipping: Optional[str] = None,
        is_visible: Optional[str] = None,
        keyword: Optional[str] = None,
        keyword_context: Optional[str] = None,
        limit: Optional[str] = None,
        mpn: Optional[str] = None,
        name: Optional[str] = None,
        out_of_stock: Optional[str] = None,
        page: Optional[str] = None,
        price: Optional[str] = None,
        sku: Optional[str] = None,
        skuin: Optional[str] = None,
        sort: Optional[str] = None,
        total_sold: Optional[str] = None,
        type: Optional[str] = None,
        upc: Optional[str] = None,
        weight: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a complete list of all products in the BigCommerce catalog, potentially without pagination limits. Use this when you need an exhaustive export or enumeration of the entire product catalog. Note: this endpoint is identical to bigcommerce_list_products — prefer bigcommerce_list_products for standard paginated browsing. Do not use this to retrieve a single product by ID or SKU.

        Args:
            availability: 
            brand_id: 
            categories: 
            categoriesin: 
            channel_idin: 
            condition: 
            date_last_imported: 
            date_last_importedmax: 
            date_last_importedmin: 
            date_last_importednot: 
            date_modified: 
            date_modifiedmax: 
            date_modifiedmin: 
            direction: 
            exclude_fields: 
            id: 
            idgreater: 
            idin: 
            idless: 
            idmax: 
            idmin: 
            idnot_in: 
            include: 
            include_fields: 
            inventory_level: 
            inventory_levelgreater: 
            inventory_levelin: 
            inventory_levelless: 
            inventory_levelmax: 
            inventory_levelmin: 
            inventory_levelnot_in: 
            inventory_low: 
            is_featured: 
            is_free_shipping: 
            is_visible: 
            keyword: 
            keyword_context: 
            limit: 
            mpn: 
            name: 
            out_of_stock: 
            page: 
            price: 
            sku: 
            skuin: 
            sort: 
            total_sold: 
            type: 
            upc: 
            weight: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_brands(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all brands available in the BigCommerce catalog. Use this to enumerate brands before associating them with products or filtering by brand. Do not use this to retrieve a single brand (use bigcommerce_get_brand) or to create a brand (use bigcommerce_create_brand).
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_categories(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of categories from BigCommerce category trees. Use this when you need to browse or enumerate categories within the tree structure. Do not use this to get all categories without tree context (use bigcommerce_list_all_categories) or to retrieve a single category (use bigcommerce_get_category).
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_category_metafields(
        self,
        after: Optional[str] = None,
        before: Optional[str] = None,
        date_createmax: Optional[str] = None,
        date_createmin: Optional[str] = None,
        date_modifiedmax: Optional[str] = None,
        date_modifiedmin: Optional[str] = None,
        direction: Optional[str] = None,
        include_fields: Optional[str] = None,
        key: Optional[str] = None,
        keyin: Optional[str] = None,
        limit: Optional[str] = None,
        namespace: Optional[str] = None,
        namespacein: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of metafields associated with categories in the BigCommerce catalog. Metafields store additional custom data attached to categories beyond standard fields. Use this when you need to read custom metadata stored on categories. Do not use this to retrieve metafields for products (use bigcommerce_get_product_metafields) or variants (use bigcommerce_get_variant_metafields).

        Args:
            after: 
            before: 
            date_createmax: 
            date_createmin: 
            date_modifiedmax: 
            date_modifiedmin: 
            direction: 
            include_fields: 
            key: 
            keyin: 
            limit: 
            namespace: 
            namespacein: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_category_trees(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all category trees configured in the BigCommerce store. Use this to enumerate the available top-level tree structures before drilling into their categories. Do not use this to retrieve categories within a specific tree (use bigcommerce_get_a_category_tree) or to list individual categories (use bigcommerce_list_categories).
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_channels(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all sales channels configured in the BigCommerce store. Use this to enumerate available channels such as storefronts, POS systems, or marketplaces. Do not use this to retrieve a single channel (use bigcommerce_get_channel) or to manage channel currency assignments (use bigcommerce_list_channels_currency_assignments).
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_channels_currency_assignments(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of currency assignments for all sales channels in the BigCommerce store. Use this to determine which currencies are enabled for each channel. Do not use this to list channels themselves (use bigcommerce_list_channels) or to update channel settings (use bigcommerce_update_channel).
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_customers(
        self,
        after: Optional[str] = None,
        before: Optional[str] = None,
        companyin: Optional[str] = None,
        customer_group_idin: Optional[str] = None,
        date_created: Optional[str] = None,
        date_createdmax: Optional[str] = None,
        date_createdmin: Optional[str] = None,
        date_modified: Optional[str] = None,
        date_modifiedmax: Optional[str] = None,
        date_modifiedmin: Optional[str] = None,
        emailin: Optional[str] = None,
        idin: Optional[str] = None,
        include: Optional[str] = None,
        limit: Optional[str] = None,
        namein: Optional[str] = None,
        namelike: Optional[str] = None,
        page: Optional[str] = None,
        phonein: Optional[str] = None,
        registration_ip_addressin: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all customer accounts in the BigCommerce store. Use this to browse or search for customers. Do not use this to retrieve details about a single customer or to manage customer attributes (use bigcommerce_list_all_customer_attributes).

        Args:
            after: Filter customers created after a specific date.
            before: Filter customers created before a specific date.
            companyin: Filter customers by company name.
            customer_group_idin: Filter customers by customer group ID.
            date_created: Filter customers created on a specific date.
            date_createdmax: Filter customers created before a specific date.
            date_createdmin: Filter customers created after a specific date.
            date_modified: Filter customers modified on a specific date.
            date_modifiedmax: Filter customers modified before a specific date.
            date_modifiedmin: Filter customers modified after a specific date.
            emailin: Filter customers by email address.
            idin: Filter customers by customer ID.
            include: Specify additional fields to include in the response.
            limit: Limit the number of results returned.
            namein: Filter customers by customer name.
            namelike: Filter customers where the name contains a specific string.
            page: Specify the page number for pagination.
            phonein: Filter customers by phone number.
            registration_ip_addressin: Filter customers by registration IP address.
            sort: Specify the sort order for the results.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_order_line_items(
        self,
        orderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of line items (products purchased) for a specific order in BigCommerce, identified by order ID. Note: this endpoint is identical to bigcommerce_list_order_products — prefer one consistently. Use this to inspect what was purchased in an order. Do not use this to retrieve order metadata (use bigcommerce_get_order).

        Args:
            orderId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_order_metafields(
        self,
        direction: Optional[str] = None,
        key: Optional[str] = None,
        limit: Optional[str] = None,
        namespace: Optional[str] = None,
        orderId: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of metafields attached to a specific order in BigCommerce, identified by its order ID. Metafields store custom key-value data on orders beyond standard order fields. Use this when you need to read custom metadata associated with an order. Do not use this to retrieve standard order details (use bigcommerce_get_order).

        Args:
            direction: 
            key: 
            limit: 
            namespace: 
            orderId: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_order_products(
        self,
        limit: Optional[str] = None,
        orderId: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all products (line items) associated with a specific order, identified by its order ID. Use this when you need to inspect which products were purchased in a given order, including quantities, prices, and variant details. Do not use this to retrieve general order metadata (use bigcommerce_get_order) or shipment information (use bigcommerce_list_order_shipments).

        Args:
            limit: 
            orderId: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_order_shipment_addresses(
        self,
        orderId: str,
    ) -> Dict[str, Any]:
        """Returns a list of shipping addresses associated with a specific order in BigCommerce, identified by order ID. Use this when you need to retrieve the delivery destination(s) for an order. Do not use this to retrieve shipment tracking records (use bigcommerce_list_order_shipments) or general order details (use bigcommerce_get_order).

        Args:
            orderId: The ID of the order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_order_shipments(
        self,
        limit: Optional[str] = None,
        orderId: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all shipments associated with a specific order in BigCommerce, identified by its order ID. Each shipment includes tracking information, shipping method, and shipped items. Use this when you need to check shipment status or tracking for an order. Do not use this to create a new shipment (use bigcommerce_create_shipment) or to retrieve order line items (use bigcommerce_list_order_products).

        Args:
            limit: 
            orderId: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_orders(
        self,
        cart_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        consignment_structure: Optional[str] = None,
        customer_id: Optional[str] = None,
        email: Optional[str] = None,
        external_order_id: Optional[str] = None,
        include: Optional[str] = None,
        limit: Optional[str] = None,
        max_date_created: Optional[str] = None,
        max_date_modified: Optional[str] = None,
        max_id: Optional[str] = None,
        max_total: Optional[str] = None,
        min_date_created: Optional[str] = None,
        min_date_modified: Optional[str] = None,
        min_id: Optional[str] = None,
        min_total: Optional[str] = None,
        page: Optional[str] = None,
        payment_method: Optional[str] = None,
        sort: Optional[str] = None,
        status_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all orders in the BigCommerce store. Use this when you need to browse or enumerate orders across the store. Do not use this to retrieve a single order (use bigcommerce_get_order) or to inspect the products within an order (use bigcommerce_list_order_products).

        Args:
            cart_id: Cart ID for filtering.
            channel_id: Channel ID for filtering.
            consignment_structure: Consignment structure for filtering.
            customer_id: Customer ID for filtering.
            email: Customer email for filtering.
            external_order_id: External order ID for filtering.
            include: Fields to include in the response.
            limit: Limit the number of results.
            max_date_created: Maximum date created for filtering.
            max_date_modified: Maximum date modified for filtering.
            max_id: Maximum ID for filtering.
            max_total: Maximum total value for filtering.
            min_date_created: Minimum date created for filtering.
            min_date_modified: Minimum date modified for filtering.
            min_id: Minimum ID for filtering.
            min_total: Minimum total value for filtering.
            page: Page number for pagination.
            payment_method: Payment method for filtering.
            sort: Sorting criteria for the response.
            status_id: Status ID for filtering.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_pricelist_records(
        self,
        after: Optional[str] = None,
        before: Optional[str] = None,
        calculated_price: Optional[str] = None,
        calculated_pricemax: Optional[str] = None,
        calculated_pricemin: Optional[str] = None,
        currency: Optional[str] = None,
        currencyin: Optional[str] = None,
        date_created: Optional[str] = None,
        date_createdmax: Optional[str] = None,
        date_createdmin: Optional[str] = None,
        date_modified: Optional[str] = None,
        date_modifiedmax: Optional[str] = None,
        date_modifiedmin: Optional[str] = None,
        include: Optional[str] = None,
        limit: Optional[str] = None,
        map_price: Optional[str] = None,
        map_pricemax: Optional[str] = None,
        map_pricemin: Optional[str] = None,
        page: Optional[str] = None,
        price: Optional[str] = None,
        priceListId: Optional[str] = None,
        pricemax: Optional[str] = None,
        pricemin: Optional[str] = None,
        product_idin: Optional[str] = None,
        retail_price: Optional[str] = None,
        retail_pricemax: Optional[str] = None,
        retail_pricemin: Optional[str] = None,
        sale_price: Optional[str] = None,
        sale_pricemax: Optional[str] = None,
        sale_pricemin: Optional[str] = None,
        sku: Optional[str] = None,
        skuin: Optional[str] = None,
        variant_idin: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all price records within a specific price list in BigCommerce, identified by its price list ID. Each record defines the price for a specific variant in that list. Use this when you need to inspect or export the pricing entries of a price list. Do not use this to retrieve available price lists themselves (use bigcommerce_list_pricelists).

        Args:
            after: 
            before: 
            calculated_price: 
            calculated_pricemax: 
            calculated_pricemin: 
            currency: 
            currencyin: 
            date_created: 
            date_createdmax: 
            date_createdmin: 
            date_modified: 
            date_modifiedmax: 
            date_modifiedmin: 
            include: 
            limit: 
            map_price: 
            map_pricemax: 
            map_pricemin: 
            page: 
            price: 
            priceListId: 
            pricemax: 
            pricemin: 
            product_idin: 
            retail_price: 
            retail_pricemax: 
            retail_pricemin: 
            sale_price: 
            sale_pricemax: 
            sale_pricemin: 
            sku: 
            skuin: 
            variant_idin: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_pricelists(
        self,
        after: Optional[str] = None,
        before: Optional[str] = None,
        date_created: Optional[str] = None,
        date_createdmax: Optional[str] = None,
        date_createdmin: Optional[str] = None,
        date_modified: Optional[str] = None,
        date_modifiedmax: Optional[str] = None,
        date_modifiedmin: Optional[str] = None,
        idin: Optional[str] = None,
        limit: Optional[str] = None,
        name: Optional[str] = None,
        namelike: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all price lists configured in the BigCommerce store. Price lists allow merchants to offer different pricing to specific customer groups or channels. Use this to discover available price lists before querying their records. Do not use this to retrieve the price records within a list (use bigcommerce_list_pricelist_records).

        Args:
            after: 
            before: 
            date_created: 
            date_createdmax: 
            date_createdmin: 
            date_modified: 
            date_modifiedmax: 
            date_modifiedmin: 
            idin: 
            limit: 
            name: 
            namelike: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_product_custom_fields(
        self,
        productId: str,
        exclude_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all custom fields associated with a specific product in BigCommerce, identified by product ID. Use this to enumerate the custom field definitions and values on a product. Do not use this to retrieve a single custom field (use bigcommerce_get_product_custom_field) or to retrieve metafields (use bigcommerce_list_product_metafields).

        Args:
            productId: The ID of the product. (required)
            exclude_fields: Fields to exclude from the response.
            include_fields: Fields to include in the response.
            limit: The maximum number of results to return.
            page: The page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_product_images(
        self,
        productId: str,
        exclude_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all images associated with a specific product in BigCommerce, identified by product ID. Use this when you need to inspect or enumerate the images attached to a product. Do not use this to add a new image (use bigcommerce_add_product_image_by_url or bigcommerce_add_product_image_by_file) or to delete an image (use bigcommerce_delete_product_image).

        Args:
            productId: The ID of the product to retrieve. (required)
            exclude_fields: Comma-separated list of fields to exclude from the response.
            include_fields: Comma-separated list of fields to include in the response.
            limit: Maximum number of results to return.
            page: Page number of results to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_product_level_custom_fields(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        productId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of custom fields defined at the product level for a specific product in BigCommerce, identified by product ID. Note: this endpoint is identical to bigcommerce_list_product_custom_fields — prefer one consistently. Use this to read product-level custom field data. Do not use this to retrieve metafields (use bigcommerce_list_product_metafields).

        Args:
            limit: Limit the number of results.
            page: Specify the page number for pagination.
            productId: ID of the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_product_metafields(
        self,
        after: Optional[str] = None,
        before: Optional[str] = None,
        dateCreated_max: Optional[str] = None,
        dateCreated_min: Optional[str] = None,
        dateModified_max: Optional[str] = None,
        dateModified_min: Optional[str] = None,
        exclude_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
        key: Optional[str] = None,
        key_in: Optional[str] = None,
        limit: Optional[str] = None,
        namespace: Optional[str] = None,
        page: Optional[str] = None,
        productId: Optional[str] = None,
        resource_idin: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of metafields associated with a specific product in BigCommerce, identified by product ID. Metafields store custom key-value data on products beyond standard fields. Use this when you need to read custom metadata on a product. Do not use this to retrieve metafields for variants (use bigcommerce_list_variant_metafields) or categories (use bigcommerce_list_category_metafields).

        Args:
            after: 
            before: 
            dateCreated_max: 
            dateCreated_min: 
            dateModified_max: 
            dateModified_min: 
            exclude_fields: Fields to exclude from the response.
            include_fields: Specific fields to include in the response.
            key: A key used to filter or search results.
            key_in: 
            limit: Maximum number of results to return.
            namespace: Resource namespace for the API call.
            page: Pagination page number.
            productId: The identifier of the product resource in Bigcommerce.
            resource_idin: Filter results by resource IDs (in).
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_product_options(
        self,
        productId: str,
        exclude_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all options (e.g. size, color) associated with a specific product in BigCommerce, identified by product ID. Use this when you need to see what configurable options are available for a product before working with variants. Do not use this to retrieve option values for a specific option or to list variants (use bigcommerce_list_variants).

        Args:
            productId: The product identifier used in the request URL. (required)
            exclude_fields: Comma-separated list of fields to exclude from the response.
            include_fields: Comma-separated list of fields to include in the response.
            limit: Maximum number of items to return per page.
            page: Page number for paginated results.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_products(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all products available in the BigCommerce catalog. Use this when you need to browse or enumerate the product catalog. Do not use this to retrieve a single product by ID or SKU — use bigcommerce_get_product or bigcommerce_get_product_by_sku instead. Note: this tool may return duplicate results if bigcommerce_list_all_products is also available; prefer this tool for standard paginated browsing.

        Args:
            limit: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_variant_metafields(
        self,
        exclude_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
        key: Optional[str] = None,
        limit: Optional[str] = None,
        namespace: Optional[str] = None,
        page: Optional[str] = None,
        productId: Optional[str] = None,
        resource_idin: Optional[str] = None,
        variantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of metafields associated with a specific variant of a product in BigCommerce, identified by product ID and variant ID. Metafields store custom key-value data on variants. Use this when you need to read custom metadata stored on a variant. Do not use this to retrieve metafields for a product (use bigcommerce_get_product_metafields) or for categories (use bigcommerce_list_category_metafields).

        Args:
            exclude_fields: 
            include_fields: 
            key: 
            limit: 
            namespace: 
            page: 
            productId: 
            resource_idin: 
            variantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_variants(
        self,
        productId: str,
        exclude_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
        limit: Optional[int] = None,
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all variants for a specific product in BigCommerce, identified by product ID. Use this when you need to enumerate all SKU combinations available for a product. Do not use this to retrieve a single variant or to list options for a product (use bigcommerce_list_product_options).

        Args:
            productId:  (required)
            exclude_fields: 
            include_fields: 
            limit: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_list_webhooks(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all webhooks configured in the BigCommerce store. Use this to enumerate active webhook subscriptions and their event scopes. Do not use this to retrieve a single webhook (use bigcommerce_get_webhook) or to create a new one (use bigcommerce_create_webhook).

        Args:
            limit: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_unassign_product_from_channel(
        self,
        channel_id: Optional[str] = None,
        product_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes the assignment of one or more products from a specific sales channel in BigCommerce, making them unavailable for sale on that channel. This action is irreversible without reassigning the product. Do not use this to assign a product to a channel (use bigcommerce_assign_product_to_channel) or to delete the product itself (use bigcommerce_delete_product).

        Args:
            channel_id: 
            product_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_batch_metafields(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates multiple product-level metafields in a single batch operation in the BigCommerce catalog. Use this when you need to modify the values or properties of several product metafields at once. Do not use this to create new metafields in batch (use bigcommerce_batch_create_metafields) or to update a single product metafield.

        Args:
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_brand(
        self,
        brandId: str,
        custom_url: Optional[_BigcommerceUpdateBrandCustomUrl] = None,
        image_url: Optional[str] = None,
        meta_description: Optional[str] = None,
        meta_keywords: Optional[List[Any]] = None,
        name: Optional[str] = None,
        page_title: Optional[str] = None,
        search_keywords: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing brand in the BigCommerce catalog, identified by its brand ID. Use this to modify brand properties such as name, page title, meta description, or search keywords. Do not use this to create a new brand (use bigcommerce_create_brand) or to upload a brand image (use bigcommerce_create_brand_image).

        Args:
            brandId: The brand identifier. (required)
            custom_url: Custom URL configuration for the page.
            image_url: URL of the page image.
            meta_description: SEO meta description for the page.
            meta_keywords: SEO keywords for the page.
            name: The name of the page.
            page_title: The title of the page as displayed to users.
            search_keywords: Keywords to help with search indexing.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_cart_line_item(
        self,
        cartId: str,
        itemId: str,
        custom_items: Optional[List[Any]] = None,
        gift_certificates: Optional[List[Any]] = None,
        include: Optional[str] = None,
        line_item: Optional[_BigcommerceUpdateCartLineItemLineItem] = None,
        version: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates a specific line item within a shopping cart in BigCommerce, identified by cart ID and item ID. Use this to change the quantity or options of an item already in the cart. Do not use this to retrieve the cart (use bigcommerce_get_cart) or to add a new item to the cart.

        Args:
            cartId:  (required)
            itemId:  (required)
            custom_items: 
            gift_certificates: 
            include: 
            line_item: 
            version: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_categories(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates multiple categories within BigCommerce category trees in a single batch operation. Use this for bulk edits to category properties such as name, description, or parent. Do not use this to update a single category by ID (use bigcommerce_update_category) or to update a category tree structure (use bigcommerce_upsert_category_tree).

        Args:
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_category(
        self,
        categoryId: str,
        custom_url: Optional[_BigcommerceUpdateCategoryCustomUrl] = None,
        default_product_sort: Optional[str] = None,
        description: Optional[str] = None,
        image_url: Optional[str] = None,
        is_visible: Optional[bool] = None,
        layout_file: Optional[str] = None,
        meta_description: Optional[str] = None,
        meta_keywords: Optional[List[Any]] = None,
        name: Optional[str] = None,
        page_title: Optional[str] = None,
        parent_id: Optional[int] = None,
        search_keywords: Optional[str] = None,
        sort_order: Optional[int] = None,
        views: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing category in the BigCommerce catalog, identified by its category ID. Use this to modify category properties such as name, description, parent, or visibility. Do not use this to update categories within a tree structure (use bigcommerce_update_category_in_tree) or to update multiple categories in batch (use bigcommerce_update_categories).

        Args:
            categoryId: The ID of the category to operate on. (required)
            custom_url: Custom URL mapping for the category.
            default_product_sort: Default sort order for products within this category.
            description: A description of the category.
            image_url: URL of the category image.
            is_visible: Whether the category is visible on the storefront.
            layout_file: The layout file used for the category page.
            meta_description: Meta description for SEO.
            meta_keywords: Meta keywords for SEO.
            name: The name of the category.
            page_title: The SEO page title for this category.
            parent_id: The ID of the parent category under which this category will be created.
            search_keywords: SEO keywords for search optimization.
            sort_order: The display order of the category among siblings.
            views: The number of times this category has been viewed.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_category_in_tree(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates one or more existing categories within a category tree in the BigCommerce catalog. Use this when you need to modify category properties such as name, description, or parent in a tree structure. Do not use this to update a standalone category by ID (use bigcommerce_update_category) or to create new categories in a tree (use bigcommerce_create_category_in_tree).

        Args:
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_channel(
        self,
        channelId: str,
        config_meta: Optional[_BigcommerceUpdateChannelConfigMeta] = None,
        is_listable_from_ui: Optional[bool] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing sales channel in BigCommerce, identified by its channel ID. Use this to modify channel properties such as name, status, or external ID. Do not use this to create a new channel (use bigcommerce_create_channel) or to manage channel currency assignments.

        Args:
            channelId: Identifier for the sales channel. (required)
            config_meta: Metadata related to the configuration.
            is_listable_from_ui: Indicates if the item is listable from the user interface.
            name: Name of the item.
            status: Status of the item.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_customer(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the details of one or more existing customer records in BigCommerce. Use this to modify customer properties such as name, email, phone, or group assignment. Do not use this to update customer attribute values (use bigcommerce_upsert_customer_attribute_values) or to create a new customer (use bigcommerce_create_customer).

        Args:
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_customer_attribute(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Updates an existing customer attribute definition in BigCommerce. Use this to modify the name or type of a customer attribute. Do not use this to update the values assigned to customers (use bigcommerce_upsert_customer_attribute_values) or to create a new attribute (use bigcommerce_create_customer_attribute).

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_customer_group(
        self,
        category_access: Optional[_BigcommerceUpdateCustomerGroupCategoryAccess] = None,
        customerGroupId: Optional[str] = None,
        discount_rules: Optional[List[Any]] = None,
        is_default: Optional[bool] = None,
        is_group_for_guests: Optional[bool] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing customer group in BigCommerce, identified by its customer group ID. Use this when you need to modify group properties such as name, discount rules, or category access. Do not use this to update individual customer records (use bigcommerce_update_customer) or to create a new customer group.

        Args:
            category_access: 
            customerGroupId: 
            discount_rules: 
            is_default: 
            is_group_for_guests: 
            name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_product(
        self,
        productId: str,
        data: Optional[_BigcommerceUpdateProductData] = None,
        meta: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing product in the BigCommerce catalog, identified by its product ID. Use this to modify product properties such as name, price, description, availability, or category. Do not use this to update multiple products at once (use bigcommerce_update_products_batch) or to update product variants (use bigcommerce_update_variant).

        Args:
            productId: ID of the product. (required)
            data: Product information for the Bigcommerce API.
            meta: Metadata related to the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_product_custom_field(
        self,
        customFieldId: str,
        productId: str,
        name: Optional[str] = None,
        value: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates a specific custom field on a product in BigCommerce, identified by product ID and custom field ID. Use this to modify the name or value of an existing custom field. Do not use this to create a new custom field (use bigcommerce_create_product_custom_fields) or to update metafields (use bigcommerce_update_batch_metafields).

        Args:
            customFieldId: ID of the custom field. (required)
            productId: ID of the product. (required)
            name: Name of the custom field value.
            value: Value of the custom field.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_products_batch(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Updates multiple products in a single batch operation in the BigCommerce catalog. Use this for bulk edits to product data such as pricing, availability, or descriptions across many products at once. Do not use this to update a single product (use bigcommerce_update_product) or to create new products.

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_variant(
        self,
        productId: str,
        product_id: int,
        variantId: str,
        bin_picking_number: Optional[str] = None,
        cost_price: Optional[float] = None,
        depth: Optional[float] = None,
        fixed_cost_shipping_price: Optional[float] = None,
        gtin: Optional[str] = None,
        height: Optional[float] = None,
        image_url: Optional[str] = None,
        inventory_level: Optional[int] = None,
        inventory_warning_level: Optional[int] = None,
        is_free_shipping: Optional[bool] = None,
        mpn: Optional[str] = None,
        price: Optional[float] = None,
        purchasing_disabled: Optional[bool] = None,
        purchasing_disabled_message: Optional[str] = None,
        retail_price: Optional[float] = None,
        sale_price: Optional[float] = None,
        sku: Optional[str] = None,
        upc: Optional[str] = None,
        weight: Optional[float] = None,
        width: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Updates the details of a specific product variant in BigCommerce, identified by product ID and variant ID. Use this to modify variant properties such as price, SKU, weight, inventory, or image. Do not use this to update variant metafields (use bigcommerce_update_variant_meta_fields) or to update the parent product (use bigcommerce_update_product).

        Args:
            productId: The BigCommerce product identifier. (required)
            product_id: Product identifier referenced in the request body. (required)
            variantId: The specific product variant identifier. (required)
            bin_picking_number: Bin location or picking number for warehouse fulfillment.
            cost_price: Cost to acquire or produce the item.
            depth: Depth of the product dimensions.
            fixed_cost_shipping_price: Fixed shipping price for this item.
            gtin: Global Trade Item Number.
            height: Height of the product dimensions.
            image_url: URL of the product's image.
            inventory_level: Current inventory quantity on hand.
            inventory_warning_level: Threshold to trigger inventory warnings.
            is_free_shipping: Indicates if the item ships for free.
            mpn: Manufacturer Part Number.
            price: Regular price of the product.
            purchasing_disabled: Flag to disable purchasing for this product.
            purchasing_disabled_message: Message shown when purchasing is disabled.
            retail_price: Suggested retail price.
            sale_price: Discounted price during promotions.
            sku: Stock Keeping Unit - unique identifier for stock keeping.
            upc: Universal Product Code for the product.
            weight: Weight of the product for shipping calculations.
            width: Width of the product dimensions.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_variant_meta_fields(
        self,
        key: str,
        metaFieldId: str,
        namespace: str,
        productId: str,
        value: str,
        variantId: str,
        description: Optional[str] = None,
        permission_set: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates a specific metafield on a product variant in BigCommerce, identified by product ID, variant ID, and metafield ID. Use this to modify the key, value, namespace, or permissions of an existing variant metafield. Do not use this to create a new variant metafield (use bigcommerce_add_variant_meta_fields) or to update multiple variant metafields in bulk (use bigcommerce_batch_create_variants_metafields).

        Args:
            key: The key (name) of the metafield. (required)
            metaFieldId: Identifier of the metafield to target. (required)
            namespace: Namespace to group related metafields; helps avoid naming collisions. (required)
            productId: The ID of the product associated with the metafield. (required)
            value: The value to store in the metafield. (required)
            variantId: The ID of the product variant associated with the metafield, if applicable. (required)
            description: Optional human-readable description of the metafield.
            permission_set: Permission settings for the metafield (for example, read/write restrictions).
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_update_variant_option(
        self,
        id: int,
        optionId: str,
        option_values: List[Any],
        productId: str,
        config: Optional[Dict[str, Any]] = None,
        display_name: Optional[str] = None,
        image_url: Optional[str] = None,
        product_id: Optional[int] = None,
        sort_order: Optional[int] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates a specific product option in BigCommerce, identified by product ID and option ID. Use this to modify option properties such as display name, type, or sort order. Do not use this to update individual option values (use bigcommerce_add_product_option_values) or to update a variant itself (use bigcommerce_update_variant).

        Args:
            id: Identifier of the image item. (required)
            optionId: Option identifier in URL path. (required)
            option_values:  (required)
            productId: Product identifier in URL path. (required)
            config: Configuration for the image or option.
            display_name: Display name for the image.
            image_url: URL of the image to associate with the product.
            product_id: The ID of the product to which the image relates.
            sort_order: The sort order of this option.
            type: The type of the image.
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_upsert_category_tree(
        self,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Inserts or updates a category tree in BigCommerce depending on whether it already exists. Use this when you need to create or overwrite a category tree definition. Do not use this to manage individual categories within a tree (use bigcommerce_create_categories or bigcommerce_update_categories) or to delete a tree (use bigcommerce_delete_category_tree).

        Args:
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bigcommerce_upsert_customer_attribute_values(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Inserts or updates customer attribute values in BigCommerce depending on whether they already exist. Use this when you need to set or modify custom attribute data for customers without knowing if values are already present. Do not use this to delete attribute values (use bigcommerce_delete_customer_attribute_values) or to manage attribute definitions (use bigcommerce_create_customer_attribute or bigcommerce_update_customer_attribute).

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

