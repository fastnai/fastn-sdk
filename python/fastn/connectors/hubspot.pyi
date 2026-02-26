"""Fastn HubSpot connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class HubspotConnector:
    """HubSpot connector ().

    Provides 68 tools.
    """

    def add_contact_to_list(
        self,
        emails: List[Any],
        vids: List[Any],
    ) -> Dict[str, Any]:
        """Adds a contact to a list in the list management system.

        Args:
            emails: An array of email addresses. (required)
            vids: An array of HubSpot contact IDs (vids). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def add_line_item_to_deal(
        self,
    ) -> Dict[str, Any]:
        """Adds a line item to a deal in the deal management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def add_note(
        self,
        associations: List[Any],
        properties: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Adds a note to a specific contact in the contact management system.

        Args:
            associations:  (required)
            properties: Properties of the HubSpot object. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def batch_create_deals(
        self,
        inputs: List[Any],
    ) -> Dict[str, Any]:
        """Creates multiple deals in the deal management system in a batch.

        Args:
            inputs:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_association(
        self,
        inputs: List[Any],
    ) -> Dict[str, Any]:
        """Creates an association between different entities in the association management system.

        Args:
            inputs:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_company(
        self,
        properties: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new company in the company management system.

        Args:
            properties: Properties of the company being created or updated in HubSpot. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_company_associations(
        self,
    ) -> Dict[str, Any]:
        """Creates associations between companies in the association management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_contact(
        self,
        properties: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new contact in the contact management system.

        Args:
            properties: Properties of the contact.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_custom_property(
        self,
        description: str,
        fieldType: str,
        groupName: str,
        label: str,
        name: str,
        type: str,
        hasUniqueValue: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a custom property in the custom property management system.

        Args:
            description: A description of the custom object. (required)
            fieldType: The type of field for the custom object. (required)
            groupName: The name of the group the custom object belongs to in HubSpot. (required)
            label: The label for the custom object. (required)
            name: The name of the custom object. (required)
            type: The type of the custom object. (required)
            hasUniqueValue: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_deal(
        self,
        properties: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new deal in the deal management system.

        Args:
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_engagement(
        self,
        associations: Dict[str, Any],
        attachments: List[Any],
        engagement: Dict[str, Any],
        metadata: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new engagement in the engagement management system.

        Args:
            associations: Associations related to the request. (required)
            attachments:  (required)
            engagement: Details about the engagement. (required)
            metadata: Metadata associated with the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_folder(
        self,
        name: str,
        parentPath: str,
        parentFolderId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new folder in the folder management system.

        Args:
            name: The name of the folder or entity. (required)
            parentPath: The path to the parent directory. (required)
            parentFolderId: The identifier of the parent folder.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_line_item(
        self,
        properties: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new line item in the line item management system.

        Args:
            properties: Properties of the deal being created or updated.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_list(
        self,
        dynamic: bool,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new list in the list management system.

        Args:
            dynamic: Dynamic flag indicating a dynamic property in the HubSpot API request. (required)
            name: Name field for the HubSpot API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_product(
        self,
        properties: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new product in the product management system.

        Args:
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_ticket(
        self,
        properties: Dict[str, Any],
        associations: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new ticket in the ticket management system.

        Args:
            properties: Additional properties for the HubSpot object. (required)
            associations: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_user(
        self,
        email: str,
        firstName: str,
        lastName: str,
        primaryTeamId: str,
        roleId: str,
        secondaryTeamIds: List[Any],
        sendWelcomeEmail: bool,
    ) -> Dict[str, Any]:
        """Creates a new user in the user management system.

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

    def create_webhook(
        self,
        hapikey: str,
    ) -> Dict[str, Any]:
        """Creates a new webhook in the webhook management system.

        Args:
            hapikey: Your HubSpot HAPI Key for authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_contact(
        self,
        contactId: str,
    ) -> Dict[str, Any]:
        """Deletes a contact from the contact management system.

        Args:
            contactId: The ID of the HubSpot contact. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_deal(
        self,
        dealId: str,
    ) -> Dict[str, Any]:
        """Deletes a deal from the deal management system.

        Args:
            dealId: The ID of the deal to be accessed in the HubSpot API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_line_item_from_deal(
        self,
    ) -> Dict[str, Any]:
        """Deletes a line item from a deal in the deal management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_product(
        self,
        productId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a product from the product management system.

        Args:
            productId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_ticket(
        self,
        ticketId: str,
    ) -> Dict[str, Any]:
        """Deletes a ticket from the ticket management system.

        Args:
            ticketId: The HubSpot ticket identifier included in the API request URL. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Deletes a user from the user management system.

        Args:
            userId: The ID of the user for the HubSpot API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_access_token(
        self,
    ) -> Dict[str, Any]:
        """Obtains an access token for authentication in the system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_associations(
        self,
        inputs: List[Any],
    ) -> Dict[str, Any]:
        """Fetches associations between different entities in the association management system.

        Args:
            inputs:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_companies(
        self,
        after: Optional[str] = None,
        limit: Optional[str] = None,
        properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of companies from the company management system.

        Args:
            after: Cursor for pagination.  Use the 'after' value from the previous response to fetch subsequent pages.
            limit: The maximum number of results to return.
            properties: Specifies which properties to include in the response.  Use this to control the data returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_company(
        self,
        companyId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific company from the company management system.

        Args:
            companyId: The ID of the HubSpot company. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contact(
        self,
        associations: Optional[str] = None,
        properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a specific contact from the contact management system.

        Args:
            associations: 
            properties: properties to return
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contact_association(
        self,
        archived: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the association of a contact in the contact management system.

        Args:
            archived: Specifies whether to include archived records in the response.  (e.g., 'true' or 'false').
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
        after: Optional[str] = None,
        associations: Optional[str] = None,
        limit: Optional[str] = None,
        properties: Optional[str] = None,
        updatedAt: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of contacts from the contact management system.

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

    def get_deal(
        self,
        associations: Optional[str] = None,
        properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific deal from the deal management system.

        Args:
            associations: 
            properties: Fields to return in the response
        Returns:
            API response as a dictionary.
        """
        ...

    def get_deal_association(
        self,
        archived: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the association of a deal in the deal management system.

        Args:
            archived: Whether to include archived deals.  Possible values depend on the specific HubSpot endpoint.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_deal_line_items(
        self,
        dealId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves line items associated with a specific deal in the deal management system.

        Args:
            dealId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_deals(
        self,
        after: Optional[str] = None,
        associations: Optional[str] = None,
        limit: Optional[str] = None,
        properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of deals from the deal management system.

        Args:
            after: The cursor for paginating results.  Use the 'after' value from a previous response to fetch the next page.
            associations: 
            limit: The maximum number of results to return.
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_engagement(
        self,
        noteId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific engagement from the engagement management system.

        Args:
            noteId: ID of the HubSpot note. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_engagements(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of engagements from the engagement management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Fetches a file from the file management system.

        Args:
            fileId: The ID of the file in HubSpot. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_line_item(
        self,
        properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific line item from the line item management system.

        Args:
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_line_items(
        self,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of line items from the line item management system.

        Args:
            limit: The limit for the number of results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_list(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific list from the list management system.

        Args:
            id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_lists(
        self,
        count: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of lists from the list management system.

        Args:
            count: Number of records to retrieve in the HubSpot HubSpot API.
            offset: Offset for pagination in the HubSpot HubSpot API.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_owners(
        self,
        after: Optional[str] = None,
        archived: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of owners in the ownership management system.

        Args:
            after: Pagination cursor for retrieving subsequent pages of results.
            archived: Filter results to include or exclude archived records.
            limit: Limit the number of results returned.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_product(
        self,
        archived: Optional[str] = None,
        associations: Optional[str] = None,
        idProperty: Optional[str] = None,
        properties: Optional[str] = None,
        propertiesWithHistory: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific product from the product management system.

        Args:
            archived: 
            associations: 
            idProperty: 
            properties: 
            propertiesWithHistory: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_products(
        self,
        after: Optional[str] = None,
        archived: Optional[str] = None,
        associations: Optional[str] = None,
        limit: Optional[str] = None,
        properties: Optional[str] = None,
        propertiesWithHistory: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of products from the product management system.

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

    def get_properties(
        self,
        archived: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of properties from the property management system.

        Args:
            archived: Show archived properties
        Returns:
            API response as a dictionary.
        """
        ...

    def get_signed_url(
        self,
        fileId: str,
    ) -> Dict[str, Any]:
        """Generates a signed URL for secure file access from the file management system.

        Args:
            fileId: ID of the file for the HubSpot HubSpot endpoint. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_ticket(
        self,
        archived: Optional[str] = None,
        associations: Optional[str] = None,
        idProperty: Optional[str] = None,
        properties: Optional[str] = None,
        propertiesWithHistory: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific ticket from the ticket management system.

        Args:
            archived: Flag to include archived items.
            associations: Association-related parameter for the request.
            idProperty: Identifier for the primary property used in the request.
            properties: List of properties to include or filter in the request.
            propertiesWithHistory: Include properties history in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_tickets(
        self,
        after: Optional[str] = None,
        archived: Optional[str] = None,
        associations: Optional[str] = None,
        limit: Optional[str] = None,
        properties: Optional[str] = None,
        propertiesWithHistory: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of tickets from the ticket management system.

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

    def get_user(
        self,
        userId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific user from the user management system.

        Args:
            userId: The ID of the user. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_details(
        self,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a user from the user management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_roles(
        self,
    ) -> Dict[str, Any]:
        """Retrieves roles assigned to a user from the user management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_users(
        self,
        after: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of users from the user management system.

        Args:
            after: 
        Returns:
            API response as a dictionary.
        """
        ...

    def read_file(
        self,
        baseUrl: str,
    ) -> Dict[str, Any]:
        """Reads the content of a file from the file management system.

        Args:
            baseUrl: The base URL for the HubSpot API request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def refresh_token(
        self,
        client_id: str,
        client_secret: str,
        refresh_token: str,
    ) -> Dict[str, Any]:
        """Refreshes an existing access token for continued authentication in the system.

        Args:
            client_id: Client ID for HubSpot API authentication. (required)
            client_secret: Client secret for HubSpot API authentication. (required)
            refresh_token: Refresh token for HubSpot API authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def search_company(
        self,
        filterGroups: Optional[List[Any]] = None,
        properties: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Searches for a company in the company management system.

        Args:
            filterGroups: 
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def search_contact(
        self,
        after: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for a contact in the contact management system.

        Args:
            after: 
            limit: 
        Returns:
            API response as a dictionary.
        """
        ...

    def search_deals(
        self,
        archived: Optional[str] = None,
        limit: Optional[str] = None,
        properties: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for deals in the deal management system.

        Args:
            archived: Filter for archived items.
            limit: Limit the number of results returned.
            properties: Specify which properties to include in the response.
        Returns:
            API response as a dictionary.
        """
        ...

    def search_products(
        self,
        filterGroups: Optional[List[Any]] = None,
        limit: Optional[int] = None,
        properties: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Searches for products in the product management system.

        Args:
            filterGroups: 
            limit: 
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def subscribe_to_events(
        self,
        hapikey: str,
    ) -> Dict[str, Any]:
        """Subscribes to events in the event management system.

        Args:
            hapikey: Your HubSpot API key for authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_company(
        self,
        properties: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing company in the company management system.

        Args:
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_contact(
        self,
        properties: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing contact in the contact management system.

        Args:
            properties: Properties of the HubSpot contact to update.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_deal(
        self,
        properties: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Updates an existing deal in the deal management system.

        Args:
            properties:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_line_item(
        self,
        properties: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing line item in the line item management system.

        Args:
            properties: Properties of the line item being updated or created.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_product(
        self,
        properties: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Updates an existing product in the product management system.

        Args:
            properties: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_ticket(
        self,
        idProperty: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing ticket in the ticket management system.

        Args:
            idProperty: Property name used to identify the resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_user(
        self,
    ) -> Dict[str, Any]:
        """Updates an existing user in the user management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_files(
        self,
        file: str,
        fileName: str,
        folderId: str,
        options: str,
        charsetHunch: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads files to the file management system.

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

