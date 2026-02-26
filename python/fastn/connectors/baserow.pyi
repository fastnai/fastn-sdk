"""Fastn Baserow connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BaserowConnector:
    """Baserow connector ().

    Provides 7 tools.
    """

    def create_row(
        self,
    ) -> Dict[str, Any]:
        """Creates a new row in the specified table of the database connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_row(
        self,
        rowId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Deletes a row from the specified table in the database connector.

        Args:
            rowId: The ID of the specific row. (required)
            tableId: The ID of the target table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_fields(
        self,
        tableId: str,
    ) -> Dict[str, Any]:
        """Fetches the fields of a specific table in the provided database connector.

        Args:
            tableId: ID of the table to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_row(
        self,
        user_field_names: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific row from a table in the selected database connector.

        Args:
            user_field_names: Indicates whether to include user field names.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_rows(
        self,
        user_field_names: bool,
    ) -> Dict[str, Any]:
        """Lists all rows within a specified table in the given database connector.

        Args:
            user_field_names: Indicates whether to include user-defined field names in the response. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def list_tables(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all tables within the specified database connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_row(
        self,
    ) -> Dict[str, Any]:
        """Updates an existing row in the specified table of the database connector.
        Returns:
            API response as a dictionary.
        """
        ...

