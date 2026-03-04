"""Fastn Stackby connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class StackbyConnector:
    """Stackby connector ().

    Provides 5 tools.
    """

    def stackby_create_rows(
        self,
        records: List[Any],
        stackId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Creates one or more new rows in a specified table in a Stackby stack with the provided field values. Use this when you need to add new records to a Stackby table. Provide the stackId, tableId, and the field data for each new row. This action creates permanent records in the table.

        Args:
            records:  (required)
            stackId: Identifier for the stack. (required)
            tableId: Identifier for the table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stackby_delete_rows(
        self,
        rowIds: List[Any],
        stackId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes one or more rows from a specified table in a Stackby stack, identified by their row IDs. Use this when you need to remove specific records from a Stackby table. This action is irreversible — deleted rows cannot be recovered. Provide the stackId, tableId, and one or more rowIds to target the correct records.

        Args:
            rowIds: An array of row identifiers. (required)
            stackId: Identifier for the stack. (required)
            tableId: Identifier for the table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def stackby_get_row_by_id(
        self,
        stackId: str,
        tableId: str,
        rowIds: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific row from a Stackby table by its unique row ID. Use this when you have a known rowId and need to fetch that exact record. Use stackby_list_rows instead when you need to retrieve all rows in a table without filtering by ID. Does not modify any data.

        Args:
            stackId: The ID of the stack. (required)
            tableId: The ID of the table. (required)
            rowIds: An array of row IDs.
        Returns:
            API response as a dictionary.
        """
        ...

    def stackby_list_rows(
        self,
        stackId: str,
        tableId: str,
        latest: Optional[bool] = None,
        offset: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all rows in a specified table within a Stackby stack. Use this when you need to retrieve the full contents of a table for browsing, auditing, or bulk processing. Use stackby_get_row_by_id instead when you only need a specific row by ID. Does not modify any data.

        Args:
            stackId: The ID of the stack containing the table. (required)
            tableId: The ID of the table to query. (required)
            latest: Filter by latest records.
            offset: Offset for pagination.
            pageSize: Number of records per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def stackby_update_rows(
        self,
        records: List[Any],
        stackId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Updates one or more existing rows in a specified table in a Stackby stack with new field values. Use this when you need to modify the data in existing records. Provide the stackId, tableId, and the updated field values for each target row. This action overwrites existing cell data for the specified fields.

        Args:
            records:  (required)
            stackId: Identifier for the stack. (required)
            tableId: Identifier for the table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

