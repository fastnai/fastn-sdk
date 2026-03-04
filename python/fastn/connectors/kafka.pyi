"""Fastn Kafka connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class KafkaConnector:
    """Kafka connector ().

    Provides 2 tools.
    """

    def kafka_consume_messages(
        self,
        group_id: Optional[str] = None,
        max_messages: Optional[int] = None,
        offset: Optional[int] = None,
        partition: Optional[str] = None,
        topic_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Reads and retrieves one or more messages from a specified Kafka topic or partition. Use this tool when you need to pull incoming event data from a Kafka topic for processing or integration. Do not use this tool to publish or produce messages to Kafka. Note: consuming messages may advance the consumer group offset, which can affect subsequent reads.

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

    def kafka_produce_messages(
        self,
        message: str,
        topic_name: str,
    ) -> Dict[str, Any]:
        """Publishes one or more messages to a specified Kafka topic. Use this tool when you need to send data into a Kafka topic as part of a data pipeline or event-driven workflow. Do not use this tool to read or consume messages from Kafka. Note: messages published to Kafka are durable and will be consumed by any active subscribers on the target topic.

        Args:
            message: The message to be sent to the Kafka topic. (required)
            topic_name: Name of the Kafka topic to send the message to. (required)
        Returns:
            API response as a dictionary.
        """
        ...

