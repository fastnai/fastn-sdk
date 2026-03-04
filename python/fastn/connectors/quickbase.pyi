"""Fastn QuickBase connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _QuickBaseCreateFieldProperties(TypedDict, total=False):
    appendOnly: bool
    maxLength: int
    sortAsGiven: bool

class _QuickBaseUpdateFieldProperties(TypedDict, total=False):
    appendOnly: bool
    maxLength: int
    numLines: int
    sortAsGiven: bool

class QuickbaseConnector:
    """QuickBase connector ().

    Provides 12 tools.
    """

    def quick_base_create_field(
        self,
        fieldType: str,
        label: str,
        tableId: str,
        addToForms: Optional[bool] = None,
        appearsByDefault: Optional[bool] = None,
        bold: Optional[bool] = None,
        fieldHelp: Optional[str] = None,
        findEnabled: Optional[bool] = None,
        noWrap: Optional[bool] = None,
        permissions: Optional[List[Any]] = None,
        properties: Optional[_QuickBaseCreateFieldProperties] = None,
    ) -> Dict[str, Any]:
        """Creates a new field (column) within a specified QuickBase table with the given configuration, such as field type, label, and properties. Use this tool when you need to extend a tables schema by adding a new field. Do not use this tool to update an existing field — use the update field tool instead.

        Args:
            fieldType:  (required)
            label:  (required)
            tableId:  (required)
            addToForms: 
            appearsByDefault: 
            bold: 
            fieldHelp: 
            findEnabled: 
            noWrap: 
            permissions: 
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def quick_base_create_table(
        self,
        appId: str,
        name: str,
        description: Optional[str] = None,
        pluralRecordName: Optional[str] = None,
        singleRecordName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new, empty table within a specified QuickBase application with the given name and settings. Use this tool when you need to add a new table to an existing application. Do not use this tool to add fields or records — use the create field and insert record tools after the table is created.

        Args:
            appId: The ID of the Quick Base application. (required)
            name: The name of the record. (required)
            description: A description of the record.
            pluralRecordName: The plural name of the record type.
            singleRecordName: The singular name of the record type.
        Returns:
            API response as a dictionary.
        """
        ...

    def quick_base_delete_fields(
        self,
        fieldIds: List[Any],
        tableId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes one or more specified fields (columns) from a QuickBase table. Use this tool when you need to remove field definitions and all associated data from a table. Do not use this tool to simply hide or disable a field. This action is irreversible — all data stored in the deleted fields will be permanently lost.

        Args:
            fieldIds: An array of field IDs to include in the response. (required)
            tableId: The ID of the Quick Base table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quick_base_delete_records(
        self,
        from: str,
        where: str,
    ) -> Dict[str, Any]:
        """Permanently deletes one or more specified records from a specified QuickBase table. Use this tool when you need to remove existing records by their record IDs from a table. Do not use this tool to update or archive records — deletion is irreversible and the records cannot be recovered after this action.

        Args:
            from: Specifies the table from which to retrieve data. (required)
            where: A condition to filter the retrieved data. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quick_base_delete_table(
        self,
        appId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing table from a QuickBase application, including all of its fields, records, and data. Use this tool when you need to completely remove a table from an application by its table ID. Do not use this tool to clear records while keeping the table structure — use the delete records tool instead. This action is irreversible and all data within the table will be permanently lost.

        Args:
            appId: The ID of the Quick Base application. (required)
            tableId: The ID of the Quick Base table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quick_base_get_field(
        self,
        fieldId: str,
        tableId: str,
        includeFieldPerms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full configuration and metadata of a single field in a QuickBase table, identified by its field ID. Use this tool when you need to inspect the definition, type, or properties of a specific field. Do not use this tool to retrieve a list of all fields — use the list fields tool instead.

        Args:
            fieldId: The ID of the Quick Base field. (required)
            tableId: The ID of the Quick Base table. (required)
            includeFieldPerms: Indicates whether to include field permissions in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def quick_base_get_table(
        self,
        appId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details and metadata of a single QuickBase table, identified by its table ID, including its name, description, and settings. Use this tool when you need information about a specific table. Do not use this tool to retrieve a list of all tables — use the list tables tool instead.

        Args:
            appId: The ID of the Quick Base application. (required)
            tableId: The ID of the Quick Base table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quick_base_insert_record(
        self,
        data: List[Any],
        to: str,
        fieldsToReturn: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Inserts one or more new records into a specified QuickBase table. Use this tool when you need to add new rows of data to an existing table. Do not use this tool to update existing records — use the update tool instead. This action creates new records and cannot be undone without a separate delete operation.

        Args:
            data:  (required)
            to: Target Quick Base table or database. (required)
            fieldsToReturn: List of field IDs to be returned in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def quick_base_list_fields(
        self,
        tableId: str,
        includeFieldPerms: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all fields (columns) defined in a specified QuickBase table, including their IDs, labels, types, and properties. Use this tool when you need an overview of the schema of a table. Do not use this tool to retrieve details of a single field — use the get field tool instead.

        Args:
            tableId: The ID of the Quick Base table. (required)
            includeFieldPerms: Indicates whether to include field permissions in the response (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def quick_base_list_tables(
        self,
        appId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all tables within a specified QuickBase application, including their IDs, names, and metadata. Use this tool when you need an overview of the tables available in an application. Do not use this tool to retrieve details of a single table — use the get table tool instead.

        Args:
            appId: The ID of the Quick Base application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def quick_base_update_field(
        self,
        fieldId: str,
        tableId: str,
        addToForms: Optional[bool] = None,
        appearsByDefault: Optional[bool] = None,
        bold: Optional[bool] = None,
        fieldHelp: Optional[str] = None,
        findEnabled: Optional[bool] = None,
        label: Optional[str] = None,
        noWrap: Optional[bool] = None,
        permissions: Optional[List[Any]] = None,
        properties: Optional[_QuickBaseUpdateFieldProperties] = None,
        required: Optional[bool] = None,
        unique: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration or metadata of a specific field (column) in a QuickBase table, such as its label, type, or properties. Use this tool when you need to modify the definition of an existing field by its field ID. Do not use this tool to update record values — use the record update tool instead. Changes to field definitions may affect all records in the table.

        Args:
            fieldId: The ID of the Quick Base field. (required)
            tableId: The ID of the Quick Base table. (required)
            addToForms: Indicates whether to add the field to forms.
            appearsByDefault: Indicates whether this field is visible by default.
            bold: Whether to display field text in bold.
            fieldHelp: Help text associated with the field.
            findEnabled: Indicates whether this field is searchable.
            label: The display name of the field.
            noWrap: Whether to prevent text wrapping in the field.
            permissions: 
            properties: Additional properties specific to the field type.
            required: Indicates whether this field is required.
            unique: Indicates whether this field must contain unique values.
        Returns:
            API response as a dictionary.
        """
        ...

    def quick_base_update_table(
        self,
        appId: str,
        tableId: str,
        description: Optional[str] = None,
        name: Optional[str] = None,
        pluralRecordName: Optional[str] = None,
        singleRecordName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the metadata or settings of an existing QuickBase table, such as its name or description, identified by its table ID. Use this tool when you need to modify table-level properties. Do not use this tool to add, remove, or update fields within the table — use the field management tools instead.

        Args:
            appId: ID of the Quick Base application. (required)
            tableId: ID of the Quick Base table. (required)
            description: Description of the table.
            name: Name of the table.
            pluralRecordName: Name used to refer to multiple records in the table.
            singleRecordName: Name used to refer to a single record in the table.
        Returns:
            API response as a dictionary.
        """
        ...

