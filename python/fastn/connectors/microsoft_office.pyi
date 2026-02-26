"""Fastn Microsoft Office connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MicrosoftOfficeConnector:
    """Microsoft Office connector ().

    Provides 7 tools.
    """

    def change_file_permission_to_read_only(
        self,
        roles: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Changes the file permission to read-only in the file management system.

        Args:
            roles: Array of roles associated with the request in Microsoft Office.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_current_user_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves information about the current user logged into the system for personalized settings or profiles.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Retrieves a specified file from the file management system for viewing or download.

        Args:
            fileName: Name of the file for the Microsoft Office API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_permissions(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Fetches the current permissions associated with a specified file in the file management system.

        Args:
            fileId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_versions(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Obtains the version history of a specified file, detailing all previously saved versions in the file management system.

        Args:
            fileName: Name of the file being accessed via the Microsoft Office API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users_in_org(
        self,
    ) -> Dict[str, Any]:
        """Lists all users currently registered in the organization for user management purposes.
        Returns:
            API response as a dictionary.
        """
        ...

    def restore_file_previous_version(
        self,
        fileName: str,
        versionNumber: str,
    ) -> Dict[str, Any]:
        """Restores a specified file to its previous version in the file management system.

        Args:
            fileName: Name of the file to be accessed in Microsoft Office. (required)
            versionNumber: Version number of the file to be accessed in Microsoft Office. (required)
        Returns:
            API response as a dictionary.
        """
        ...

