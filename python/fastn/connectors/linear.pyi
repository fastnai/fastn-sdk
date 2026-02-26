"""Fastn Linear connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class LinearConnector:
    """Linear connector ().

    Provides 8 tools.
    """

    def create_issue(
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
        """Creates a new issue in the project management system.

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

    def delete_issue(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Deletes a specified issue from the project management system.

        Args:
            id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_issues(
        self,
        limit: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Retrieves all issues from the project management system.

        Args:
            limit: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_issue(
        self,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific issue from the project management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_issue_history(
        self,
        issueId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the history of changes made to a specific issue in the project management system.

        Args:
            issueId: The ID of the Linear issue.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user(
        self,
    ) -> Dict[str, Any]:
        """Fetches user information from the project management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
        after: str,
        first: str,
    ) -> Dict[str, Any]:
        """Fetches a list of users from the project management system.

        Args:
            after:  (required)
            first:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_issue(
        self,
        id: Optional[str] = None,
        input: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing issue in the project management system.

        Args:
            id: 
            input: 
        Returns:
            API response as a dictionary.
        """
        ...

