"""Fastn Google Cloud SQL connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class GoogleCloudSqlConnector:
    """Google Cloud SQL connector ().

    Provides 1 tools.
    """

    def google_cloud_sql_execute_query(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a SQL query against a specified Google Cloud SQL database instance (MySQL, PostgreSQL, or SQL Server) using a Python code execution backend. Use this tool when you need to retrieve, insert, update, or delete data in a Cloud SQL database. Do not use this tool for BigQuery queries — use google_bigquery_run_query for that. Write operations (INSERT, UPDATE, DELETE, DROP) are irreversible and will permanently modify or delete data in the target database. Ensure queries are validated before execution.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

