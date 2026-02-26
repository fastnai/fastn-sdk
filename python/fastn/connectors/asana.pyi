"""Fastn Asana connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AsanaConnector:
    """Asana connector ().

    Provides 19 tools.
    """

    def add_project_to_task(
        self,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Associates an existing project with a specific task in the project management connector.

        Args:
            opt_pretty: Optional parameter for pretty printing the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def add_user_to_workspace_(
        self,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a user to a specified workspace in the project management connector.

        Args:
            opt_fields: Optional fields to include in the response.
            opt_pretty: Optional parameter to pretty print the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_project(
        self,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new project in the project management connector.

        Args:
            opt_fields: 
            opt_pretty: Optional parameter for pretty printing the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_project_status(
        self,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new project status within the project management connector.

        Args:
            opt_fields: Comma-separated list of fields to include in the response.
            opt_pretty: Indicates whether to return the response in a pretty-printed format.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_task(
        self,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new task within a project in the project management connector.

        Args:
            opt_fields: Optional fields to include in the response.
            opt_pretty: Optional parameter for pretty printing the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_project(
        self,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified project from the project management connector.

        Args:
            opt_pretty: Optional parameter to format the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_task(
        self,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific task from the project management connector.

        Args:
            opt_pretty: Optional parameter for pretty printing the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def duplicate_task(
        self,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a duplicate of a specific task within the project management connector.

        Args:
            opt_fields: Optional fields to include in the response.
            opt_pretty: Optional parameter to pretty-print the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_project(
        self,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific project from the project management connector.

        Args:
            opt_fields: Specifies which fields to include in the response.
            opt_pretty: Formats the response for better readability.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_project_status(
        self,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the status of a specific project from the project management connector.

        Args:
            opt_fields: Optional fields to include in the response.
            opt_pretty: Optional parameter to pretty-print the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_projects(
        self,
        workspace: str,
        archived: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
        team: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of projects from the specified project management connector.

        Args:
            workspace: The workspace or organization to filter projects on. (required)
            archived: Only return projects whose archived
            limit: The number of objects to return per page.
            offset: The offset for pagination.
            opt_fields: This endpoint returns a resource which excludes some properties by default.
            opt_pretty: Provides the response in a “pretty” format. 
            team: The team to filter projects on.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_task(
        self,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific task from the project management connector.

        Args:
            opt_fields: Specifies which fields to include in the response.  (Asana specific)
            opt_pretty: Specifies whether to format the response as pretty-printed JSON. (Asana specific)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tasks(
        self,
        project: str,
        assignee: Optional[str] = None,
        completed_since: Optional[str] = None,
        limit: Optional[str] = None,
        modified_since: Optional[str] = None,
        offset: Optional[str] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
        section: Optional[str] = None,
        workspace: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of tasks associated with the specified project within the project management connector.

        Args:
            project: The ID of the project to query.  This is a required parameter. (required)
            assignee: The ID of the assignee to filter by.
            completed_since: Filter tasks completed since this date.
            limit: Maximum number of results to return.
            modified_since: Filter tasks modified since this date.
            offset: Offset for pagination.
            opt_fields: Comma-separated list of fields to include in the response.
            opt_pretty: Format the response in a human-readable format.
            section: The ID of the section to query.
            workspace: The ID of the workspace to query.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspace(
        self,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific workspace from the project management connector.

        Args:
            opt_fields: Specifies which fields to include in the response.
            opt_pretty: Indicates whether to format the response for readability.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspace_teams(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of teams associated with a workspace in the project management connector.

        Args:
            limit: Limit the number of results.
            offset: Offset for pagination.
            opt_fields: Specify optional fields to include in the response.
            opt_pretty: Format the response for pretty printing.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspaces(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gathers a list of workspaces available within the project management connector.

        Args:
            limit: Limit the number of results returned.
            offset: Offset for pagination.
            opt_fields: Comma-separated list of fields to include in the response.
            opt_pretty: Flag to enable pretty printing of the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def remove_project_from_task(
        self,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes an association between a project and a specific task in the project management connector.

        Args:
            opt_pretty: Optional parameter for pretty printing the response from Asana V1 API
        Returns:
            API response as a dictionary.
        """
        ...

    def update_project(
        self,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates information for a specific project in the project management connector.

        Args:
            opt_fields: Optional fields to include in the response.
            opt_pretty: Format the response to be more human-readable.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_task(
        self,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of a specific task in the project management connector.

        Args:
            opt_fields: Optional fields to include in the response.
            opt_pretty: Optional parameter for pretty printing the response.
        Returns:
            API response as a dictionary.
        """
        ...

