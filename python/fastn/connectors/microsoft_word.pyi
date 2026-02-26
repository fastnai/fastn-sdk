"""Fastn Microsoft Word connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class MicrosoftWordConnector:
    """Microsoft Word connector ().

    Provides 11 tools.
    """

    def create_word_doc(
        self,
    ) -> Dict[str, Any]:
        """Creates a new Word document in the storage system utilizing the relevant connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_word_doc(
        self,
        fileName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing Word document from the storage system through the connector.

        Args:
            fileName: Name of the file to be processed by the MicroSoftWord API.
        Returns:
            API response as a dictionary.
        """
        ...

    def download_word_doc(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Downloads a Word document from the storage system using the specified connector.

        Args:
            fileName:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_doc(
        self,
        fileName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific Word document from the storage system using the connector.

        Args:
            fileName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_shared_docs(
        self,
    ) -> Dict[str, Any]:
        """Fetches the list of documents that are shared with you through the connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_word_docs(
        self,
        expand: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all Word documents available in the storage system using the relevant connector.

        Args:
            expand: 
            orderby: 
            select: 
            skipToken: 
            top: 
        Returns:
            API response as a dictionary.
        """
        ...

    def open_word_doc(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Opens an existing Word document in the storage system via the specified connector.

        Args:
            fileName: The name of the file to be processed by the MicroSoftWord API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def share_word_doc(
        self,
        recipients: Optional[List[Any]] = None,
        requireSignIn: Optional[bool] = None,
        roles: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Shares a Word document with selected users using the appropriate connector.

        Args:
            recipients: 
            requireSignIn: Indicates whether recipients need to sign in to access the document.
            roles: Array of roles associated with the document.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_existing_doc(
        self,
    ) -> Dict[str, Any]:
        """Updates an existing Word document in the storage system using the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_word_file(
        self,
    ) -> Dict[str, Any]:
        """Uploads a Word document to the specified storage system using the appropriate connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def user_onedrive_files(
        self,
    ) -> Dict[str, Any]:
        """Accesses the user's OneDrive files through the appropriate connector.
        Returns:
            API response as a dictionary.
        """
        ...

