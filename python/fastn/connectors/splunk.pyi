"""Fastn Splunk connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SplunkConnector:
    """Splunk connector ().

    Provides 1 tools.
    """

    def send_event(
        self,
        event: Optional[str] = None,
        fields: Optional[Dict[str, Any]] = None,
        host: Optional[str] = None,
        sourcetype: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends an event to the specified endpoint in the application context. This operation allows you to trigger specific behaviors or log activities related to the event within the given environment.

        Args:
            event: 
            fields: 
            host: 
            sourcetype: 
        Returns:
            API response as a dictionary.
        """
        ...

