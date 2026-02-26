"""Fastn Kafka connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class KafkaConnector:
    """Kafka connector ().

    Provides 2 tools.
    """

    def consumer(
        self,
        group_id: Optional[str] = None,
        max_messages: Optional[int] = None,
        offset: Optional[int] = None,
        partition: Optional[str] = None,
        topic_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Facilitates the consumption of data from various sources in the context of data integration and processing.

        Args:
            group_id: 
            max_messages: 
            offset: 
            partition: 
            topic_name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def producer(
        self,
        message: str,
        topic_name: str,
    ) -> Dict[str, Any]:
        """Enables the production and publication of data to different targets within data pipelines, allowing seamless information flow.

        Args:
            message: The message to be sent to the Kafka topic. (required)
            topic_name: Name of the Kafka topic to send the message to. (required)
        Returns:
            API response as a dictionary.
        """
        ...

