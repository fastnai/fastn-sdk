"""Fastn CrateDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class CratedbConnector:
    """CrateDB connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a database query using the database connector, allowing you to retrieve, update, or manipulate data stored within the database.

        Args:
            query: The SQL query string. (required)
        Returns:
            API response as a dictionary.
        """
        ...

