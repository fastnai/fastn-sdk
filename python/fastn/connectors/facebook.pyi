"""Fastn Facebook connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class FacebookConnector:
    """Facebook connector ().

    Provides 16 tools.
    """

    def change_business_user_role(
        self,
        role: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Changes the role of a user within the business account in the specified system.

        Args:
            role: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_business_account(
        self,
        name: Optional[str] = None,
        primary_page: Optional[str] = None,
        timezone_id: Optional[str] = None,
        vertical: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new business account in the specified system.

        Args:
            name: 
            primary_page: 
            timezone_id: 
            vertical: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_access_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a new access token for authentication in the specified system.

        Args:
            client_id: 
            client_secret: 
            code: 
            redirect_uri: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_business_account(
        self,
        businessAccountId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a specific business account from the system.

        Args:
            businessAccountId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_business_invoices(
        self,
        end_date: Optional[str] = None,
        start_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all invoices related to the business account in the specified system.

        Args:
            end_date: 
            start_date: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_business_users(
        self,
        businessAccountId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of users associated with the business account in the specified system.

        Args:
            businessAccountId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_campaign_level_invoicing(
        self,
        end_date: Optional[str] = None,
        fields: Optional[str] = None,
        start_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches invoicing information at the campaign level from the specified system.

        Args:
            end_date: 
            fields: 
            start_date: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_lead_info(
        self,
        leadgenId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific lead in the system.

        Args:
            leadgenId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_leads_from_form(
        self,
        fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets lead information submitted through a form in the specified system.

        Args:
            fields: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_my_business_accounts(
        self,
    ) -> Dict[str, Any]:
        """Fetches all business accounts associated with the user from the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_pending_invite_users(
        self,
        businessAccountId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets a list of users who have pending invitations to join the business account in the system.

        Args:
            businessAccountId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_system_users(
        self,
        businessAccountId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the system users from the specified system.

        Args:
            businessAccountId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def invite_people(
        self,
        email: Optional[str] = None,
        role: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Invites individuals to join the business account in the system.

        Args:
            email: 
            role: 
        Returns:
            API response as a dictionary.
        """
        ...

    def refresh_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        fb_exchange_token: Optional[str] = None,
        set_token_expires_in_60_days: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Refreshes the authorization token in the specified system.

        Args:
            client_id: 
            client_secret: 
            fb_exchange_token: 
            set_token_expires_in_60_days: 
        Returns:
            API response as a dictionary.
        """
        ...

    def remove_pending_user_invite(
        self,
        businessUserId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Removes a pending user invite from the business account in the specified system.

        Args:
            businessUserId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_business_account(
        self,
        name: Optional[str] = None,
        primary_page: Optional[str] = None,
        timezone_id: Optional[str] = None,
        vertical: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the information of an existing business account in the specified system.

        Args:
            name: 
            primary_page: 
            timezone_id: 
            vertical: 
        Returns:
            API response as a dictionary.
        """
        ...

