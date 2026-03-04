"""Fastn AWS Simple Storage Service connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _AwsS3CompleteMultipartUploadCompletemultipartupload(TypedDict, total=False):
    Part: Dict[str, Any]

class AwsSimpleStorageServiceConnector:
    """AWS Simple Storage Service connector ().

    Provides 12 tools.
    """

    def aws_s3_complete_multipart_upload(
        self,
        CompleteMultipartUpload: _AwsS3CompleteMultipartUploadCompletemultipartupload,
        _omit_xml_declaration: str,
        bucketName: str,
        fileName: str,
        uploadId: str,
    ) -> Dict[str, Any]:
        """Completes a multipart upload in AWS S3 by assembling all previously uploaded parts into a single object. Use this tool as the final step after uploading all parts via aws_s3_upload_part. You must provide the upload ID and the list of part numbers with their ETags. Once completed, the assembled object is immediately available in the bucket and the action cannot be undone without versioning enabled.

        Args:
            CompleteMultipartUpload: Details for completing a multipart upload. (required)
            _omit_xml_declaration: Flag to omit the XML declaration in the request body. (required)
            bucketName: Name of the S3 bucket. (required)
            fileName: Name of the file in the bucket. (required)
            uploadId: ID of the multipart upload. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_s3_create_bucket(
        self,
        bucketName: str,
    ) -> Dict[str, Any]:
        """Creates a new AWS S3 bucket with the specified name in the configured region. Use this tool when you need a new storage container before uploading objects. Bucket names must be globally unique across all AWS accounts. This action creates a persistent resource and incurs storage costs. Do not use this tool if the bucket already exists — use aws_s3_list_buckets to check first.

        Args:
            bucketName: Name of the S3 bucket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_s3_create_multipart_upload(
        self,
        bucketName: str,
        fileName: str,
        uploads: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Initiates a multipart upload session for a large object in AWS S3 and returns an upload ID required for subsequent part uploads. Use this tool as the first step when uploading files that are too large for a single PUT request (typically over 5 GB, recommended for files over 100 MB). After receiving the upload ID, upload each part using aws_s3_upload_part, then finalize with aws_s3_complete_multipart_upload. Incomplete multipart uploads incur storage costs until aborted or completed.

        Args:
            bucketName: Name of the S3 bucket. (required)
            fileName: Name of the file within the bucket. (required)
            uploads: Details about the uploads (if any).
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_s3_get_object(
        self,
        bucketName: Optional[str] = None,
        object: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads and returns a specific object from a specified AWS S3 bucket. Use this tool when you need to access or read the content of a stored file by its key. Do not use this tool to list available objects — use aws_s3_list_objects instead. Does not modify any data.

        Args:
            bucketName: 
            object: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_s3_get_presigned_url(
        self,
        bucketName: str,
        expiration: str,
        objectKey: str,
    ) -> Dict[str, Any]:
        """Generates a time-limited presigned URL for a specific object in an AWS S3 bucket, granting temporary access to that object without requiring AWS credentials. Use this tool when you need to securely share a private S3 object with external users or services. The URL expires after the configured duration and should not be treated as a permanent link. Does not modify the object.

        Args:
            bucketName: The name of the S3 bucket. (required)
            expiration: The expiration time for the generated URL (e.g., in ISO 8601 format). (required)
            objectKey: The key of the object within the S3 bucket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_s3_list_buckets(
        self,
    ) -> Dict[str, Any]:
        """Lists all AWS S3 buckets owned by the authenticated account, returning their names and creation dates. Use this tool when you need to discover existing buckets before uploading objects or managing storage. Does not return objects within buckets — use aws_s3_list_objects for that. Does not modify any resources.
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_s3_list_objects(
        self,
        bucketName: Optional[str] = None,
        listtype: Optional[str] = None,
        prefix: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all objects stored in a specified AWS S3 bucket, returning their keys, sizes, and last-modified timestamps. Use this tool when you need to discover or audit files stored in a bucket. Does not return file content — use aws_s3_get_object to download a specific file. Does not modify any data.

        Args:
            bucketName: 
            listtype: 
            prefix: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_s3_put_object(
        self,
        body: Dict[str, Any],
        bucketName: str,
        fileName: str,
    ) -> Dict[str, Any]:
        """Uploads a single object to a specified AWS S3 bucket at the given key path. Use this tool when you need to store any file type in S3. If an object already exists at the specified key, it will be overwritten. For image files, consider aws_s3_put_object_image. For files larger than 100 MB, consider aws_s3_create_multipart_upload instead. This action creates or replaces an object and cannot be undone without versioning enabled.

        Args:
            body: Request body for AWS Simple Storage Service. (required)
            bucketName: Name of the bucket in AWS Simple Storage Service. (required)
            fileName: Name of the file in AWS Simple Storage Service. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_s3_put_object_image(
        self,
        bucketName: str,
        fileName: str,
        body: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads an image file as an object to a specified AWS S3 bucket and path using a PUT request with region-specific endpoint. Use this tool when you need to store an image in a region-specific S3 bucket. If the object already exists at the specified key, it will be overwritten. For non-image files, use aws_s3_put_object. For large images, consider aws_s3_create_multipart_upload instead.

        Args:
            bucketName: Name of the S3 bucket. (required)
            fileName: Name of the file to be uploaded. (required)
            body: The data to be uploaded to the S3 bucket.
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_s3_put_parquet_object(
        self,
        body: List[Any],
        bucketName: str,
        fileName: str,
    ) -> Dict[str, Any]:
        """Uploads a Parquet-formatted file as an object to a specified AWS S3 bucket, optimized for analytics and columnar data storage. Use this tool when you need to store structured data in Parquet format for downstream analytics processing (e.g., with AWS Athena or Redshift Spectrum). If the object already exists at the specified key, it will be overwritten. For non-Parquet files, use aws_s3_put_object.

        Args:
            body:  (required)
            bucketName: Name of the S3 bucket. (required)
            fileName: Name of the file to be uploaded. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_s3_upload_image(
        self,
        bucketName: Optional[str] = None,
        imageBase64: Optional[str] = None,
        imageExtension: Optional[str] = None,
        imageName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads an image file to a specified AWS S3 bucket for storage, processing, or sharing. Use this tool when you need to store an image in S3. For uploading non-image binary files, use aws_s3_put_object. For large files requiring multipart upload, use aws_s3_create_multipart_upload instead. This action creates or overwrites an object in S3 and cannot be undone without versioning enabled.

        Args:
            bucketName: The name of the storage bucket where the image will be uploaded.
            imageBase64: The image file encoded as a Base64 string.
            imageExtension: The file extension for the image (for example: jpg, png, gif).
            imageName: The filename to assign to the uploaded image.
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_s3_upload_part(
        self,
        bucketName: str,
        fileName: str,
        partNumber: str,
        uploadId: str,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Uploads a single part of a multipart upload to a specified AWS S3 bucket as part of a larger file transfer. Use this tool for each segment of a large file after initiating a multipart upload with aws_s3_create_multipart_upload. Each part must be at least 5 MB except for the last part. After all parts are uploaded, finalize the upload with aws_s3_complete_multipart_upload.

        Args:
            bucketName: Name of the S3 bucket. (required)
            fileName: Name of the file to be uploaded or accessed. (required)
            partNumber: Number of the part being uploaded. (required)
            uploadId: ID of the multipart upload. (required)
            body: Body of the request for AWS Simple Storage Service.
        Returns:
            API response as a dictionary.
        """
        ...

