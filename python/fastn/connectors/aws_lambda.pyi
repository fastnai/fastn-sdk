"""Fastn AWS Lambda connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AwsLambdaConnector:
    """AWS Lambda connector ().

    Provides 1 tools.
    """

    def invoke_function(
        self,
        Qualifier: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Invokes a specified function within the appropriate environment, allowing for dynamic execution of code as needed.

        Args:
            Qualifier: Qualifier for the AWS Lambda function (e.g., version or alias).
        Returns:
            API response as a dictionary.
        """
        ...

