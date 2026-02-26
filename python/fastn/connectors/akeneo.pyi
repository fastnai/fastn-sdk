"""Fastn Akeneo connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AkeneoConnector:
    """Akeneo connector ().

    Provides 24 tools.
    """

    def generate_token(
        self,
        grant_type: Optional[str] = None,
        password: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a new authentication token for access to the API.

        Args:
            grant_type: 
            password: 
            username: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_asset(
        self,
        code: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific asset linked to a product or category.

        Args:
            code: The unique code identifying the resource to retrieve via the Akeneo endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_asset_from_asset_families(
        self,
        asset: str,
        assetFamily: str,
    ) -> Dict[str, Any]:
        """Retrieves an asset associated with specific asset families.

        Args:
            asset: The asset identifier or name used to specify which data source asset to retrieve or operate on. (required)
            assetFamily: The asset family or category used to further scope the data source selection. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_attribute(
        self,
        attributeCode: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details for a specific attribute in the system.

        Args:
            attributeCode: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_attribute_definition(
        self,
        attributeCode: str,
    ) -> Dict[str, Any]:
        """Gets the definition details for a specific attribute in the system.

        Args:
            attributeCode: The attribute code identifying the specific data source or attribute to query. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_attribute_options(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        search: Optional[str] = None,
        with_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets available options for a particular attribute in the inventory.

        Args:
            limit: Maximum number of items to return per page.
            page: Page number of results to retrieve.
            search: 
            with_count: Include the total number of items in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_attributes(
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
        """Fetches a list of attributes associated with products in the system.

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

    def get_brands(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        search: Optional[str] = None,
        search_after: Optional[str] = None,
        with_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains a list of brands available in the inventory.

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

    def get_categories(
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
        """Gets the categories available for products in the inventory.

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

    def get_channels(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        with_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets a list of channels available for product distribution.

        Args:
            limit: 
            page: 
            with_count: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_family_variant(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        with_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets the family variant details for a specific product family.

        Args:
            limit: Maximum number of items to return.
            page: Page number for pagination.
            with_count: Include the total count of items in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_family_variants(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        with_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains the family variants associated with a specific product family.

        Args:
            limit: Maximum number of items to return.
            page: Page number for pagination.
            with_count: Flag to include total item count in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_main_product_image(
        self,
        assetCode: str,
    ) -> Dict[str, Any]:
        """Fetches the main image associated with a specific product.

        Args:
            assetCode: The unique code identifying the asset to retrieve or operate on. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific product from the inventory.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_by_uuid(
        self,
        productId: str,
    ) -> Dict[str, Any]:
        """Retrieves a product using its unique identifier (UUID) in the system.

        Args:
            productId: ID of the product. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_families(
        self,
        limit: str,
        page: str,
        with_count: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all product families in the inventory.

        Args:
            limit: Maximum number of items to return. (required)
            page: Page number for pagination. (required)
            with_count: Whether to include the total count of items in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_model(
        self,
        productModel: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific product model from the database.

        Args:
            productModel: Identifier or slug for the product model resource being accessed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product_models(
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
        """Fetches product models associated with a specific product.

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

    def get_products(
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
        """Obtains a list of products available in the system.

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

    def get_reference_entities(
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
        """Retrieves a list of reference entities used within the system.

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

    def get_reference_entity(
        self,
        referenceEntity: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details for a specific reference entity.

        Args:
            referenceEntity: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_reference_entity_record_by_code(
        self,
        code: Optional[str] = None,
        referenceEntity: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a reference entity record using its code.

        Args:
            code: 
            referenceEntity: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_reference_entity_records(
        self,
        search_after: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves records of a specific reference entity.

        Args:
            search_after: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_env_config(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the environment configuration settings for the system.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

