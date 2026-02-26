"""Fastn Fastn Unified APIs connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FastnUnifiedApisConnector:
    """Fastn Unified APIs connector ().

    Provides 1 tools.
    """

    def universal_command_layer(
        self,
        projectId: Optional[str] = None,
        stage: Optional[str] = None,
        x_fastn_api_key: Optional[str] = None,
        x_fastn_space_tenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """The Universal Command Layer executes versatile commands across multiple systems, enabling seamless integration and automation of actions without being limited to a single connector.

        Args:
            projectId: 
            stage: 
            x_fastn_api_key: 
            x_fastn_space_tenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

