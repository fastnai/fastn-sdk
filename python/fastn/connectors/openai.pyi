"""Fastn OpenAI connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class OpenaiConnector:
    """OpenAI connector ().

    Provides 7 tools.
    """

    def open_ai_chat_completion(
        self,
        messages: List[Any],
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a conversational prompt to OpenAIs chat completions API and returns a natural-language response. Use this tool for open-ended question answering, customer support automation, content generation, summarization, and any interactive text-based task. Do not use this tool when you need structured tabular output or API spec generation; use the dedicated table or API generation tools instead. This operation sends data to OpenAIs external API and consumes token quota proportional to input and output length.

        Args:
            messages:  (required)
            model: The OpenAI model to use (e.g., 'text-davinci-003').
        Returns:
            API response as a dictionary.
        """
        ...

    def open_ai_create_batch_embeddings(
        self,
        input: List[Any],
        model: str,
        dimensions: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates vector embeddings for multiple text inputs in a single batch request using OpenAIs embeddings API. Use this tool when you need to embed large datasets of text efficiently in one call, minimizing API round-trips for semantic search, clustering, or classification pipelines. Prefer this over the single-embedding tool when processing more than one text at a time. Note: this sends data to OpenAIs external API and will consume API quota proportional to the number of tokens submitted.

        Args:
            input: A list of input prompts or data for the OpenAI request. (required)
            model: The OpenAI model to use for generating the response. (required)
            dimensions: Optional dimensions parameter for the request (if applicable).
        Returns:
            API response as a dictionary.
        """
        ...

    def open_ai_create_embedding(
        self,
        input: str,
        dimensions: Optional[float] = None,
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a single vector embedding for a text input using OpenAIs embeddings API. Use this tool to convert a piece of text into a numerical vector representation suitable for semantic search, similarity comparison, or downstream machine learning tasks. For embedding multiple texts at once, use the batch embeddings tool instead. This operation sends data to OpenAIs external API and consumes token quota.

        Args:
            input: The input text for the Open AI model. (required)
            dimensions: 
            model: The name of the Open AI model to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def open_ai_generate_api_spec(
        self,
        messages: List[Any],
        model: str,
        tools: List[Any],
    ) -> Dict[str, Any]:
        """Generates API specifications, endpoint definitions, or backend integration code from a natural-language description using OpenAIs chat completions API. Use this tool when you need to scaffold API contracts or integration blueprints for development workflows. Do not use this tool for general-purpose chat or unrelated content generation. Output quality depends on the specificity of the prompt provided.

        Args:
            messages:  (required)
            model: Specifies the language model to use for the Open AI API call. (required)
            tools:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def open_ai_generate_image(
        self,
        n: int,
        prompt: str,
        size: str,
    ) -> Dict[str, Any]:
        """Generates one or more images from a natural-language text prompt using OpenAIs DALL·E image generation API. Use this tool when you need to create original images for creative projects, visual content, or prototyping. Returns image URLs or base64-encoded image data depending on the response format requested. Do not use this tool for editing or modifying existing images. This operation consumes OpenAI API credits and the generated images may expire after a short time if accessed via URL.

        Args:
            n: The number of responses to generate. (required)
            prompt: The text prompt to send to the Open AI model. (required)
            size: Specifies the size of the language model to use. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def open_ai_generate_table(
        self,
        messages: List[Any],
        tools: List[Any],
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates a structured tabular data representation from a natural-language prompt or unstructured input using OpenAIs chat completions API. Use this tool when you need to organize information into rows and columns for data analysis, reporting, or display purposes. Do not use this tool for general-purpose conversation or non-tabular text generation; use the chat completion tool instead. Output format and schema depend on the prompt provided.

        Args:
            messages:  (required)
            tools:  (required)
            model: Specifies the OpenAI model to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def open_ai_list_models(
        self,
    ) -> Dict[str, Any]:
        """Returns the full list of OpenAI models available to the authenticated account, including model IDs, ownership, and creation timestamps. Use this tool to discover which models are accessible before selecting one for completions, embeddings, or fine-tuning. Do not use this tool to retrieve details about a single model by ID. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

