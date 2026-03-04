"""Fastn Postgres connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class PostgresConnector:
    """Postgres connector ().

    Provides 1 tools.
    """

    def postgres_execute_query(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a raw SQL query against a PostgreSQL database and returns the result set. Use this tool when you need to run SELECT, INSERT, UPDATE, DELETE, or DDL statements directly against a Postgres instance. Not suitable for NoSQL or non-relational datastores. Modifying queries (INSERT, UPDATE, DELETE, DROP) are destructive and irreversible; use with caution.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

