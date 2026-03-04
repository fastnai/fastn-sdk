"""Fastn Xata connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class XataConnector:
    """Xata connector ().

    Provides 1 tools.
    """

    def xata_execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a SQL or Xata-native query against a connected Postgres-compatible database (Xata-hosted, AWS RDS, Amazon Aurora, GCP Cloud SQL, or Azure Database) and returns the resulting rows or confirmation of data manipulation. Use this for SELECT queries to retrieve data, or DML statements (INSERT, UPDATE, DELETE) to modify data. Be aware that DML statements cause immediate, potentially irreversible changes to the database. Do not use this tool if you are unsure of the querys impact on production data — validate queries in a non-production environment first.

        Args:
            query: The Xata query string. (required)
        Returns:
            API response as a dictionary.
        """
        ...

