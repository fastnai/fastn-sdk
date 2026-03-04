"""Fastn Hugging Face connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class HuggingFaceConnector:
    """Hugging Face connector ().

    Provides 3 tools.
    """

    def hugging_face_analyze_sentiment(
        self,
        inputs: str,
    ) -> Dict[str, Any]:
        """Analyzes the sentiment of a provided text using the Cardiff NLP Twitter-RoBERTa model on Hugging Face, returning a classification of positive, negative, or neutral. Use this when you need to determine the emotional tone of text such as reviews, messages, or social media content. Not suitable for text generation or summarization — use hugging_face_generate_text or hugging_face_summarize_text for those tasks. Each call sends input to an external API.

        Args:
            inputs:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hugging_face_generate_text(
        self,
        inputs: str,
    ) -> Dict[str, Any]:
        """Generates text using the Mistral-7B-Instruct model hosted on Hugging Face Inference API. Use this for instruction-following tasks such as question answering, text generation, and conversational responses. Not optimized for summarization or sentiment analysis — use hugging_face_summarize_text or hugging_face_analyze_sentiment for those tasks. Each call sends input to an external API.

        Args:
            inputs:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hugging_face_summarize_text(
        self,
        inputs: str,
    ) -> Dict[str, Any]:
        """Generates a concise summary of a provided text using the Facebook BART-large-CNN model on Hugging Face. Use this when you need to distill a long document or passage into its key points. Not suitable for sentiment analysis or text generation — use hugging_face_analyze_sentiment or hugging_face_generate_text for those tasks. Each call sends input to an external API.

        Args:
            inputs:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

