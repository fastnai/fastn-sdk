"""Fastn Tally connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TallyConnector:
    """Tally connector ().

    Provides 14 tools.
    """

    def create_form(
        self,
        status: str,
        blocks: Optional[List[Any]] = None,
        settings: Optional[Dict[str, Any]] = None,
        templateId: Optional[str] = None,
        workspaceId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new form in the specified application for data collection.

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

    def create_webhook(
        self,
        eventTypes: List[Any],
        formId: str,
        url: str,
        externalSubscriber: Optional[str] = None,
        httpHeaders: Optional[List[Any]] = None,
        signingSecret: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the specified application to receive real-time notifications.

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

    def create_workspace(
        self,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new workspace within the specified application to organize projects and tasks.

        Args:
            name: The name of the workspace to create. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_acc_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves account information for the authenticated user in the specified application.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_form(
        self,
        formId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific form by its ID in the specified application.

        Args:
            formId: The unique identifier of the form to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_form_questions(
        self,
        formId: str,
    ) -> Dict[str, Any]:
        """Retrieves the questions associated with a specific form in the specified application.

        Args:
            formId: The unique identifier of the form to retrieve questions from. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_forms(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
        workspaceIds: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all forms available in the specified application.

        Args:
            limit: The maximum number of forms to return in the response.
            page: The page number of the paginated results to retrieve.
            workspaceIds: Comma-separated list of workspace IDs to filter the forms.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_invites(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of invites sent within the specified application.

        Args:
            organizationId: Unique identifier of the organization whose invites are to be retrieved. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_submissions(
        self,
        afterId: Optional[str] = None,
        endDate: Optional[str] = None,
        filter: Optional[str] = None,
        page: Optional[str] = None,
        startDate: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves submissions for a specific form in the specified application.

        Args:
            afterId: Returns submissions after the specified submission ID for pagination.
            endDate: The end date for restricting the submission return range.
            filter: Filter criteria to narrow down the submissions.
            page: Page number of the submissions list to return.
            startDate: The start date for restricting the submission return range.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
        organizationId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of users in the specified application.

        Args:
            organizationId: The unique identifier of the organization to retrieve users for. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhook_events(
        self,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves events from webhooks in the specified application.

        Args:
            page: The page number to fetch in the webhook events pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_webhooks(
        self,
        limit: Optional[str] = None,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all webhooks configured in the specified application.

        Args:
            limit: Maximum number of webhook records to return per page.
            page: Page number for paginated webhook results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspace(
        self,
        workspaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific workspace in the specified application.

        Args:
            workspaceId: The unique identifier of the workspace to retrieve. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspaces(
        self,
        page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all workspaces available in the specified application.

        Args:
            page: The page number of workspaces to retrieve for paginated results.
        Returns:
            API response as a dictionary.
        """
        ...

