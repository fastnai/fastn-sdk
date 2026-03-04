"""Fastn Bloomreach Engagement connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _BloomreachEngagementAnonymizeCustomerCustomerIds(TypedDict, total=False):
    registered: str

class _BloomreachEngagementExportEventsCustomerIds(TypedDict, total=False):
    registered: str

class _BloomreachEngagementGetCustomerAttributesCustomerIds(TypedDict, total=False):
    registered: str

class _BloomreachEngagementPartialUpdateCatalogItemProperties(TypedDict, total=False):
    manufacturer: str
    name: str

class _BloomreachEngagementTrackEventCustomerIds(TypedDict, total=False):
    email: str

class _BloomreachEngagementTrackEventProperties(TypedDict, total=False):
    price: float
    product_id: str
    product_name: str

class _BloomreachEngagementUpdateCustomerPropertiesCustomerIds(TypedDict, total=False):
    registered: str

class _BloomreachEngagementUpdateCustomerPropertiesProperties(TypedDict, total=False):
    email: str
    first_name: str

class BloomreachEngagementConnector:
    """Bloomreach Engagement connector ().

    Provides 18 tools.
    """

    def bloomreach_engagement_anonymize_customer(
        self,
        customer_ids: _BloomreachEngagementAnonymizeCustomerCustomerIds,
    ) -> Dict[str, Any]:
        """Anonymizes the personal data of a single customer in Bloomreach Engagement. Use this to comply with data privacy requirements (e.g., GDPR right-to-erasure) for an individual customer. This action is irreversible — anonymized data cannot be restored. For bulk anonymization of multiple customers, use bloomreach_engagement_anonymize_customers_bulk instead.

        Args:
            customer_ids: Customer IDs for the Bloomreach Engagement API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_anonymize_customers_bulk(
        self,
        customers: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Anonymizes personal data for multiple customers in bulk within Bloomreach Engagement. Use this to comply with data privacy requirements (e.g., GDPR right-to-erasure) for a large set of customers in a single operation. This action is irreversible — anonymized customer data cannot be restored. For anonymizing a single customer, use bloomreach_engagement_anonymize_customer instead.

        Args:
            customers: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_create_catalog(
        self,
        fields: List[Any],
        name: str,
        is_product_catalog: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new catalog in Bloomreach Engagement for the current project. Use this to set up a new catalog before adding items to it. A catalog with the same name or ID must not already exist. Does not add items to the catalog; use bloomreach_engagement_partial_update_catalog_item or related tools after creation.

        Args:
            fields:  (required)
            name: Name of the entity. (required)
            is_product_catalog: Indicates if it's a product catalog.
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_delete_catalog(
        self,
        catalogId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an entire catalog and all its contents from Bloomreach Engagement. Use this only when the full catalog and all associated items should be removed. This action is irreversible — the catalog and its items cannot be recovered. Do not use this to remove individual catalog items; use bloomreach_engagement_delete_catalog_items instead.

        Args:
            catalogId: ID of the catalog. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_delete_catalog_items(
        self,
        catalogId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes one or more specified items from a catalog in Bloomreach Engagement. Use this when you need to remove specific catalog entries by their IDs. This action is irreversible — deleted items cannot be recovered. Do not use this to delete an entire catalog; use bloomreach_engagement_delete_catalog instead.

        Args:
            catalogId: Catalog ID for Bloomreach Engagement API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_execute_batch_commands(
        self,
        commands: List[Any],
    ) -> Dict[str, Any]:
        """Executes a batch of tracking or data commands against Bloomreach Engagement in a single API call. Use this to send multiple customer or event updates efficiently instead of making individual requests. Each command in the batch is processed as if called independently; failures may be partial. Review batch results carefully, as individual command errors may not fail the entire request.

        Args:
            commands:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_export_events(
        self,
        customer_ids: _BloomreachEngagementExportEventsCustomerIds,
        order: str,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Exports customer event data from Bloomreach Engagement for analysis or reporting. Use this to retrieve historical event records for one or more customers. Triggers a data export operation via POST; does not modify any records. Results may include event types, timestamps, and associated customer identifiers.

        Args:
            customer_ids: Customer IDs for filtering. (required)
            order: Order of results (e.g., asc, desc). (required)
            limit: Limit the number of results.
            skip: Number of results to skip.
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_get_catalog(
        self,
        catalogId: str,
    ) -> Dict[str, Any]:
        """Retrieves metadata for a specific catalog in Bloomreach Engagement, including its name and configuration, identified by catalog ID. Use this to inspect a single catalogs details. Does not return catalog items; use bloomreach_engagement_list_catalog_items for that. Does not modify any data.

        Args:
            catalogId: ID of the catalog. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_get_customer_attributes(
        self,
        customer_ids: _BloomreachEngagementGetCustomerAttributesCustomerIds,
    ) -> Dict[str, Any]:
        """Retrieves attribute values for one or more customers from Bloomreach Engagement. Use this to access customer profile properties such as behavioral signals, preferences, or demographic data for segmentation and targeting. Does not modify any customer data. Do not use this to retrieve event history; use bloomreach_engagement_export_events instead.

        Args:
            customer_ids: Object containing customer IDs. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_get_system_time(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the current server system time from Bloomreach Engagement. Use this to synchronize timestamps or verify server time before time-sensitive tracking operations. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_list_catalog_items(
        self,
        catalogId: str,
        count: Optional[str] = None,
        field: Optional[str] = None,
        order: Optional[str] = None,
        query: Optional[str] = None,
        skip: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all items within a specific catalog in Bloomreach Engagement. Use this to retrieve the full collection of entries for a given catalog ID. Does not modify any data. To retrieve or update a single item, use the appropriate single-item tool instead.

        Args:
            catalogId: ID of the catalog. (required)
            count: Number of results to return.
            field: Specifies the field to filter or sort by.
            order: Sorting order (e.g., asc, desc).
            query: Query string for filtering results.
            skip: Number of results to skip.
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_list_catalogs(
        self,
    ) -> Dict[str, Any]:
        """Lists all catalogs available in the current Bloomreach Engagement project. Use this to discover catalog IDs and names before performing catalog-level operations. Does not return catalog items; use bloomreach_engagement_list_catalog_items for that. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_list_consent_categories(
        self,
    ) -> Dict[str, Any]:
        """Lists all available consent categories defined in Bloomreach Engagement for the current project. Use this to retrieve consent category identifiers and labels needed when managing customer consent preferences. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_list_imports(
        self,
    ) -> Dict[str, Any]:
        """Lists all import jobs and their statuses for the current Bloomreach Engagement project. Use this to monitor the progress or outcome of data import operations. Does not trigger or modify any import job. Returns job identifiers, statuses, and associated metadata.
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_partial_update_catalog_item(
        self,
        catalogId: str,
        itemId: str,
        properties: Optional[_BloomreachEngagementPartialUpdateCatalogItemProperties] = None,
        upsert: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Partially updates specific fields of a single catalog item in Bloomreach Engagement without overwriting the entire record. Use this when only a subset of a catalog items properties need to change. To replace all fields, use a full update operation instead. Modifies the item in place; changes cannot be automatically reversed.

        Args:
            catalogId: ID of the catalog (required)
            itemId: ID of the item (required)
            properties: Properties of the product being updated or created
            upsert: Indicates whether to upsert the data
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_track_event(
        self,
        customer_ids: _BloomreachEngagementTrackEventCustomerIds,
        event_type: str,
        properties: _BloomreachEngagementTrackEventProperties,
        timestamp: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Tracks a new customer event in Bloomreach Engagement by sending event data to the platform. Use this to record customer actions or interactions (e.g., purchases, page views, clicks) associated with a specific customer profile. This writes data to the platform and cannot be automatically undone. Do not use this to retrieve event history; use bloomreach_engagement_export_events instead.

        Args:
            customer_ids: Identifiers for the customer associated with the event (required)
            event_type: Type of event (e.g., purchase, page view) (required)
            properties: Additional properties related to the event (required)
            timestamp: Timestamp of the event
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_update_catalog_name(
        self,
        catalogId: str,
        name: str,
        fields: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the name of an existing catalog in Bloomreach Engagement. Use this to rename a catalog identified by its catalog ID. Only the catalog name is updated; catalog contents and items are not affected. Do not use this to update individual catalog items or other catalog properties.

        Args:
            catalogId: ID of the catalog. (required)
            name: Name of the entity. (required)
            fields: 
        Returns:
            API response as a dictionary.
        """
        ...

    def bloomreach_engagement_update_customer_properties(
        self,
        customer_ids: _BloomreachEngagementUpdateCustomerPropertiesCustomerIds,
        properties: _BloomreachEngagementUpdateCustomerPropertiesProperties,
        update_timestamp: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates or updates properties on a customer profile in Bloomreach Engagement. Use this to set or modify customer attributes such as name, email, or custom properties. If the customer does not exist, a new profile may be created. Does not retrieve customer data; use bloomreach_engagement_get_customer_attributes for that.

        Args:
            customer_ids: Customer IDs for Bloomreach Engagement API. (required)
            properties: Customer properties for Bloomreach Engagement API. (required)
            update_timestamp: Timestamp of the last update.
        Returns:
            API response as a dictionary.
        """
        ...

