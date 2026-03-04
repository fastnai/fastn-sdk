"""Fastn AWS Simple Queue Service connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _AwsSimpleQueueServiceCreateQueueAttributes(TypedDict, total=False):
    VisibilityTimeout: str

class _AwsSimpleQueueServiceCreateQueueTags(TypedDict, total=False):
    QueueType: str

class AwsSimpleQueueServiceConnector:
    """AWS Simple Queue Service connector ().

    Provides 3 tools.
    """

    def aws_simple_queue_service_create_queue(
        self,
        QueueName: str,
        Attributes: Optional[_AwsSimpleQueueServiceCreateQueueAttributes] = None,
        tags: Optional[_AwsSimpleQueueServiceCreateQueueTags] = None,
    ) -> Dict[str, Any]:
        """Creates a new AWS SQS message queue with the specified name and configuration, returning the queue URL. Use this tool when you need to establish a new queue before sending or receiving messages. If a queue with the same name and attributes already exists, SQS returns the existing queue URL. This action creates a persistent resource.

        Args:
            QueueName: Name of the SQS queue to be created. (required)
            Attributes: Attributes for the SQS queue.
            tags: Tags for the SQS queue.
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_simple_queue_service_receive_messages_from_queue(
        self,
        QueueUrl: str,
        queueId: str,
        queueName: str,
        MaxNumberOfMessages: Optional[int] = None,
        VisibilityTimeout: Optional[int] = None,
        WaitTimeSeconds: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Receives one or more messages from a specified AWS SQS queue and returns their content and metadata. Use this tool when you need to consume and process queued messages. Note: received messages remain in the queue and become temporarily invisible to other consumers; they must be explicitly deleted after processing to prevent redelivery. Do not use this tool if you only want to check queue attributes without consuming messages.

        Args:
            QueueUrl: The URL of the SQS queue. (required)
            queueId: The ID of the queue. (required)
            queueName: The name of the queue. (required)
            MaxNumberOfMessages: The maximum number of messages to receive.
            VisibilityTimeout: The duration (in seconds) for which messages are hidden from other consumers.
            WaitTimeSeconds: The duration (in seconds) to wait for a message before returning.
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_simple_queue_service_send_message_to_queue(
        self,
        MessageBody: str,
        QueueUrl: str,
    ) -> Dict[str, Any]:
        """Sends a message to a specified AWS SQS queue, making it available for consumers to receive and process. Use this tool when you need to enqueue a task, notification, or data payload for asynchronous processing. The message is delivered immediately and cannot be recalled after sending. Do not use this tool to broadcast to multiple subscribers — use the AWS SNS connector instead.

        Args:
            MessageBody: The message body to be sent to the queue. (required)
            QueueUrl: URL of the SQS queue. (required)
        Returns:
            API response as a dictionary.
        """
        ...

