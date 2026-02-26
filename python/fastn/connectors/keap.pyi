"""Fastn Keap connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class KeapConnector:
    """Keap connector ().

    Provides 11 tools.
    """

    def create_appointment(
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
        """Creates a new appointment in the system.

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

    def create_contact(
        self,
        email_addresses: List[Any],
        addresses: Optional[List[Any]] = None,
        family_name: Optional[str] = None,
        given_name: Optional[str] = None,
        job_title: Optional[str] = None,
        opt_in_reason: Optional[str] = None,
        phone_numbers: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact in the system.

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

    def delete_appointment(
        self,
        appointmentId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing appointment from the system.

        Args:
            appointmentId: ID of the appointment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing contact from the system.

        Args:
            contactId: The ID of the contact in Keap. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_affiliates(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of affiliates associated with the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_appointment(
        self,
        appointmentId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific appointment in the system.

        Args:
            appointmentId: The ID of the appointment. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_appointments(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of appointments scheduled in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific contact in the system.

        Args:
            contactId: The ID of the contact in Keap. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of contacts from the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users_(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of users from the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_appointment(
        self,
        contact_id: int,
        end_date: str,
        start_date: str,
        description: Optional[str] = None,
        location: Optional[str] = None,
        remind_time: Optional[int] = None,
        title: Optional[str] = None,
        user: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates an existing appointment in the system.

        Args:
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

