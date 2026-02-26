"""Fastn Files.com connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FilesComConnector:
    """Files.com connector ().

    Provides 4 tools.
    """

    def download_file(
        self,
        preview_size: Optional[str] = None,
        with_previews: Optional[str] = None,
        with_priority_color: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads a specified file from the connector, allowing users to obtain a copy of the file for local use or storage.

        Args:
            preview_size: Specify the size of previews to be returned.
            with_previews: Whether to include previews in the response.
            with_priority_color: Whether to include priority color information in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def file_upload(
        self,
        action: str,
        ref: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a file to the designated connector, enabling users to store their documents and media files securely in the connected application.

        Args:
            action: The action to be performed (e.g., upload, download). (required)
            ref: Reference ID for the Files.com action.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_or_folder(
        self,
        path: str,
    ) -> Dict[str, Any]:
        """Retrieves a file or folder from the specified connector, allowing users to access its contents and properties within a given application context.

        Args:
            path: The path component of the URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_files_in_folders(
        self,
        path: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of files contained within specified folders in the connector, providing users with an overview of available documents within the organizational structure.

        Args:
            path: 
        Returns:
            API response as a dictionary.
        """
        ...

