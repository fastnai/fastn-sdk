"""Fastn Postgres connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class PostgresConnector:
    """Postgres connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a database query using the designated database connector.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

