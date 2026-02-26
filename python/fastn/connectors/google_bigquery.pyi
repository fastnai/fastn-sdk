"""Fastn Google BigQuery connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GoogleBigqueryConnector:
    """Google BigQuery connector ().

    Provides 7 tools.
    """

    def big_query(
        self,
        connectionProperties: List[Any],
        jobCreationMode: str,
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
        """Executes SQL queries against Google BigQuery to manage and analyze large datasets.

        Args:
            connectionProperties: Connection properties for the Google BigQuery job. (required)
            jobCreationMode: Mode for creating the Google BigQuery job. (required)
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

    def generate_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Generates an access token required for authorized API calls, granting permission to access specific resources.

        Args:
            client_id: Client ID for the Google BigQuery application. (required)
            client_secret: Client secret for the Google BigQuery application. (required)
            code: Authorization code received from Google BigQuery OAuth flow. (required)
            redirect_uri: Redirect URI registered for the Google BigQuery application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_auth_token(
        self,
        assertion: str,
        grant_type: str,
    ) -> Dict[str, Any]:
        """Creates an authentication token for secure access to an API or service, enabling user verification.

        Args:
            assertion: Assertion for authentication. (required)
            grant_type: Grant type for authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_refresh_token(
        self,
    ) -> Dict[str, Any]:
        """Generates a refresh token that can be used to obtain new access tokens for a connected service.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_datasets(
        self,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches datasets within a specific Google BigQuery project, providing an overview of available data collections.

        Args:
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_projects(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of projects associated with the Google Cloud account, allowing you to manage and collaborate on projects.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables(
        self,
        datasetId: Optional[str] = None,
        projectId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains the tables within a specified dataset in Google BigQuery, allowing users to view and interact with individual data tables.

        Args:
            datasetId: 
            projectId: 
        Returns:
            API response as a dictionary.
        """
        ...

