"""Fastn Zamzar connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class ZamzarConnector:
    """Zamzar connector ().

    Provides 10 tools.
    """

    def convert_amazon_file_zamzar(
        self,
        source_file: str,
        target_format: str,
    ) -> Dict[str, Any]:
        """Converts a file stored in Amazon using the Zamzar online service, enabling users to transform video, audio, image, or eBook formats without requiring an account or downloads.

        Args:
            source_file: URL or path to the source file. (required)
            target_format: Desired format for the converted file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def convert_local_file(
        self,
        source_file: str,
        target_format: str,
    ) -> Dict[str, Any]:
        """Converts a local file into the specified format within the local environment.

        Args:
            source_file: URL or path to the source file. (required)
            target_format: Desired format for the converted file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def convert_url_file_zamzar(
        self,
        source_file: str,
        target_format: str,
    ) -> Dict[str, Any]:
        """Converts a file located at a URL through the Zamzar online converter, allowing for media transformation without the necessity of download or account creation.

        Args:
            source_file: URL or path to the source file to be converted. (required)
            target_format: The desired format for the converted file (e.g., 'pdf', 'docx'). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_file(
        self,
        content: str,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new file in the specified storage system with the provided content.

        Args:
            content: Content of the file to be converted (likely base64 encoded). (required)
            name: Original name of the file to be converted. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_file_zamzar(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific file from the Zamzar service, allowing users to manage their converted files online without the necessity of creating an account or downloading any software.

        Args:
            fileId: The unique identifier of the file on Zamzar. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_zamzar(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Fetches a specific file from the Zamzar platform, enabling users to access their converted video, audio, image, or eBook files online without any downloads or account requirements.

        Args:
            fileId: The ID of the file to be processed on Zamzar. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_files(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of files from the specified storage system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_import_file(
        self,
        importId: str,
    ) -> Dict[str, Any]:
        """Retrieves the status or details of a specific import file in the specified storage system.

        Args:
            importId: The unique identifier for the import operation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_import_files(
        self,
    ) -> Dict[str, Any]:
        """Gets a list of all import files in the specified storage system.
        Returns:
            API response as a dictionary.
        """
        ...

    def import_file(
        self,
        filename: str,
        url: str,
    ) -> Dict[str, Any]:
        """Imports a file into the specified storage system from an external source.

        Args:
            filename: Name of the file to be converted. (required)
            url: URL of the file to be converted. (required)
        Returns:
            API response as a dictionary.
        """
        ...

