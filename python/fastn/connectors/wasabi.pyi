"""Fastn Wasabi connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class WasabiConnector:
    """Wasabi connector ().

    Provides 3 tools.
    """

    def get_buckets(
        self,
    ) -> Dict[str, Any]:
        """Lists all available buckets in the storage system of the connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_object(
        self,
        bucketName: str,
        object: str,
    ) -> Dict[str, Any]:
        """Retrieves an object from the specified storage in the connector.

        Args:
            bucketName: The name of the bucket containing the object. (required)
            object: The name of the object within the bucket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def put_object(
        self,
    ) -> Dict[str, Any]:
        """Uploads a new object or replaces an existing one in the specified storage of the connector.
        Returns:
            API response as a dictionary.
        """
        ...

