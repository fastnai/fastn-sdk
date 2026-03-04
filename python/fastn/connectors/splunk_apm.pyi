"""Fastn Splunk APM connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class SplunkApmConnector:
    """Splunk APM connector ().

    Provides 3 tools.
    """

    def splunk_apm_create_trace(
        self,
        body: List[Any],
    ) -> Dict[str, Any]:
        """Creates and submits a new trace entry to Splunk APM using the SignalFx v1 trace ingestion format. Use this tool when you need to instrument a transaction or send custom trace data to Splunk APM for performance tracking across microservices and distributed systems. Do NOT use this tool to retrieve existing trace data — use splunk_apm_get_trace instead. Side effect: the submitted trace is ingested into Splunk APM and will appear in trace analysis and performance dashboards.

        Args:
            body:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def splunk_apm_get_trace(
        self,
        traceId: str,
    ) -> Dict[str, Any]:
        """Retrieves the latest snapshot of a specific trace from Splunk APM by its trace ID, including span-level details about the transaction flow and performance metrics across microservices. Use this tool when you need to inspect the execution path and timing of a known transaction. Do NOT use this tool to list all incidents or create new traces — use splunk_apm_list_incidents or splunk_apm_create_trace respectively. This tool is read-only and has no side effects.

        Args:
            traceId: Trace ID for identifying the specific trace in Splunk APM. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def splunk_apm_list_incidents(
        self,
        includeResolved: Optional[str] = None,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of active and historical incidents from Splunk APM, including details about performance degradations and reliability issues affecting your microservices and distributed systems. Use this tool when you need to review, triage, or report on incidents across your monitored services. Do NOT use this tool to retrieve individual trace data — use splunk_apm_get_trace instead. This tool is read-only and has no side effects.

        Args:
            includeResolved: 
            limit: 
            offset: 
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

