"""Fastn Google Cloud Storage connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GoogleCloudStorageConnector:
    """Google Cloud Storage connector ().

    Provides 11 tools.
    """

    def create_bucket(
        self,
        project: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new bucket in your cloud storage service, allowing you to organize and store files.

        Args:
            project: 
        Returns:
            API response as a dictionary.
        """
        ...

    def download_file(
        self,
        fileId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads a specified file from your cloud storage service to your local machine.

        Args:
            fileId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_buckets(
        self,
        maxResults: Optional[str] = None,
        pageToken: Optional[str] = None,
        project: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all buckets available in your cloud storage service.

        Args:
            maxResults: 
            pageToken: 
            project: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file(
        self,
        bucketName: Optional[str] = None,
        fileName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific file's details from the specified bucket in your cloud storage service.

        Args:
            bucketName: 
            fileName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_files(
        self,
        maxResults: Optional[str] = None,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of files stored in the specified bucket within your cloud storage service.

        Args:
            maxResults: 
            pageToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_projects(
        self,
        pageSize: Optional[str] = None,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all projects associated with your account in the project management system.

        Args:
            pageSize: 
            pageToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def start_upload_session(
        self,
        bucket_name: Optional[str] = None,
        file_content: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Starts a new upload session for files to be transferred to your cloud storage service.

        Args:
            bucket_name: 
            file_content: 
            file_name: 
            mime_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_binary_file_to_bucket(
        self,
        contentType: str,
    ) -> Dict[str, Any]:
        """Uploads a binary file to the specified bucket in your cloud storage service.

        Args:
            contentType:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_file(
        self,
        file_content: Optional[str] = None,
        mime_type: Optional[str] = None,
        upload_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a file to the specified bucket in your cloud storage service using a direct transfer.

        Args:
            file_content: 
            mime_type: 
            upload_url: 
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_file_from_download_url(
        self,
        bucketName: Optional[str] = None,
        downloadUrl: Optional[str] = None,
        fileName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a file from a download URL directly to your specified bucket in your cloud storage service.

        Args:
            bucketName: 
            downloadUrl: 
            fileName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_json_file_to_bucket(
        self,
        contentType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a JSON file to the specified bucket in your cloud storage service.

        Args:
            contentType: 
        Returns:
            API response as a dictionary.
        """
        ...

