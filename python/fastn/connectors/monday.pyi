"""Fastn Monday connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MondayConnector:
    """Monday connector ().

    Provides 13 tools.
    """

    def create_board(
        self,
    ) -> Dict[str, Any]:
        """Creates a new board in the Board Management connector, allowing for organization and tracking of tasks.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_item(
        self,
    ) -> Dict[str, Any]:
        """Creates a new item within a specific board in the Item Management connector to track tasks or projects.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_item_update(
        self,
        body: Optional[str] = None,
        itemId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates an update for an item in the Item Management connector, allowing for modifications and version control.

        Args:
            body: 
            itemId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_board(
        self,
    ) -> Dict[str, Any]:
        """Deletes a specified board from the Board Management connector, eliminating it and all associated items and data.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_item(
        self,
    ) -> Dict[str, Any]:
        """Deletes a specified item from the Item Management connector, removing it from the board.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified webhook from the Webhook Management connector, ceasing its operations and notifications.

        Args:
            webhookId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_boards(
        self,
    ) -> Dict[str, Any]:
        """Fetches the list of boards available in the Board Management connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_columns(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the list of columns within a board in the Board Management connector, outlining its structure and categories.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_item(
        self,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific item in the Item Management connector, providing insights into its attributes and status.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_logs_for_board(
        self,
    ) -> Dict[str, Any]:
        """Fetches the logs associated with a specific board in the Board Management connector to review activity and changes.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of users in the system from the User Management connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def register_webhook(
        self,
        boardId: Optional[str] = None,
        event: Optional[str] = None,
        webhookUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Registers a webhook in the Webhook Management connector to listen for specific events and trigger actions.

        Args:
            boardId: 
            event: 
            webhookUrl: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_item(
        self,
    ) -> Dict[str, Any]:
        """Updates the details of an existing item in the Item Management connector, ensuring that the item reflects the most current information.
        Returns:
            API response as a dictionary.
        """
        ...

