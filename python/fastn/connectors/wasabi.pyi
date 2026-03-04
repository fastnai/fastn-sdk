"""Fastn Wasabi connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class WasabiConnector:
    """Wasabi connector ().

    Provides 3 tools.
    """

    def wasabi_get_object(
        self,
        bucketName: str,
        object: str,
    ) -> Dict[str, Any]:
        """Downloads and returns the contents of a specific object from a Wasabi bucket. Use this tool when you need to read or retrieve a stored file by its bucket name and object key. Do not use this tool to list available objects or buckets; use wasabi_list_buckets for discovery instead. This operation is read-only and has no side effects.

        Args:
            bucketName: The name of the bucket containing the object. (required)
            object: The name of the object within the bucket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def wasabi_list_buckets(
        self,
    ) -> Dict[str, Any]:
        """Lists all S3-compatible buckets available in the authenticated Wasabi account. Use this tool when you need to discover which buckets exist before performing object-level operations. Returns bucket names and creation dates. Does not return object contents or metadata within buckets.
        Returns:
            API response as a dictionary.
        """
        ...

    def wasabi_put_object(
        self,
        body: Dict[str, Any],
        bucketName: str,
        object: str,
    ) -> Dict[str, Any]:
        """Uploads a new object to a specified Wasabi bucket, or fully replaces an existing object at the same key. Use this tool when you need to store or overwrite a file in Wasabi cloud storage. Requires the target bucket name and object key (path). Note: if an object with the same key already exists, it will be permanently overwritten without warning. This operation is irreversible for the previous version unless versioning is enabled on the bucket.

        Args:
            body: Body of the request (may be empty depending on the operation). (required)
            bucketName: The name of the bucket containing the object. (required)
            object: The name of the object within the bucket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

