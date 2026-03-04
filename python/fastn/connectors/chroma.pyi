"""Fastn Chroma connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class ChromaConnector:
    """Chroma connector ().

    Provides 4 tools.
    """

    def chroma_list_collections(
        self,
        databaseName: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all collections within a specified Chroma database. Use this tool when you need to enumerate available collections before querying, inserting, or managing records within them. Do not use this tool to retrieve records or databases — use chroma_list_records or chroma_list_databases respectively. This tool is read-only and has no side effects.

        Args:
            databaseName: 
            limit: 
            offset: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def chroma_list_databases(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all databases available within a specified Chroma tenant. Use this tool when you need to discover or enumerate databases before interacting with their collections or records. Do not use this tool to retrieve collections or records — use chroma_list_collections for that. This tool is read-only and has no side effects.

        Args:
            limit: 
            offset: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def chroma_list_records(
        self,
        collectionId: Optional[str] = None,
        databaseName: Optional[str] = None,
        ids: Optional[List[Any]] = None,
        include: Optional[List[Any]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        tenantId: Optional[str] = None,
        where: Optional[str] = None,
        where_document: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves records from a specific Chroma collection by applying filter conditions or ID-based lookups. Use this tool when you need to fetch stored embedding records and their associated metadata from a known collection without performing a vector similarity search. Do not use this tool for semantic or nearest-neighbor searches — use chroma_query_records for that instead. This tool does not modify any data.

        Args:
            collectionId: 
            databaseName: 
            ids: 
            include: 
            limit: 
            offset: 
            tenantId: 
            where: 
            where_document: 
        Returns:
            API response as a dictionary.
        """
        ...

    def chroma_upsert_records(
        self,
        collectionId: Optional[str] = None,
        databaseName: Optional[str] = None,
        documents: Optional[List[Any]] = None,
        embeddings: Optional[List[Any]] = None,
        ids: Optional[List[Any]] = None,
        tenantId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Inserts new embedding records or updates existing ones in a specific Chroma collection. If a record with the given ID already exists, it will be overwritten; otherwise, a new record is created. Use this tool when you need to add or refresh embeddings, documents, or metadata in a collection. Do not use this tool if you only want to read or query records. This operation modifies the collection and cannot be undone — overwritten records cannot be recovered.

        Args:
            collectionId: 
            databaseName: 
            documents: 
            embeddings: 
            ids: 
            tenantId: 
        Returns:
            API response as a dictionary.
        """
        ...

