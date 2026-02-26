"""Fastn Xata connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class XataConnector:
    """Xata connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a query in the database connector to retrieve or manipulate data based on specified criteria.

        Args:
            query: The Xata query string. (required)
        Returns:
            API response as a dictionary.
        """
        ...

