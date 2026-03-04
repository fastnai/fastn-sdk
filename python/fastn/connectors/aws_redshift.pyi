"""Fastn AWS Redshift connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AwsRedshiftConnector:
    """AWS Redshift connector ().

    Provides 2 tools.
    """

    def aws_redshift_execute_query(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a SQL statement against an AWS Redshift database and returns the result. Use this tool to retrieve, insert, update, or delete data. Warning: DML and DDL statements (INSERT, UPDATE, DELETE, DROP, etc.) will modify or permanently delete data and cannot be undone. Do not use this tool if you only need table structure — use aws_redshift_get_table_schema instead.

        Args:
            query: The SQL query string to execute.
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_redshift_get_table_schema(
        self,
        table_name: str,
        table_schema: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the schema of a specified table in an AWS Redshift database, returning column names and data types. Use this tool when you need to inspect or understand the structure of a table before constructing queries. Does not return row data and does not modify the database.

        Args:
            table_name:  (required)
            table_schema: 
        Returns:
            API response as a dictionary.
        """
        ...

