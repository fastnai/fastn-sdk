"""Fastn AWS Simple Notification Service connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AwsSimpleNotificationServiceConnector:
    """AWS Simple Notification Service connector ().

    Provides 6 tools.
    """

    def aws_sns_confirm_subscription(
        self,
        Token: str,
        TopicArn: str,
    ) -> Dict[str, Any]:
        """Confirms a pending AWS SNS subscription using a token received at the subscribed endpoint, activating the subscription so the endpoint begins receiving published messages. Use this tool after creating a subscription that requires confirmation. Do not use this tool if the subscription is already confirmed or if auto-confirmation is configured.

        Args:
            Token: Token for message authentication or authorization (if required). (required)
            TopicArn: Amazon Resource Name (ARN) of the SNS topic. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_sns_create_subscription(
        self,
        Action: str,
        Endpoint: str,
        Protocol: str,
        ReturnSubscriptionArn: bool,
        TopicArn: str,
    ) -> Dict[str, Any]:
        """Creates a new subscription on a specified AWS SNS topic, registering an endpoint (e.g., email, SQS queue, HTTP URL, Lambda) to receive messages published to that topic. Use this tool when you need to add a new subscriber to an existing SNS topic. The subscription may require confirmation before it becomes active — use aws_sns_confirm_subscription to complete the process. This action creates a persistent subscription record.

        Args:
            Action: The action to perform (e.g., Subscribe, Publish). (required)
            Endpoint: The endpoint to which messages will be delivered. (required)
            Protocol: The protocol to use for the subscription (e.g., http, https, sqs). (required)
            ReturnSubscriptionArn: Whether to return the subscription ARN. (required)
            TopicArn: The ARN of the topic to which to subscribe or publish. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_sns_create_topic(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new AWS SNS topic in the configured region and returns its ARN. Use this tool when you need to establish a new pub/sub channel before adding subscriptions or publishing messages. If a topic with the same name already exists, SNS returns the existing topics ARN without creating a duplicate. This action creates a persistent resource.

        Args:
            name: Name for the AWS Simple Notification Service resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_sns_list_subscriptions(
        self,
    ) -> Dict[str, Any]:
        """Lists all subscriptions associated with a specified AWS SNS topic, returning details such as subscriber endpoints, protocols, and subscription status. Use this tool when you need to audit or review who is subscribed to a topic. Does not modify any subscriptions.
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_sns_list_topics(
        self,
    ) -> Dict[str, Any]:
        """Lists all AWS SNS topics available in the configured region, returning their ARNs and names. Use this tool when you need to discover existing topics before publishing messages or managing subscriptions. Does not return subscription details — use aws_sns_list_subscriptions for that. Does not modify any resources.
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_sns_publish_message(
        self,
        Message: str,
        TargetArn: str,
    ) -> Dict[str, Any]:
        """Publishes a message to a specified AWS SNS topic, delivering it to all active subscribers of that topic. Use this tool when you need to broadcast a notification or message to multiple endpoints simultaneously. The message is delivered immediately and cannot be recalled after publishing. Do not use this tool to send messages to individual SQS queues directly — use the AWS SQS connector instead.

        Args:
            Message: The message to be sent. (required)
            TargetArn: The ARN of the target topic or endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

