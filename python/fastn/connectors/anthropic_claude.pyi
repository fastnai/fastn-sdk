"""Fastn Anthropic Claude connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AnthropicClaudeConnector:
    """Anthropic Claude connector ().

    Provides 6 tools.
    """

    def anthropic_claude_count_message_tokens(
        self,
        messages: Optional[List[Any]] = None,
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Counts the number of tokens that a given message would consume when sent to an Anthropic Claude model, without actually sending the message. Use this tool to estimate token usage before making a request, to stay within model context limits or manage API costs. Do not use this tool to send a message — use anthropic_claude_create_message instead.

        Args:
            messages: 
            model: 
        Returns:
            API response as a dictionary.
        """
        ...

    def anthropic_claude_create_message(
        self,
        max_tokens: Optional[int] = None,
        messages: Optional[List[Any]] = None,
        model: Optional[str] = None,
        tool_choice: Optional[str] = None,
        tools: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Sends a synchronous message request to an Anthropic Claude model and returns the models response, supporting text and image inputs. Use this tool for real-time, single-turn or multi-turn AI interactions where an immediate response is required. Do not use this tool for processing large volumes of prompts — use anthropic_claude_create_message_batch instead.

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

    def anthropic_claude_create_message_batch(
        self,
        requests: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Submits a batch of message requests to the Anthropic Claude API for asynchronous processing, allowing multiple prompts to be handled in a single operation. Use this tool when you need to process a large number of prompts efficiently without waiting for each response individually. Results are not returned immediately — use anthropic_claude_get_message_batch_result to retrieve outputs once processing is complete. Do not use this tool for single, synchronous message interactions — use anthropic_claude_create_message instead.

        Args:
            requests: 
        Returns:
            API response as a dictionary.
        """
        ...

    def anthropic_claude_get_message_batch(
        self,
        messageBatch: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the status and metadata of a specific Anthropic Claude message batch by its batch ID, including processing state and request counts. Use this tool to check whether a batch has completed before fetching its results. Do not use this tool to retrieve the individual message responses — use anthropic_claude_get_message_batch_result instead.

        Args:
            messageBatch: 
        Returns:
            API response as a dictionary.
        """
        ...

    def anthropic_claude_get_message_batch_result(
        self,
        messageBatchId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the individual results of a completed Anthropic Claude message batch operation by batch ID, returning the models responses for each request in the batch. Use this tool after a batch has finished processing to collect outputs. Do not use this tool to check the status of a batch — use anthropic_claude_get_message_batch instead.

        Args:
            messageBatchId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def anthropic_claude_list_models(
        self,
    ) -> Dict[str, Any]:
        """Lists all available Anthropic Claude AI models accessible via the API, including their IDs and capabilities. Use this tool to discover which models are available for use in message creation or batch operations. Do not use this tool to create messages or count tokens.
        Returns:
            API response as a dictionary.
        """
        ...

