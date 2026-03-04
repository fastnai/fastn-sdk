"""Fastn MiniMax connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MinimaxConnector:
    """MiniMax connector ().

    Provides 1 tools.
    """

    def minimax_chat_completion(
        self,
        messages: List[Any],
        model: str,
    ) -> Dict[str, Any]:
        """Sends a chat completion request to the MiniMax AI API and returns a generated text response. Use this tool when you need to generate conversational AI responses, complete prompts, or interact with the MiniMax large language model. Do not use this tool for accounting, tax management, or any non-AI tasks. This tool makes a POST request to the MiniMax chat API and may incur usage costs per call.

        Args:
            messages:  (required)
            model: Model related to the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

