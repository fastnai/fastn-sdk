"""Fastn Salesforce connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SalesforceConnector:
    """Salesforce connector ().

    Provides 44 tools.
    """

    def access_token(
        self,
        client_id: str,
        client_secret: str,
        grant_type: str,
        password: str,
        username: str,
    ) -> Dict[str, Any]:
        """Generates an access token for authentication to the system.

        Args:
            client_id: Client ID for Salesforce OAuth2 authentication. (required)
            client_secret: Client secret for Salesforce OAuth2 authentication. (required)
            grant_type: Grant type for Salesforce OAuth2 authentication. (required)
            password: User's password for Salesforce authentication. (required)
            username: Username for Salesforce authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def add_field_to_permission_set(
        self,
        Field: str,
        ParentId: str,
        PermissionsEdit: Optional[bool] = None,
        PermissionsRead: Optional[bool] = None,
        SobjectType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a field to an existing permission set within the Salesforce environment.

        Args:
            Field: The name of the field. (required)
            ParentId: The ID of the parent object. (required)
            PermissionsEdit: Indicates whether edit access is permitted.
            PermissionsRead: Indicates whether read access is permitted.
            SobjectType: The type of Salesforce object.
        Returns:
            API response as a dictionary.
        """
        ...

    def add_note_to_object(
        self,
        Body: str,
        ParentId: str,
        Title: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a note to a specific object in the system.

        Args:
            Body: Body of the Salesforce record. (required)
            ParentId: Parent ID for the Salesforce record. (required)
            Title: Title of the Salesforce record.
        Returns:
            API response as a dictionary.
        """
        ...

    def assign_permission_set_to_user(
        self,
        AssigneeId: str,
        PermissionSetId: str,
    ) -> Dict[str, Any]:
        """Assigns a permission set to a specific user within the Salesforce environment.

        Args:
            AssigneeId: The ID of the Assignee. (required)
            PermissionSetId: The ID of the Permission Set. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def attach_file_to_opportunity(
        self,
        ContentDocumentId: str,
        LinkedEntityId: str,
        ShareType: str,
    ) -> Dict[str, Any]:
        """Attaches a file to an opportunity in the system.

        Args:
            ContentDocumentId: ID of the content document. (required)
            LinkedEntityId: ID of the linked entity. (required)
            ShareType: Type of share. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_account(
        self,
        Name: str,
        BillingCity: Optional[str] = None,
        BillingCountry: Optional[str] = None,
        BillingPostalCode: Optional[str] = None,
        BillingState: Optional[str] = None,
        BillingStreet: Optional[str] = None,
        Description: Optional[str] = None,
        OwnerId: Optional[str] = None,
        ParentId: Optional[str] = None,
        Phone: Optional[str] = None,
        ShippingCity: Optional[str] = None,
        ShippingCountry: Optional[str] = None,
        ShippingPostalCode: Optional[str] = None,
        ShippingState: Optional[str] = None,
        ShippingStreet: Optional[str] = None,
        Type: Optional[str] = None,
        Website: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new account in the system.

        Args:
            Name: The name of the account. (required)
            BillingCity: The billing city of the account.
            BillingCountry: The billing country of the account.
            BillingPostalCode: The billing postal code of the account.
            BillingState: The billing state/province of the account.
            BillingStreet: The billing street address of the account.
            Description: A description of the account.
            OwnerId: The ID of the account owner.
            ParentId: The ID of the parent account, if applicable.
            Phone: The phone number of the account.
            ShippingCity: The shipping city of the account.
            ShippingCountry: The shipping country of the account.
            ShippingPostalCode: The shipping postal code of the account.
            ShippingState: The shipping state/province of the account.
            ShippingStreet: The shipping street address of the account.
            Type: The type of account.
            Website: The website URL of the account.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_apex_class(
        self,
        apexClassName: str,
        webhookUrl: str,
    ) -> Dict[str, Any]:
        """Creates a new Apex class within the Salesforce environment.

        Args:
            apexClassName: The name of the Apex class to be invoked. (required)
            webhookUrl: The URL for the webhook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_apex_trigger(
        self,
        tableEnum: str,
        triggerName: str,
        apexClassName: Optional[str] = None,
        operation: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Apex trigger within the Salesforce environment.

        Args:
            tableEnum: The table enum. (required)
            triggerName: The name of the trigger. (required)
            apexClassName: The name of the Apex class.
            operation: The operation to be performed.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_contact(
        self,
        FirstName: str,
        LastName: str,
        AccountId: Optional[str] = None,
        Description: Optional[str] = None,
        Email: Optional[str] = None,
        MailingCity: Optional[str] = None,
        MailingCountry: Optional[str] = None,
        MailingPostalCode: Optional[str] = None,
        MailingState: Optional[str] = None,
        MailingStreet: Optional[str] = None,
        OwnerId: Optional[str] = None,
        Phone: Optional[str] = None,
        ReportsToId: Optional[str] = None,
        Salutation: Optional[str] = None,
        Title: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact in the system.

        Args:
            FirstName: First name of the account contact. (required)
            LastName: Last name of the account contact. (required)
            AccountId: Unique identifier for the account (optional).
            Description: Description of the account.
            Email: Email address associated with the account.
            MailingCity: City of the mailing address.
            MailingCountry: Country of the mailing address.
            MailingPostalCode: Postal code of the mailing address.
            MailingState: State or province of the mailing address.
            MailingStreet: Street address of the mailing address.
            OwnerId: Salesforce ID of the account owner.
            Phone: Phone number associated with the account.
            ReportsToId: Salesforce ID of the account's parent account (if applicable).
            Salutation: Salutation for the account contact.
            Title: Title of the account.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_content_version(
        self,
        PathOnClient: str,
        Title: str,
        VersionData: str,
    ) -> Dict[str, Any]:
        """Creates a new content version in the system.

        Args:
            PathOnClient: Path on client for the Salesforce object. (required)
            Title: Title of the Salesforce object. (required)
            VersionData: Version data for the Salesforce object. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_custom_field(
        self,
        FullName: str,
        Metadata: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new custom field within the Salesforce environment.

        Args:
            FullName: Full name of the user or entity. (required)
            Metadata: Metadata related to the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_opportunity(
        self,
        AccountId: str,
        CloseDate: str,
        Name: str,
        StageName: str,
        Amount: Optional[int] = None,
        CampaignId: Optional[str] = None,
        Description: Optional[str] = None,
        ForecastCategoryName: Optional[str] = None,
        IsPrivate: Optional[bool] = None,
        LeadSource: Optional[str] = None,
        NextStep: Optional[str] = None,
        OwnerId: Optional[str] = None,
        Pricebook2Id: Optional[str] = None,
        Probability: Optional[int] = None,
        Type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new opportunity in the system.

        Args:
            AccountId: ID of the related Account (required)
            CloseDate: Expected closing date of the Opportunity (required)
            Name: Name of the Opportunity (required)
            StageName: Name of the Opportunity Stage (required)
            Amount: Amount of the Opportunity
            CampaignId: ID of the related Campaign
            Description: Description of the Opportunity
            ForecastCategoryName: Name of the Forecast Category
            IsPrivate: Indicates if the Opportunity is private
            LeadSource: Source of the Opportunity lead
            NextStep: Description of the next step in the sales process
            OwnerId: ID of the Opportunity owner
            Pricebook2Id: ID of the related Price Book
            Probability: Probability of closing the Opportunity
            Type: Type of the Opportunity
        Returns:
            API response as a dictionary.
        """
        ...

    def create_permission_set(
        self,
        Label: str,
        Name: str,
        Description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new permission set within the Salesforce environment.

        Args:
            Label: Label for the Salesforce object. (required)
            Name: Name of the Salesforce object. (required)
            Description: Description of the Salesforce object.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_remote_site(
        self,
        FullName: str,
        Metadata: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new remote site setting within the Salesforce environment.

        Args:
            FullName: The full name of the user or entity. (required)
            Metadata: Metadata associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_sale(
        self,
        AccountId: str,
        CloseDate: str,
        Name: str,
        StageName: str,
        Amount: Optional[int] = None,
        Description: Optional[str] = None,
        ForecastCategoryName: Optional[str] = None,
        NextStep: Optional[str] = None,
        OwnerId: Optional[str] = None,
        Probability: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new sale in the system.

        Args:
            AccountId: The ID of the related Account. (required)
            CloseDate: The expected close date of the opportunity. (required)
            Name: The name of the opportunity. (required)
            StageName: The stage of the opportunity. (required)
            Amount: The amount of the opportunity.
            Description: Description of the opportunity.
            ForecastCategoryName: The forecast category of the opportunity.
            NextStep: The next step in the sales process.
            OwnerId: The ID of the opportunity owner.
            Probability: The probability of closing the opportunity (%).
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_account(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Deletes an existing account from the system.

        Args:
            accountId: The ID of the Salesforce account. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Deletes a contact from the system.

        Args:
            contactId: ID of the contact in Salesforce. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_opportunity(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Deletes an opportunity from the system.

        Args:
            opportunityId: ID of the opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_sale(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Deletes a sale from the system.

        Args:
            opportunityId: The ID of the Salesforce opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def generate_token_client_credentials(
        self,
        client_id: str,
        client_secret: str,
    ) -> Dict[str, Any]:
        """Generates a client credentials token for authentication to the system.

        Args:
            client_id: Client ID for Salesforce API authentication. (required)
            client_secret: Client secret for Salesforce API authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_account(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Retrieves account information from the system.

        Args:
            accountId: The ID of the Salesforce account. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_accounts(
        self,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of accounts from the system.

        Args:
            q: Query parameter for filtering results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_apex_class_by_name(
        self,
        apexClassName: str,
    ) -> Dict[str, Any]:
        """Retrieves an Apex class by its name within the Salesforce environment.

        Args:
            apexClassName: The name of the Apex class to execute. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_apex_trigger_by_name(
        self,
        apexTriggerName: str,
    ) -> Dict[str, Any]:
        """Retrieves an Apex trigger by its name within the Salesforce environment.

        Args:
            apexTriggerName: The name of the Apex trigger. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves contact information from the system.

        Args:
            contactId: The ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of contacts from the system.

        Args:
            q: The query string for the Salesforce API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_content_document_by_id(
        self,
        contentDocumentId: str,
    ) -> Dict[str, Any]:
        """Retrieves content document information by its ID from the system.

        Args:
            contentDocumentId: The ID of the content document in Salesforce. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_content_version(
        self,
        contentVersionId: str,
    ) -> Dict[str, Any]:
        """Retrieves content version information from the system.

        Args:
            contentVersionId: The ID of the content version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_by_opportunity_id(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Retrieves a file associated with a specific opportunity ID from the system.

        Args:
            opportunityId: ID of the Salesforce opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file_content(
        self,
        attributeUrl: str,
    ) -> Dict[str, Any]:
        """Retrieves the content of a file from the system.

        Args:
            attributeUrl: The URL for accessing the attribute. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_lead(
        self,
        leadId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific lead from the system.

        Args:
            leadId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_leads(
        self,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of leads from the system.

        Args:
            q: Query parameter for Salesforce search.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_opportunities(
        self,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of opportunities from the system.

        Args:
            q: Query string parameter for Salesforce API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_opportunity(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Retrieves opportunity information from the system.

        Args:
            opportunityId: The ID of the opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_properties(
        self,
        resourceName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves properties from the system.

        Args:
            resourceName: Resource ( eg: Company, Contact, Account )
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sale(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Retrieves sale information from the system.

        Args:
            opportunityId: The ID of the opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_sales(
        self,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of sales from the system.

        Args:
            q: Query parameter for the Salesforce API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user(
        self,
    ) -> Dict[str, Any]:
        """Retrieves user information from the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_details(
        self,
    ) -> Dict[str, Any]:
        """Retrieves detailed user information from the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_version_data(
        self,
        contentVersionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves version data from the system.

        Args:
            contentVersionId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_account(
        self,
        Name: str,
        BillingCity: Optional[str] = None,
        BillingCountry: Optional[str] = None,
        BillingPostalCode: Optional[str] = None,
        BillingState: Optional[str] = None,
        BillingStreet: Optional[str] = None,
        Description: Optional[str] = None,
        OwnerId: Optional[str] = None,
        ParentId: Optional[str] = None,
        Phone: Optional[str] = None,
        ShippingCity: Optional[str] = None,
        ShippingCountry: Optional[str] = None,
        ShippingPostalCode: Optional[str] = None,
        ShippingState: Optional[str] = None,
        ShippingStreet: Optional[str] = None,
        Type: Optional[str] = None,
        Website: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates existing account information in the system.

        Args:
            Name: The name of the account. (required)
            BillingCity: The billing city of the account.
            BillingCountry: The billing country of the account.
            BillingPostalCode: The billing postal code of the account.
            BillingState: The billing state/province of the account.
            BillingStreet: The billing street address of the account.
            Description: A description of the account.
            OwnerId: The ID of the account owner.
            ParentId: The ID of the parent account, if applicable.
            Phone: The phone number of the account.
            ShippingCity: The shipping city of the account.
            ShippingCountry: The shipping country of the account.
            ShippingPostalCode: The shipping postal code of the account.
            ShippingState: The shipping state/province of the account.
            ShippingStreet: The shipping street address of the account.
            Type: The type of account.
            Website: The website URL of the account.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_contact(
        self,
        AccountId: str,
        FirstName: str,
        LastName: str,
        Description: Optional[str] = None,
        Email: Optional[str] = None,
        MailingCity: Optional[str] = None,
        MailingCountry: Optional[str] = None,
        MailingPostalCode: Optional[str] = None,
        MailingState: Optional[str] = None,
        MailingStreet: Optional[str] = None,
        OwnerId: Optional[str] = None,
        Phone: Optional[str] = None,
        ReportsToId: Optional[str] = None,
        Salutation: Optional[str] = None,
        Title: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates existing contact information in the system.

        Args:
            AccountId: The ID of the associated Account. (required)
            FirstName: The contact's first name. (required)
            LastName: The contact's last name. (required)
            Description: A description of the contact.
            Email: The contact's email address.
            MailingCity: The contact's mailing city.
            MailingCountry: The contact's mailing country.
            MailingPostalCode: The contact's mailing postal code.
            MailingState: The contact's mailing state/province.
            MailingStreet: The contact's mailing street address.
            OwnerId: The ID of the contact's owner.
            Phone: The contact's phone number.
            ReportsToId: The ID of the contact's manager.
            Salutation: The contact's salutation.
            Title: The contact's title.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_opportunity(
        self,
        AccountId: str,
        Name: str,
        Amount: Optional[int] = None,
        CampaignId: Optional[str] = None,
        CloseDate: Optional[str] = None,
        Description: Optional[str] = None,
        ForecastCategoryName: Optional[str] = None,
        IsPrivate: Optional[bool] = None,
        LeadSource: Optional[str] = None,
        NextStep: Optional[str] = None,
        OwnerId: Optional[str] = None,
        Pricebook2Id: Optional[str] = None,
        Probability: Optional[int] = None,
        StageName: Optional[str] = None,
        Type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates existing opportunity information in the system.

        Args:
            AccountId: The ID of the associated Account. (required)
            Name: The name of the opportunity. (required)
            Amount: The amount of the opportunity.
            CampaignId: The ID of the associated campaign.
            CloseDate: The expected closing date of the opportunity.
            Description: Description of the opportunity.
            ForecastCategoryName: The name of the forecast category.
            IsPrivate: Indicates if the opportunity is private.
            LeadSource: The source of the opportunity lead.
            NextStep: The next step in the sales process.
            OwnerId: The ID of the opportunity owner.
            Pricebook2Id: The ID of the associated price book.
            Probability: The probability of closing the opportunity (percentage).
            StageName: The name of the opportunity stage.
            Type: The type of opportunity.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_sale(
        self,
        Amount: int,
        StageName: str,
        CloseDate: Optional[str] = None,
        Description: Optional[str] = None,
        ForecastCategoryName: Optional[str] = None,
        NextStep: Optional[str] = None,
        Probability: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates existing sale information in the system.

        Args:
            Amount: Amount of the opportunity. (required)
            StageName: Name of the opportunity stage. (required)
            CloseDate: Expected close date of the opportunity.
            Description: Description of the opportunity.
            ForecastCategoryName: Name of the forecast category.
            NextStep: Next step in the sales process.
            Probability: Probability of closing the opportunity (in percentage).
        Returns:
            API response as a dictionary.
        """
        ...

