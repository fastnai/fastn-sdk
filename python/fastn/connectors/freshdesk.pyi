"""Fastn Freshdesk connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FreshdeskConnector:
    """Freshdesk connector ().

    Provides 6 tools.
    """

    def create_ticket(
        self,
        cc_emails: Optional[List[Any]] = None,
        description: Optional[str] = None,
        email: Optional[str] = None,
        priority: Optional[str] = None,
        status: Optional[str] = None,
        subject: Optional[str] = None,
        tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new support ticket in your ticket management system.

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

    def delete_ticket(
        self,
        ticket_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes an existing support ticket from your ticket management system.

        Args:
            ticket_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_ticket(
        self,
        ticket_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific support ticket in your ticket management system.

        Args:
            ticket_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def list_tickets(
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
        """Lists all support tickets within your ticket management system.

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

    def search_tickets(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for support tickets based on specified criteria in your ticket management system.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_ticket(
        self,
        custom_fields: Optional[str] = None,
        priority: Optional[str] = None,
        status: Optional[str] = None,
        tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Updates the information of an existing support ticket in your ticket management system.

        Args:
            custom_fields: 
            priority: 
            status: 
            tags: 
        Returns:
            API response as a dictionary.
        """
        ...

