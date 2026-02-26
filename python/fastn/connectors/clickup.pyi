"""Fastn Clickup connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ClickupConnector:
    """Clickup connector ().

    Provides 14 tools.
    """

    def create_folder(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new folder in the desired workspace using the specified connector.

        Args:
            name: Name of the item/object in Clickup. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_list(
        self,
        name: str,
        assignee: Optional[int] = None,
        content: Optional[str] = None,
        due_date: Optional[int] = None,
        due_date_time: Optional[bool] = None,
        include_markdown_description: Optional[bool] = None,
        priority: Optional[int] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new task list in the specified workspace using the connector.

        Args:
            name: The name of the task. (required)
            assignee: The ID of the user assigned to the task.
            content: The content or description of the task.
            due_date: The due date of the task (timestamp).
            due_date_time: Indicates whether to use a date and time for the due date.
            include_markdown_description: Indicates whether the description should be rendered as Markdown.
            priority: The priority level of the task.
            status: The status of the task.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_task(
        self,
        assignees: Optional[List[Any]] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        priority: Optional[int] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new task within a selected list in the specified connector.

        Args:
            assignees: 
            description: 
            name: 
            priority: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_folder(
        self,
        folderId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified folder from the workspace in the connector environment.

        Args:
            folderId: The ID of the folder to interact with in Clickup. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_list(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Deletes a selected task list from the workspace in the connector context.

        Args:
            listId: The ID of the Clickup list. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_folder(
        self,
        folderId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific folder in the connector's workspace.

        Args:
            folderId: The ID of the Clickup folder. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_folders(
        self,
        archived: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all folders within a specified workspace in the connector environment.

        Args:
            archived: Filter by archived status (e.g., true, false).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_list(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific task list in the connector's environment.

        Args:
            listId: ID of the Clickup list. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_lists(
        self,
        archived: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all task lists within the connector's workspace.

        Args:
            archived: Whether to include archived items.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_spaces(
        self,
        team_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of spaces available in the context of the connector.

        Args:
            team_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_teams(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of teams within the specified connector's workspace.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspaces(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of workspaces in the specified connector context.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_folder(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the properties of an existing folder within the connector's workspace.

        Args:
            name: The name of the item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_list(
        self,
        assignee: int,
        content: str,
        due_date: int,
        due_date_time: bool,
        name: str,
        priority: int,
        status: str,
        include_markdown_description: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates an existing task list within the workspace using the connector.

        Args:
            assignee: The ID of the user assigned to the task. (required)
            content: The content or description of the task. (required)
            due_date: The due date of the task (timestamp). (required)
            due_date_time: Indicates whether to include the due date and time. (required)
            name: The name of the task. (required)
            priority: The priority level of the task. (required)
            status: The status of the task. (required)
            include_markdown_description: Indicates whether the description should be parsed as Markdown.
        Returns:
            API response as a dictionary.
        """
        ...

