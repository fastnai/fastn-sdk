"""Fastn Tally connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _TallyCreateFormSettings(TypedDict, total=False):
    closeDate: str
    closeMessageDescription: str
    closeMessageTitle: str
    closeTime: str
    closeTimezone: str
    hasPartialSubmissions: bool
    hasProgressBar: bool
    hasRespondentEmailNotifications: bool
    hasSelfEmailNotifications: bool
    isClosed: bool
    language: str
    pageAutoJump: bool
    password: str
    redirectOnCompletion: str
    respondentEmailBody: str
    respondentEmailFromName: str
    respondentEmailReplyTo: str
    respondentEmailSubject: str
    respondentEmailTo: str
    saveForLater: bool
    selfEmailBody: str
    selfEmailFromName: str
    selfEmailReplyTo: str
    selfEmailSubject: str
    selfEmailTo: str
    styles: str
    submissionsDataRetentionDuration: int
    submissionsDataRetentionUnit: str
    submissionsLimit: int
    uniqueSubmissionKey: str

class TallyConnector:
    """Tally connector ().

    Provides 14 tools.
    """

    def tally_create_form(
        self,
        status: str,
        blocks: Optional[List[Any]] = None,
        settings: Optional[_TallyCreateFormSettings] = None,
        templateId: Optional[str] = None,
        workspaceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new form in the authenticated Tally account for data collection. Use this tool when you need to build a new form from scratch. Do not use this tool to update an existing form or retrieve existing forms — use tally_list_forms or tally_get_form instead. This action permanently creates a new form resource in Tally.

        Args:
            status: Current status of the form. (required)
            blocks: Array of block objects representing the form's components.
            settings: Configuration settings for the form.
            templateId: Identifier of the template used for creating the form.
            workspaceId: Identifier of the workspace in which the form is created.
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_create_webhook(
        self,
        eventTypes: List[Any],
        formId: str,
        url: str,
        externalSubscriber: Optional[str] = None,
        httpHeaders: Optional[List[Any]] = None,
        signingSecret: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the authenticated Tally account to receive real-time event notifications at a specified URL. Use this tool when you need to set up an integration that listens for Tally events such as form submissions. Do not use this tool to list existing webhooks — use tally_list_webhooks instead. This action registers a new active webhook endpoint.

        Args:
            eventTypes: The list of event types that will trigger the webhook. (required)
            formId: The unique identifier of the form for which the webhook is being created. (required)
            url: The URL to which webhook notifications will be sent. (required)
            externalSubscriber: An optional identifier for an external subscriber associated with the webhook.
            httpHeaders: Custom HTTP headers to include in the webhook request.
            signingSecret: Secret used to sign webhook payloads for verification.
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_create_workspace(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new workspace in the authenticated Tally account. Use this tool when you need to set up a new workspace to organize forms and projects. Do not use this tool to update an existing workspace. This action permanently creates a new workspace resource in Tally.

        Args:
            name: The name of the workspace to create. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_get_account_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves account profile information for the currently authenticated Tally user, including name, email, and account settings. Use this tool when you need to identify or verify the authenticated users details. Do not use this tool to list organization members — use tally_list_users instead. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_get_form(
        self,
        formId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details of a specific Tally form identified by formId, including its title, status, and configuration. Use this tool when you need metadata about a single form. Do not use this tool to list all forms — use tally_list_forms instead, or to retrieve submissions — use tally_list_submissions instead. Does not modify any data.

        Args:
            formId: The unique identifier of the form to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_get_workspace(
        self,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific Tally workspace identified by workspaceId, including its name and configuration. Use this tool when you need full details of a single workspace. Do not use this tool to list all workspaces — use tally_list_workspaces instead. Does not modify any data.

        Args:
            workspaceId: The unique identifier of the workspace to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_list_form_questions(
        self,
        formId: str,
    ) -> Dict[str, Any]:
        """Lists all questions defined in a specific Tally form identified by formId. Use this tool when you need to inspect the structure or fields of a form. Do not use this tool to retrieve form submissions — use tally_list_submissions instead. Does not modify any data.

        Args:
            formId: The unique identifier of the form to retrieve questions from. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_list_forms(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        workspaceIds: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all forms available in the authenticated Tally account. Use this tool when you need to discover existing forms before accessing form-specific resources such as submissions or questions. Do not use this tool to retrieve details of a single form — use tally_get_form instead. Does not modify any data.

        Args:
            limit: The maximum number of forms to return in the response.
            page: The page number of the paginated results to retrieve.
            workspaceIds: Comma-separated list of workspace IDs to filter the forms.
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_list_invites(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Lists all pending and sent invites for a specific Tally organization identified by organizationId. Use this tool when you need to review who has been invited to join an organization. Do not use this tool to list current users — use tally_list_users instead. Does not modify any data.

        Args:
            organizationId: Unique identifier of the organization whose invites are to be retrieved. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_list_submissions(
        self,
        formId: str,
        afterId: Optional[str] = None,
        endDate: Optional[str] = None,
        filter: Optional[str] = None,
        page: Optional[str] = None,
        startDate: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all submissions received for a specific Tally form identified by formId. Use this tool when you need to retrieve respondent data collected by a form. Do not use this tool to retrieve the form structure or questions — use tally_get_form or tally_list_form_questions instead. Does not modify any data.

        Args:
            formId: The unique identifier of the Tally form to get submissions from. (required)
            afterId: Returns submissions after the specified submission ID for pagination.
            endDate: The end date for restricting the submission return range.
            filter: Filter criteria to narrow down the submissions.
            page: Page number of the submissions list to return.
            startDate: The start date for restricting the submission return range.
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_list_users(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Lists all users belonging to a specific Tally organization identified by organizationId. Use this tool when you need to review the members of an organization. Do not use this tool to retrieve account information for the authenticated user — use tally_get_account_info instead. Does not modify any data.

        Args:
            organizationId: The unique identifier of the organization to retrieve users for. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_list_webhook_events(
        self,
        webhookId: str,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all events fired by a specific Tally webhook identified by webhookId. Use this tool when you need to inspect the event history or delivery log for a particular webhook. Do not use this tool to list all webhooks — use tally_list_webhooks instead. Does not modify any data.

        Args:
            webhookId: Unique identifier of the webhook whose events are to be retrieved. (required)
            page: The page number to fetch in the webhook events pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_list_webhooks(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all webhooks configured in the authenticated Tally account. Use this tool when you need to audit or review existing webhook integrations. Do not use this tool to retrieve events for a specific webhook — use tally_list_webhook_events instead. Does not modify any data.

        Args:
            limit: Maximum number of webhook records to return per page.
            page: Page number for paginated webhook results.
        Returns:
            API response as a dictionary.
        """
        ...

    def tally_list_workspaces(
        self,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all workspaces available in the authenticated Tally account. Use this tool when you need to discover existing workspaces before accessing workspace-specific resources. Do not use this tool to retrieve details of a single workspace — use tally_get_workspace instead. Does not modify any data.

        Args:
            page: The page number of workspaces to retrieve for paginated results.
        Returns:
            API response as a dictionary.
        """
        ...

