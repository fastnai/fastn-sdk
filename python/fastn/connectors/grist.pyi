"""Fastn Grist connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GristConnector:
    """Grist connector ().

    Provides 20 tools.
    """

    def add_columns(
        self,
        columns: List[Any],
    ) -> Dict[str, Any]:
        """Adds new columns to an existing table identified by the table ID.

        Args:
            columns:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def add_records_(
        self,
        noparse: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds new records to a specified table in the database.

        Args:
            noparse: A parameter to indicate whether to parse the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_doc(
        self,
        name: str,
        isPinned: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Creates a new document in the specified workspace.

        Args:
            name: Name of the item. (required)
            isPinned: Indicates whether the item is pinned.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_table(
        self,
        tables: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new table in the specified workspace.

        Args:
            tables:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_workspace(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new workspace under the specified organization.

        Args:
            name: Name of the resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_column(
        self,
        columnId: str,
        docId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Deletes a column from a specific table identified by the column ID.

        Args:
            columnId: The ID of the column. (required)
            docId: The ID of the document. (required)
            tableId: The ID of the table. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_doc(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Deletes a document from the workspace using the document ID.

        Args:
            docId: The unique identifier for the Grist document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_org(
        self,
        orgId: str,
    ) -> Dict[str, Any]:
        """Deletes an organization identified by its organization ID from the system.

        Args:
            orgId: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_workspace(
        self,
        orgId: str,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Deletes a workspace from the organization using the workspace ID.

        Args:
            orgId: The ID of the Grist organization. (required)
            workspaceId: The ID of the Grist workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_columns(
        self,
        docId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of columns from a specified table.

        Args:
            docId: The unique identifier for the Grist document. (required)
            tableId: The unique identifier for the table within the document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_doc(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific document identified by the document ID.

        Args:
            docId: The unique identifier for the Grist document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_org(
        self,
        orgId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific organization based on the provided organization ID.

        Args:
            orgId: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_orgs(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of organizations in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records(
        self,
        XLimit: Optional[str] = None,
        XSort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of records from a specified table.

        Args:
            XLimit: Limit the number of records returned.
            XSort: Specify the sorting order for the records.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of tables within a given workspace.

        Args:
            docId: The unique identifier for the Grist document. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspace(
        self,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific workspace using the workspace ID.

        Args:
            workspaceId: The ID of the Grist workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspaces(
        self,
        orgId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of workspaces associated with the organization.

        Args:
            orgId: The ID of the organization. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_doc(
        self,
        name: str,
        isPinned: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates the information of an existing document based on the document ID.

        Args:
            name: The name of the item. (required)
            isPinned: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_org(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the information of an existing organization specified by the organization ID.

        Args:
            name: The name of the resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_workspace(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the information of an existing workspace identified by the workspace ID.

        Args:
            name: Name of the resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

