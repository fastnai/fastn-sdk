"""Fastn Redis connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class RedisConnector:
    """Redis connector ().

    Provides 3 tools.
    """

    def redis_delete_key(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Permanently removes a key and its associated value from the Redis store. Use this tool when you need to evict a cached entry or clean up a specific key. This action is immediate and cannot be undone. Do not use this tool to retrieve or overwrite a key — use redis_get_key or redis_set_key instead.

        Args:
            id: Unique identifier for the Redis operation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def redis_get_key(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieves the value associated with a specific key from the Redis store. Use this tool when you need to read a cached or stored value by its key. Returns null or an empty result if the key does not exist. Do not use this tool to set or delete a key — use redis_set_key or redis_delete_key instead.

        Args:
            id: Unique identifier for the Redis operation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def redis_set_key(
        self,
        body: Dict[str, Any],
        id: str,
        expired_in_seconds: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sets a key-value pair in the Redis store, creating the key if it does not exist or overwriting its value if it does. Use this tool when you need to store or cache a value under a specific key in Redis. Do not use this tool to retrieve a value — use redis_get_key instead. Note: if the key already exists, its value will be overwritten.

        Args:
            body: Request body for the Redis API. (required)
            id: Unique identifier for the Redis request. (required)
            expired_in_seconds: Token expiration time in seconds.
        Returns:
            API response as a dictionary.
        """
        ...

