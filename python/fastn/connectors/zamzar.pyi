"""Fastn Zamzar connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ZamzarConnector:
    """Zamzar connector ().

    Provides 10 tools.
    """

    def convert_amazon_file(
        self,
        source_file: str,
        target_format: str,
    ) -> Dict[str, Any]:
        """Converts a file stored in Amazon S3 into the required format.

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

    def convert_url_file(
        self,
        source_file: str,
        target_format: str,
    ) -> Dict[str, Any]:
        """Converts a file located at a specified URL into the desired format.

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

    def delete_file(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Removes a file from the specified storage system.

        Args:
            fileId: The unique identifier of the file on Zamzar. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a single file from the specified storage system.

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

