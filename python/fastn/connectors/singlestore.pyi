"""Fastn SingleStore connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SinglestoreConnector:
    """SingleStore connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Executes a database query using the appropriate connector.

        Args:
            query: The SingleStore query string. (required)
        Returns:
            API response as a dictionary.
        """
        ...

