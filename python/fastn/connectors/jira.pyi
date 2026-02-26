"""Fastn Jira connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class JiraConnector:
    """Jira connector ().

    Provides 16 tools.
    """

    def assign_issue(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Assigns a specified user to an existing issue in the connector, facilitating collaboration and accountability.

        Args:
            accountId: Account ID for the Jira operation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bulk_fetch_changelogs(
        self,
        issueIdsOrKeys: List[Any],
        fieldIds: Optional[List[Any]] = None,
        maxResults: Optional[int] = None,
        nextPageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches changelogs in bulk from the designated connector to gather a comprehensive history of changes made.

        Args:
            issueIdsOrKeys: Array of issue IDs or keys to filter by. (required)
            fieldIds: Array of field IDs to include in the response.
            maxResults: Maximum number of results to return.
            nextPageToken: Token for retrieving the next page of results.
        Returns:
            API response as a dictionary.
        """
        ...

    def bulk_fetch_issues(
        self,
        issueIdsOrKeys: List[Any],
        expand: Optional[List[Any]] = None,
        fields: Optional[List[Any]] = None,
        fieldsByKeys: Optional[bool] = None,
        properties: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Fetches multiple issues in bulk from the connector, streamlining the process of reviewing and managing tasks.

        Args:
            issueIdsOrKeys: Array of issue IDs or keys to retrieve from Jira. (required)
            expand: Array of fields to expand in the Jira API response.
            fields: Array of fields to retrieve from Jira.
            fieldsByKeys: Boolean indicating whether to return fields by keys.
            properties: Array of properties to retrieve from Jira.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_issue(
        self,
        fields: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new issue in the specified project using the connector, allowing for tracking and management of tasks.

        Args:
            fields:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_issue(
        self,
        issueId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific issue from the connector, permanently removing it from the project management system.

        Args:
            issueId: The ID of the Jira issue. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def edit_issue(
        self,
        fields: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Edits an existing issue within the connector to update details such as description, priority, and assignees.

        Args:
            fields: Fields for the Jira issue.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_assignees(
        self,
        project: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of potential assignees for issues within the connector, helping to delegate tasks effectively.

        Args:
            project:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_cloud_id(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the cloud ID associated with the connector, necessary for managing integrations within the cloud environment.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_events(
        self,
    ) -> Dict[str, Any]:
        """Retrieves events from the specified connector to keep track of changes and updates that have occurred.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_issue(
        self,
        issueId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific issue from the connector, providing insights into its status and history.

        Args:
            issueId: ID of the Jira issue (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_issue_statuses(
        self,
        issueKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of possible statuses for issues within the connector, aiding in understanding the current workflow.

        Args:
            issueKey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_projects(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of available projects within the connector, providing an overview of all active and archived projects.
        Returns:
            API response as a dictionary.
        """
        ...

    def link_issues(
        self,
        type: Dict[str, Any],
        inwardIssue: Optional[Dict[str, Any]] = None,
        outwardIssue: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Links two issues together in the connector to signify a relationship or dependency between them.

        Args:
            type: Type of the issue. (required)
            inwardIssue: Details of the inward issue in the Jira request ( either use this or Outward issue ).
            outwardIssue: Details of the outward issue in the Jira request ( either use this or Inward issue ).
        Returns:
            API response as a dictionary.
        """
        ...

    def search(
        self,
        jql: str,
    ) -> Dict[str, Any]:
        """Performs a search in the connector's data to find relevant items or issues based on the specified criteria.

        Args:
            jql: The JQL query to filter Jira issues. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def search_changelogs(
        self,
        expand: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches through changelogs using the specified connector to identify historical changes relevant to a specific query.

        Args:
            expand: Fields to expand in the Jira API response.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_issue_status(
        self,
        transition: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the status of a specific issue in the connector, reflecting its current progress in the management process.

        Args:
            transition: 
        Returns:
            API response as a dictionary.
        """
        ...

