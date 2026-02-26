"""Fastn MiniMax connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MinimaxConnector:
    """MiniMax connector ().

    Provides 1 tools.
    """

    def chat_completion(
        self,
        messages: List[Any],
        model: str,
    ) -> Dict[str, Any]:
        """Generates conversational responses in the chatCompletion context, allowing for dynamic and interactive dialog with users.

        Args:
            messages:  (required)
            model: Model related to the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

