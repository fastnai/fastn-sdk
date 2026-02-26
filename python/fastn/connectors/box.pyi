"""Fastn Box connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BoxConnector:
    """Box connector ().

    Provides 10 tools.
    """

    def create_folder(
        self,
        name: str,
        parent: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new folder in the connected service, allowing for better organization of files and data.

        Args:
            name: Name of the new item. (required)
            parent: Parent folder information.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_file(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified file from the connected service, permanently removing it from storage.

        Args:
            fileId: The ID of the file in Box. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_account_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves account information from the connected service, allowing you to view details such as account status and settings.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific file from the connected service, providing information such as file size, type, and content.

        Args:
            fileId: The ID of the file to access on Box. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_metadata(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Fetches metadata for a specific file in the connected service, including information such as creation date, modification date, and file type.

        Args:
            fileId: The ID of the file in Box. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_folder(
        self,
        folderId: str,
    ) -> Dict[str, Any]:
        """Fetches details about a specified folder in the connected service, including its contents and properties.

        Args:
            folderId: ID of the folder to access on Box. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def move_file_to_folder(
        self,
        parent: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Moves a file from its current location to a specified folder within the connected service, enabling better file management.

        Args:
            parent: Parent folder details for the Box API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def rename_file(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Renames a specified file in the connected service, allowing for more descriptive or organized naming conventions.

        Args:
            name: Name of the file or folder in Box. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def search(
        self,
        query: str,
    ) -> Dict[str, Any]:
        """Searches for specific files, folders, or data within the connected service based on provided search criteria.

        Args:
            query: Query string parameters for the Box API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def share_file(
        self,
        shared_link: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Shares a specified file with designated users or groups within the connected service, facilitating collaboration.

        Args:
            shared_link: Settings for the shared link. (required)
        Returns:
            API response as a dictionary.
        """
        ...

