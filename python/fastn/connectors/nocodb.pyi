"""Fastn NocoDB connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class NocodbConnector:
    """NocoDB connector ().

    Provides 8 tools.
    """

    def nocodb_count_records(
        self,
        tableId: str,
        viewId: Optional[str] = None,
        where: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns the total count of records in a specified NocoDB table. Use this tool when you need to know how many rows exist in a table, optionally filtered by query conditions, without retrieving the actual record data. Do NOT use this tool to fetch record details — use nocodb_list_table_records instead. This is a read-only operation with no side effects.

        Args:
            tableId: ID of the table to be accessed. (required)
            viewId: ID of the view to be used for the request.
            where: A WHERE clause to filter the data.
        Returns:
            API response as a dictionary.
        """
        ...

    def nocodb_create_records(
        self,
        body: List[Any],
        tableId: str,
    ) -> Dict[str, Any]:
        """Creates one or more new records in a specified NocoDB table. Use this tool when you need to add new rows of data to a given table. Do NOT use this tool to update existing records — use nocodb_update_records instead. This action permanently writes new data to the table.

        Args:
            body:  (required)
            tableId: The unique identifier of the table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def nocodb_delete_records(
        self,
        body: List[Any],
        tableId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes one or more records from a specified NocoDB table. Use this tool when you need to remove records identified within the request body from a given table. Do NOT use this tool to update records — use nocodb_update_records instead. This action is irreversible; deleted records cannot be recovered.

        Args:
            body:  (required)
            tableId: The ID of the table to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def nocodb_get_record(
        self,
        recordId: str,
        tableId: str,
        fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single record from a specified NocoDB table by its record ID. Use this tool when you need to fetch all field values for one specific record. Do NOT use this tool to retrieve multiple records — use nocodb_list_table_records instead. This is a read-only operation with no side effects.

        Args:
            recordId: The ID of the record to access. (required)
            tableId: The ID of the table containing the record. (required)
            fields: Specifies which fields to include in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def nocodb_link_records(
        self,
        body: List[Any],
        linkFieldId: str,
        recordId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Creates a link between two records in NocoDB using a defined link field. Use this tool when you need to establish a relational association between a source record and one or more target records via a specific link field ID. Do NOT use this tool to unlink records or to update non-relational fields — use nocodb_update_records instead. This action modifies the relational data structure of the table.

        Args:
            body:  (required)
            linkFieldId: The ID of the link field. (required)
            recordId: The ID of the record. (required)
            tableId: The ID of the table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def nocodb_list_linked_records(
        self,
        fieldId: str,
        linkFieldId: str,
        tableId: str,
        fields: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        sort: Optional[str] = None,
        where: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all records linked to a specific record in NocoDB via a defined link field. Use this tool when you need to fetch the related records associated with a source record through a relational link field. Do NOT use this tool to create or remove links — use nocodb_link_records for that. This is a read-only operation with no side effects.

        Args:
            fieldId: ID of the field. (required)
            linkFieldId: ID of the linked field. (required)
            tableId: ID of the target table. (required)
            fields: Comma-separated list of fields to retrieve.
            limit: Maximum number of records to return.
            offset: Number of records to skip.
            sort: Field to sort by (e.g., 'name ASC', 'date DESC').
            where: SQL WHERE clause for filtering records.
        Returns:
            API response as a dictionary.
        """
        ...

    def nocodb_list_table_records(
        self,
        tableId: str,
        fields: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        sort: Optional[str] = None,
        viewId: Optional[str] = None,
        where: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all records from a specified NocoDB table. Use this tool when you need to fetch a full list of rows from a given table, optionally filtered or paginated. Do NOT use this tool to retrieve a single record — use nocodb_get_record instead. This is a read-only operation with no side effects.

        Args:
            tableId: ID of the target table. (required)
            fields: Comma-separated list of fields to include in the result.
            limit: Number of records to return.
            offset: Number of records to skip.
            sort: Comma-separated list of fields to sort by.
            viewId: ID of the view to use for data retrieval.
            where: WHERE clause for filtering the data.
        Returns:
            API response as a dictionary.
        """
        ...

    def nocodb_update_records(
        self,
        tableId: str,
        body: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates one or more existing records in a specified NocoDB table. Use this tool when you need to modify field values of existing records identified within the request body for a given table. Do NOT use this tool to create new records — use nocodb_create_records instead. This action overwrites the specified fields of the targeted records.

        Args:
            tableId: The ID of the table to interact with. (required)
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

