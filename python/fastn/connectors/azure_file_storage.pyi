"""Fastn Azure File Storage connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AzureFileStorageConnector:
    """Azure File Storage connector ().

    Provides 4 tools.
    """

    def add_content_to_file(
        self,
        range: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Appends additional content to an existing file using the File Management connector.

        Args:
            range: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_file(
        self,
        x_ms_content_length: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new file in the File Management connector with the provided content and specifications.

        Args:
            x_ms_content_length: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_content(
        self,
        fileName: Optional[str] = None,
        fileShare: Optional[str] = None,
        path: Optional[str] = None,
        storageAccountName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the content of a specified file using the File Management connector.

        Args:
            fileName: 
            fileShare: 
            path: 
            storageAccountName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_files(
        self,
        comp: Optional[str] = None,
        include: Optional[str] = None,
        marker: Optional[str] = None,
        maxresults: Optional[str] = None,
        restype: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of files from the File Management connector based on specified parameters.

        Args:
            comp: 
            include: 
            marker: 
            maxresults: 
            restype: 
        Returns:
            API response as a dictionary.
        """
        ...

