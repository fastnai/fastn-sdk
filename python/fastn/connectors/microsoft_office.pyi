"""Fastn Microsoft Office connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MicrosoftOfficeConnector:
    """Microsoft Office connector ().

    Provides 7 tools.
    """

    def microsoft_office_change_file_permission_to_read_only(
        self,
        fileId: str,
        permissionId: str,
        roles: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates a specific permission entry on a OneDrive file to read-only, restricting the grantee from making further edits. Use this when you need to revoke write access for a particular user or share link while preserving their ability to view the file. Requires a valid file item ID and permission ID. This action modifies the files access control settings immediately. Do not use this to remove a permission entirely or to set other permission roles such as write or owner.

        Args:
            fileId: ID of the file in Microsoft Office. (required)
            permissionId: ID of the permission for the file in Microsoft Office. (required)
            roles: Array of roles associated with the request in Microsoft Office.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_office_get_current_user(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the Microsoft 365 profile of the currently authenticated user, including display name, email address, job title, and account details. Use this to identify who is performing actions or to personalize responses based on the logged-in users profile. Do not use this to retrieve information about other users in the organization; use microsoft_office_list_users_in_org for that. This tool is read-only and has no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_office_get_file(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Retrieves the metadata and properties of a specified file in the current users OneDrive by its path, including name, size, last modified date, and download URL. Use this to look up a files details before downloading, sharing, or modifying it. Requires the file name as a path relative to the drive root. Do not use this to list all files in a folder or to retrieve file version history. This tool is read-only and has no side effects.

        Args:
            fileName: Name of the file for the Microsoft Office API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_office_list_file_permissions(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Lists all permission entries currently set on a specified file in the current users OneDrive, including granted roles, share links, and identities with access. Use this to audit who has access to a file before making permission changes. Requires a valid file item ID. Do not use this to modify permissions; use microsoft_office_change_file_permission_to_read_only or a dedicated update tool for that. This tool is read-only and has no side effects.

        Args:
            fileId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_office_list_file_versions(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Lists all saved versions of a specified file in the current users OneDrive, including version IDs, timestamps, and size information. Use this to review a files change history or to identify a specific version to restore. Requires the file name as a path relative to the drive root. Do not use this to restore a version; use microsoft_office_restore_file_previous_version for that. This tool is read-only and has no side effects.

        Args:
            fileName: Name of the file being accessed via the Microsoft Office API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_office_list_users_in_org(
        self,
    ) -> Dict[str, Any]:
        """Lists all users registered in the Microsoft 365 organization. Use this to retrieve a directory of all organizational user accounts for management, auditing, or lookup purposes. Do not use this to retrieve only the currently authenticated user; use microsoft_office_get_current_user for that. This tool is read-only and has no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_office_restore_file_previous_version(
        self,
        fileName: str,
        versionNumber: str,
    ) -> Dict[str, Any]:
        """Restores a specified file in the current users OneDrive to a previously saved version identified by its version number. Use this when a file has been corrupted, accidentally modified, or needs to be rolled back to an earlier state. Requires the file name and the target version number. This action is destructive — it overwrites the current file content with the selected version. The current state will be saved as a new version entry, but the active content will change immediately. Do not use this if you only want to view version history without making changes; use microsoft_office_list_file_versions instead.

        Args:
            fileName: Name of the file to be accessed in Microsoft Office. (required)
            versionNumber: Version number of the file to be accessed in Microsoft Office. (required)
        Returns:
            API response as a dictionary.
        """
        ...

