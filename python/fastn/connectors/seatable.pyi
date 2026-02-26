"""Fastn SeaTable connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SeatableConnector:
    """SeaTable connector ().

    Provides 18 tools.
    """

    def append_columns(
        self,
        columns: List[Any],
        table_name: str,
    ) -> Dict[str, Any]:
        """Appends a new column to a specified table in the database connector.

        Args:
            columns:  (required)
            table_name: The name of the SeaTable table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def append_row(
        self,
        rows: List[Any],
        table_name: str,
        apply_default: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Appends a new row to a specified table in the database connector.

        Args:
            rows:  (required)
            table_name: The name of the table to which data will be added. (required)
            apply_default: Boolean indicating whether to apply default values for missing fields.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_base(
        self,
        name: str,
        color: Optional[str] = None,
        icon: Optional[str] = None,
        workspace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new base in the database connector.

        Args:
            name: Name of the entry. (required)
            color: Color of the entry (optional).
            icon: Icon for the entry (optional).
            workspace_id: ID of the workspace where the entry will be created (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def create_table(
        self,
        columns: List[Any],
        table_name: str,
    ) -> Dict[str, Any]:
        """Creates a new table within a specified base in the database connector.

        Args:
            columns:  (required)
            table_name: The name of the table to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_base(
        self,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing base from the database connector.

        Args:
            name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_column(
        self,
        column: str,
        table_name: str,
    ) -> Dict[str, Any]:
        """Deletes a specified column from a table in the database connector.

        Args:
            column: The name of the column to retrieve data from. (required)
            table_name: The name of the table to retrieve data from. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_row(
        self,
        row_ids: List[Any],
        table_name: str,
    ) -> Dict[str, Any]:
        """Deletes a specified row from a table in the database connector.

        Args:
            row_ids: An array of row IDs to be processed. (required)
            table_name: The name of the table in the SeaTable base. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_table(
        self,
        table_name: str,
    ) -> Dict[str, Any]:
        """Deletes a specified table from a base in the database connector.

        Args:
            table_name: The name of the table to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_base_token(
        self,
        baseName: str,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Obtains a secure token for accessing a specific base in the database connector.

        Args:
            baseName: The name of the SeaTable base. (required)
            workspaceId: The ID of the SeaTable workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_bases(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of bases in the database connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_columns(
        self,
        table_name: str,
        view_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of columns in a specified table within the database connector.

        Args:
            table_name: The name of the SeaTable to retrieve data from. (required)
            view_name: The name of the view within the table to retrieve data from.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_row(
        self,
        table_name: str,
        convert_keys: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific row in a table within the database connector.

        Args:
            table_name: The name of the table to retrieve data from. (required)
            convert_keys: Specifies whether to convert keys.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_rows(
        self,
        table_name: str,
        convert_keys: Optional[str] = None,
        limit: Optional[str] = None,
        start: Optional[str] = None,
        view_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of rows from a specified table in the database connector.

        Args:
            table_name: The name of the table to retrieve data from. (required)
            convert_keys: Specifies how keys should be converted.
            limit: Limits the number of records retrieved.
            start: Specifies the starting point for record retrieval.
            view_name: The name of the view to retrieve data from.
        Returns:
            API response as a dictionary.
        """
        ...

    def insert_column(
        self,
        column_name: str,
        column_type: str,
        table_name: str,
        anchor_column: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Inserts a new column at a specified position in a table within the database connector.

        Args:
            column_name: The name of the new column. (required)
            column_type: The data type of the new column (e.g., text, number, date). (required)
            table_name: The name of the table to which the column will be added. (required)
            anchor_column: The name of the column to use as an anchor (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def rename_table(
        self,
        new_table_name: str,
        table_name: str,
    ) -> Dict[str, Any]:
        """Renames an existing table within a specified base in the database connector.

        Args:
            new_table_name: The new name for the table. (required)
            table_name: The current name of the table to be renamed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_base(
        self,
        name: str,
        color: Optional[str] = None,
        icon: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing base in the database connector.

        Args:
            name: The name of the item. (required)
            color: The color of the item.
            icon: The icon associated with the item.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_column_name(
        self,
        column: str,
        new_column_name: str,
        op_type: str,
        table_name: str,
    ) -> Dict[str, Any]:
        """Updates the name of an existing column in a specified table within the database connector.

        Args:
            column: The current name of the column to be renamed. (required)
            new_column_name: The new name for the column. (required)
            op_type: Specifies the type of operation.  Must be 'rename_column'. (required)
            table_name: The name of the table containing the column to be renamed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_row(
        self,
        table_name: str,
        updates: List[Any],
    ) -> Dict[str, Any]:
        """Updates the details of a specific row in a table within the database connector.

        Args:
            table_name: The name of the table to update. (required)
            updates:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

