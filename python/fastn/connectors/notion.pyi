"""Fastn Notion connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class NotionConnector:
    """Notion connector ().

    Provides 17 tools.
    """

    def append_block_children(
        self,
        children: List[Any],
    ) -> Dict[str, Any]:
        """Add new block children to a specified block within the page.

        Args:
            children:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def append_to_page(
        self,
        children: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Append content to an existing page in the application.

        Args:
            children: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_database(
        self,
        parent: Dict[str, Any],
        properties: Dict[str, Any],
        cover: Optional[Dict[str, Any]] = None,
        icon: Optional[Dict[str, Any]] = None,
        title: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Create a new database in the connected system for data storage.

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

    def create_page(
        self,
        parent: Dict[str, Any],
        properties: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Create a new page within the designated workspace of the application.

        Args:
            parent: Specifies the database where the new page will be created. (required)
            properties: Properties to set on the new page within the database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_ticket(
        self,
        parent: Dict[str, Any],
        properties: Dict[str, Any],
        archived: Optional[bool] = None,
        cover: Optional[str] = None,
        created_by: Optional[Dict[str, Any]] = None,
        created_time: Optional[str] = None,
        icon: Optional[str] = None,
        id: Optional[str] = None,
        in_trash: Optional[bool] = None,
        last_edited_by: Optional[Dict[str, Any]] = None,
        last_edited_time: Optional[str] = None,
        object: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Create a new ticket in the ticketing system for tracking issues or requests.

        Args:
            parent: Parent object of the Notion page (usually a database). (required)
            properties: Properties of the Notion page. (required)
            archived: Indicates whether the Notion page is archived.
            cover: Cover image URL for the Notion page.
            created_by: User who created the Notion page.
            created_time: Creation timestamp of the Notion page.
            icon: Icon URL for the Notion page.
            id: Unique ID of the Notion page.
            in_trash: Indicates whether the Notion page is in trash.
            last_edited_by: User who last edited the Notion page.
            last_edited_time: Last edited timestamp of the Notion page.
            object: Object type of the Notion page.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_block(
        self,
        blockId: str,
    ) -> Dict[str, Any]:
        """Delete a specific block from the application based on the given identifier.

        Args:
            blockId: ID of the Notion block. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_access_token(
        self,
        code: str,
        grant_type: str,
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Retrieve an access token for authentication within the application or service.

        Args:
            code: Authorization code received from the Notion OAuth flow. (required)
            grant_type: Grant type for the OAuth flow (e.g., 'authorization_code'). (required)
            redirect_uri: Redirect URI registered for the Notion application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_tasks(
        self,
        dbId: str,
    ) -> Dict[str, Any]:
        """Retrieve a list of all tasks in a specific project or workspace.

        Args:
            dbId: ID of the Notion database. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_users(
        self,
        page_size: Optional[str] = None,
        start_cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieve a list of all users in the connected system.

        Args:
            page_size: Number of results to return per page.
            start_cursor: Cursor to start pagination from.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_block(
        self,
        blockId: str,
    ) -> Dict[str, Any]:
        """Get detailed information about a specific block in the application.

        Args:
            blockId: ID of the Notion block. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_block_children(
        self,
        page_size: Optional[str] = None,
        start_cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieve the children blocks of a specified block in the system.

        Args:
            page_size: Number of results per page.
            start_cursor: Cursor for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_database(
        self,
        filter: Optional[Dict[str, Any]] = None,
        sorts: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Get detailed information about a specific database in the system.

        Args:
            filter: Filters to apply to the database query.
            sorts: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_databases(
        self,
        filter: Optional[Dict[str, Any]] = None,
        page_size: Optional[int] = None,
        sort: Optional[Dict[str, Any]] = None,
        start_cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetch a list of databases available in the connected system.

        Args:
            filter: Filter criteria for Notion database entries.
            page_size: Number of records to return per page.
            sort: Sorting options for retrieved Notion data.
            start_cursor: Cursor for pagination, starting point for data retrieval. Remove this when you're getting data for first page.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_page(
        self,
        filter_properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get the content of a specific page within the application.

        Args:
            filter_properties: Specify the properties to filter by.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieve detailed information about a specific user in the connected system.

        Args:
            id: ID of the Notion resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def search(
        self,
        filter: Optional[Dict[str, Any]] = None,
        query: Optional[str] = None,
        start_cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Search for specific information in a designated database or system.

        Args:
            filter: Filter parameters for the Notion API request.
            query: Search query for the Notion API.
            start_cursor: Cursor for pagination in the Notion API.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_database(
        self,
        description: Optional[List[Any]] = None,
        properties: Optional[Dict[str, Any]] = None,
        title: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Update an existing database within the application to modify its structure or data.

        Args:
            description: 
            properties: Properties of the Notion page.
            title: 
        Returns:
            API response as a dictionary.
        """
        ...

