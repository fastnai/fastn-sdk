"""Fastn Azure File Storage connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AzureFileStorageConnector:
    """Azure File Storage connector ().

    Provides 4 tools.
    """

    def azure_file_storage_add_content_to_file(
        self,
        body: Optional[int] = None,
        comp: Optional[str] = None,
        fileName: Optional[str] = None,
        filePath: Optional[str] = None,
        path: Optional[str] = None,
        range: Optional[str] = None,
        storageAccountName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Appends additional content to an existing file in an Azure File Storage share. Use this tool when you need to extend the content of a file that already exists without replacing it entirely, for example adding log entries or incremental data. Do not use this tool to create a new file — use azure_file_storage_create_file for that. Do not use this tool to overwrite a files full content. Requires the storage account name, file share path, and file name.

        Args:
            body: 
            comp: 
            fileName: 
            filePath: 
            path: 
            range: 
            storageAccountName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_file_storage_create_file(
        self,
        fileName: Optional[str] = None,
        fileShare: Optional[str] = None,
        path: Optional[str] = None,
        storageAccountName: Optional[str] = None,
        x_ms_content_length: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new file in an Azure File Storage share with the specified content. Use this tool when you need to write a new file to a file share, for example uploading a document or configuration file. WARNING: If a file with the same name already exists at the specified path, it will be overwritten — this action is irreversible without a prior backup. Do not use this tool to append content to an existing file — use azure_file_storage_add_content_to_file for that. Requires the storage account name, file share name, path, file name, and content.

        Args:
            fileName: 
            fileShare: 
            path: 
            storageAccountName: 
            x_ms_content_length: 
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_file_storage_get_file_content(
        self,
        fileName: Optional[str] = None,
        fileShare: Optional[str] = None,
        path: Optional[str] = None,
        storageAccountName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the content of a specific file from an Azure File Storage share. Use this tool when you need to read the data stored in a known file, for example to display, process, or analyze its contents. Do not use this tool to list files in a directory — use azure_file_storage_list_files for discovery. Requires the storage account name, file share name, directory path, and file name.

        Args:
            fileName: 
            fileShare: 
            path: 
            storageAccountName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_file_storage_list_files(
        self,
        comp: Optional[str] = None,
        fileShare: Optional[str] = None,
        include: Optional[str] = None,
        marker: Optional[str] = None,
        maxresults: Optional[str] = None,
        path: Optional[str] = None,
        restype: Optional[str] = None,
        storageAccountName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all files and directories at a specified path within an Azure File Storage share. Use this tool when you need to browse or enumerate the contents of a directory in a file share before reading or modifying a specific file. Do not use this tool to retrieve the content of a specific file — use azure_file_storage_get_file_content for that. Requires the storage account name, file share name, and directory path.

        Args:
            comp: 
            fileShare: 
            include: 
            marker: 
            maxresults: 
            path: 
            restype: 
            storageAccountName: 
        Returns:
            API response as a dictionary.
        """
        ...

