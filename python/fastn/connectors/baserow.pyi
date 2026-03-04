"""Fastn Baserow connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class BaserowConnector:
    """Baserow connector ().

    Provides 7 tools.
    """

    def baserow_create_row(
        self,
        tableId: str,
        body: Optional[Dict[str, Any]] = None,
        user_field_names: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new row in a specified Baserow table, identified by table ID. Use this to insert a new record with field values into the table. Do not use this to update an existing row. This action permanently adds a row to the table.

        Args:
            tableId: The ID of the table. (required)
            body: Body of the API request.
            user_field_names: Indicates whether to include user field names.
        Returns:
            API response as a dictionary.
        """
        ...

    def baserow_delete_row(
        self,
        rowId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a single row from a specified Baserow table, identified by table ID and row ID. Use this to remove a record that is no longer needed. Do not use this to update or archive a row — deletion is irreversible and cannot be undone.

        Args:
            rowId: The ID of the specific row. (required)
            tableId: The ID of the target table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def baserow_get_row(
        self,
        rowId: str,
        tableId: str,
        user_field_names: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Retrieves a single row from a specified Baserow table using the table ID and row ID. Use this when you need the full field data for a known row. Do not use this to list multiple rows or search by field value — use baserow_list_rows instead. This is a read-only operation with no side effects.

        Args:
            rowId: The ID of the row to access. (required)
            tableId: The ID of the table containing the row. (required)
            user_field_names: Indicates whether to include user field names.
        Returns:
            API response as a dictionary.
        """
        ...

    def baserow_list_fields(
        self,
        tableId: str,
    ) -> Dict[str, Any]:
        """Lists all fields (columns) defined in a specified Baserow table, identified by table ID, including field names, types, and configuration. Use this to understand the schema of a table before reading or writing rows. Do not use this to retrieve row data — use baserow_list_rows or baserow_get_row instead. This is a read-only operation with no side effects.

        Args:
            tableId: ID of the table to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def baserow_list_rows(
        self,
        tableId: str,
        user_field_names: bool,
    ) -> Dict[str, Any]:
        """Lists all rows within a specified Baserow table, identified by table ID. Use this to retrieve or paginate through all records in a table. Do not use this to retrieve a single known row — use baserow_get_row instead. This is a read-only operation with no side effects.

        Args:
            tableId: The ID of the target table. (required)
            user_field_names: Indicates whether to include user-defined field names in the response. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def baserow_list_tables(
        self,
    ) -> Dict[str, Any]:
        """Lists all tables across all databases available in the connected Baserow account. Use this to discover available tables and their IDs before performing row or field operations. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def baserow_update_row(
        self,
        body: Dict[str, Any],
        rowId: str,
        tableId: str,
        user_field_names: str,
    ) -> Dict[str, Any]:
        """Updates one or more field values on an existing row in a specified Baserow table, identified by table ID and row ID. Use this to modify record data without replacing the entire row. Do not use this to create a new row or delete an existing one. Changes are applied immediately and overwrite the specified field values.

        Args:
            body: Body of the request (currently empty). (required)
            rowId: The ID of the row to be accessed. (required)
            tableId: The ID of the table to be accessed. (required)
            user_field_names: Names of user fields. (required)
        Returns:
            API response as a dictionary.
        """
        ...

