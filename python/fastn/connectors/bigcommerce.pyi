"""Fastn Bigcommerce connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BigcommerceConnector:
    """Bigcommerce connector ().

    Provides 76 tools.
    """

    def add_product_image_by_file(
        self,
        image_file: str,
        description: Optional[str] = None,
        is_thumbnail: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds an image to a product from a file upload.

        Args:
            image_file: The image file to upload. (required)
            description: Description for the product image.
            is_thumbnail: Flag to indicate whether the image should be set as the product's thumbnail.
            sort_order: The display order of the image.
        Returns:
            API response as a dictionary.
        """
        ...

    def add_product_image_by_url(
        self,
        description: Optional[str] = None,
        image_url: Optional[str] = None,
        is_thumbnail: Optional[bool] = None,
        sort_order: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Adds an image to a product from a URL.

        Args:
            description: 
            image_url: 
            is_thumbnail: 
            sort_order: 
        Returns:
            API response as a dictionary.
        """
        ...

    def add_product_option_values(
        self,
        label: Optional[str] = None,
        sort_order: Optional[int] = None,
        value_data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Adds values to an existing product option.

        Args:
            label: 
            sort_order: 
            value_data: 
        Returns:
            API response as a dictionary.
        """
        ...

    def add_variant_image(
        self,
        image_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds an image to a specific variant.

        Args:
            image_url: 
        Returns:
            API response as a dictionary.
        """
        ...

    def add_variant_meta_fields(
        self,
        description: Optional[str] = None,
        key: Optional[str] = None,
        namespace: Optional[str] = None,
        permission_set: Optional[str] = None,
        value: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds metafields to a specific variant.

        Args:
            description: 
            key: 
            namespace: 
            permission_set: 
            value: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_brand_(
        self,
        name: str,
        custom_url: Optional[Dict[str, Any]] = None,
        image_url: Optional[str] = None,
        meta_description: Optional[str] = None,
        meta_keywords: Optional[List[Any]] = None,
        page_title: Optional[str] = None,
        search_keywords: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new brand in the system.

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

    def create_brand_image(
        self,
        image: str,
    ) -> Dict[str, Any]:
        """Creates an image for a brand.

        Args:
            image: The image data or URL to be used by the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_categories(
        self,
    ) -> Dict[str, Any]:
        """Creates new categories within the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_category(
        self,
        name: str,
        parent_id: int,
    ) -> Dict[str, Any]:
        """Creates a new category in the system.

        Args:
            name: The name of the resource being created or updated. (required)
            parent_id: The identifier of the parent resource under which the new item will be created. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_channel(
        self,
        name: str,
        platform: str,
        status: str,
        type: str,
    ) -> Dict[str, Any]:
        """Creates a new channel in the system.

        Args:
            name: The resource name. (required)
            platform: The target platform; for this schema, BigCommerce. (required)
            status: The desired status of the resource. (required)
            type: The type category of the resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_customer(
        self,
    ) -> Dict[str, Any]:
        """Creates a new customer in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_customer_attribute(
        self,
    ) -> Dict[str, Any]:
        """Creates a new customer attribute in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product(
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
        custom_url: Optional[Dict[str, Any]] = None,
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
        """Creates a new product in the system.

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

    def create_product_custom_fields(
        self,
        name: str,
        value: str,
    ) -> Dict[str, Any]:
        """Creates custom fields for a product.

        Args:
            name: The name of the item. (required)
            value: The value of the item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product_meta_fields(
        self,
        key: str,
        namespace: str,
        value: str,
        description: Optional[str] = None,
        permission_set: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates new metafields for a product.

        Args:
            key: The key for the configuration setting. (required)
            namespace: The namespace for the configuration entry. (required)
            value: The value for the configuration entry. (required)
            description: Description of the configuration entry.
            permission_set: Permissions associated with this configuration.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product_options(
        self,
        display_name: Optional[str] = None,
        name: Optional[str] = None,
        option_values: Optional[List[Any]] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates options for a product.

        Args:
            display_name: 
            name: 
            option_values: 
            type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_shipment(
        self,
        comments: Optional[str] = None,
        items: Optional[List[Any]] = None,
        order_address_id: Optional[int] = None,
        tracking_number: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new shipment for an order.

        Args:
            comments: Any comments related to the order update.
            items: 
            order_address_id: The ID of the order address.
            tracking_number: The tracking number for the shipment.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_variant(
        self,
        inventory_level: Optional[int] = None,
        option_values: Optional[List[Any]] = None,
        price: Optional[float] = None,
        sku: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new variant for an existing product.

        Args:
            inventory_level: Current inventory level for the product.
            option_values: 
            price: Price of the product.
            sku: Stock Keeping Unit for the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_webhook(
        self,
        destination: str,
        is_active: bool,
        scope: str,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the system.

        Args:
            destination: Destination or target of the Bigcommerce API request. (required)
            is_active: Indicates whether the item is active in Bigcommerce. (required)
            scope: Scope or context of the Bigcommerce API request. (required)
            headers: Optional headers for the Bigcommerce API request.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_batch_meta_fields(
        self,
    ) -> Dict[str, Any]:
        """Deletes multiple metafields at once.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_catagory_tree(
        self,
    ) -> Dict[str, Any]:
        """Deletes a specified category tree in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_categories(
        self,
    ) -> Dict[str, Any]:
        """Deletes specified categories from the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_customer_attribute(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Deletes a specified customer attribute.

        Args:
            id: ID parameter for the BigCommerce2 API endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_customer_attribute_values(
        self,
        idin: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Deletes specific customer attribute values.

        Args:
            idin: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified product from the system.

        Args:
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product_custom_field(
        self,
        customFieldId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified product custom field.

        Args:
            customFieldId: The ID of the custom field. (required)
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product_image(
        self,
        imageId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified image from a product.

        Args:
            imageId: The image identifier associated with the product. (required)
            productId: The product identifier related to the image. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_variant_meta_field(
        self,
        metaFieldId: str,
        productId: str,
        variantId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified metafield from a variant.

        Args:
            metaFieldId: The identifier of the metafield to operate on. (required)
            productId: The identifier of the product associated with the request. (required)
            variantId: The identifier of the product variant associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_variant_option(
        self,
        optionId: str,
        productId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified variant option.

        Args:
            optionId: The ID of the option for the product. (required)
            productId: The ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Deletes a specified webhook from the system.

        Args:
            id: The ID of the URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_a_category_tree(
        self,
        categoryTreeId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific category tree identified by ID.

        Args:
            categoryTreeId: The ID of the category tree. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_customer_attribute_values(
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
        """Retrieves all customer attribute values.

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

    def get_all_customer_attributes(
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
        """Retrieves all customer attributes available in the system.

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

    def get_brand(
        self,
        exclude_fields: Optional[List[Any]] = None,
        include_fields: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific brand.

        Args:
            exclude_fields: List of field names to exclude from the API response.
            include_fields: List of field names to explicitly include in the API response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_brands(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of brands in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_cart(
        self,
        include: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the shopping cart for the current session.

        Args:
            include: Specifies additional data to include in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_categories(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of categories available in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_category(
        self,
        exclude_fields: Optional[List[Any]] = None,
        include_fields: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific category.

        Args:
            exclude_fields: Fields to exclude from the response.
            include_fields: Fields to include in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_category_trees(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the category trees available in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_channel(
        self,
        channelId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific channel.

        Args:
            channelId: The channel ID for the Bigcommerce API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_channel_active_theme(
        self,
        channelId: str,
    ) -> Dict[str, Any]:
        """Gets the currently active theme for a specified channel.

        Args:
            channelId: The channel ID for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_channels(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of channels in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_channels_currency_assignments(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the currency assignments for all channels.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_customers(
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
        """Fetches a list of customers in the system.

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

    def get_order(
        self,
        orderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific order.

        Args:
            orderId: The order ID.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order_line_items(
        self,
        orderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the line items for a specific order.

        Args:
            orderId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_order_shipment_address(
        self,
        orderId: str,
    ) -> Dict[str, Any]:
        """Fetches the shipment address for a specific order.

        Args:
            orderId: The ID of the order. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_orders(
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
        """Fetches a list of orders in the system.

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

    def get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific product.

        Args:
            productId: The ID of the product being accessed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_by_sku(
        self,
        sku: str,
    ) -> Dict[str, Any]:
        """Retrieves a product by its SKU.

        Args:
            sku: The Stock Keeping Unit (SKU) identifier. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_custom_field(
        self,
        exclude_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific product custom field.

        Args:
            exclude_fields: Comma-separated list of fields to exclude from the response.
            include_fields: Comma-separated list of fields to include in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_custom_fields(
        self,
        exclude_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all custom fields associated with a product.

        Args:
            exclude_fields: Fields to exclude from the response.
            include_fields: Fields to include in the response.
            limit: The maximum number of results to return.
            page: The page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_images(
        self,
        exclude_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches images associated with a specific product.

        Args:
            exclude_fields: Comma-separated list of fields to exclude from the response.
            include_fields: Comma-separated list of fields to include in the response.
            limit: Maximum number of results to return.
            page: Page number of results to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_level_custom_fields(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches product-level custom fields for a product.

        Args:
            limit: Limit the number of results.
            page: Specify the page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_metafields(
        self,
        exclude_fields: Optional[str] = None,
        include_fields: Optional[str] = None,
        key: Optional[str] = None,
        limit: Optional[str] = None,
        namespace: Optional[str] = None,
        page: Optional[str] = None,
        resource_idin: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches metafields associated with a specific product.

        Args:
            exclude_fields: Fields to exclude from the response.
            include_fields: Specific fields to include in the response.
            key: A key used to filter or search results.
            limit: Maximum number of results to return.
            namespace: Resource namespace for the API call.
            page: Pagination page number.
            resource_idin: Filter results by resource IDs (in).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_options(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves options associated with a specific product.

        Args:
            productId: The product identifier used in the request URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of products available in the system.

        Args:
            limit: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_variants(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Fetches all variants for a specified product.

        Args:
            productId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhook(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific webhook.

        Args:
            id: The ID of the URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhooks(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all webhooks set up in the system.

        Args:
            limit: 
            page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_batch_metafields(
        self,
    ) -> Dict[str, Any]:
        """Updates metafields in a batch operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_brand(
        self,
        custom_url: Optional[Dict[str, Any]] = None,
        image_url: Optional[str] = None,
        meta_description: Optional[str] = None,
        meta_keywords: Optional[List[Any]] = None,
        name: Optional[str] = None,
        page_title: Optional[str] = None,
        search_keywords: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the information of an existing brand.

        Args:
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

    def update_cart_line_item(
        self,
        include: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates a line item within the shopping cart.

        Args:
            include: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_categories(
        self,
    ) -> Dict[str, Any]:
        """Updates existing categories in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_category(
        self,
        custom_url: Optional[Dict[str, Any]] = None,
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
        """Updates an existing category in the system.

        Args:
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

    def update_channel(
        self,
        config_meta: Optional[Dict[str, Any]] = None,
        is_listable_from_ui: Optional[bool] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing channel.

        Args:
            config_meta: Metadata related to the configuration.
            is_listable_from_ui: Indicates if the item is listable from the user interface.
            name: Name of the item.
            status: Status of the item.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_customer(
        self,
    ) -> Dict[str, Any]:
        """Updates the information of an existing customer.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_customer_attribute(
        self,
    ) -> Dict[str, Any]:
        """Updates an existing customer attribute.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product(
        self,
        data: Optional[Dict[str, Any]] = None,
        meta: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing product.

        Args:
            data: Product information for the Bigcommerce API.
            meta: Metadata related to the product.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product_custom_field(
        self,
        name: Optional[str] = None,
        value: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates a specific product custom field.

        Args:
            name: Name of the custom field value.
            value: Value of the custom field.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_products_batch(
        self,
    ) -> Dict[str, Any]:
        """Updates multiple products in a batch operation.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_variant(
        self,
        product_id: int,
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
        """Updates the information of a specific variant.

        Args:
            product_id: Product identifier referenced in the request body. (required)
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

    def update_variant_meta_fields(
        self,
        key: str,
        namespace: str,
        value: str,
        description: Optional[str] = None,
        permission_set: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates metafields for a specific variant.

        Args:
            key: The key (name) of the metafield. (required)
            namespace: Namespace to group related metafields; helps avoid naming collisions. (required)
            value: The value to store in the metafield. (required)
            description: Optional human-readable description of the metafield.
            permission_set: Permission settings for the metafield (for example, read/write restrictions).
        Returns:
            API response as a dictionary.
        """
        ...

    def update_variant_option(
        self,
        id: int,
        option_values: List[Any],
        config: Optional[Dict[str, Any]] = None,
        display_name: Optional[str] = None,
        image_url: Optional[str] = None,
        product_id: Optional[int] = None,
        sort_order: Optional[int] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates options for a specific variant.

        Args:
            id: Identifier of the image item. (required)
            option_values:  (required)
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

    def upsert_category_tree(
        self,
    ) -> Dict[str, Any]:
        """Inserts or updates a category tree, depending on its existence.
        Returns:
            API response as a dictionary.
        """
        ...

    def upsert_customer_attribute_values(
        self,
    ) -> Dict[str, Any]:
        """Inserts or updates values for customer attributes, depending on their existence.
        Returns:
            API response as a dictionary.
        """
        ...

