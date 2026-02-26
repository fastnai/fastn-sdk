"""Fastn Cloud Convert connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class CloudConvertConnector:
    """Cloud Convert connector ().

    Provides 6 tools.
    """

    def create_job(
        self,
        tasks: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new job in the system using the specified connector.

        Args:
            tasks: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_webhooks(
        self,
        url: str,
        events: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the system using the specified connector.

        Args:
            url: URL of the file to be converted. (required)
            events: Array of events to be triggered during the conversion process.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing webhook from the system using the specified connector.

        Args:
            webhookId: The ID of the webhook.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_job_status(
        self,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the current status of a job from the system using the specified connector.

        Args:
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_task_status(
        self,
        taskId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the status of a specific task within a job using the specified connector.

        Args:
            taskId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhooks(
        self,
    ) -> Dict[str, Any]:
        """Lists all webhooks configured in the system using the specified connector.
        Returns:
            API response as a dictionary.
        """
        ...

