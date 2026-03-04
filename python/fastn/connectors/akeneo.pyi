"""Fastn Akeneo connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _AkeneoCreateSubscriberContact(TypedDict, total=False):
    technical_email: str

class _AkeneoCreateSubscriptionConfig(TypedDict, total=False):
    secret: Dict[str, Any]
    url: str

class AkeneoConnector:
    """Akeneo connector ().

    Provides 32 tools.
    """

    def akeneo_create_subscriber(
        self,
        contact: _AkeneoCreateSubscriberContact,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new subscriber in the Akeneo event platform, enabling that subscriber to later receive event-driven notifications about product data changes. Use this tool as the first step before creating subscriptions. This action creates a persistent subscriber record. Do not use this tool to create subscriptions; use akeneo_create_subscription after the subscriber is created.

        Args:
            contact: Contact-related details for the entity, such as technical contact information. (required)
            name: The name of the entity being created or modified in Akeneo. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_create_subscription(
        self,
        config: _AkeneoCreateSubscriptionConfig,
        events: List[Any],
        subscriberId: str,
        type: str,
        source: Optional[str] = None,
        subject: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new event subscription for a specific subscriber in the Akeneo event platform. Use this tool when you need to register a subscriber to receive real-time notifications about product information changes or updates. Requires a valid subscriberId. This action creates a persistent subscription record — it cannot be undone without an explicit delete operation. Do not use this tool to create the subscriber itself; use akeneo_create_subscriber first.

        Args:
            config: Configuration details for the subscription, including callback URL and optional secrets. (required)
            events: A list of event names or types that the subscription should listen for (e.g., product.created, product.updated). (required)
            subscriberId: Identifier of an existing subscriber (used for operations that target a specific subscriber). (required)
            type: The type of resource or subscription being created or targeted (e.g., webhook, product, category). (required)
            source: Identifier of the origin or source system within Akeneo that generates the events.
            subject: A short title or subject for the webhook/event subscription or payload context.
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_generate_token(
        self,
        grant_type: Optional[str] = None,
        password: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a new OAuth authentication token for accessing the Akeneo PIM REST API. Use this tool when an access token is required or has expired before making authenticated API calls. This action exchanges credentials for a token via the OAuth v1 endpoint. The generated token grants API access and should be handled securely.

        Args:
            grant_type: 
            password: 
            username: 
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_asset(
        self,
        code: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific asset from the media asset family in Akeneo PIM, identified by its asset code. Use this tool when you need the details of a single media asset by code. Do not use this tool for assets in other asset families; use akeneo_get_asset_from_asset_families for that purpose. Note: this tool is functionally similar to akeneo_get_media_asset and targets the same asset family.

        Args:
            code: The unique code identifying the resource to retrieve via the Akeneo endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_asset_from_asset_families(
        self,
        asset: str,
        assetFamily: str,
    ) -> Dict[str, Any]:
        """Retrieves a single asset from a specified asset family in Akeneo PIM, identified by both the asset family code and the asset code. Use this tool when you need details of a specific asset belonging to any named asset family. Do not use this tool for assets in the hardcoded media family; use akeneo_get_media_asset for that purpose.

        Args:
            asset: The asset identifier or name used to specify which data source asset to retrieve or operate on. (required)
            assetFamily: The asset family or category used to further scope the data source selection. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_association_type(
        self,
        associationTypeCode: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single association type in Akeneo PIM, identified by its association type code. Use this tool when you need to inspect the configuration of a specific product relationship type (e.g., cross-sell, upsell). Do not use this tool to list all association types; use akeneo_list_association_types instead.

        Args:
            associationTypeCode: The code identifying the association type to be used by the Akeneo endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_attribute(
        self,
        attributeCode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific attribute in Akeneo PIM, identified by its attribute code. Use this tool when you need the type, labels, validation rules, and configuration of a single attribute. Do not use this tool to list all attributes; use akeneo_list_attributes instead. Note: this tool targets the same endpoint as akeneo_get_attribute_definition — prefer akeneo_get_attribute_definition when the intent is to inspect structural schema.

        Args:
            attributeCode: 
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_attribute_definition(
        self,
        attributeCode: str,
    ) -> Dict[str, Any]:
        """Retrieves the full definition of a specific attribute in Akeneo PIM, identified by its attribute code. Use this tool when you need structural metadata about an attribute such as its type, validation rules, labels, and configuration. Do not use this tool to list all attributes; use akeneo_list_attributes instead. Note: this tool is functionally similar to akeneo_get_attribute and targets the same endpoint — prefer this tool when the intent is to inspect attribute structure and configuration.

        Args:
            attributeCode: The attribute code identifying the specific data source or attribute to query. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_attribute_option(
        self,
        attributeCode: str,
        optionCode: str,
    ) -> Dict[str, Any]:
        """Retrieves a single, specific option for a given attribute in Akeneo PIM, identified by both the attribute code and the option code. Use this tool when you need the details of one selectable value (e.g., a specific color or size) for a product attribute. Do not use this tool to list all options for an attribute; use akeneo_list_attribute_options instead.

        Args:
            attributeCode: The code of the attribute to target in Akeneo (e.g., 'color', 'size'). (required)
            optionCode: The code of the option for the specified attribute (e.g., a specific value identifier). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_family_variant(
        self,
        familyCode: str,
        familyVariantCode: str,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        with_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific variant within a product family in Akeneo PIM, identified by both the family code and the family variant code. Use this tool when you need the variant axes, levels, and attribute sets for one particular family variant. Do not use this tool to list all variants for a family; use akeneo_list_family_variants instead.

        Args:
            familyCode: Code identifying the family category within the data source. (required)
            familyVariantCode: Code identifying a specific variant within the family. (required)
            limit: Maximum number of items to return.
            page: Page number for pagination.
            with_count: Include the total count of items in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_main_product_image(
        self,
        assetCode: str,
    ) -> Dict[str, Any]:
        """Retrieves the main product image asset from the main_product_image asset family in Akeneo PIM, identified by the asset code. Use this tool when you need the primary image associated with a specific product. Do not use this tool for assets in other asset families; use akeneo_get_asset_from_asset_families or akeneo_get_media_asset for those cases.

        Args:
            assetCode: The unique code identifying the asset to retrieve or operate on. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_media_asset(
        self,
        assetId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single media asset from the media asset family in Akeneo PIM, identified by its asset ID. Use this tool when you need metadata or download information for a specific image or media file linked to a product. Do not use this tool to retrieve assets from other asset families; use akeneo_get_asset_from_asset_families for that purpose.

        Args:
            assetId: The identifier of the asset to target with this request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single product from Akeneo PIM using its product identifier (SKU or legacy ID) via the standard products endpoint. Use this tool when you have a product identifier and need its full attribute values, associations, and metadata. Do not use this tool if you have a UUID; use akeneo_get_product_by_uuid instead. Do not use this tool to list products; use akeneo_list_products instead.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_product_by_id(
        self,
        productId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a single product from Akeneo PIM using its UUID. Use this tool when you have a specific product UUID and need its full details, including attribute values, associations, and metadata. Do not use this tool to search or list products; use akeneo_list_products instead. Note: this endpoint uses the products-uuid API path, so a UUID (not a legacy SKU identifier) is required.

        Args:
            productId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_product_by_uuid(
        self,
        productId: str,
        withAttributeOptions: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a single product from Akeneo PIM using its UUID via the products-uuid endpoint. Use this tool when you have a UUID and need the full details of that specific product, including attribute values and associations. Do not use this tool if you have a legacy SKU identifier; use akeneo_get_product instead. Do not use this tool to list products; use akeneo_list_products instead.

        Args:
            productId: ID of the product. (required)
            withAttributeOptions: 
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_product_model(
        self,
        productModel: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific product model in Akeneo PIM, identified by its product model code. Use this tool when you need the attribute values, associations, and family variant information for a single product model. Do not use this tool to list all product models; use akeneo_list_product_models instead.

        Args:
            productModel: Identifier or slug for the product model resource being accessed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_reference_entity(
        self,
        referenceEntity: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the definition and metadata of a specific reference entity in Akeneo PIM, identified by its reference entity code. Use this tool when you need to inspect the structure of a reference entity, such as its attributes and labels. Do not use this tool to retrieve records within a reference entity; use akeneo_get_reference_entity_record_by_code or akeneo_list_reference_entity_records for that purpose.

        Args:
            referenceEntity: 
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_get_reference_entity_record_by_code(
        self,
        code: Optional[str] = None,
        referenceEntity: Optional[str] = None,
        withAttributeOptions: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a single record from a specific reference entity in Akeneo PIM, identified by both the reference entity code and the record code. Use this tool when you need the attribute values and metadata of one specific reference entity record (e.g., a specific brand or designer). Do not use this tool to list all records; use akeneo_list_reference_entity_records instead.

        Args:
            code: 
            referenceEntity: 
            withAttributeOptions: 
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_association_types(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all association types configured in Akeneo PIM. Use this tool when you need to understand the full set of relationship types that can exist between products (e.g., cross-sell, upsell, substitution). Do not use this tool to retrieve a single association type by code; use akeneo_get_association_type instead.

        Args:
            limit: 
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_attribute_options(
        self,
        attributeCode: str,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        search: Optional[str] = None,
        with_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all available options for a specific attribute in Akeneo PIM, identified by its attribute code. Use this tool when you need to enumerate all selectable values for a select or multi-select attribute (e.g., all available colors or sizes). Do not use this tool to retrieve a single attribute option; use akeneo_get_attribute_option instead.

        Args:
            attributeCode: Code identifying the specific attribute to fetch. (required)
            limit: Maximum number of items to return per page.
            page: Page number of results to retrieve.
            search: 
            with_count: Include the total number of items in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_attributes(
        self,
        attributes: Optional[str] = None,
        convert_measurements: Optional[str] = None,
        limit: Optional[str] = None,
        locales: Optional[str] = None,
        page: Optional[str] = None,
        pagination_type: Optional[str] = None,
        scope: Optional[str] = None,
        search: Optional[str] = None,
        search_after: Optional[str] = None,
        search_locale: Optional[str] = None,
        search_scope: Optional[str] = None,
        with_asset_share_links: Optional[str] = None,
        with_attribute_options: Optional[str] = None,
        with_completenesses: Optional[str] = None,
        with_count: Optional[str] = None,
        with_quality_scores: Optional[str] = None,
        with_root_parent: Optional[str] = None,
        with_workflow_execution_statuses: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all attributes defined in Akeneo PIM. Use this tool when you need to enumerate the full set of product attributes available in the system, including their types and configurations. Do not use this tool to retrieve a single attribute by code; use akeneo_get_attribute or akeneo_get_attribute_definition instead.

        Args:
            attributes: Comma-separated list of attribute codes to filter the response by.
            convert_measurements: Whether to convert measurement units in the response.
            limit: Maximum number of results to return in a single page.
            locales: Comma-separated list of locales to consider for localized data.
            page: Page number for pagination.
            pagination_type: Pagination method to use (e.g., 'page' or 'search_after').
            scope: Scope of data to fetch (e.g., 'channel', 'catalog').
            search: Search query string used to filter results.
            search_after: Cursor value to paginate results after a given item.
            search_locale: Locale used for the search query.
            search_scope: Scope of the search (e.g., 'attributes', 'categories').
            with_asset_share_links: Include asset share links in the response when available.
            with_attribute_options: Include attribute option data in the response.
            with_completenesses: Include completeness information for products.
            with_count: Include total count of matching items in the response.
            with_quality_scores: Include quality scores for items when available.
            with_root_parent: Include root parent information for hierarchical data.
            with_workflow_execution_statuses: Include workflow execution statuses in the response when applicable.
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_brands(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        search: Optional[str] = None,
        search_after: Optional[str] = None,
        with_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all brand records from the brand reference entity in Akeneo PIM. Use this tool when you need to enumerate all brands available in the product information system. Do not use this tool to retrieve a single brand record; use akeneo_get_reference_entity_record_by_code with the brand entity code instead.

        Args:
            limit: Maximum number of items to return per page.
            page: Page number to retrieve.
            search: 
            search_after: 
            with_count: Indicates whether to include the total item count in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_categories(
        self,
        attributes: Optional[str] = None,
        convert_measurements: Optional[str] = None,
        limit: Optional[str] = None,
        locales: Optional[str] = None,
        page: Optional[str] = None,
        pagination_type: Optional[str] = None,
        scope: Optional[str] = None,
        search: Optional[str] = None,
        search_after: Optional[str] = None,
        search_locale: Optional[str] = None,
        search_scope: Optional[str] = None,
        with_asset_share_links: Optional[str] = None,
        with_attribute_options: Optional[str] = None,
        with_completenesses: Optional[str] = None,
        with_count: Optional[str] = None,
        with_quality_scores: Optional[str] = None,
        with_root_parent: Optional[str] = None,
        with_workflow_execution_statuses: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all product categories defined in Akeneo PIM. Use this tool when you need to enumerate the category tree structure used for organizing products. Do not use this tool to retrieve a single category by code.

        Args:
            attributes: Comma-separated attribute codes to include in the response.
            convert_measurements: Whether to convert measurement values to a specified unit.
            limit: Maximum number of results to return per page.
            locales: Comma-separated locale codes to apply for localization.
            page: Page number to retrieve.
            pagination_type: Pagination style to use for the results.
            scope: Scope filter for the query.
            search: Search query to filter results.
            search_after: Cursor-like value for pagination (search_after).
            search_locale: Locale used for search matching.
            search_scope: Scope used for the search.
            with_asset_share_links: Include asset share links in the response.
            with_attribute_options: Include attribute options in the response.
            with_completenesses: Include completeness information in the response.
            with_count: Include the total count of results in the response.
            with_quality_scores: Include quality scores for attributes.
            with_root_parent: Include the root parent information in the response.
            with_workflow_execution_statuses: Include workflow execution statuses in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_channels(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        with_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all distribution channels configured in Akeneo PIM. Use this tool when you need to discover available channels (e.g., e-commerce, print, mobile) and their associated locales, currencies, and category trees. Do not use this tool to retrieve information about a single channel.

        Args:
            limit: 
            page: 
            with_count: 
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_family_variants(
        self,
        familyCode: str,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        with_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all variants belonging to a specific product family in Akeneo PIM, identified by the family code. Use this tool when you need to enumerate the variant axes and levels defined for a product family. Do not use this tool to retrieve a single family variant; use akeneo_get_family_variant instead.

        Args:
            familyCode: Unique code identifying the family of data sources to retrieve. (required)
            limit: Maximum number of items to return.
            page: Page number for pagination.
            with_count: Flag to include total item count in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_measurement_families(
        self,
    ) -> Dict[str, Any]:
        """Lists all measurement families defined in Akeneo PIM. Use this tool when you need to discover or enumerate how product dimensions, weights, and other measurable attributes are grouped and categorized. Returns the full collection of measurement families with their units. Do not use this tool to retrieve a single measurement family by ID.
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_product_families(
        self,
        limit: str,
        page: str,
        with_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all product families defined in Akeneo PIM. Use this tool when you need to enumerate the groupings that define which attributes and attribute requirements apply to products. Do not use this tool to retrieve a single product family or its variants; use akeneo_get_family_variant or akeneo_list_family_variants for variant-level details.

        Args:
            limit: Maximum number of items to return. (required)
            page: Page number for pagination. (required)
            with_count: Whether to include the total count of items in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_product_models(
        self,
        attributes: Optional[str] = None,
        convert_measurements: Optional[str] = None,
        limit: Optional[str] = None,
        locales: Optional[str] = None,
        page: Optional[str] = None,
        pagination_type: Optional[str] = None,
        scope: Optional[str] = None,
        search: Optional[str] = None,
        search_after: Optional[str] = None,
        search_locale: Optional[str] = None,
        search_scope: Optional[str] = None,
        with_asset_share_links: Optional[str] = None,
        with_attribute_options: Optional[str] = None,
        with_completenesses: Optional[str] = None,
        with_count: Optional[str] = None,
        with_quality_scores: Optional[str] = None,
        with_root_parent: Optional[str] = None,
        with_workflow_execution_statuses: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all product models in Akeneo PIM. Use this tool when you need to enumerate product models across the catalog, which serve as the parent level in a product variant hierarchy. Do not use this tool to retrieve a single product model; use akeneo_get_product_model instead.

        Args:
            attributes: List of attribute codes to include in the response.
            convert_measurements: Flag to convert measurement units in the results.
            limit: Maximum number of results to return per page.
            locales: Locale codes to localize the results.
            page: Page number to retrieve.
            pagination_type: Pagination strategy to use (e.g., 'page', 'search_after').
            scope: Resource scope to query (e.g., 'admin', 'system').
            search: Search query string.
            search_after: Cursor for 'search after' pagination.
            search_locale: Locale code for search.
            search_scope: Scope for the search operation.
            with_asset_share_links: Include asset share links in the response.
            with_attribute_options: Include attribute option information in the response.
            with_completenesses: Include completeness information in the response.
            with_count: Include the total count of results in the response.
            with_quality_scores: Include quality scores in the response.
            with_root_parent: Include root parent information in the results.
            with_workflow_execution_statuses: Include workflow execution statuses in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_products(
        self,
        attributes: Optional[str] = None,
        convert_measurements: Optional[str] = None,
        limit: Optional[str] = None,
        locales: Optional[str] = None,
        page: Optional[str] = None,
        pagination_type: Optional[str] = None,
        scope: Optional[str] = None,
        search: Optional[str] = None,
        search_after: Optional[str] = None,
        search_locale: Optional[str] = None,
        search_scope: Optional[str] = None,
        with_asset_share_links: Optional[str] = None,
        with_attribute_options: Optional[str] = None,
        with_completenesses: Optional[str] = None,
        with_count: Optional[str] = None,
        with_quality_scores: Optional[str] = None,
        with_root_parent: Optional[str] = None,
        with_workflow_execution_statuses: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all products in Akeneo PIM using the UUID-based products endpoint. Use this tool when you need to enumerate or paginate through the full product catalog. Returns products identified by UUID. Do not use this tool to retrieve a single product; use akeneo_get_product_by_id or akeneo_get_product_by_uuid instead.

        Args:
            attributes: List of attribute codes to include in results.
            convert_measurements: Convert measurement units in the response if applicable.
            limit: Maximum number of results to return.
            locales: Comma-separated locale codes to filter results by locale.
            page: Page number for paginated results.
            pagination_type: Pagination strategy (e.g., page, scroll).
            scope: Scope filter for the request (e.g., 'system', 'catalog').
            search: Search query string used to filter results.
            search_after: Cursor for pagination using a search after token.
            search_locale: Locale to be used for the search, if relevant.
            search_scope: The scope of the search (e.g., global, local).
            with_asset_share_links: Whether to include links to asset shares in the response.
            with_attribute_options: Include possible options for attributes in the response.
            with_completenesses: Return completeness scores for items where available.
            with_count: Return the total count of matching items in the response.
            with_quality_scores: Return quality scores of items when available.
            with_root_parent: Include information about the root parent in results when applicable.
            with_workflow_execution_statuses: Include statuses of workflow executions in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_reference_entities(
        self,
        attributes: Optional[str] = None,
        convert_measurements: Optional[str] = None,
        limit: Optional[str] = None,
        locales: Optional[str] = None,
        page: Optional[str] = None,
        pagination_type: Optional[str] = None,
        scope: Optional[str] = None,
        search: Optional[str] = None,
        search_after: Optional[str] = None,
        search_locale: Optional[str] = None,
        search_scope: Optional[str] = None,
        with_asset_share_links: Optional[str] = None,
        with_attribute_options: Optional[str] = None,
        with_completenesses: Optional[str] = None,
        with_count: Optional[str] = None,
        with_quality_scores: Optional[str] = None,
        with_root_parent: Optional[str] = None,
        with_workflow_execution_statuses: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all reference entities defined in Akeneo PIM. Use this tool when you need to discover the available reference entities (e.g., brand, designer, material) and their structural definitions. Do not use this tool to retrieve a single reference entity; use akeneo_get_reference_entity instead.

        Args:
            attributes: Specific attributes to include or filter on in the results.
            convert_measurements: Convert measurement units in the results if applicable.
            limit: Maximum number of results to return.
            locales: Locales to consider for localized data.
            page: Page number to retrieve.
            pagination_type: Type of pagination to apply (e.g., page-based, offset-based).
            scope: Scope to narrow the query to a particular subset.
            search: Query string used to filter results.
            search_after: Pagination cursor-based parameter for results after a given point.
            search_locale: Locale to use for the search operation.
            search_scope: Scope of the search within the data.
            with_asset_share_links: Include asset share links in the response.
            with_attribute_options: Include the options for attributes in the response.
            with_completenesses: Include completeness data in the results.
            with_count: Include the total count of matching items in the response.
            with_quality_scores: Include quality score metrics in the results.
            with_root_parent: Include root parent information in the results.
            with_workflow_execution_statuses: Include statuses of workflow executions in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def akeneo_list_reference_entity_records(
        self,
        referenceEntities: Optional[str] = None,
        search_after: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all records belonging to a specific reference entity in Akeneo PIM, identified by its reference entity code. Use this tool when you need to enumerate all records within a reference entity (e.g., all brand records). Do not use this tool to retrieve a single record by code; use akeneo_get_reference_entity_record_by_code instead.

        Args:
            referenceEntities: 
            search_after: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_update_env_config(
        self,
        data: Optional[Dict[str, Any]] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates one or more environment configuration settings in the Fastn platform via a GraphQL mutation. Use this tool when you need to modify system-level environment parameters or integration configuration values. This is a write operation that directly alters configuration state and may affect system behavior for all users. Confirm the intended changes before calling this tool, as modifications may be difficult to reverse without knowing the prior state. Do not use this tool to create new configurations — use fastn_add_env_configs instead.

        Args:
            data: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

