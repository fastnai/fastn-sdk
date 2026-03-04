"""Fastn Clappia connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _ClappiaAddUserToAppPermissions(TypedDict, total=False):
    canBulkUpload: bool
    canChangeStatus: bool
    canDeleteData: bool
    canEditApp: bool
    canEditData: bool
    canSubmitData: bool
    canViewAnalytics: bool
    canViewData: bool

class _ClappiaCreateSubmissionData(TypedDict, total=False):
    annual_revenue: str
    code_scanner: str
    counter: int
    date_selector: str
    drop_down: str
    email_input: str
    multi_line_text: str
    multiple_selector: str
    nfc_reader: str
    number_input: int
    phone_number: str
    ratings: int
    rich_text_editor: str
    single_line_text: str
    single_selector: str
    slider: int
    tags: str
    time_selector: str
    toggle: str
    url_input: str

class _ClappiaListSubmissionsFilters(TypedDict, total=False):
    conditions: List[Any]
    operator: str
    queries: List[Any]

class _ClappiaUpdateSubmissionData(TypedDict, total=False):
    annual_revenue: str
    code_scanner: str
    counter: int
    date_selector: str
    drop_down: str
    email_input: str
    multi_line_text: str
    multiple_selector: str
    nfc_reader: str
    number_input: int
    phone_number: str
    ratings: int
    rich_text_editor: str
    single_line_text: str
    single_selector: str
    slider: int
    tags: str
    time_selector: str
    toggle: str
    url_input: str

class ClappiaConnector:
    """Clappia connector ().

    Provides 9 tools.
    """

    def clappia_add_user_to_app(
        self,
        appId: str,
        emailAddress: str,
        permissions: _ClappiaAddUserToAppPermissions,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Adds a user to a specific Clappia application, granting them access to that app. Use this tool when a user needs to be assigned to a particular app within the workplace. Do not use this tool to grant general workplace access (use clappia_add_user_to_workplace instead). This action modifies app-level membership and may trigger access notifications.

        Args:
            appId: The ID of the application. (required)
            emailAddress: The email address of the user. (required)
            permissions: Permissions granted to the user. (required)
            workplaceId: The ID of the workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clappia_add_user_to_workplace(
        self,
        userEmail: str,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Adds a user to a Clappia workplace, granting them access to the workplace environment. Use this tool when onboarding a new user who needs workplace-level access. Do not use this tool to add a user to a specific app (use clappia_add_user_to_app instead). This action modifies workplace membership and may trigger notifications to the added user.

        Args:
            userEmail: The email address of the user. (required)
            workplaceId: The ID of the workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clappia_create_submission(
        self,
        appId: str,
        data: _ClappiaCreateSubmissionData,
        requestingUserEmailAddress: str,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Creates a new form submission in a specified Clappia app. Use this tool when you need to submit new data entries into a Clappia application form. Do not use this tool to update an existing submission (use clappia_update_submission instead). This action creates a permanent record in the app and cannot be undone without a separate delete operation.

        Args:
            appId: The unique identifier for the Clappia app. (required)
            data: The data to be processed by the Clappia app. (required)
            requestingUserEmailAddress: The email address of the user making the request. (required)
            workplaceId: The unique identifier for the Clappia workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clappia_get_submission(
        self,
        appId: str,
        submissionId: str,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single Clappia form submission by its ID. Use this tool when you need to inspect all field values and metadata for one specific submission. Do not use this tool to retrieve multiple submissions (use clappia_list_submissions instead). No data is modified by this call.

        Args:
            appId: The unique identifier for the application. (required)
            submissionId: The unique identifier for the submission. (required)
            workplaceId: The unique identifier for the workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clappia_list_submissions(
        self,
        appId: str,
        forward: bool,
        pageSize: int,
        requestingUserEmailAddress: str,
        workplaceId: str,
        filters: Optional[_ClappiaListSubmissionsFilters] = None,
    ) -> Dict[str, Any]:
        """Lists all submissions for a specified Clappia application. Use this tool when you need to retrieve a collection of submission records from an app, for example for reporting or bulk review. Do not use this tool to retrieve a single submission by ID (use clappia_get_submission instead). No data is modified by this call.

        Args:
            appId: The ID of the application. (required)
            forward: Indicates whether to forward the request. (required)
            pageSize: The number of records per page. (required)
            requestingUserEmailAddress: The email address of the user making the request. (required)
            workplaceId: The ID of the workplace. (required)
            filters: Filtering criteria for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def clappia_list_user_apps(
        self,
        emailAddress: str,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Lists all Clappia applications associated with a specific user. Use this tool when you need to retrieve the full set of apps a given user has access to within a Clappia workplace. Do not use this tool to retrieve apps across the entire workplace (use clappia_list_workplace_apps instead). No data is modified by this call.

        Args:
            emailAddress: The ID of the user. (required)
            workplaceId: The ID of the workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clappia_list_workplace_apps(
        self,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Lists all Clappia applications available in the workplace. Use this tool when you need a complete inventory of apps within a Clappia workplace, regardless of user. Do not use this tool to filter apps by a specific user (use clappia_list_user_apps instead). No data is modified by this call.

        Args:
            workplaceId: The ID of the workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def clappia_list_workplace_users(
        self,
        token: str,
        workplaceId: str,
        pageSize: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Lists all users in a Clappia workplace, including their membership details. Use this tool when you need a full roster of users who belong to a workplace. Do not use this tool to retrieve apps or submissions. No data is modified by this call.

        Args:
            token: Authentication token. (required)
            workplaceId: The ID of the workplace. (required)
            pageSize: Number of records per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def clappia_update_submission(
        self,
        appId: str,
        data: _ClappiaUpdateSubmissionData,
        requestingUserEmailAddress: str,
        submissionId: str,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Updates the field values of an existing Clappia form submission. Use this tool when you need to modify data in a submission that has already been created. Do not use this tool to create a new submission (use clappia_create_submission instead). This action overwrites existing submission data and the change is permanent unless subsequently updated again.

        Args:
            appId: The unique identifier of the Clappia app. (required)
            data: The data being submitted to the Clappia app. (required)
            requestingUserEmailAddress: The email address of the user making the request. (required)
            submissionId: The unique identifier of the submission. (required)
            workplaceId: The unique identifier of the Clappia workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

