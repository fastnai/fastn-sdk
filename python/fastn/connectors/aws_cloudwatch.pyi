"""Fastn AWS Cloudwatch connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class AwsCloudwatchConnector:
    """AWS Cloudwatch connector ().

    Provides 1 tools.
    """

    def execute_query(
        self,
        endTime: Optional[str] = None,
        limit: Optional[int] = None,
        logGroupName: Optional[str] = None,
        queryString: Optional[str] = None,
        startTime: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes a SQL query against the connected database to retrieve or manipulate data.

        Args:
            endTime: End time for the log query (e.g., ISO8601 format).
            limit: Maximum number of log events to return.
            logGroupName: Name of the Cloudwatch log group to query.
            queryString: Filter logs based on a provided query string (CloudWatch Insights).
            startTime: Start time for the log query (e.g., ISO8601 format).
        Returns:
            API response as a dictionary.
        """
        ...

