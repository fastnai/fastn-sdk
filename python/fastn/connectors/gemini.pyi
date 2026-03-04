"""Fastn Gemini connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _GeminiCodeExecutionContents(TypedDict, total=False):
    parts: Dict[str, Any]

class GeminiConnector:
    """Gemini connector ().

    Provides 5 tools.
    """

    def gemini_bounding_box_generation(
        self,
        contents: List[Any],
        model: str,
    ) -> Dict[str, Any]:
        """Submits an image to a specified Gemini model and returns bounding box coordinates identifying the locations of detected objects within the image. Use this for computer vision tasks that require spatial object localization. The target model must support multimodal input — use gemini_list_models to verify. Do not use this for generating image captions without coordinates — use gemini_generate_image_caption instead.

        Args:
            contents:  (required)
            model: The name of the model to use. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def gemini_chat_completion(
        self,
        contents: List[Any],
        model: str,
    ) -> Dict[str, Any]:
        """Sends a prompt to a specified Gemini model and returns a generated natural language response. Use this for conversational interactions, question answering, summarization, or general text generation tasks. The target model must be specified in the request. Do not use this for image captioning or object detection — use gemini_generate_image_caption or gemini_bounding_box_generation instead.

        Args:
            contents:  (required)
            model: Specifies the model to use for the Gemini API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def gemini_code_execution(
        self,
        contents: _GeminiCodeExecutionContents,
        model: str,
        tools: List[Any],
    ) -> Dict[str, Any]:
        """Submits a code snippet to a specified Gemini model that supports code execution and returns the result of running the code. Use this to dynamically test, debug, or evaluate algorithms through the Gemini API. The target model must support code execution capabilities — use gemini_list_models to verify. Do not use this for general text generation — use gemini_chat_completion instead.

        Args:
            contents: Content to be processed by the Gemini model. (required)
            model: Name of the Gemini model to use. (required)
            tools:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def gemini_generate_image_caption(
        self,
        contents: List[Any],
        model: str,
    ) -> Dict[str, Any]:
        """Submits an image to a specified Gemini model and returns a descriptive natural language caption. Use this to generate textual descriptions of images for accessibility, indexing, or visual data interpretation. The target model must support multimodal input — use gemini_list_models to verify. Do not use this for object detection with coordinates — use gemini_bounding_box_generation instead.

        Args:
            contents:  (required)
            model: Specifies the model to use for the Gemini API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def gemini_list_models(
        self,
        pageSize: Optional[str] = None,
        pageToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all available Gemini generative AI models from the Google Generative Language API. Returns model names, versions, and supported generation methods. Use this to discover which models are available before calling gemini_chat_completion, gemini_code_execution, gemini_generate_image_caption, or gemini_bounding_box_generation. Do not use this to generate content — use the appropriate generation tool instead.

        Args:
            pageSize: 
            pageToken: 
        Returns:
            API response as a dictionary.
        """
        ...

