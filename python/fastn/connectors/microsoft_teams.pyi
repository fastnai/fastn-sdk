"""Fastn Microsoft Teams connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _MicrosoftTeamsSendMessageInChatBody(TypedDict, total=False):
    content: str

class _MicrosoftTeamsSendMessageToChannelBody(TypedDict, total=False):
    content: str

class MicrosoftTeamsConnector:
    """Microsoft Teams connector ().

    Provides 13 tools.
    """

    def microsoft_intune_create_subscription(
        self,
        changeType: str,
        expirationDateTime: str,
        resource: str,
        NotificationUrl: Optional[str] = None,
        clientState: Optional[str] = None,
        lifecycleNotificationUrl: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Microsoft Graph change notification subscription to receive real-time webhook notifications for Intune or Azure AD resource changes such as device state changes or group membership updates. Use this when you need continuous event-driven notifications delivered to a configured webhook endpoint. The subscription remains active until it expires or is explicitly deleted. This action has persistent side effects — notifications will be sent to the webhook endpoint until the subscription is removed. Do not use this for one-time data queries; use the appropriate list or get tool instead.

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

    def microsoft_teams_get_current_user(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the profile details of the currently authenticated Microsoft Teams user, including their user ID, display name, email address, and account settings. Use this when you need to identify who is making the request, display their profile, or obtain their user ID for personalization or authorization purposes. Do not use this to retrieve another users profile; use microsoft_teams_get_user_details with a specific user ID instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_teams_get_user_details(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific user in Microsoft Teams by user ID. Use this when you need to retrieve detailed information about a specific user, such as their profile, contact information, or account settings. Do not use this to retrieve all users at once; use microsoft_teams_list_users instead.

        Args:
            userId: User ID for the Microsoft Teams API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_teams_list_channels(
        self,
        teamId: str,
        filter: Optional[str] = None,
        select: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all channels available in a specified Microsoft Teams team. Use this tool when you need to list all channels within a team or to explore what channels are available. Do not use this tool to retrieve details about a single specific channel; use get_channel instead.

        Args:
            teamId: ID of the Microsoft Teams team. (required)
            filter: Filter criteria for Microsoft Teams data.
            select: Fields to select in the Microsoft Teams API response.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_teams_list_chat_members(
        self,
        chatId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all members in a specific chat. Use this when you need to see who is a member of a specific chat or when you need to check if a user is part of a chat. Do not use this to retrieve general chat metadata or chat settings.

        Args:
            chatId: ID of the chat for Microsoft Teams. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_teams_list_messages(
        self,
        chatId: str,
        filter: Optional[str] = None,
        orderby: Optional[str] = None,
        skiptoken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of messages from a specified chat in Microsoft Teams, identified by its chat ID. Use this when you need to fetch the message history of a specific chat. Do not use this to retrieve a single message by ID; use the appropriate get_message action instead. Do not use this to search messages by keyword; use search_messages instead.

        Args:
            chatId: ID of the chat in Microsoft Teams. (required)
            filter: Filter criteria for the Microsoft Teams data.
            orderby: Field to order the Microsoft Teams data by.
            skiptoken: 
            top: Number of records to retrieve.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_teams_list_my_chats(
        self,
        filter: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all chats that the currently authenticated user is a member of, including group chats and direct message conversations. Use this when you need to display a users chat list, find a specific chat by name, or obtain a chat ID for further operations such as sending messages or listing members. Do not use this to retrieve details about a single specific chat; use the appropriate get_chat action instead. This only returns chats for the authenticated user, not chats belonging to other users.

        Args:
            filter: 
            skipToken: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_teams_list_my_joined_teams(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all Microsoft Teams teams that the currently authenticated user has joined. Use this when you need to enumerate all teams the user is a member of, for example to display a team picker or find a team ID for further operations. Do not use this to retrieve teams the user has not joined or to search for teams by name.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_teams_list_team_channels(
        self,
        teamId: str,
    ) -> Dict[str, Any]:
        """Retrieves all channels associated with a specific Microsoft Teams team, identified by its team ID. Use this when you need to list all channels within a team, display them to the user, or find a channel ID for further operations such as sending messages. Do not use this to retrieve details of a single channel by ID; use the appropriate get_channel action instead. Note: this tool duplicates the functionality of microsoft_teams_list_channels — prefer using microsoft_teams_list_channels if both are available.

        Args:
            teamId: The ID of the Microsoft Teams team. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_teams_list_teams(
        self,
        UserId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all Microsoft Teams teams that the authenticated user has joined. Use this when you need to enumerate all teams the user is a member of. Do not use this to retrieve details of a single specific team; use the appropriate get_team action with a team ID instead.

        Args:
            UserId: The ID of the user for the Microsoft Teams API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_teams_list_users(
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
        """Retrieves a list of all users registered in the Microsoft Teams directory. Use this when you need to display a full user directory, enumerate all user accounts, or audit user membership. Do not use this to retrieve details about a single specific user; use microsoft_teams_get_user_details instead.

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

    def microsoft_teams_send_message_in_chat(
        self,
        chatId: str,
        body: Optional[_MicrosoftTeamsSendMessageInChatBody] = None,
    ) -> Dict[str, Any]:
        """Sends a message to a specified Teams chat, identified by its chat ID. Use this when you need to post a message into an existing group chat or direct message (1:1) chat. The message will be visible to all chat members and cannot be unsent once delivered. Do not use this to post a message to a team channel; use microsoft_teams_send_message_to_channel instead.

        Args:
            chatId: The ID of the chat to send the message to. (required)
            body: Content of the message.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_teams_send_message_to_channel(
        self,
        channelId: str,
        teamId: str,
        body: Optional[_MicrosoftTeamsSendMessageToChannelBody] = None,
    ) -> Dict[str, Any]:
        """Sends a message to a specified channel in Microsoft Teams. Use this tool when you need to post a message to a specific team channel. This creates a new message record in the channel timeline and notifies channel members based on their notification settings. Once sent, the message is permanently added to the channel. While you can edit or delete the message later, it cannot be unsent instantaneously. Do not use this tool to send direct messages to users; use send_direct_message instead.

        Args:
            channelId: The ID of the target channel within the team. (required)
            teamId: The ID of the target team. (required)
            body: The main body of the message sent to Microsoft Teams.
        Returns:
            API response as a dictionary.
        """
        ...

