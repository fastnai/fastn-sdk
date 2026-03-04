"""Fastn Coda connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _CodaAddPermissionPrincipal(TypedDict, total=False):
    email: str
    type: str

class _CodaCreateDocInitialpage(TypedDict, total=False):
    iconName: str
    imageUrl: str
    name: str
    pageContent: Dict[str, Any]
    parentPageId: str
    subtitle: str

class _CodaCreatePagePagecontent(TypedDict, total=False):
    canvasContent: Dict[str, Any]
    type: str

class _CodaUpdatePageContentupdate(TypedDict, total=False):
    canvasContent: Dict[str, Any]
    insertionMode: str

class CodaConnector:
    """Coda connector ().

    Provides 21 tools.
    """

    def coda_add_permission(
        self,
        access: str,
        docId: str,
        principal: _CodaAddPermissionPrincipal,
        suppressEmail: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Grants a user or group access to a specified Coda document by adding a new permission entry with the specified access level (e.g., read, write). Use this to share a doc with a new principal. Requires a valid docId. Does not modify existing permissions — use coda_delete_permission first if replacing access.

        Args:
            access: Access level for the coda v1 API. (required)
            docId: Document ID for the coda v1 API. (required)
            principal: Principal details for the coda v1 API. (required)
            suppressEmail: Flag to suppress email notifications for the coda v1 API.
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_create_doc(
        self,
        folderId: str,
        initialPage: _CodaCreateDocInitialpage,
        sourceDoc: str,
        timezone: str,
        title: str,
    ) -> Dict[str, Any]:
        """Creates a new Coda document, optionally specifying a title, source doc to copy from, and folder location. Use this to programmatically provision new docs for users or workflows. This action creates a new resource — to modify an existing doc, use the update tools instead.

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

    def coda_create_page(
        self,
        docId: str,
        name: str,
        pageContent: _CodaCreatePagePagecontent,
        subtitle: str,
        iconName: Optional[str] = None,
        imageUrl: Optional[str] = None,
        parentPageId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new page within a specified Coda document. Use this to add a page to an existing doc, optionally specifying name, parent page, and initial content. Requires a valid docId. This action creates a new resource in Coda — to modify an existing page, use coda_update_page instead.

        Args:
            docId:  (required)
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

    def coda_delete_doc(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an entire Coda document identified by its docId, including all pages, tables, and content within it. Use this only when the entire document should be irreversibly removed. This action is destructive and cannot be undone. Requires a valid docId.

        Args:
            docId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_delete_page(
        self,
        docId: str,
        pageId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific page from a Coda document identified by docId and pageId. Use this only when the page and all its content should be irreversibly removed. This action is destructive and cannot be undone — all content on the page will be lost. Requires both a valid docId and pageId.

        Args:
            docId:  (required)
            pageId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_delete_permission(
        self,
        docId: str,
        permissionId: str,
    ) -> Dict[str, Any]:
        """Permanently removes a specific permission entry from a Coda document, revoking the associated user or groups access. Use this to revoke access for a principal identified by permissionId. Requires a valid docId and permissionId. This action is irreversible — the permission must be re-added manually if removed in error.

        Args:
            docId: Document ID for the coda v1 API. (required)
            permissionId: Permission ID for the coda v1 API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_export_page_content(
        self,
        docId: str,
        outputFormat: str,
        pageId: str,
    ) -> Dict[str, Any]:
        """Initiates an export of the content of a specific page within a Coda document in a designated format (e.g., PDF, Markdown). Use this to extract readable or downloadable content from a page. Requires a valid docId and pageId. This triggers an asynchronous export job — check the export status separately to retrieve the result. Does not modify the page.

        Args:
            docId: ID of the document in Coda. (required)
            outputFormat: Desired output format for the response. (required)
            pageId: ID of the page within the document in Coda. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_get_column(
        self,
        columnId: str,
        docId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single column in a specified Coda table, including its name, ID, data type, and format settings. Use this when you need metadata about a specific column. Requires a valid docId, tableId, and columnId. Does not return row data or modify the column.

        Args:
            columnId: ID of the column in the Coda doc. (required)
            docId: ID of the Coda document. (required)
            tableId: ID of the table in the Coda doc. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_get_doc(
        self,
        docId: str,
    ) -> Dict[str, Any]:
        """Retrieves metadata and details for a single Coda document identified by its docId, including its name, owner, and timestamps. Use this when you need information about a specific doc. Requires a valid docId. Does not return page or table contents — use page or table tools for that.

        Args:
            docId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_get_page(
        self,
        docId: str,
        pageId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details and metadata of a single page within a Coda document, identified by docId and pageId. Use this when you need information about a specific page such as its name, type, or parent. Requires both a valid docId and pageId. Does not return the full rendered page content — use the export tool for that.

        Args:
            docId:  (required)
            pageId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_get_user_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves profile and account information for the currently authenticated Coda user, including name, email, and account ID. Use this to confirm which user account is active or to fetch the current users identity before performing user-scoped operations. Does not return information about other users.
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_list_columns(
        self,
        docId: str,
        tableId: str,
    ) -> Dict[str, Any]:
        """Returns a list of all columns in a specified table within a Coda document, including column names, IDs, and data types. Use this to inspect the schema of a table before reading or writing row data. Requires a valid docId and tableId. Does not return row data — use a row-level tool for that.

        Args:
            docId: Document ID in Coda. (required)
            tableId: Table ID within the document in Coda. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_list_controls(
        self,
        docId: str,
        limit: Optional[str] = None,
        pageToken: Optional[str] = None,
        sortBy: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of interactive controls (such as buttons, sliders, and dropdowns) defined within a specified Coda document. Use this to discover controls available in a doc. Requires a valid docId. Does not trigger or interact with controls — this is a read-only listing.

        Args:
            docId: Document ID for the coda v1 API. (required)
            limit: Limit the number of results returned by the coda v1 API.
            pageToken: Pagination token for the coda v1 API.
            sortBy: Field to sort the results by in the coda v1 API.
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_list_doc_categories(
        self,
    ) -> Dict[str, Any]:
        """Returns a list of all available document categories in Coda. Use this to discover valid category values before creating or filtering documents by category. This is a global listing and does not require a docId. Does not create or modify categories.
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_list_docs(
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
        """Returns a list of all Coda documents accessible to the authenticated user, including document names, IDs, and metadata. Use this to discover available docs before performing doc-level operations. Does not return the contents of any document — use coda_get_doc or page-level tools for that.

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

    def coda_list_formulas(
        self,
        docId: str,
        limit: Optional[str] = None,
        pageToken: Optional[str] = None,
        sortBy: Optional[str] = None,
        syncToken: Optional[str] = None,
        useColumnNames: Optional[str] = None,
        valueFormat: Optional[str] = None,
        visibleOnly: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of named formulas defined within a specified Coda document, including their names and IDs. Use this to discover formulas available in a doc before referencing them. Requires a valid docId. Does not evaluate or return formula results — use the appropriate Coda formula tool for computed values.

        Args:
            docId: ID of the document. (required)
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

    def coda_list_pages(
        self,
        docId: str,
        limit: Optional[str] = None,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all pages within a specified Coda document, including page names, IDs, and hierarchy. Use this to enumerate pages in a doc before retrieving or updating individual pages. Requires a valid docId. Does not return page content — use coda_get_page for that.

        Args:
            docId:  (required)
            limit: 
            pageToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_list_permissions(
        self,
        docId: str,
        limit: Optional[str] = None,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all permissions configured for a specified Coda document, including the principals (users or groups) and their access levels. Use this to audit who has access to a doc. Requires a valid docId. Does not modify permissions — use coda_add_permission or coda_delete_permission for that.

        Args:
            docId: ID of the document. (required)
            limit: Limit the number of results returned.
            pageToken: Pagination token for fetching subsequent pages of results.
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_list_table_columns(
        self,
        docId: Optional[str] = None,
        tableId: Optional[str] = None,
        visibleOnly: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all columns in a specified table within a Coda document, including column names, IDs, and data types. Use this to inspect the schema of a table before reading or writing row data. Requires a valid docId and tableId. Note: this tool duplicates the functionality of coda_list_columns — prefer coda_list_columns where available. Does not return row data.

        Args:
            docId: 
            tableId: 
            visibleOnly: 
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_list_tables(
        self,
        docId: str,
        limit: Optional[str] = None,
        pageToken: Optional[str] = None,
        sortBy: Optional[str] = None,
        tableTypes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all tables within a specified Coda document, including table names, IDs, and metadata. Use this to discover which tables exist in a doc before querying rows or columns. Requires a valid docId. Does not return table row data — use a row-level tool for that.

        Args:
            docId:  (required)
            limit: 
            pageToken: 
            sortBy: 
            tableTypes: 
        Returns:
            API response as a dictionary.
        """
        ...

    def coda_update_page(
        self,
        docId: str,
        pageId: str,
        categoryNames: Optional[str] = None,
        contentUpdate: Optional[_CodaUpdatePageContentupdate] = None,
        discoverable: Optional[str] = None,
        earnCredit: Optional[str] = None,
        iconName: Optional[str] = None,
        imageUrl: Optional[str] = None,
        isHidden: Optional[bool] = None,
        mode: Optional[str] = None,
        name: Optional[str] = None,
        slug: Optional[str] = None,
        subtitle: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the name, content, or settings of an existing page in a Coda document identified by docId and pageId. Use this to rename a page or modify its properties. Requires both a valid docId and pageId. This action modifies an existing page — to create a new page, use coda_create_page instead.

        Args:
            docId: The unique identifier for the Coda document. (required)
            pageId: The unique identifier for the page within the Coda document. (required)
            categoryNames: Comma-separated list of category names.
            contentUpdate: 
            discoverable: Indicates whether the item is discoverable.
            earnCredit: Indicates whether the item earns credit.
            iconName: 
            imageUrl: 
            isHidden: 
            mode: Operational mode for the request.
            name: Name of the item being added or modified.
            slug: URL-friendly identifier for the item.
            subtitle: 
        Returns:
            API response as a dictionary.
        """
        ...

