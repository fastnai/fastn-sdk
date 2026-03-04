"""Fastn Clickup connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class ClickupConnector:
    """Clickup connector ().

    Provides 14 tools.
    """

    def clickup_create_folder(
        self,
        name: str,
        spaceId: str,
    ) -> Dict[str, Any]:
        """Creates a new folder within a specified ClickUp space. Use this when you need to organize lists under a new folder inside an existing space. Do not use this to create spaces, lists, or tasks — use clickup_list_spaces, clickup_create_list, or clickup_create_task instead. Creating a folder is a persistent action; the folder must be explicitly deleted to remove it.

        Args:
            name: Name of the item/object in Clickup. (required)
            spaceId: The ID of the space in Clickup. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickup_create_list(
        self,
        folderId: str,
        name: str,
        assignee: Optional[int] = None,
        content: Optional[str] = None,
        due_date: Optional[int] = None,
        due_date_time: Optional[bool] = None,
        include_markdown_description: Optional[bool] = None,
        priority: Optional[int] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new task list inside a specified ClickUp folder. Use this when you need to add a new list to an existing folder to organize tasks. Do not use this to create folders or tasks — use clickup_create_folder or clickup_create_task instead. Creating a list is a persistent action; the list must be explicitly deleted to remove it.

        Args:
            folderId: The ID of the folder where the task will be created. (required)
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

    def clickup_create_task(
        self,
        assignees: Optional[List[Any]] = None,
        description: Optional[str] = None,
        list_id: Optional[str] = None,
        name: Optional[str] = None,
        priority: Optional[int] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new task within a specified ClickUp list. Use this when you need to add a task to an existing list, providing details such as task name, description, assignees, due date, and priority. Do not use this to create lists or folders — use clickup_create_list or clickup_create_folder instead. Creating a task is a persistent action that cannot be undone without explicitly deleting the task.

        Args:
            assignees: 
            description: 
            list_id: 
            name: 
            priority: 
            status: 
        Returns:
            API response as a dictionary.
        """
        ...

    def clickup_delete_folder(
        self,
        folderId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified folder from a ClickUp workspace, including all lists and tasks contained within it. Use this only when the folder and all its contents need to be removed. Do not use this to delete individual lists or tasks — use clickup_delete_list or task-specific tools instead. This action is irreversible: the folder and all nested content will be permanently deleted and cannot be recovered.

        Args:
            folderId: The ID of the folder to interact with in Clickup. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickup_delete_list(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified task list from a ClickUp workspace. Use this only when a list and all its contents need to be removed. Do not use this to delete folders or tasks — use clickup_delete_folder or task-specific tools instead. This action is irreversible: the list and all tasks within it will be permanently deleted and cannot be recovered.

        Args:
            listId: The ID of the Clickup list. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickup_get_folder(
        self,
        folderId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single specified folder in a ClickUp workspace, including its name, lists, and metadata. Use this when you need full details about one specific folder by its ID. Do not use this to retrieve all folders in a space — use clickup_list_folders instead. This is a read-only operation with no side effects.

        Args:
            folderId: The ID of the Clickup folder. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickup_get_list(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single specified task list in ClickUp, including its name, status, priority, and associated metadata. Use this when you need full details about one specific list by its ID. Do not use this to retrieve all lists in a folder — use clickup_list_lists instead. This is a read-only operation with no side effects.

        Args:
            listId: ID of the Clickup list. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickup_list_folders(
        self,
        spaceId: str,
        archived: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all folders within a specified ClickUp space. Use this to enumerate folders before accessing lists or folder details within a space. Do not use this to retrieve a single folders details — use clickup_get_folder instead. This is a read-only operation with no side effects.

        Args:
            spaceId: The ID of the Clickup space. (required)
            archived: Filter by archived status (e.g., true, false).
        Returns:
            API response as a dictionary.
        """
        ...

    def clickup_list_lists(
        self,
        folderId: str,
        archived: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all task lists within a specified ClickUp folder. Use this to enumerate lists before accessing tasks or list details within a folder. Do not use this to retrieve a single lists details — use clickup_get_list instead. This is a read-only operation with no side effects.

        Args:
            folderId: ID of the Clickup folder. (required)
            archived: Whether to include archived items.
        Returns:
            API response as a dictionary.
        """
        ...

    def clickup_list_spaces(
        self,
        team_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all spaces available within a specified ClickUp team (workspace). Use this to discover the spaces a team has configured before drilling into folders or lists. Do not use this to retrieve folders, lists, or tasks — use clickup_list_folders, clickup_list_lists, or task-specific tools instead. This is a read-only operation with no side effects.

        Args:
            team_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def clickup_list_teams(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all teams (also referred to as workspaces) accessible to the authenticated ClickUp user. Use this as the starting point to discover available workspaces before querying spaces, folders, or lists. Do not use this to list spaces or folders — use clickup_list_spaces or clickup_list_folders instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def clickup_list_workspaces(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all workspaces (teams) accessible to the authenticated ClickUp user. Use this as the entry point to discover available workspaces before navigating to spaces, folders, or lists. Note: this endpoint is equivalent to clickup_list_teams and returns the same data; prefer clickup_list_teams for consistency when listing teams. Do not use this to retrieve spaces or folders — use clickup_list_spaces or clickup_list_folders instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def clickup_update_folder(
        self,
        folderId: str,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the properties of an existing folder in a ClickUp workspace, such as its name or override settings. Use this when you need to modify folder-level attributes without recreating the folder. Do not use this to update lists or tasks — use clickup_update_list or task-specific tools instead. This action overwrites the existing folder properties with the values provided.

        Args:
            folderId: The ID of the folder. (required)
            name: The name of the item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clickup_update_list(
        self,
        assignee: int,
        content: str,
        due_date: int,
        due_date_time: bool,
        listId: str,
        name: str,
        priority: int,
        status: str,
        include_markdown_description: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates the properties of an existing task list in a ClickUp workspace, such as its name, due date, priority, or status. Use this when you need to modify list-level settings without deleting or recreating the list. Do not use this to update folders or individual tasks — use clickup_update_folder or task-specific tools instead. This action overwrites existing list properties with the values provided.

        Args:
            assignee: The ID of the user assigned to the task. (required)
            content: The content or description of the task. (required)
            due_date: The due date of the task (timestamp). (required)
            due_date_time: Indicates whether to include the due date and time. (required)
            listId: The ID of the list where the task should be created. (required)
            name: The name of the task. (required)
            priority: The priority level of the task. (required)
            status: The status of the task. (required)
            include_markdown_description: Indicates whether the description should be parsed as Markdown.
        Returns:
            API response as a dictionary.
        """
        ...

