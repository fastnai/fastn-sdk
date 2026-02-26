"""Fastn Coda connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class CodaConnector:
    """Coda connector ().

    Provides 21 tools.
    """

    def add_permission(
        self,
        access: str,
        principal: Dict[str, Any],
        suppressEmail: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Grants permission to a user for specific operations in the system.

        Args:
            access: Access level for the coda v1 API. (required)
            principal: Principal details for the coda v1 API. (required)
            suppressEmail: Flag to suppress email notifications for the coda v1 API.
        Returns:
            API response as a dictionary.
        """
        ...

    def content_export(
        self,
        outputFormat: str,
    ) -> Dict[str, Any]:
        """Exports content from the specified source in a designated format.

        Args:
            outputFormat: Desired output format for the response. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_doc(
        self,
        folderId: str,
        initialPage: Dict[str, Any],
        sourceDoc: str,
        timezone: str,
        title: str,
    ) -> Dict[str, Any]:
        """Creates a new document in the system.

        Args:
            folderId:  (required)
            initialPage:  (required)
            sourceDoc:  (required)
            timezone:  (required)
            title:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_page(
        self,
        name: str,
        pageContent: Dict[str, Any],
        subtitle: str,
        iconName: Optional[str] = None,
        imageUrl: Optional[str] = None,
        parentPageId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new page within a specified document.

        Args:
            name:  (required)
            pageContent:  (required)
            subtitle:  (required)
            iconName: 
            imageUrl: 
            parentPageId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_doc(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Deletes a document from the system.

        Args:
            docId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_page(
        self,
        docId: str,
        pageId: str,
    ) -> Dict[str, Any]:
        """Removes a specific page from a document in the system.

        Args:
            docId:  (required)
            pageId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_permission(
        self,
        docId: str,
        permissionId: str,
    ) -> Dict[str, Any]:
        """Removes permission from a user for specified operations in the system.

        Args:
            docId: Document ID for the coda v1 API. (required)
            permissionId: Permission ID for the coda v1 API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_column(
        self,
        columnId: str,
        docId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific column from a table.

        Args:
            columnId: ID of the column in the Coda doc. (required)
            docId: ID of the Coda document. (required)
            tableId: ID of the table in the Coda doc. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_columns(
        self,
        docId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Retrieves all columns from a specified table in the database.

        Args:
            docId: Document ID in Coda. (required)
            tableId: Table ID within the document in Coda. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_controls(
        self,
        limit: Optional[str] = None,
        pageToken: Optional[str] = None,
        sortBy: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains the various controls available in the system.

        Args:
            limit: Limit the number of results returned by the coda v1 API.
            pageToken: Pagination token for the coda v1 API.
            sortBy: Field to sort the results by in the coda v1 API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_doc(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific document's details from the system.

        Args:
            docId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_doc_categories(
        self,
    ) -> Dict[str, Any]:
        """Fetches the categories for documents in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_docs(
        self,
        folderId: Optional[str] = None,
        inGallery: Optional[str] = None,
        isOwner: Optional[str] = None,
        isPublished: Optional[str] = None,
        isStarred: Optional[str] = None,
        limit: Optional[str] = None,
        pageToken: Optional[str] = None,
        query: Optional[str] = None,
        sourceDoc: Optional[str] = None,
        workspaceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all documents stored in the system.

        Args:
            folderId: 
            inGallery: 
            isOwner: 
            isPublished: 
            isStarred: 
            limit: 
            pageToken: 
            query: 
            sourceDoc: 
            workspaceId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_formulas(
        self,
        limit: Optional[str] = None,
        pageToken: Optional[str] = None,
        sortBy: Optional[str] = None,
        syncToken: Optional[str] = None,
        useColumnNames: Optional[str] = None,
        valueFormat: Optional[str] = None,
        visibleOnly: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the formulas used within the documents in the system.

        Args:
            limit: Limit the number of results returned.
            pageToken: Token for pagination.
            sortBy: Field to sort results by.
            syncToken: Sync token for incremental updates.
            useColumnNames: Use column names in the response.
            valueFormat: Format of the values in the response.
            visibleOnly: Return only visible items.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_page(
        self,
        docId: str,
        pageId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific page’s details from a document.

        Args:
            docId:  (required)
            pageId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_pages(
        self,
        limit: Optional[str] = None,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains all pages within a specified document.

        Args:
            limit: 
            pageToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_permissions(
        self,
        limit: Optional[str] = None,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains the permissions set for users within the system.

        Args:
            limit: Limit the number of results returned.
            pageToken: Pagination token for fetching subsequent pages of results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_table_collumns(
        self,
        visibleOnly: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the columns of a specified table in the database.

        Args:
            visibleOnly: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tables(
        self,
        limit: Optional[str] = None,
        pageToken: Optional[str] = None,
        sortBy: Optional[str] = None,
        tableTypes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all tables available in the database.

        Args:
            limit: 
            pageToken: 
            sortBy: 
            tableTypes: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_info(
        self,
    ) -> Dict[str, Any]:
        """Fetches information about the current user in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_page(
        self,
        categoryNames: Optional[str] = None,
        discoverable: Optional[str] = None,
        earnCredit: Optional[str] = None,
        mode: Optional[str] = None,
        slug: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the content or settings of a specified page in the system.

        Args:
            categoryNames: Comma-separated list of category names.
            discoverable: Indicates whether the item is discoverable.
            earnCredit: Indicates whether the item earns credit.
            mode: Operational mode for the request.
            slug: URL-friendly identifier for the item.
        Returns:
            API response as a dictionary.
        """
        ...

