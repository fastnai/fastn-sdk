"""Fastn Discord connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _DiscordSendDmMessageAllowedMentions(TypedDict, total=False):
    parse: List[Any]

class _DiscordSendMessageToChannelAllowedMentions(TypedDict, total=False):
    parse: List[Any]
    roles: List[Any]
    users: List[Any]

class _DiscordSendMessageToChannelEmbed(TypedDict, total=False):
    author: Dict[str, Any]
    color: int
    description: str
    fields: List[Any]
    footer: Dict[str, Any]
    image: Dict[str, Any]
    thumbnail: Dict[str, Any]
    title: str

class DiscordConnector:
    """Discord connector ().

    Provides 14 tools.
    """

    def discord_create_dm_channel(
        self,
        name: str,
        icon: Optional[str] = None,
        last_message_id: Optional[str] = None,
        owner_id: Optional[str] = None,
        recipient_id: Optional[str] = None,
        type: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a direct message (DM) channel between the bot and a specified Discord user, returning the channel ID needed to send DMs. Use this before calling discord_send_dm_message when no existing DM channel ID is available for the target user. Does not send any message by itself.

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

    def discord_create_guild(
        self,
        name: str,
        afk_timeout: Optional[int] = None,
        default_message_notifications: Optional[int] = None,
        explicit_content_filter: Optional[int] = None,
        preferred_locale: Optional[str] = None,
        verification_level: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new Discord guild (server) with the authenticated bot as the owner. Use this to programmatically provision a new community server. Note that Discord restricts bot guild creation to accounts in fewer than 10 guilds. Do not use this to update an existing guild — use discord_update_guild instead.

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

    def discord_delete_guild(
        self,
        guildId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified Discord guild (server) and all of its channels, messages, roles, and members. Use this only when a guild must be fully removed. This action is irreversible — all guild data will be permanently lost. Requires a valid guildId and owner-level permissions.

        Args:
            guildId: ID of the Discord guild. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def discord_get_gateway_connection(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the Discord gateway WebSocket URL used by bots to establish a real-time connection for receiving events and updates from Discord. Use this during bot initialization to obtain the connection endpoint. Do not use this for REST API operations — it is only relevant for WebSocket-based bot event streaming. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def discord_get_guild(
        self,
        guildId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Discord guild (server) by its guild ID, including name, owner, member count, and settings. Use this for single-guild lookups. Do not use this to list all guilds — use discord_list_guilds instead. Does not modify any data.

        Args:
            guildId: ID of the Discord guild (server). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def discord_get_my_account(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the account information of the currently authenticated Discord user or bot, including username, ID, and avatar. Use this to confirm the identity of the active session or bot account. Do not use this to look up another users profile — use discord_get_user instead. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def discord_get_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Retrieves the public profile information of a specific Discord user by their user ID, including username, avatar, and account flags. Use this for single-user lookups. Do not use this to list all members of a guild — use discord_list_guild_members instead. Does not modify any data.

        Args:
            userId: The ID of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def discord_list_channels(
        self,
        serverId: str,
    ) -> Dict[str, Any]:
        """Returns all channels available in a specified Discord guild (server). Use this to discover channel IDs before sending messages or performing channel-specific operations. Requires a valid serverId. Does not modify any data.

        Args:
            serverId: The ID of the Discord server. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def discord_list_guild_members(
        self,
        guild_id: str,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of members (users) belonging to a specified Discord guild. Use this to enumerate guild membership or look up member details. Requires a valid guild_id. Do not use this to retrieve a single users profile — use discord_get_user instead. Does not modify any data.

        Args:
            guild_id: The ID of the Discord guild. (required)
            limit: The limit for the request (e.g., number of results).
        Returns:
            API response as a dictionary.
        """
        ...

    def discord_list_guilds(
        self,
        include_applications: Optional[bool] = None,
        with_counts: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all Discord guilds (servers) that the authenticated user or bot is a member of. Use this to discover available guilds and their IDs before performing guild-specific operations. Does not modify any data.

        Args:
            include_applications: Whether to include applications in the response.
            with_counts: Whether to include counts in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def discord_send_dm_message(
        self,
        channelId: str,
        content: str,
        allowed_mentions: Optional[_DiscordSendDmMessageAllowedMentions] = None,
        embeds: Optional[List[Any]] = None,
        flags: Optional[int] = None,
        tts: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Sends a direct message (DM) to a specific Discord user via an existing DM channel. Use this for private, one-on-one communication with a user rather than posting to a guild channel. Requires a valid DM channelId — create one first with discord_create_dm_channel if needed. Do not use this to post to public guild channels.

        Args:
            channelId: ID of the channel to send the message to. (required)
            content: The actual message content. (required)
            allowed_mentions: Mentions allowed in the message.
            embeds: 
            flags: Message flags (e.g., ephemeral messages).
            tts: Whether the message should be sent as text-to-speech.
        Returns:
            API response as a dictionary.
        """
        ...

    def discord_send_message(
        self,
        channelId: Optional[str] = None,
        content: Optional[str] = None,
        embeds: Optional[List[Any]] = None,
        tts: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Sends a message to a specified Discord channel by channel ID. Use this to post text content to a guild channel programmatically. Requires a valid channelId. Do not use this to send direct messages to users — use discord_send_dm_message instead. The message will be visible to all members with access to the channel.

        Args:
            channelId: 
            content: 
            embeds: 
            tts: 
        Returns:
            API response as a dictionary.
        """
        ...

    def discord_send_message_to_channel(
        self,
        channelId: str,
        content: str,
        allowed_mentions: Optional[_DiscordSendMessageToChannelAllowedMentions] = None,
        components: Optional[List[Any]] = None,
        embed: Optional[_DiscordSendMessageToChannelEmbed] = None,
        tts: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Sends a text message to a specified Discord channel. Use this to post announcements, notifications, or bot responses into a guild channel. Requires a valid channelId. Do not use this to send direct messages to users — use discord_send_dm_message instead. Sending a message is visible to all members with access to that channel.

        Args:
            channelId: The ID of the Discord channel. (required)
            content: The text content of the message. (required)
            allowed_mentions: Specifies which users and roles should be mentioned in the message.
            components: 
            embed: An embedded rich media object within the message.
            tts: Whether the message should be read aloud by Discord.
        Returns:
            API response as a dictionary.
        """
        ...

    def discord_update_guild(
        self,
        guildId: str,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the settings or metadata of an existing Discord guild, such as its name, icon, or region. Use this to modify guild configuration. Requires a valid guildId and sufficient permissions. Do not use this to delete a guild or manage individual channels.

        Args:
            guildId: Guild ID for the Discord API request. (required)
            name: Name parameter for the Discord API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

