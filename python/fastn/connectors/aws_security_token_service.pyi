"""Fastn AWS Security Token Service connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AwsSecurityTokenServiceConnector:
    """AWS Security Token Service connector ().

    Provides 2 tools.
    """

    def aws_security_token_service_assume_role(
        self,
        RoleArn: str,
        RoleSessionName: str,
    ) -> Dict[str, Any]:
        """Assumes a specified AWS IAM role via AWS Security Token Service and returns temporary security credentials (access key, secret key, and session token) scoped to that roles permissions. Use this tool when you need to act under a different IAM roles permissions. Do not use this tool if low-latency fast role assumption is needed — use aws_security_token_service_fastn_assume_role instead. Credentials are temporary and will expire after the configured duration.

        Args:
            RoleArn: ARN of the role to assume. (required)
            RoleSessionName: Name of the assumed role session. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def aws_security_token_service_fastn_assume_role(
        self,
        RoleArn: str,
        RoleSessionName: str,
    ) -> Dict[str, Any]:
        """Assumes an AWS IAM role using a fast-path mechanism and returns temporary security credentials (access key, secret key, and session token) via AWS Security Token Service. Use this tool when low-latency role assumption is required and the fast role assumption feature is configured. Do not use this tool if standard role assumption is sufficient — use aws_security_token_service_assume_role instead. Credentials are temporary and will expire.

        Args:
            RoleArn: The ARN of the role to assume. (required)
            RoleSessionName: The name of the role session. (required)
        Returns:
            API response as a dictionary.
        """
        ...

