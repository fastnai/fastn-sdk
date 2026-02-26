"""Fastn Open AI connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class OpenAiConnector:
    """Open AI connector ().

    Provides 7 tools.
    """

    def api_generator(
        self,
        messages: List[Any],
        model: str,
        tools: List[Any],
    ) -> Dict[str, Any]:
        """Generates custom APIs and sync endpoints for your applications using the apiGenerator connector, perfect for developers looking to streamline backend integrations.

        Args:
            messages:  (required)
            model: Specifies the language model to use for the Open AI API call. (required)
            tools:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def chat_gpt(
        self,
        messages: List[Any],
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Engages in natural language conversation and generates human-like text responses using the chatGPT connector, ideal for customer support and interactive experiences.

        Args:
            messages:  (required)
            model: The OpenAI model to use (e.g., 'text-davinci-003').
        Returns:
            API response as a dictionary.
        """
        ...

    def create_batch_embeddings(
        self,
        input: List[Any],
        model: str,
        dimensions: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates multiple embeddings in a single batch using the CreateBatchEmbeddings connector, optimizing processing time for large datasets in natural language applications.

        Args:
            input: A list of input prompts or data for the OpenAI request. (required)
            model: The OpenAI model to use for generating the response. (required)
            dimensions: Optional dimensions parameter for the request (if applicable).
        Returns:
            API response as a dictionary.
        """
        ...

    def create_embeddings(
        self,
        input: str,
        dimensions: Optional[float] = None,
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates single embeddings for text inputs using the createEmbeddings connector, which can be used for semantic search and natural language processing tasks.

        Args:
            input: The input text for the Open AI model. (required)
            dimensions: 
            model: The name of the Open AI model to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_open_ai_models(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of available OpenAI models using the getOpenAIModels connector, helping developers choose the right model for their machine learning tasks.
        Returns:
            API response as a dictionary.
        """
        ...

    def image_generation(
        self,
        n: int,
        prompt: str,
        size: str,
    ) -> Dict[str, Any]:
        """Generates images based on textual descriptions using the imageGeneration connector, suitable for creative projects and visual content creation.

        Args:
            n: The number of responses to generate. (required)
            prompt: The text prompt to send to the Open AI model. (required)
            size: Specifies the size of the language model to use. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def table_generator(
        self,
        messages: List[Any],
        tools: List[Any],
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates structured data representations in tabular form using the table_generator connector, useful for organizing information and facilitating data analysis.

        Args:
            messages:  (required)
            tools:  (required)
            model: Specifies the OpenAI model to use.
        Returns:
            API response as a dictionary.
        """
        ...

