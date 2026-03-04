"""Fastn Microsoft SQL Server connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MicrosoftSqlServerConnector:
    """Microsoft SQL Server connector ().

    Provides 1 tools.
    """

    def microsoft_sql_server_execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a raw SQL query against a Microsoft SQL Server database, returning result sets for SELECT statements or applying data modifications for INSERT, UPDATE, and DELETE statements. Use this tool when you need to read, write, or manipulate structured data in the database using a custom SQL command. Do not use this tool for schema management operations such as creating or dropping tables unless explicitly required; prefer dedicated DDL tools if available. Note: write operations (INSERT, UPDATE, DELETE) permanently modify data and cannot be automatically undone.

        Args:
            query:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

