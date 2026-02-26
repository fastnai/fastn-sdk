"""Fastn Cohere connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class CohereConnector:
    """Cohere connector ().

    Provides 16 tools.
    """

    def chat(
        self,
        messages: List[Any],
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Interacts with the Chat connector to facilitate text-based conversations, enabling a chatbot experience with users.

        Args:
            messages:  (required)
            model: Name of the Cohere model to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def classify(
        self,
    ) -> Dict[str, Any]:
        """Categorizes text inputs using the Classify connector, helping to automatically assign labels or categories to various pieces of content.
        Returns:
            API response as a dictionary.
        """
        ...

    def cohere(
        self,
    ) -> Dict[str, Any]:
        """Generates text embeddings using the Cohere connector, suitable for natural language understanding tasks.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_dataset(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Removes a specified dataset from the system with the deleteDataset connector, ensuring it no longer occupies storage or is accessible.

        Args:
            id: The ID for the requested resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def detokenize(
        self,
        model: str,
        tokens: List[Any],
    ) -> Dict[str, Any]:
        """Merges tokens back into text with the detokenize connector, facilitating conversion from tokenized form to human-readable text.

        Args:
            model: Specifies the Cohere model to use. (required)
            tokens: An array of integer tokens representing the input text. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def embed(
        self,
        embedding_types: List[Any],
        images: List[Any],
        input_type: str,
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uses the Embed connector to create vector representations of text or other data types for machine learning applications.

        Args:
            embedding_types: Array of embedding types to use. (required)
            images: Array of image URLs to embed. (required)
            input_type: Type of input data. (required)
            model: Name of the Cohere model to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connector(
        self,
    ) -> Dict[str, Any]:
        """Fetches information about a specific connector through the getConnector connector, providing details about its capabilities and usage.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_connectors(
        self,
    ) -> Dict[str, Any]:
        """Lists all available connectors using the getConnectors connector, giving users insight into which integrations are possible.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_dataset(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Obtains detailed information about a particular dataset using the getDataset connector, including its attributes and content.

        Args:
            id: Identifier for the resource.  Specific meaning depends on the Cohere endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_dataset_usage(
        self,
    ) -> Dict[str, Any]:
        """Fetches the usage details of a specific dataset through the getDatasetUsage connector, revealing insights on how the dataset is utilized.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_datasets(
        self,
    ) -> Dict[str, Any]:
        """Retrieves available datasets using the getDatasets connector, providing an overview of datasets accessible for training and evaluation.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_model(
        self,
        XClientName: str,
    ) -> Dict[str, Any]:
        """Retrieves the specifications of a particular model using the getModel connector, allowing users to understand its architecture and parameters.

        Args:
            XClientName: Client name for the Cohere API connection. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_models(
        self,
    ) -> Dict[str, Any]:
        """Lists all available models with the getModels connector, enabling users to explore different machine learning models accessible for various tasks.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_embed_jobs(
        self,
    ) -> Dict[str, Any]:
        """Lists all embed jobs processed under the Embed connector, allowing users to manage and monitor job statuses.
        Returns:
            API response as a dictionary.
        """
        ...

    def rerank(
        self,
        documents: List[Any],
        model: str,
        query: str,
        top_n: int,
    ) -> Dict[str, Any]:
        """Utilizes the Rerank connector to reorder a list of items based on relevance to user queries, improving search result accuracy.

        Args:
            documents: An array of documents to be processed. (required)
            model: The name of the Cohere model to use. (required)
            query: The search query. (required)
            top_n: The number of top results to return. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tokenize(
        self,
        model: str,
        text: str,
    ) -> Dict[str, Any]:
        """Splits input text into tokens using the tokenize connector, enabling further processing in NLP applications.

        Args:
            model: The name of the Cohere model to use. (required)
            text: The input text to process. (required)
        Returns:
            API response as a dictionary.
        """
        ...

