"""Fastn Splunk connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _SplunkSendEventFields(TypedDict, total=False):
    category: List[Any]
    severity: str

class SplunkConnector:
    """Splunk connector ().

    Provides 1 tools.
    """

    def splunk_send_event(
        self,
        event: Optional[str] = None,
        fields: Optional[_SplunkSendEventFields] = None,
        host: Optional[str] = None,
        sourcetype: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends a single event payload to the Splunk HTTP Event Collector (HEC) endpoint for ingestion into Splunk indexes. Use this tool when you need to log an activity, record a system event, or trigger Splunk-based alerts and dashboards with new data. Do NOT use this tool to query or retrieve existing Splunk data — it is write-only. Side effect: the event is indexed in Splunk and becomes visible in search results and dashboards according to your Splunk index configuration.

        Args:
            event: 
            fields: 
            host: 
            sourcetype: 
        Returns:
            API response as a dictionary.
        """
        ...

