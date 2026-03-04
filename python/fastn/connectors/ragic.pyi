"""Fastn Ragic connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class RagicConnector:
    """Ragic connector ().

    Provides 5 tools.
    """

    def ragic_create_record(
        self,
        body: Dict[str, Any],
        database: str,
        region: str,
        sheetIndex: str,
        tabFolder: str,
        v: str,
        api: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new record in a specified Ragic sheet, identified by the region, database, tab folder, and sheet index. Use this tool when you need to add a new entry to a Ragic sheet. Do not use this tool to update an existing record — use ragic_update_record instead.

        Args:
            body: The request body (currently empty). (required)
            database: The name of the database. (required)
            region: The region of the database. (required)
            sheetIndex: The index of the sheet. (required)
            tabFolder: The name of the tab folder. (required)
            v: API version. (required)
            api: 
        Returns:
            API response as a dictionary.
        """
        ...

    def ragic_delete_record(
        self,
        database: str,
        recordId: str,
        region: str,
        sheetIndex: str,
        tabFolder: str,
        v: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific record from a Ragic sheet, identified by the region, database, tab folder, sheet index, and record ID. Use this tool only when you intend to irreversibly remove a record from the database. This action cannot be undone. Do not use this tool to update a record — use ragic_update_record instead.

        Args:
            database: Name of the database. (required)
            recordId: ID of the record. (required)
            region: Region of the database. (required)
            sheetIndex: Index of the sheet. (required)
            tabFolder: Name of the tab folder. (required)
            v: Version of the API being called. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ragic_get_record(
        self,
        database: str,
        recordId: str,
        region: str,
        sheetIndex: str,
        tabFolder: str,
        v: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single record from a Ragic sheet, identified by the region, database, tab folder, sheet index, and record ID. Use this tool when you need to inspect or read all fields of one specific record. Do not use this tool to retrieve multiple records — use ragic_list_records instead.

        Args:
            database: Name of the database. (required)
            recordId: ID of the record. (required)
            region: Region of the database. (required)
            sheetIndex: Index of the sheet. (required)
            tabFolder: Name of the tab folder. (required)
            v: API version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ragic_list_records(
        self,
        database: str,
        region: str,
        sheetIndex: str,
        tabFolder: str,
        v: str,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all records from a specified Ragic sheet, identified by the region, database, tab folder, and sheet index. Use this tool when you need to browse or process multiple entries from a sheet at once. Do not use this tool to retrieve a single known record — use ragic_get_record instead.

        Args:
            database: Name of the database. (required)
            region: Region of the database. (required)
            sheetIndex: Index of the sheet. (required)
            tabFolder: Name of the tab folder. (required)
            v: Specifies the API version. (required)
            limit: Limit the number of results.
            offset: Offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def ragic_update_record(
        self,
        database: str,
        recordId: str,
        region: str,
        sheetIndex: str,
        tabFolder: str,
        v: str,
        body: Optional[Dict[str, Any]] = None,
        doLinkLoad: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields of an existing record in a Ragic sheet, identified by the region, database, tab folder, sheet index, and record ID. Use this tool when you need to modify specific fields of an existing entry without replacing the entire record. Do not use this tool to create a new record — use ragic_create_record instead.

        Args:
            database: Name of the database. (required)
            recordId: ID of the record. (required)
            region: Region of the database. (required)
            sheetIndex: Index of the sheet. (required)
            tabFolder: Name of the tab folder. (required)
            v: API version. (required)
            body: Body of the API request.
            doLinkLoad: Indicates whether to load links.
        Returns:
            API response as a dictionary.
        """
        ...

