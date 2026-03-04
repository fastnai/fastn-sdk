"""Fastn Firebase Realtime Database connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class FirebaseRealtimeDatabaseConnector:
    """Firebase Realtime Database connector ().

    Provides 3 tools.
    """

    def firebase_realtime_database_add_records(
        self,
        body: Dict[str, Any],
        projectId: Optional[str] = None,
        tableName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds one or more new records to a specified path (table/node) in the Firebase Realtime Database by posting data and generating a new unique key. Use this tool when you need to insert new entries without overwriting existing data. Do not use this tool to update existing records — use a dedicated update operation if available.

        Args:
            body:  (required)
            projectId: 
            tableName: 
        Returns:
            API response as a dictionary.
        """
        ...

    def firebase_realtime_database_get_auth_token(
        self,
        email: Optional[str] = None,
        key: Optional[str] = None,
        password: Optional[str] = None,
        returnSecureToken: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Authenticates a user with Firebase using email and password credentials via the Firebase Identity Toolkit, and returns a secure ID token for use in subsequent authenticated requests. Use this tool to obtain an access token before calling other Firebase Realtime Database operations that require authentication. Do not use this tool to read or write database records.

        Args:
            email: 
            key: 
            password: 
            returnSecureToken: 
        Returns:
            API response as a dictionary.
        """
        ...

    def firebase_realtime_database_list_records(
        self,
        limitToFirst: Optional[str] = None,
        orderBy: Optional[str] = None,
        projectId: Optional[str] = None,
        startAt: Optional[str] = None,
        tableName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all records stored at a specified path (table/node) in the Firebase Realtime Database. Use this tool when you need to read existing data for analysis, display, or further processing. Do not use this tool to write or modify data — use firebase_realtime_database_add_records instead.

        Args:
            limitToFirst: 
            orderBy: 
            projectId: 
            startAt: 
            tableName: 
        Returns:
            API response as a dictionary.
        """
        ...

