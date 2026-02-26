"""Fastn Bloomreach engagement connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BloomreachEngagementConnector:
    """Bloomreach engagement connector ().

    Provides 18 tools.
    """

    def add_event(
        self,
        customer_ids: Dict[str, Any],
        event_type: str,
        properties: Dict[str, Any],
        timestamp: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a new event in the specified connector's system.

        Args:
            customer_ids: Identifiers for the customer associated with the event (required)
            event_type: Type of event (e.g., purchase, page view) (required)
            properties: Additional properties related to the event (required)
            timestamp: Timestamp of the event
        Returns:
            API response as a dictionary.
        """
        ...

    def anonymize_customer(
        self,
        customer_ids: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Anonymizes a single customer’s information in the specified connector's database.

        Args:
            customer_ids: Customer IDs for the Bloomreach Engagement API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def anonymize_customers_in_bulk(
        self,
        customers: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Anonymizes multiple customers’ information in bulk within the specified connector's system.

        Args:
            customers: 
        Returns:
            API response as a dictionary.
        """
        ...

    def batch_commands(
        self,
        commands: List[Any],
    ) -> Dict[str, Any]:
        """Executes a batch of commands in the specified connector's system to optimize performance.

        Args:
            commands:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_catalog(
        self,
        fields: List[Any],
        name: str,
        is_product_catalog: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new catalog within the specified connector's framework.

        Args:
            fields:  (required)
            name: Name of the entity. (required)
            is_product_catalog: Indicates if it's a product catalog.
        Returns:
            API response as a dictionary.
        """
        ...

    def customer_attributes(
        self,
        customer_ids: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Fetches customer attributes stored within the specified connector's system.

        Args:
            customer_ids: Object containing customer IDs. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_catalog(
        self,
        catalogId: str,
    ) -> Dict[str, Any]:
        """Deletes an entire catalog from the specified connector's system.

        Args:
            catalogId: ID of the catalog. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_catalog_items(
        self,
        catalogId: str,
    ) -> Dict[str, Any]:
        """Removes specified items from a catalog in the connector's environment.

        Args:
            catalogId: Catalog ID for Bloomreach Engagement API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def export_events(
        self,
        customer_ids: Dict[str, Any],
        order: str,
        limit: Optional[int] = None,
        skip: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Exports event data from the specified connector for further analysis.

        Args:
            customer_ids: Customer IDs for filtering. (required)
            order: Order of results (e.g., asc, desc). (required)
            limit: Limit the number of results.
            skip: Number of results to skip.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_catalog_items(
        self,
        count: Optional[str] = None,
        field: Optional[str] = None,
        order: Optional[str] = None,
        query: Optional[str] = None,
        skip: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches items listed within a specific catalog in the specified connector's system.

        Args:
            count: Number of results to return.
            field: Specifies the field to filter or sort by.
            order: Sorting order (e.g., asc, desc).
            query: Query string for filtering results.
            skip: Number of results to skip.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_catalog_name(
        self,
        catalogId: str,
    ) -> Dict[str, Any]:
        """Retrieves the name of a specific catalog within the specified connector's environment.

        Args:
            catalogId: ID of the catalog. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_catalogs(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of catalogs available in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_consent_categories(
        self,
    ) -> Dict[str, Any]:
        """Obtains the available consent categories from the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_system_time(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the current system time from the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_imports(
        self,
    ) -> Dict[str, Any]:
        """Lists all import jobs and their statuses in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def partial_update_catalog_item(
        self,
        properties: Optional[Dict[str, Any]] = None,
        upsert: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Partially updates a catalog item in the specified connector's catalog.

        Args:
            properties: Properties of the product being updated or created
            upsert: Indicates whether to upsert the data
        Returns:
            API response as a dictionary.
        """
        ...

    def update_catalog_name(
        self,
        name: str,
        fields: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the name of an existing catalog in the specified connector's structure.

        Args:
            name: Name of the entity. (required)
            fields: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_customer_properties(
        self,
        customer_ids: Dict[str, Any],
        properties: Dict[str, Any],
        update_timestamp: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates the properties associated with a customer in the specified connector's system.

        Args:
            customer_ids: Customer IDs for Bloomreach Engagement API. (required)
            properties: Customer properties for Bloomreach Engagement API. (required)
            update_timestamp: Timestamp of the last update.
        Returns:
            API response as a dictionary.
        """
        ...

