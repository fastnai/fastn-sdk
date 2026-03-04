"""Fastn SingleStore connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class SinglestoreConnector:
    """SingleStore connector ().

    Provides 1 tools.
    """

    def singlestore_execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a SQL query against a SingleStore database and returns the results. Use this to run SELECT statements for data retrieval, or DML statements (INSERT, UPDATE, DELETE) for data modification. Suitable for ad-hoc analytics, application queries, and data inspection tasks. Be aware that DML statements will modify data and are not automatically reversible; DDL statements (DROP, TRUNCATE) may cause irreversible data loss. Do not use this tool if you only need metadata about available tools or connectors.

        Args:
            query: The SingleStore query string. (required)
        Returns:
            API response as a dictionary.
        """
        ...

