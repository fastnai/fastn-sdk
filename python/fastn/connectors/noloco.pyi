"""Fastn Noloco connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class NolocoConnector:
    """Noloco connector ().

    Provides 4 tools.
    """

    def noloco_create_records(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Creates one or more new records in your Noloco app. Use this tool when you need to add multiple entries to a data collection in a single operation. Do NOT use this tool to update existing records—use noloco_update_record instead. This action permanently writes new data to your app.

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def noloco_delete_record(
        self,
        id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific record from your Noloco app. Use this tool when you need to remove a single record identified by its ID. Do NOT use this tool to update records—use noloco_update_record instead. This action is irreversible; the deleted record cannot be recovered.

        Args:
            id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def noloco_list_records(
        self,
        after: Optional[str] = None,
        fields: Optional[str] = None,
        first: Optional[str] = None,
        tableName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of records from your Noloco app. Use this tool when you need to fetch multiple records from a data collection, optionally filtered or paginated. Do NOT use this tool to fetch, update, or delete a single record—use the appropriate noloco_get_record, noloco_update_record, or noloco_delete_record tools instead. This is a read-only operation with no side effects.

        Args:
            after: 
            fields: 
            first: 
            tableName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def noloco_update_record(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Updates field values of an existing record in your Noloco app. Use this tool when you need to modify specific fields of a single record. Do NOT use this tool to create new records—use noloco_create_records instead. This action overwrites the specified fields of the targeted record.

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

