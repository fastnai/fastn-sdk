"""Fastn Chroma connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ChromaConnector:
    """Chroma connector ().

    Provides 4 tools.
    """

    def get_collections(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all collections from the specified database using the relevant connector.

        Args:
            limit: 
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_databases(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all available databases using the designated connector, providing a list of databases within the system.

        Args:
            limit: 
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def search_records(
        self,
        ids: Optional[List[Any]] = None,
        include: Optional[List[Any]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        where: Optional[str] = None,
        where_document: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for specific records within the database using the specified connector, allowing for refined data retrieval based on search parameters.

        Args:
            ids: 
            include: 
            limit: 
            offset: 
            where: 
            where_document: 
        Returns:
            API response as a dictionary.
        """
        ...

    def upsert_records(
        self,
        documents: Optional[List[Any]] = None,
        embeddings: Optional[List[Any]] = None,
        ids: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Inserts new records or updates existing records in the system using the appropriate connector to ensure data integrity.

        Args:
            documents: 
            embeddings: 
            ids: 
        Returns:
            API response as a dictionary.
        """
        ...

