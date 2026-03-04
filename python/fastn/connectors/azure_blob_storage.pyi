"""Fastn Azure Blob Storage connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AzureBlobStorageConnector:
    """Azure Blob Storage connector ().

    Provides 4 tools.
    """

    def azure_blob_storage_get_blob(
        self,
        containerName: Optional[str] = None,
        fileName: Optional[str] = None,
        storageAccountName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the content of a single blob from a specific container in an Azure Blob Storage account. Use this tool when you need to read or download the content of a known blob by its file name. Do not use this tool to list available blobs — use azure_blob_storage_list_blobs for discovery first. Requires the container name and the blob file name.

        Args:
            containerName: 
            fileName: 
            storageAccountName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_blob_storage_list_blobs(
        self,
        containerName: Optional[str] = None,
        delimiter: Optional[str] = None,
        marker: Optional[str] = None,
        maxresults: Optional[str] = None,
        prefix: Optional[str] = None,
        showonly: Optional[str] = None,
        storageAccountName: Optional[str] = None,
        timeout: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all blobs within a specific container in an Azure Blob Storage account. Use this tool when you need to enumerate the blobs (files) stored inside a named container, for example to discover available files before downloading one. Do not use this tool to list containers themselves — use azure_blob_storage_list_containers for that. Returns blob names and metadata for the specified container.

        Args:
            containerName: 
            delimiter: 
            marker: 
            maxresults: 
            prefix: 
            showonly: 
            storageAccountName: 
            timeout: 
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_blob_storage_list_containers(
        self,
        storageAccountName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all containers available in an Azure Blob Storage account. Use this tool when you need to discover which containers exist in the storage account before drilling into a specific container. Do not use this tool to list blobs inside a container — use azure_blob_storage_list_blobs for that. Returns container names and associated metadata.

        Args:
            storageAccountName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def azure_blob_storage_put_blob(
        self,
        body: Optional[Dict[str, Any]] = None,
        containerName: Optional[str] = None,
        date: Optional[str] = None,
        fileName: Optional[str] = None,
        storageAccountName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads (creates or overwrites) a blob in a specific container in an Azure Blob Storage account. Use this tool when you need to store a new file or replace an existing blob with updated content. WARNING: If a blob with the same file name already exists in the container, it will be overwritten immediately — this action is irreversible without a prior backup. Requires the container name, file name, and blob content.

        Args:
            body: 
            containerName: 
            date: 
            fileName: 
            storageAccountName: 
        Returns:
            API response as a dictionary.
        """
        ...

