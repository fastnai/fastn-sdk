"""Fastn Freshdesk connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class FreshdeskConnector:
    """Freshdesk connector ().

    Provides 6 tools.
    """

    def freshdesk_create_ticket(
        self,
        cc_emails: Optional[List[Any]] = None,
        description: Optional[str] = None,
        email: Optional[str] = None,
        priority: Optional[str] = None,
        status: Optional[str] = None,
        subject: Optional[str] = None,
        tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new support ticket in Freshdesk with details such as subject, description, requester, status, priority, and assignee. Use this when a new customer issue or request needs to be logged. Do not use this to update an existing ticket — use freshdesk_update_ticket instead. Creating a ticket triggers notifications to the assigned agent and requester if configured.

        Args:
            cc_emails: 
            description: 
            email: 
            priority: 
            status: 
            subject: 
            tags: 
        Returns:
            API response as a dictionary.
        """
        ...

    def freshdesk_delete_ticket(
        self,
        ticket_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a Freshdesk support ticket identified by its ticket ID. Use this only when a ticket must be fully removed from the system. This action is irreversible — the ticket and all its associated data cannot be recovered after deletion. Do not use this to close or resolve a ticket — use freshdesk_update_ticket to change ticket status instead.

        Args:
            ticket_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def freshdesk_get_ticket(
        self,
        ticket_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single Freshdesk support ticket by its ticket ID, including status, priority, requester, description, and custom fields. Use this when you have a specific ticket ID and need complete ticket information. Do not use this to search for tickets by criteria — use freshdesk_search_tickets or freshdesk_list_tickets instead.

        Args:
            ticket_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def freshdesk_list_tickets(
        self,
        company_id: Optional[str] = None,
        email: Optional[str] = None,
        filter: Optional[str] = None,
        include: Optional[str] = None,
        order_by: Optional[str] = None,
        order_type: Optional[str] = None,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
        requester_id: Optional[str] = None,
        updated_since: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a paginated list of all support tickets in Freshdesk. Use this to browse or enumerate tickets without specific filter criteria. Do not use this when you need to search by specific field values — use freshdesk_search_tickets instead, or freshdesk_get_ticket when you have a specific ticket ID.

        Args:
            company_id: 
            email: 
            filter: 
            include: 
            order_by: 
            order_type: 
            page: 
            per_page: 
            requester_id: 
            updated_since: 
        Returns:
            API response as a dictionary.
        """
        ...

    def freshdesk_search_tickets(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches Freshdesk support tickets using a query string with field-based filters such as status, priority, requester, tag, or date ranges. Returns a filtered list of matching tickets. Use this when you know specific criteria to narrow results. Do not use this to retrieve all tickets without filters — use freshdesk_list_tickets instead.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

    def freshdesk_update_ticket(
        self,
        custom_fields: Optional[str] = None,
        priority: Optional[str] = None,
        status: Optional[str] = None,
        tags: Optional[List[Any]] = None,
        ticket_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields on an existing Freshdesk support ticket identified by its ticket ID. Use this to change ticket properties such as status, priority, assignee, subject, description, or custom fields. Do not use this to create a new ticket or to delete a ticket. This operation modifies the ticket in place and cannot be undone without a subsequent update.

        Args:
            custom_fields: 
            priority: 
            status: 
            tags: 
            ticket_id: 
        Returns:
            API response as a dictionary.
        """
        ...

