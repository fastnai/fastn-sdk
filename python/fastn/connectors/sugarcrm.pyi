"""Fastn SugarCRM connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class SugarcrmConnector:
    """SugarCRM connector ().

    Provides 17 tools.
    """

    def sugarcrm_create_contact(
        self,
        account_id: Optional[str] = None,
        alt_address_city: Optional[str] = None,
        alt_address_country: Optional[str] = None,
        alt_address_postalcode: Optional[str] = None,
        alt_address_state: Optional[str] = None,
        alt_address_street: Optional[str] = None,
        assigned_user_id: Optional[str] = None,
        birthdate: Optional[str] = None,
        department: Optional[str] = None,
        description: Optional[str] = None,
        do_not_call: Optional[bool] = None,
        email: Optional[List[Any]] = None,
        facebook: Optional[str] = None,
        first_name: Optional[str] = None,
        googleplus: Optional[str] = None,
        last_name: Optional[str] = None,
        lead_source: Optional[str] = None,
        phone_fax: Optional[str] = None,
        phone_home: Optional[str] = None,
        phone_mobile: Optional[str] = None,
        phone_other: Optional[str] = None,
        phone_work: Optional[str] = None,
        portal_active: Optional[bool] = None,
        portal_name: Optional[str] = None,
        primary_address_city: Optional[str] = None,
        primary_address_country: Optional[str] = None,
        primary_address_postalcode: Optional[str] = None,
        primary_address_state: Optional[str] = None,
        primary_address_street: Optional[str] = None,
        salutation: Optional[str] = None,
        title: Optional[str] = None,
        twitter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact record in SugarCRM to store information about a customer, partner, or lead-derived person. Use this tool when a new person must be added to the CRM contacts for the first time. Do not use this tool to update an existing contact (use sugarcrm_update_contact) or to create lead or opportunity records. This operation permanently adds a contact record to SugarCRM.

        Args:
            account_id: ID of the associated account.
            alt_address_city: Alternative address city.
            alt_address_country: Alternative address country.
            alt_address_postalcode: Alternative address postal code.
            alt_address_state: Alternative address state.
            alt_address_street: Alternative address street.
            assigned_user_id: ID of the assigned user.
            birthdate: Lead's birthdate.
            department: Lead's department.
            description: Description of the lead.
            do_not_call: Indicates if the lead should not be contacted.
            email: 
            facebook: Lead's Facebook profile URL.
            first_name: Lead's first name.
            googleplus: Lead's Google+ profile URL.
            last_name: Lead's last name.
            lead_source: Source of the lead.
            phone_fax: Lead's fax number.
            phone_home: Lead's home phone number.
            phone_mobile: Lead's mobile phone number.
            phone_other: Lead's other phone number.
            phone_work: Lead's work phone number.
            portal_active: Indicates if the lead is active on the portal.
            portal_name: Portal name associated with the lead.
            primary_address_city: Primary address city.
            primary_address_country: Primary address country.
            primary_address_postalcode: Primary address postal code.
            primary_address_state: Primary address state.
            primary_address_street: Primary address street.
            salutation: Lead's salutation.
            title: Lead's title.
            twitter: Lead's Twitter handle.
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_create_lead(
        self,
        account_name: Optional[str] = None,
        alt_address_city: Optional[str] = None,
        alt_address_country: Optional[str] = None,
        alt_address_postalcode: Optional[str] = None,
        alt_address_state: Optional[str] = None,
        alt_address_street: Optional[str] = None,
        assigned_user_id: Optional[str] = None,
        birthdate: Optional[str] = None,
        campaign_id: Optional[str] = None,
        department: Optional[str] = None,
        description: Optional[str] = None,
        do_not_call: Optional[bool] = None,
        email: Optional[List[Any]] = None,
        facebook: Optional[str] = None,
        first_name: Optional[str] = None,
        googleplus: Optional[str] = None,
        last_name: Optional[str] = None,
        lead_source: Optional[str] = None,
        opportunity_amount: Optional[str] = None,
        phone_fax: Optional[str] = None,
        phone_home: Optional[str] = None,
        phone_mobile: Optional[str] = None,
        phone_other: Optional[str] = None,
        phone_work: Optional[str] = None,
        portal_active: Optional[bool] = None,
        portal_name: Optional[str] = None,
        primary_address_city: Optional[str] = None,
        primary_address_country: Optional[str] = None,
        primary_address_postalcode: Optional[str] = None,
        primary_address_state: Optional[str] = None,
        primary_address_street: Optional[str] = None,
        refered_by: Optional[str] = None,
        salutation: Optional[str] = None,
        status: Optional[str] = None,
        title: Optional[str] = None,
        twitter: Optional[str] = None,
        website: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new lead record in SugarCRM to represent a potential customer or inquiry. Use this tool when you want to add a brand-new lead to the CRM pipeline for the first time. Do not use this tool to update an existing lead (use sugarcrm_update_lead) or to create contact or opportunity records. This operation permanently adds a lead record to SugarCRM.

        Args:
            account_name: Account name associated with the record.
            alt_address_city: Alternative address city.
            alt_address_country: Alternative address country.
            alt_address_postalcode: Alternative address postal code.
            alt_address_state: Alternative address state.
            alt_address_street: Alternative address street.
            assigned_user_id: ID of the assigned user.
            birthdate: Birthdate of the individual.
            campaign_id: Campaign ID.
            department: Department of the individual.
            description: Description of the record.
            do_not_call: Do not call flag.
            email: 
            facebook: Facebook profile URL.
            first_name: First name of the individual.
            googleplus: Google Plus profile URL.
            last_name: Last name of the individual.
            lead_source: Source of the lead.
            opportunity_amount: Opportunity amount.
            phone_fax: Fax number.
            phone_home: Home phone number.
            phone_mobile: Mobile phone number.
            phone_other: Other phone number.
            phone_work: Work phone number.
            portal_active: Portal active flag.
            portal_name: Portal name.
            primary_address_city: Primary address city.
            primary_address_country: Primary address country.
            primary_address_postalcode: Primary address postal code.
            primary_address_state: Primary address state.
            primary_address_street: Primary address street.
            refered_by: Referred by.
            salutation: Salutation.
            status: Status of the record.
            title: Title of the individual.
            twitter: Twitter handle.
            website: Website URL.
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_create_opportunity(
        self,
        account_id: Optional[str] = None,
        amount: Optional[str] = None,
        assigned_user_id: Optional[str] = None,
        best_case: Optional[str] = None,
        campaign_id: Optional[str] = None,
        date_closed: Optional[str] = None,
        date_entered: Optional[str] = None,
        date_modified: Optional[str] = None,
        description: Optional[str] = None,
        lead_source: Optional[str] = None,
        name: Optional[str] = None,
        next_step: Optional[str] = None,
        opportunity_type: Optional[str] = None,
        probability: Optional[int] = None,
        renewal: Optional[bool] = None,
        sales_stage: Optional[str] = None,
        service: Optional[bool] = None,
        service_duration: Optional[int] = None,
        service_end_date: Optional[str] = None,
        service_start_date: Optional[str] = None,
        worst_case: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new opportunity record in SugarCRM to track a potential sale or revenue-generating deal. Use this tool when a new sales opportunity must be added to the pipeline for the first time. Do not use this tool to update an existing opportunity (use sugarcrm_update_opportunity) or to create lead or contact records. This operation permanently adds an opportunity record to SugarCRM.

        Args:
            account_id: The ID of the account associated with the opportunity.
            amount: The amount of the opportunity.
            assigned_user_id: The ID of the user assigned to the opportunity.
            best_case: The best-case amount for the opportunity.
            campaign_id: The ID of the campaign associated with the opportunity.
            date_closed: The date the opportunity was closed.
            date_entered: The date and time the opportunity was created.
            date_modified: The date and time the opportunity was last modified.
            description: A description of the opportunity.
            lead_source: The source of the lead.
            name: The name of the opportunity.
            next_step: The next step in the sales process.
            opportunity_type: The type of opportunity.
            probability: The probability of closing the opportunity (percentage).
            renewal: Indicates if this is a renewal opportunity.
            sales_stage: The current sales stage of the opportunity.
            service: Indicates if this opportunity involves a service.
            service_duration: The duration of the service (in days or other units).
            service_end_date: The end date of the service.
            service_start_date: The start date of the service.
            worst_case: The worst-case amount for the opportunity.
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a contact record from SugarCRM by contact ID. Use this tool when a contact must be fully removed from the CRM — for example, a duplicate or invalid record. Do not use this tool to simply update contact information (use sugarcrm_update_contact instead). This operation is irreversible; the contact record cannot be recovered after deletion.

        Args:
            contactId: The ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_delete_lead(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a lead record from SugarCRM by lead ID. Use this tool when a lead must be fully removed from the CRM — for example, duplicate records or invalid inquiries. Do not use this tool to simply update or close a lead (use sugarcrm_update_lead instead). This operation is irreversible; the lead record cannot be recovered after deletion.

        Args:
            opportunityId:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_delete_opportunity(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an opportunity record from SugarCRM by opportunity ID. Use this tool when an opportunity must be fully removed from the sales pipeline — for example, a cancelled or duplicate deal. Do not use this tool to simply update or close an opportunity (use sugarcrm_update_opportunity instead). This operation is irreversible; the opportunity record cannot be recovered after deletion.

        Args:
            opportunityId: The ID of the opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_get_access_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        password: Optional[str] = None,
        platform: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains an OAuth2 access token from SugarCRM using user credentials or a grant flow via the /oauth2/token endpoint. Use this tool as the first authentication step before making any other SugarCRM API calls; the returned access token must be included in subsequent requests. Do not use this tool to renew an existing session (use sugarcrm_get_refresh_token instead). This operation posts credentials to the authentication endpoint and returns a short-lived access token.

        Args:
            client_id: 
            client_secret: 
            grant_type: 
            password: 
            platform: 
            username: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details of a single contact record from SugarCRM by its unique contact ID. Use this tool when you need to inspect or display all fields of one specific contact. Do not use this tool to retrieve multiple contacts at once (use sugarcrm_list_contacts) or to fetch lead or opportunity records. This is a read-only operation with no side effects.

        Args:
            contactId: The ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_get_lead(
        self,
        leadId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details of a single lead record from SugarCRM by its unique lead ID. Use this tool when you need to inspect or display all fields of one specific lead. Do not use this tool to retrieve multiple leads at once (use sugarcrm_list_leads) or to fetch contact or opportunity records. This is a read-only operation with no side effects.

        Args:
            leadId: The ID of the lead to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_get_opportunity(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Retrieves full details of a single opportunity record from SugarCRM by its unique opportunity ID. Use this tool when you need to inspect or display all fields of one specific opportunity. Do not use this tool to retrieve multiple opportunities at once (use sugarcrm_list_opportunities) or to fetch lead or contact records. This is a read-only operation with no side effects.

        Args:
            opportunityId: The ID of the opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_get_refresh_token(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        grant_type: Optional[str] = None,
        platform: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Obtains a new OAuth2 refresh token from SugarCRM using the /oauth2/token endpoint. Use this tool to silently renew a user session and obtain a new access token without requiring the user to re-authenticate interactively. Do not use this tool to obtain an initial access token from credentials (use sugarcrm_get_access_token instead). Calling this tool issues a POST request to the authentication endpoint and may invalidate the previously issued refresh token.

        Args:
            client_id: 
            client_secret: 
            grant_type: 
            platform: 
            refresh_token: 
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_list_contacts(
        self,
        fields: Optional[str] = None,
        max_num: Optional[str] = None,
        offset: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all contact records in SugarCRM. Use this tool when you need to browse multiple contacts at once, search for a contact by name, or identify a contacts ID before calling sugarcrm_get_contact. Do not use this tool when you already know the contact ID and need full detail for a single record (use sugarcrm_get_contact instead). This is a read-only operation with no side effects.

        Args:
            fields: Comma-separated list of fields to retrieve.
            max_num: Maximum number of records to retrieve.
            offset: Offset for pagination.
            order_by: Field to order results by.
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_list_leads(
        self,
        fields: Optional[str] = None,
        max_num: Optional[str] = None,
        offset: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all lead records in SugarCRM. Use this tool when you need an overview of leads in the pipeline, want to browse multiple leads at once, or need to identify a leads ID before calling sugarcrm_get_lead. Do not use this tool when you already know the lead ID and need full detail for a single record (use sugarcrm_get_lead instead). This is a read-only operation with no side effects.

        Args:
            fields: Comma-separated list of fields to retrieve.
            max_num: Maximum number of records to retrieve.
            offset: Offset for pagination.
            order_by: Field to order the results by.
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_list_opportunities(
        self,
        fields: Optional[str] = None,
        max_num: Optional[str] = None,
        offset: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all opportunity records in SugarCRM. Use this tool when you need an overview of the sales pipeline, want to browse multiple opportunities at once, or need to identify an opportunitys ID before calling sugarcrm_get_opportunity. Do not use this tool when you already know the opportunity ID and need full detail for a single record (use sugarcrm_get_opportunity instead). This is a read-only operation with no side effects.

        Args:
            fields: Comma-separated list of fields to retrieve.
            max_num: Maximum number of records to retrieve.
            offset: Offset for pagination.
            order_by: Field to order the results by.
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_update_contact(
        self,
        contactId: str,
        account_id: Optional[str] = None,
        alt_address_city: Optional[str] = None,
        alt_address_country: Optional[str] = None,
        alt_address_postalcode: Optional[str] = None,
        alt_address_state: Optional[str] = None,
        alt_address_street: Optional[str] = None,
        assigned_user_id: Optional[str] = None,
        birthdate: Optional[str] = None,
        department: Optional[str] = None,
        description: Optional[str] = None,
        do_not_call: Optional[bool] = None,
        email: Optional[List[Any]] = None,
        facebook: Optional[str] = None,
        first_name: Optional[str] = None,
        googleplus: Optional[str] = None,
        last_name: Optional[str] = None,
        lead_source: Optional[str] = None,
        phone_fax: Optional[str] = None,
        phone_home: Optional[str] = None,
        phone_mobile: Optional[str] = None,
        phone_other: Optional[str] = None,
        phone_work: Optional[str] = None,
        portal_active: Optional[bool] = None,
        portal_name: Optional[str] = None,
        primary_address_city: Optional[str] = None,
        primary_address_country: Optional[str] = None,
        primary_address_postalcode: Optional[str] = None,
        primary_address_state: Optional[str] = None,
        primary_address_street: Optional[str] = None,
        salutation: Optional[str] = None,
        title: Optional[str] = None,
        twitter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing contact record in SugarCRM by contact ID. Use this tool when you need to modify fields on a contact — such as name, email, phone number, or account association — after the contact has been created. Do not use this tool to create a new contact (use sugarcrm_create_contact) or to update lead or opportunity records. This operation overwrites the specified fields and the change is permanent unless manually reversed.

        Args:
            contactId:  (required)
            account_id: ID of the associated account in SugarCRM.
            alt_address_city: City for the alternative address.
            alt_address_country: Country for the alternative address.
            alt_address_postalcode: Postal code for the alternative address.
            alt_address_state: State/Province for the alternative address.
            alt_address_street: Street address for the alternative address.
            assigned_user_id: ID of the assigned user in SugarCRM.
            birthdate: Contact's birthdate.
            department: Contact's department.
            description: Description of the contact.
            do_not_call: Indicates if the contact should not be called.
            email: 
            facebook: Contact's Facebook profile URL.
            first_name: Contact's first name.
            googleplus: Contact's Google+ profile URL.
            last_name: Contact's last name.
            lead_source: Source of the lead.
            phone_fax: Contact's fax number.
            phone_home: Contact's home phone number.
            phone_mobile: Contact's mobile phone number.
            phone_other: Contact's other phone number.
            phone_work: Contact's work phone number.
            portal_active: Indicates if the contact is active in the portal.
            portal_name: Contact's portal name.
            primary_address_city: City for the primary address.
            primary_address_country: Country for the primary address.
            primary_address_postalcode: Postal code for the primary address.
            primary_address_state: State/Province for the primary address.
            primary_address_street: Street address for the primary address.
            salutation: Contact's salutation (e.g., Mr., Ms.).
            title: Contact's title or job position.
            twitter: Contact's Twitter handle.
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_update_lead(
        self,
        leadId: str,
        account_name: Optional[str] = None,
        alt_address_city: Optional[str] = None,
        alt_address_country: Optional[str] = None,
        alt_address_postalcode: Optional[str] = None,
        alt_address_state: Optional[str] = None,
        alt_address_street: Optional[str] = None,
        assigned_user_id: Optional[str] = None,
        birthdate: Optional[str] = None,
        campaign_id: Optional[str] = None,
        department: Optional[str] = None,
        description: Optional[str] = None,
        do_not_call: Optional[bool] = None,
        email: Optional[List[Any]] = None,
        facebook: Optional[str] = None,
        first_name: Optional[str] = None,
        googleplus: Optional[str] = None,
        last_name: Optional[str] = None,
        lead_source: Optional[str] = None,
        opportunity_amount: Optional[str] = None,
        phone_fax: Optional[str] = None,
        phone_home: Optional[str] = None,
        phone_mobile: Optional[str] = None,
        phone_other: Optional[str] = None,
        phone_work: Optional[str] = None,
        portal_active: Optional[bool] = None,
        portal_name: Optional[str] = None,
        primary_address_city: Optional[str] = None,
        primary_address_country: Optional[str] = None,
        primary_address_postalcode: Optional[str] = None,
        primary_address_state: Optional[str] = None,
        primary_address_street: Optional[str] = None,
        refered_by: Optional[str] = None,
        salutation: Optional[str] = None,
        status: Optional[str] = None,
        title: Optional[str] = None,
        twitter: Optional[str] = None,
        website: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing lead record in SugarCRM by lead ID. Use this tool when you need to modify one or more fields on a lead — such as name, contact details, status, or assignment — after the lead has already been created. Do not use this tool to create a new lead (use sugarcrm_create_lead) or to update contact or opportunity records. This operation overwrites the specified fields on the lead and the change is permanent unless manually reversed.

        Args:
            leadId: ID of the lead. (required)
            account_name: Name of the associated account.
            alt_address_city: Alternative address city.
            alt_address_country: Alternative address country.
            alt_address_postalcode: Alternative address postal code.
            alt_address_state: Alternative address state/province.
            alt_address_street: Alternative address street.
            assigned_user_id: ID of the assigned user.
            birthdate: Lead's birthdate.
            campaign_id: ID of the associated campaign.
            department: Lead's department.
            description: Description of the lead.
            do_not_call: Indicates if the lead should not be called.
            email: 
            facebook: Lead's Facebook profile URL.
            first_name: Lead's first name.
            googleplus: Lead's Google+ profile URL.
            last_name: Lead's last name.
            lead_source: Source of the lead.
            opportunity_amount: Amount of the associated opportunity.
            phone_fax: Lead's fax number.
            phone_home: Lead's home phone number.
            phone_mobile: Lead's mobile phone number.
            phone_other: Lead's other phone number.
            phone_work: Lead's work phone number.
            portal_active: Indicates if the lead is active on the portal.
            portal_name: Name of the portal.
            primary_address_city: Primary address city.
            primary_address_country: Primary address country.
            primary_address_postalcode: Primary address postal code.
            primary_address_state: Primary address state/province.
            primary_address_street: Primary address street.
            refered_by: Person who referred the lead.
            salutation: Lead's salutation.
            status: Status of the lead.
            title: Lead's title.
            twitter: Lead's Twitter handle.
            website: Lead's website.
        Returns:
            API response as a dictionary.
        """
        ...

    def sugarcrm_update_opportunity(
        self,
        opportunityId: str,
        account_id: Optional[str] = None,
        amount: Optional[str] = None,
        assigned_user_id: Optional[str] = None,
        best_case: Optional[str] = None,
        campaign_id: Optional[str] = None,
        date_closed: Optional[str] = None,
        date_entered: Optional[str] = None,
        date_modified: Optional[str] = None,
        description: Optional[str] = None,
        lead_source: Optional[str] = None,
        name: Optional[str] = None,
        next_step: Optional[str] = None,
        opportunity_type: Optional[str] = None,
        probability: Optional[int] = None,
        renewal: Optional[bool] = None,
        sales_stage: Optional[str] = None,
        service: Optional[bool] = None,
        service_duration: Optional[int] = None,
        service_end_date: Optional[str] = None,
        service_start_date: Optional[str] = None,
        worst_case: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing opportunity record in SugarCRM by opportunity ID. Use this tool when you need to modify fields on an opportunity — such as deal stage, close date, amount, or assigned user — after it has been created. Do not use this tool to create a new opportunity (use sugarcrm_create_opportunity) or to update lead or contact records. This operation overwrites the specified fields and the change is permanent unless manually reversed.

        Args:
            opportunityId: The ID of the opportunity. (required)
            account_id: The ID of the account associated with the opportunity.
            amount: The amount of the opportunity.
            assigned_user_id: The ID of the user assigned to the opportunity.
            best_case: The best-case amount for the opportunity.
            campaign_id: The ID of the associated marketing campaign.
            date_closed: The date the opportunity was closed.
            date_entered: The date the opportunity was created.
            date_modified: The date the opportunity was last modified.
            description: A description of the opportunity.
            lead_source: The source of the lead.
            name: The name of the opportunity.
            next_step: The next step in the sales process.
            opportunity_type: The type of opportunity.
            probability: The probability of closing the opportunity (percentage).
            renewal: Indicates if this is a renewal opportunity.
            sales_stage: The current sales stage of the opportunity.
            service: Indicates if this is a service opportunity.
            service_duration: The duration of the service (in days or other relevant unit).
            service_end_date: The end date of the service.
            service_start_date: The start date of the service.
            worst_case: The worst-case amount for the opportunity.
        Returns:
            API response as a dictionary.
        """
        ...

