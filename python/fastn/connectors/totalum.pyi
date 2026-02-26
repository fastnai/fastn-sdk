"""Fastn Totalum connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TotalumConnector:
    """Totalum connector ().

    Provides 10 tools.
    """

    def create_user(
        self,
        access: Dict[str, Any],
        email: str,
        name: str,
        password: str,
        role: str,
    ) -> Dict[str, Any]:
        """Creates a new user in the user management system.

        Args:
            access: Specifies the user's access permissions. (required)
            email: The user's email address. (required)
            name: The user's full name. (required)
            password: The user's password. (required)
            role: The user's role within the system. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing user from the user management system.

        Args:
            userId: The ID of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_current_user(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the current user's information from the user management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_download_url(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Generates a downloadable URL for a specified file in the file storage system.

        Args:
            fileName: Name of the file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_project_info(
        self,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific project in the project management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific user from the user management system.

        Args:
            userId: The ID of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ocr_of_image(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Performs Optical Character Recognition (OCR) on a provided image to extract text.

        Args:
            fileName: Name of the file to be processed by Totalum. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def ocr_of_pdf(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Performs Optical Character Recognition (OCR) on a provided PDF to extract text.

        Args:
            fileName: Name of the file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_user(
        self,
        email: str,
        name: str,
        password: str,
        role: str,
        access: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the information of an existing user in the user management system.

        Args:
            email: The user's email address. (required)
            name: The user's name. (required)
            password: The user's password. (required)
            role: The user's role. (required)
            access: Specifies the user's access permissions.
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_file(
        self,
        file: str,
        fileName: str,
    ) -> Dict[str, Any]:
        """Uploads a file to the file storage system.

        Args:
            file: The file content to be processed by Totalum. (required)
            fileName: The name of the file being uploaded. (required)
        Returns:
            API response as a dictionary.
        """
        ...

