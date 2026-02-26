"""Fastn Splunk APM connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SplunkApmConnector:
    """Splunk APM connector ().

    Provides 3 tools.
    """

    def create_trace(
        self,
    ) -> Dict[str, Any]:
        """Creates a new trace entry in the tracing system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_incidents(
        self,
        includeResolved: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches incident reports from the incidents management system.

        Args:
            includeResolved: 
            limit: 
            offset: 
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_trace(
        self,
        traceId: str,
    ) -> Dict[str, Any]:
        """Retrieves trace information from the tracing system.

        Args:
            traceId: Trace ID for identifying the specific trace in Splunk APM. (required)
        Returns:
            API response as a dictionary.
        """
        ...

