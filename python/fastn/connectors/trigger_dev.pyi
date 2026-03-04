"""Fastn Trigger.dev connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _TriggerDevTriggerTaskOptions(TypedDict, total=False):
    concurrencyKey: str
    delay: str
    idempotencyKey: str
    machine: str
    queue: Dict[str, Any]
    tags: List[Any]
    ttl: str

class _TriggerDevUpdateRunMetadataMetadata(TypedDict, total=False):
    key: str

class TriggerDevConnector:
    """Trigger.dev connector ().

    Provides 22 tools.
    """

    def trigger_dev_activate_schedule(
        self,
        scheduleId: str,
    ) -> Dict[str, Any]:
        """Activates a previously deactivated schedule in Trigger.dev, causing it to resume triggering tasks according to its configured timing. Use this when a schedule has been paused and you want to re-enable it. Do not use this on a schedule that is already active. This does not create a new schedule — use the create schedule tool for that.

        Args:
            scheduleId: The unique identifier of the schedule in Trigger.dev to target for this request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_batch_trigger_tasks(
        self,
        items: List[Any],
    ) -> Dict[str, Any]:
        """Triggers multiple Trigger.dev tasks simultaneously in a single batch request. Use this when you need to initiate many task runs at once for efficiency. Do not use this to trigger a single task — use the trigger task tool instead. Each task in the batch is triggered independently and may have its own payload.

        Args:
            items:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_cancel_run(
        self,
        runId: str,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Cancels a currently executing or queued task run in Trigger.dev, halting any further processing. Use this when a run must be stopped before it completes. Do not use this to pause a run — cancellation is immediate and the run cannot be resumed. This action is irreversible.

        Args:
            runId: The unique identifier of the run or resource the request targets. (required)
            body: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_create_environment_variables(
        self,
        env: str,
        name: str,
        projectRef: str,
        value: str,
    ) -> Dict[str, Any]:
        """Creates one or more new environment variables in a specified environment of a Trigger.dev project. Use this when the variables do not yet exist and need to be defined for the first time. Do not use this to update existing variables — use the update tool instead. If a variable with the same name already exists, the request may fail or be rejected.

        Args:
            env: The environment (for example: dev, staging, prod) where the Trigger.dev project is deployed. (required)
            name: The name identifier for the resource or parameter being provided in the request. (required)
            projectRef: The project reference or identifier within Trigger.dev. (required)
            value: The value associated with the name field for the Trigger.dev request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_create_schedule(
        self,
        cron: str,
        deduplicationKey: str,
        task: str,
        externalId: Optional[str] = None,
        timezone: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new schedule in Trigger.dev that will trigger a specified task at defined intervals or times. Use this when you need to set up a new recurring or one-time scheduled task. Do not use this to modify an existing schedule — use the update schedule tool instead.

        Args:
            cron: A cron expression that defines the schedule for the trigger (for example: '0 0 * * *'). (required)
            deduplicationKey: Optional key to deduplicate trigger runs; events with the same key within the deduplication window are treated as duplicates. (required)
            task: The identifier or name of the task to execute when the trigger fires. (required)
            externalId: Optional external identifier to associate with the scheduled job for idempotency or tracking.
            timezone: IANA timezone name used to interpret the cron schedule (for example: 'America/Los_Angeles').
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_deactivate_schedule(
        self,
        scheduleId: str,
    ) -> Dict[str, Any]:
        """Deactivates an active schedule in Trigger.dev, pausing task triggering without deleting the schedule configuration. Use this when you want to temporarily stop a schedule without losing its settings. To permanently remove a schedule, use the delete schedule tool instead.

        Args:
            scheduleId: The identifier of the schedule resource in Trigger.dev that the request targets. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_delete_environment_variable(
        self,
        env: str,
        name: str,
        projectRef: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a single named environment variable from a specified environment of a Trigger.dev project. Use this when a configuration value is no longer needed and must be removed. Do not use this to update or rename a variable — use the update tool instead. This action is irreversible; the variable cannot be recovered after deletion.

        Args:
            env: The environment in which the Trigger.dev resource operates (e.g., production, staging). (required)
            name: The name or identifier of the Trigger.dev resource or endpoint. (required)
            projectRef: The reference or identifier of the Trigger.dev project associated with this resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_delete_schedule(
        self,
        scheduleId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific schedule from Trigger.dev, removing all its configuration and stopping any future task triggering associated with it. Use this when a schedule is no longer needed at all. To temporarily pause a schedule without deleting it, use the deactivate schedule tool instead. This action is irreversible.

        Args:
            scheduleId: The identifier of the schedule to target in Trigger.dev. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_get_environment_variable(
        self,
        env: str,
        name: str,
        projectRef: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single named environment variable from a specified environment of a Trigger.dev project. Use this when you need to inspect the current value or metadata of one specific variable. Do not use this to list all variables — use the list environment variables tool instead.

        Args:
            env: The environment identifier for the target (for example, production, staging, or dev). (required)
            name: The name of the target resource or trigger inside Trigger.dev. (required)
            projectRef: The unique project reference or ID within Trigger.dev that identifies the project. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_get_run(
        self,
        runId: str,
    ) -> Dict[str, Any]:
        """Retrieves the details, status, and output of a single task run in Trigger.dev by its run ID. Use this to check whether a specific run succeeded, failed, or is still in progress. Do not use this to list multiple runs — use the list runs tool instead.

        Args:
            runId: The identifier of the run in Trigger.dev (used in the endpoint URL). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_get_schedule(
        self,
        scheduleId: str,
    ) -> Dict[str, Any]:
        """Retrieves the configuration and status details of a single schedule in Trigger.dev by its schedule ID. Use this when you need to inspect a specific schedules timing, activation state, or parameters. Do not use this to list all schedules — use the list schedules tool instead.

        Args:
            scheduleId: Identifier of the schedule resource used by Trigger.dev (scheduleId). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_import_environment_variables(
        self,
        env: str,
        projectRef: str,
        variables: List[Any],
        override: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Imports one or more environment variables into a specified environment of a Trigger.dev project in bulk. Use this when you need to populate or seed an environment (e.g. production, staging) with multiple variables at once. Prefer this over creating variables one by one when handling bulk imports. Does not delete existing variables not included in the import payload. This operation overwrites values for any variable names that already exist.

        Args:
            env: The environment name (for example, production or staging) to target within Trigger.dev. (required)
            projectRef: The identifier or reference for the Trigger.dev project or workspace. (required)
            variables:  (required)
            override: If true, existing variables will be replaced by the provided variables.
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_list_environment_variables(
        self,
        env: str,
        projectRef: str,
    ) -> Dict[str, Any]:
        """Lists all environment variables configured in a specified environment of a Trigger.dev project. Use this to get an overview of all available configuration values for a given environment. Do not use this to retrieve a single variable by name — use the get environment variable tool instead.

        Args:
            env: The target environment for the Trigger.dev project (for example: "production", "staging", or "development"). (required)
            projectRef: The unique reference or identifier for the Trigger.dev project to which the request applies. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_list_runs(
        self,
        filterbulkAction: Optional[List[Any]] = None,
        filtercreatedAtfrom: Optional[str] = None,
        filtercreatedAtperiod: Optional[str] = None,
        filtercreatedAtto: Optional[str] = None,
        filterisTest: Optional[bool] = None,
        filterschedule: Optional[str] = None,
        filterstatus: Optional[List[Any]] = None,
        filtertag: Optional[List[Any]] = None,
        filtertaskIdentifier: Optional[List[Any]] = None,
        filterversion: Optional[List[Any]] = None,
        pageafter: Optional[str] = None,
        pagebefore: Optional[str] = None,
        pagesize: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists the history of task runs in Trigger.dev, including their statuses, timestamps, and associated task identifiers. Use this to get an overview of run history or to find runs to inspect further. Do not use this to retrieve details of a single run — use the get run tool instead.

        Args:
            filterbulkAction: An array of bulk action identifiers to filter results by bulk actions.
            filtercreatedAtfrom: Start of the creation date range (ISO 8601 timestamp) to filter results from.
            filtercreatedAtperiod: Predefined period (e.g., 'last_7_days', 'last_30_days') to filter creation date range.
            filtercreatedAtto: End of the creation date range (ISO 8601 timestamp) to filter results up to.
            filterisTest: When true, limits results to test tasks; when false, excludes test tasks.
            filterschedule: Filter results by schedule identifier or schedule type.
            filterstatus: An array of status values to filter results by task status (e.g., succeeded, failed).
            filtertag: An array of tags to filter results to tasks that contain any of these tags.
            filtertaskIdentifier: An array of task identifiers to filter results to specific tasks.
            filterversion: An array of version strings to filter results to specific versions.
            pageafter: Cursor for pagination to return results after the given cursor.
            pagebefore: Cursor for pagination to return results before the given cursor.
            pagesize: Number of items to return per page (page size). Typically an integer represented as a string.
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_list_schedules(
        self,
        page: Optional[str] = None,
        perPage: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all schedules configured in Trigger.dev, including their timing, activation state, and associated tasks. Use this to get an overview of all scheduled tasks in the project. Do not use this to retrieve a single schedule by ID — use the get schedule tool instead.

        Args:
            page: The page of results to retrieve for paginated responses.
            perPage: Number of items to return per page for paginated responses.
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_list_timezones(
        self,
    ) -> Dict[str, Any]:
        """Lists all timezone identifiers supported by Trigger.dev for use in schedule definitions. Use this to discover valid timezone values before creating or updating a schedule. Do not use this for any purpose other than looking up accepted timezone strings.
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_replay_run(
        self,
        runId: str,
    ) -> Dict[str, Any]:
        """Creates a new task run in Trigger.dev using the same payload and configuration as a previously executed run. Use this to re-execute a run for debugging, testing, or retrying a failed workflow without manually re-supplying input data. This creates a new independent run — it does not modify or restart the original run.

        Args:
            runId: The unique identifier of the run to target in Trigger.dev. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_reschedule_run(
        self,
        delay: str,
        runId: str,
    ) -> Dict[str, Any]:
        """Reschedules a delayed or waiting task run in Trigger.dev to a new execution time. Use this when a run has been scheduled for the future and you need to change when it will execute. Do not use this on runs that are already actively executing or completed — use the cancel run tool to stop an in-progress run.

        Args:
            delay: The delay before executing the trigger, expressed as a duration (for example '5m', '30s', or an ISO 8601 duration). (required)
            runId: The identifier of the run to target within Trigger.dev. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_trigger_task(
        self,
        taskIdentifier: str,
        context: Optional[Dict[str, Any]] = None,
        options: Optional[_TriggerDevTriggerTaskOptions] = None,
        payload: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Triggers a single task in Trigger.dev by its task identifier, starting a new run with the provided payload. Use this to initiate a specific long-running task with retry and scaling support. To trigger multiple tasks at once, use the batch trigger tasks tool instead.

        Args:
            taskIdentifier: The unique identifier (ID or slug) of the Trigger.dev task to invoke. (required)
            context: Optional contextual metadata for the task run (for example user info, environment, or correlation ids).
            options: Optional settings that control task execution behavior in Trigger.dev.
            payload: Arbitrary JSON payload to pass to the triggered task. Shape depends on the task's expected input.
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_update_environment_variable(
        self,
        env: str,
        name: str,
        projectRef: str,
        value: str,
    ) -> Dict[str, Any]:
        """Updates the value of an existing named environment variable in a specified environment of a Trigger.dev project. Use this when you need to change the value of an already-existing variable. Do not use this to create a new variable — use the create tool instead. Only the value can be updated; the variable name itself cannot be changed via this endpoint.

        Args:
            env: The environment identifier (for example, 'production' or 'staging') for the resource. (required)
            name: The name of the target resource or endpoint within Trigger.dev. (required)
            projectRef: The Trigger.dev project reference or ID that the request targets. (required)
            value: The primary value or payload content for the Trigger.dev request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_update_run_metadata(
        self,
        runId: str,
        metadata: Optional[_TriggerDevUpdateRunMetadataMetadata] = None,
    ) -> Dict[str, Any]:
        """Updates the metadata key-value pairs attached to a specific task run in Trigger.dev. Use this to annotate or enrich a run record with additional tracking or contextual information after it has been created. Does not affect the execution or state of the run itself — only its metadata is modified.

        Args:
            runId: The identifier of the run in Trigger.dev that this request targets. (required)
            metadata: Additional metadata for the Trigger.dev run or task.
        Returns:
            API response as a dictionary.
        """
        ...

    def trigger_dev_update_schedule(
        self,
        cron: str,
        scheduleId: str,
        task: str,
        externalId: Optional[str] = None,
        timezone: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the configuration of an existing schedule in Trigger.dev, such as its timing, cron expression, or associated parameters. Use this when a schedule already exists and you need to modify how or when it fires. Do not use this to create a new schedule — use the create schedule tool instead.

        Args:
            cron: A cron expression that defines when the task should run (e.g., '0 9 * * *'). (required)
            scheduleId: The unique identifier of an existing schedule (used for retrieving or modifying a specific schedule). (required)
            task: The identifier or name of the task to execute when the schedule triggers. (required)
            externalId: An optional external identifier to correlate this schedule with records in an external system.
            timezone: The IANA timezone (e.g., 'America/Los_Angeles') used to evaluate the cron expression.
        Returns:
            API response as a dictionary.
        """
        ...

