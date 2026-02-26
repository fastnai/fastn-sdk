"""Fastn Zendesk connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ZendeskConnector:
    """Zendesk connector ().

    Provides 10 tools.
    """

    def create_ticket(
        self,
        ticket: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new ticket in the system to initiate a support request for a user.

        Args:
            ticket: Details of the Zendesk ticket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_ticket(
        self,
        ticketId: str,
    ) -> Dict[str, Any]:
        """Deletes a ticket from the system, removing it permanently from the ticket records.

        Args:
            ticketId: ID of the Zendesk ticket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_groups(
        self,
        exclude_deleted: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches groups within the ticketing system to manage user permissions and access.

        Args:
            exclude_deleted: Specifies whether to exclude deleted records from the results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_ticket(
        self,
        ticketId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific ticket in the system.

        Args:
            ticketId: The ID of the Zendesk ticket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_ticket_audits(
        self,
        ticketId: str,
    ) -> Dict[str, Any]:
        """Obtains audit history for a specific ticket in the system to track changes and updates.

        Args:
            ticketId: The ID of the Zendesk ticket. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_ticket_comments(
        self,
        include: Optional[str] = None,
        include_inline_images: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches comments associated with a specific ticket in the system to view user interactions.

        Args:
            include: Specifies which fields to include in the response.
            include_inline_images: Specifies whether to include inline images in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_ticket_fields(
        self,
        creator: Optional[str] = None,
        locale: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves configurable fields for tickets in the system to understand the data structure.

        Args:
            creator: The creator of the request.
            locale: The locale for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def list_search(
        self,
        query: str,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for specific entries within the ticket system to help locate tickets based on criteria.

        Args:
            query: Search query for filtering Zendesk data. (required)
            sort_by: Field to sort the results by.
            sort_order: Order of sorting (e.g., asc, desc).
        Returns:
            API response as a dictionary.
        """
        ...

    def list_tickets(
        self,
        external_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all tickets in the system, providing an overview of current support requests.

        Args:
            external_id: External ID for the Zendesk resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_ticket(
        self,
        ticket: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing ticket in the system, allowing changes to its details or status.

        Args:
            ticket: Details for updating the Zendesk ticket.
        Returns:
            API response as a dictionary.
        """
        ...

