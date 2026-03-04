"""Fastn Seafile connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class SeafileConnector:
    """Seafile connector ().

    Provides 17 tools.
    """

    def seafile_create_department(
        self,
        group_name: str,
        group_owner: Optional[str] = None,
        parent_group: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new department in the Seafile address book. Use this tool when an admin needs to add a department to the organizations address book structure. Do not use this tool to create standard collaboration groups; use seafile_create_group instead.

        Args:
            group_name: The name of the group to be created. (required)
            group_owner: The username of the group owner.
            parent_group: The ID of the parent group (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_create_file(
        self,
        p: str,
        repo_id: str,
    ) -> Dict[str, Any]:
        """Creates a new empty file at a specified path within a Seafile repository. Use this tool when you need to initialize a new file in a library before uploading content. Do not use this tool to upload file content directly; a separate upload action is required after creation.

        Args:
            p: Description of parameter 'p'. (required)
            repo_id: The ID of the repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_create_group(
        self,
        group_name: str,
        group_owner: str,
    ) -> Dict[str, Any]:
        """Creates a new group in Seafile. Use this tool when an admin needs to set up a new group for team collaboration or permission management. This action creates the group record but does not add members — member management requires separate actions. Do not use this tool to create departments; use seafile_create_department instead.

        Args:
            group_name: The name of the group to be created. (required)
            group_owner: The username of the group owner. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_create_user(
        self,
        email: str,
        password: str,
        is_active: Optional[str] = None,
        is_staff: Optional[str] = None,
        login_id: Optional[str] = None,
        name: Optional[str] = None,
        quota_total: Optional[str] = None,
        role: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new user account in Seafile. Use this tool when an admin needs to provision a new user with credentials and profile details. Do not use this tool to update an existing users information.

        Args:
            email: User's email address. (required)
            password: User's password. (required)
            is_active: Indicates whether the user account is active.
            is_staff: Indicates whether the user is a staff member.
            login_id: User's login ID.
            name: User's full name.
            quota_total: Total storage quota for the user.
            role: User's role in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_delete_department(
        self,
        group_id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified department from the Seafile address book by department (group) ID. Use this tool when an admin needs to remove a department from the organization structure. This action is irreversible — the department and its configuration cannot be recovered after deletion. Do not use this tool to delete standard groups; use seafile_delete_group instead.

        Args:
            group_id: The ID of the group. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_delete_file(
        self,
        p: str,
        repo_id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified file from a Seafile repository. Use this tool when a user or admin needs to remove a file from storage. This action is irreversible — the file cannot be recovered after deletion unless versioning or trash recovery is configured separately. Do not use this tool to delete entire libraries or directories.

        Args:
            p: Description of parameter p (required)
            repo_id: The ID of the repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_delete_group(
        self,
        group_id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified group from Seafile by group ID. Use this tool when an admin needs to remove a group and all its associated memberships. This action is irreversible — the group and its membership records cannot be recovered after deletion. Do not use this tool to delete departments; use seafile_delete_department instead.

        Args:
            group_id: The ID of the group. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_delete_user(
        self,
        user_id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified user account from Seafile by user ID. Use this tool when an admin needs to remove a user from the system, such as during offboarding. This action is irreversible — the user account and associated data cannot be recovered after deletion. Do not use this tool to simply deactivate a user; use an update tool if deactivation is preferred.

        Args:
            user_id: The ID of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_download_file(
        self,
        p: str,
        repo_id: str,
        reuse: str,
    ) -> Dict[str, Any]:
        """Generates a download link or retrieves the contents of a specified file from a Seafile repository. Use this tool when you need to access or transfer the actual file contents. Do not use this tool to retrieve file metadata only; use seafile_get_file_detail instead.

        Args:
            p: Description of parameter 'p'. (required)
            repo_id: The ID of the repository. (required)
            reuse: Description of parameter 'reuse'. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_get_account_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves account information for the currently authenticated Seafile user, including email, usage quota, and account status. Use this tool when you need to inspect the current users account details. Do not use this tool to retrieve information about other users — use seafile_list_users or seafile_search_user instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_get_department_details(
        self,
        group_id: str,
        return_ancestors: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific department in the Seafile address book, identified by department (group) ID. Use this tool when you need metadata for a single department such as its name, parent group, or member count. Do not use this tool to list all departments — use seafile_list_departments instead. Do not use this tool for standard groups; use seafile_list_groups instead.

        Args:
            group_id: The ID of the Seafile group. (required)
            return_ancestors: Specifies whether to return ancestor information.
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_get_file_detail(
        self,
        p: str,
        repo_id: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed metadata about a specific file in a Seafile repository, including its name, size, last modified time, and modifier. Use this tool when you need file information without downloading its contents. Do not use this tool to download the files contents; use seafile_download_file instead.

        Args:
            p: Description of parameter 'p' needed for Seafile API call. (required)
            repo_id: The ID of the repository. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_list_departments(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all departments in the Seafile organizations address book. Use this tool when an admin needs to enumerate or review all existing departments. Do not use this tool to list standard groups; use seafile_list_groups instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_list_file_activities(
        self,
        avatar_size: Optional[str] = None,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a log of recent file activity events in Seafile, such as uploads, downloads, edits, and deletions. Use this tool when you need to audit or review file operation history. Do not use this tool to retrieve metadata about a specific file; use seafile_get_file_detail instead.

        Args:
            avatar_size: Size of the avatar image.
            page: Page number for pagination.
            per_page: Number of items per page for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_list_groups(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all groups in the Seafile organization. Use this tool when an admin needs to view or enumerate all existing groups. Do not use this tool to list departments — use seafile_list_departments instead. For a single groups details, use the appropriate get-group tool if available.

        Args:
            page: Specifies the page number for pagination.
            per_page: Specifies the number of items per page for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_list_users(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all user accounts registered in Seafile. Use this tool when an admin needs to enumerate or audit all users in the system. For finding a specific user by search criteria, use seafile_search_user instead.

        Args:
            page: The page number to retrieve.
            per_page: The number of items per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def seafile_search_user(
        self,
        query: str,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for Seafile user accounts matching specified criteria such as email or username. Use this tool when you need to locate a specific user without knowing their exact user ID. Do not use this tool to retrieve all users — use seafile_list_users instead.

        Args:
            query: A search query string. (required)
            page: The page number for pagination.
            per_page: The number of items per page.
        Returns:
            API response as a dictionary.
        """
        ...

