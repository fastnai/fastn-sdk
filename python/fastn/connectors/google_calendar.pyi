"""Fastn Google Calendar connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class GoogleCalendarConnector:
    """Google Calendar connector ().

    Provides 2 tools.
    """

    def create_meeting(
        self,
    ) -> Dict[str, Any]:
        """Creates a new meeting in the specified calendar system using the createMeeting connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_events(
        self,
        alwaysIncludeEmail: Optional[str] = None,
        iCalUID: Optional[str] = None,
        maxResults: Optional[str] = None,
        orderBy: Optional[str] = None,
        pageToken: Optional[str] = None,
        q: Optional[str] = None,
        showDeleted: Optional[str] = None,
        showHiddenInvitations: Optional[str] = None,
        singleEvents: Optional[str] = None,
        timeMax: Optional[str] = None,
        timeMin: Optional[str] = None,
        timeZone: Optional[str] = None,
        updatedMin: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves events from the specified calendar system using the getEvents connector.

        Args:
            alwaysIncludeEmail: 
            iCalUID: 
            maxResults: 
            orderBy: 
            pageToken: 
            q: 
            showDeleted: 
            showHiddenInvitations: 
            singleEvents: 
            timeMax: 
            timeMin: 
            timeZone: 
            updatedMin: 
        Returns:
            API response as a dictionary.
        """
        ...

