"""Fastn HTTP API connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class HttpApiConnector:
    """HTTP API connector ().

    Provides 5 tools.
    """

    def http_api_delete(
        self,
        baseUrl: str,
        headers: List[Any],
        params: List[Any],
    ) -> Dict[str, Any]:
        """Sends an HTTP DELETE request to permanently remove a resource at a specified URL. Use this when you need to delete a resource entirely. This action is irreversible—the resource cannot be recovered after deletion. Do not use this if you only intend to update or deactivate a resource.

        Args:
            baseUrl:  (required)
            headers:  (required)
            params:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def http_api_get(
        self,
        baseUrl: str,
        headers: List[Any],
        params: List[Any],
    ) -> Dict[str, Any]:
        """Sends an HTTP GET request to retrieve data from a specified URL. Use this when you need to read or fetch information from an endpoint without modifying any data. For creating or modifying resources, use http_api_post, http_api_put, or http_api_patch instead. No data is modified by this call.

        Args:
            baseUrl:  (required)
            headers:  (required)
            params:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def http_api_patch(
        self,
        baseUrl: str,
        body: Dict[str, Any],
        headers: List[Any],
        params: List[Any],
    ) -> Dict[str, Any]:
        """Sends an HTTP PATCH request to partially update an existing resource at a specified URL. Use this when you need to modify only specific fields of a resource without replacing it entirely. For full replacement, use http_api_put instead. This call may modify server-side data.

        Args:
            baseUrl:  (required)
            body:  (required)
            headers:  (required)
            params:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def http_api_post(
        self,
        baseUrl: str,
        body: Dict[str, Any],
        headers: List[Any],
        params: List[Any],
    ) -> Dict[str, Any]:
        """Sends an HTTP POST request to create a new resource or submit data to a specified URL. Use this when creating a new record or triggering an action on the server. For updates, use http_api_put or http_api_patch instead. This call may create or modify server-side data.

        Args:
            baseUrl:  (required)
            body:  (required)
            headers:  (required)
            params:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def http_api_put(
        self,
        baseUrl: str,
        body: Dict[str, Any],
        headers: List[Any],
        params: List[Any],
    ) -> Dict[str, Any]:
        """Sends an HTTP PUT request to fully replace or create a resource at a specified URL. Use this when you need to overwrite an existing resource in its entirety. For partial updates, use http_api_patch instead. This call may modify or overwrite server-side data.

        Args:
            baseUrl:  (required)
            body:  (required)
            headers:  (required)
            params:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

