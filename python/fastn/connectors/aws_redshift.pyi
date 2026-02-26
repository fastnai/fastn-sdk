"""Fastn AWS Redshift connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AwsRedshiftConnector:
    """AWS Redshift connector ().

    Provides 2 tools.
    """

    def execute_query(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a specified query against the database using the Database Connector, allowing retrieval or manipulation of data based on the provided SQL statement.

        Args:
            query: The SQL query string to execute.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_table_schema(
        self,
        table_name: str,
        table_schema: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the schema of a specified table within the database using the Database Connector, providing details about the table's structure, including column names and data types.

        Args:
            table_name:  (required)
            table_schema: 
        Returns:
            API response as a dictionary.
        """
        ...

