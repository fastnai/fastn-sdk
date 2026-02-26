"""Fastn Noloco connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class NolocoConnector:
    """Noloco connector ().

    Provides 4 tools.
    """

    def add_records(
        self,
    ) -> Dict[str, Any]:
        """Adds new records to the database using the designated connector, allowing for the input of multiple entries at once.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_record(
        self,
        id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific record from the database through the specified connector, effectively removing it from the system.

        Args:
            id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records(
        self,
        after: Optional[str] = None,
        fields: Optional[str] = None,
        first: Optional[str] = None,
        tableName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves records from the database using the appropriate connector for data retrieval.

        Args:
            after: 
            fields: 
            first: 
            tableName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_record(
        self,
    ) -> Dict[str, Any]:
        """Updates an existing record in the database with new information through the chosen connector, ensuring the record is current.
        Returns:
            API response as a dictionary.
        """
        ...

