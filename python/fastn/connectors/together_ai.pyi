"""Fastn Together AI connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TogetherAiConnector:
    """Together AI connector ().

    Provides 9 tools.
    """

    def chat_generate(
        self,
        messages: List[Any],
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates conversational responses based on user input using the chatGenerate connector.

        Args:
            messages:  (required)
            model: Specifies the AI model to use for processing.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_completion(
        self,
        max_tokens: int,
        model: str,
        prompt: str,
        temperature: float,
    ) -> Dict[str, Any]:
        """Creates text completions based on prompt inputs through the createCompletion connector.

        Args:
            max_tokens: Maximum number of tokens to generate in the Together AI response. (required)
            model: Specifies the model to use for the Together AI request. (required)
            prompt: The input prompt for the Together AI API. (required)
            temperature: Temperature parameter controlling the randomness of the Together AI response. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_embedding(
        self,
        input: str,
        model: str,
    ) -> Dict[str, Any]:
        """Generates embeddings for input text to facilitate semantic search or similarity tasks using the createEmbedding connector.

        Args:
            input: Input data for the Together AI API. (required)
            model: Specifies the model to use for processing the input in Together AI API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_image(
        self,
        height: int,
        prompt: str,
        width: int,
        model: Optional[str] = None,
        n: Optional[int] = None,
        steps: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates an image based on specified parameters and prompts using the createImage connector.

        Args:
            height: Height of the generated image. (required)
            prompt: Text prompt describing the desired image. (required)
            width: Width of the generated image. (required)
            model: Name of the model to use for image generation.
            n: Number of images to generate.
            steps: Number of diffusion steps.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_rerank_request(
        self,
        documents: Optional[List[Any]] = None,
        model: Optional[str] = None,
        query: Optional[str] = None,
        rank_fields: Optional[List[Any]] = None,
        return_documents: Optional[bool] = None,
        top_n: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Submits a request to rerank documents based on relevance using the createRerankRequest connector.

        Args:
            documents: 
            model: Name of the model to use in Together AI.
            query: Search query to be processed by Together AI.
            rank_fields: Fields to use for ranking results in Together AI.
            return_documents: Flag indicating whether to return the documents in the response from Together AI.
            top_n: Number of top results to return from Together AI.
        Returns:
            API response as a dictionary.
        """
        ...

    def inference(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        model: Optional[str] = None,
        n: Optional[int] = None,
        repetition_penalty: Optional[int] = None,
        stop: Optional[List[Any]] = None,
        temperature: Optional[float] = None,
        top_k: Optional[int] = None,
        top_p: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Performs inference on given data to yield predictions or outputs through the inference connector.

        Args:
            prompt: The input prompt for text generation in Together AI. (required)
            max_tokens: Maximum number of tokens to generate for Together AI.
            model: Specifies the model to use for text generation in Together AI.
            n: Number of different outputs to generate for Together AI.
            repetition_penalty: Penalty for repeating tokens in generated text for Together AI.
            stop: List of strings to stop generation when encountered. Together AI.
            temperature: Temperature parameter for Together AI. Controls randomness of generated text.
            top_k: Top-k sampling parameter for Together AI. Controls diversity of generated text.
            top_p: Nucleus sampling parameter for Together AI.  Controls diversity of generated text.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_files(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of files stored in the system using the listFiles connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_jobs(
        self,
    ) -> Dict[str, Any]:
        """Lists all jobs currently being processed or completed within the system using the listJobs connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_models(
        self,
    ) -> Dict[str, Any]:
        """Lists all available models in the system through the listModels connector.
        Returns:
            API response as a dictionary.
        """
        ...

