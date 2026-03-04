"""Fastn AITable connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _AitableCreateFieldProperty(TypedDict, total=False):
    defaultValue: str

class AitableConnector:
    """AITable connector ().

    Provides 9 tools.
    """

    def aitable_create_datasheet(
        self,
        description: Optional[str] = None,
        fields: Optional[List[Any]] = None,
        name: Optional[str] = None,
        spaceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new datasheet within a specified AITable space. Use this when you need to set up a new table to store structured data inside an existing space. Do not use this to create records or fields within an already existing datasheet.

        Args:
            description: 
            fields: 
            name: 
            spaceId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aitable_create_field(
        self,
        dataSheetId: Optional[str] = None,
        name: Optional[str] = None,
        property: Optional[_AitableCreateFieldProperty] = None,
        spaceId: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new field (column) in an AITable datasheet within a specified space. Use this when you need to add a new data column to an existing datasheet. Do not use this to update existing fields or add records.

        Args:
            dataSheetId: 
            name: 
            property: 
            spaceId: 
            type: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aitable_create_records(
        self,
        dataSheetId: Optional[str] = None,
        records: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates one or more new records in an AITable datasheet. Use this when you need to add new rows of data to an existing datasheet. Do not use this to update existing records or create new datasheets.

        Args:
            dataSheetId: 
            records: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aitable_delete_records(
        self,
        commaSeparatedRecordIds: Optional[str] = None,
        dataSheetId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes one or more specified records from an AITable datasheet. Use this when you need to permanently remove existing rows from a datasheet by their record IDs. Do not use this to update or archive records — deletion is irreversible and the data cannot be recovered.

        Args:
            commaSeparatedRecordIds: 
            dataSheetId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aitable_list_fields(
        self,
        datasheetId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all fields (columns) defined in an AITable datasheet. Use this when you need to inspect the schema or available columns of a datasheet. Do not use this to retrieve records or views.

        Args:
            datasheetId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aitable_list_records(
        self,
        dataSheetId: Optional[str] = None,
        viewId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of records from an AITable datasheet. Use this when you need to read or display rows of data from a specific datasheet. Supports filtering and pagination. Do not use this to create, update, or delete records.

        Args:
            dataSheetId: 
            viewId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aitable_list_spaces(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all spaces accessible in the authenticated AITable account. Use this when you need to discover available workspaces before interacting with their datasheets or fields. Do not use this to retrieve datasheets, records, or views.
        Returns:
            API response as a dictionary.
        """
        ...

    def aitable_list_views(
        self,
        dataSheetId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all views defined in an AITable datasheet. Use this when you need to discover available views (e.g., grid, gallery, kanban) within a datasheet. Do not use this to retrieve records or field definitions.

        Args:
            dataSheetId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def aitable_update_record(
        self,
        dataSheetId: Optional[str] = None,
        records: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates one or more existing records in an AITable datasheet by applying field-level changes. Use this when you need to modify the values of specific fields in existing rows. Do not use this to create new records or delete records.

        Args:
            dataSheetId: 
            records: 
        Returns:
            API response as a dictionary.
        """
        ...

