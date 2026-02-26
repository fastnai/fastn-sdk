"""Fastn Leady connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class LeadyConnector:
    """Leady connector ().

    Provides 10 tools.
    """

    def get_blacklist_resources(
        self,
        cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves resources that are currently blacklisted in the specified context of monitoring or compliance.

        Args:
            cursor: Cursor for pagination in the Leady API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_companies(
        self,
        id: str,
        secure_token: str,
    ) -> Dict[str, Any]:
        """Fetches a list of companies from the database, providing details relevant for business analytics and insights.

        Args:
            id: Unique identifier for the Leady API resource. (required)
            secure_token: Secure token for accessing the Leady API resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_magnitudes(
        self,
        country: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains different magnitudes relevant to data analytics, useful for measuring various metrics within the defined context.

        Args:
            country: Country code for the Leady Leady endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_persons(
        self,
        id: str,
        secure_token: str,
    ) -> Dict[str, Any]:
        """Retrieves data about individuals from the database, useful for profiling, recognition, or verification purposes.

        Args:
            id: Identifier for the resource in Leady Leady. (required)
            secure_token: Secure token for accessing the resource in Leady Leady. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_resource(
        self,
        resourceDomain: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific resource, including attributes and configurations, based on the provided identifier.

        Args:
            resourceDomain: The domain of the resource being accessed in Leady. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_resources(
        self,
        cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a collection of resources available in the designated context, which can be used for further processing or analysis.

        Args:
            cursor: Cursor for pagination in Leady Leady API
        Returns:
            API response as a dictionary.
        """
        ...

    def get_saved_filters(
        self,
        cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of saved filters that help in organizing and managing data sets according to specific criteria.

        Args:
            cursor: Cursor for pagination in Leady API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sessions(
        self,
        action_count_max: Optional[str] = None,
        action_count_min: Optional[str] = None,
        cursor: Optional[str] = None,
        period_end: Optional[str] = None,
        period_start: Optional[str] = None,
        saved_filter_id: Optional[str] = None,
        seconds_spent_max: Optional[str] = None,
        seconds_spent_min: Optional[str] = None,
        session_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains session details, providing insights into user interactions and engagements within the defined application.

        Args:
            action_count_max: Maximum number of actions to include in the response.
            action_count_min: Minimum number of actions to include in the response.
            cursor: Cursor for pagination.  Use the cursor from a previous response to fetch the next page of results.
            period_end: End timestamp for the time period to filter results (e.g., ISO 8601 format).
            period_start: Start timestamp for the time period to filter results (e.g., ISO 8601 format).
            saved_filter_id: ID of a saved filter to apply to the results.
            seconds_spent_max: Maximum seconds spent per action to include in the response.
            seconds_spent_min: Minimum seconds spent per action to include in the response.
            session_type: Type of session to filter results (e.g., 'web', 'mobile').
        Returns:
            API response as a dictionary.
        """
        ...

    def get_token(
        self,
        email: str,
        password: str,
    ) -> Dict[str, Any]:
        """Retrieves a token for authentication purposes, allowing access to secured endpoints and operations within the application.

        Args:
            email: The user's email address. (required)
            password: The password for authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_turnovers(
        self,
        country: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches turnover data in the relevant context of financial performance analysis, providing insights into business revenue streams.

        Args:
            country: Country filter for the Leady API Leady Endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

