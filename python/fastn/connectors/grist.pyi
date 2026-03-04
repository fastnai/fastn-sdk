"""Fastn Grist connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class GristConnector:
    """Grist connector ().

    Provides 20 tools.
    """

    def grist_add_columns(
        self,
        columns: List[Any],
        docId: str,
        tableId: str,
        hidden: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds one or more new columns to an existing table in a Grist document, identified by document ID and table ID. Use this tool when you need to extend a tables schema with additional fields. Do not use this tool to add rows of data — use grist_add_records instead. Column additions are persisted immediately and affect the table structure.

        Args:
            columns:  (required)
            docId: The unique identifier of the Grist document. (required)
            tableId: The unique identifier of the table within the document. (required)
            hidden: A hidden parameter for internal use.
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_add_records(
        self,
        docId: str,
        records: List[Any],
        tableId: str,
        noparse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds one or more new records to a specified table in a Grist document, identified by document ID and table ID. Use this tool when you need to insert new rows of data into an existing table. Do not use this tool to update existing records — use an update operation instead. This tool modifies table data and the changes are persisted immediately.

        Args:
            docId: The ID of the Grist document. (required)
            records:  (required)
            tableId: The ID of the table within the document. (required)
            noparse: A parameter to indicate whether to parse the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_create_doc(
        self,
        name: str,
        workspaceId: str,
        isPinned: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new document in a specified Grist workspace, identified by workspace ID. Use this tool when you need to provision a new Grist document as a container for tables and data. Do not use this tool to create a table inside an existing document — use grist_create_table instead. The document is created immediately and persisted.

        Args:
            name: Name of the item. (required)
            workspaceId: The ID of the workspace. (required)
            isPinned: Indicates whether the item is pinned.
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_create_table(
        self,
        docId: str,
        tables: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new table within a specified Grist document, identified by document ID. Use this tool when you need to add a new structured data container to an existing document. Do not use this tool to create a new document — use grist_create_doc instead. The table is created immediately and persisted to the document.

        Args:
            docId: The unique identifier for the Grist document. (required)
            tables:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_create_workspace(
        self,
        name: str,
        orgId: str,
    ) -> Dict[str, Any]:
        """Creates a new workspace under a specified Grist organization, identified by organization ID. Use this tool when you need to provision a new workspace to organize documents within an organization. Do not use this tool to create a document — use grist_create_doc instead. The workspace is created immediately and persisted.

        Args:
            name: Name of the resource. (required)
            orgId: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_delete_column(
        self,
        columnId: str,
        docId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific column from a Grist table using the document ID, table ID, and column ID. Use this tool when a column is no longer needed and must be removed from the table schema. This action is irreversible — deleted columns and all their data cannot be recovered. Do not use this tool if you only want to clear column data; use an update operation instead.

        Args:
            columnId: The ID of the column. (required)
            docId: The ID of the document. (required)
            tableId: The ID of the table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_delete_doc(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a Grist document and all its contents, identified by document ID. Use this tool only when the document and all its tables, columns, and records are no longer needed. This action is irreversible — deleted documents cannot be recovered. Do not use this tool if you only want to update document metadata — use grist_update_doc instead.

        Args:
            docId: The unique identifier for the Grist document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_delete_org(
        self,
        orgId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific Grist organization and all its associated workspaces and documents, identified by organization ID. Use this tool only when the entire organization and all its contents must be removed. This action is irreversible and cannot be undone. Do not use this tool to remove a single workspace or document — use grist_delete_workspace or grist_delete_doc instead.

        Args:
            orgId: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_delete_workspace(
        self,
        orgId: str,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a workspace from a Grist organization, identified by organization ID and workspace ID. All documents contained within the workspace will also be deleted. Use this tool only when the workspace and all its contents are no longer needed. This action is irreversible and cannot be undone. Do not use this tool to remove a single document — use grist_delete_doc instead.

        Args:
            orgId: The ID of the Grist organization. (required)
            workspaceId: The ID of the Grist workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_get_doc(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Retrieves metadata and details for a specific Grist document, identified by document ID. Use this tool when you need to inspect document-level properties such as its name, workspace, or access settings. Do not use this tool to list all documents — use grist_list_tables or grist_list_workbooks for broader discovery. This tool is read-only and has no side effects.

        Args:
            docId: The unique identifier for the Grist document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_get_org(
        self,
        orgId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific Grist organization, identified by organization ID, including its name and settings. Use this tool when you need to inspect organization-level properties or verify an organization exists before managing its workspaces. Do not use this tool to list all organizations — use grist_list_orgs for that. This tool is read-only and has no side effects.

        Args:
            orgId: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_get_workspace(
        self,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific Grist workspace, identified by workspace ID, including its name and associated documents. Use this tool when you need to inspect workspace-level properties or verify a workspace exists before creating documents within it. Do not use this tool to list all workspaces in an organization — use grist_list_workspaces for that. This tool is read-only and has no side effects.

        Args:
            workspaceId: The ID of the Grist workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_list_columns(
        self,
        docId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Returns a list of columns defined in a specified Grist table, including their IDs and metadata, identified by document ID and table ID. Use this tool when you need to inspect a tables schema or discover available fields before reading or writing records. Do not use this tool to retrieve row data — use grist_list_records for that. This tool is read-only and has no side effects.

        Args:
            docId: The unique identifier for the Grist document. (required)
            tableId: The unique identifier for the table within the document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_list_orgs(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all Grist organizations accessible to the authenticated user. Use this tool when you need to discover available organizations before accessing their workspaces or documents. Do not use this tool to retrieve details of a single organization — use grist_get_org for that. This tool is read-only and has no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_list_records(
        self,
        docId: str,
        tableId: str,
        XLimit: Optional[str] = None,
        XSort: Optional[str] = None,
        filter: Optional[str] = None,
        hidden: Optional[str] = None,
        limit: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of records from a specified table within a Grist document, identified by document ID and table ID. Use this tool when you need to read all or filtered rows from a table. Do not use this tool to retrieve table schema or column definitions — use grist_list_columns for that. This tool is read-only and has no side effects.

        Args:
            docId: The ID of the Grist document. (required)
            tableId: The ID of the table within the document. (required)
            XLimit: Limit the number of records returned.
            XSort: Specify the sorting order for the records.
            filter: Filter the records based on specified criteria.
            hidden: Specify whether to include hidden records.
            limit: Limit the number of records returned.
            sort: Specify the sorting order for the records.
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_list_tables(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Returns a list of all tables within a specified Grist document, identified by document ID. Use this tool when you need to discover available tables before accessing their columns or records. Do not use this tool to retrieve records or columns — use grist_list_records or grist_list_columns for that. This tool is read-only and has no side effects.

        Args:
            docId: The unique identifier for the Grist document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_list_workspaces(
        self,
        orgId: str,
    ) -> Dict[str, Any]:
        """Returns a list of all workspaces associated with a specified Grist organization, identified by organization ID. Use this tool when you need to discover available workspaces before accessing or creating documents within them. Do not use this tool to retrieve workspace details for a single workspace — use grist_get_workspace for that. This tool is read-only and has no side effects.

        Args:
            orgId: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_update_doc(
        self,
        docId: str,
        name: str,
        isPinned: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates the metadata (such as name) of an existing Grist document, identified by document ID. Use this tool when you need to rename or modify document-level properties without affecting its contents. Do not use this tool to modify table data or structure — use table or record-specific tools for that. Changes are persisted immediately.

        Args:
            docId: The ID of the Grist document. (required)
            name: The name of the item. (required)
            isPinned: 
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_update_org(
        self,
        name: str,
        orgId: str,
    ) -> Dict[str, Any]:
        """Updates the details (such as name) of a specific Grist organization, identified by organization ID. Use this tool when you need to modify organization-level metadata. Do not use this tool to update workspaces or documents within the organization — use grist_update_workspace or grist_update_doc instead. Changes are persisted immediately.

        Args:
            name: The name of the resource. (required)
            orgId: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def grist_update_workspace(
        self,
        name: str,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Updates the metadata (such as name) of an existing Grist workspace, identified by workspace ID. Use this tool when you need to rename or modify workspace-level properties. Do not use this tool to update documents inside the workspace — use grist_update_doc instead. Changes are persisted immediately.

        Args:
            name: Name of the resource. (required)
            workspaceId: The ID of the workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

