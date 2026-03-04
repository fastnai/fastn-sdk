"""Fastn Jira connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _JiraCreateIssueFields(TypedDict, total=False):
    assignee: Dict[str, Any]
    description: Dict[str, Any]
    issuetype: Dict[str, Any]
    project: Dict[str, Any]
    summary: str

class _JiraUpdateIssueStatusTransition(TypedDict, total=False):
    id: str

class JiraConnector:
    """Jira connector ().

    Provides 12 tools.
    """

    def (
        self,
        type: Dict[str, Any],
        inwardIssue: Optional[Dict[str, Any]] = None,
        outwardIssue: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a link between two Jira issues to establish a named relationship such as blocks, is blocked by, relates to, or duplicates. Use this to connect related or dependent issues when you need to express how one issue relates to another. Requires both issue keys and a valid link type. Do not use this to update other issue properties; use Jira_edit_issue instead. This action is reversible by deleting the issue link.

        Args:
            type: Type of the issue. (required)
            inwardIssue: Details of the inward issue in the Jira request ( either use this or Outward issue ).
            outwardIssue: Details of the outward issue in the Jira request ( either use this or Inward issue ).
        Returns:
            API response as a dictionary.
        """
        ...

    def jira_assign_issue(
        self,
        accountId: str,
        issueId: str,
    ) -> Dict[str, Any]:
        """Assigns a specified user to an existing issue in Jira, facilitating collaboration and accountability. Use this when you need to assign an issue to a team member by issue ID. Do not use this to create a new issue; use Jira_create_issue instead.

        Args:
            accountId: Account ID for the Jira operation. (required)
            issueId: ID of the Jira issue. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def jira_bulk_fetch_changelogs(
        self,
        issueIdsOrKeys: List[Any],
        fieldIds: Optional[List[Any]] = None,
        maxResults: Optional[int] = None,
        nextPageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves changelog records in bulk from Jira for multiple issues in a single request, returning the complete history of field changes, status transitions, and other modifications. Use this when you need to audit or analyze change history across multiple issues simultaneously, such as for compliance tracking or reporting on issue evolution over time. Do not use this to retrieve current issue data; use Jira_get_issue instead. Do not use this for a single issues changelog; use Jira_get_issue_changelog instead. This tool is optimized for batch retrieval and is more efficient than fetching changelogs individually.

        Args:
            issueIdsOrKeys: Array of issue IDs or keys to filter by. (required)
            fieldIds: Array of field IDs to include in the response.
            maxResults: Maximum number of results to return.
            nextPageToken: Token for retrieving the next page of results.
        Returns:
            API response as a dictionary.
        """
        ...

    def jira_bulk_fetch_issues(
        self,
        issueIdsOrKeys: List[Any],
        expand: Optional[List[Any]] = None,
        fields: Optional[List[Any]] = None,
        fieldsByKeys: Optional[bool] = None,
        properties: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves multiple Jira issues in bulk using a list of issue IDs or keys in a single request. Use this when you need to fetch several issues at once for batch operations, reporting, or bulk review, which is more efficient than fetching issues individually. Do not use this to retrieve a single issue; use Jira_get_issue instead. Do not use this to search issues by criteria; use Jira_search_issues instead.

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

    def jira_create_issue(
        self,
        fields: _JiraCreateIssueFields,
    ) -> Dict[str, Any]:
        """Creates a new issue in the specified project in Jira, allowing for tracking and management of tasks. Use this when you need to create a new task, bug, feature request, or other issue type in Jira. Do not use this to modify an existing issue; use Jira_edit_issue instead, or to assign users to an issue; use Jira_assign_issue instead.

        Args:
            fields:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def jira_delete_issue(
        self,
        issueId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific issue from Jira, permanently removing it from the project management system. This action is irreversible and cannot be undone. The issue and all related data including issue links, comments, attachments, and audit logs will be permanently deleted. Workflows and automations tied to this issue may also be affected. Use this only when you are certain the issue needs to be completely removed from Jira.

        Args:
            issueId: The ID of the Jira issue. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def jira_get_cloud_id(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the Jira cloud ID required to authenticate and access Jira instances via this connector. Use this to obtain the cloud identifier needed before calling other Jira tools that require cloud authentication.
        Returns:
            API response as a dictionary.
        """
        ...

    def jira_list_events(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of events from Jira, including activity logs, status changes, and system-generated notifications that document changes and updates across your Jira instance. Use this to retrieve all recent events and activity logs from your Jira instance when you need to monitor system-wide changes, track user actions, or understand what has been happening in your projects. Do not use this to retrieve the history of changes to a specific issue; use Jira_get_issue_changelog instead. For real-time webhooks or continuous monitoring, configure webhooks in Jira directly rather than polling this endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def jira_list_issue_statuses(
        self,
        issueKey: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all valid status transitions available for a specific issue in Jira. Use this when you need to see what workflow states an issue can be moved to, helping determine which statuses are valid next steps for that issue. Requires the issue key. Do not use this to change an issues status; use Jira_update_issue_status instead.

        Args:
            issueKey: 
        Returns:
            API response as a dictionary.
        """
        ...

    def jira_list_projects(
        self,
    ) -> Dict[str, Any]:
        """Lists all projects available in Jira. Use this to retrieve all projects across your Jira instance for navigation, filtering, or populating project selection menus in your workflow. Do not use this to retrieve details about a single project; use Jira_get_project instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def jira_search_issues(
        self,
        jql: str,
    ) -> Dict[str, Any]:
        """Searches for Jira issues based on specified criteria such as keywords, project, status, assignee, or custom fields. Use this to find issues matching specific search criteria across your Jira instance. Supports JQL (Jira Query Language) for advanced filtering. Do not use this to retrieve a single issue by ID; use Jira_get_issue instead.

        Args:
            jql: The JQL query to filter Jira issues. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def jira_update_issue_status(
        self,
        issue_key: Optional[str] = None,
        transition: Optional[_JiraUpdateIssueStatusTransition] = None,
    ) -> Dict[str, Any]:
        """Updates the status of a specific issue in Jira by transitioning it to a new workflow state. Use this when you need to move an issue from one status to another (e.g., from To Do to In Progress or from In Progress to Done). Requires the issue key and the target status transition ID. Do not use this to retrieve available statuses; use Jira_list_issue_statuses instead.

        Args:
            issue_key: 
            transition: 
        Returns:
            API response as a dictionary.
        """
        ...

