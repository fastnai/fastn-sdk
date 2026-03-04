"""Fastn Keap connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class KeapConnector:
    """Keap connector ().

    Provides 11 tools.
    """

    def keap_create_appointment(
        self,
        end_date: str,
        start_date: str,
        title: str,
        contact_id: Optional[int] = None,
        description: Optional[str] = None,
        location: Optional[str] = None,
        remind_time: Optional[int] = None,
        user: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new appointment in Keap CRM. Use this tool when you need to schedule a new appointment for a contact or user. Do not use this tool to modify an existing appointment; use keap_update_appointment instead. Note: creating an appointment may trigger associated Keap automation workflows.

        Args:
            end_date: The end date for the event. (required)
            start_date: The start date for the event. (required)
            title: The title of the event. (required)
            contact_id: The ID of the contact associated with the event.
            description: A description of the event.
            location: The location of the event.
            remind_time: The time before the event to send a reminder (in minutes).
            user: The ID of the user associated with the event.
        Returns:
            API response as a dictionary.
        """
        ...

    def keap_create_contact(
        self,
        email_addresses: List[Any],
        addresses: Optional[List[Any]] = None,
        family_name: Optional[str] = None,
        given_name: Optional[str] = None,
        job_title: Optional[str] = None,
        opt_in_reason: Optional[str] = None,
        phone_numbers: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact record in Keap CRM. Use this tool when you need to add a new individual to your CRM database. Do not use this tool to update an existing contact; use keap_update_contact instead. Note: creating a contact may trigger associated Keap automation workflows or sequences.

        Args:
            email_addresses:  (required)
            addresses: 
            family_name: Contact's family name.
            given_name: Contact's given name.
            job_title: Contact's job title.
            opt_in_reason: Reason for contact opt-in.
            phone_numbers: 
        Returns:
            API response as a dictionary.
        """
        ...

    def keap_delete_appointment(
        self,
        appointmentId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific appointment from Keap CRM, identified by its appointment ID. Use this tool when an appointment must be removed entirely. Do not use this tool to reschedule or modify an appointment; use keap_update_appointment instead. Warning: this action is irreversible and cannot be undone.

        Args:
            appointmentId: ID of the appointment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def keap_delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific contact from Keap CRM, identified by their contact ID. Use this tool only when a contact record must be fully removed. Do not use this tool to update contact information; use keap_update_contact instead. Warning: this action is irreversible and will remove all data associated with that contact.

        Args:
            contactId: The ID of the contact in Keap. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def keap_get_appointment(
        self,
        appointmentId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single appointment in Keap CRM, identified by its appointment ID. Use this tool when you need the full details of one specific appointment. Do not use this tool to list multiple appointments; use keap_list_appointments instead.

        Args:
            appointmentId: The ID of the appointment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def keap_get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single contact in Keap CRM, identified by their contact ID. Use this tool when you need the full profile of one specific contact. Do not use this tool to list multiple contacts; use keap_list_contacts instead.

        Args:
            contactId: The ID of the contact in Keap. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def keap_list_affiliates(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all affiliates associated with the Keap account. Use this tool when you need to enumerate affiliates for reporting, lookup, or management purposes. Do not use this tool to retrieve details about a single affiliate.
        Returns:
            API response as a dictionary.
        """
        ...

    def keap_list_appointments(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of appointments scheduled in Keap CRM. Use this tool when you need to browse or enumerate multiple appointments. Do not use this tool to fetch details for a single appointment; use keap_get_appointment instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def keap_list_contacts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of contacts from Keap CRM. Use this tool when you need to browse or enumerate multiple contact records. Do not use this tool to fetch details for a single contact; use keap_get_contact instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def keap_list_users(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all users in the Keap account. Use this tool when you need to enumerate available users for assignment, auditing, or lookup purposes. Do not use this tool to retrieve details about a single user.
        Returns:
            API response as a dictionary.
        """
        ...

    def keap_update_appointment(
        self,
        appointmentId: str,
        contact_id: int,
        end_date: str,
        start_date: str,
        description: Optional[str] = None,
        location: Optional[str] = None,
        remind_time: Optional[int] = None,
        title: Optional[str] = None,
        user: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing appointment in Keap CRM, identified by its appointment ID. Use this tool to modify appointment fields such as date, time, title, or participants. Do not use this tool to create a new appointment; use keap_create_appointment instead.

        Args:
            appointmentId: The ID of the appointment (for update operations). (required)
            contact_id: The Keap ID of the contact associated with the appointment. (required)
            end_date: The end date and time of the appointment (ISO 8601 format). (required)
            start_date: The start date and time of the appointment (ISO 8601 format). (required)
            description: A description of the appointment.
            location: The location of the appointment.
            remind_time: The reminder time in minutes before the appointment.
            title: The title of the appointment.
            user: The Keap ID of the user associated with the appointment.
        Returns:
            API response as a dictionary.
        """
        ...

