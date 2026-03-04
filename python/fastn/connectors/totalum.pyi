"""Fastn Totalum connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _TotalumCreateUserAccess(TypedDict, total=False):
    customPages: Dict[str, Any]
    pages: Dict[str, Any]
    types: Dict[str, Any]

class _TotalumUpdateUserAccess(TypedDict, total=False):
    customPages: Dict[str, Any]
    pages: Dict[str, Any]
    types: Dict[str, Any]

class TotalumConnector:
    """Totalum connector ().

    Provides 10 tools.
    """

    def totalum_create_user(
        self,
        access: _TotalumCreateUserAccess,
        email: str,
        name: str,
        password: str,
        role: str,
    ) -> Dict[str, Any]:
        """Creates a new user account in Totalum with the provided profile information. Use this tool when you need to onboard a new user to the system. Do not use this to update an existing user — use the update user tool instead. This operation creates a persistent user record and may trigger onboarding notifications depending on system configuration.

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

    def totalum_delete_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing user from Totalum by user ID. Use this tool only when you need to fully remove a user account and all associated data. Do not use this to temporarily disable or update a user — use the update user tool instead. This action is irreversible and cannot be undone once executed.

        Args:
            userId: The ID of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def totalum_get_current_user(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the profile and account information of the currently authenticated user in Totalum. Use this tool when you need to identify who is logged in or inspect the active sessions user details. Do not use this to look up another user by ID — use the get user tool instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def totalum_get_file_download_url(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Generates a pre-signed or direct download URL for a specific file stored in Totalum, identified by file name. Use this tool when you need to provide a user or system with a link to download a file. Do not use this to retrieve file metadata or upload new files — use the dedicated tools for those. This is a read-only operation; the URL may expire after a set period.

        Args:
            fileName: Name of the file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def totalum_get_project_info(
        self,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific project in the project management system. Use this tool when you need to inspect project-level metadata and settings. Do not use this to retrieve individual user or file information — use the dedicated user or file tools instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def totalum_get_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Retrieves the profile and account information of a specific user in Totalum by user ID. Use this tool when you need to look up details for a known user. Do not use this to retrieve the currently authenticated user — use the get current user tool instead. This is a read-only operation with no side effects.

        Args:
            userId: The ID of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def totalum_ocr_image(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Performs Optical Character Recognition (OCR) on a provided image file and returns the extracted text content. Use this tool when you need to convert text within an image (e.g., JPEG, PNG) into machine-readable text for further processing or search. Do not use this for PDF files — use the PDF OCR tool instead. This operation does not modify or store the source image.

        Args:
            fileName: Name of the file to be processed by Totalum. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def totalum_ocr_pdf(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Performs Optical Character Recognition (OCR) on a provided PDF file and returns the extracted text content. Use this tool when you need to convert a scanned or image-based PDF into machine-readable text for further processing or search. Do not use this for image files — use the image OCR tool instead. This operation does not modify or store the source PDF.

        Args:
            fileName: Name of the file. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def totalum_update_user(
        self,
        email: str,
        name: str,
        password: str,
        role: str,
        userId: str,
        access: Optional[_TotalumUpdateUserAccess] = None,
    ) -> Dict[str, Any]:
        """Updates the profile or account information of an existing user in Totalum by user ID. Use this tool when you need to modify user attributes such as name, email, or role. Do not use this to create a new user — use the create user tool instead. This operation overwrites existing user data and cannot be automatically undone.

        Args:
            email: The user's email address. (required)
            name: The user's name. (required)
            password: The user's password. (required)
            role: The user's role. (required)
            userId: The ID of the user. (required)
            access: Specifies the user's access permissions.
        Returns:
            API response as a dictionary.
        """
        ...

    def totalum_upload_file(
        self,
        file: str,
        fileName: str,
    ) -> Dict[str, Any]:
        """Uploads a file to the Totalum file storage system. Use this tool when you need to store a new file for later retrieval, download, or OCR processing. Do not use this to update an existing file — delete and re-upload instead. This operation creates a new file record and may be irreversible without a separate delete action.

        Args:
            file: The file content to be processed by Totalum. (required)
            fileName: The name of the file being uploaded. (required)
        Returns:
            API response as a dictionary.
        """
        ...

