"""Fastn Google BigQuery connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class GoogleBigqueryConnector:
    """Google BigQuery connector ().

    Provides 9 tools.
    """

    def google_bigquery_generate_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Generates a short-lived OAuth 2.0 access token by exchanging credentials with the Google OAuth 2.0 token endpoint. Use this tool when you need to obtain an access token to authorize subsequent Google BigQuery API calls. Do not use this tool to generate refresh tokens or authorization tokens — use google_bigquery_generate_refresh_token or google_bigquery_generate_auth_token for those. Calling this tool triggers a network request to Googles token endpoint and returns a bearer token with a limited expiry.

        Args:
            client_id: Client ID for the Google BigQuery application. (required)
            client_secret: Client secret for the Google BigQuery application. (required)
            code: Authorization code received from Google BigQuery OAuth flow. (required)
            redirect_uri: Redirect URI registered for the Google BigQuery application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_bigquery_generate_auth_token(
        self,
        assertion: str,
        grant_type: str,
    ) -> Dict[str, Any]:
        """Generates an OAuth 2.0 authorization token for secure access to Google BigQuery by calling the Google OAuth 2.0 token endpoint. Use this tool when you need to authenticate a user or service account before executing queries or managing BigQuery resources. Do not use this tool to generate refresh tokens — use google_bigquery_generate_refresh_token for that. Returns a bearer token required for authorized BigQuery API requests.

        Args:
            assertion: Assertion for authentication. (required)
            grant_type: Grant type for authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def google_bigquery_generate_refresh_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a long-lived OAuth 2.0 refresh token for Google BigQuery by exchanging an authorization code with the Google OAuth 2.0 token endpoint. Use this tool when you need to obtain a refresh token that can be used to generate new access tokens without re-prompting the user for credentials. Do not use this tool if you only need a short-lived access token — use google_bigquery_generate_access_token for that. This operation involves a network call to Googles token endpoint and returns credentials that provide ongoing API access.

        Args:
            client_id: 
            client_secret: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_bigquery_get_table(
        self,
        datasetId: str,
        projectId: str,
        tableId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        prettyPrint: Optional[bool] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed metadata for a specific table in Google BigQuery, including schema, row count, creation time, and storage size. Use this tool when you need to inspect the structure or properties of a single known table identified by projectId, datasetId, and tableId. Do not use this tool to list all tables in a dataset — use google_bigquery_list_tables for that. This is a read-only operation and does not modify any table data.

        Args:
            datasetId: The ID of the dataset that contains the table. (required)
            projectId: The ID of the Google Cloud project that owns the dataset and table. (required)
            tableId: The ID of the table within the dataset. (required)
            access_token: OAuth 2.0 access token used as an alternative to a bearer token for authentication.
            alt: Data format for the response (e.g., json).
            callback: JSONP callback function name for wrapping the response.
            fields: Selector specifying which fields to include in a partial response.
            key: API key that identifies the project and provides API access, quota, and reports. Alternative to OAuth tokens.
            prettyPrint: Returns response with indentations and line breaks for readability when set.
            quotaUser: Available to use for quota purposes for server-side applications. Overrides userIp if both are provided.
            uploadType: Legacy upload protocol for media (e.g., 'media', 'multipart').
            upload_protocol: Upload protocol for media (e.g., 'raw', 'multipart').
            xgafv: Version of error format (often used as a parameter in Google APIs).
        Returns:
            API response as a dictionary.
        """
        ...

    def google_bigquery_list_datasets(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all datasets within a specified Google BigQuery project, returning dataset IDs and basic metadata. Use this tool when you need to discover which datasets exist inside a known project identified by projectId. Do not use this tool to list tables within a dataset — use google_bigquery_list_tables for that. This is a read-only operation and does not modify any data.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_bigquery_list_projects(
        self,
    ) -> Dict[str, Any]:
        """Lists all Google Cloud projects associated with the authenticated account that are accessible via the BigQuery API. Use this tool when you need to discover available project IDs before performing dataset or table operations. Do not use this tool to list datasets or tables — use google_bigquery_list_datasets or google_bigquery_list_tables for those. This is a read-only operation and does not modify any resources.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_bigquery_list_tables(
        self,
        datasetId: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all tables within a specified dataset in Google BigQuery, returning table IDs, types, and basic metadata. Use this tool when you need to discover which tables exist inside a known dataset identified by projectId and datasetId. Do not use this tool to retrieve the full schema or row data of a specific table — use google_bigquery_get_table for that. This is a read-only operation and does not modify any data.

        Args:
            datasetId: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_bigquery_run_query(
        self,
        connectionProperties: List[Any],
        jobCreationMode: str,
        project_id: str,
        queryParameters: List[Any],
        continuous: Optional[bool] = None,
        createSession: Optional[bool] = None,
        defaultDataset: Optional[Dict[str, Any]] = None,
        dryRun: Optional[bool] = None,
        kind: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None,
        location: Optional[str] = None,
        maxResults: Optional[int] = None,
        maximumBytesBilled: Optional[int] = None,
        parameterMode: Optional[str] = None,
        preserveNulls: Optional[bool] = None,
        query: Optional[str] = None,
        requestId: Optional[str] = None,
        timeoutMs: Optional[int] = None,
        useLegacySql: Optional[bool] = None,
        useQueryCache: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Executes a synchronous SQL query against a specified Google BigQuery project and returns query results. Use this tool when you need to run ad-hoc or analytical SQL statements against large datasets stored in BigQuery. Requires a valid projectId and a SQL query string in the request body. Do not use this tool for schema inspection or table listing — use google_bigquery_get_table or google_bigquery_list_tables for those. Query execution may incur data processing costs proportional to the amount of data scanned.

        Args:
            connectionProperties: Connection properties for the Google BigQuery job. (required)
            jobCreationMode: Mode for creating the Google BigQuery job. (required)
            project_id: Google Cloud Project ID. (required)
            queryParameters:  (required)
            continuous: Whether the query is continuous.
            createSession: Whether to create a session for the query.
            defaultDataset: Default dataset for the query.
            dryRun: Whether to perform a dry run of the query.
            kind: Kind of the query job.
            labels: Labels for the query job.
            location: Location of the query job.
            maxResults: Maximum number of results to return.
            maximumBytesBilled: Maximum bytes billed for the query.
            parameterMode: Parameter mode for the query.
            preserveNulls: Whether to preserve nulls in the query results.
            query: The SQL query to execute.
            requestId: Request ID for the query.
            timeoutMs: Timeout for the query in milliseconds.
            useLegacySql: Whether to use legacy SQL.
            useQueryCache: Whether to use the query cache.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_bigquery_test_table_permissions(
        self,
        datasetId: str,
        permissions: List[Any],
        projectId: str,
        tableId: str,
        access_token: Optional[str] = None,
        alt: Optional[str] = None,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        prettyPrint: Optional[bool] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Tests whether the caller has a specified set of IAM permissions on a specific BigQuery table by calling the testIamPermissions endpoint. Use this tool when you need to verify access rights before performing read, write, or administrative operations on a table. Requires projectId, datasetId, tableId, and the list of permissions to test. Do not use this tool to grant or revoke permissions — it is a read-only check that does not modify any access controls.

        Args:
            datasetId: The ID of the BigQuery dataset containing the target table. (required)
            permissions: An array of permission strings to check or modify for the specified resource. (required)
            projectId: The ID of the Google Cloud project that owns the dataset and table. (required)
            tableId: The ID of the BigQuery table to which the request applies. (required)
            access_token: OAuth 2.0 access token passed as a query parameter (alternate to providing a bearer token in the auth object).
            alt: Data format for the response, for example 'json'.
            callback: Name of the JavaScript callback function that handles the response (for JSONP).
            fields: Selector specifying which fields to include in a partial response.
            key: API key that identifies the project and provides API access, quota, and reports.
            prettyPrint: Returns response with indentations and line breaks for readability.
            quotaUser: Available for quota purposes for server-side applications. Overrides userIp if provided.
            uploadType: Legacy upload protocol for media. Common values: 'media', 'multipart'.
            upload_protocol: Upload protocol for media, such as 'raw' or 'multipart'.
            xgafv: V1 error format version. Used to specify the error format version.
        Returns:
            API response as a dictionary.
        """
        ...

