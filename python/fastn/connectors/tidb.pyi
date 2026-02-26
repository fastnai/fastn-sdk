"""Fastn TiDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TidbConnector:
    """TiDB connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a database query using the specified database connector.

        Args:
            query: The TiDB query string. (required)
        Returns:
            API response as a dictionary.
        """
        ...

