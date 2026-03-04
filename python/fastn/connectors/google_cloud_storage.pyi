"""Fastn Google Cloud Storage connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class GoogleCloudStorageConnector:
    """Google Cloud Storage connector ().

    Provides 12 tools.
    """

    def google_cloud_storage_create_bucket(
        self,
        location: Optional[str] = None,
        name: Optional[str] = None,
        project: Optional[str] = None,
        storageClass: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new storage bucket in Google Cloud Storage for organizing and storing objects (files). Use this when you need to provision a new container for data storage within a GCS project. Bucket names must be globally unique. This operation provisions a persistent resource—deletion requires a separate delete action and will remove all objects inside.

        Args:
            location: 
            name: 
            project: 
            storageClass: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_cloud_storage_download_file(
        self,
        alt: Optional[str] = None,
        bucketName: Optional[str] = None,
        fileName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads the binary content of a specific object (file) from a Google Cloud Storage bucket. Use this when you need to retrieve the actual file contents from GCS, identified by bucket name and file name. To retrieve only file metadata without downloading content, use the get file tool instead. Requires the bucket name and exact object name.

        Args:
            alt: 
            bucketName: 
            fileName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_cloud_storage_get_file(
        self,
        bucketName: Optional[str] = None,
        fileName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves metadata and details for a single object (file) stored in a specified Google Cloud Storage bucket. Use this when you need to inspect a files properties such as size, content type, creation time, or storage class. Does not download the files content—use the download tool for that. Requires the bucket name and the exact file name (object name).

        Args:
            bucketName: 
            fileName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_cloud_storage_list_buckets(
        self,
        maxResults: Optional[str] = None,
        pageToken: Optional[str] = None,
        project: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all Google Cloud Storage buckets available in your GCS project. Use this to enumerate existing buckets before performing operations such as uploading files or checking bucket configurations. Returns bucket names and metadata. To list files within a specific bucket, use the list files tool instead.

        Args:
            maxResults: 
            pageToken: 
            project: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_cloud_storage_list_files(
        self,
        bucketName: Optional[str] = None,
        maxResults: Optional[str] = None,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all objects (files) stored in a specified Google Cloud Storage bucket. Use this to enumerate the contents of a bucket, including object names and metadata summaries. Returns a collection of objects—use the get file tool to retrieve full details for a single object. Requires the bucket name.

        Args:
            bucketName: 
            maxResults: 
            pageToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_cloud_storage_list_projects(
        self,
        pageSize: Optional[str] = None,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all Google Cloud projects associated with your account using the Cloud Resource Manager API. Use this to identify available project IDs before performing project-scoped GCS operations such as listing buckets. Not specific to Cloud Storage—returns all Google Cloud projects regardless of which services they use.

        Args:
            pageSize: 
            pageToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_cloud_storage_start_upload_session(
        self,
        bucket_name: Optional[str] = None,
        file_content: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Initiates a resumable upload session for transferring a file to a Google Cloud Storage bucket. Use this as the first step when uploading large files that may require multiple requests or when you need fault-tolerant uploads that can be resumed after interruption. After calling this tool, use the session URI returned to upload file chunks. Not needed for small files—use the direct upload tool instead.

        Args:
            bucket_name: 
            file_content: 
            file_name: 
            mime_type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_cloud_storage_upload_binary_file(
        self,
        bucketName: str,
        contentType: str,
        name: str,
        body: Optional[str] = None,
        uploadType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a binary file to a specified Google Cloud Storage bucket. Use this when you need to store raw binary content such as images, PDFs, compressed archives, or other non-text files in GCS. For JSON-structured data, use the JSON file upload tool instead. This operation creates or overwrites an object in the bucket and cannot be undone without a separate delete action. Requires the target bucket name and the binary content to upload.

        Args:
            bucketName:  (required)
            contentType:  (required)
            name:  (required)
            body: 
            uploadType: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_cloud_storage_upload_file(
        self,
        file_content: Optional[str] = None,
        mime_type: Optional[str] = None,
        upload_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a local file or in-memory content directly to a specified Google Cloud Storage bucket using a single-request transfer. Use this for small to medium files that can be transferred in one request. For large files or resumable transfers, use the upload session tools instead. This operation creates or overwrites an object in the bucket and cannot be undone without a separate delete action.

        Args:
            file_content: 
            mime_type: 
            upload_url: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_cloud_storage_upload_file_from_url(
        self,
        bucketName: Optional[str] = None,
        downloadUrl: Optional[str] = None,
        fileName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a file to a specified Google Cloud Storage bucket by fetching it directly from a remote download URL. Use this when you have a publicly accessible or authenticated URL pointing to a file and want to store it in GCS without downloading it locally first. Not suitable for uploading local files or binary content already in memory—use the direct upload tool instead. This operation stores a new object in the bucket and cannot be undone without a separate delete action.

        Args:
            bucketName: 
            downloadUrl: 
            fileName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_cloud_storage_upload_json_file(
        self,
        body: Dict[str, Any],
        bucketName: Optional[str] = None,
        contentType: Optional[str] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a JSON-formatted file to a specified Google Cloud Storage bucket. Use this when you need to store structured JSON data as an object in GCS. The content type will be set appropriately for JSON. For binary or other file types, use the binary file upload tool instead. This operation creates or overwrites an object in the bucket and cannot be undone without a separate delete action. Requires the target bucket name and the JSON content to upload.

        Args:
            body:  (required)
            bucketName: 
            contentType: 
            name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_drive_download_file_post(
        self,
        fileId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads the binary content of a specified file from Google Drive using the async download endpoint (POST). Use this for files that require server-side processing before download, such as large files. For standard file downloads, prefer google_drive_download_file. Does not modify the file. Note: there is a duplicate download action in this connector — confirm which endpoint is appropriate for your use case.

        Args:
            fileId: 
        Returns:
            API response as a dictionary.
        """
        ...

