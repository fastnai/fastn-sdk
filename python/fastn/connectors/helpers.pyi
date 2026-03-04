"""Fastn Helpers connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class HelpersConnector:
    """Helpers connector ().

    Provides 2 tools.
    """

    def helpers_list_time_zones(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all available IANA time zones. Use this tool when you need to present time zone options to a user, validate a time zone value, or resolve a local time to UTC in a workflow. Do not use this tool to get times-of-day categories — use helpers_list_times_of_day instead. This tool is read-only and has no side effects.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

    def helpers_list_times_of_day(
        self,
        interval: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Returns the standard times-of-day categories (morning, afternoon, evening, night) as a list. Use this tool when you need to present time-of-day options to a user, categorize activities by time of day, or populate a time-of-day selector in a workflow. Do not use this tool to retrieve time zones — use helpers_list_time_zones instead. This tool is read-only and has no side effects.

        Args:
            interval: 
        Returns:
            API response as a dictionary.
        """
        ...

