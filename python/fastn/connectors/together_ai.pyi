"""Fastn Together AI connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class TogetherAiConnector:
    """Together AI connector ().

    Provides 9 tools.
    """

    def together_ai_create_chat_completion(
        self,
        messages: List[Any],
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a structured conversation history to a Together AI chat model and returns a conversational response. Use this tool for multi-turn dialogue, instruction-following tasks, or any scenario where messages are formatted with roles (system, user, assistant). Do not use this for single-prompt text generation without a chat structure — use the completion tool instead. This tool sends data to an external model and may incur usage costs.

        Args:
            messages:  (required)
            model: Specifies the AI model to use for processing.
        Returns:
            API response as a dictionary.
        """
        ...

    def together_ai_create_completion(
        self,
        max_tokens: int,
        model: str,
        prompt: str,
        temperature: float,
    ) -> Dict[str, Any]:
        """Sends a text prompt to a Together AI language model and returns a text completion. Use this tool for single-turn, prompt-based text generation tasks such as summarization, classification, or content generation where a chat format is not required. Do not use this for multi-turn conversations — use the chat completion tool instead. This tool sends data to an external model and may incur usage costs.

        Args:
            max_tokens: Maximum number of tokens to generate in the Together AI response. (required)
            model: Specifies the model to use for the Together AI request. (required)
            prompt: The input prompt for the Together AI API. (required)
            temperature: Temperature parameter controlling the randomness of the Together AI response. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def together_ai_create_embedding(
        self,
        input: str,
        model: str,
    ) -> Dict[str, Any]:
        """Generates vector embeddings for one or more input texts using a Together AI embedding model. Use this tool when you need to convert text into numerical vector representations for semantic search, similarity comparison, clustering, or retrieval-augmented generation (RAG) pipelines. Do not use this for generating readable text responses — use the completion or chat tools instead. This tool sends data to an external model and may incur usage costs.

        Args:
            input: Input data for the Together AI API. (required)
            model: Specifies the model to use for processing the input in Together AI API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def together_ai_create_image(
        self,
        height: int,
        prompt: str,
        width: int,
        model: Optional[str] = None,
        n: Optional[int] = None,
        steps: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Generates one or more images from a text prompt using Together AIs image generation models. Use this tool when you need to produce AI-generated images based on a natural language description. Do not use this for text completions, chat responses, or embeddings. Returns image data or URLs. This tool sends requests to an external model and may incur usage costs.

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

    def together_ai_create_rerank_request(
        self,
        documents: Optional[List[Any]] = None,
        model: Optional[str] = None,
        query: Optional[str] = None,
        rank_fields: Optional[List[Any]] = None,
        return_documents: Optional[bool] = None,
        top_n: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Submits a reranking request to Together AI to reorder a list of documents by relevance to a given query. Use this tool when you have a set of candidate documents and need to rank them by semantic relevance before presenting results to a user or downstream process. Do not use this for initial retrieval or embedding generation. Returns a ranked list of documents. This tool sends data to an external API and may incur usage costs.

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

    def together_ai_list_files(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all files uploaded to Together AI, typically used for fine-tuning datasets. Use this tool when you need to audit available files, verify an upload succeeded, or find a file ID to reference in a fine-tuning job. Do not use this to download file contents — use a dedicated download tool for that. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def together_ai_list_jobs(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all fine-tuning jobs from Together AI, including their statuses (pending, running, completed, or failed). Use this tool when you need to monitor the progress of fine-tuning runs or audit previously submitted jobs. Do not use this to retrieve details about a single specific job — use a dedicated get-job tool if available. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def together_ai_list_models(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all AI models available on the Together AI platform, including their names, types, and capabilities. Use this tool when you need to discover which models are available before making inference, completion, or embedding requests. Do not use this to run a model — use the dedicated inference, completion, chat, or embedding tools for that. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def together_ai_run_inference(
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
        """Submits a raw inference request to the Together AI legacy inference endpoint and returns model predictions or outputs. Use this tool when you need to call the base inference API directly without specifying a versioned endpoint. Do not use this for chat completions, text completions, embeddings, or image generation — use the dedicated tools for those instead. This tool sends data to an external model and may incur usage costs.

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

