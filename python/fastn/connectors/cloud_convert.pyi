"""Fastn Cloud Convert connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _CloudConvertCreateJobTasks(TypedDict, total=False):
    : Dict[str, Any]

class CloudConvertConnector:
    """Cloud Convert connector ().

    Provides 6 tools.
    """

    def cloud_convert_create_job(
        self,
        tasks: Optional[_CloudConvertCreateJobTasks] = None,
    ) -> Dict[str, Any]:
        """Creates and immediately executes a new CloudConvert conversion job using the synchronous API endpoint, waiting for the job to complete before returning the result. Use this when you need to convert files and require the output synchronously in a single request. Do not use this for long-running or asynchronous jobs where webhook notifications are preferred — use cloud_convert_create_webhook to handle async callbacks instead. Job creation triggers file processing and may incur usage costs; completed jobs cannot be undone.

        Args:
            tasks: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cloud_convert_create_webhook(
        self,
        url: str,
        events: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook subscription in CloudConvert to receive event notifications (such as job completion or failure) at a specified URL. Use this when you need to be notified asynchronously about CloudConvert job or task events. Do not use this to list or delete existing webhooks — use cloud_convert_list_webhooks or cloud_convert_delete_webhook instead. Creating a webhook is a persistent action; it will continue sending notifications until explicitly deleted.

        Args:
            url: URL of the file to be converted. (required)
            events: Array of events to be triggered during the conversion process.
        Returns:
            API response as a dictionary.
        """
        ...

    def cloud_convert_delete_webhook(
        self,
        webhookId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified webhook from the CloudConvert account. Use this when a webhook subscription is no longer needed and should stop receiving event notifications. Do not use this to delete jobs or tasks — use job or task-specific tools instead. This action is irreversible: the webhook configuration will be permanently removed and must be recreated if needed again.

        Args:
            webhookId: The ID of the webhook.
        Returns:
            API response as a dictionary.
        """
        ...

    def cloud_convert_get_job_status(
        self,
        jobId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the current status and details of a specific CloudConvert job by its job ID, including the status of all tasks within the job and any output file references. Use this to check whether a conversion job has completed, is still processing, or has failed. Do not use this to retrieve individual task status — use cloud_convert_get_task_status instead. This is a read-only operation with no side effects.

        Args:
            jobId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cloud_convert_get_task_status(
        self,
        taskId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the current status and details of a specific CloudConvert task by its task ID, including its operation type, progress, and result. Use this to monitor the progress of an individual conversion or processing step within a job. Do not use this to retrieve overall job status — use cloud_convert_get_job_status instead. This is a read-only operation with no side effects.

        Args:
            taskId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def cloud_convert_list_webhooks(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all webhook subscriptions configured for the authenticated CloudConvert user. Use this to inspect existing webhook URLs and their event configurations before creating or deleting webhooks. Do not use this to retrieve job or task status — use cloud_convert_get_job_status or cloud_convert_get_task_status instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

