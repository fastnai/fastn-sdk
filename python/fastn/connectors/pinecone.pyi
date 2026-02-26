"""Fastn Pinecone connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class PineconeConnector:
    """Pinecone connector ().

    Provides 35 tools.
    """

    def cancel_import(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Cancels an ongoing import process in the database connector.

        Args:
            XPineconeAPIVersion: The Pinecone API version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def chat_prompt(
        self,
        messages: List[Any],
        model: str,
        stream: bool,
    ) -> Dict[str, Any]:
        """Sends a chat prompt for responses in the assistant connector.

        Args:
            messages:  (required)
            model: Specifies the Pinecone model to use. (required)
            stream: Indicates whether to stream the response. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def check_assistant_status(
        self,
        assistantName: str,
    ) -> Dict[str, Any]:
        """Checks and retrieves the status of a specific assistant in the assistant connector.

        Args:
            assistantName: Name of the assistant for the Pinecone API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_assistant(
        self,
        instructions: str,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new assistant in the assistant connector.

        Args:
            instructions: Instructions for the Pinecone operation. (required)
            name: Name for the Pinecone operation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_collection(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Creates a new collection in the database connector.

        Args:
            XPineconeAPIVersion: The Pinecone API version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_index(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Creates a new index in the database connector.

        Args:
            XPineconeAPIVersion: The version of the Pinecone API being used. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_assistant(
        self,
        NameAssistant: str,
    ) -> Dict[str, Any]:
        """Deletes a specific assistant from the assistant connector.

        Args:
            NameAssistant: Name of the assistant  in the Pinecone API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_collection(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Deletes an existing collection from the database connector.

        Args:
            XPineconeAPIVersion: The Pinecone API version to use. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_file_from_assistant(
        self,
        assistantName: str,
        fileId: str,
    ) -> Dict[str, Any]:
        """Deletes a file from the assistant connector.

        Args:
            assistantName: Name of the assistant. (required)
            fileId: Identifier of the file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_index(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Deletes an existing index from the database connector.

        Args:
            XPineconeAPIVersion: The Pinecone API version to use. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_vectors(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Deletes specific vectors from the database connector.

        Args:
            XPineconeAPIVersion: Specifies the version of the Pinecone API to use. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def edit_index(
        self,
    ) -> Dict[str, Any]:
        """Modifies the properties of an existing index in the database connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def embed_data(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Embeds data into the database connector for further usage.

        Args:
            XPineconeAPIVersion: Specifies the version of the Pinecone API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def evaluate_answer(
        self,
        answer: str,
        ground_truth_answer: str,
        question: str,
    ) -> Dict[str, Any]:
        """Evaluates the provided answer against expected criteria in the assistant connector.

        Args:
            answer: The provided answer to the question. (required)
            ground_truth_answer: The correct answer to the question. (required)
            question: The question to be processed by the Pinecone API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_assistant_context_(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Retrieves the context associated with a specific assistant in the assistant connector.

        Args:
            query: The search query to be executed on Pinecone. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_assistants(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of available assistants in the assistant connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_collection_description(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Retrieves the description and specifications of a specific collection in the database connector.

        Args:
            XPineconeAPIVersion: Specifies the version of the Pinecone API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_collections(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Retrieves all collections available in the database connector.

        Args:
            XPineconeAPIVersion: Specifies the version of the Pinecone API being used. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_description(
        self,
        assistantName: str,
        fileId: str,
    ) -> Dict[str, Any]:
        """Fetches a detailed description of a specific file in the assistant connector.

        Args:
            assistantName: Name of the Pinecone assistant. (required)
            fileId: ID of the file to process in the Pinecone API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_files(
        self,
        assistantName: str,
    ) -> Dict[str, Any]:
        """Retrieves all files associated with the assistant connector.

        Args:
            assistantName: Name of the assistant for the Pinecone API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_import_description(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Fetches a detailed description of a specific import in the database connector.

        Args:
            XPineconeAPIVersion: The Pinecone API version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_imports(
        self,
        paginationToken: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the status and details of all ongoing imports in the database connector.

        Args:
            paginationToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_index_description(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Retrieves the description and specifications of a specific index in the database connector.

        Args:
            XPineconeAPIVersion: Pinecone API version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_index_stats(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Retrieves statistics regarding the performance and usage of an index in the database connector.

        Args:
            XPineconeAPIVersion: Pinecone API version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_indexes(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all index definitions from the database connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_vector_ids(
        self,
        namespace: Optional[str] = None,
        prefix: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the IDs of vectors stored in the database connector.

        Args:
            namespace: Namespace for the Pinecone index.
            prefix: Prefix for the Pinecone index.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_vectors(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Fetches existing vectors from the database connector.

        Args:
            XPineconeAPIVersion: The version of the Pinecone API being used. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def open_ai_compatible_chat(
        self,
        messages: List[Any],
    ) -> Dict[str, Any]:
        """Facilitates compatible chat interactions using OpenAI technology in the assistant connector.

        Args:
            messages:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def query_vectors(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Queries and retrieves vectors based on specific criteria from the database connector.

        Args:
            XPineconeAPIVersion: The version of the Pinecone API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rerank_documents(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Re-evaluates and ranks documents based on specified criteria in the database connector.

        Args:
            XPineconeAPIVersion: Specifies the version of the Pinecone API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def start_import(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Starts an import process for data in the database connector.

        Args:
            XPineconeAPIVersion: Specify the Pinecone API version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_assistant(
        self,
        instructions: str,
    ) -> Dict[str, Any]:
        """Updates the properties of an existing assistant in the assistant connector.

        Args:
            instructions: Instructions for the Pinecone API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_vector(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Updates a specific vector in the database connector.

        Args:
            XPineconeAPIVersion: The version of the Pinecone API being used. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_file_to_assistant(
        self,
        file: str,
    ) -> Dict[str, Any]:
        """Uploads a file to a specific assistant in the assistant connector.

        Args:
            file: File data for the Pinecone API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def upsert_vectors(
        self,
        XPineconeAPIVersion: str,
    ) -> Dict[str, Any]:
        """Inserts or updates vectors in the database connector, ensuring either creation or modification as necessary.

        Args:
            XPineconeAPIVersion: Specify the Pinecone API version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

