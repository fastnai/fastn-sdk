"""Fastn LLama 2 connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class Llama2Connector:
    """LLama 2 connector ().

    Provides 2 tools.
    """

    def create_prediction(
        self,
    ) -> Dict[str, Any]:
        """Creates a new prediction using the Prediction Connector, allowing you to define parameters and model inputs for generating forecasts.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_prediction(
        self,
        predictionId: str,
    ) -> Dict[str, Any]:
        """Retrieves an existing prediction using the Prediction Connector, enabling you to access results and details based on a specified prediction ID.

        Args:
            predictionId: The ID of the prediction to retrieve from the LLama 2 API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

