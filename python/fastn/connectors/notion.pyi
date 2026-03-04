"""Fastn Notion connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _NotionCreateDatabaseParent(TypedDict, total=False):
    page_id: str
    type: str

class _NotionCreateDatabaseProperties(TypedDict, total=False):
    _1: Dict[str, Any]
    Description: Dict[str, Any]
    Food_group: Dict[str, Any]
    In_stock: Dict[str, Any]
    Last_ordered: Dict[str, Any]
    Meals: Dict[str, Any]
    Name: Dict[str, Any]
    Number_of_meals: Dict[str, Any]
    Photo: Dict[str, Any]
    Price: Dict[str, Any]
    Store_availability: Dict[str, Any]

class _NotionCreateDatabaseCover(TypedDict, total=False):
    external: Dict[str, Any]
    type: str

class _NotionCreateDatabaseIcon(TypedDict, total=False):
    emoji: str
    type: str

class _NotionCreatePageParent(TypedDict, total=False):
    database_id: str

class _NotionCreatePageProperties(TypedDict, total=False):
    Notes: Dict[str, Any]
    Tasks: Dict[str, Any]

class _NotionListDatabasesFilter(TypedDict, total=False):
    property: str
    value: str

class _NotionListDatabasesSort(TypedDict, total=False):
    direction: str
    timestamp: str

class _NotionQueryDatabaseFilter(TypedDict, total=False):
    or: List[Any]

class _NotionSearchFilter(TypedDict, total=False):
    property: str
    value: str

class _NotionUpdateDatabaseProperties(TypedDict, total=False):
    _1: str
    Photo: Dict[str, Any]
    Store_availability: Dict[str, Any]

class NotionConnector:
    """Notion connector ().

    Provides 16 tools.
    """

    def notion_append_block_children(
        self,
        children: List[Any],
        parentId: str,
    ) -> Dict[str, Any]:
        """Append new child blocks (such as paragraphs, headings, or lists) to a specified existing block in Notion. Use this to add content beneath an existing block without modifying its current children. Do not use this to create a new top-level page—use notion_create_page instead. Do not use this to modify existing blocks—use the appropriate update_block tool instead.

        Args:
            children:  (required)
            parentId: Parent ID of the Notion page or database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_append_to_page(
        self,
        children: Optional[List[Any]] = None,
        pageId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Append new content blocks (such as text, images, or code blocks) as children to a specified existing Notion page. Use this to add content to the end of an existing page without modifying its current blocks. Do not use this to modify existing blocks—use the appropriate update_block tool instead. Do not use this to retrieve page content—use notion_list_block_children instead.

        Args:
            children: 
            pageId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_create_database(
        self,
        parent: _NotionCreateDatabaseParent,
        properties: _NotionCreateDatabaseProperties,
        cover: Optional[_NotionCreateDatabaseCover] = None,
        icon: Optional[_NotionCreateDatabaseIcon] = None,
        title: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Create a new database in Notion for storing and organizing structured data. Use this when you need to set up a new database with defined properties and schema. Once created, the database is permanently added to the workspace and visible to all users with access. To add content to an existing database, use notion_create_page instead. To modify an existing databases properties or schema, use notion_update_database instead.

        Args:
            parent: Parent object specifying where to create the page. (required)
            properties: Properties of the Notion page. (required)
            cover: Cover image for the Notion page.
            icon: Icon for the Notion page.
            title: 
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_create_page(
        self,
        parent: _NotionCreatePageParent,
        properties: _NotionCreatePageProperties,
    ) -> Dict[str, Any]:
        """Create a new page in Notion as a standalone page or as a child under a database or parent page. Use this when the user wants to create a new page with properties and optional content blocks. Once created, the page is permanently added and visible to all users with access. Do not use this to append blocks to an existing page—use notion_append_block_children instead. To update an existing page, use notion_update_page instead.

        Args:
            parent: Specifies the database where the new page will be created. (required)
            properties: Properties to set on the new page within the database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_delete_block(
        self,
        blockId: str,
    ) -> Dict[str, Any]:
        """Permanently delete a specific block from Notion using its block ID. Use this when you need to remove a block from a page or database. This action is irreversible and cannot be undone. Do not use this to delete an entire page or database—use the appropriate delete_page or delete_database tool instead.

        Args:
            blockId: ID of the Notion block. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_get_access_token(
        self,
        code: str,
        grant_type: str,
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Exchange a Notion OAuth authorization code for an access token required to authenticate subsequent Notion API requests. Use this during the initial OAuth setup flow when you have a valid authorization code and need to obtain a token to access Notion workspaces and pages. The returned token grants access according to the permissions granted during authorization. Do not use this if you already have a valid access token. Do not use this to refresh an existing token—use the appropriate token refresh flow instead.

        Args:
            code: Authorization code received from the Notion OAuth flow. (required)
            grant_type: Grant type for the OAuth flow (e.g., 'authorization_code'). (required)
            redirect_uri: Redirect URI registered for the Notion application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_get_block(
        self,
        blockId: str,
    ) -> Dict[str, Any]:
        """Retrieve detailed information about a specific Notion block by its ID, including its type, content, and metadata. Use this when you need to inspect a single known block. Do not use this to list all blocks within a page—use notion_list_block_children instead. Do not use this to search for blocks by name or content—use notion_search instead.

        Args:
            blockId: ID of the Notion block. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_get_page(
        self,
        filter_properties: Optional[str] = None,
        pageId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieve the full properties and metadata of a specific Notion page by its ID, including its title, properties, and content block references. Use this when you need to access a single pages data. Do not use this to retrieve the block content within the page—use notion_list_block_children instead. To retrieve multiple pages or search across pages, use notion_list_databases or notion_search instead.

        Args:
            filter_properties: Specify the properties to filter by.
            pageId: The ID of the Notion page.
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_get_user(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieve detailed information about a specific Notion user by their ID. Use this when you need to fetch a users profile details such as their name, email, avatar, or account status. To list all users in a workspace, use list_users instead.

        Args:
            id: ID of the Notion resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_list_block_children(
        self,
        blockId: str,
        page_size: Optional[str] = None,
        start_cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieve all children blocks of a specified parent block in Notion. Use this when you need to get all child blocks within a parent block (such as page contents, list items, or nested blocks), typically when the user asks to see the structure or contents of a specific Notion block or page. Do not use this to query database entries—use notion_query_database instead. Do not use this to retrieve page properties or metadata—use notion_get_page instead.

        Args:
            blockId: ID of the Notion block. (required)
            page_size: Number of results per page.
            start_cursor: Cursor for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_list_databases(
        self,
        filter: Optional[_NotionListDatabasesFilter] = None,
        page_size: Optional[int] = None,
        sort: Optional[_NotionListDatabasesSort] = None,
        start_cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieve a list of all Notion databases accessible to the authenticated user. Use this when you need to discover available databases, present database options to the user, or enumerate all databases before selecting one to query or update. Note: this tool calls the Notion search endpoint filtered to databases. To retrieve a specific databases schema or metadata by ID, use notion_get_database instead. To query entries within a database, use notion_query_database instead.

        Args:
            filter: Filter criteria for Notion database entries.
            page_size: Number of records to return per page.
            sort: Sorting options for retrieved Notion data.
            start_cursor: Cursor for pagination, starting point for data retrieval. Remove this when you're getting data for first page.
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_list_tasks(
        self,
        dbId: str,
    ) -> Dict[str, Any]:
        """Retrieve a list of tasks from a specific Notion database by querying it. Use this when you need to fetch multiple tasks at once from a known database. Requires a database ID. Do not use this to retrieve a single task by ID—use notion_get_page instead. To filter tasks by specific criteria, use notion_query_database instead.

        Args:
            dbId: ID of the Notion database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_list_users(
        self,
        page_size: Optional[str] = None,
        start_cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieve a list of all users in the connected Notion workspace. Use this when you need to see all users with access to the workspace, or when looking up user information for sharing, permissions, or collaboration purposes. Do not use this to retrieve details for a specific user—use notion_get_user instead.

        Args:
            page_size: Number of results to return per page.
            start_cursor: Cursor to start pagination from.
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_query_database(
        self,
        databaseId: str,
        filter: Optional[_NotionQueryDatabaseFilter] = None,
        sorts: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Query a Notion database by applying filters and sorts to retrieve matching entries. Use this when the user wants to find specific items in a Notion database based on property values, dates, or other criteria. Do not use this to retrieve a databases schema or metadata—use notion_get_database instead. Do not use this to retrieve block children or page content—use notion_list_block_children instead. Do not use this to search across all databases—use notion_search instead.

        Args:
            databaseId: The unique identifier for the Notion database. (required)
            filter: Filters to apply to the database query.
            sorts: 
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_search(
        self,
        filter: Optional[_NotionSearchFilter] = None,
        query: Optional[str] = None,
        start_cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Search across all Notion pages, databases, and content within accessible workspaces using a text query. Use this when the user wants to find content by keyword, locate pages or databases by name, or search across multiple Notion resources without specifying a particular database. Do not use this to query a specific database with structured filters—use notion_query_database instead.

        Args:
            filter: Filter parameters for the Notion API request.
            query: Search query for the Notion API.
            start_cursor: Cursor for pagination in the Notion API.
        Returns:
            API response as a dictionary.
        """
        ...

    def notion_update_database(
        self,
        databaseId: str,
        description: Optional[List[Any]] = None,
        properties: Optional[_NotionUpdateDatabaseProperties] = None,
        title: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Update an existing database within Notion to modify its structure or data. Use this when you need to modify database properties, settings, or metadata such as the database name, description, or field configuration. Do not use this to add or modify database contents; use create_page or update_page instead. Note: Changes to the database schema may affect existing pages and integrations.

        Args:
            databaseId: ID of the Notion database. (required)
            description: 
            properties: Properties of the Notion page.
            title: 
        Returns:
            API response as a dictionary.
        """
        ...

