"""Fastn AWS Security Token Service connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AwsSecurityTokenServiceConnector:
    """AWS Security Token Service connector ().

    Provides 2 tools.
    """

    def assume_role(
        self,
        RoleArn: str,
        RoleSessionName: str,
    ) -> Dict[str, Any]:
        """Assumes a role in the AWS connector, allowing access to resources with specific permissions granted to that role.

        Args:
            RoleArn: ARN of the role to assume. (required)
            RoleSessionName: Name of the assumed role session. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_assume_role(
        self,
        RoleArn: str,
        RoleSessionName: str,
    ) -> Dict[str, Any]:
        """Uses the fast role assumption feature in the AWS connector to quickly assume a role and gain temporary security credentials for accessing AWS resources.

        Args:
            RoleArn: The ARN of the role to assume. (required)
            RoleSessionName: The name of the role session. (required)
        Returns:
            API response as a dictionary.
        """
        ...

