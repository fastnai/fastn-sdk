"""Fastn influxDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class InfluxdbConnector:
    """influxDB connector ().

    Provides 12 tools.
    """

    def create_bucket(
        self,
        name: str,
        orgID: str,
        description: Optional[str] = None,
        retentionRules: Optional[List[Any]] = None,
        rp: Optional[str] = None,
        schemaType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new bucket in the storage service with specified parameters such as name and configuration.

        Args:
            name: The name of the bucket to be created. (required)
            orgID: The ID of the organization to create the bucket in. (required)
            description: An optional description for the bucket.
            retentionRules: 
            rp: The retention policy for the bucket.
            schemaType: The schema type for the bucket.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_organization(
        self,
        name: str,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new organization in the system with specified details such as name and configuration.

        Args:
            name: Name of the object. (required)
            description: Description of the object.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_bucket(
        self,
        bucketId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified bucket from the storage service permanently.

        Args:
            bucketId: ID of the InfluxDB bucket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_organization(
        self,
        orgId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified organization from the system permanently.

        Args:
            orgId: The ID of the InfluxDB organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_bucket(
        self,
        bucketId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific bucket identified by its unique identifier.

        Args:
            bucketId: ID of the InfluxDB bucket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_buckets(
        self,
        after: Optional[str] = None,
        limit: Optional[str] = None,
        name: Optional[str] = None,
        offset: Optional[str] = None,
        org: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all buckets in the storage service.

        Args:
            after: Return data after this timestamp.
            limit: Maximum number of results to return.
            name: Name of the Bucket.
            offset: Number of results to skip.
            org: Name of the organization.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organization(
        self,
        orgId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific organization identified by its unique identifier.

        Args:
            orgId: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organizations(
        self,
        descending: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        org: Optional[str] = None,
        orgID: Optional[str] = None,
        userID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all organizations within the system.

        Args:
            descending: Sort results in descending order (true/false).
            limit: Maximum number of results to return.
            offset: Number of results to skip.
            org: Name of the organization.
            orgID: ID of the organization.
            userID: ID of the user.
        Returns:
            API response as a dictionary.
        """
        ...

    def query_data(
        self,
        orgID: str,
    ) -> Dict[str, Any]:
        """Queries data stored in a specific bucket in the storage service using defined criteria.

        Args:
            orgID: ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_bucket(
        self,
        name: str,
        description: Optional[str] = None,
        retentionRules: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the properties of an existing bucket in the storage service based on the provided changes.

        Args:
            name: The name of the bucket. (required)
            description: An optional description for the bucket.
            retentionRules: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_organization(
        self,
        name: str,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the properties of an existing organization in the system based on the provided changes.

        Args:
            name: Name of the resource. (required)
            description: Description of the resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def write_data(
        self,
        bucket: str,
        org: str,
        orgID: Optional[str] = None,
        precision: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Writes data to a specified bucket in the storage service for storage and retrieval.

        Args:
            bucket: The name of the bucket to query. (required)
            org: The name of the organization. (required)
            orgID: The ID of the organization.
            precision: The precision of the data (e.g., 'ns', 'u', 'ms', 's', 'm', 'h').
        Returns:
            API response as a dictionary.
        """
        ...

