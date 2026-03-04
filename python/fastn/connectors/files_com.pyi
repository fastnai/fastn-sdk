"""Fastn Files.com connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class FilesComConnector:
    """Files.com connector ().

    Provides 4 tools.
    """

    def file_transport_protocol_download_file(
        self,
        path: str,
        preview_size: Optional[str] = None,
        with_previews: Optional[str] = None,
        with_priority_color: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads the binary content of a specified file from an FTP server by its path. Use this tool when you need to obtain the actual file content for local use, processing, or storage. Do not use this tool to list folder contents or retrieve file metadata only — use file_transport_protocol_list_files_in_folder or file_transport_protocol_get_file_metadata instead.

        Args:
            path: The path to the resource on Files.com. (required)
            preview_size: Specify the size of previews to be returned.
            with_previews: Whether to include previews in the response.
            with_priority_color: Whether to include priority color information in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def file_transport_protocol_get_file_metadata(
        self,
        path: str,
    ) -> Dict[str, Any]:
        """Retrieves metadata and properties for a specific file or folder on an FTP server by its path, including details such as size, type, timestamps, and permissions. Use this tool when you need to inspect the attributes of a single file or folder without downloading its content. Do not use this tool to list all files within a folder — use file_transport_protocol_list_files_in_folder instead.

        Args:
            path: The path component of the URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def file_transport_protocol_list_files_in_folder(
        self,
        path: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all files contained within a specified folder path in an FTP server. Use this tool when you need an overview of files inside a directory, such as browsing folder contents or enumerating documents for downstream processing. Do not use this tool to retrieve file contents or metadata for a single file — use file_transport_protocol_download_file or file_transport_protocol_get_file_metadata instead.

        Args:
            path: 
        Returns:
            API response as a dictionary.
        """
        ...

    def file_transport_protocol_upload_file(
        self,
        action: str,
        path: str,
        ref: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a file to a specified path on an FTP server, creating or overwriting the file at the destination. Use this tool when you need to store a new document or media file on the FTP server. Note: if a file already exists at the target path it may be overwritten. Do not use this tool to download or list files.

        Args:
            action: The action to be performed (e.g., upload, download). (required)
            path: The path to the resource on Files.com. (required)
            ref: Reference ID for the Files.com action.
        Returns:
            API response as a dictionary.
        """
        ...

