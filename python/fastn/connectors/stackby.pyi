"""Fastn Stackby connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class StackbyConnector:
    """Stackby connector ().

    Provides 5 tools.
    """

    def create_rows(
        self,
        records: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new row in the database using the specified connector.

        Args:
            records:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_rows(
        self,
        rowIds: List[Any],
    ) -> Dict[str, Any]:
        """Deletes a row from the database via the specified connector.

        Args:
            rowIds: An array of row identifiers. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def list_rows(
        self,
        latest: Optional[bool] = None,
        offset: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all rows in the database using the specified connector.

        Args:
            latest: Filter by latest records.
            offset: Offset for pagination.
            pageSize: Number of records per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def retrieve_rows_by_id(
        self,
        rowIds: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves a row by its unique ID from the database via the specified connector.

        Args:
            rowIds: An array of row IDs.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_rows(
        self,
        records: List[Any],
    ) -> Dict[str, Any]:
        """Updates an existing row in the database using the specified connector.

        Args:
            records:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

