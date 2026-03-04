"""Fastn SeaTable connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class SeatableConnector:
    """SeaTable connector ().

    Provides 18 tools.
    """

    def seatable_append_columns(
        self,
        base_uuid: str,
        columns: List[Any],
        table_name: str,
    ) -> Dict[str, Any]:
        """Appends one or more new columns to the end of a SeaTable table in a single batch operation. Use this tool when you need to add multiple columns at once to an existing table. Do NOT use this tool if you need to insert a column at a specific position — use the insert column tool instead.

        Args:
            base_uuid: The UUID of the SeaTable base. (required)
            columns:  (required)
            table_name: The name of the SeaTable table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_append_row(
        self,
        base_uuid: str,
        rows: List[Any],
        table_name: str,
        apply_default: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Appends a new row with the provided field values to the end of a specified SeaTable table. Use this tool when you need to add a new record to an existing table. Do NOT use this tool to update an existing row — use the update row tool instead.

        Args:
            base_uuid: The UUID of the SeaTable base. (required)
            rows:  (required)
            table_name: The name of the table to which data will be added. (required)
            apply_default: Boolean indicating whether to apply default values for missing fields.
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_create_base(
        self,
        name: str,
        color: Optional[str] = None,
        icon: Optional[str] = None,
        workspace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new base (database) in SeaTable. Use this tool when you need to set up a new top-level database to store tables and data. Do NOT use this tool to create a new table within an existing base — use the create table tool instead.

        Args:
            name: Name of the entry. (required)
            color: Color of the entry (optional).
            icon: Icon for the entry (optional).
            workspace_id: ID of the workspace where the entry will be created (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_create_table(
        self,
        base_uuid: str,
        columns: List[Any],
        table_name: str,
    ) -> Dict[str, Any]:
        """Creates a new empty table in a specified SeaTable base. Use this tool when you need to add a new table to an existing base. Do NOT use this tool to create a new base — use the create base tool instead. After creation, use the insert column or append columns tools to define the tables schema.

        Args:
            base_uuid: The UUID of the SeaTable base. (required)
            columns:  (required)
            table_name: The name of the table to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_delete_base(
        self,
        name: Optional[str] = None,
        workspaceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific base (database) from a SeaTable workspace. Use this tool when you need to remove an entire base and all of its tables and data. Do NOT use this tool if you only want to delete a single table or row — use the dedicated delete table or delete row tools. This action is irreversible: all data within the base will be permanently lost.

        Args:
            name: 
            workspaceId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_delete_column(
        self,
        base_uuid: str,
        column: str,
        table_name: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific column from a SeaTable table. Use this tool when you need to remove an existing column and all its data from a table in a base. Do NOT use this tool if you only want to rename or reorder a column — use the update column name tool instead. This action is irreversible: all data stored in the deleted column will be permanently lost.

        Args:
            base_uuid: The UUID of the SeaTable base to access. (required)
            column: The name of the column to retrieve data from. (required)
            table_name: The name of the table to retrieve data from. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_delete_row(
        self,
        base_uuid: str,
        row_ids: List[Any],
        table_name: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific row from a SeaTable table. Use this tool when you need to remove an existing row and all its data. Do NOT use this tool if you only want to clear or update cell values — use the update row tool instead. This action is irreversible: the deleted row cannot be recovered.

        Args:
            base_uuid: The UUID of the SeaTable base. (required)
            row_ids: An array of row IDs to be processed. (required)
            table_name: The name of the table in the SeaTable base. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_delete_table(
        self,
        base_uuid: str,
        table_name: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific table and all of its data from a SeaTable base. Use this tool when you need to remove an entire table, including all its rows and columns. Do NOT use this tool if you only want to delete a single row or column — use the dedicated delete row or delete column tools. This action is irreversible: all data in the table will be permanently lost.

        Args:
            base_uuid: The UUID of the SeaTable base. (required)
            table_name: The name of the table to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_get_base_token(
        self,
        baseName: str,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves the access token for a specific SeaTable base identified by workspace ID and base name. Use this tool when you need an authentication token to perform API operations directly against a base. Do NOT use this tool to retrieve general account credentials or tokens for other services.

        Args:
            baseName: The name of the SeaTable base. (required)
            workspaceId: The ID of the SeaTable workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_get_row(
        self,
        base_uuid: str,
        rowId: str,
        table_name: str,
        convert_keys: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a single row by its ID from a specified SeaTable table, returning all field values for that row. Use this tool when you know the exact row ID and need to fetch its data. Do NOT use this tool to retrieve multiple rows — use the list rows tool instead.

        Args:
            base_uuid: The UUID of the SeaTable base. (required)
            rowId: The ID of the row to retrieve. (required)
            table_name: The name of the table to retrieve data from. (required)
            convert_keys: Specifies whether to convert keys.
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_insert_column(
        self,
        base_uuid: str,
        column_name: str,
        column_type: str,
        table_name: str,
        anchor_column: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Inserts a new column at a specified position in a SeaTable table. Use this tool when you need to add a single column at a particular location within an existing table. Do NOT use this tool to append multiple columns at once — use the append columns tool instead. The column will be empty upon creation.

        Args:
            base_uuid: The UUID of the SeaTable base where the column will be created. (required)
            column_name: The name of the new column. (required)
            column_type: The data type of the new column (e.g., text, number, date). (required)
            table_name: The name of the table to which the column will be added. (required)
            anchor_column: The name of the column to use as an anchor (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_list_bases(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the list of all bases (databases) accessible to the authenticated user in SeaTable. Use this tool when you need to discover available bases or find a bases ID or name before performing operations on it. Do NOT use this tool to retrieve tables within a base — use the list tables or list columns tools for that.
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_list_columns(
        self,
        base_uuid: str,
        table_name: str,
        view_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full list of columns defined in a specified SeaTable table, including their names, types, and configuration. Use this tool when you need to inspect the schema of a table. Do NOT use this tool to retrieve row data — use the list rows tool instead.

        Args:
            base_uuid: The UUID of the SeaTable base. (required)
            table_name: The name of the SeaTable to retrieve data from. (required)
            view_name: The name of the view within the table to retrieve data from.
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_list_rows(
        self,
        base_uuid: str,
        table_name: str,
        convert_keys: Optional[str] = None,
        limit: Optional[str] = None,
        start: Optional[str] = None,
        view_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of rows in a specified SeaTable table, returning all field values for each row. Use this tool when you need to read multiple records from a table. Do NOT use this tool to fetch a single row by ID — use the get row tool instead. Large tables may return paginated results.

        Args:
            base_uuid: The UUID of the SeaTable base. (required)
            table_name: The name of the table to retrieve data from. (required)
            convert_keys: Specifies how keys should be converted.
            limit: Limits the number of records retrieved.
            start: Specifies the starting point for record retrieval.
            view_name: The name of the view to retrieve data from.
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_rename_table(
        self,
        base_uuid: str,
        new_table_name: str,
        table_name: str,
    ) -> Dict[str, Any]:
        """Renames a specific table within a SeaTable base. Use this tool when you need to change the display name of an existing table without modifying its data or structure. Do NOT use this tool to delete or restructure a table — use the appropriate dedicated tools for those operations.

        Args:
            base_uuid: The UUID of the SeaTable base containing the table. (required)
            new_table_name: The new name for the table. (required)
            table_name: The current name of the table to be renamed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_update_base(
        self,
        name: str,
        workspaceId: str,
        color: Optional[str] = None,
        icon: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the metadata or settings of a specific SeaTable base, such as its name or icon. Use this tool when you need to modify properties of an existing base without altering its tables or data. Do NOT use this tool to update row or column data — use the update row or update column name tools instead.

        Args:
            name: The name of the item. (required)
            workspaceId: The unique identifier for the SeaTable workspace. (required)
            color: The color of the item.
            icon: The icon associated with the item.
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_update_column_name(
        self,
        base_uuid: str,
        column: str,
        new_column_name: str,
        op_type: str,
        table_name: str,
    ) -> Dict[str, Any]:
        """Updates the display name of a specific column in a SeaTable table. Use this tool when you need to rename an existing column without changing its data or type. Do NOT use this tool to delete a column, change column type, or modify row data — use the appropriate dedicated tools for those operations.

        Args:
            base_uuid: The unique identifier of the SeaTable base. (required)
            column: The current name of the column to be renamed. (required)
            new_column_name: The new name for the column. (required)
            op_type: Specifies the type of operation.  Must be 'rename_column'. (required)
            table_name: The name of the table containing the column to be renamed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def seatable_update_row(
        self,
        base_uuid: str,
        table_name: str,
        updates: List[Any],
    ) -> Dict[str, Any]:
        """Updates the field values of a specific existing row in a SeaTable table. Use this tool when you need to modify data in one or more cells of an existing row. Do NOT use this tool to add a new row — use the append row tool instead. Only the fields provided in the request will be updated; other fields remain unchanged.

        Args:
            base_uuid: The UUID of the SeaTable base. (required)
            table_name: The name of the table to update. (required)
            updates:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

