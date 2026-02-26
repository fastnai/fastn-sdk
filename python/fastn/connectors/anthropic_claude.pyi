"""Fastn Anthropic Claude connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AnthropicClaudeConnector:
    """Anthropic Claude connector ().

    Provides 6 tools.
    """

    def count_message_token(
        self,
        messages: Optional[List[Any]] = None,
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Counts the number of tokens in a message for the specified messaging connector, helping to manage message size and character limits.

        Args:
            messages: 
            model: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_message(
        self,
        max_tokens: Optional[int] = None,
        messages: Optional[List[Any]] = None,
        model: Optional[str] = None,
        tool_choice: Optional[str] = None,
        tools: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new message using the specified messaging connector, allowing users to send text, images, or other content to recipients.

        Args:
            max_tokens: 
            messages: 
            model: 
            tool_choice: 
            tools: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_message_batch(
        self,
        requests: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a batch of messages using the specified messaging connector, enabling users to send multiple messages at once for efficiency.

        Args:
            requests: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_message_batch(
        self,
        messageBatch: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a batch of messages from the specified messaging connector, allowing users to access and manage previously sent messages.

        Args:
            messageBatch: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_message_batch_result(
        self,
        messageBatchId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains the results of a message batch operation from the specified messaging connector, providing status updates and feedback on message delivery.

        Args:
            messageBatchId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_modals(
        self,
    ) -> Dict[str, Any]:
        """Fetches available modals related to the specified messaging connector, allowing users to access interactive elements for enhancing user engagement.
        Returns:
            API response as a dictionary.
        """
        ...

