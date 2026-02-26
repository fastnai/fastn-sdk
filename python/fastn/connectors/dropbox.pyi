"""Fastn Dropbox connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class DropboxConnector:
    """Dropbox connector ().

    Provides 10 tools.
    """

    def create_or_update_file(
        self,
    ) -> Dict[str, Any]:
        """Creates a new file or updates an existing file in the file management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Retrieves an access token for authenticating requests in the file management system.

        Args:
            client_id: Your Dropbox application's client ID. (required)
            client_secret: Your Dropbox application's client secret. (required)
            code: Authorization code received from Dropbox OAuth flow. (required)
            redirect_uri: The redirect URI registered for your Dropbox application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_cursor(
        self,
        path: str,
        include_deleted: Optional[bool] = None,
        include_has_explicit_shared_members: Optional[bool] = None,
        include_media_info: Optional[bool] = None,
        include_mounted_folders: Optional[bool] = None,
        include_non_downloadable_files: Optional[bool] = None,
        recursive: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Obtains a cursor for pagination or continuation purposes in the file management system.

        Args:
            path:  (required)
            include_deleted: 
            include_has_explicit_shared_members: 
            include_media_info: 
            include_mounted_folders: 
            include_non_downloadable_files: 
            recursive: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_metadata(
        self,
        path: str,
        include_deleted: Optional[bool] = None,
        include_has_explicit_shared_members: Optional[bool] = None,
        include_media_info: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves metadata for a specified file in the file management system.

        Args:
            path: The path to the file or folder in Dropbox. (required)
            include_deleted: Whether to include deleted files and folders in the response.
            include_has_explicit_shared_members: Whether to include information about explicitly shared members.
            include_media_info: Whether to include media information in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_folder(
        self,
        path: str,
    ) -> Dict[str, Any]:
        """Fetches the details of a specified folder within the file management system.

        Args:
            path: The path to the file or folder on Dropbox. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_folder_continue(
        self,
        cursor: str,
    ) -> Dict[str, Any]:
        """Continues fetching folder details using a cursor in the file management system.

        Args:
            cursor: Cursor string used to continue fetching the next set of folder entries. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_folders(
        self,
        path: str,
        include_deleted: Optional[bool] = None,
        include_has_explicit_shared_members: Optional[bool] = None,
        include_media_info: Optional[bool] = None,
        include_mounted_folders: Optional[bool] = None,
        include_non_downloadable_files: Optional[bool] = None,
        recursive: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of folders available in the file management system.

        Args:
            path: The path of the folder to retrieve information about. (required)
            include_deleted: Whether to include deleted files in the response.
            include_has_explicit_shared_members: Whether to include whether each file or folder has explicit shared members.
            include_media_info: Whether to include media information for files.
            include_mounted_folders: Whether to include mounted folders in the response.
            include_non_downloadable_files: Whether to include files that cannot be downloaded.
            recursive: Whether to list subfolder contents recursively.
        Returns:
            API response as a dictionary.
        """
        ...

    def iterate_with_cursor(
        self,
        cursor: str,
    ) -> Dict[str, Any]:
        """Iterates through files in the file management system using a previously obtained cursor.

        Args:
            cursor: Cursor for pagination of Dropbox data. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def read_file(
        self,
        path: str,
        responseContentType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Reads the contents of a specified file in the file management system.

        Args:
            path: Path to the file within the Dropbox account. (required)
            responseContentType: 
        Returns:
            API response as a dictionary.
        """
        ...

    def refresh_token(
        self,
        client_id: str,
        client_secret: str,
        refresh_token: str,
    ) -> Dict[str, Any]:
        """Refreshes an expired access token to maintain session authentication in the file management system.

        Args:
            client_id: Client ID for Dropbox API access. (required)
            client_secret: Client secret for Dropbox API access. (required)
            refresh_token: Refresh token for Dropbox authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

