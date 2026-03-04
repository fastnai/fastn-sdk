"""Fastn HubSpot connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _HubSpotAddNoteProperties(TypedDict, total=False):
    hs_note_body: str
    hs_timestamp: str

class _HubSpotCreateCompanyProperties(TypedDict, total=False):
    annualrevenue: int
    city: str
    country: str
    description: str
    domain: str
    industry: str
    lifecyclestage: str
    name: str
    numberofemployees: int
    phone: str
    state: str

class _HubSpotCreateContactProperties(TypedDict, total=False):
    company: str
    email: str
    firstname: str
    lastname: str
    lifecyclestage: str
    phone: str
    website: str

class _HubSpotCreateDealProperties(TypedDict, total=False):
    amount: str
    annualcontractvalue: str
    closedate: str
    currency: str
    dealname: str
    dealstage: str
    dealtype: str
    description: str
    forecastcategory: str
    hubspot_owner_id: str
    pipeline: str
    priority: str
    probability: str
    source: str

class _HubSpotCreateEngagementAssociations(TypedDict, total=False):
    dealIds: List[Any]

class _HubSpotCreateEngagementEngagement(TypedDict, total=False):
    type: str

class _HubSpotCreateEngagementMetadata(TypedDict, total=False):
    body: str

class _HubSpotCreateLineItemProperties(TypedDict, total=False):
    description: str
    discount: float
    hs_billing_frequency: str
    hs_mrr: float
    hs_product_id: str
    hs_recurring_billing_end_date: str
    hs_recurring_billing_start_date: str
    hs_tcv: float
    name: str
    price: float
    quantity: int

class _HubSpotCreateProductProperties(TypedDict, total=False):
    description: str
    hs_cost_of_goods_sold: float
    hs_recurring_billing_start_date: str
    name: str
    price: float

class _HubSpotUpdateCompanyProperties(TypedDict, total=False):
    annualrevenue: int
    city: str
    country: str
    description: str
    domain: str
    hubspot_owner_id: str
    industry: str
    lifecyclestage: str
    name: str
    numberofemployees: int
    phone: str
    state: str

class _HubSpotUpdateContactProperties(TypedDict, total=False):
    company: str
    email: str
    firstname: str
    lastname: str
    lifecyclestage: str
    phone: str
    website: str

class _HubSpotUpdateDealProperties(TypedDict, total=False):
    type: str

class _HubSpotUpdateLineItemProperties(TypedDict, total=False):
    description: str
    discount: float
    hs_billing_frequency: str
    hs_mrr: float
    hs_recurring_billing_end_date: str
    hs_recurring_billing_start_date: str
    hs_tcv: float
    name: str
    price: float
    quantity: int

class _HubSpotUpdateProductProperties(TypedDict, total=False):
    description: str
    hs_folder: str
    hs_sku_: str
    hs_status: str
    name: str
    price: str

class _HubSpotUpdateTicketProperties(TypedDict, total=False):
    property_checkbox: str
    property_date: str
    property_dropdown: str
    property_multiple_checkboxes: str
    property_number: str
    property_radio: str
    property_string: str

class _HubSpotUpsertWebhookSettingsThrottling(TypedDict, total=False):
    maxConcurrentRequests: int
    period: str

class HubspotConnector:
    """HubSpot connector ().

    Provides 68 tools.
    """

    def hub_spot_add_contact_to_list(
        self,
        emails: List[Any],
        id: str,
        vids: List[Any],
    ) -> Dict[str, Any]:
        """Adds one or more contacts to a specified HubSpot list using email addresses or contact VIDs (unique contact identifiers in HubSpot). Requires id (list ID) and either emails (array of valid email strings) or vids (array of valid contact VIDs). Returns the count of contacts successfully added, contacts that were discarded (already in list or invalid), invalid email addresses, and invalid VIDs. Use this when you need to bulk-add contacts to a static or dynamic list. Do not use this to remove contacts from a list; use the remove contacts endpoint instead. Do not use this to create a new list; use the create list endpoint instead. Side effect: contacts added to the list will be included in any automated workflows, email campaigns, or segmentation rules associated with that list. This action can be undone by removing contacts from the list using the remove contacts endpoint.

        Args:
            emails: An array of email addresses. (required)
            id: An identifier for the URL. (required)
            vids: An array of HubSpot contact IDs (vids). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_add_line_item_to_deal(
        self,
        body: List[Any],
        dealId: Optional[str] = None,
        lineItemId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Associates an existing line item with a specific deal in HubSpot. Use this when you need to link an existing line item to a deal to track products or services included in that deal. This creates an association record and may update the deals total value or product count if those fields are configured to aggregate from line items. Side effects may include triggering workflows or automations tied to line item associations. Do not use this to create a new line item; use HubSpot_create_line_item instead. Do not use this if the line item or deal does not already exist in the system.

        Args:
            body:  (required)
            dealId: 
            lineItemId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_add_note(
        self,
        associations: List[Any],
        properties: _HubSpotAddNoteProperties,
    ) -> Dict[str, Any]:
        """Creates and adds a new note to a CRM record (such as a contact, deal, or company) in HubSpot. Use this when you need to document interactions, record follow-ups, or attach internal comments to a CRM record. Do not use this to update an existing note; use HubSpot_update_note instead. The note will appear in the associated records activity timeline.

        Args:
            associations:  (required)
            properties: Properties of the HubSpot object. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_batch_create_deals(
        self,
        inputs: List[Any],
    ) -> Dict[str, Any]:
        """Creates multiple deals in the deal management system in a batch. Use this when you need to create multiple deals at once to improve performance and reduce API calls. To create a single deal, use HubSpot_create_deal instead. This action cannot be undone; ensure the deal data is correct before proceeding.

        Args:
            inputs:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_association(
        self,
        fromResource: str,
        inputs: List[Any],
        toResource: str,
    ) -> Dict[str, Any]:
        """Creates associations in batch between two HubSpot object types (e.g., contacts to deals, companies to opportunities). Use this to link multiple pairs of objects in a single API call. Specify the fromResource and toResource object types as path parameters and provide the association pairs in the request body. Do not use this to delete associations; use the appropriate delete association tool instead. Do not use this to create a company-to-company association; use HubSpot_create_company_associations instead.

        Args:
            fromResource: source resource. (required)
            inputs:  (required)
            toResource: destination resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_company(
        self,
        properties: _HubSpotCreateCompanyProperties,
    ) -> Dict[str, Any]:
        """Creates a new company record in HubSpot. Use this when you need to add a new company with details such as name, website, industry, and other company properties. Do not use this to modify an existing company; use HubSpot_update_company instead.

        Args:
            properties: Properties of the company being created or updated in HubSpot. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_company_associations(
        self,
        body: List[Any],
        childId: str,
        parentId: str,
    ) -> Dict[str, Any]:
        """Creates associations between two companies in HubSpots association management system. Use this to link a parent company to a child company when you want to establish a relationship (such as parent-subsidiary, partner, or affiliated company relationships) between them in the CRM. Do not use this to associate contacts with companies; use the contacts association endpoints instead. Do not use this to create associations between companies and deals or other object types; use the appropriate object-specific association endpoints. Creating an association may trigger workflows or automations configured on your HubSpot account.

        Args:
            body:  (required)
            childId: Identifier for the specific child resource. (required)
            parentId: Identifier for the parent resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_contact(
        self,
        properties: Optional[_HubSpotCreateContactProperties] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact record in HubSpot CRM. Use this when you need to add a new contact with properties such as name, email, phone, or other custom fields. Do not use this to update an existing contact; use HubSpot_update_contact instead.

        Args:
            properties: Properties of the contact.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_custom_property(
        self,
        description: str,
        fieldType: str,
        groupName: str,
        label: str,
        name: str,
        resource: str,
        type: str,
        hasUniqueValue: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new custom property on a HubSpot object type (e.g., contacts, deals, companies). Use this to add a new custom field for tracking data not covered by default HubSpot properties. Provide the resource (object type) as a path parameter. Do not use this to update an existing property; use the update_custom_property tool instead. This custom property will be available immediately for all objects of the specified type and may trigger webhook notifications.

        Args:
            description: A description of the custom object. (required)
            fieldType: The type of field for the custom object. (required)
            groupName: The name of the group the custom object belongs to in HubSpot. (required)
            label: The label for the custom object. (required)
            name: The name of the custom object. (required)
            resource: The resource path for the HubSpot API endpoint. (required)
            type: The type of the custom object. (required)
            hasUniqueValue: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_deal(
        self,
        properties: Optional[_HubSpotCreateDealProperties] = None,
    ) -> Dict[str, Any]:
        """Creates a new deal in the deal management system. Use this when you need to add a new deal to HubSpot with specified properties such as deal name, amount, and stage. Do not use this to update an existing deal; use HubSpot_update_deal instead. This action may trigger associated workflows or notifications based on your HubSpot configuration. The created deal can be deleted but the action itself cannot be undone.

        Args:
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_engagement(
        self,
        associations: _HubSpotCreateEngagementAssociations,
        attachments: List[Any],
        engagement: _HubSpotCreateEngagementEngagement,
        metadata: _HubSpotCreateEngagementMetadata,
    ) -> Dict[str, Any]:
        """Creates a new engagement (such as a note, email, call, or task) associated with a contact or company in HubSpot. Use this when you need to log an interaction or activity with a contact or company. Do not use this to update or modify an existing engagement; use HubSpot_update_engagement instead. This engagement will be visible in the contact or company timeline and may trigger automated workflows.

        Args:
            associations: Associations related to the request. (required)
            attachments:  (required)
            engagement: Details about the engagement. (required)
            metadata: Metadata associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_folder(
        self,
        name: str,
        parentPath: str,
        parentFolderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new folder in HubSpots file management system to organize and store files. Use this to create a new folder when organizing files in HubSpot or when the user requests to create a folder for storing documents. Do not use this to upload files; use the upload_file tool instead. Do not use this to move or rename existing folders; use update_folder instead.

        Args:
            name: The name of the folder or entity. (required)
            parentPath: The path to the parent directory. (required)
            parentFolderId: The identifier of the parent folder.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_line_item(
        self,
        properties: Optional[_HubSpotCreateLineItemProperties] = None,
    ) -> Dict[str, Any]:
        """Creates a new line item in HubSpots line item management system. Use this when you need to add a new line item to associate with a deal or order. Do not use this to update an existing line item; use HubSpot_update_line_item instead. Note: Creating a line item may trigger associated workflows or update related deal totals.

        Args:
            properties: Properties of the deal being created or updated.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_list(
        self,
        dynamic: bool,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new list in HubSpots list management system. Use this when you need to set up a new contact list for marketing campaigns, segmentation, or organization purposes. Do not use this to retrieve an existing list; use HubSpot_get_list instead. The newly created list will be immediately available for adding contacts and can be used in workflows and automations.

        Args:
            dynamic: Dynamic flag indicating a dynamic property in the HubSpot API request. (required)
            name: Name field for the HubSpot API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_product(
        self,
        properties: Optional[_HubSpotCreateProductProperties] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the product management system. Use this when you need to add a new product with details such as name, description, price, or other product attributes to HubSpot. Do not use this to retrieve existing product details (use HubSpot_get_product instead) or to modify an existing product. Once created, the product record can be modified or deleted in HubSpot.

        Args:
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_ticket(
        self,
        properties: Dict[str, Any],
        associations: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new ticket in HubSpots ticket management system. Use this when you need to create a new support ticket or issue record for a customer or contact. Do not use this to update an existing ticket; use HubSpot_update_ticket instead. This action will trigger any automated workflows or notifications configured for new tickets in your HubSpot account. Created tickets cannot be deleted through the API.

        Args:
            properties: Additional properties for the HubSpot object. (required)
            associations: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_create_user(
        self,
        email: str,
        firstName: str,
        lastName: str,
        primaryTeamId: str,
        roleId: str,
        secondaryTeamIds: List[Any],
        sendWelcomeEmail: bool,
    ) -> Dict[str, Any]:
        """Creates a new user in the user management system. Use this when you need to add a new user account to HubSpot. Do not use this to update an existing user; use HubSpot_update_user instead. The new user will be able to access HubSpot immediately after creation.

        Args:
            email: The user's email address. (required)
            firstName: The user's first name. (required)
            lastName: The user's last name. (required)
            primaryTeamId: The ID of the user's primary team. (required)
            roleId: The ID of the user's role. (required)
            secondaryTeamIds: An array of IDs for the user's secondary teams. (required)
            sendWelcomeEmail: Whether to send a welcome email to the new user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Deletes a contact from the contact management system. Use this when you need to permanently remove a contact record by providing its contact ID. Do not use this if you intend to archive or soft-delete the contact; confirm the contact ID before deletion to avoid accidental removal. This action is permanent and cannot be undone. Side effects may include removal of all associated interactions, emails, and relationships linked to this contact.

        Args:
            contactId: The ID of the HubSpot contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_delete_deal(
        self,
        dealId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a deal from HubSpot by its deal ID and removes all associated records and history. This action may cascade to related objects (e.g., deal activities, custom properties, and associations with contacts or companies). Use this when the user explicitly requests to remove a deal or when a deal is no longer relevant and must be purged from the system. Do not use this to update or modify a deal; use HubSpot_update_deal instead. Do not use this to retrieve deal information; use HubSpot_get_deal instead. This action cannot be undone and all deal-related data will be lost. Ensure the deal ID is correct before confirming the deletion.

        Args:
            dealId: The ID of the deal to be accessed in the HubSpot API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_delete_line_item_from_deal(
        self,
        body: List[Any],
        dealId: Optional[str] = None,
        lineItemId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently removes a line item association from a specific deal in HubSpot. Use this when you need to disassociate a product or service line item from an existing deal record. Do not use this to delete the entire deal; use HubSpot_delete_deal instead. Do not use this to delete the line item object itself; use a delete_line_item tool instead. This action updates the deals composition and may trigger automated workflows configured for deal modifications. This deletion is permanent and cannot be undone.

        Args:
            body:  (required)
            dealId: 
            lineItemId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_delete_product(
        self,
        productId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a product from the product management system. Use this to remove a product by its product ID. This action is irreversible and will permanently remove the product. Any associations with this product may also be affected.

        Args:
            productId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_delete_ticket(
        self,
        ticketId: str,
    ) -> Dict[str, Any]:
        """Deletes a ticket from the ticket management system. Use this when you need to permanently remove a ticket and all associated data. Do not use this if you want to close or resolve a ticket instead—use HubSpot_update_ticket to change the ticket status. This action cannot be undone and will remove all associated communications and metadata.

        Args:
            ticketId: The HubSpot ticket identifier included in the API request URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_delete_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Deletes a user from the user management system. Use this when you need to permanently remove a user account from HubSpot. Do not use this if you want to deactivate a user temporarily; contact an administrator for alternative account management options. This action is permanent and cannot be undone.

        Args:
            userId: The ID of the user for the HubSpot API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        connection: Dict[str, Any],
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Exchanges an OAuth authorization code or client credentials for a HubSpot access token. Use this to authenticate API requests to HubSpot when initially setting up the connection. The returned token is required for all subsequent HubSpot API calls. Do not use this to refresh an existing token; use HubSpot_refresh_token instead. Do not use this for non-HubSpot authentication.

        Args:
            client_id: Client ID for the HubSpot application. (required)
            client_secret: Client secret for the HubSpot application. (required)
            code: Authorization code received from the HubSpot OAuth flow. (required)
            connection: Details about the connection to the HubSpot API. (required)
            redirect_uri: Redirect URI registered for the HubSpot application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_company(
        self,
        companyId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific company from the company management system. Use this when you need to fetch company information by its unique company ID. To retrieve multiple companies or search across all companies, use HubSpot_list_companies instead.

        Args:
            companyId: The ID of the HubSpot company. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_contact(
        self,
        contactId: str,
        associations: Optional[str] = None,
        properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific contact by their ID from HubSpot. Use this when you need to fetch details for a single contact and you have their contact ID. Do not use this tool to retrieve multiple contacts (use HubSpot_list_contacts instead) or to search for contacts by name or email (use HubSpot_search_contacts instead).

        Args:
            contactId: The ID of the contact in HubSpot. (required)
            associations: 
            properties: properties to return
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_contact_association(
        self,
        contactId: str,
        objectType: str,
        archived: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the association of a contact in the contact management system. Use this to retrieve associated objects (such as companies, deals, or tickets) linked to a specific contact by its ID. Do not use this to list all contacts or to search for contacts by keyword; use a contact list or search tool instead.

        Args:
            contactId: The ID of the HubSpot contact. (required)
            objectType: The type of object being accessed in the HubSpot API. (required)
            archived: Specifies whether to include archived records in the response.  (e.g., 'true' or 'false').
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_deal(
        self,
        dealId: str,
        associations: Optional[str] = None,
        properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific deal from the deal management system. Use this when you need to fetch information about a single deal by its deal ID. Do not use this to list all deals or search deals by criteria; use HubSpot_list_deals or HubSpot_search_deals instead.

        Args:
            dealId: The ID of the deal in HubSpot. (required)
            associations: 
            properties: Fields to return in the response
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_deal_notes_association(
        self,
        dealId: str,
        archived: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all notes associated with a specific deal in HubSpot by the deals unique ID. Use this to fetch the list of notes linked to a particular deal. Do not use this to list all deals; use HubSpot_list_deals instead. Do not use this to retrieve associations with object types other than notes; use HubSpot_get_contact_association or the appropriate object-specific association tool for other types.

        Args:
            dealId: ID of the HubSpot deal to access. (required)
            archived: Whether to include archived deals.  Possible values depend on the specific HubSpot endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_engagement(
        self,
        noteId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific engagement (such as a note, call, email, or meeting) from HubSpot by its unique engagement ID. Use this when you need to fetch the complete information for a single engagement record. Do not use this to list all engagements or filter by criteria; use HubSpot_list_engagements instead.

        Args:
            noteId: ID of the HubSpot note. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_file(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Retrieves metadata and details of a specific file from HubSpots file management system by its unique file ID. Use this when you need to access a files properties, URL, or storage information. Do not use this to list all files; use a list_files endpoint instead. Do not use this to retrieve file content directly from a URL; use HubSpot_get_file_content instead.

        Args:
            fileId: The ID of the file in HubSpot. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_file_content(
        self,
        baseUrl: str,
    ) -> Dict[str, Any]:
        """Retrieves the content of a file from a given URL, typically a file associated with a HubSpot record such as an attachment or document. Use this to download or read the binary or text content of a file when you have a direct file URL. Do not use this to retrieve file metadata by file ID; use HubSpot_get_file instead. Do not use this to access files from non-HubSpot sources.

        Args:
            baseUrl: The base URL for the HubSpot API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_line_item(
        self,
        line_item_id: str,
        properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific line item by its unique ID from HubSpot. Use this when you need to fetch the properties, pricing, quantity, and other details of an individual line item. Do not use this to retrieve multiple line items or list all line items; use HubSpot_list_line_items instead.

        Args:
            line_item_id: The ID of the line item. (required)
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_list(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific contact list from HubSpot by its list ID. Use this when you need to fetch information about a particular list, such as its name, description, member count, or creation date. Do not use this to create a new list; use HubSpot_create_list instead. To retrieve all lists, use HubSpot_list_lists instead.

        Args:
            id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_product(
        self,
        productId: str,
        archived: Optional[str] = None,
        associations: Optional[str] = None,
        idProperty: Optional[str] = None,
        properties: Optional[str] = None,
        propertiesWithHistory: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific product from the product management system. Use this to get product information by product ID when you need to access details like name, description, price, or other product attributes. Do not use this to create new products (use HubSpot_create_product instead) or to list all products.

        Args:
            productId:  (required)
            archived: 
            associations: 
            idProperty: 
            properties: 
            propertiesWithHistory: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_signed_url(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Generates a signed URL for secure file access from the file management system. Use this to obtain a time-limited URL that grants temporary access to a specific file stored in HubSpots file manager. Provide the file ID to retrieve its signed URL. Do not use this to list files or retrieve file metadata; use appropriate file listing or metadata endpoints instead.

        Args:
            fileId: ID of the file for the HubSpot HubSpot endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_ticket(
        self,
        ticketId: str,
        archived: Optional[str] = None,
        associations: Optional[str] = None,
        idProperty: Optional[str] = None,
        properties: Optional[str] = None,
        propertiesWithHistory: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific ticket from the ticket management system. Use this to fetch a single ticket by its ID when you need full ticket information including status, priority, subject, and associated contacts. To retrieve multiple tickets or list all tickets, use HubSpot_list_tickets instead.

        Args:
            ticketId: The unique identifier of the ticket in HubSpot. (required)
            archived: Flag to include archived items.
            associations: Association-related parameter for the request.
            idProperty: Identifier for the primary property used in the request.
            properties: List of properties to include or filter in the request.
            propertiesWithHistory: Include properties history in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific user from the user management system. Use this when you need to fetch information about a single user by their ID. Do not use this to retrieve multiple users; use a list users tool instead.

        Args:
            userId: The ID of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_user_details(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the current authenticated users details from HubSpot. Use this to access information about the logged-in user, including their user ID, email, and account information. Do not use this to retrieve details about a specific contact or customer in HubSpot; use contact-specific endpoints for that purpose.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_get_user_roles(
        self,
    ) -> Dict[str, Any]:
        """Retrieves roles assigned to a user from the user management system. Use this to fetch the roles and permissions associated with a specific user to determine their access level and capabilities. Do not use this to list all users or to modify user roles; use the user list or update user role tools instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_associations(
        self,
        fromObjectType: str,
        inputs: List[Any],
        toObjectType: str,
    ) -> Dict[str, Any]:
        """Retrieves batch associations between two HubSpot object types (e.g., contacts and companies) by providing the source and target object types. Use this to retrieve all associations linking two specific object types in HubSpot (e.g., which companies are associated with which contacts). Specify the fromObjectType and toObjectType in the request. Do not use this to create or delete associations; use the create or delete association tools instead. Do not use this to retrieve associations for a single object; use HubSpot_get_contact_association or the appropriate object-specific association tool instead.

        Args:
            fromObjectType:  (required)
            inputs:  (required)
            toObjectType:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_companies(
        self,
        after: Optional[str] = None,
        limit: Optional[str] = None,
        properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of companies from the company management system. Use this to fetch all companies or a collection of companies for bulk operations or displaying company lists. To retrieve a single companys detailed information by ID, use HubSpot_get_company instead.

        Args:
            after: Cursor for pagination.  Use the 'after' value from the previous response to fetch subsequent pages.
            limit: The maximum number of results to return.
            properties: Specifies which properties to include in the response.  Use this to control the data returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_contacts(
        self,
        after: Optional[str] = None,
        associations: Optional[str] = None,
        limit: Optional[str] = None,
        properties: Optional[str] = None,
        updatedAt: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of contacts from the contact management system. Use this to retrieve all contacts in your HubSpot account, or to get contact records when you need to access contact data for marketing, sales, or service operations. Do not use this to retrieve a single contact by ID; use HubSpot_get_contact instead.

        Args:
            after: Pagination cursor to fetch the next set of results.
            associations: Specify which associations to include in the response.
            limit: Maximum number of results to return in the response.
            properties: List of contact or object properties to include in the response.
            updatedAt: Return results updated after this timestamp.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_deal_line_items(
        self,
        dealId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all line items associated with a specific deal in the deal management system. Use this when you need to view the products, services, or line items included in a deal to understand deal composition, pricing, or inventory impact. Do not use this to retrieve a single line item by ID; use get_line_item instead. Do not use this to search or filter line items across all deals; use search_line_items instead.

        Args:
            dealId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_deals(
        self,
        after: Optional[str] = None,
        associations: Optional[str] = None,
        limit: Optional[str] = None,
        properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of deals from HubSpots deal management system. Use this to fetch all deals or to retrieve deals with optional filters such as status, owner, or date range. Do not use this to retrieve a single deal by ID; use HubSpot_get_deal instead. Do not use this to search deals by complex criteria; use HubSpot_search_deals instead.

        Args:
            after: The cursor for paginating results.  Use the 'after' value from a previous response to fetch the next page.
            associations: 
            limit: The maximum number of results to return.
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_engagements(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of engagements from the engagement management system. Use this to fetch all engagements or filtered engagements based on query parameters. Do not use this to retrieve a single engagement by ID; use a dedicated get_engagement endpoint instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_line_items(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all line items from HubSpots line item management system. Use this when you need to list or retrieve all available line items, view line item details in bulk, or filter line items by properties. Do not use this to retrieve a specific line item by ID; use HubSpot_get_line_item instead.

        Args:
            limit: The limit for the number of results.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_lists(
        self,
        count: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all contact lists from HubSpot. Use this when you need to see all available contact lists or browse existing lists in the account. Do not use this tool to retrieve a single list by ID; use HubSpot_get_list instead.

        Args:
            count: Number of records to retrieve in the HubSpot HubSpot API.
            offset: Offset for pagination in the HubSpot HubSpot API.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_owners(
        self,
        after: Optional[str] = None,
        archived: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all owners in HubSpot. Use this to retrieve all users with ownership permissions when you need to assign deals, tickets, or other CRM objects to a specific owner, or to populate owner dropdown options. Do not use this to search for a specific owner by name or email; use search_deals or search_contacts instead if you need to filter by criteria.

        Args:
            after: Pagination cursor for retrieving subsequent pages of results.
            archived: Filter results to include or exclude archived records.
            limit: Limit the number of results returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_products(
        self,
        after: Optional[str] = None,
        archived: Optional[str] = None,
        associations: Optional[str] = None,
        limit: Optional[str] = None,
        properties: Optional[str] = None,
        propertiesWithHistory: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of products from the product management system. Use this to retrieve all products or filter products by specific criteria such as name, status, or custom properties. Do not use this to retrieve a single product by ID; use get_product instead.

        Args:
            after: 
            archived: 
            associations: 
            limit: 
            properties: 
            propertiesWithHistory: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_properties(
        self,
        archived: Optional[str] = None,
        resourceName: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of properties available in the property management system. Use this when you need to see all available property definitions for a resource type, such as when building custom integrations or validating property names. To retrieve a specific property, use HubSpot_get_property instead.

        Args:
            archived: Show archived properties
            resourceName: Resource ( deals, companies, contacts )
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_tickets(
        self,
        after: Optional[str] = None,
        archived: Optional[str] = None,
        associations: Optional[str] = None,
        limit: Optional[str] = None,
        properties: Optional[str] = None,
        propertiesWithHistory: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of tickets from the ticket management system. Use this to fetch all tickets or a filtered collection of tickets when you need to browse, filter, or iterate through multiple tickets. To retrieve a single ticket with full details by ID, use HubSpot_get_ticket instead.

        Args:
            after: Pagination cursor to retrieve the next page of results.
            archived: Filter results to include archived items when applicable.
            associations: Specify associations to include in the response.
            limit: Maximum number of items to return in the response.
            properties: Comma-separated list of property names to include in the response.
            propertiesWithHistory: Include properties with historical values if supported.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_list_users(
        self,
        after: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all users from the user management system. Use this when you need to view all users in your HubSpot account or iterate through the user collection. Do not use this to retrieve a single user by ID (use HubSpot_get_user instead) or to create/update users (use HubSpot_create_user or HubSpot_update_user instead).

        Args:
            after: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_refresh_token(
        self,
        client_id: str,
        client_secret: str,
        refresh_token: str,
    ) -> Dict[str, Any]:
        """Refreshes an existing access token for continued authentication in the system. Use this tool when your current access token is about to expire or has expired to maintain an active connection to HubSpot without requiring manual re-authentication. Do not use this tool if you need to obtain an initial access token (use OAuth authorization flow instead) or to revoke token access (use token revocation endpoint instead). Note: The old token may remain valid for a brief period after refresh. A new refresh token is issued with each refresh, and the previous refresh token becomes invalid.

        Args:
            client_id: Client ID for HubSpot API authentication. (required)
            client_secret: Client secret for HubSpot API authentication. (required)
            refresh_token: Refresh token for HubSpot API authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_search_company(
        self,
        filterGroups: Optional[List[Any]] = None,
        properties: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Searches for one or more companies in HubSpot using filters such as company name, domain, or custom properties. Use this when you need to find companies matching specific search criteria. Do not use this to retrieve a company by its unique ID; use HubSpot_get_company instead.

        Args:
            filterGroups: 
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_search_contact(
        self,
        after: Optional[str] = None,
        filterGroups: Optional[List[Any]] = None,
        limit: Optional[str] = None,
        properties: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Searches for one or more contacts in HubSpot using filters such as name, email, phone number, or other contact attributes. Use this when you need to locate existing contacts based on specific criteria. Do not use this to retrieve a contact by its ID; use HubSpot_get_contact instead.

        Args:
            after: 
            filterGroups: 
            limit: 
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_search_deals(
        self,
        archived: Optional[str] = None,
        filterGroups: Optional[List[Any]] = None,
        limit: Optional[int] = None,
        properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for deals in HubSpot using filters and criteria. Use this when you need to find deals matching specific conditions such as deal stage, deal amount, owner, company name, or custom properties. Supports complex filtering and sorting. Do not use this to retrieve all deals without filters; use list_deals instead if you need all deals or a simple paginated list.

        Args:
            archived: Filter for archived items.
            filterGroups: 
            limit: Limit the number of results returned.
            properties: Specify which properties to include in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_search_products(
        self,
        filterGroups: Optional[List[Any]] = None,
        limit: Optional[int] = None,
        properties: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Searches for products in the product management system by applying filters and search criteria. Use this to find specific products, check product availability, or retrieve products matching certain conditions. Do not use this to retrieve a single product by ID; use HubSpot_get_product instead.

        Args:
            filterGroups: 
            limit: 
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_subscribe_to_events(
        self,
        active: bool,
        appId: str,
        eventType: str,
        hapikey: str,
        propertyName: str,
    ) -> Dict[str, Any]:
        """Subscribes to events in the event management system. Use this when you want to set up real-time notifications or webhooks for specific HubSpot events (such as contact updates, deal changes, or form submissions) to be delivered to your application.

        Args:
            active: Indicates if the property is active. (required)
            appId: Identifier for the HubSpot application. (required)
            eventType: Type of event associated with the property. (required)
            hapikey: Your HubSpot API key for authentication. (required)
            propertyName: Name of the property. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_update_company(
        self,
        companyId: str,
        properties: Optional[_HubSpotUpdateCompanyProperties] = None,
    ) -> Dict[str, Any]:
        """Updates an existing company record in HubSpot. Use this when you need to modify company details such as name, website, industry, or other company properties by providing the company ID. Do not use this to create a new company; use HubSpot_create_company instead.

        Args:
            companyId:  (required)
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_update_contact(
        self,
        contactId: str,
        properties: Optional[_HubSpotUpdateContactProperties] = None,
    ) -> Dict[str, Any]:
        """Updates an existing contacts properties in HubSpot CRM by the contacts unique ID. Use this when you need to modify fields such as name, email, phone, or custom properties on an existing contact record. Do not use this to create a new contact; use HubSpot_create_contact instead. Do not use this to delete a contact; use HubSpot_delete_contact instead.

        Args:
            contactId: The ID of the HubSpot contact to update. (required)
            properties: Properties of the HubSpot contact to update.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_update_deal(
        self,
        dealId: str,
        properties: _HubSpotUpdateDealProperties,
    ) -> Dict[str, Any]:
        """Updates an existing deal in the deal management system. Use this tool when you need to modify properties of a specific deal by its ID, such as changing the deal amount, stage, or other deal attributes. Do not use this tool to create a new deal (use HubSpot_create_deal instead) or to retrieve deal information (use HubSpot_get_deal instead). Note: This action may trigger associated workflows or update related contact and company records if configured in your HubSpot account.

        Args:
            dealId:  (required)
            properties:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_update_line_item(
        self,
        line_item_id: str,
        properties: Optional[_HubSpotUpdateLineItemProperties] = None,
    ) -> Dict[str, Any]:
        """Updates an existing line item in the line item management system. Use this to modify the properties of a line item, such as quantity, price, or description. Provide the line item ID and the fields you want to update. Do not use this tool to create a new line item; use create_line_item instead. Do not use this tool to delete a line item; use delete_line_item instead. This action may trigger associated deal or quote updates if the line item is linked to those objects.

        Args:
            line_item_id: The ID of the line item. (required)
            properties: Properties of the line item being updated or created.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_update_product(
        self,
        productId: Optional[str] = None,
        properties: Optional[_HubSpotUpdateProductProperties] = None,
    ) -> Dict[str, Any]:
        """Updates an existing product in the product management system. Use this to modify product properties such as name, description, price, or other attributes. Requires the product ID. Do not use this to create a new product; use HubSpot_create_product instead. This action may trigger associated workflows or update related records in HubSpot.

        Args:
            productId: 
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_update_ticket(
        self,
        properties: _HubSpotUpdateTicketProperties,
        ticketId: str,
        idProperty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing ticket in the ticket management system. Use this when you need to modify ticket properties such as status, priority, assignee, subject, or description. This tool accepts the ticket ID and a JSON object of fields to update. Do not use this to create a new ticket—use a create_ticket tool instead. Do not use this to delete a ticket—use HubSpot_delete_ticket instead. Updating a ticket may trigger notifications to assigned team members or contacts depending on the fields changed.

        Args:
            properties: HubSpot ticket properties to be set or updated. (required)
            ticketId: Unique identifier for the HubSpot ticket. (required)
            idProperty: Property name used to identify the resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_update_user(
        self,
        email: str,
        firstName: str,
        id: str,
        idProperty: str,
        lastName: str,
        primaryTeamId: str,
        roleId: str,
        sendWelcomeEmail: bool,
        userId: str,
    ) -> Dict[str, Any]:
        """Updates an existing user in the user management system. Use this when you need to modify a users properties such as email, name, role, or other attributes by their user ID. Do not use this to create a new user (use HubSpot_create_user instead) or to list all users (use HubSpot_list_users instead). Note: This action modifies the user record immediately and may trigger audit logs or notifications depending on HubSpot settings.

        Args:
            email: The user's email address. (required)
            firstName: The first name of the user. (required)
            id: Unique identifier for the resource. (required)
            idProperty: ID property for the user. (required)
            lastName: The last name of the user. (required)
            primaryTeamId: The ID of the user's primary team. (required)
            roleId: The ID of the user's role. (required)
            sendWelcomeEmail: Indicates whether to send a welcome email. (required)
            userId: The ID of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_upload_file(
        self,
        file: str,
        fileName: str,
        folderId: str,
        options: str,
        charsetHunch: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a file to HubSpots file management system. Use this when you need to store a document, image, or other file asset in HubSpot for use in campaigns, templates, or records. The uploaded file will be assigned a unique file ID and can be referenced in other HubSpot objects. Do not use this to upload user profile pictures or avatar images; use the contacts or companies API endpoints directly for profile assets. Do not use this to create a folder; use HubSpot_create_folder instead.

        Args:
            file: The file to be uploaded or processed. (required)
            fileName: The name of the file. (required)
            folderId: Identifier of the target folder. (required)
            options: Additional options for the request. (required)
            charsetHunch: Character set hint for the request content.
        Returns:
            API response as a dictionary.
        """
        ...

    def hub_spot_upsert_webhook_settings(
        self,
        appId: str,
        hapikey: str,
        targetUrl: str,
        throttling: _HubSpotUpsertWebhookSettingsThrottling,
    ) -> Dict[str, Any]:
        """Creates or updates webhook settings for a specific HubSpot app. If no webhook exists for the app, a new one is created; if one already exists, its configuration is updated with the provided settings. Webhooks allow HubSpot to send HTTP POST notifications to your application when specific events occur. Use this when you need to set up or modify event-driven integrations between HubSpot and your application. Do not use this to retrieve webhook settings; use HubSpot_get_webhook instead. Do not use this to delete a webhook; use HubSpot_delete_webhook instead. Once configured, the webhook will begin delivering HTTP POST notifications for all subscribed events to the target URL; ensure the target URL is accessible and can handle the payload, otherwise event delivery will fail. Existing webhook subscriptions for this app may be updated or replaced.

        Args:
            appId: The ID of the HubSpot application. (required)
            hapikey: Your HubSpot HAPI Key for authentication. (required)
            targetUrl: The URL to which the request is directed. (required)
            throttling: Settings related to request throttling. (required)
        Returns:
            API response as a dictionary.
        """
        ...

