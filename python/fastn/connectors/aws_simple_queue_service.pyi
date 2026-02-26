"""Fastn AWS Simple Queue Service connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AwsSimpleQueueServiceConnector:
    """AWS Simple Queue Service connector ().

    Provides 3 tools.
    """

    def create_queue(
        self,
        QueueName: str,
        Attributes: Optional[Dict[str, Any]] = None,
        tags: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new message queue using the createQueue connector, enabling the management and organization of messages for processing.

        Args:
            QueueName: Name of the SQS queue to be created. (required)
            Attributes: Attributes for the SQS queue.
            tags: Tags for the SQS queue.
        Returns:
            API response as a dictionary.
        """
        ...

    def read_messages_from_queue(
        self,
        QueueUrl: str,
        MaxNumberOfMessages: Optional[int] = None,
        VisibilityTimeout: Optional[int] = None,
        WaitTimeSeconds: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Retrieves messages from the specified queue using the readMessagesFromQueue connector, facilitating the consumption and processing of queued messages.

        Args:
            QueueUrl: The URL of the SQS queue. (required)
            MaxNumberOfMessages: The maximum number of messages to receive.
            VisibilityTimeout: The duration (in seconds) for which messages are hidden from other consumers.
            WaitTimeSeconds: The duration (in seconds) to wait for a message before returning.
        Returns:
            API response as a dictionary.
        """
        ...

    def send_message_to_queue(
        self,
        MessageBody: str,
        QueueUrl: str,
    ) -> Dict[str, Any]:
        """Sends a message to the specified queue utilizing the sendMessageToQueue connector, allowing you to transfer data or notifications to the designated queue.

        Args:
            MessageBody: The message body to be sent to the queue. (required)
            QueueUrl: URL of the SQS queue. (required)
        Returns:
            API response as a dictionary.
        """
        ...

