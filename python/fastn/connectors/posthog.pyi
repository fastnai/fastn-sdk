"""Fastn Posthog connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _PosthogExecuteQueryQuery(TypedDict, total=False):
    kind: str
    query: str

class PosthogConnector:
    """Posthog connector ().

    Provides 18 tools.
    """

    def posthog_execute_query(
        self,
        projectId: str,
        query: _PosthogExecuteQueryQuery,
        async: Optional[bool] = None,
        client_query_id: Optional[str] = None,
        name: Optional[str] = None,
        refresh: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a custom HogQL or SQL-based query against PostHog event data and returns the query results. Use this tool when you need to run ad-hoc analytical queries against PostHogs data warehouse. Not suitable for retrieving pre-built insights; use posthog_get_insight for those. Requires a valid projectId and a well-formed query body.

        Args:
            projectId: Unique identifier for the project. (required)
            query: Contains the query parameters for the request. (required)
            async: 
            client_query_id: 
            name: Name associated with the request.
            refresh: Refresh interval or flag.
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_find_group(
        self,
        projectId: str,
        group_key: Optional[str] = None,
        group_type_index: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for and retrieves a specific group in a PostHog project based on given filter criteria such as group type and group key. Use this tool when you need to look up a particular group by its properties. Use posthog_list_groups to enumerate all groups without specific search criteria. Requires a valid projectId and relevant search parameters.

        Args:
            projectId: Identifier for the specific project. (required)
            group_key: Unique identifier for the group.
            group_type_index: Index or type of the group.
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_get_event(
        self,
        eventId: str,
        projectId: str,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single PostHog event identified by its event ID within a given project. Use this tool when you need full metadata for one specific event. Use posthog_list_events instead when you need a collection of events. Requires a valid projectId and eventId.

        Args:
            eventId: Unique identifier for the event. (required)
            projectId: Unique identifier for the project. (required)
            format: The format of the response data.
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_get_insight(
        self,
        insightId: str,
        projectId: str,
        format: Optional[str] = None,
        from_dashboard: Optional[str] = None,
        refresh: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single PostHog insight identified by its insight ID, including its query definition, filters, and results. Use this tool when you need full details for one specific insight. Use posthog_list_insights to enumerate multiple insights. Requires a valid projectId and insightId.

        Args:
            insightId: The identifier for the insight. (required)
            projectId: The identifier for the project. (required)
            format: The format of the response or request, e.g., JSON or XML.
            from_dashboard: Indicator whether the request originates from the dashboard.
            refresh: Flag to indicate if data should be refreshed.
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_get_insight_activity(
        self,
        insightId: str,
        projectId: str,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the activity log for a single specific insight in a PostHog project, showing changes and actions taken on that insight over time. Use this tool when you need the audit trail for one known insight. Use posthog_list_insights_activity to get activity across all insights. Requires a valid projectId and insightId.

        Args:
            insightId:  (required)
            projectId:  (required)
            format: 
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_get_organization(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific PostHog organization, including its settings, membership, and configuration. Use this tool when you need metadata for one known organization. Use posthog_list_organizations to enumerate all available organizations. Requires a valid organizationId.

        Args:
            organizationId: The unique identifier for your organization within Posthug. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_get_person(
        self,
        personId: str,
        projectId: str,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed profile information about a single person in a PostHog project, including their properties, distinct IDs, and associated metadata. Use this tool when you need full details for one known person. Use posthog_list_persons to enumerate multiple persons. Requires a valid projectId and personId.

        Args:
            personId: Unique identifier of the person. (required)
            projectId: Unique identifier of the project. (required)
            format: The data format for the request, either CSV or JSON.
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_get_person_activity(
        self,
        personId: str,
        projectId: str,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the activity log for a single specific person in a PostHog project, showing all tracked actions and changes associated with that person over time. Use this tool when you need the audit trail for one known person. Use posthog_list_persons_activity to get activity across all persons. Requires a valid projectId and personId.

        Args:
            personId: Unique identifier of the person. (required)
            projectId: Unique identifier of the project. (required)
            format: The format in which data is to be sent, e.g., 'json' or 'xml'.
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_get_project(
        self,
        organizationId: str,
        projectId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific PostHog project within an organization, including its settings and configuration. Use this tool when you need metadata for one known project. Use posthog_list_projects to enumerate all projects for an organization. Requires a valid organizationId and projectId.

        Args:
            organizationId: The identifier for the organization within Posthug. (required)
            projectId: The identifier for the specific project within Posthug. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_list_events(
        self,
        projectId: str,
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
        """Retrieves a paginated list of events recorded in a PostHog project. Use this tool when you need to browse or enumerate multiple events across a project. Use posthog_get_event instead when you need details for a single known event. Requires a valid projectId.

        Args:
            projectId: The unique identifier of the project. (required)
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

    def posthog_list_feature_flags(
        self,
        projectId: str,
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
        """Retrieves the list of all feature flags defined in a PostHog project. Use this tool when you need to enumerate or inspect feature flags for a project. Requires a valid projectId.

        Args:
            projectId: Identifier for the project. (required)
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

    def posthog_list_groups(
        self,
        group_type_index: str,
        projectId: str,
        cursor: Optional[int] = None,
        search: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all groups defined in a PostHog project. Use this tool when you need to enumerate or browse groups across a project. Use posthog_find_group when searching for a group matching specific criteria. Requires a valid projectId.

        Args:
            group_type_index: Index to specify group type filtering. (required)
            projectId: Unique identifier for the project in Posthug. (required)
            cursor: Pagination cursor for retrieving subsequent pages.
            search: Search string to filter results.
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_list_insights(
        self,
        projectId: str,
        basic: Optional[str] = None,
        created_by: Optional[str] = None,
        format: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        refresh: Optional[str] = None,
        short_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of insights defined in a PostHog project, including their names, filters, and metadata. Use this tool when you need to enumerate or browse insights for a project. Use posthog_get_insight when you need full details for a single known insight. Requires a valid projectId.

        Args:
            projectId: Unique identifier for the project. (required)
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

    def posthog_list_insights_activity(
        self,
        projectId: str,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the aggregated activity log across all insights in a PostHog project. Use this tool when you need a broad audit trail of changes to insights project-wide. Use posthog_get_insight_activity when you need activity for a single specific insight. Requires a valid projectId.

        Args:
            projectId: The unique identifier of the project in Posthug. (required)
            format: The format of the request or response, e.g., JSON or XML.
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_list_organizations(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all PostHog organizations accessible with the current credentials. Use this tool when you need to discover or enumerate available organizations. Use posthog_get_organization when you need full details for a single known organization.

        Args:
            limit: The maximum number of records to return.
            offset: The starting point of the pagination, often used to skip a number of records.
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_list_persons(
        self,
        projectId: str,
        distinct_id: Optional[str] = None,
        email: Optional[str] = None,
        format: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        properties: Optional[List[Any]] = None,
        search: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of persons tracked in a PostHog project, including their properties and distinct IDs. Use this tool when you need to enumerate or browse all persons in a project. Use posthog_get_person when you need full details for a single known person. Requires a valid projectId.

        Args:
            projectId: Identifier for the specific Posthug project. (required)
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

    def posthog_list_persons_activity(
        self,
        projectId: str,
        format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the aggregated activity log across all persons in a PostHog project. Use this tool when you need a broad audit trail of activity for all tracked persons project-wide. Use posthog_get_person_activity when you need activity for a single specific person. Requires a valid projectId.

        Args:
            projectId: The ID of the project within Posthug. (required)
            format: The format in which the response should be returned (e.g., JSON, XML).
        Returns:
            API response as a dictionary.
        """
        ...

    def posthog_list_projects(
        self,
        organizationId: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all PostHog projects associated with a specific organization. Use this tool when you need to enumerate or discover projects within an organization. Use posthog_get_project when you need detailed information for a single known project. Requires a valid organizationId.

        Args:
            organizationId: The unique identifier for the organization within Posthug. (required)
            limit: The maximum number of items to return.
            offset: The number of items to skip before starting to collect the result set.
        Returns:
            API response as a dictionary.
        """
        ...

