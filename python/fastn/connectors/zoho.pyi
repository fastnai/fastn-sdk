"""Fastn Zoho connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ZohoConnector:
    """Zoho connector ().

    Provides 28 tools.
    """

    def add_note(
        self,
        data: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Adds a note to a specified record in the application.

        Args:
            data: 
        Returns:
            API response as a dictionary.
        """
        ...

    def copy_file(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Copies a specified file to a new location within the application.

        Args:
            data: The data to be sent to the Zoho WorkDrive API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_contact(
        self,
        data: List[Any],
    ) -> Dict[str, Any]:
        """Creates a new contact entry in the specified address book of the application.

        Args:
            data:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_deals(
        self,
        data: List[Any],
        trigger: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new deal entry in the CRM of the application.

        Args:
            data:  (required)
            trigger: Array of triggers.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_field(
        self,
        module: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new field for data entry in the application.

        Args:
            module: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_folder(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new folder in the specified directory of the application.

        Args:
            data: Contains the attributes and type of the resource to be created. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_leads(
        self,
        data: List[Any],
        lar_id: Optional[str] = None,
        trigger: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new lead entry in the CRM of the application.

        Args:
            data:  (required)
            lar_id: LAR ID.
            trigger: Array of triggers.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_contact(
        self,
        record_id: str,
    ) -> Dict[str, Any]:
        """Deletes a specified contact from the address book in the application.

        Args:
            record_id: The ID of the record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_deal(
        self,
        record_id: str,
    ) -> Dict[str, Any]:
        """Deletes a specified deal from the CRM of the application.

        Args:
            record_id: The ID of the record to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_file(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Permanently deletes a specified file from the application.

        Args:
            data: Contains attributes of the resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_lead(
        self,
        record_id: str,
    ) -> Dict[str, Any]:
        """Deletes a specified lead from the CRM of the application.

        Args:
            record_id: The ID of the record to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_accounts(
        self,
        fields: Optional[str] = None,
        page: Optional[str] = None,
        page_token: Optional[str] = None,
        per_page: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves account information from the application's database.

        Args:
            fields: 
            page: 
            page_token: 
            per_page: 
            sort_by: 
            sort_order: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_contacts(
        self,
        criteria: Optional[str] = None,
        exclude_nulls: Optional[str] = None,
        fields: Optional[str] = None,
        include_links: Optional[str] = None,
        on_demand_properties: Optional[str] = None,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
        skip_empty_fields: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches the list of contacts from the specified address book in the application.

        Args:
            criteria: Criteria for filtering records.
            exclude_nulls: Whether to exclude null values in the response.
            fields: Specific fields to retrieve.
            include_links: Whether to include links in the response.
            on_demand_properties: Properties to retrieve on demand.
            page: The page number to retrieve.
            per_page: Number of records per page in the response.
            skip_empty_fields: Whether to skip fields with empty values in the response.
            sort_by: Field to sort the results by.
            sort_order: Sort order (ascending or descending).
        Returns:
            API response as a dictionary.
        """
        ...

    def get_deals(
        self,
        criteria: Optional[str] = None,
        exclude_associated_modules: Optional[str] = None,
        exclude_nulls: Optional[str] = None,
        fields: Optional[str] = None,
        from: Optional[str] = None,
        group: Optional[str] = None,
        include: Optional[str] = None,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
        skip_assigned_to_lookup: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        to: Optional[str] = None,
        trigger: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves deals from the CRM of the application.

        Args:
            criteria: Criteria for filtering records.
            exclude_associated_modules: Specifies associated modules to exclude from the response.
            exclude_nulls: Whether to exclude records with null values.
            fields: Comma-separated list of fields to retrieve.
            from: Start date or ID for pagination.
            group: Field to group results by.
            include: Specifies the fields to include in the response.
            page: Page number for pagination.
            per_page: Number of records per page in the response.
            skip_assigned_to_lookup: Whether to skip the 'assigned to' lookup field.
            sort_by: Field to sort the results by.
            sort_order: Sorting order (ascending or descending).
            to: End date or ID for pagination.
            trigger: Trigger for the API call.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_fields(
        self,
        module: str,
    ) -> Dict[str, Any]:
        """Fetches a list of available fields from the application for use in data entry.

        Args:
            module: Module ( Accounts, Leads, Contacts ) (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_file(
        self,
        resourceId: str,
    ) -> Dict[str, Any]:
        """Retrieves a specific file from the application.

        Args:
            resourceId: The unique identifier of the resource in Zoho WorkDrive. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_leads(
        self,
        page: Optional[str] = None,
        page_token: Optional[str] = None,
        per_page: Optional[str] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves leads associated with the specified accounts in the application.

        Args:
            page: 
            page_token: 
            per_page: 
            sort_by: 
            sort_order: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves user information from the application.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_user_teams(
        self,
        zuid: str,
    ) -> Dict[str, Any]:
        """Fetches the list of teams associated with the user in the application.

        Args:
            zuid: The ZUID (Zoho Unique Identifier) for the resource. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def move_to_trash(
        self,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Moves a specified file to the trash in the application.

        Args:
            data: The data object containing attributes and type information.
        Returns:
            API response as a dictionary.
        """
        ...

    def rename_file(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Renames a specified file within the application.

        Args:
            data: The main data object for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def restore_file(
        self,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Restores a previously deleted file from the trash in the application.

        Args:
            data: The data object containing attributes and type information. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def search(
        self,
        criteria: Optional[str] = None,
        page: Optional[str] = None,
        per_page: Optional[str] = None,
        word: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Performs a search operation within the application based on specified parameters.

        Args:
            criteria: 
            page: 
            per_page: 
            word: 
        Returns:
            API response as a dictionary.
        """
        ...

    def search_by_query(
        self,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Performs a search in the application using a specific query string.

        Args:
            query: 
        Returns:
            API response as a dictionary.
        """
        ...

    def update_contact(
        self,
        data: List[Any],
    ) -> Dict[str, Any]:
        """Updates details of an existing contact in the application.

        Args:
            data:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_deals(
        self,
        data: List[Any],
    ) -> Dict[str, Any]:
        """Updates an existing deal in the CRM of the application.

        Args:
            data:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_leads(
        self,
        data: List[Any],
    ) -> Dict[str, Any]:
        """Updates an existing lead in the CRM of the application.

        Args:
            data:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def upload_file(
        self,
        content: str,
        filename: str,
        parent_id: str,
        override_name_exist: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Uploads a file to the specified location in the application.

        Args:
            content: The content of the file to be uploaded (base64 encoded). (required)
            filename: The name of the file to be uploaded. (required)
            parent_id: The ID of the parent folder where the file should be uploaded. (required)
            override_name_exist: Indicates whether to override an existing file with the same name.  (Implementation details may vary).
        Returns:
            API response as a dictionary.
        """
        ...

