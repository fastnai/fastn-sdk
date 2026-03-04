"""Fastn Linear connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _LinearUpdateIssueInput(TypedDict, total=False):
    assigneeId: str
    cycleId: str
    description: str
    dueDate: str
    estimate: int
    labelIds: List[Any]
    parentId: str
    priority: int
    projectId: str
    stateId: str
    teamId: str
    title: str

class LinearConnector:
    """Linear connector ().

    Provides 8 tools.
    """

    def linear_create_issue(
        self,
        teamId: str,
        title: str,
        assigneeId: Optional[str] = None,
        cycleId: Optional[str] = None,
        description: Optional[str] = None,
        dueDate: Optional[str] = None,
        estimate: Optional[int] = None,
        labelIds: Optional[List[Any]] = None,
        parentId: Optional[str] = None,
        priority: Optional[int] = None,
        projectId: Optional[str] = None,
        stateId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new issue in the project management system. Use this when you need to create a new task or bug report with a title, description, and optional assignee and project. Do not use this to update an existing issue; use linear_update_issue instead. This may trigger notifications to assigned team members and create an audit log entry.

        Args:
            teamId: ID of the team the issue belongs to. (required)
            title: Title of the issue. (required)
            assigneeId: ID of the issue's assignee.
            cycleId: ID of the cycle the issue belongs to.
            description: Description of the issue.
            dueDate: Due date of the issue (ISO 8601 format).
            estimate: Estimate of the issue's effort.
            labelIds: Array of label IDs to associate with the issue.
            parentId: ID of the parent issue (if applicable).
            priority: Priority of the issue.
            projectId: ID of the project the issue belongs to.
            stateId: ID of the issue's state.
        Returns:
            API response as a dictionary.
        """
        ...

    def linear_delete_issue(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Deletes a specified issue from the project management system. This action permanently removes the issue and cannot be undone. Use this to remove an issue by its ID when the issue is no longer needed or was created in error.

        Args:
            id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linear_get_issue(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific issue from the project management system. Use this to fetch a single issue by its ID to view its full details including title, description, status, assignee, priority, labels, and timestamps. Do not use this to list multiple issues; use linear_list_issues instead.

        Args:
            id: ID of the resource.  Specific meaning depends on the Linear API endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linear_get_issue_history(
        self,
        issueId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the history of changes made to a specific issue in the project management system. Use this to view all changes to an issue, including comments, status changes, assignee changes, and other modifications. This is useful for auditing, understanding how an issue evolved, or viewing activity timelines. Do not use this to retrieve the current state of an issue; use linear_get_issue instead. This tool only retrieves data and does not modify any records.

        Args:
            issueId: The ID of the Linear issue.
        Returns:
            API response as a dictionary.
        """
        ...

    def linear_get_user(
        self,
    ) -> Dict[str, Any]:
        """Retrieves detailed profile information for a specific Linear user by their user ID, including their name, email, and account details. Use this when you need information about a single known user. Do not use this to list all users in the workspace; use linear_list_users instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def linear_list_issues(
        self,
        limit: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Lists all issues in the Linear workspace across all teams and projects. Use this to retrieve a complete list of issues for display, bulk review, or reporting. Do not use this to retrieve details of a single issue; use linear_get_issue instead. For filtered or targeted searches, consider filtering parameters if supported.

        Args:
            limit: 
        Returns:
            API response as a dictionary.
        """
        ...

    def linear_list_users(
        self,
        after: str,
        first: str,
    ) -> Dict[str, Any]:
        """Lists all active users in the Linear workspace. Use this to retrieve user names and IDs for task assignment, populating assignee dropdowns, or identifying team members. Do not use this to retrieve details about a single user; use linear_get_user instead.

        Args:
            after:  (required)
            first:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def linear_update_issue(
        self,
        id: Optional[str] = None,
        input: Optional[_LinearUpdateIssueInput] = None,
    ) -> Dict[str, Any]:
        """Updates an existing issue in the project management system. Use this to modify issue properties such as title, description, status, assignee, priority, or labels. Do not use this to create a new issue; use linear_create_issue instead. This action may trigger notifications to watchers and update related activity logs.

        Args:
            id: 
            input: 
        Returns:
            API response as a dictionary.
        """
        ...

