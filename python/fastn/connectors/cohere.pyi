"""Fastn Cohere connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class CohereConnector:
    """Cohere connector ().

    Provides 16 tools.
    """

    def cohere_chat(
        self,
        messages: List[Any],
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a message to Coheres chat model (v2 API) and returns a generated text response, supporting multi-turn conversations and optional connector-augmented retrieval (e.g., web search). Use this tool when you need to generate conversational replies, answer questions, or produce open-ended text. Do not use this tool for classification or embedding tasks.

        Args:
            messages:  (required)
            model: Name of the Cohere model to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_chat_v1(
        self,
        prompt: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a message to Coheres chat model using the v1 API endpoint and returns a generated text response. Use this tool when specifically targeting the v1 chat API for compatibility reasons. For most use cases, prefer cohere_chat which uses the newer v2 API. Do not use this tool for embedding generation — use cohere_embed instead.

        Args:
            prompt: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_classify(
        self,
        body: str,
    ) -> Dict[str, Any]:
        """Classifies one or more text inputs into predefined categories using Coheres classification model. Use this tool when you need to automatically assign labels to content, such as sentiment analysis, topic detection, or intent recognition. Requires example labels to be configured. Do not use this tool for open-ended text generation — use cohere_chat instead.

        Args:
            body: The request body for the Cohere API endpoint.  The exact format depends on the specific Cohere API call. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_delete_dataset(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified dataset from Cohere by its ID, freeing associated storage. Use this tool when a dataset is no longer needed. This action is irreversible — once deleted, the dataset and its contents cannot be recovered. Do not use this tool if you only want to inspect or update a dataset.

        Args:
            id: The ID for the requested resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_detokenize(
        self,
        model: str,
        tokens: List[Any],
    ) -> Dict[str, Any]:
        """Converts a sequence of token IDs back into human-readable text using Coheres detokenization endpoint. Use this tool when you have a tokenized representation and need to reconstruct the original string. Do not use this tool for splitting text into tokens — use cohere_tokenize instead.

        Args:
            model: Specifies the Cohere model to use. (required)
            tokens: An array of integer tokens representing the input text. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_embed(
        self,
        embedding_types: List[Any],
        images: List[Any],
        input_type: str,
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates vector embeddings for one or more text inputs using Coheres embedding model (v2 API). Use this tool when you need numerical representations of text for tasks such as semantic search, clustering, or similarity comparison. Do not use this tool for batch dataset embedding — use cohere_list_embed_jobs to manage async jobs instead.

        Args:
            embedding_types: Array of embedding types to use. (required)
            images: Array of image URLs to embed. (required)
            input_type: Type of input data. (required)
            model: Name of the Cohere model to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_get_connector(
        self,
    ) -> Dict[str, Any]:
        """Retrieves configuration and capability details for a specific Cohere connector (e.g., web-search) by its ID. Use this tool when you need to inspect a single connectors settings or verify its availability. Do not use this tool to browse all connectors — use cohere_list_connectors instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_get_dataset(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific Cohere dataset by its ID, including its attributes, schema, and status. Use this tool when you need to inspect a single dataset before using it for training or evaluation. Do not use this tool to list all datasets — use cohere_list_datasets instead.

        Args:
            id: Identifier for the resource.  Specific meaning depends on the Cohere endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_get_dataset_usage(
        self,
    ) -> Dict[str, Any]:
        """Retrieves aggregated usage statistics for datasets in your Cohere account, such as storage consumed. Use this tool when you need to monitor dataset storage utilization or plan capacity. Do not use this tool to retrieve metadata about a specific dataset — use cohere_get_dataset instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_get_model(
        self,
        XClientName: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed specifications for a single Cohere model, including its architecture, supported endpoints, and parameters. Use this tool when you need to inspect a specific model before using it in a task. Do not use this tool to browse all available models — use cohere_list_models instead.

        Args:
            XClientName: Client name for the Cohere API connection. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_list_connectors(
        self,
    ) -> Dict[str, Any]:
        """Lists all connectors configured in your Cohere account, such as web-search or custom data integrations. Use this tool when you need to discover which connectors are available for use in chat or retrieval tasks. Do not use this tool to retrieve details for a specific connector — use cohere_get_connector instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_list_datasets(
        self,
    ) -> Dict[str, Any]:
        """Lists all datasets available in your Cohere account, including their names, types, and statuses. Use this tool when you need an overview of datasets accessible for fine-tuning or evaluation. Do not use this tool to retrieve full details for a single dataset — use cohere_get_dataset instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_list_embed_jobs(
        self,
    ) -> Dict[str, Any]:
        """Lists all asynchronous embed jobs submitted to Cohere, including their statuses and associated dataset IDs. Use this tool to monitor the progress of batch embedding jobs or to retrieve job IDs for further inspection. Do not use this tool to create embeddings directly — use cohere_embed instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_list_models(
        self,
    ) -> Dict[str, Any]:
        """Lists all machine learning models available in your Cohere account. Use this tool when you need to discover which models are accessible for tasks such as text generation, embedding, or classification. Returns model names, types, and availability. Do not use this tool to retrieve detailed specifications for a single model — use cohere_get_model instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_rerank(
        self,
        documents: List[Any],
        model: str,
        query: str,
        top_n: int,
    ) -> Dict[str, Any]:
        """Reranks a list of candidate documents or passages by their relevance to a given query using Coheres reranking model (v2 API). Use this tool to improve the ordering of search results or retrieved documents before presenting them to a user. Do not use this tool for generating embeddings or classifying text.

        Args:
            documents: An array of documents to be processed. (required)
            model: The name of the Cohere model to use. (required)
            query: The search query. (required)
            top_n: The number of top results to return. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere_tokenize(
        self,
        model: str,
        text: str,
    ) -> Dict[str, Any]:
        """Splits input text into token IDs using Coheres tokenization endpoint, which is useful for measuring token counts or preparing input for downstream NLP processing. Use this tool when you need to understand how a model will segment a given string. Do not use this tool to reconstruct text from tokens — use cohere_detokenize instead.

        Args:
            model: The name of the Cohere model to use. (required)
            text: The input text to process. (required)
        Returns:
            API response as a dictionary.
        """
        ...

