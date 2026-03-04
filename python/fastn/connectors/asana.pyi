"""Fastn Asana connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _AsanaAddProjectToTaskData(TypedDict, total=False):
    insert_after: str
    insert_before: str
    project: str
    section: str

class _AsanaAddUserToWorkspaceData(TypedDict, total=False):
    user: str

class _AsanaCreateProjectData(TypedDict, total=False):
    archived: bool
    color: str
    created_at: str
    current_status: Dict[str, Any]
    current_status_update: Dict[str, Any]
    custom_field_settings: List[Any]
    custom_fields: Dict[str, Any]
    default_access_level: str
    default_view: str
    due_date: str
    due_on: str
    followers: str
    gid: str
    html_notes: str
    members: List[Any]
    minimum_access_level_for_customization: str
    minimum_access_level_for_sharing: str
    modified_at: str
    name: str
    notes: str
    owner: str
    privacy_setting: str
    public: bool
    resource_type: str
    start_on: str
    team: str
    workspace: str

class _AsanaCreateProjectStatusData(TypedDict, total=False):
    color: str
    gid: str
    html_text: str
    resource_type: str
    text: str
    title: str

class _AsanaCreateTaskData(TypedDict, total=False):
    actual_time_minutes: int
    approval_status: str
    assignee: str
    assignee_section: str
    assignee_status: str
    completed: bool
    completed_at: str
    completed_by: Dict[str, Any]
    created_at: str
    created_by: Dict[str, Any]
    custom_fields: Dict[str, Any]
    dependencies: List[Any]
    dependents: List[Any]
    due_at: str
    due_on: str
    external: Dict[str, Any]
    followers: List[Any]
    gid: str
    hearted: bool
    hearts: List[Any]
    html_notes: str
    is_rendered_as_separator: bool
    liked: bool
    likes: List[Any]
    memberships: List[Any]
    modified_at: str
    name: str
    notes: str
    num_hearts: int
    num_likes: int
    num_subtasks: int
    parent: str
    projects: List[Any]
    resource_subtype: str
    resource_type: str
    start_at: str
    start_on: str
    tags: List[Any]
    workspace: str

class _AsanaDuplicateTaskData(TypedDict, total=False):
    include: str
    name: str

class _AsanaRemoveProjectFromTaskData(TypedDict, total=False):
    project: str

class _AsanaUpdateProjectData(TypedDict, total=False):
    archived: bool
    color: str
    created_at: str
    current_status: Dict[str, Any]
    current_status_update: Dict[str, Any]
    custom_field_settings: List[Any]
    custom_fields: Dict[str, Any]
    default_access_level: str
    default_view: str
    due_date: str
    due_on: str
    followers: str
    gid: str
    html_notes: str
    members: List[Any]
    minimum_access_level_for_customization: str
    minimum_access_level_for_sharing: str
    modified_at: str
    name: str
    notes: str
    owner: str
    privacy_setting: str
    public: bool
    resource_type: str
    start_on: str
    team: str

class _AsanaUpdateTaskData(TypedDict, total=False):
    actual_time_minutes: int
    approval_status: str
    assignee: str
    assignee_section: str
    assignee_status: str
    completed: bool
    completed_at: str
    completed_by: Dict[str, Any]
    created_at: str
    created_by: Dict[str, Any]
    custom_fields: Dict[str, Any]
    dependencies: List[Any]
    dependents: List[Any]
    due_at: str
    due_on: str
    external: Dict[str, Any]
    followers: List[Any]
    gid: str
    hearted: bool
    hearts: List[Any]
    html_notes: str
    is_rendered_as_separator: bool
    liked: bool
    likes: List[Any]
    memberships: List[Any]
    modified_at: str
    name: str
    notes: str
    num_hearts: int
    num_likes: int
    num_subtasks: int
    parent: str
    projects: List[Any]
    resource_subtype: str
    resource_type: str
    start_at: str
    start_on: str
    tags: List[Any]
    workspace: str

class AsanaConnector:
    """Asana connector ().

    Provides 19 tools.
    """

    def asana_add_project_to_task(
        self,
        task_gid: str,
        data: Optional[_AsanaAddProjectToTaskData] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Associates an existing Asana project with a specific task identified by its task GID. Use this tool when you need to link a task to one or more projects so it appears in those projects task lists. Do not use this tool to create a new project — use asana_create_project for that. This action modifies the tasks project membership and is reversible via asana_remove_project_from_task.

        Args:
            task_gid: GID of the task. (required)
            data: Data payload for the Asana V1 API request.
            opt_pretty: Optional parameter for pretty printing the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_add_user_to_workspace(
        self,
        data: _AsanaAddUserToWorkspaceData,
        workspace_gid: str,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a user to a specific Asana workspace identified by its workspace GID. Use this tool when you need to grant a user access to a workspace so they can collaborate on projects and tasks within it. Do not use this tool to add a user to a specific team — use the appropriate team membership tool for that. This action modifies workspace membership and takes effect immediately.

        Args:
            data: Data payload for the Asana API request. (required)
            workspace_gid: Workspace Global ID. (required)
            opt_fields: Optional fields to include in the response.
            opt_pretty: Optional parameter to pretty print the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_create_project(
        self,
        data: Optional[_AsanaCreateProjectData] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new project in Asana. Use this tool when you need to set up a new project to organize tasks, assign ownership, and track work within a workspace or team. Do not use this tool to update an existing project — use asana_update_project for that. This action creates a persistent project record in Asana and cannot be undone without a separate delete operation.

        Args:
            data: Data payload for the Asana API request.
            opt_fields: 
            opt_pretty: Optional parameter for pretty printing the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_create_project_status(
        self,
        project_gid: str,
        data: Optional[_AsanaCreateProjectStatusData] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
        project_status_gid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new status update for a specific Asana project identified by its project GID. Use this tool when you need to post a status update (e.g., on track, at risk, off track) to a project to communicate progress to stakeholders. Do not use this tool to update the projects metadata such as its name or due date — use asana_update_project for that. This action creates a persistent status record in Asana and cannot be undone without a separate delete operation.

        Args:
            project_gid: Globally unique identifier for the Asana project. (required)
            data: Data for creating a new task in Asana.
            opt_fields: Comma-separated list of fields to include in the response.
            opt_pretty: Indicates whether to return the response in a pretty-printed format.
            project_status_gid: Globally unique identifier for the Asana project status.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_create_task(
        self,
        data: Optional[_AsanaCreateTaskData] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new task in Asana, optionally associating it with a specific project or workspace. Use this tool when you need to add a new unit of work, specifying fields such as name, description, assignee, due date, and project membership. Do not use this tool to update an existing task — use asana_update_task for that. This action creates a persistent task record in Asana and cannot be undone without a separate delete operation.

        Args:
            data: Data payload for the Asana API request.
            opt_fields: Optional fields to include in the response.
            opt_pretty: Optional parameter for pretty printing the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_delete_project(
        self,
        project_gid: str,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific Asana project identified by its project GID. Use this tool when you need to remove a project and all of its associated data from Asana. Do not use this tool if you only want to archive or update the project — use asana_update_project for modifications. This action is irreversible: once deleted, the project and all its tasks, sections, and statuses cannot be recovered.

        Args:
            project_gid: Project Global ID (GID). (required)
            opt_pretty: Optional parameter to format the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_delete_task(
        self,
        task_gid: str,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific Asana task identified by its task GID. Use this tool when you need to remove a task that is no longer needed. Do not use this tool if you only want to close or complete a task — use asana_update_task to mark it complete instead. This action is irreversible: once deleted, the task and all its data cannot be recovered.

        Args:
            task_gid: Globally unique identifier for the task. (required)
            opt_pretty: Optional parameter for pretty printing the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_duplicate_task(
        self,
        task_gid: str,
        data: Optional[_AsanaDuplicateTaskData] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a duplicate copy of a specific Asana task identified by its task GID. Use this tool when you need to replicate a tasks structure, including its name, description, and optionally its subtasks, assignees, and attachments, without recreating it from scratch. Do not use this tool to create a brand-new task with custom fields — use asana_create_task for that. This action creates a new persistent task record in Asana and cannot be undone without a separate delete operation.

        Args:
            task_gid: Global ID of the task. (required)
            data: Data payload for Asana V1 API endpoint.
            opt_fields: Optional fields to include in the response.
            opt_pretty: Optional parameter to pretty-print the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_get_project(
        self,
        project_gid: str,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single Asana project identified by its project GID. Use this tool when you need to inspect a specific projects properties such as its name, description, owner, due date, and status. Do not use this tool to retrieve all projects — use asana_list_projects for that. This tool is read-only and has no side effects.

        Args:
            project_gid: Global ID of the Asana project. (required)
            opt_fields: Specifies which fields to include in the response.
            opt_pretty: Formats the response for better readability.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_get_project_status(
        self,
        project_status_gid: str,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the status of a specific Asana project identified by its project GID. Use this tool when you need to check the current status update (e.g., on track, at risk, off track) for a project. Do not use this tool to retrieve details about the project itself — use asana_get_project for that. This tool is read-only and has no side effects.

        Args:
            project_status_gid: The project status global ID. (required)
            opt_fields: Optional fields to include in the response.
            opt_pretty: Optional parameter to pretty-print the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_get_task(
        self,
        task_gid: str,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single Asana task identified by its task GID. Use this tool when you need to inspect a specific tasks properties such as name, description, assignee, due date, and completion status. Do not use this tool to retrieve multiple tasks at once — use asana_list_tasks for that. This tool is read-only and has no side effects.

        Args:
            task_gid: The GID (Globally unique identifier) of the Asana task. (required)
            opt_fields: Specifies which fields to include in the response.  (Asana specific)
            opt_pretty: Specifies whether to format the response as pretty-printed JSON. (Asana specific)
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_get_workspace(
        self,
        workspace_gid: str,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single Asana workspace identified by its workspace GID. Use this tool when you need to inspect a specific workspaces properties such as its name, email domains, and settings. Do not use this tool to retrieve all workspaces — use asana_list_workspaces for that. This tool is read-only and has no side effects.

        Args:
            workspace_gid: The GID of the Asana workspace. (required)
            opt_fields: Specifies which fields to include in the response.
            opt_pretty: Indicates whether to format the response for readability.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_list_projects(
        self,
        workspace: str,
        archived: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
        team: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all projects accessible in Asana. Use this tool when you need an overview of all projects, for example to find a project GID before updating or deleting it. Do not use this tool to retrieve a single projects full details — use asana_get_project for that. This tool is read-only and has no side effects.

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

    def asana_list_tasks(
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
        """Lists all tasks available in Asana. Use this tool when you need an overview of tasks across the system, for example to find tasks to update or delete. Do not use this tool to retrieve a single tasks full details — use asana_get_task for that. This tool is read-only and has no side effects.

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

    def asana_list_workspace_teams(
        self,
        workspace_gid: str,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all teams associated with a specific Asana workspace identified by its workspace GID. Use this tool when you need to discover which teams exist within a workspace, for example before adding a user to a team or assigning a project to a team. Do not use this tool to retrieve workspace details — use asana_get_workspace for that. This tool is read-only and has no side effects.

        Args:
            workspace_gid: The Global ID of the Asana workspace. (required)
            limit: Limit the number of results.
            offset: Offset for pagination.
            opt_fields: Specify optional fields to include in the response.
            opt_pretty: Format the response for pretty printing.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_list_workspaces(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all workspaces accessible to the authenticated Asana user. Use this tool when you need to discover available workspaces, for example to obtain a workspace GID before retrieving teams or projects within it. Do not use this tool to retrieve a single workspaces full details — use asana_get_workspace for that. This tool is read-only and has no side effects.

        Args:
            limit: Limit the number of results returned.
            offset: Offset for pagination.
            opt_fields: Comma-separated list of fields to include in the response.
            opt_pretty: Flag to enable pretty printing of the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_remove_project_from_task(
        self,
        task_gid: str,
        data: Optional[_AsanaRemoveProjectFromTaskData] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes the association between a specific project and a task in Asana, identified by the tasks GID. Use this tool when you need to unlink a task from a project without deleting either the task or the project. Do not use this tool to delete the task or the project — use asana_delete_task or asana_delete_project for those operations. This action modifies the tasks project membership and is reversible by re-adding the project via asana_add_project_to_task.

        Args:
            task_gid: GID of the task in Asana V1 API (required)
            data: Data payload for Asana V1 API
            opt_pretty: Optional parameter for pretty printing the response from Asana V1 API
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_update_project(
        self,
        project_gid: str,
        data: Optional[_AsanaUpdateProjectData] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields of a specific Asana project identified by its project GID. Use this tool to modify project properties such as name, description, due date, owner, or privacy settings. Do not use this tool to delete a project — use asana_delete_project for that, or to post a status update — use asana_create_project_status instead. Changes take effect immediately in Asana.

        Args:
            project_gid: The project GID. (required)
            data: Data payload for the Asana V1 API request.
            opt_fields: Optional fields to include in the response.
            opt_pretty: Format the response to be more human-readable.
        Returns:
            API response as a dictionary.
        """
        ...

    def asana_update_task(
        self,
        task_gid: str,
        data: Optional[_AsanaUpdateTaskData] = None,
        opt_fields: Optional[str] = None,
        opt_pretty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields of a specific Asana task identified by its task GID. Use this tool to modify task properties such as name, description, due date, assignee, or completion status. Do not use this tool to delete a task — use asana_delete_task for that. This action overwrites the specified fields and the changes take effect immediately in Asana.

        Args:
            task_gid: Global ID of the task. (required)
            data: Data payload for the Asana V1 API request.
            opt_fields: Optional fields to include in the response.
            opt_pretty: Optional parameter for pretty printing the response.
        Returns:
            API response as a dictionary.
        """
        ...

