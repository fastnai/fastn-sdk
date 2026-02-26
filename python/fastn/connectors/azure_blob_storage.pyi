"""Fastn Azure blob Storage connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AzureBlobStorageConnector:
    """Azure blob Storage connector ().

    Provides 4 tools.
    """

    def get_blob(
        self,
        containerName: Optional[str] = None,
        fileName: Optional[str] = None,
        storageAccountName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves an existing blob from the storage system using the getBlob connector.

        Args:
            containerName: 
            fileName: 
            storageAccountName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_containers(
        self,
        storageAccountName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all available containers in the storage system through the getContainers connector.

        Args:
            storageAccountName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def list_blobs(
        self,
        delimiter: Optional[str] = None,
        marker: Optional[str] = None,
        maxresults: Optional[str] = None,
        prefix: Optional[str] = None,
        showonly: Optional[str] = None,
        timeout: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all blobs within a specific container in the storage system utilizing the listBlobs connector.

        Args:
            delimiter: 
            marker: 
            maxresults: 
            prefix: 
            showonly: 
            timeout: 
        Returns:
            API response as a dictionary.
        """
        ...

    def put_blob(
        self,
        date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a new blob to the storage system using the putBlob connector.

        Args:
            date: 
        Returns:
            API response as a dictionary.
        """
        ...

