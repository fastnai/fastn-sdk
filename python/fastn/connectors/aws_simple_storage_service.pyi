"""Fastn AWS Simple Storage Service connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AwsSimpleStorageServiceConnector:
    """AWS Simple Storage Service connector ().

    Provides 11 tools.
    """

    def complete_multipart_upload(
        self,
        uploadId: str,
    ) -> Dict[str, Any]:
        """Completes a multipart upload in the storage connector by combining all uploaded parts into a single object.

        Args:
            uploadId: ID of the multipart upload. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_bucket(
        self,
        bucketName: str,
    ) -> Dict[str, Any]:
        """Creates a new bucket in the storage connector, enabling you to organize and manage your data effectively.

        Args:
            bucketName: Name of the S3 bucket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_multipart_upload(
        self,
        uploads: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Initiates a multipart upload in the storage connector, enabling the upload of large objects by splitting them into smaller parts.

        Args:
            uploads: Details about the uploads (if any).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_buckets(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of buckets from the storage connector, allowing you to view existing storage containers.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_object(
        self,
        bucketName: Optional[str] = None,
        object: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a specific object from a bucket in the storage connector, allowing you to access and download files.

        Args:
            bucketName: 
            object: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_objects(
        self,
        listtype: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of objects stored in a specified bucket from the storage connector, allowing you to view stored files.

        Args:
            listtype: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_presigned_url(
        self,
    ) -> Dict[str, Any]:
        """Generates a presigned URL for accessing a specific object in the storage connector, allowing temporary access without authentication.
        Returns:
            API response as a dictionary.
        """
        ...

    def put_object(
        self,
    ) -> Dict[str, Any]:
        """Uploads a single object to a specified bucket in the storage connector, allowing you to store files securely.
        Returns:
            API response as a dictionary.
        """
        ...

    def put_object_image(
        self,
    ) -> Dict[str, Any]:
        """Uploads an image object to a specified bucket in the storage connector, suitable for image file management.
        Returns:
            API response as a dictionary.
        """
        ...

    def put_parquet_object(
        self,
    ) -> Dict[str, Any]:
        """Uploads a Parquet object file to a specified bucket in the storage connector, optimizing data storage and retrieval.
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_part(
        self,
        partNumber: str,
        uploadId: str,
    ) -> Dict[str, Any]:
        """Uploads a single part of a multipart upload to a specified bucket in the storage connector, allowing for larger file uploads in segments.

        Args:
            partNumber: Number of the part being uploaded. (required)
            uploadId: ID of the multipart upload. (required)
        Returns:
            API response as a dictionary.
        """
        ...

