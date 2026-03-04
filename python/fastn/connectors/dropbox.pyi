"""Fastn Dropbox connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class DropboxConnector:
    """Dropbox connector ().

    Provides 8 tools.
    """

    def dropbox_download_file(
        self,
        path: str,
        responseContentType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads and returns the binary contents of a specified file from Dropbox. Use this tool when you need to read or process the actual content of a file stored in Dropbox. Do not use this tool to retrieve file metadata only — use dropbox_get_file_metadata instead. Large files may result in significant data transfer.

        Args:
            path: Path to the file within the Dropbox account. (required)
            responseContentType: 
        Returns:
            API response as a dictionary.
        """
        ...

    def dropbox_get_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Exchanges a Dropbox OAuth2 authorization code for an access token and refresh token, enabling authenticated access to the Dropbox API. Use this tool during the initial OAuth2 authorization flow after receiving an authorization code from the user consent screen. Do not use this tool to renew an expired token — use dropbox_refresh_token instead. This call modifies session state by issuing new credentials.

        Args:
            client_id: Your Dropbox application's client ID. (required)
            client_secret: Your Dropbox application's client secret. (required)
            code: Authorization code received from Dropbox OAuth flow. (required)
            redirect_uri: The redirect URI registered for your Dropbox application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def dropbox_get_file_metadata(
        self,
        path: str,
        include_deleted: Optional[bool] = None,
        include_has_explicit_shared_members: Optional[bool] = None,
        include_media_info: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves metadata for a specified file or folder in Dropbox, including its name, path, size, content hash, and last modified date. Use this tool when you need to inspect properties of a specific Dropbox item without downloading its content. Do not use this tool to list the contents of a folder — use dropbox_list_folder instead, and do not use it to download file content — use dropbox_download_file instead.

        Args:
            path: The path to the file or folder in Dropbox. (required)
            include_deleted: Whether to include deleted files and folders in the response.
            include_has_explicit_shared_members: Whether to include information about explicitly shared members.
            include_media_info: Whether to include media information in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def dropbox_get_latest_cursor(
        self,
        path: str,
        include_deleted: Optional[bool] = None,
        include_has_explicit_shared_members: Optional[bool] = None,
        include_media_info: Optional[bool] = None,
        include_mounted_folders: Optional[bool] = None,
        include_non_downloadable_files: Optional[bool] = None,
        recursive: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves the latest pagination cursor for a specified Dropbox folder without returning any folder contents. Use this tool when you want to track future changes to a folder from the current point in time, for example before starting a long-polling sync loop. Do not use this tool if you need to list current folder contents — use dropbox_list_folder instead.

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

    def dropbox_list_folder(
        self,
        path: str,
        include_deleted: Optional[bool] = None,
        include_has_explicit_shared_members: Optional[bool] = None,
        include_media_info: Optional[bool] = None,
        include_mounted_folders: Optional[bool] = None,
        include_non_downloadable_files: Optional[bool] = None,
        recursive: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Lists the files and subfolders contained within a specified Dropbox folder path. Use this tool to retrieve the initial page of folder contents. If the response indicates more results are available (has_more: true), use dropbox_list_folder_continue with the returned cursor to fetch subsequent pages. Do not use this tool to retrieve metadata for a single file — use dropbox_get_file_metadata instead.

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

    def dropbox_list_folder_continue(
        self,
        cursor: str,
    ) -> Dict[str, Any]:
        """Continues listing the contents of a Dropbox folder using a pagination cursor returned by a previous list_folder or list_folder/get_latest_cursor call. Use this tool when a prior folder listing was truncated and you need to fetch the next page of results. Do not use this as the first call to list a folder — use dropbox_list_folder instead. Requires a valid cursor string as input.

        Args:
            cursor: Cursor string used to continue fetching the next set of folder entries. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def dropbox_refresh_token(
        self,
        client_id: str,
        client_secret: str,
        refresh_token: str,
    ) -> Dict[str, Any]:
        """Exchanges a Dropbox OAuth2 refresh token for a new short-lived access token, restoring authenticated API access after the previous token has expired. Use this tool when an API call fails due to an expired access token. Do not use this tool to obtain an initial access token — use dropbox_get_access_token instead. This call modifies session state by issuing a new token.

        Args:
            client_id: Client ID for Dropbox API access. (required)
            client_secret: Client secret for Dropbox API access. (required)
            refresh_token: Refresh token for Dropbox authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def dropbox_upload_file(
        self,
        content: str,
        fileName: str,
        filePath: str,
    ) -> Dict[str, Any]:
        """Uploads a file to a specified path in Dropbox, creating a new file or overwriting an existing one depending on the write mode specified. Use this tool to save or update file content in Dropbox. Note that this operation modifies Dropbox storage and, if the write mode is set to overwrite, will permanently replace any existing file at the target path. Do not use this tool to create folders — only file content is uploaded.

        Args:
            content: The content of the file to be uploaded. (required)
            fileName: Name of the file to be uploaded or accessed. (required)
            filePath: Path to the file within the Dropbox account. (required)
        Returns:
            API response as a dictionary.
        """
        ...

