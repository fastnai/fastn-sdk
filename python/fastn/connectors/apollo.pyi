"""Fastn Apollo connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class ApolloConnector:
    """Apollo connector ().

    Provides 18 tools.
    """

    def apollo_bulk_enrich_organizations(
        self,
        domains: str,
    ) -> Dict[str, Any]:
        """Enriches multiple organizations profiles in a single request by matching each entry against Apollos database using identifiers such as domain or company name. Returns enriched company data for each matched organization. Use this tool when you need to enrich a list of companies at once. For enriching a single organization, use apollo_enrich_organization instead.

        Args:
            domains: Domains parameter for the apollo v1 endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def apollo_bulk_enrich_people(
        self,
        details: List[Any],
        reveal_personal_emails: Optional[str] = None,
        reveal_phone_number: Optional[str] = None,
        webhook_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Enriches multiple peoples profiles in a single request by matching each entry against Apollos database using identifiers such as email, name, or LinkedIn URL. Returns enriched contact data for each matched person. Use this tool when you need to enrich a list of contacts at once. For enriching a single person, use apollo_enrich_person instead.

        Args:
            details:  (required)
            reveal_personal_emails: Whether to reveal personal emails.
            reveal_phone_number: Whether to reveal phone numbers.
            webhook_url: Webhook URL for notifications.
        Returns:
            API response as a dictionary.
        """
        ...

    def apollo_create_account(
        self,
        account_stage_id: Optional[str] = None,
        domain: Optional[str] = None,
        name: Optional[str] = None,
        owner_id: Optional[str] = None,
        phone: Optional[str] = None,
        raw_address: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new account (company) record in Apollo. Accepts fields such as name, domain, phone, industry, and address. Use this tool when you need to add a company that does not yet exist in Apollo. Do not use this tool to update an existing account — use apollo_update_account instead. Account creation is reversible only by manual deletion.

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

    def apollo_create_contact(
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
        """Creates a new contact (person) record in Apollo. Accepts fields such as first name, last name, email, phone, title, and account association. Use this tool when you need to add a person who does not yet exist in Apollo. Do not use this tool to update an existing contact — use apollo_update_contact instead. Contact creation is not automatically reversible.

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

    def apollo_create_deal(
        self,
        name: str,
        account_id: Optional[str] = None,
        amount: Optional[str] = None,
        closed_date: Optional[str] = None,
        opportunity_stage_id: Optional[str] = None,
        owner_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new deal (opportunity) record in Apollo. Accepts fields such as name, stage ID, value, close date, owner, and associated contacts or accounts. Use this tool to add a new sales opportunity to the pipeline. Do not use this tool to update an existing deal. Deal creation is not automatically reversible.

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

    def apollo_create_task(
        self,
        contact_ids: str,
        due_at: str,
        priority: str,
        status: str,
        type: str,
        user_id: str,
        note: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates one or more tasks in Apollo in a single bulk request. Each task can be assigned to a user, linked to a contact or account, and given a due date, priority, and type. Use this tool to schedule follow-up actions or reminders within the CRM. Note: this endpoint uses bulk creation even for a single task. Task creation is not automatically reversible.

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

    def apollo_enrich_organization(
        self,
        domain: str,
    ) -> Dict[str, Any]:
        """Enriches a single organizations profile by matching against Apollos database using identifiers such as domain or company name. Returns enriched company data including industry, employee count, revenue, and technology stack. Use this tool when you have partial information about a company and need a complete organization record. Do not use this tool for bulk enrichment of multiple organizations — use apollo_bulk_enrich_organizations instead.

        Args:
            domain: Domain parameter for the apollo v1 endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def apollo_enrich_person(
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
        """Enriches a single persons profile by matching against Apollos database using identifiers such as email, name, or LinkedIn URL. Returns enriched contact data including job title, employer, phone, and social profiles. Use this tool when you have partial information about an individual and need a complete contact record. Do not use this tool for bulk enrichment of multiple people — use apollo_bulk_enrich_people instead.

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

    def apollo_get_account(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single Apollo account (company) record by its account ID. Returns fields such as name, domain, industry, phone, address, and associated contacts. Use this tool when you already know the account ID and need complete account information. Do not use this tool to search for accounts by criteria — use apollo_search_accounts instead.

        Args:
            accountId: Account ID for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def apollo_get_deal(
        self,
        dealId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single Apollo deal (opportunity) record by its deal ID. Returns fields such as name, stage, value, close date, owner, and associated contacts and accounts. Use this tool when you already know the deal ID and need complete deal information. Do not use this tool to browse or filter multiple deals — use apollo_list_deals instead.

        Args:
            dealId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def apollo_list_contact_stages(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the list of all configured contact stages in the Apollo CRM. Returns stage names and IDs used to categorize contacts in the sales pipeline. Use this tool to look up valid stage IDs before creating or updating a contact. Do not use this tool to retrieve contacts themselves — use apollo_search_contacts instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def apollo_list_deal_stages(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the list of all configured deal (opportunity) stages in the Apollo CRM. Returns stage names and IDs. Use this tool to look up valid stage IDs before creating or updating a deal. Do not use this tool to retrieve individual deals — use apollo_get_deal or apollo_list_deals instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def apollo_list_deals(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
        sort_by_field: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of deals (opportunities) from Apollo using a search query. Returns deal records including name, stage, value, owner, and associated contacts. Use this tool to browse or filter multiple deals. Do not use this tool to retrieve a single specific deal by ID — use apollo_get_deal instead.

        Args:
            page: 
            per_page: 
            sort_by_field: 
        Returns:
            API response as a dictionary.
        """
        ...

    def apollo_list_users(
        self,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of users (team members) in the Apollo organization. Returns user details such as name, email, role, and ID. Use this tool to look up internal Apollo user IDs needed for assigning tasks, deals, or contacts. Do not use this tool to retrieve external contacts or leads — use apollo_search_contacts instead.

        Args:
            page: 
            per_page: 
        Returns:
            API response as a dictionary.
        """
        ...

    def apollo_search_accounts(
        self,
        account_stage_ids: Optional[str] = None,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
        q_organization_name: Optional[str] = None,
        sort_ascending: Optional[str] = None,
        sort_by_field: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches Apollo accounts (companies) using filters such as name, domain, industry, location, or employee count. Returns a paginated list of matching account records. Use this tool to find accounts before retrieving or updating them. Do not use this tool to retrieve a single known account by ID — use apollo_get_account instead.

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

    def apollo_search_contacts(
        self,
        contact_stage_ids: Optional[str] = None,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
        q_keywords: Optional[str] = None,
        sort_ascending: Optional[str] = None,
        sort_by_field: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches Apollo contacts (people) using filters such as name, email, title, company, location, or contact stage. Returns a paginated list of matching contact records. Use this tool to find contacts before retrieving or updating them. Do not use this tool to retrieve a single known contact by ID — query by ID is not supported; use search with a unique identifier such as email instead.

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

    def apollo_update_account(
        self,
        accountId: str,
        account_stage_id: Optional[str] = None,
        domain: Optional[str] = None,
        name: Optional[str] = None,
        owner_id: Optional[str] = None,
        phone: Optional[str] = None,
        raw_address: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates fields on an existing Apollo account (company) record by account ID. Use this tool when you need to modify account properties such as name, domain, phone, industry, or custom fields for a known account. Do not use this tool to create a new account — use apollo_create_account instead. This operation overwrites the fields provided and cannot be undone without a subsequent update.

        Args:
            accountId: ID of the account. (required)
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

    def apollo_update_contact(
        self,
        contactId: str,
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
        """Updates fields on an existing Apollo contact record by contact ID. Accepts fields such as name, email, phone, title, account association, and custom fields. Use this tool when you need to modify a known contacts information. Do not use this tool to create a new contact — use apollo_create_contact instead. This operation overwrites the fields provided and cannot be undone without a subsequent update.

        Args:
            contactId:  (required)
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

