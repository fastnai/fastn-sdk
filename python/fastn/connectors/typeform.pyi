"""Fastn Typeform connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _TypeformCreateFormSettings(TypedDict, total=False):
    is_public: bool
    language: str
    meta: Dict[str, Any]
    progress_bar: str
    show_progress_bar: bool
    show_typeform_branding: bool

class _TypeformUpdateFormSettings(TypedDict, total=False):
    is_public: bool
    language: str
    meta: Dict[str, Any]
    progress_bar: str
    show_progress_bar: bool
    show_typeform_branding: bool

class TypeformConnector:
    """Typeform connector ().

    Provides 12 tools.
    """

    def typeform_create_form(
        self,
        fields: List[Any],
        settings: _TypeformCreateFormSettings,
        title: str,
    ) -> Dict[str, Any]:
        """Creates a new Typeform form with specified fields, settings, and configuration. Use this tool when you need to programmatically build a new survey or data collection form in Typeform. Do not use this tool to modify an existing form; use typeform_update_form instead. This action creates a persistent form resource that can immediately be shared with respondents.

        Args:
            fields:  (required)
            settings: Settings for the Typeform. (required)
            title: Title of the Typeform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def typeform_create_or_update_webhook(
        self,
        enabled: bool,
        event: str,
        form_id: str,
        tag: str,
        url: str,
    ) -> Dict[str, Any]:
        """Creates a new webhook or updates an existing webhook on a specified Typeform form, identified by the form ID and webhook tag. Use this tool to register a callback URL that Typeform will notify when new responses are submitted. If a webhook with the given tag already exists, it will be overwritten. Do not use this tool to delete a webhook; use typeform_delete_webhook instead. This action modifies webhook configuration and may affect real-time event delivery immediately.

        Args:
            enabled: Indicates whether the webhook is enabled or disabled. (required)
            event: Type of event being sent to Typeform. (required)
            form_id: The unique identifier of the Typeform form. (required)
            tag: A tag associated with the Typeform form. (required)
            url: URL to receive webhook notifications from Typeform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def typeform_delete_form(
        self,
        form_id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified Typeform form and all its associated data, identified by the form ID. Use this tool when you need to remove a form that is no longer needed. Do not use this tool if you only want to update or deactivate the form; use typeform_update_form instead. This action is irreversible — the form, its questions, and all collected responses will be permanently lost.

        Args:
            form_id: The ID of the Typeform form to interact with. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def typeform_delete_responses(
        self,
        form_id: str,
        included_response_ids: str,
    ) -> Dict[str, Any]:
        """Permanently deletes specified responses from a Typeform form, identified by the form ID and response token IDs. Use this tool when you need to remove specific respondent data, for example to fulfill a data deletion request. Do not use this tool to retrieve or export responses before deletion; use typeform_list_responses first. This action is irreversible — deleted responses cannot be recovered.

        Args:
            form_id:  (required)
            included_response_ids: Comma-separated list of response IDs to include in the results. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def typeform_delete_webhook(
        self,
        form_id: str,
        tag: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified webhook from a Typeform form, identified by the form ID and webhook tag. Use this tool when you need to remove a webhook that is no longer needed. Do not use this tool if you only want to disable or update the webhook; use typeform_create_or_update_webhook instead. This action is irreversible — the webhook configuration cannot be recovered after deletion.

        Args:
            form_id: The unique identifier of the Typeform form. (required)
            tag: A tag associated with the Typeform form. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def typeform_get_form(
        self,
        form_id: str,
    ) -> Dict[str, Any]:
        """Retrieves the full configuration and field definitions of a specific Typeform form, identified by its form ID. Use this tool when you need to inspect a forms structure, questions, settings, or metadata. Do not use this tool to list all available forms; use typeform_list_forms instead. This is a read-only operation with no side effects.

        Args:
            form_id: The unique identifier of the Typeform form. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def typeform_get_user_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves profile information for the currently authenticated Typeform account, including username, email, and account metadata. Use this tool when you need to verify the authenticated users identity or retrieve account-level details. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def typeform_get_webhook(
        self,
        form_id: str,
        my_webhook_tag: str,
    ) -> Dict[str, Any]:
        """Retrieves configuration details for a single webhook on a specified Typeform form, identified by the form ID and webhook tag. Use this tool when you need to inspect a specific webhooks URL, enabled status, or secret. Do not use this tool to list all webhooks for a form; use typeform_list_webhooks instead. This is a read-only operation with no side effects.

        Args:
            form_id: ID of the Typeform form associated with this webhook. (required)
            my_webhook_tag: Unique identifier for the webhook within Typeform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def typeform_list_forms(
        self,
        page: Optional[str] = None,
        page_size: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all Typeform forms available in the authenticated account, including their IDs, titles, and metadata. Use this tool when you need an overview of all forms or to find a specific form ID. Do not use this tool to retrieve the full field definitions of a single form; use typeform_get_form instead. This is a read-only operation with no side effects.

        Args:
            page: The page number to retrieve.
            page_size: The number of results per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def typeform_list_responses(
        self,
        form_id: str,
    ) -> Dict[str, Any]:
        """Retrieves all submitted responses for a specified Typeform form, including answer data, metadata, and submission timestamps. Use this tool when you need to analyze or export form response data. Do not use this tool to delete responses; use typeform_delete_responses instead. This is a read-only operation with no side effects.

        Args:
            form_id: The ID of the Typeform form. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def typeform_list_webhooks(
        self,
        form_id: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all webhooks configured for a specified Typeform form, including their tags, URLs, and enabled status. Use this tool when you need an overview of all event listeners set up for a form. Do not use this tool to retrieve details about a single webhook; use typeform_get_webhook instead. This is a read-only operation with no side effects.

        Args:
            form_id: ID of the Typeform form to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def typeform_update_form(
        self,
        fields: List[Any],
        form_id: str,
        settings: _TypeformUpdateFormSettings,
        title: str,
    ) -> Dict[str, Any]:
        """Updates the configuration, fields, or settings of an existing Typeform form, identified by its form ID. Use this tool when you need to modify questions, logic, or form metadata. Do not use this tool to create a new form; use typeform_create_form instead. This action overwrites the existing form definition and changes will be immediately reflected for new respondents.

        Args:
            fields:  (required)
            form_id: ID of the Typeform. (required)
            settings: Form settings for the Typeform. (required)
            title: Title of the Typeform. (required)
        Returns:
            API response as a dictionary.
        """
        ...

