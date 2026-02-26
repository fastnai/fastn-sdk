"""Fastn Redis connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class RedisConnector:
    """Redis connector ().

    Provides 3 tools.
    """

    def add(
        self,
        expired_in_seconds: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a new item or record using the 'add' operation in the specified connector.

        Args:
            expired_in_seconds: Token expiration time in seconds.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete(
        self,
    ) -> Dict[str, Any]:
        """Removes an existing record using the 'delete' operation in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get(
        self,
    ) -> Dict[str, Any]:
        """Retrieves data using the 'get' operation in the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

