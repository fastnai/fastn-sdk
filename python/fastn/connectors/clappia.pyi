"""Fastn Clappia connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ClappiaConnector:
    """Clappia connector ().

    Provides 9 tools.
    """

    def add_user_to_app(
        self,
        appId: str,
        emailAddress: str,
        permissions: Dict[str, Any],
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Adds a user to the application via the specified connector.

        Args:
            appId: The ID of the application. (required)
            emailAddress: The email address of the user. (required)
            permissions: Permissions granted to the user. (required)
            workplaceId: The ID of the workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def add_user_to_workplace(
        self,
        userEmail: str,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Adds a user to the workplace using the specified connector.

        Args:
            userEmail: The email address of the user. (required)
            workplaceId: The ID of the workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_submission(
        self,
        appId: str,
        data: Dict[str, Any],
        requestingUserEmailAddress: str,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Creates a new submission in the specified connector.

        Args:
            appId: The unique identifier for the Clappia app. (required)
            data: The data to be processed by the Clappia app. (required)
            requestingUserEmailAddress: The email address of the user making the request. (required)
            workplaceId: The unique identifier for the Clappia workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_submission(
        self,
        appId: str,
        submissionId: str,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific submission from the specified connector.

        Args:
            appId: The unique identifier for the application. (required)
            submissionId: The unique identifier for the submission. (required)
            workplaceId: The unique identifier for the workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_submissions(
        self,
        appId: str,
        forward: bool,
        pageSize: int,
        requestingUserEmailAddress: str,
        workplaceId: str,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all submissions from the specified connector.

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

    def get_user_apps(
        self,
        emailAddress: str,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Fetches applications associated with a specific user from the specified connector.

        Args:
            emailAddress: The ID of the user. (required)
            workplaceId: The ID of the workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workplace_apps(
        self,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of applications available in the workplace through the specified connector.

        Args:
            workplaceId: The ID of the workplace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workplace_users(
        self,
        token: str,
        workplaceId: str,
        pageSize: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of users from the workplace using the specified connector.

        Args:
            token: Authentication token. (required)
            workplaceId: The ID of the workplace. (required)
            pageSize: Number of records per page.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_submission(
        self,
        appId: str,
        data: Dict[str, Any],
        requestingUserEmailAddress: str,
        submissionId: str,
        workplaceId: str,
    ) -> Dict[str, Any]:
        """Updates the details of a submission in the specified connector.

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

