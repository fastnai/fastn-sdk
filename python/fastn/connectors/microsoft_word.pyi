"""Fastn Microsoft Word connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MicrosoftWordConnector:
    """Microsoft Word connector ().

    Provides 11 tools.
    """

    def microsoft_word_create_doc(
        self,
        body: str,
        fileName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Word document in the authenticated users OneDrive by uploading content to a specified file path via the Microsoft Graph API. Use this tool when you need to create a brand-new Word document that does not yet exist. Do not use this tool to update an existing document — use the update tool instead. Note: if a file with the same name already exists at the specified path, it may be overwritten.

        Args:
            body: Request body content for the MicroSoftWord API. (required)
            fileName: Name of the file in MicroSoftWord.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_word_delete_doc(
        self,
        fileName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific Word document from the authenticated users OneDrive by file name via the Microsoft Graph API. Use this tool only when you need to remove a Word document that is no longer needed. Do not use this tool if the intent is to update or archive the document — use the update or download tools instead. Warning: this operation is irreversible; the file will be moved to the recycle bin and may be permanently lost.

        Args:
            fileName: Name of the file to be processed by the MicroSoftWord API.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_word_download_doc(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Downloads the binary content of a specific Word document from the users OneDrive by file name via the Microsoft Graph API. Use this tool when you need to retrieve a Word documents file content for local use or processing. Do not use this tool if you only need file metadata such as size or modification date — use the get document metadata tool instead. This tool does not modify the document.

        Args:
            fileName:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_word_get_doc(
        self,
        fileName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the metadata and details (such as name, size, creation date, and modification date) of a specific Word document stored in the users OneDrive by file name via the Microsoft Graph API. Use this tool when you need information about a documents properties without downloading its content. Do not use this tool if you need the actual file content — use the download or open tools instead. This tool does not modify the document.

        Args:
            fileName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_word_list_docs(
        self,
        expand: Optional[str] = None,
        orderby: Optional[str] = None,
        select: Optional[str] = None,
        skipToken: Optional[str] = None,
        top: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all Word documents (.docx files) available in the authenticated users OneDrive by searching for files with the .docx extension via the Microsoft Graph API. Use this tool when you need to discover or enumerate all Word documents in the users OneDrive. Do not use this tool if you are looking for a specific known document by name — use the open or get tool instead. This tool does not modify any files.

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

    def microsoft_word_list_onedrive_files(
        self,
    ) -> Dict[str, Any]:
        """Lists all files and folders at the root of the authenticated users OneDrive account via the Microsoft Graph API. Use this tool when you need to browse or enumerate the users OneDrive root directory contents before selecting a specific file to open, download, or share. Do not use this tool if you already know the file name or path — use a targeted get or download tool instead. This tool does not modify any files.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_word_list_shared_docs(
        self,
    ) -> Dict[str, Any]:
        """Lists all documents and files that have been shared with the authenticated user in OneDrive via the Microsoft Graph API. Use this tool when you need to view or enumerate files that others have shared with the current user. Do not use this tool to list documents owned by the user — use the list OneDrive files or list Word documents tools instead. This tool does not modify any files.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_word_open_doc(
        self,
        fileName: str,
    ) -> Dict[str, Any]:
        """Retrieves the binary content of a specific Word document from the users OneDrive by file name, suitable for opening or reading the document via the Microsoft Graph API. Use this tool when you need to access the raw content of a known Word document for viewing or editing. Do not use this tool if you need file metadata only — use the get document metadata tool instead. This tool does not modify the document.

        Args:
            fileName: The name of the file to be processed by the MicroSoftWord API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_word_share_doc(
        self,
        fileId: str,
        recipients: Optional[List[Any]] = None,
        requireSignIn: Optional[bool] = None,
        roles: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Shares a Word document stored in the users OneDrive with one or more specified users by sending an invite via the Microsoft Graph API. Use this tool when you need to grant other users access to a specific Word document. Do not use this tool for listing existing shares or changing document content. Note: sharing permissions granted through this tool may need to be manually revoked if access needs to be removed later.

        Args:
            fileId: ID of the MicroSoftWord document. (required)
            recipients: 
            requireSignIn: Indicates whether recipients need to sign in to access the document.
            roles: Array of roles associated with the document.
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_word_update_doc(
        self,
        existingDocName: str,
        body: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Replaces the full binary content of an existing Word document (.docx) stored in the users OneDrive by uploading new content to the specified file path via the Microsoft Graph API. Use this tool when you need to overwrite an existing Word document with updated content. Do not use this tool to create a new document — use the create tool instead. Warning: this operation permanently overwrites the existing file content and cannot be automatically undone.

        Args:
            existingDocName:  (required)
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def microsoft_word_upload_doc(
        self,
        body: str,
        fileName: str,
    ) -> Dict[str, Any]:
        """Uploads a Word document file to the authenticated users OneDrive at a specified file path via the Microsoft Graph API. Use this tool when you need to transfer a locally available Word document to OneDrive storage. Do not use this tool to create a document from scratch without existing content — use the create tool instead. Note: if a file with the same name already exists at the target path, it may be overwritten.

        Args:
            body: The content of the Microsoft Word document. (required)
            fileName: Name of the file to be processed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

