"""Fastn Supabase connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SupabaseConnector:
    """Supabase connector ().

    Provides 4 tools.
    """

    def delete_rows(
        self,
        condition: Optional[str] = None,
        key: Optional[str] = None,
        value: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes rows from the specified database connector, enabling you to remove records from tables based on specific conditions.

        Args:
            condition: 
            key: 
            value: 
        Returns:
            API response as a dictionary.
        """
        ...

    def insert_rows(
        self,
    ) -> Dict[str, Any]:
        """Inserts new rows into the specified database connector, enabling you to add new records to tables quickly and efficiently.
        Returns:
            API response as a dictionary.
        """
        ...

    def read_rows(
        self,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Reads rows from the specified database connector, allowing you to retrieve data from tables based on defined criteria.

        Args:
            select: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_rows(
        self,
        condition: Optional[str] = None,
        key: Optional[str] = None,
        value: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates existing rows in the specified database connector, allowing you to modify data in tables according to the provided identifiers and new values.

        Args:
            condition: 
            key: 
            value: 
        Returns:
            API response as a dictionary.
        """
        ...

