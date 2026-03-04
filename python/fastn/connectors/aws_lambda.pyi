"""Fastn AWS Lambda connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AwsLambdaConnector:
    """AWS Lambda connector ().

    Provides 1 tools.
    """

    def aws_lambda_invoke_function(
        self,
        body: Dict[str, Any],
        functionName: str,
        Qualifier: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Invokes a specified AWS Lambda function by name and returns its response. Supports synchronous and asynchronous invocation modes. Use this tool when you need to trigger a Lambda function to execute backend logic, process data, or respond to a programmatic event. Do not use this tool to create, update, or delete Lambda functions. Note: invoking a Lambda function may trigger side effects such as database writes, external API calls, or other irreversible actions depending on the functions implementation.

        Args:
            body: Main request body for the AWS Lambda function. (required)
            functionName: Name of the AWS Lambda function to invoke. (required)
            Qualifier: Qualifier for the AWS Lambda function (e.g., version or alias).
        Returns:
            API response as a dictionary.
        """
        ...

