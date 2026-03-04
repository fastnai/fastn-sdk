"""Fastn influx_db connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _InfluxDbQueryDataDialect(TypedDict, total=False):
    annotations: List[Any]
    commentPrefix: str
    dateTimeFormat: str
    delimiter: str
    header: bool

class _InfluxDbQueryDataExtern(TypedDict, total=False):
    body: List[Any]
    imports: List[Any]
    name: str
    package: Dict[str, Any]
    type: str

class InfluxDbConnector:
    """influx_db connector ().

    Provides 12 tools.
    """

    def influx_db_create_bucket(
        self,
        name: str,
        orgID: str,
        description: Optional[str] = None,
        retentionRules: Optional[List[Any]] = None,
        rp: Optional[str] = None,
        schemaType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new bucket in InfluxDB Cloud for storing time series data. A bucket belongs to a specific organization and can be configured with a retention period. Use this when setting up a new data storage namespace. Do not use this to update an existing bucket.

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

    def influx_db_create_organization(
        self,
        name: str,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new organization in InfluxDB Cloud with specified details such as name and configuration. Use this when onboarding a new team or tenant that requires its own isolated InfluxDB environment. Do not use this to update an existing organization.

        Args:
            name: Name of the object. (required)
            description: Description of the object.
        Returns:
            API response as a dictionary.
        """
        ...

    def influx_db_delete_bucket(
        self,
        bucketId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific bucket from InfluxDB Cloud by its bucket ID. All time series data stored in the bucket will be irreversibly destroyed. Use this only when the bucket and its data are no longer needed. Do not use this if you only want to update bucket settings or retention policies.

        Args:
            bucketId: ID of the InfluxDB bucket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def influx_db_delete_organization(
        self,
        orgId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific organization from InfluxDB Cloud by its organization ID. Use this to remove an organization and all associated resources. This action is irreversible — all data, buckets, dashboards, and members belonging to the organization will be permanently lost. Do not use this if you only need to update or rename the organization.

        Args:
            orgId: The ID of the InfluxDB organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def influx_db_get_bucket(
        self,
        bucketId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single InfluxDB Cloud bucket identified by its bucket ID, including its name, organization, and retention rules. Use this when you need metadata for a specific bucket. Do not use this to list all buckets or to write data.

        Args:
            bucketId: ID of the InfluxDB bucket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def influx_db_get_organization(
        self,
        orgId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single InfluxDB Cloud organization identified by its organization ID, including its name, status, and configuration. Use this when you need metadata for a specific organization. Do not use this to list all organizations or to modify organization data.

        Args:
            orgId: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def influx_db_list_buckets(
        self,
        after: Optional[str] = None,
        limit: Optional[str] = None,
        name: Optional[str] = None,
        offset: Optional[str] = None,
        org: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all buckets available in the InfluxDB Cloud organization. Use this to enumerate buckets when you do not have a specific bucket ID, or to audit existing storage namespaces. Do not use this to retrieve details of a single bucket by ID.

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

    def influx_db_list_organizations(
        self,
        descending: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        org: Optional[str] = None,
        orgID: Optional[str] = None,
        userID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all organizations accessible in InfluxDB Cloud. Use this to enumerate organizations when you do not have a specific organization ID, or to audit existing organizations. Do not use this to retrieve details of a single organization by ID.

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

    def influx_db_query_data(
        self,
        orgID: str,
        query: str,
        dialect: Optional[_InfluxDbQueryDataDialect] = None,
        extern: Optional[_InfluxDbQueryDataExtern] = None,
        now: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a Flux or SQL query against a specified InfluxDB Cloud organization and returns matching time series data. Use this for real-time analytics, dashboards, or data exploration. Requires a valid query string and organization context. Do not use this to write or delete data.

        Args:
            orgID: ID of the organization. (required)
            query: InfluxQL query to execute. (required)
            dialect: Dialect options for data import.
            extern: External data to import.
            now: Timestamp representing the current time.
            params: Additional parameters for the request.
            type: Type of data being sent.
        Returns:
            API response as a dictionary.
        """
        ...

    def influx_db_update_bucket(
        self,
        bucketId: str,
        name: str,
        description: Optional[str] = None,
        retentionRules: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing InfluxDB Cloud bucket, such as its name, description, or retention period, identified by its bucket ID. Use this to modify bucket settings without affecting stored data. Do not use this to delete a bucket or write data into it.

        Args:
            bucketId: The ID of the bucket. (required)
            name: The name of the bucket. (required)
            description: An optional description for the bucket.
            retentionRules: 
        Returns:
            API response as a dictionary.
        """
        ...

    def influx_db_update_organization(
        self,
        name: str,
        orgId: str,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the metadata of an existing InfluxDB Cloud organization, such as its name or description, identified by its organization ID. Use this to modify organization-level settings. Do not use this to delete an organization or manage its buckets.

        Args:
            name: Name of the resource. (required)
            orgId: The ID of the organization. (required)
            description: Description of the resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def influx_db_write_data(
        self,
        bucket: str,
        org: str,
        body: Optional[str] = None,
        orgID: Optional[str] = None,
        precision: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Writes time series data points to a specified InfluxDB Cloud bucket using line protocol format. Use this to ingest metrics, events, or sensor readings. This action appends data to the bucket and may be subject to retention policies. Do not use this to query or delete data.

        Args:
            bucket: The name of the bucket to query. (required)
            org: The name of the organization. (required)
            body: The body of the request (if applicable).
            orgID: The ID of the organization.
            precision: The precision of the data (e.g., 'ns', 'u', 'ms', 's', 'm', 'h').
        Returns:
            API response as a dictionary.
        """
        ...

