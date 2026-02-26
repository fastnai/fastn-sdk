"""Fastn SeaFile connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SeafileConnector:
    """SeaFile connector ().

    Provides 17 tools.
    """

    def create_department(
        self,
        group_name: str,
        group_owner: Optional[str] = None,
        parent_group: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new department in the department management system.

        Args:
            group_name: The name of the group to be created. (required)
            group_owner: The username of the group owner.
            parent_group: The ID of the parent group (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def create_file(
        self,
        p: str,
    ) -> Dict[str, Any]:
        """Creates a new file in the file management system.

        Args:
            p: Description of parameter 'p'. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_group(
        self,
        group_name: str,
        group_owner: str,
    ) -> Dict[str, Any]:
        """Creates a new group in the group management system.

        Args:
            group_name: The name of the group to be created. (required)
            group_owner: The username of the group owner. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_user(
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
        """Creates a new user in the user management system.

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

    def delete_department(
        self,
        group_id: str,
    ) -> Dict[str, Any]:
        """Deletes a specified department from the department management system.

        Args:
            group_id: The ID of the group. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_file(
        self,
        p: str,
    ) -> Dict[str, Any]:
        """Deletes a specified file from the file management system.

        Args:
            p: Description of parameter p (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_group(
        self,
        group_id: str,
    ) -> Dict[str, Any]:
        """Deletes a specified group from the group management system.

        Args:
            group_id: The ID of the group. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_user(
        self,
        user_id: str,
    ) -> Dict[str, Any]:
        """Deletes a specified user from the user management system.

        Args:
            user_id: The ID of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def download_file(
        self,
        p: str,
        reuse: str,
    ) -> Dict[str, Any]:
        """Downloads a specified file from the file management system to your local device.

        Args:
            p: Description of parameter 'p'. (required)
            reuse: Description of parameter 'reuse'. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_account_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves account information from the account management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_department_details(
        self,
        return_ancestors: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specified department in the department management system.

        Args:
            return_ancestors: Specifies whether to return ancestor information.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_departments(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of all departments in the organization from the department management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_activities(
        self,
        avatar_size: Optional[str] = None,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a log of all activities related to a specified file in the file management system.

        Args:
            avatar_size: Size of the avatar image.
            page: Page number for pagination.
            per_page: Number of items per page for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_detail(
        self,
        p: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specified file in the file management system.

        Args:
            p: Description of parameter 'p' needed for Seafile API call. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_groups(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all groups in the organization from the group management system.

        Args:
            page: Specifies the page number for pagination.
            per_page: Specifies the number of items per page for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all users from the user management system.

        Args:
            page: The page number to retrieve.
            per_page: The number of items per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def search_user(
        self,
        query: str,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for users within the user management system based on given criteria.

        Args:
            query: A search query string. (required)
            page: The page number for pagination.
            per_page: The number of items per page.
        Returns:
            API response as a dictionary.
        """
        ...

