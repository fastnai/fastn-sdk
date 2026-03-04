"""Fastn Google Calendar connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _GoogleCalendarCreateCalendarConferenceproperties(TypedDict, total=False):
    allowedConferenceSolutionTypes: List[Any]

class _GoogleCalendarCreateEventBirthdayproperties(TypedDict, total=False):
    contact: str
    customTypeName: str
    type: str

class _GoogleCalendarCreateEventConferencedata(TypedDict, total=False):
    conferenceId: str
    conferenceSolution: Dict[str, Any]
    createRequest: Dict[str, Any]
    entryPoints: List[Any]
    notes: str
    parameters: Dict[str, Any]
    signature: str

class _GoogleCalendarCreateEventCreator(TypedDict, total=False):
    displayName: str
    email: str
    id: str
    self: bool

class _GoogleCalendarCreateEventEnd(TypedDict, total=False):
    date: str
    dateTime: str
    timeZone: str

class _GoogleCalendarCreateEventExtendedproperties(TypedDict, total=False):
    private: Dict[str, Any]
    shared: Dict[str, Any]

class _GoogleCalendarCreateEventFocustimeproperties(TypedDict, total=False):
    autoDeclineMode: str
    chatStatus: str
    declineMessage: str

class _GoogleCalendarCreateEventGadget(TypedDict, total=False):
    display: str
    height: int
    iconLink: str
    link: str
    preferences: Dict[str, Any]
    title: str
    type: str
    width: int

class _GoogleCalendarCreateEventOrganizer(TypedDict, total=False):
    displayName: str
    email: str
    id: str
    self: bool

class _GoogleCalendarCreateEventOriginalstarttime(TypedDict, total=False):
    date: str
    dateTime: str
    timeZone: str

class _GoogleCalendarCreateEventOutofofficeproperties(TypedDict, total=False):
    autoDeclineMode: str
    declineMessage: str

class _GoogleCalendarCreateEventReminders(TypedDict, total=False):
    overrides: List[Any]
    useDefault: bool

class _GoogleCalendarCreateEventSource(TypedDict, total=False):
    title: str
    url: str

class _GoogleCalendarCreateEventStart(TypedDict, total=False):
    date: str
    dateTime: str
    timeZone: str

class _GoogleCalendarCreateEventWorkinglocationproperties(TypedDict, total=False):
    customLocation: Dict[str, Any]
    officeLocation: Dict[str, Any]
    type: str

class GoogleCalendarConnector:
    """Google Calendar connector ().

    Provides 9 tools.
    """

    def google_calendar_create_calendar(
        self,
        summary: str,
        alt: Optional[str] = None,
        conferenceProperties: Optional[_GoogleCalendarCreateCalendarConferenceproperties] = None,
        description: Optional[str] = None,
        etag: Optional[str] = None,
        fields: Optional[str] = None,
        id: Optional[str] = None,
        kind: Optional[str] = None,
        location: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        timeZone: Optional[str] = None,
        userIp: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new secondary calendar in the authenticated users Google Calendar account, allowing events and reminders to be organized in a separate, dedicated timeline. Use this when you need to set up a distinct calendar for a specific project, team, or purpose. Do not use this to add events to an existing calendar; use google_calendar_create_event instead. Calendar creation is permanent and cannot be undone without separately deleting the calendar.

        Args:
            summary: The summary or title of the event. (required)
            alt: Data format for the response.
            conferenceProperties: Conference properties for the event.
            description: A more detailed description of the event.
            etag: Version tag for the event.
            fields: Specifies fields to include in a partial response.
            id: Unique identifier of the event.
            kind: Type of the resource.
            location: Location of the event.
            prettyPrint: Returns response in a human-readable format.
            quotaUser: An opaque string that represents a user for quota purposes.
            timeZone: Time zone of the event.
            userIp: IP address of the site where the request originates.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_calendar_create_event(
        self,
        headers: Dict[str, Any],
        anyoneCanAddSelf: Optional[bool] = None,
        attachments: Optional[List[Any]] = None,
        attendees: Optional[List[Any]] = None,
        attendeesOmitted: Optional[bool] = None,
        birthdayProperties: Optional[_GoogleCalendarCreateEventBirthdayproperties] = None,
        colorId: Optional[str] = None,
        conferenceData: Optional[_GoogleCalendarCreateEventConferencedata] = None,
        conferenceDataVersion: Optional[str] = None,
        created: Optional[str] = None,
        creator: Optional[_GoogleCalendarCreateEventCreator] = None,
        description: Optional[str] = None,
        end: Optional[_GoogleCalendarCreateEventEnd] = None,
        endTimeUnspecified: Optional[bool] = None,
        etag: Optional[str] = None,
        eventType: Optional[str] = None,
        extendedProperties: Optional[_GoogleCalendarCreateEventExtendedproperties] = None,
        focusTimeProperties: Optional[_GoogleCalendarCreateEventFocustimeproperties] = None,
        gadget: Optional[_GoogleCalendarCreateEventGadget] = None,
        guestsCanInviteOthers: Optional[bool] = None,
        guestsCanModify: Optional[bool] = None,
        guestsCanSeeOtherGuests: Optional[bool] = None,
        hangoutLink: Optional[str] = None,
        htmlLink: Optional[str] = None,
        iCalUID: Optional[str] = None,
        id: Optional[str] = None,
        key: Optional[str] = None,
        kind: Optional[str] = None,
        location: Optional[str] = None,
        locked: Optional[bool] = None,
        maxAttendees: Optional[str] = None,
        organizer: Optional[_GoogleCalendarCreateEventOrganizer] = None,
        originalStartTime: Optional[_GoogleCalendarCreateEventOriginalstarttime] = None,
        outOfOfficeProperties: Optional[_GoogleCalendarCreateEventOutofofficeproperties] = None,
        privateCopy: Optional[bool] = None,
        recurrence: Optional[List[Any]] = None,
        recurringEventId: Optional[str] = None,
        reminders: Optional[_GoogleCalendarCreateEventReminders] = None,
        sendNotifications: Optional[str] = None,
        sendUpdates: Optional[str] = None,
        sequence: Optional[int] = None,
        source: Optional[_GoogleCalendarCreateEventSource] = None,
        start: Optional[_GoogleCalendarCreateEventStart] = None,
        status: Optional[str] = None,
        summary: Optional[str] = None,
        supportsAttachments: Optional[str] = None,
        transparency: Optional[str] = None,
        updated: Optional[str] = None,
        visibility: Optional[str] = None,
        workingLocationProperties: Optional[_GoogleCalendarCreateEventWorkinglocationproperties] = None,
    ) -> Dict[str, Any]:
        """Creates a new event or meeting in Google Calendar with specified details such as title, start and end time, participants, and location. Use this when you need to schedule a new calendar event, add a meeting to the calendar, or create a reminder for a specific date and time. Do not use this to retrieve events; use google_calendar_list_events instead. The created event is immediately saved and synced across all connected devices and cannot be undone without manually deleting the event.

        Args:
            headers: Headers for the Google Meet API call. (required)
            anyoneCanAddSelf: Whether anyone can add themselves to the meeting.
            attachments: Attachments for the Google Meet event.
            attendees: Attendees of the Google Meet event.
            attendeesOmitted: Whether attendees are omitted.
            birthdayProperties: Birthday properties of the event.
            colorId: Color ID for the event.
            conferenceData: Conference data for the Google Meet event.
            conferenceDataVersion: Version of the conference data.
            created: Creation time of the event.
            creator: Creator of the event.
            description: Description of the Google Meet event.
            end: End time of the Google Meet event.
            endTimeUnspecified: Whether the end time is unspecified.
            etag: ETag for the event.
            eventType: Type of event.
            extendedProperties: Extended properties of the event.
            focusTimeProperties: Focus time properties of the event.
            gadget: Gadget properties for the event.
            guestsCanInviteOthers: Whether guests can invite others.
            guestsCanModify: Whether guests can modify the event.
            guestsCanSeeOtherGuests: Whether guests can see other guests.
            hangoutLink: Hangout link for the event.
            htmlLink: HTML link for the event.
            iCalUID: iCal UID for the event.
            id: ID of the Google Meet event.
            key: Key for identifying the conference.
            kind: Kind of the event.
            location: Location of the Google Meet event.
            locked: Whether the event is locked.
            maxAttendees: Maximum number of attendees allowed.
            organizer: Organizer of the event.
            originalStartTime: Original start time of the event.
            outOfOfficeProperties: Out of office properties of the event.
            privateCopy: Whether the event is a private copy.
            recurrence: Recurrence rules for the event.
            recurringEventId: ID of the recurring event.
            reminders: Reminders for the event.
            sendNotifications: Whether to send notifications.
            sendUpdates: Whether to send updates.
            sequence: Sequence number of the event.
            source: Source of the event.
            start: Start time of the Google Meet event.
            status: Status of the event.
            summary: Summary of the Google Meet event.
            supportsAttachments: Whether the conference supports attachments.
            transparency: Transparency of the event.
            updated: Last updated time of the event.
            visibility: Visibility of the event.
            workingLocationProperties: Working location properties of the event.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_calendar_delete_event(
        self,
        eventId: str,
        alt: Optional[str] = None,
        fields: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        sendNotifications: Optional[str] = None,
        sendUpdates: Optional[str] = None,
        userIp: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specified event from Google Calendar permanently, removing it from the users schedule. This action cannot be undone. Use this when you need to remove a single event by its event ID. Do not use this to archive or hide events; modify the event instead if you need to change rather than delete it.

        Args:
            eventId: The ID of the event to delete. (required)
            alt: Data format for the response.
            fields: Comma-separated list of fields to include in the response.
            prettyPrint: Specifies whether to format the response.
            quotaUser: An opaque string identifying the user making the request.
            sendNotifications: Whether to send notifications to event attendees upon deletion.
            sendUpdates: Specifies whether to send updates about the deleted event.
            userIp: IP address of the site where the request originates.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_calendar_get_access_rule(
        self,
        ruleId: str,
        alt: Optional[str] = None,
        fields: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        userIp: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific access rule for Google Calendar, detailing permissions granted to users or groups for calendar access. Use this when you need to fetch details about a single access rule by its ID. To retrieve all access rules for the calendar, use google_calendar_list_access_rules instead.

        Args:
            ruleId: The ID of the access rule to retrieve. (required)
            alt: Data format for the response.
            fields: Specifies fields to include in a partial response.
            prettyPrint: Returns response with indentations and line breaks.
            quotaUser: An opaque string that should be sent to the server in the `x-goog-quota-user` header.
            userIp: IP address of the site where the request originates.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_calendar_get_calendar(
        self,
        calendarId: str,
        alt: Optional[str] = None,
        fields: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        userIp: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the resource metadata and configuration settings for a specific Google Calendar by its calendar ID, including its name, description, time zone, and access settings. Use this when you need the full details of a single known calendar. Do not use this to list all calendars associated with the account; use google_calendar_list_calendars instead. Do not use this to retrieve events within the calendar; use google_calendar_list_events instead.

        Args:
            calendarId: The ID of the calendar to retrieve. (required)
            alt: Specifies the format of the response data.
            fields: Specifies which fields to include in the response.
            prettyPrint: Specifies whether the response should be formatted for readability.
            quotaUser: An opaque string that should be sent to the server alongside the request.
            userIp: The IP address of the end user.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_calendar_get_event(
        self,
        eventId: str,
        alt: Optional[str] = None,
        alwaysIncludeEmail: Optional[str] = None,
        fields: Optional[str] = None,
        maxAttendees: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        timeZone: Optional[str] = None,
        userIp: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific event in Google Calendar, including its description, participants, and timings. Use this when you have a specific event ID and need its full details. To retrieve all events from the calendar, use google_calendar_list_events instead.

        Args:
            eventId: The unique identifier for the event. (required)
            alt: Data format of the response (e.g., json).
            alwaysIncludeEmail: Whether to always include the email address of the creator.
            fields: Comma-separated list of fields to include in the response.
            maxAttendees: Maximum number of attendees to include in the response.
            prettyPrint: Whether to return response in a human-readable format.
            quotaUser: An opaque string identifying the user for quota purposes.
            timeZone: Time zone for the response.
            userIp: IP address of the end user.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_calendar_list_access_rules(
        self,
        alt: Optional[str] = None,
        fields: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        userIp: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns the complete list of access control rules (ACL) for the authenticated users primary Google Calendar, detailing which users or groups have been granted view or edit permissions. Use this to audit or review all sharing and permission settings for the calendar. Do not use this to retrieve a single access rule by its ID; use google_calendar_get_access_rule instead.

        Args:
            alt: Data format for the response.
            fields: Specifies fields to include in a partial response.
            prettyPrint: Returns response in a pretty print format.
            quotaUser: An opaque string that represents a user for quota purposes.
            userIp: IP address of the site where the request originates. Use this if you want to enforce per-user limits.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_calendar_list_calendars(
        self,
        alt: Optional[str] = None,
        fields: Optional[str] = None,
        key: Optional[str] = None,
        maxResults: Optional[str] = None,
        minAccessRole: Optional[str] = None,
        pageToken: Optional[str] = None,
        prettyPrint: Optional[str] = None,
        quotaUser: Optional[str] = None,
        showDeleted: Optional[str] = None,
        showHidden: Optional[str] = None,
        syncToken: Optional[str] = None,
        userIp: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns a list of all calendars in the authenticated users Google Calendar account, including their names, IDs, access roles, and display settings. Use this when you need a complete overview of all available calendars associated with the account. Do not use this to retrieve detailed information about a single specific calendar; use google_calendar_get_calendar instead.

        Args:
            alt: Data format for the response (e.g., 'json').
            fields: Specifies fields to include in a partial response.
            key: API key.  Refer to Google Calendar API documentation for details.
            maxResults: Maximum number of calendars to return.
            minAccessRole: Minimum access role for the calendars returned.
            pageToken: Token to retrieve the next page of results.
            prettyPrint: Returns response in a human-readable format.
            quotaUser: An opaque string that should be sent to the server in each request.
            showDeleted: Whether to include deleted calendars in the response.
            showHidden: Whether to include hidden calendars in the response.
            syncToken: Token for synchronization.
            userIp: IP address of the end user.
        Returns:
            API response as a dictionary.
        """
        ...

    def google_calendar_list_events(
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
        """Returns a list of events from the authenticated users primary Google Calendar, including upcoming meetings, reminders, and scheduled items, with optional filtering by time range or other parameters. Use this when you need to view scheduled events, check for upcoming meetings, or display a calendar agenda. Do not use this to retrieve the full details of a single event by ID; use google_calendar_get_event instead. Do not use this to create or modify events; use google_calendar_create_event instead.

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

