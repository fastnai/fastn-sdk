"""Fastn Fathom connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class FathomConnector:
    """Fathom connector ().

    Provides 7 tools.
    """

    def fathom_create_webhook(
        self,
        destination_url: Optional[str] = None,
        include_action_items: Optional[bool] = None,
        include_crm_matches: Optional[bool] = None,
        include_summary: Optional[bool] = None,
        include_transcript: Optional[bool] = None,
        triggered_for: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new webhook subscription in Fathom that sends real-time HTTP POST notifications to a specified URL when meeting events occur (e.g., meeting recorded, transcript ready). Use this tool to integrate Fathom event triggers into external systems or workflows. Each call creates a new subscription, so avoid calling it multiple times with the same endpoint to prevent duplicate notifications. Do not use this tool to update an existing webhook; delete and recreate it instead.

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

    def fathom_delete_webhook(
        self,
        id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing Fathom webhook subscription identified by its webhook ID, stopping all future event notifications to the registered endpoint. This action is irreversible — the webhook cannot be restored after deletion and must be recreated if needed. Use this tool when decommissioning an integration or rotating webhook endpoints. Do not use this tool if you only want to temporarily pause notifications.

        Args:
            id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fathom_get_recording_summary(
        self,
        destination_url: str,
        id: str,
    ) -> Dict[str, Any]:
        """Returns the AI-generated summary of a specific Fathom meeting recording, identified by its recording ID. The summary includes key topics, decisions, and action items extracted from the meeting. Use this tool when you need a condensed overview rather than the full transcript. Do not use this tool to retrieve the verbatim conversation; use fathom_get_recording_transcript for that purpose.

        Args:
            destination_url: The destination URL to be used or tracked by the Fathom endpoint (the target URL for the operation). (required)
            id: The unique identifier of the URL resource in Fathom. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def fathom_get_recording_transcript(
        self,
        destination_url: str,
        id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns the full text transcript of a specific Fathom meeting recording, identified by its recording ID. Use this tool when you need the verbatim conversation from a meeting. Do not use this tool to retrieve a high-level summary or action items; use fathom_get_recording_summary for that purpose.

        Args:
            destination_url: The destination URL to be tracked or processed by Fathom. (required)
            id: Identifier for a URL resource (for example, a site or tracked URL ID).
        Returns:
            API response as a dictionary.
        """
        ...

    def fathom_list_meetings(
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
        """Returns a paginated list of all meetings recorded by Fathom for the authenticated account. Use this tool to browse or search past meetings and obtain meeting or recording IDs needed to fetch transcripts or summaries. Do not use this tool to retrieve the content of a specific meeting; use fathom_get_recording_transcript or fathom_get_recording_summary for that purpose.

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

    def fathom_list_team_members(
        self,
        cursor: Optional[str] = None,
        team: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all team members in the authenticated Fathom account. Use this tool to enumerate users and their roles within a team, for example to audit team composition or map user identities. Do not use this tool to retrieve meeting recordings or team-level information.

        Args:
            cursor: 
            team: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fathom_list_teams(
        self,
        cursor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a paginated list of all teams in the authenticated Fathom account. Use this tool to discover team IDs and organizational structure for downstream operations such as listing team members. Do not use this tool to retrieve meeting data or individual team details.

        Args:
            cursor: 
        Returns:
            API response as a dictionary.
        """
        ...

