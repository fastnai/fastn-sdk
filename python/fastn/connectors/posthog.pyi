"""Fastn Posthog connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class PosthogConnector:
    """Posthog connector ().

    Provides 18 tools.
    """

    def execute_query(
        self,
        query: Dict[str, Any],
        async: Optional[bool] = None,
        client_query_id: Optional[str] = None,
        name: Optional[str] = None,
        refresh: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a custom query on the database using the relevant connector.

        Args:
            query: Contains the query parameters for the request. (required)
            async: 
            client_query_id: 
            name: Name associated with the request.
            refresh: Refresh interval or flag.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_event(
        self,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific event using the relevant connector.

        Args:
            format: The format of the response data.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_events(
        self,
        after: Optional[str] = None,
        before: Optional[str] = None,
        distinct_id: Optional[int] = None,
        event: Optional[str] = None,
        format: Optional[str] = None,
        key: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        person_id: Optional[int] = None,
        properties: Optional[List[Any]] = None,
        select: Optional[List[Any]] = None,
        where: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of events recorded in the system using the relevant connector.

        Args:
            after: Filter for records created after this timestamp.
            before: Filter for records created before this timestamp.
            distinct_id: Unique identifier for a specific user or entity.
            event: The name of the event to query.
            format: The format of the response data.
            key: The API key for the request.
            limit: Limits the number of results returned.
            offset: The starting point for result pagination.
            person_id: Identifier for the person associated with the event.
            properties: 
            select: Specific fields to select from the data.
            where: Conditions to filter the query results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_feature_flags(
        self,
        active: Optional[str] = None,
        created_by_id: Optional[str] = None,
        evaluation_runtime: Optional[str] = None,
        excluded_properties: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        search: Optional[str] = None,
        tags: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves feature flags present in the system using the relevant connector.

        Args:
            active: Filter by active status.
            created_by_id: ID of the creator of the item.
            evaluation_runtime: Specify evaluation runtime environment.
            excluded_properties: Properties to exclude from the response.
            limit: Maximum number of items to retrieve.
            offset: Number of items to skip before starting to collect the result set.
            search: Search term for filtering results.
            tags: Tags associated with the items.
            type: Type of the item.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_groups(
        self,
        group_type_index: str,
        cursor: Optional[int] = None,
        search: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of groups within the system using the relevant connector.

        Args:
            group_type_index: Index to specify group type filtering. (required)
            cursor: Pagination cursor for retrieving subsequent pages.
            search: Search string to filter results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_groups_find(
        self,
        group_key: Optional[str] = None,
        group_type_index: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Finds groups based on specific criteria using the relevant connector.

        Args:
            group_key: Unique identifier for the group.
            group_type_index: Index or type of the group.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_insight(
        self,
        format: Optional[str] = None,
        from_dashboard: Optional[str] = None,
        refresh: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific insight using the relevant connector.

        Args:
            format: The format of the response or request, e.g., JSON or XML.
            from_dashboard: Indicator whether the request originates from the dashboard.
            refresh: Flag to indicate if data should be refreshed.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_insight_activity(
        self,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves activity logs for a specific insight using the relevant connector.

        Args:
            format: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_insights(
        self,
        basic: Optional[str] = None,
        created_by: Optional[str] = None,
        format: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        refresh: Optional[str] = None,
        short_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves insights generated by the system using the relevant connector.

        Args:
            basic: Basic parameter for additional identification or credentials.
            created_by: Identifier of the creator.
            format: Format specification for the request or response.
            limit: Maximum number of items to retrieve.
            offset: Number of items to skip before starting to collect the result set.
            refresh: Flag indicating whether to refresh the data.
            short_id: Short identifier for specific resources.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_insights_activity(
        self,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves activity logs for insights in the system using the relevant connector.

        Args:
            format: The format of the request or response, e.g., JSON or XML.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organization(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific organization using the relevant connector.

        Args:
            organizationId: The unique identifier for your organization within Posthug. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organizations(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of organizations in the system using the relevant connector.

        Args:
            limit: The maximum number of records to return.
            offset: The starting point of the pagination, often used to skip a number of records.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_person(
        self,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific person using the relevant connector.

        Args:
            format: The data format for the request, either CSV or JSON.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_person_activity(
        self,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves activity logs for a specific person using the relevant connector.

        Args:
            format: The format in which data is to be sent, e.g., 'json' or 'xml'.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_persons(
        self,
        distinct_id: Optional[str] = None,
        email: Optional[str] = None,
        format: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        properties: Optional[List[Any]] = None,
        search: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of persons in the system using the relevant connector.

        Args:
            distinct_id: Unique identifier for the user or entity.
            email: Email address of the user or target entity.
            format: The response format.
            limit: Maximum number of records to retrieve.
            offset: Number of records to skip before starting to collect the result set.
            properties: 
            search: Search term or keyword.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_persons_activity(
        self,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves activity logs for all persons using the relevant connector.

        Args:
            format: The format in which the response should be returned (e.g., JSON, XML).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_project(
        self,
        organizationId: str,
        projectId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific project using the relevant connector.

        Args:
            organizationId: The identifier for the organization within Posthug. (required)
            projectId: The identifier for the specific project within Posthug. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_projects(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of projects associated with the organization using the relevant connector.

        Args:
            limit: The maximum number of items to return.
            offset: The number of items to skip before starting to collect the result set.
        Returns:
            API response as a dictionary.
        """
        ...

