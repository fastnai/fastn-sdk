"""Fastn Microsoft SQL Server connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MicrosoftSqlServerConnector:
    """Microsoft SQL Server connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
    ) -> Dict[str, Any]:
        """Executes a query in the specified database connector, retrieving or manipulating data based on the provided SQL command.
        Returns:
            API response as a dictionary.
        """
        ...

