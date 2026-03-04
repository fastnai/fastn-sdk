"""Fastn Uploadcare connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class UploadcareConnector:
    """Uploadcare connector ().

    Provides 4 tools.
    """

    def upload_care_delete_file(
        self,
        fileId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific file from Uploadcare storage by its file ID. Use this tool when you need to remove a file that is no longer needed. This action is irreversible — once deleted, the file and its associated metadata cannot be recovered. Do not use this tool if you only want to retrieve or inspect file information.

        Args:
            fileId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_care_get_file(
        self,
        fileId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed metadata about a specific file stored in Uploadcare by its file ID. Returns information such as file name, size, MIME type, upload date, and CDN URL. Use this tool when you need to inspect or verify details of a single known file. Do not use this tool to list multiple files — use upload_care_list_files instead.

        Args:
            fileId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_care_list_files(
        self,
        from: Optional[str] = None,
        include: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all files stored in the Uploadcare account, including metadata such as file names, sizes, MIME types, and CDN URLs. Use this tool when you need an overview of all stored files or want to find files to act on. Do not use this tool to retrieve details of a single specific file — use upload_care_get_file instead.

        Args:
            from: 
            include: 
            limit: 
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_care_upload_file(
        self,
        UPLOADCARE_PUB_KEY: Optional[str] = None,
        UPLOADCARE_STORE: Optional[str] = None,
        file: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a new file to Uploadcare storage via the base upload endpoint. Upon success, returns the uploaded files UUID and CDN URL for future access. Use this tool when you need to store a new file in Uploadcare. Note that uploading a file consumes storage quota and makes the file immediately accessible via the CDN. Do not use this tool to update or replace an existing file — delete the old file first, then upload the new one.

        Args:
            UPLOADCARE_PUB_KEY: 
            UPLOADCARE_STORE: 
            file: 
        Returns:
            API response as a dictionary.
        """
        ...

