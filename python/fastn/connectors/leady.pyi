"""Fastn Leady connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class LeadyConnector:
    """Leady connector ().

    Provides 1 tools.
    """

    def remove_tool_from_kroger(
        self,
        country: Optional[str] = None,
    ) -> Dict[str, Any]:
        """REMOVE_TOOL_FROM_KROGER

        Args:
            country: Country filter for the Leady API Leady Endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

