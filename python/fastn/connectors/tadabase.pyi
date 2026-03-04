"""Fastn Tadabase connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class TadabaseConnector:
    """Tadabase connector ().

    Provides 8 tools.
    """

    def tadabase_create_record(
        self,
        tableId: str,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new record in a specified Tadabase table identified by tableId. Use this tool when you need to insert new data into a table. Do not use this tool to modify an existing record — use tadabase_update_record instead. This action permanently adds a new record to the table.

        Args:
            tableId: The ID of the table to interact with. (required)
            body: Data for the record to be created or updated.
        Returns:
            API response as a dictionary.
        """
        ...

    def tadabase_delete_record(
        self,
        recordId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific record from a Tadabase table identified by tableId and recordId. Use this tool only when a record must be removed from the database. This action is irreversible — the deleted record cannot be recovered. Do not use this tool to update or archive a record — use tadabase_update_record instead.

        Args:
            recordId: The ID of the record to access. (required)
            tableId: The ID of the table containing the record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tadabase_get_record(
        self,
        recordId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single record from a Tadabase table using its unique record ID. Use this tool when you already know the specific recordId and need to fetch its full details. Do not use this tool to retrieve multiple records — use tadabase_list_records instead. Does not modify any data.

        Args:
            recordId: The unique identifier of the record. (required)
            tableId: The unique identifier of the table containing the record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tadabase_list_fields(
        self,
        tableId: str,
        fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all fields (columns) defined in a specified Tadabase table. Use this tool when you need to discover the schema or structure of a table, such as field names, types, and configuration. Do not use this tool to retrieve record data — use tadabase_list_records instead. Does not modify any data.

        Args:
            tableId: The ID of the table to access. (required)
            fields: Specify which fields to retrieve (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def tadabase_list_records(
        self,
        tableId: str,
        display_names: Optional[str] = None,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists multiple records from a specified Tadabase table, optionally filtered by criteria. Use this tool when you need to retrieve a collection of records from a table identified by tableId. Do not use this tool to retrieve a single record by ID — use tadabase_get_record instead. Does not modify any data.

        Args:
            tableId: The ID of the table to access. (required)
            display_names: Specifies whether to include display names in the response.
            limit: Limits the number of records returned.
            page: Specifies the page number for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def tadabase_list_records_sorted(
        self,
        tableId: str,
        order: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists records from a Tadabase table sorted by one or more specified conditions. Use this tool when you need to retrieve an ordered list of records from a specific table (identified by tableId) using sort criteria. Do not use this tool to retrieve a single record by ID — use tadabase_get_record instead. Does not modify any data.

        Args:
            tableId: The ID of the table to access. (required)
            order: Specifies the order of the results (e.g., asc, desc).
            order_by: Specifies the field to order the results by.
        Returns:
            API response as a dictionary.
        """
        ...

    def tadabase_list_tables(
        self,
    ) -> Dict[str, Any]:
        """Lists all data tables available in the Tadabase application. Use this tool when you need to discover which tables exist before querying records or fields. Do not use this tool to retrieve records or fields from a specific table. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def tadabase_update_record(
        self,
        body: Dict[str, Any],
        recordId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Updates an existing record in a Tadabase table identified by tableId and recordId with new field values. Use this tool when you need to modify one or more fields of an existing record. Do not use this tool to create a new record — use tadabase_create_record instead. This action overwrites the specified fields on the existing record.

        Args:
            body: Data for the record to be updated or created. (required)
            recordId: The ID of the record to be updated or retrieved. (required)
            tableId: The ID of the table containing the record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

