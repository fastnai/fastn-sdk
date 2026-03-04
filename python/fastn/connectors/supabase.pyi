"""Fastn Supabase connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class SupabaseConnector:
    """Supabase connector ().

    Provides 4 tools.
    """

    def supabase_delete_rows(
        self,
        condition: Optional[str] = None,
        key: Optional[str] = None,
        tableName: Optional[str] = None,
        value: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes one or more rows from a specified Supabase table based on a filter condition (key, operator, and value). Use this tool when you need to remove records that match a specific condition from a Supabase database table. Do not use this tool to update row data (use supabase_update_rows) or when you are unsure of the filter — incorrect conditions may delete unintended rows. This operation is irreversible; deleted rows cannot be recovered unless a backup exists.

        Args:
            condition: 
            key: 
            tableName: 
            value: 
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_insert_rows(
        self,
        body: List[Any],
        tableName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Inserts one or more new rows into a specified Supabase table. Use this tool when you need to add new records to a Supabase database table. Do not use this tool to modify existing rows (use supabase_update_rows) or to remove rows (use supabase_delete_rows). This operation permanently adds records to the table and may fail if required fields are missing or unique constraints are violated.

        Args:
            body:  (required)
            tableName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_list_rows(
        self,
        range: Optional[str] = None,
        select: Optional[str] = None,
        tableName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves rows from a specified Supabase table, with optional filtering criteria. Use this tool when you need to read or inspect records in a Supabase database table. Do not use this tool to modify, insert, or delete data — use supabase_update_rows, supabase_insert_rows, or supabase_delete_rows for those operations. This is a read-only operation with no side effects.

        Args:
            range: 
            select: 
            tableName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def supabase_update_rows(
        self,
        body: Dict[str, Any],
        condition: Optional[str] = None,
        key: Optional[str] = None,
        tableName: Optional[str] = None,
        value: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates one or more existing rows in a specified Supabase table that match a filter condition (key, operator, and value). Use this tool when you need to modify field values in records that already exist in the table. Do not use this tool to add new rows (use supabase_insert_rows) or to delete rows (use supabase_delete_rows). Ensure the filter condition is precise — an overly broad condition may update unintended rows. This operation modifies data in place and is permanent unless manually reversed.

        Args:
            body:  (required)
            condition: 
            key: 
            tableName: 
            value: 
        Returns:
            API response as a dictionary.
        """
        ...

