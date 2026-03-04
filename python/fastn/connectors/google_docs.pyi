"""Fastn Google Docs connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _GoogleDocsCreateDocBody(TypedDict, total=False):
    content: List[Any]

class _GoogleDocsCreateDocDocumentstyle(TypedDict, total=False):
    background: Dict[str, Any]
    marginBottom: Dict[str, Any]
    marginLeft: Dict[str, Any]
    marginRight: Dict[str, Any]
    marginTop: Dict[str, Any]
    pageSize: Dict[str, Any]

class _GoogleDocsCreateDocNamedstyles(TypedDict, total=False):
    styles: List[Any]

class _GoogleDocsUpdateDocWritecontrol(TypedDict, total=False):
    requiredRevisionId: str

class GoogleDocsConnector:
    """Google Docs connector ().

    Provides 4 tools.
    """

    def google_docs_create_doc(
        self,
        title: str,
        Authorization: Optional[str] = None,
        body: Optional[_GoogleDocsCreateDocBody] = None,
        callback: Optional[str] = None,
        documentStyle: Optional[_GoogleDocsCreateDocDocumentstyle] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        namedStyles: Optional[_GoogleDocsCreateDocNamedstyles] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new blank Google Docs document and returns its document ID and metadata. Use this when you need to create a new document, optionally providing a title. Do not use this to modify an existing document; use google_docs_update_doc instead. The document is created immediately and will persist until manually deleted.

        Args:
            title:  (required)
            Authorization: 
            body: 
            callback: 
            documentStyle: 
            fields: 
            key: 
            namedStyles: 
            prettyPrint: 
            quotaUser: 
            uploadType: 
            upload_protocol: 
            xgafv: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_docs_get_doc(
        self,
        documentId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific document from Google Docs by its document ID, returning full content and metadata. Use this when you need to read the full content or metadata of a single document whose ID you already know. Do not use this to list or search for documents; use google_docs_list_docs instead.

        Args:
            documentId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_docs_list_docs(
        self,
        nextPageToken: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists documents accessible via Google Drive, optionally filtered by name, owner, or other Drive query parameters. Use this when you need to discover or search for documents without knowing their IDs. Do not use this to retrieve the full content of a specific document by ID; use google_docs_get_doc instead.

        Args:
            nextPageToken: 
            pageSize: 
        Returns:
            API response as a dictionary.
        """
        ...

    def google_docs_update_doc(
        self,
        docId: str,
        fields: Optional[str] = None,
        requests: Optional[List[Any]] = None,
        writeControl: Optional[_GoogleDocsUpdateDocWritecontrol] = None,
    ) -> Dict[str, Any]:
        """Applies a batch of structured update requests to an existing Google Docs document, supporting text edits, formatting changes, table insertions, and content reorganization. Use this when you need to modify the content or structure of an existing document identified by its document ID. Do not use this to create a new document; use google_docs_create_doc instead. Do not use this to read document content; use google_docs_get_doc instead. This operation modifies the document in place; changes are applied immediately and individual batch steps cannot be selectively undone.

        Args:
            docId:  (required)
            fields: 
            requests: 
            writeControl: 
        Returns:
            API response as a dictionary.
        """
        ...

