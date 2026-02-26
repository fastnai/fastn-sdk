"""Fastn Microsoft Teams connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MicrosoftTeamsConnector:
    """Microsoft Teams connector ().

    Provides 13 tools.
    """

    def create_subscription(
        self,
        changeType: str,
        expirationDateTime: str,
        resource: str,
        NotificationUrl: Optional[str] = None,
        clientState: Optional[str] = None,
        lifecycleNotificationUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new subscription for notifications in the Microsoft Teams connector.

        Args:
            changeType: Type of change that triggered the notification. (required)
            expirationDateTime: Expiration date and time for the notification. (required)
            resource: Resource related to the notification. (required)
            NotificationUrl: URL to receive notifications.
            clientState: 
            lifecycleNotificationUrl: URL for lifecycle notifications.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_teams(
        self,
        UserId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all teams available in the Microsoft Teams connector.

        Args:
            UserId: The ID of the user for the Microsoft Teams API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_channels(
        self,
        filter: Optional[str] = None,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all channels available in the Microsoft Teams connector.

        Args:
            filter: Filter criteria for Microsoft Teams data.
            select: Fields to select in the Microsoft Teams API response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_chat(
        self,
        chatId: str,
    ) -> Dict[str, Any]:
        """Gets specific details about a chat using the Microsoft Teams connector.

        Args:
            chatId: ID of the chat for Microsoft Teams. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_me(
        self,
    ) -> Dict[str, Any]:
        """Fetches the details of the current user in the Microsoft Teams connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_messages(
        self,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        skiptoken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of messages from a particular chat in the Microsoft Teams connector.

        Args:
            filter: Filter criteria for the Microsoft Teams data.
            orderby: Field to order the Microsoft Teams data by.
            skiptoken: 
            top: Number of records to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_my_chats(
        self,
        filter: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains a list of chats that the current user is involved in within the Microsoft Teams connector.

        Args:
            filter: 
            skipToken: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_my_joined_teams(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of teams that the current user has joined in the Microsoft Teams connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_team_channels(
        self,
        teamId: str,
    ) -> Dict[str, Any]:
        """Gets all channels associated with a specific team in the Microsoft Teams connector.

        Args:
            teamId: The ID of the Microsoft Teams team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_details(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific user in the Microsoft Teams connector.

        Args:
            userId: User ID for the Microsoft Teams API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
        count: Optional[str] = None,
        expand: Optional[str] = None,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        search: Optional[str] = None,
        select: Optional[str] = None,
        skip: Optional[str] = None,
        skiptoken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all users in the Microsoft Teams connector.

        Args:
            count: 
            expand: 
            filter: 
            orderby: 
            search: 
            select: 
            skip: 
            skiptoken: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def send_message_in_chat(
        self,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Sends a message in a specified chat using the Microsoft Teams connector.

        Args:
            body: Content of the message.
        Returns:
            API response as a dictionary.
        """
        ...

    def send_message_to_channel(
        self,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Sends a message to a specified channel in the Microsoft Teams connector.

        Args:
            body: The main body of the message sent to Microsoft Teams.
        Returns:
            API response as a dictionary.
        """
        ...

