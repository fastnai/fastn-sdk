"""Fastn Weather API connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class WeatherApiConnector:
    """Weather API connector ().

    Provides 1 tools.
    """

    def get_current_weather(
        self,
        cityName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the current weather information from the designated weather service.

        Args:
            cityName: 
        Returns:
            API response as a dictionary.
        """
        ...

