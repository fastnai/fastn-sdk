"""Fastn Facebook connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class FacebookConnector:
    """Facebook connector ().

    Provides 16 tools.
    """

    def facebook_change_business_user_role(
        self,
        businessUserId: Optional[str] = None,
        role: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the role of an existing user within a Facebook business account. Use this when you need to promote or demote a users permissions (e.g., from Employee to Admin). Do not use this to invite new users — use facebook_invite_people instead. This operation modifies user permissions and takes effect immediately.

        Args:
            businessUserId: 
            role: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_create_business_account(
        self,
        name: Optional[str] = None,
        primary_page: Optional[str] = None,
        timezone_id: Optional[str] = None,
        userId: Optional[str] = None,
        vertical: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Facebook business account under the specified user. Use this when onboarding a new business entity that does not yet have a Facebook Business account. Do not use this to update an existing business account — use facebook_update_business_account instead. This action is partially irreversible: the business account will persist and must be explicitly deleted if no longer needed.

        Args:
            name: 
            primary_page: 
            timezone_id: 
            userId: 
            vertical: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_get_access_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Exchanges an authorization code or credentials for a new Facebook OAuth access token. Use this during the initial authentication flow to obtain an access token required for subsequent API calls. Do not use this to renew an existing token — use facebook_refresh_token instead. This operation does not modify any user or business data.

        Args:
            client_id: 
            client_secret: 
            code: 
            redirect_uri: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_get_business_account(
        self,
        businessAccountId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single Facebook business account by its ID. Use this when you need metadata such as name, timezone, currency, or verification status for a specific business. Do not use this to list all accessible business accounts — use facebook_list_my_business_accounts instead. This is a read-only operation with no side effects.

        Args:
            businessAccountId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_get_campaign_level_invoicing(
        self,
        businessAccountId: Optional[str] = None,
        end_date: Optional[str] = None,
        fields: Optional[str] = None,
        start_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves invoicing details broken down at the campaign level for a specific Facebook business account. Use this when you need to analyze ad spend or billing data per campaign. Do not use this if you only need a general summary of business invoices — use facebook_list_business_invoices instead. This is a read-only operation with no side effects.

        Args:
            businessAccountId: 
            end_date: 
            fields: 
            start_date: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_get_lead_info(
        self,
        leadgenId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a single Facebook lead by its leadgen ID. Use this when you have a specific lead ID and need to inspect its submitted field values. Do not use this to retrieve all leads from a form — use facebook_list_leads_from_form instead. This is a read-only operation with no side effects.

        Args:
            leadgenId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_invite_people(
        self,
        businessAccountId: Optional[str] = None,
        email: Optional[str] = None,
        role: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Sends an invitation to one or more individuals to join a Facebook business account. Use this to grant new users access to the business. Do not use this to change the role of an already-existing user — use facebook_change_business_user_role instead. This action creates a pending invite and sends a notification to the invitee.

        Args:
            businessAccountId: 
            email: 
            role: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_list_business_invoices(
        self,
        businessAccountId: Optional[str] = None,
        end_date: Optional[str] = None,
        start_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all invoices associated with a Facebook business account. Use this when you need a full list of billing records for a given business account ID. Do not use this for campaign-level invoice breakdowns — use facebook_get_campaign_level_invoicing instead. This is a read-only operation with no side effects.

        Args:
            businessAccountId: 
            end_date: 
            start_date: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_list_business_users(
        self,
        businessAccountId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all human users associated with a Facebook business account. Use this to review who has access to a business and their roles. Do not use this for system (automated) users — use facebook_list_system_users instead, or for pending invitees use facebook_list_pending_invite_users. This is a read-only operation with no side effects.

        Args:
            businessAccountId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_list_leads_from_form(
        self,
        fields: Optional[str] = None,
        formId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all leads submitted through a specific Facebook Lead Ad form. Use this when you need to retrieve lead data (e.g., name, email, phone) collected via a Facebook form identified by its formId. Do not use this to retrieve a single lead by ID — use facebook_get_lead_info instead. This is a read-only operation with no side effects.

        Args:
            fields: 
            formId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_list_my_business_accounts(
        self,
    ) -> Dict[str, Any]:
        """Lists all Facebook business accounts associated with the authenticated user. Use this to discover which business accounts the current user has access to. Do not use this to retrieve details of a single specific business account — use facebook_get_business_account instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_list_pending_invite_users(
        self,
        businessAccountId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all users with pending invitations to join a Facebook business account. Use this to audit outstanding invites that have not yet been accepted. Do not use this to list active business users — use facebook_list_business_users instead. This is a read-only operation with no side effects.

        Args:
            businessAccountId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_list_system_users(
        self,
        businessAccountId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all system users associated with a Facebook business account. System users are non-human accounts used for automated API access. Use this when you need to audit or manage programmatic access credentials linked to a business. Do not use this to list human business users — use facebook_list_business_users instead. This is a read-only operation with no side effects.

        Args:
            businessAccountId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_refresh_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        fb_exchange_token: Optional[str] = None,
        set_token_expires_in_60_days: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Refreshes an existing Facebook OAuth access token to extend its validity. Use this when the current access token is near expiry and you need a new one without repeating the full authentication flow. Do not use this to obtain a first-time token — use facebook_get_access_token instead. This operation does not modify any user or business data.

        Args:
            client_id: 
            client_secret: 
            fb_exchange_token: 
            set_token_expires_in_60_days: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_remove_pending_user_invite(
        self,
        businessUserId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a pending user invitation from a Facebook business account. Use this when a previously sent invite should be cancelled before the recipient accepts it. Do not use this to remove an already-accepted business user — use a user role or access management tool instead. This action is irreversible: the invite cannot be restored after deletion.

        Args:
            businessUserId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def facebook_update_business_account(
        self,
        businessAccountId: Optional[str] = None,
        name: Optional[str] = None,
        primary_page: Optional[str] = None,
        timezone_id: Optional[str] = None,
        vertical: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing Facebook business account, such as its name, address, or other profile fields. Use this when you need to modify metadata on an existing business account. Do not use this to create a new business account — use facebook_create_business_account instead. Changes take effect immediately.

        Args:
            businessAccountId: 
            name: 
            primary_page: 
            timezone_id: 
            vertical: 
        Returns:
            API response as a dictionary.
        """
        ...

