"""Fastn Gemini connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GeminiConnector:
    """Gemini connector ().

    Provides 5 tools.
    """

    def bounding_box_generation(
        self,
        contents: List[Any],
    ) -> Dict[str, Any]:
        """Generates bounding box coordinates for object detection tasks in computer vision applications.

        Args:
            contents:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def chat_completion(
        self,
        contents: List[Any],
    ) -> Dict[str, Any]:
        """Facilitates chat interactions by processing and generating conversational responses in natural language scenarios.

        Args:
            contents:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def code_execution(
        self,
        contents: Dict[str, Any],
        tools: List[Any],
    ) -> Dict[str, Any]:
        """Executes code snippets in a specified programming environment, enabling dynamic testing and debugging of algorithms.

        Args:
            contents: Content to be processed by the Gemini model. (required)
            tools:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_image_caption(
        self,
        contents: List[Any],
    ) -> Dict[str, Any]:
        """Creates descriptive captions for images, facilitating better understanding and accessibility in visual data interpretation.

        Args:
            contents:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_gemini_models(
        self,
        pageSize: Optional[str] = None,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves available models from the Gemini architecture for use in machine learning applications, enhancing the capability for AI development.

        Args:
            pageSize: 
            pageToken: 
        Returns:
            API response as a dictionary.
        """
        ...

