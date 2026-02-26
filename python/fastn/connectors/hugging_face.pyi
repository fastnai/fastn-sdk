"""Fastn Hugging Face connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class HuggingFaceConnector:
    """Hugging Face connector ().

    Provides 3 tools.
    """

    def hugging_face(
        self,
        inputs: str,
    ) -> Dict[str, Any]:
        """Utilizes the huggingFace connector to access a variety of natural language processing models for tasks such as text classification, translation, and generation.

        Args:
            inputs:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sentiment_analysis(
        self,
        inputs: str,
    ) -> Dict[str, Any]:
        """Analyzes the sentiment of a given text using the sentimentAnalysis connector to determine if the tone is positive, negative, or neutral.

        Args:
            inputs:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def summarization(
        self,
        inputs: str,
    ) -> Dict[str, Any]:
        """Generates a concise summary of a given text using the summarization connector to distill the main points and key information.

        Args:
            inputs:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

