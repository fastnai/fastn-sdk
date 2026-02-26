"""Fastn Firebase Realtime Database connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FirebaseRealtimeDatabaseConnector:
    """Firebase Realtime Database connector ().

    Provides 3 tools.
    """

    def add_records(
        self,
    ) -> Dict[str, Any]:
        """Adds new records to the designated connector, allowing the user to store and manage data effectively within the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_records(
        self,
        limitToFirst: Optional[str] = None,
        orderBy: Optional[str] = None,
        startAt: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches existing records from the specified connector, providing access to stored data for analysis or further processing.

        Args:
            limitToFirst: 
            orderBy: 
            startAt: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_token(
        self,
        key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves an authentication token from the specified connector, enabling secure access to its APIs and functionalities for further operations.

        Args:
            key: 
        Returns:
            API response as a dictionary.
        """
        ...

