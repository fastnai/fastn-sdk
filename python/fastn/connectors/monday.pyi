"""Fastn Monday connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MondayConnector:
    """Monday connector ().

    Provides 13 tools.
    """

    def monday_create_board(
        self,
        BoardName: str,
    ) -> Dict[str, Any]:
        """Creates a new board in Monday.com with a specified name and configuration, allowing you to organize tasks and projects. Use this tool when you need to set up a new workspace or project board. Do not use this tool to add items to an existing board — use the create item tool for that purpose.

        Args:
            BoardName: The name of the Monday.com board. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def monday_create_item(
        self,
        BoardID: Optional[str] = None,
        ItemName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new item (task or record) within a specified Monday.com board, optionally setting its column values at creation time. Use this tool when you need to add a new task, project entry, or record to an existing board. Do not use this tool to create a new board — use the create board tool for that purpose.

        Args:
            BoardID: The ID of the Monday.com board.
            ItemName: The name of the item on the Monday.com board.
        Returns:
            API response as a dictionary.
        """
        ...

    def monday_create_item_update(
        self,
        body: Optional[str] = None,
        itemId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Posts a new update (comment or note) on a specific item in Monday.com, enabling communication and change tracking on that item. Use this tool when you need to add a textual update or comment to an existing item. Do not use this tool to modify item column values or metadata — use the update item tool for that purpose.

        Args:
            body: 
            itemId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def monday_delete_board(
        self,
        BoardID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified board from Monday.com, along with all of its items, columns, and associated data. Use this tool only when a board and all its contents need to be completely removed. Do not use this tool if you only want to archive a board or delete individual items. This action is irreversible — all board data will be permanently lost.

        Args:
            BoardID: The ID of the Monday.com board.
        Returns:
            API response as a dictionary.
        """
        ...

    def monday_delete_item(
        self,
        ItemID: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified item from a Monday.com board, removing all of its data and updates. Use this tool when a task or record needs to be fully removed from a board. Do not use this tool if you only want to update or archive an item. This action is irreversible — the deleted item cannot be recovered.

        Args:
            ItemID: ID of the item in Monday.com. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def monday_delete_webhook(
        self,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified webhook from Monday.com, stopping it from listening for events and sending notifications. Use this tool when you need to deregister a webhook that is no longer needed. Do not use this tool if you only want to pause or update a webhook. This action is irreversible — the deleted webhook cannot be restored and must be recreated if needed again.

        Args:
            webhookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def monday_get_item(
        self,
        ItemID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details and column values of a specific item on a Monday.com board by its ID. Use this tool when you need to read the current state, attributes, or status of a single item. Do not use this tool to retrieve multiple items or boards — use the appropriate list tool for that purpose.

        Args:
            ItemID: ID of the item in Monday.com
        Returns:
            API response as a dictionary.
        """
        ...

    def monday_list_boards(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the list of all boards available in the connected Monday.com account. Use this tool when you need to discover existing boards, their IDs, or their configurations before performing board-level operations. Do not use this tool to retrieve items within a board — use the get item tool for that purpose.
        Returns:
            API response as a dictionary.
        """
        ...

    def monday_list_columns(
        self,
        BoardID: str,
    ) -> Dict[str, Any]:
        """Retrieves the list of all columns defined within a specific Monday.com board, including their types and configuration. Use this tool when you need to understand the structure of a board before reading or writing item data. Do not use this tool to retrieve item values — use the get item tool for that purpose.

        Args:
            BoardID: The ID of the Monday.com board. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def monday_list_logs_for_board(
        self,
        BoardID: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the activity logs associated with a specific Monday.com board, providing a history of changes and actions performed on it. Use this tool when you need to audit or review what has changed on a board over time. Do not use this tool to retrieve item data or column structure — use the appropriate item or column tools for those purposes.

        Args:
            BoardID: The ID of the Monday.com board.
        Returns:
            API response as a dictionary.
        """
        ...

    def monday_list_users(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all users in the connected Monday.com account, including their names, emails, and roles. Use this tool when you need to look up user IDs for assignment or to audit account membership. Do not use this tool to retrieve item or board data — use the appropriate board or item tools for those purposes.
        Returns:
            API response as a dictionary.
        """
        ...

    def monday_register_webhook(
        self,
        boardId: Optional[str] = None,
        event: Optional[str] = None,
        webhookUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Registers a new webhook in Monday.com to listen for specific board or item events and trigger configured actions or notifications. Use this tool when you need to set up event-driven integrations that respond to changes in Monday.com. Do not use this tool to update or delete an existing webhook — use the appropriate update or delete tool instead.

        Args:
            boardId: 
            event: 
            webhookUrl: 
        Returns:
            API response as a dictionary.
        """
        ...

    def monday_update_item(
        self,
        BoardID: Optional[str] = None,
        ColumnID: Optional[str] = None,
        ItemID: Optional[str] = None,
        Label: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the column values or attributes of an existing item on a Monday.com board. Use this tool when you need to modify the details, status, assignee, or any other field of an existing item. Do not use this tool to post a comment or textual update on an item — use the create item update tool for that purpose.

        Args:
            BoardID: The ID of the Monday.com board.
            ColumnID: The ID of the column in the Monday.com board.
            ItemID: The ID of the item in the Monday.com board.
            Label: Label for the item.
        Returns:
            API response as a dictionary.
        """
        ...

