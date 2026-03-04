"""Fastn SQL connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class SqlConnector:
    """SQL connector ().

    Provides 1 tools.
    """

    def sql_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a SQL query against the connected SQL database to retrieve or manipulate data. Use this tool when you need to run SELECT statements to fetch records, or DML statements (INSERT, UPDATE, DELETE) to modify data in the database. Do NOT use this tool for schema-level operations such as creating or dropping tables—confirm your database permissions before executing write operations. Side effect: write queries (INSERT, UPDATE, DELETE) will permanently modify data in the database; ensure queries are correct before execution.

        Args:
            query: The SQL query to be executed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

