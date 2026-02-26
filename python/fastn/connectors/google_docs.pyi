"""Fastn Google Docs connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GoogleDocsConnector:
    """Google Docs connector ().

    Provides 4 tools.
    """

    def create_doc(
        self,
        callback: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        uploadType: Optional[str] = None,
        upload_protocol: Optional[str] = None,
        xgafv: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new document in the specified document management system.

        Args:
            callback: 
            fields: 
            key: 
            prettyPrint: 
            quotaUser: 
            uploadType: 
            upload_protocol: 
            xgafv: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_doc(
        self,
        documentId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific document from the specified document management system.

        Args:
            documentId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_docs(
        self,
        nextPageToken: Optional[str] = None,
        pageSize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of documents from the specified document management system.

        Args:
            nextPageToken: 
            pageSize: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_doc(
        self,
        fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing document in the specified document management system.

        Args:
            fields: 
        Returns:
            API response as a dictionary.
        """
        ...

