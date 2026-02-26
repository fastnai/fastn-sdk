"""Fastn Discord connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class DiscordConnector:
    """Discord connector ().

    Provides 14 tools.
    """

    def create_dm_channel(
        self,
        name: str,
        icon: Optional[str] = None,
        last_message_id: Optional[str] = None,
        owner_id: Optional[str] = None,
        recipient_id: Optional[str] = None,
        type: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a direct message (DM) channel between users in the application.

        Args:
            name: Name of the item. (required)
            icon: URL of the icon.
            last_message_id: The ID of the last message.
            owner_id: The ID of the owner.
            recipient_id: The ID of the recipient.
            type: Type of the item.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_guild(
        self,
        name: str,
        afk_timeout: Optional[int] = None,
        default_message_notifications: Optional[int] = None,
        explicit_content_filter: Optional[int] = None,
        preferred_locale: Optional[str] = None,
        verification_level: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new guild (community) in the application.

        Args:
            name: The name associated with the request. (required)
            afk_timeout: Timeout duration for Away From Keyboard (AFK) status.
            default_message_notifications: Default notification settings for messages.
            explicit_content_filter: Level of explicit content filtering.
            preferred_locale: The preferred locale for the user.
            verification_level: The verification level for the server.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_guild(
        self,
        guildId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified guild from the application.

        Args:
            guildId: ID of the Discord guild. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_channels_(
        self,
        serverId: str,
    ) -> Dict[str, Any]:
        """Gets a list of channels available in a specific guild in the application.

        Args:
            serverId: The ID of the Discord server. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_gateway_connection(
        self,
    ) -> Dict[str, Any]:
        """Establishes a connection to the gateway for real-time communication in the application.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_guild(
        self,
        guildId: str,
    ) -> Dict[str, Any]:
        """Fetches the details of a specific guild in the application.

        Args:
            guildId: ID of the Discord guild (server). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_guilds(
        self,
        include_applications: Optional[bool] = None,
        with_counts: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all guilds that the user is a member of in the application.

        Args:
            include_applications: Whether to include applications in the response.
            with_counts: Whether to include counts in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_my_account(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the account information of the user in the application.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific user in the application.

        Args:
            userId: The ID of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of users in the application.

        Args:
            limit: The limit for the request (e.g., number of results).
        Returns:
            API response as a dictionary.
        """
        ...

    def send_dm_message(
        self,
        content: str,
        allowed_mentions: Optional[Dict[str, Any]] = None,
        embeds: Optional[List[Any]] = None,
        flags: Optional[int] = None,
        tts: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Sends a direct message to a specified user in the application.

        Args:
            content: The actual message content. (required)
            allowed_mentions: Mentions allowed in the message.
            embeds: 
            flags: Message flags (e.g., ephemeral messages).
            tts: Whether the message should be sent as text-to-speech.
        Returns:
            API response as a dictionary.
        """
        ...

    def send_message(
        self,
        content: Optional[str] = None,
        embeds: Optional[List[Any]] = None,
        tts: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Sends a message to a specified channel in the application.

        Args:
            content: 
            embeds: 
            tts: 
        Returns:
            API response as a dictionary.
        """
        ...

    def send_message_to_channel_(
        self,
        content: str,
        allowed_mentions: Optional[Dict[str, Any]] = None,
        components: Optional[List[Any]] = None,
        embed: Optional[Dict[str, Any]] = None,
        tts: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Sends a message to a specific channel within the application.

        Args:
            content: The text content of the message. (required)
            allowed_mentions: Specifies which users and roles should be mentioned in the message.
            components: 
            embed: An embedded rich media object within the message.
            tts: Whether the message should be read aloud by Discord.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_guild(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the information of an existing guild in the application.

        Args:
            name: Name parameter for the Discord API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

