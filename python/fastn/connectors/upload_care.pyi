"""Fastn Upload Care connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class UploadCareConnector:
    """Upload Care connector ().

    Provides 4 tools.
    """

    def delete_file(
        self,
        fileId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified file from the storage system using the deleteFile connector.

        Args:
            fileId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file(
        self,
        fileId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific file using the getFile connector.

        Args:
            fileId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_files(
        self,
        from: Optional[str] = None,
        include: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all files stored in the system using the getFiles connector.

        Args:
            from: 
            include: 
            limit: 
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_file(
        self,
        UPLOADCARE_PUB_KEY: Optional[str] = None,
        UPLOADCARE_STORE: Optional[str] = None,
        file: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a file to the specified storage system using the uploadFile connector.

        Args:
            UPLOADCARE_PUB_KEY: 
            UPLOADCARE_STORE: 
            file: 
        Returns:
            API response as a dictionary.
        """
        ...

