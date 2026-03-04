"""Fastn Box connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _BoxCreateFolderParent(TypedDict, total=False):
    id: str

class _BoxMoveFileToFolderParent(TypedDict, total=False):
    id: str

class _BoxShareFileSharedLink(TypedDict, total=False):
    access: str

class BoxConnector:
    """Box connector ().

    Provides 10 tools.
    """

    def box_create_folder(
        self,
        name: str,
        parent: Optional[_BoxCreateFolderParent] = None,
    ) -> Dict[str, Any]:
        """Creates a new folder in Box under a specified parent folder. Use this to establish a new organizational directory for storing related files and documents. Do not use this to move existing files into a folder (use box_move_file_to_folder instead). The folder is created immediately and will be visible to users with access to the parent folder.

        Args:
            name: Name of the new item. (required)
            parent: Parent folder information.
        Returns:
            API response as a dictionary.
        """
        ...

    def box_delete_file(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified file from Box, removing it from the users storage and making it inaccessible to all collaborators. Use this to clean up files that are no longer needed. Do not use this if you only want to remove a users access (use box_share_file to revoke sharing instead). This action is irreversible — the file cannot be recovered once deleted.

        Args:
            fileId: The ID of the file in Box. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def box_get_account_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves profile and account information for the currently authenticated Box user, including details such as name, email, account status, and storage usage. Use this to confirm the identity of the connected account or to check account limits. Do not use this to retrieve information about other users or to list files. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def box_get_file(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Downloads the binary content of a specific file from Box. Use this when you need the actual file data rather than just metadata. Do not use this to retrieve file metadata such as name or creation date (use box_get_file_metadata instead). This is a read-only operation with no side effects.

        Args:
            fileId: The ID of the file to access on Box. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def box_get_file_metadata(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Retrieves metadata for a specific file in Box, including attributes such as file name, size, creation date, last modification date, owner, and file type. Use this to inspect file properties without downloading the file content. Do not use this to retrieve the actual file content (use box_get_file instead). This is a read-only operation with no side effects.

        Args:
            fileId: The ID of the file in Box. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def box_list_folder_items(
        self,
        folderId: str,
    ) -> Dict[str, Any]:
        """Lists the items (files and subfolders) contained within a specified Box folder. Use this to browse folder contents and retrieve item IDs for subsequent operations. Do not use this to retrieve folder metadata alone or to search across multiple folders (use box_search instead). This is a read-only operation with no side effects.

        Args:
            folderId: ID of the folder to access on Box. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def box_move_file_to_folder(
        self,
        fileId: str,
        parent: _BoxMoveFileToFolderParent,
    ) -> Dict[str, Any]:
        """Moves a specified file to a designated folder in Box by updating its parent folder reference. Use this to reorganize files within a Box account. Do not use this to copy a file or to rename it (use box_rename_file instead). The file will no longer appear in its original location after this operation.

        Args:
            fileId: ID of the file in Box. (required)
            parent: Parent folder details for the Box API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def box_rename_file(
        self,
        fileId: str,
        name: str,
    ) -> Dict[str, Any]:
        """Renames a specified file in Box by updating its display name. Use this to correct or clarify a file name without altering the files content or location. Do not use this to move the file to a different folder (use box_move_file_to_folder instead) or to update file content. The rename takes effect immediately and the previous name will no longer be associated with the file.

        Args:
            fileId: ID of the file in Box. (required)
            name: Name of the file or folder in Box. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def box_search(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Searches for files, folders, or other content within a Box account based on provided query criteria such as name, content, or metadata. Use this when you do not know the exact file or folder ID and need to locate items by keyword or filter. Do not use this to list the contents of a known folder (use box_list_folder_items instead). This is a read-only operation with no side effects.

        Args:
            query: Query string parameters for the Box API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def box_share_file(
        self,
        fileId: str,
        shared_link: _BoxShareFileSharedLink,
    ) -> Dict[str, Any]:
        """Shares a specified file in Box with designated users or groups by updating the files shared link or collaboration settings. Use this to grant other users access to a file for collaboration purposes. Do not use this to move or rename the file. Sharing settings can be changed or revoked later, but shared links generated during this call will be accessible to recipients immediately.

        Args:
            fileId: The ID of the file. (required)
            shared_link: Settings for the shared link. (required)
        Returns:
            API response as a dictionary.
        """
        ...

