"""Fastn Fathom connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FathomConnector:
    """Fathom connector ().

    Provides 7 tools.
    """

    def create_webhook_fathom(
        self,
        destination_url: Optional[str] = None,
        include_action_items: Optional[bool] = None,
        include_crm_matches: Optional[bool] = None,
        include_summary: Optional[bool] = None,
        include_transcript: Optional[bool] = None,
        triggered_for: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook in Fathom to listen for specific events related to meeting recordings or summaries.

        Args:
            destination_url: 
            include_action_items: 
            include_crm_matches: 
            include_summary: 
            include_transcript: 
            triggered_for: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook_fathom(
        self,
        id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing webhook in Fathom that is no longer needed for meeting event tracking.

        Args:
            id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_recording_summary_fathom(
        self,
        destination_url: str,
    ) -> Dict[str, Any]:
        """Retrieves a summary of a specific recording from Fathom, providing concise insights and action items from the meeting.

        Args:
            destination_url: The destination URL to be used or tracked by the Fathom endpoint (the target URL for the operation). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_recording_transcript_fathom(
        self,
        destination_url: str,
    ) -> Dict[str, Any]:
        """Fetches the full transcript of a specific meeting recording from Fathom for detailed review or reference.

        Args:
            destination_url: The destination URL to be tracked or processed by Fathom. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def list_meetings_fathom(
        self,
        calendar_invitees_domains: Optional[str] = None,
        calendar_invitees_domains_type: Optional[str] = None,
        created_after: Optional[str] = None,
        created_before: Optional[str] = None,
        cursor: Optional[str] = None,
        include_action_items: Optional[str] = None,
        include_crm_matches: Optional[str] = None,
        include_summary: Optional[str] = None,
        include_transcript: Optional[str] = None,
        recorded_by: Optional[str] = None,
        teams: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all meetings recorded by Fathom, providing an overview of past discussions and key topics covered.

        Args:
            calendar_invitees_domains: Comma-separated list of invitee email domains to filter calendar invitees.
            calendar_invitees_domains_type: Type of domain filter to apply for calendar invitees (e.g., include or exclude).
            created_after: Only include records created after this ISO 8601 timestamp.
            created_before: Only include records created before this ISO 8601 timestamp.
            cursor: Pagination cursor for retrieving the next page of results.
            include_action_items: Whether to include action items in the response. Use 'true' or 'false'.
            include_crm_matches: Whether to include CRM match information. Use 'true' or 'false'.
            include_summary: Whether to include a summary in the response. Use 'true' or 'false'.
            include_transcript: Whether to include a transcript in the response. Use 'true' or 'false'.
            recorded_by: Filter results by the identifier of the user who recorded the session.
            teams: Comma-separated list or identifier of teams to filter results by.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_team_members_fathom(
        self,
        cursor: Optional[str] = None,
        team: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of team members associated with Fathom, enabling management of participants in meetings.

        Args:
            cursor: 
            team: 
        Returns:
            API response as a dictionary.
        """
        ...

    def list_teams_fathom(
        self,
        cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all teams registered in Fathom, offering an organized view of collaborative groups within the meeting assistant.

        Args:
            cursor: 
        Returns:
            API response as a dictionary.
        """
        ...

