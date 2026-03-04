"""Fastn Power BI connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class PowerBiConnector:
    """Power BI connector ().

    Provides 6 tools.
    """

    def power_bi_add_rows(
        self,
        datasetId: str,
        rows: List[Any],
        tableName: str,
    ) -> Dict[str, Any]:
        """Adds new rows of data to a specified table within a Power BI push dataset. Use this tool when you need to append records to an existing dataset table for real-time dashboard updates. Do not use this tool to modify existing rows or change table schema; use the update table tool for schema changes. This operation appends data and does not deduplicate or overwrite existing rows.

        Args:
            datasetId: The ID of the dataset to interact with. (required)
            rows:  (required)
            tableName: The name of the table within the dataset. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def power_bi_create_dataset(
        self,
        name: str,
        tables: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new push dataset in the authenticated users Power BI workspace. Use this tool when you need to define a new dataset with its tables and schema before pushing data into it. Do not use this tool if the dataset already exists; use the update table tool to modify an existing datasets schema instead. This operation provisions a new dataset resource in Power BI and cannot be undone without explicitly deleting it.

        Args:
            name: Name of the dataset or operation. (required)
            tables:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def power_bi_generate_token(
        self,
        client_id: str,
        client_secret: str,
        grant_type: str,
        password: str,
        username: str,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a new OAuth 2.0 access token for Power BI using a specified Azure Active Directory tenant via the Microsoft identity platform. Use this tool at the start of an authentication flow or when no valid token exists. Do not use this tool to renew an already-issued token; use the refresh token tool instead. The returned token must be included in subsequent Power BI API requests as a Bearer token.

        Args:
            client_id: The client ID for authentication. (required)
            client_secret: The client secret for authentication (if using client credentials). (required)
            grant_type: The grant type for authentication (e.g., password, client_credentials). (required)
            password: The user's password for authentication. (required)
            username: The username for authentication. (required)
            tenantId: The ID of the Power BI tenant.
        Returns:
            API response as a dictionary.
        """
        ...

    def power_bi_get_dataset(
        self,
        datasetId: str,
    ) -> Dict[str, Any]:
        """Retrieves metadata for a single Power BI dataset by its dataset ID from the authenticated users workspace. Use this tool when you need to confirm a dataset exists or inspect its properties such as name, tables, and connectivity mode. Do not use this tool to retrieve row-level data from the dataset; it returns structural metadata only.

        Args:
            datasetId: ID of the dataset in Power BI. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def power_bi_refresh_token(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        refresh_token: str,
    ) -> Dict[str, Any]:
        """Refreshes an existing OAuth 2.0 access token for Power BI using the Microsoft identity platform organizations endpoint. Use this tool when a previously issued access token has expired and you need to obtain a new one without requiring the user to re-authenticate. Do not use this tool to generate a brand-new token for a first-time authentication flow; use the generate token tool instead. This call exchanges a refresh token for a new access token and may invalidate the old refresh token.

        Args:
            client_id: Client ID for Power BI API authentication. (required)
            client_secret: Client secret for Power BI API authentication. (required)
            redirect_uri: Redirect URI for Power BI API authentication. (required)
            refresh_token: Refresh token for Power BI API authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def power_bi_update_table(
        self,
        columns: List[Any],
        datasetId: str,
        name: str,
        tableName: str,
    ) -> Dict[str, Any]:
        """Updates the schema of an existing table within a specified Power BI push dataset. Use this tool when the column structure of a table needs to change, such as adding, removing, or renaming columns. Do not use this tool to insert or modify row data; use the add rows tool instead. This operation overwrites the existing table schema and may cause data loss if columns are removed.

        Args:
            columns:  (required)
            datasetId: ID of the Power BI dataset. (required)
            name: Name of the dataset. (required)
            tableName: Name of the table within the Power BI dataset. (required)
        Returns:
            API response as a dictionary.
        """
        ...

