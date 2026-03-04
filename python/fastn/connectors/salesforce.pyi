"""Fastn Salesforce connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _SalesforceCreateCustomFieldV57Metadata(TypedDict, total=False):
    label: str
    length: int
    type: str

class _SalesforceCreateCustomFieldV59Metadata(TypedDict, total=False):
    externalId: bool
    label: str
    length: int
    required: bool
    type: str

class _SalesforceCreateRemoteSiteMetadata(TypedDict, total=False):
    description: str
    disableProtocolSecurity: bool
    isActive: bool
    url: str
    urls: str

class SalesforceConnector:
    """Salesforce connector ().

    Provides 45 tools.
    """

    def salesforce_add_field_to_permission_set(
        self,
        Field: str,
        ParentId: str,
        PermissionsEdit: Optional[bool] = None,
        PermissionsRead: Optional[bool] = None,
        SobjectType: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a field-level permission to an existing permission set in Salesforce, granting read or edit access to a specific field for users assigned to that permission set. Use this when you need to extend an existing permission set to include access to a specific object field. Provide the permission set ID, field API name, and the desired access level. Do not use this to create a new permission set; use Salesforce_create_permission_set instead. Do not use this to assign a permission set to a user; use Salesforce_assign_permission_set_to_user instead. This action immediately affects the field access of all users assigned to the permission set.

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

    def salesforce_add_note_to_object(
        self,
        Body: str,
        ParentId: str,
        Title: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a new note to a specific Salesforce object such as an account, lead, contact, or opportunity. Use this tool when you need to attach a text note to a Salesforce record by providing the parent object ID, note title, and note body. Do not use this tool to update an existing note; use Salesforce_update_note instead. Do not use this tool to add attachments or files; use Salesforce_create_content_version instead. This action creates a permanent Note record in Salesforce that cannot be undone; the note record must be explicitly deleted to remove it.

        Args:
            Body: Body of the Salesforce record. (required)
            ParentId: Parent ID for the Salesforce record. (required)
            Title: Title of the Salesforce record.
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_assign_permission_set_to_user(
        self,
        AssigneeId: str,
        PermissionSetId: str,
    ) -> Dict[str, Any]:
        """Assigns a permission set to a specific user within the Salesforce environment. Use this to grant a user access to a permission set, which bundles specific permissions and customizations. Provide the user ID and permission set ID to create the assignment. Do not use this to assign users to profiles; use role assignment tools instead. This creates a new assignment and does not modify existing ones. This action immediately grants the user all permissions included in the assigned permission set. The assignment takes effect immediately and may affect the users access to Salesforce features and data.

        Args:
            AssigneeId: The ID of the Assignee. (required)
            PermissionSetId: The ID of the Permission Set. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_attach_file_to_opportunity(
        self,
        ContentDocumentId: str,
        LinkedEntityId: str,
        ShareType: str,
    ) -> Dict[str, Any]:
        """Attaches a file to an opportunity in the system. Use this when you need to link an existing file to a specific opportunity and have both the file ID and opportunity ID. Do not use this to upload a new file; upload the file first, then use this tool to attach it. Do not use this without valid file and opportunity IDs. This creates a ContentDocumentLink record and may trigger related workflows or audit logging depending on your Salesforce configuration.

        Args:
            ContentDocumentId: ID of the content document. (required)
            LinkedEntityId: ID of the linked entity. (required)
            ShareType: Type of share. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_create_account(
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
        """Creates a new account in the system. Use this tool to create a new Salesforce account when you need to add a new company or customer record to the CRM. Do not use this tool to retrieve existing accounts (use Salesforce_get_account or Salesforce_list_accounts instead) or to update existing account records (use Salesforce_update_account instead). The new account record will be immediately available for queries and related operations, and may trigger configured workflows or automated processes.

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

    def salesforce_create_apex_class(
        self,
        apexClassName: str,
        webhookUrl: str,
    ) -> Dict[str, Any]:
        """Creates a new Apex class within the Salesforce environment. Apex is Salesforces object-oriented programming language used to build custom business logic. Use this tool when you need to programmatically create a new Apex class and deploy it to your Salesforce org. Provide the class body, API version, and other required metadata. Do not use this tool to retrieve or list existing Apex classes; use list_apex_classes or get_apex_class instead. Note: This action creates a permanent record in Salesforce and cannot be undone without explicit deletion.

        Args:
            apexClassName: The name of the Apex class to be invoked. (required)
            webhookUrl: The URL for the webhook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_create_apex_trigger(
        self,
        tableEnum: str,
        triggerName: str,
        apexClassName: Optional[str] = None,
        operation: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Apex trigger within the Salesforce environment. Use this when you need to define custom business logic that executes in response to specific Salesforce events (such as before/after insert, update, delete, or undelete operations on records). Do not use this to modify an existing trigger; use the update action instead. Note: Creating a trigger activates it immediately if deployment is successful, which will cause it to execute on matching record operations.

        Args:
            tableEnum: The table enum. (required)
            triggerName: The name of the trigger. (required)
            apexClassName: The name of the Apex class.
            operation: The operation to be performed.
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_create_contact(
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
        """Creates a new contact in the system. Use this when you need to add a new contact to Salesforce with details like name, email, phone, or company. Do not use this to update an existing contact; use Salesforce_update_contact instead.

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

    def salesforce_create_content_version(
        self,
        PathOnClient: str,
        Title: str,
        VersionData: str,
    ) -> Dict[str, Any]:
        """Creates a new content version in the system. Use this when you need to upload a new file version or create a new content version for an existing content document, such as uploading a PDF, Word document, or other file type. Do not use this to retrieve existing content versions; use Salesforce_get_content_version instead. This action may trigger file versioning workflows, notifications to users with access to the associated content document, and audit log entries recording the file creation.

        Args:
            PathOnClient: Path on client for the Salesforce object. (required)
            Title: Title of the Salesforce object. (required)
            VersionData: Version data for the Salesforce object. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_create_custom_field_v57(
        self,
        FullName: str,
        Metadata: _SalesforceCreateCustomFieldV57Metadata,
    ) -> Dict[str, Any]:
        """Creates a new custom field on a Salesforce object using the Tooling API (v57.0), extending the objects data model. Use this tool when you need to add a custom field to a standard or custom Salesforce object. Provide the field definition including field type, label, and parent object. Do not use this tool to modify an existing custom field; use the update_custom_field tool instead. This action may trigger metadata deployment and validation workflows in your Salesforce org. Custom fields, once created, require explicit deletion and may have dependencies that must be removed first.

        Args:
            FullName: The full name of the user or entity. (required)
            Metadata: Metadata associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_create_custom_field_v59(
        self,
        FullName: str,
        Metadata: _SalesforceCreateCustomFieldV59Metadata,
    ) -> Dict[str, Any]:
        """Creates a new custom field on a Salesforce object using the Tooling API (v59.0), extending the objects data model. Use this tool when you need to add a custom field to a standard or custom Salesforce object and require API v59.0 compatibility. Provide the field definition including field type, label, and parent object. Do not use this tool to modify an existing custom field; use the update_custom_field tool instead. This action may trigger metadata deployment and validation workflows in your Salesforce org. Custom fields, once created, require explicit deletion and may have dependencies that must be removed first.

        Args:
            FullName: Full name of the user or entity. (required)
            Metadata: Metadata related to the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_create_opportunity(
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
        """Creates a new opportunity record in Salesforce. Use this when you need to add a new sales opportunity to track a potential deal, including details such as the opportunity name, account, amount, close date, and stage. Do not use this tool to update an existing opportunity (use update_opportunity instead). This action creates a permanent record in Salesforce and cannot be undone; delete the record separately if needed.

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

    def salesforce_create_permission_set(
        self,
        Label: str,
        Name: str,
        Description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new permission set in Salesforce that can be assigned to users to control their access to fields, objects, and features. Use this when you need to define a new custom permission set from scratch. Provide the permission set name, label, and optional description. Do not use this to add field-level access to an existing permission set; use Salesforce_add_field_to_permission_set instead. Do not use this to assign the permission set to a user; use Salesforce_assign_permission_set_to_user instead. This action creates a permanent record and cannot be undone without explicit deletion.

        Args:
            Label: Label for the Salesforce object. (required)
            Name: Name of the Salesforce object. (required)
            Description: Description of the Salesforce object.
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_create_remote_site(
        self,
        FullName: str,
        Metadata: _SalesforceCreateRemoteSiteMetadata,
    ) -> Dict[str, Any]:
        """Creates a new remote site setting within the Salesforce environment. Use this tool when you need to allow Salesforce to make outbound HTTP requests to an external domain by configuring a remote site setting. Provide the remote site name and the target URL. Do not use this tool if you only want to retrieve or modify existing remote site settings; use list_remote_sites or update_remote_site instead. Note: This action creates a permanent record in Salesforce and cannot be undone without explicit deletion.

        Args:
            FullName: The full name of the user or entity. (required)
            Metadata: Metadata associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_create_sale(
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
        """Creates a new sale (Opportunity) record in Salesforce with specified details such as name, account, stage, and amount. Use this when a user needs to add a new sales opportunity to track. To modify an existing sale use update_sale instead. This action triggers any configured Salesforce workflow rules and automations for opportunity creation.

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

    def salesforce_delete_account(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing account record from Salesforce by its account ID. This action is irreversible and cannot be undone. Use this when you need to remove an account record that is no longer needed or was created in error. Side effects may include removal of related contacts, opportunities, cases, and other child records depending on your Salesforce configuration and deletion rules. Do not use this if you only want to deactivate or modify the account; use Salesforce_update_account instead.

        Args:
            accountId: The ID of the Salesforce account. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Deletes a contact from the system. Use this when you need to remove a contact record by its ID. This action is permanent and cannot be undone. Side effects may include: removal of related activities, opportunity associations, and any dependent child records depending on Salesforce configuration. Do not use this if you only want to archive or deactivate the contact; use Salesforce_update_contact instead if you need to change its status.

        Args:
            contactId: ID of the contact in Salesforce. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_delete_opportunity(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific opportunity record from Salesforce by its ID. This action cannot be undone. Use this tool when the user wants to remove an opportunity that is no longer needed or was created in error. Do not use this tool if the user wants to archive or close an opportunity instead of permanently removing it, or if they want to modify opportunity details (use Salesforce_update_opportunity instead).

        Args:
            opportunityId: ID of the opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_delete_sale(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Deletes a sale (Opportunity) from the system by its ID. Use this when you need to permanently remove a sale record that is no longer relevant or was created in error. Do not use this to archive or close a sale—use Salesforce_update_sale to change its status instead. Note: Deletion may cascade to related records (e.g., related activities, notes) and is logged in Salesforces audit trail. This action is permanent and cannot be undone.

        Args:
            opportunityId: The ID of the Salesforce opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_generate_access_token(
        self,
        client_id: str,
        client_secret: str,
        grant_type: str,
        password: str,
        username: str,
    ) -> Dict[str, Any]:
        """Generates an OAuth 2.0 access token for authentication to the Salesforce API. Use this tool when you need to authenticate requests to Salesforce endpoints or when the current authentication token has expired. Do not use this tool if you already have a valid access token; instead, reuse the existing token to avoid unnecessary API calls.

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

    def salesforce_generate_client_credentials_token(
        self,
        client_id: str,
        client_secret: str,
        domain: str,
    ) -> Dict[str, Any]:
        """Generates an OAuth2 access token using the client credentials flow for service-to-service authentication with Salesforce. Use this to obtain a bearer token before making API calls to Salesforce when no user context is required. Provide the domain, client ID, and client secret. Do not use this for user-interactive authentication flows; use user-based OAuth2 flows instead. Do not use this if a valid token already exists; reuse the existing token to avoid unnecessary API calls.

        Args:
            client_id: Client ID for Salesforce API authentication. (required)
            client_secret: Client secret for Salesforce API authentication. (required)
            domain: Salesforce domain. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_account(
        self,
        accountId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single Salesforce account record by its ID, including all account fields such as name, industry, billing address, annual revenue, and custom fields. Use this tool to retrieve detailed information about a specific Salesforce account when you have its account ID. Do not use this tool to list multiple accounts or search for accounts by criteria (use Salesforce_list_accounts or Salesforce_search_accounts instead). This tool requires a specific account ID.

        Args:
            accountId: The ID of the Salesforce account. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_apex_class_by_name(
        self,
        apexClassName: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific Apex class definition from Salesforces Tooling API by querying its name, useful for inspecting custom code components. Use this tool when you need to retrieve metadata about a specific Apex class, such as when auditing custom code or verifying class definitions. Do not use this to retrieve Apex triggers, test classes, or Apex pages; use the appropriate query endpoints for those component types instead.

        Args:
            apexClassName: The name of the Apex class to execute. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_apex_trigger_by_name(
        self,
        apexTriggerName: str,
    ) -> Dict[str, Any]:
        """Retrieves a single Apex trigger metadata record by its name using the Salesforce Tooling API. Use this to fetch the metadata and details of a specific Apex trigger by providing its exact name. This is useful for inspecting trigger code, status, or related metadata in development or deployment workflows. Do not use this to list all Apex triggers; use Salesforce_list_apex_triggers or a search query instead. This tool requires the exact trigger name and returns only a single trigger record.

        Args:
            apexTriggerName: The name of the Apex trigger. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Retrieves contact information for a specific contact by ID. Use this when you need to fetch detailed information about a single contact, such as their email, phone, company, or other attributes. Do not use this to retrieve multiple contacts; use Salesforce_list_contacts instead. Do not use this to search by name or other criteria; use Salesforce_search_contacts instead.

        Args:
            contactId: The ID of the contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_content_document_by_id(
        self,
        contentDocumentId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific content document record by its ID, including metadata such as title, file size, and creation date. Use this tool when you have a specific ContentDocument ID and need to retrieve its metadata, including title, file type, and owner information. This is useful for accessing document properties before downloading file content. Do not use this tool to retrieve the actual file contents; use Salesforce_get_file_content instead. Do not use this to search for documents by name or other criteria; use Salesforce_search_content_documents instead.

        Args:
            contentDocumentId: The ID of the content document in Salesforce. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_content_version(
        self,
        contentVersionId: str,
    ) -> Dict[str, Any]:
        """Retrieves content version information from the system. Use this when you need to retrieve a specific content version by its ID to view details such as version number, file name, file type, file size, or creation metadata. Do not use this to list all content versions; use Salesforce_list_content_versions instead.

        Args:
            contentVersionId: The ID of the content version. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_file_by_opportunity_id(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Retrieves a file associated with a specific opportunity ID from the system. Use this when you need to fetch a file linked to a particular opportunity and have the opportunity ID available. Do not use this to list all files in an opportunity; use a list files tool instead. Do not use this without an opportunity ID.

        Args:
            opportunityId: ID of the Salesforce opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_file_content(
        self,
        attributeUrl: str,
    ) -> Dict[str, Any]:
        """Retrieves the binary content (file data) of a document stored in Salesforce, such as PDFs, images, or other file types. Use this tool when you need to download or access the actual file data (binary content) of a document. Provide the documents attribute URL, typically obtained from a ContentDocument record. This is required to download PDFs, images, or other attachments. Do not use this tool to retrieve document metadata such as title or creation date; use Salesforce_get_content_document_by_id instead. Do not use this if you do not have the attribute URL.

        Args:
            attributeUrl: The URL for accessing the attribute. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_lead(
        self,
        leadId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information for a specific lead by ID from Salesforce. Use this when you have a lead ID and need to fetch all details about that lead, including name, company, email, phone, status, and custom fields. Do not use this to search for leads by name or email; use a search or query tool instead. Do not use this to retrieve metadata about the Lead object; use Salesforce_get_resource_properties instead.

        Args:
            leadId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_opportunity(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single opportunity record from Salesforce by its ID. Use this when you need to fetch detailed information about a specific opportunity, such as its stage, amount, close date, and owner. Requires the opportunity ID. Do not use this tool to search for opportunities by criteria (use search_opportunities instead) or to list all opportunities (use list_opportunities instead).

        Args:
            opportunityId: The ID of the opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_resource_properties(
        self,
        resourceName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves metadata properties and field information for a specified Salesforce object resource. Use this when you need to understand the structure, available fields, data types, or validation rules for a specific Salesforce object (like Lead, Account, Opportunity, or custom objects). Do not use this to retrieve actual record data; use Salesforce_get_lead, Salesforce_get_account, or other object-specific retrieval tools for that purpose.

        Args:
            resourceName: Resource ( eg: Company, Contact, Account )
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_sale(
        self,
        opportunityId: str,
    ) -> Dict[str, Any]:
        """Retrieves a single sale (Opportunity) record from Salesforce by its ID. Use this to get detailed information about a specific sale opportunity including stage, amount, and close date. To search or filter multiple sales use search_sales or list_sales instead.

        Args:
            opportunityId: The ID of the opportunity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_user(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the authenticated users profile information from Salesforce, including user ID, name, email, and organization details. Use this to fetch details about the currently logged-in user for identity verification, notification addressing, or workflow logic. Do not use this to retrieve details for other users by ID; this endpoint always returns the current authenticated users information only.
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_user_details(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the authenticated Salesforce users profile information, including user ID, email, name, and account details from the OAuth2 userinfo endpoint. Use this tool when you need to get information about the currently authenticated user, such as verifying user identity, retrieving the users email for notifications, or obtaining user metadata for workflow logic. Do not use this to retrieve information about other users; for that, use the Salesforce user records query endpoint instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_get_version_data(
        self,
        contentVersionId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the version data (binary content) for a specific ContentVersion record in Salesforce by its ID. Use this to download or retrieve the binary content of a specific file version stored in Salesforces Files library (ContentVersion). Provide the ContentVersion ID to fetch the associated version data. Do not use this to retrieve ContentVersion metadata or list all versions of a file; use Salesforce_query_content_versions or list_content_versions instead. This tool returns only the binary file content, not record details.

        Args:
            contentVersionId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_list_accounts(
        self,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of account records from Salesforce using a SOQL query. Use this to fetch all accounts or to retrieve multiple account records matching specific criteria such as industry, owner, or billing region, for customer management, sales reporting, or account analysis. To retrieve a single account by ID, use Salesforce_get_account instead.

        Args:
            q: Query parameter for filtering results.
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_list_contacts(
        self,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of contact records from Salesforce using a SOQL query. Use this to fetch all contacts or to retrieve contacts matching specific query criteria such as name, email, account, or owner. Do not use this to retrieve a single contact by ID; use Salesforce_get_contact instead. Do not use this to search contacts by free-text criteria; use Salesforce_search_contacts instead.

        Args:
            q: The query string for the Salesforce API.
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_list_leads(
        self,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of lead records from Salesforce using a SOQL query. Use this tool when you need to fetch all leads or query leads matching specific criteria such as status, owner, company, or date range. Supports filtering and pagination through query parameters. Do not use this tool to retrieve a single lead by ID; use Salesforce_get_lead instead.

        Args:
            q: Query parameter for Salesforce search.
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_list_opportunities(
        self,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of opportunity records from Salesforce using a SOQL query. Use this to fetch all opportunities or to retrieve opportunities matching specific filter criteria such as stage, owner, amount, or close date. To retrieve a single opportunity by ID, use Salesforce_get_opportunity instead.

        Args:
            q: Query string parameter for Salesforce API.
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_list_sales(
        self,
        q: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of sale (Opportunity) records from Salesforce using a SOQL query. Use this to fetch all sales records or to retrieve multiple sales matching specific criteria such as stage, owner, amount range, or close date, for reporting, analysis, or workflow automation. To retrieve a single sale by ID, use Salesforce_get_sale instead.

        Args:
            q: Query parameter for the Salesforce API.
        Returns:
            API response as a dictionary.
        """
        ...

    def salesforce_update_account(
        self,
        Name: str,
        accountId: str,
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
        """Updates existing account information in Salesforce by account ID. Use this to modify account fields such as name, phone, billing address, website, industry, or custom fields. Provide only the fields you want to change along with the account ID. Side effects may include triggering workflow rules and automation processes depending on your Salesforce configuration. Do not use this to create a new account; use Salesforce_create_account instead. Do not use this to delete an account; use Salesforce_delete_account instead.

        Args:
            Name: The name of the account. (required)
            accountId: The ID of the account (for update operations). (required)
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

    def salesforce_update_contact(
        self,
        AccountId: str,
        FirstName: str,
        LastName: str,
        contactId: str,
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
        """Updates existing contact information in the system. Use this to modify fields like email, phone, address, or other contact details for an existing contact record by its ID. Provide only the fields you want to change. Side effects may include: triggering workflow rules, updating related record fields, and sending field change notifications depending on Salesforce configuration. Do not use this to create a new contact; use Salesforce_create_contact instead. Do not use this to delete a contact; use Salesforce_delete_contact instead.

        Args:
            AccountId: The ID of the associated Account. (required)
            FirstName: The contact's first name. (required)
            LastName: The contact's last name. (required)
            contactId: The ID of the contact (used for updates). (required)
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

    def salesforce_update_opportunity(
        self,
        AccountId: str,
        Name: str,
        opportunityId: str,
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
        """Modifies an existing opportunity record in Salesforce by its ID. Use this tool when the user wants to update opportunity details such as name, stage, amount, close date, or other custom fields. Do not use this tool to delete an opportunity (use Salesforce_delete_opportunity instead) or to retrieve opportunity data (use Salesforce_get_opportunity instead).

        Args:
            AccountId: The ID of the associated Account. (required)
            Name: The name of the opportunity. (required)
            opportunityId: The ID of the opportunity. (required)
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

    def salesforce_update_sale(
        self,
        Amount: int,
        StageName: str,
        opportunityId: str,
        CloseDate: Optional[str] = None,
        Description: Optional[str] = None,
        ForecastCategoryName: Optional[str] = None,
        NextStep: Optional[str] = None,
        Probability: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates an existing sale (Opportunity) record with new information. Use this to modify sale details such as stage, amount, close date, owner, or custom fields for a specific sale by its ID. Do not use this to delete a sale—use Salesforce_delete_sale instead. Note: Updates may trigger workflows, field validations, and are logged in Salesforces audit trail.

        Args:
            Amount: Amount of the opportunity. (required)
            StageName: Name of the opportunity stage. (required)
            opportunityId: ID of the opportunity to be updated. (required)
            CloseDate: Expected close date of the opportunity.
            Description: Description of the opportunity.
            ForecastCategoryName: Name of the forecast category.
            NextStep: Next step in the sales process.
            Probability: Probability of closing the opportunity (in percentage).
        Returns:
            API response as a dictionary.
        """
        ...

