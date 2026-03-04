"""Fastn LLama 2 connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class Llama2Connector:
    """LLama 2 connector ().

    Provides 2 tools.
    """

    def llama2_create_prediction(
        self,
        prompt: str,
    ) -> Dict[str, Any]:
        """Submits a new inference request to the LLama 2 model on Replicate by defining model inputs and parameters. Use this when you need to generate a language model response or forecast. This action creates a new prediction record; results may not be immediately available and may need to be polled using llama2_get_prediction. Note: despite the GET method in the endpoint, this action initiates a new prediction.

        Args:
            prompt: The prompt to be sent to the LLama 2 model. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def llama2_get_prediction(
        self,
        predictionId: str,
    ) -> Dict[str, Any]:
        """Retrieves the status and results of an existing LLama 2 prediction on Replicate, identified by its prediction ID. Use this when you need to check whether a previously submitted prediction has completed and to retrieve its output. Do not use this to create a new prediction — use llama2_create_prediction instead.

        Args:
            predictionId: The ID of the prediction to retrieve from the LLama 2 API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

