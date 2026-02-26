"""Fastn Tadabase connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TadabaseConnector:
    """Tadabase connector ().

    Provides 8 tools.
    """

    def create_record(
        self,
    ) -> Dict[str, Any]:
        """Creates a new record in the database.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_record(
        self,
        recordId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified record from the database.

        Args:
            recordId: The ID of the record to access. (required)
            tableId: The ID of the table containing the record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_fields(
        self,
        fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the fields or columns of a specified table in the database.

        Args:
            fields: Specify which fields to retrieve (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_record(
        self,
        recordId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific record from the database using its unique identifier.

        Args:
            recordId: The unique identifier of the record. (required)
            tableId: The unique identifier of the table containing the record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records(
        self,
        display_names: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves multiple records from the database based on specified criteria.

        Args:
            display_names: Specifies whether to include display names in the response.
            limit: Limits the number of records returned.
            page: Specifies the page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of all available tables in the database.
        Returns:
            API response as a dictionary.
        """
        ...

    def sort_by_condition(
        self,
        order: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sorts records based on specified conditions in the database.

        Args:
            order: Specifies the order of the results (e.g., asc, desc).
            order_by: Specifies the field to order the results by.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_record(
        self,
    ) -> Dict[str, Any]:
        """Updates an existing record in the database with new information.
        Returns:
            API response as a dictionary.
        """
        ...

