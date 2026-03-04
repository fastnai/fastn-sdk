"""Fastn Fastn Unified APIs connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class FastnUnifiedApisConnector:
    """Fastn Unified APIs connector ().

    Provides 1 tools.
    """

    def fastn_execute_universal_command(
        self,
        flowName: Optional[str] = None,
        input: Optional[Dict[str, Any]] = None,
        projectId: Optional[str] = None,
        stage: Optional[str] = None,
        x_fastn_api_key: Optional[str] = None,
        x_fastn_space_tenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a named command flow across any service integrated with Fastns Universal Command Layer (UCL). Use this tool when you need to trigger a cross-system automation or action that is not covered by a dedicated connector tool. The flow to execute is specified by the flow name in the request path. This tool routes the request to the appropriate underlying service via Fastn and may perform writes, updates, or deletions depending on the flow definition — review the flows side effects before calling it. Do not use this tool when a dedicated, service-specific tool already exists for the intended action.

        Args:
            flowName: 
            input: 
            projectId: 
            stage: 
            x_fastn_api_key: 
            x_fastn_space_tenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

