"""Fastn Weather API connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class WeatherApiConnector:
    """Weather API connector ().

    Provides 1 tools.
    """

    def weather_api_get_current_weather(
        self,
        cityName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns the current weather conditions for a specified location using the WeatherAPI service. Use this tool when you need real-time weather data such as temperature, humidity, wind speed, and condition descriptions. Do not use this tool for historical weather data or multi-day forecasts. This operation is read-only and has no side effects.

        Args:
            cityName: 
        Returns:
            API response as a dictionary.
        """
        ...

