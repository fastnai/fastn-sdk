"""Fastn Telegram connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class TelegramConnector:
    """Telegram connector ().

    Provides 10 tools.
    """

    def telegram_delete_message(
        self,
        chat_id: str,
        message_id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific message from a Telegram chat by chat ID and message ID. Use this tool when you need to remove an incorrect, outdated, or inappropriate message sent by the bot. Note that message deletion is irreversible—the message cannot be recovered after deletion. The bot must have the appropriate delete permissions in the target chat. Do not use this tool to edit message content (use telegram_edit_message_text or telegram_edit_message_caption instead).

        Args:
            chat_id: Unique identifier for the target chat. (required)
            message_id: Unique identifier for the message. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def telegram_edit_message_caption(
        self,
        chat_id: str,
        message_id: str,
        business_connection_id: Optional[str] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[str] = None,
        inline_message_id: Optional[str] = None,
        parse_mode: Optional[str] = None,
        reply_markup: Optional[str] = None,
        show_caption_above_media: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Edits the caption of a previously sent Telegram message that contains media (such as a photo, video, or document). Use this tool when you need to update the descriptive text attached to a media message without resending the media. Do not use this tool to edit plain text messages (use telegram_edit_message_text) or to modify the media file itself. Only messages sent by the bot can be edited.

        Args:
            chat_id: Unique identifier for the target chat. (required)
            message_id: Unique identifier for the message. (required)
            business_connection_id: Identifier for the business connection (if applicable).
            caption: Caption for the message.
            caption_entities: List of special entities in the caption (e.g., hashtags, mentions).
            inline_message_id: Unique identifier for an inline message.
            parse_mode: Formatting style for the message text (e.g., Markdown, HTML).
            reply_markup: Custom keyboard or inline buttons for the message.
            show_caption_above_media: Specifies whether to show the caption above the media.
        Returns:
            API response as a dictionary.
        """
        ...

    def telegram_edit_message_text(
        self,
        chat_id: str,
        message_id: str,
        text: str,
        business_connection_id: Optional[str] = None,
        disable_web_page_preview: Optional[str] = None,
        entities: Optional[str] = None,
        inline_message_id: Optional[str] = None,
        link_preview_options: Optional[str] = None,
        parse_mode: Optional[str] = None,
        reply_markup: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Edits the text content of a previously sent Telegram text message. Use this tool when you need to correct, update, or append information to an existing bot message in a chat. Do not use this tool to edit media captions (use telegram_edit_message_caption) or to send a new message (use telegram_send_message). Only messages originally sent by the bot can be edited, and edits are visible to all chat participants.

        Args:
            chat_id: Unique identifier for the target chat. (required)
            message_id: Unique identifier for the message (optional, for replies). (required)
            text: The text content of the message. (required)
            business_connection_id: Identifier for the business connection (optional).
            disable_web_page_preview: Disables link previews for the message (optional, boolean).
            entities: List of special entities that appear in the text (optional, array of objects).
            inline_message_id: Unique identifier for the inline message (optional).
            link_preview_options: Options for customizing link previews (optional).
            parse_mode: Formatting style for the message text (optional).
            reply_markup: Custom keyboard or inline keyboard (optional, JSON object).
        Returns:
            API response as a dictionary.
        """
        ...

    def telegram_get_chat(
        self,
        chat_id: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed metadata for a specific Telegram chat, including its title, type (private, group, supergroup, or channel), description, member count, and settings. Use this tool when you need to inspect or validate chat properties before sending messages or performing administrative actions. Do not use this tool to retrieve message history or chat updates (use telegram_list_updates instead).

        Args:
            chat_id: The unique identifier for the Telegram chat. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def telegram_list_updates(
        self,
        allowed_updates: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        timeout: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of pending incoming updates for the bot, including new messages, edited messages, callback queries, and other events, using Telegrams long-polling mechanism. Use this tool to process incoming user interactions when webhooks are not configured. Do not use this tool to retrieve static chat metadata (use telegram_get_chat) or to send messages. Note that confirmed updates are removed from the queue once acknowledged, so each update should be processed exactly once.

        Args:
            allowed_updates: Specifies the types of updates to receive.
            limit: Limits the number of updates to be retrieved.
            offset: Identifier of the first update to be returned.
            timeout: Timeout in seconds for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def telegram_send_audio(
        self,
        audio: str,
        chat_id: str,
        allow_paid_broadcast: Optional[str] = None,
        allow_sending_without_reply: Optional[str] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[str] = None,
        disable_notification: Optional[str] = None,
        duration: Optional[str] = None,
        message_thread_id: Optional[str] = None,
        parse_mode: Optional[str] = None,
        performer: Optional[str] = None,
        protect_content: Optional[str] = None,
        reply_bodyeters: Optional[str] = None,
        reply_markup: Optional[str] = None,
        reply_to_message_id: Optional[str] = None,
        thumbnail: Optional[str] = None,
        title: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends an audio file to a specified Telegram chat or user, displayed in the Telegram music player with support for title and performer metadata. Use this tool when you need to share music or audio recordings in formats such as MP3. Do not use this tool for OGG/OPUS voice messages (use telegram_send_voice) or general file attachments (use telegram_send_document). Sending audio is a write operation and is visible to all participants in the target chat.

        Args:
            audio: Audio file to be sent (if applicable). (required)
            chat_id: The ID of the chat to send the message to. (required)
            allow_paid_broadcast: Indicates whether paid broadcast is allowed.
            allow_sending_without_reply: Indicates whether sending without reply is allowed.
            caption: Caption for the message.
            caption_entities: Entities within the caption (e.g., mentions, hashtags).
            disable_notification: Indicates whether to disable notification for the message.
            duration: Duration of the audio (if applicable).
            message_thread_id: The ID of the message thread (if applicable).
            parse_mode: The parsing mode for the message text (e.g., Markdown).
            performer: Performer name (if applicable).
            protect_content: Indicates whether to protect content from forwarding.
            reply_bodyeters: Parameters for reply message (if applicable).
            reply_markup: Custom keyboard or inline buttons for the message.
            reply_to_message_id: ID of the message to reply to.
            thumbnail: Thumbnail for the message (if applicable).
            title: Title of the message (if applicable).
        Returns:
            API response as a dictionary.
        """
        ...

    def telegram_send_document(
        self,
        chat_id: str,
        document: str,
        allow_paid_broadcast: Optional[str] = None,
        allow_sending_without_reply: Optional[str] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[str] = None,
        disable_content_type_detection: Optional[str] = None,
        disable_notification: Optional[str] = None,
        message_thread_id: Optional[str] = None,
        parse_mode: Optional[str] = None,
        protect_content: Optional[str] = None,
        reply_bodyeters: Optional[str] = None,
        reply_markup: Optional[str] = None,
        reply_to_message_id: Optional[str] = None,
        thumbnail: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a file as a document to a specified Telegram chat or user. Use this tool when you need to deliver files such as PDFs, spreadsheets, ZIPs, or other file types that should be received as downloadable attachments. Do not use this tool for sending photos intended for inline display (use telegram_send_photo), audio files (use telegram_send_audio), or voice messages (use telegram_send_voice). Sending a document is a write operation and is visible to all participants in the target chat.

        Args:
            chat_id: Unique identifier for the target chat. (required)
            document: The document file ID to be sent. (required)
            allow_paid_broadcast: Allows sending the message to a paid broadcast channel.
            allow_sending_without_reply: Allows sending the message without waiting for a reply.
            caption: The caption of the document.
            caption_entities: List of special entities that appear in the caption (like usernames, URLs, etc.).
            disable_content_type_detection: Disables automatic detection of the document's content type.
            disable_notification: Sends the message silently. Users will receive a notification with no sound.
            message_thread_id: Unique identifier for the target message thread.
            parse_mode: The format of the caption (Markdown, HTML).
            protect_content: Protects the content from forwarding and prevents saving.
            reply_bodyeters: If the message is a reply, this is the ID of the original message.
            reply_markup: Additional markup for the message (inline keyboard, etc.).
            reply_to_message_id: ID of the message to which this message is a reply.
            thumbnail: Thumbnail for the document.
        Returns:
            API response as a dictionary.
        """
        ...

    def telegram_send_message(
        self,
        chat_id: str,
        text: str,
        allow_sending_without_reply: Optional[str] = None,
        business_connection_id: Optional[str] = None,
        disable_notification: Optional[str] = None,
        disable_web_page_preview: Optional[str] = None,
        entities: Optional[str] = None,
        link_preview_options: Optional[str] = None,
        message_thread_id: Optional[str] = None,
        parse_mode: Optional[str] = None,
        protect_content: Optional[str] = None,
        reply_bodyeters: Optional[str] = None,
        reply_markup: Optional[str] = None,
        reply_to_message_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a plain text message to a specified Telegram user, group, supergroup, or channel using the bot. Supports optional formatting modes (Markdown or HTML) and reply markup. Use this tool for delivering text-based notifications, responses, or alerts. Do not use this tool to send media such as photos (use telegram_send_photo), audio (use telegram_send_audio), documents (use telegram_send_document), or voice messages (use telegram_send_voice). Sending a message is a write operation and is immediately visible to all participants in the target chat.

        Args:
            chat_id: Unique identifier for the target chat. (required)
            text: The text content of the message. (required)
            allow_sending_without_reply: Allows sending messages without a reply.
            business_connection_id: Identifier for the business connection (if applicable).
            disable_notification: Disables notification for the message.
            disable_web_page_preview: Disables web page preview for the message.
            entities: List of special entities in the message text.
            link_preview_options: Options for customizing link previews.
            message_thread_id: Unique identifier for the message thread.
            parse_mode: Formatting style for the message text.
            protect_content: Protects the content of the message.
            reply_bodyeters: Message reply parameters.
            reply_markup: Custom keyboard or inline buttons for the message.
            reply_to_message_id: ID of the message to reply to.
        Returns:
            API response as a dictionary.
        """
        ...

    def telegram_send_photo(
        self,
        chat_id: str,
        photo: str,
        allow_paid_broadcast: Optional[str] = None,
        allow_sending_without_reply: Optional[str] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[str] = None,
        disable_notification: Optional[str] = None,
        has_spoiler: Optional[str] = None,
        message_thread_id: Optional[str] = None,
        parse_mode: Optional[str] = None,
        protect_content: Optional[str] = None,
        reply_bodyeters: Optional[str] = None,
        reply_markup: Optional[str] = None,
        reply_to_message_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a photo to a specified Telegram chat or user, displayed inline in the chat. An optional caption can be included. Use this tool when you need to deliver image content such as screenshots, charts, or pictures. Do not use this tool for sending general files or non-image documents (use telegram_send_document) or audio content. Sending a photo is a write operation and is visible to all participants in the target chat.

        Args:
            chat_id: Unique identifier for the target chat. (required)
            photo: Photo to be sent. (required)
            allow_paid_broadcast: Allows paid broadcasts (boolean,optional).
            allow_sending_without_reply: Allows sending without reply (boolean,optional).
            caption: Caption for the photo.
            caption_entities: List of special entities that appear in the caption (optional).
            disable_notification: Disables notification for the message (boolean, optional).
            has_spoiler: Marks message as spoiler (boolean, optional).
            message_thread_id: Unique identifier for the target message thread (optional).
            parse_mode: Formatting of the caption (optional).
            protect_content: Protects the content from forwarding (boolean, optional).
            reply_bodyeters: List of users to reply to (optional).
            reply_markup: Inline keyboard markup (optional).
            reply_to_message_id: ID of the message to reply to (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def telegram_send_voice(
        self,
        chat_id: str,
        voice: str,
        allow_paid_broadcast: Optional[str] = None,
        allow_sending_without_reply: Optional[str] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[str] = None,
        disable_notification: Optional[str] = None,
        duration: Optional[str] = None,
        message_thread_id: Optional[str] = None,
        parse_mode: Optional[str] = None,
        protect_content: Optional[str] = None,
        reply_bodyeters: Optional[str] = None,
        reply_markup: Optional[str] = None,
        reply_to_message_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends an audio file as a voice message to a specified Telegram chat or user. The file must be in OGG format encoded with OPUS for Telegram to display it as a playable voice note. Use this tool when you need to deliver spoken audio content, such as voice notifications or recorded messages. Do not use this tool to send general audio files in other formats (use telegram_send_audio) or documents (use telegram_send_document). Sending a message is a write operation and is visible to all participants in the target chat.

        Args:
            chat_id: Telegram API Parameter: Unique identifier for the target chat. (required)
            voice: Telegram API Parameter: Voice file to send. (required)
            allow_paid_broadcast: Telegram API Parameter: Whether paid broadcast is allowed.
            allow_sending_without_reply: Telegram API Parameter: Whether sending without reply is allowed.
            caption: Telegram API Parameter: Caption for the voice message.
            caption_entities: Telegram API Parameter: Entities within the caption.
            disable_notification: Telegram API Parameter: Whether to disable notification for the message.
            duration: Telegram API Parameter: Duration of the voice message.
            message_thread_id: Telegram API Parameter: Unique identifier for the target message thread.
            parse_mode: Telegram API Parameter: Format for parsing the caption.
            protect_content: Telegram API Parameter: Whether to protect content from forwarding.
            reply_bodyeters: Telegram API Parameter:  (Typo assumed) Reply parameters.  Clarification needed.
            reply_markup: Telegram API Parameter: Inline keyboard markup for the message.
            reply_to_message_id: Telegram API Parameter: ID of the message to reply to.
        Returns:
            API response as a dictionary.
        """
        ...

