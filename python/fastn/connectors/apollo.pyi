"""Fastn Apollo connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ApolloConnector:
    """Apollo connector ().

    Provides 18 tools.
    """

    def bulk_organization_enrichment(
        self,
        domains: str,
    ) -> Dict[str, Any]:
        """Performs bulk enrichment of organization data in the CRM system.

        Args:
            domains: Domains parameter for the apollo v1 endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def bulk_people_enrichment(
        self,
        reveal_personal_emails: Optional[str] = None,
        reveal_phone_number: Optional[str] = None,
        webhook_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Performs bulk enrichment of people data in the CRM system.

        Args:
            reveal_personal_emails: Whether to reveal personal emails.
            reveal_phone_number: Whether to reveal phone numbers.
            webhook_url: Webhook URL for notifications.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_account(
        self,
        account_stage_id: Optional[str] = None,
        domain: Optional[str] = None,
        name: Optional[str] = None,
        owner_id: Optional[str] = None,
        phone: Optional[str] = None,
        raw_address: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new account in the CRM system.

        Args:
            account_stage_id: ID of the account stage.
            domain: Domain name.
            name: Name of the account.
            owner_id: ID of the account owner.
            phone: Phone number.
            raw_address: Raw address string.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_contact(
        self,
        first_name: str,
        last_name: str,
        mobile_phone: str,
        organization_name: str,
        account_id: Optional[str] = None,
        contact_stage_id: Optional[str] = None,
        corporate_phone: Optional[str] = None,
        direct_phone: Optional[str] = None,
        email: Optional[str] = None,
        home_phone: Optional[str] = None,
        label_names: Optional[str] = None,
        other_phone: Optional[str] = None,
        present_raw_address: Optional[str] = None,
        title: Optional[str] = None,
        website_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact in the CRM system.

        Args:
            first_name:  (required)
            last_name:  (required)
            mobile_phone:  (required)
            organization_name:  (required)
            account_id: 
            contact_stage_id: 
            corporate_phone: 
            direct_phone: 
            email: 
            home_phone: 
            label_names: 
            other_phone: 
            present_raw_address: 
            title: 
            website_url: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_deal(
        self,
        name: str,
        account_id: Optional[str] = None,
        amount: Optional[str] = None,
        closed_date: Optional[str] = None,
        opportunity_stage_id: Optional[str] = None,
        owner_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new deal in the CRM system.

        Args:
            name:  (required)
            account_id: 
            amount: 
            closed_date: 
            opportunity_stage_id: 
            owner_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_task(
        self,
        contact_ids: str,
        due_at: str,
        priority: str,
        status: str,
        type: str,
        user_id: str,
        note: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new task in the CRM system.

        Args:
            contact_ids:  (required)
            due_at:  (required)
            priority:  (required)
            status:  (required)
            type:  (required)
            user_id:  (required)
            note: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_account(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific account in the CRM system.

        Args:
            accountId: Account ID for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contact_stages(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the various stages of contacts in the CRM system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_deal(
        self,
        dealId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific deal in the CRM system.

        Args:
            dealId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_deal_stages(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the various stages of deals in the CRM system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_deals(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
        sort_by_field: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all deals in the CRM system.

        Args:
            page: 
            per_page: 
            sort_by_field: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of users in the CRM system.

        Args:
            page: 
            per_page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def organization_enrichment(
        self,
        domain: str,
    ) -> Dict[str, Any]:
        """Enriches organization data for a specified account in the CRM system.

        Args:
            domain: Domain parameter for the apollo v1 endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def people_enrichment(
        self,
        domain: Optional[str] = None,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        hashed_email: Optional[str] = None,
        id: Optional[str] = None,
        last_name: Optional[str] = None,
        linkedin_url: Optional[str] = None,
        name: Optional[str] = None,
        organization_name: Optional[str] = None,
        reveal_personal_emails: Optional[str] = None,
        reveal_phone_number: Optional[str] = None,
        webhook_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Enriches people data for a specified contact in the CRM system.

        Args:
            domain: Domain of the user.
            email: Email address of the user.
            first_name: First name of the user.
            hashed_email: Hashed email address of the user.
            id: User ID.
            last_name: Last name of the user.
            linkedin_url: LinkedIn URL of the user.
            name: Full name of the user.
            organization_name: Name of the user's organization.
            reveal_personal_emails: Flag indicating whether to reveal personal emails.
            reveal_phone_number: Flag indicating whether to reveal phone number.
            webhook_url: Webhook URL for notifications.
        Returns:
            API response as a dictionary.
        """
        ...

    def search_accounts(
        self,
        account_stage_ids: Optional[str] = None,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
        q_organization_name: Optional[str] = None,
        sort_ascending: Optional[str] = None,
        sort_by_field: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for accounts in the CRM system based on specified criteria.

        Args:
            account_stage_ids: Comma-separated list of account stage IDs to filter by.
            page: Page number for pagination.
            per_page: Number of items per page for pagination.
            q_organization_name: Query string to filter organizations by name.
            sort_ascending: Sort results in ascending order (true/false).
            sort_by_field: Field to sort results by.
        Returns:
            API response as a dictionary.
        """
        ...

    def search_contacts(
        self,
        contact_stage_ids: Optional[str] = None,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
        q_keywords: Optional[str] = None,
        sort_ascending: Optional[str] = None,
        sort_by_field: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for contacts in the CRM system based on specified criteria.

        Args:
            contact_stage_ids: 
            page: 
            per_page: 
            q_keywords: 
            sort_ascending: 
            sort_by_field: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_account(
        self,
        account_stage_id: Optional[str] = None,
        domain: Optional[str] = None,
        name: Optional[str] = None,
        owner_id: Optional[str] = None,
        phone: Optional[str] = None,
        raw_address: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing account in the CRM system.

        Args:
            account_stage_id: ID of the account stage.
            domain: Domain name.
            name: Account name.
            owner_id: ID of the account owner.
            phone: Account phone number.
            raw_address: Raw account address.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_contact(
        self,
        account_id: Optional[str] = None,
        contact_stage_id: Optional[str] = None,
        corporate_phone: Optional[str] = None,
        direct_phone: Optional[str] = None,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        home_phone: Optional[str] = None,
        label_names: Optional[str] = None,
        last_name: Optional[str] = None,
        mobile_phone: Optional[str] = None,
        organization_name: Optional[str] = None,
        other_phone: Optional[str] = None,
        present_raw_address: Optional[str] = None,
        title: Optional[str] = None,
        website_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing contact in the CRM system.

        Args:
            account_id: 
            contact_stage_id: 
            corporate_phone: 
            direct_phone: 
            email: 
            first_name: 
            home_phone: 
            label_names: 
            last_name: 
            mobile_phone: 
            organization_name: 
            other_phone: 
            present_raw_address: 
            title: 
            website_url: 
        Returns:
            API response as a dictionary.
        """
        ...

