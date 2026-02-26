"""Fastn Servicenow connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ServicenowConnector:
    """Servicenow connector ().

    Provides 36 tools.
    """

    def _get_hardwares(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_limit: Optional[str] = None,
        sysparm_no_count: Optional[str] = None,
        sysparm_offset: Optional[str] = None,
        sysparm_query: Optional[str] = None,
        sysparm_query_category: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_suppress_pagination_header: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all hardware components in the system.

        Args:
            sysparm_display_value: Retrieve display values instead of internal keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_limit: Maximum number of records to retrieve.
            sysparm_no_count: Omit total count in the response.
            sysparm_offset: Starting record offset for pagination.
            sysparm_query: Advanced query string for filtering records.
            sysparm_query_category: Category for the query.
            sysparm_query_no_domain: Ignore domain when querying.
            sysparm_suppress_pagination_header: Suppress pagination header in the response.
            sysparm_view: Name of the view to use for filtering.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_asset(
        self,
        acquisition_method: Optional[str] = None,
        asset_function: Optional[str] = None,
        asset_tag: Optional[str] = None,
        assigned: Optional[str] = None,
        assigned_to: Optional[Dict[str, Any]] = None,
        beneficiary: Optional[str] = None,
        checked_in: Optional[str] = None,
        checked_out: Optional[str] = None,
        ci: Optional[Dict[str, Any]] = None,
        comments: Optional[str] = None,
        company: Optional[Dict[str, Any]] = None,
        cost: Optional[str] = None,
        cost_center: Optional[Dict[str, Any]] = None,
        delivery_date: Optional[str] = None,
        department: Optional[Dict[str, Any]] = None,
        depreciated_amount: Optional[str] = None,
        depreciation: Optional[Dict[str, Any]] = None,
        depreciation_date: Optional[str] = None,
        display_name: Optional[str] = None,
        disposal_reason: Optional[str] = None,
        due: Optional[str] = None,
        due_in: Optional[str] = None,
        eligible_for_refresh: Optional[str] = None,
        expenditure_type: Optional[str] = None,
        gl_account: Optional[str] = None,
        install_date: Optional[str] = None,
        install_status: Optional[str] = None,
        invoice_number: Optional[str] = None,
        justification: Optional[str] = None,
        lease_id: Optional[str] = None,
        life_cycle_stage: Optional[str] = None,
        life_cycle_stage_status: Optional[str] = None,
        location: Optional[Dict[str, Any]] = None,
        managed_by: Optional[str] = None,
        model: Optional[Dict[str, Any]] = None,
        model_category: Optional[Dict[str, Any]] = None,
        old_status: Optional[str] = None,
        old_substatus: Optional[str] = None,
        order_date: Optional[str] = None,
        owned_by: Optional[str] = None,
        parent: Optional[str] = None,
        po_number: Optional[str] = None,
        pre_allocated: Optional[str] = None,
        purchase_date: Optional[str] = None,
        quantity: Optional[str] = None,
        request_line: Optional[str] = None,
        resale_price: Optional[str] = None,
        reserved_for: Optional[str] = None,
        residual: Optional[str] = None,
        residual_date: Optional[str] = None,
        resold_value: Optional[str] = None,
        retired: Optional[str] = None,
        retirement_date: Optional[str] = None,
        salvage_value: Optional[str] = None,
        serial_number: Optional[str] = None,
        skip_sync: Optional[str] = None,
        stockroom: Optional[str] = None,
        substatus: Optional[str] = None,
        support_group: Optional[str] = None,
        supported_by: Optional[str] = None,
        sys_class_name: Optional[str] = None,
        sys_created_by: Optional[str] = None,
        sys_created_on: Optional[str] = None,
        sys_domain: Optional[Dict[str, Any]] = None,
        sys_domain_path: Optional[str] = None,
        sys_id: Optional[str] = None,
        sys_mod_count: Optional[str] = None,
        sys_tags: Optional[str] = None,
        sys_updated_by: Optional[str] = None,
        sys_updated_on: Optional[str] = None,
        vendor: Optional[Dict[str, Any]] = None,
        warranty_expiration: Optional[str] = None,
        work_notes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new asset in the system.

        Args:
            acquisition_method: Method of asset acquisition.
            asset_function: Function of the asset.
            asset_tag: Unique identifier for the asset.
            assigned: Assignment status.
            assigned_to: Details of the assigned user.
            beneficiary: Beneficiary of the asset.
            checked_in: Flag indicating check-in status.
            checked_out: Flag indicating checkout status.
            ci: Details of the CI.
            comments: Comments related to the asset.
            company: Details of the company.
            cost: Cost of the asset.
            cost_center: Details of the cost center.
            delivery_date: Date of asset delivery.
            department: Details of the department.
            depreciated_amount: Amount of depreciation.
            depreciation: Details of depreciation.
            depreciation_date: Date of depreciation.
            display_name: Display name of the asset.
            disposal_reason: Reason for asset disposal.
            due: Due date for the asset.
            due_in: Date when the item is due.
            eligible_for_refresh: Flag indicating eligibility for refresh.
            expenditure_type: Type of expenditure.
            gl_account: General Ledger account.
            install_date: Date of asset installation.
            install_status: Status of asset installation.
            invoice_number: Invoice number associated with the asset.
            justification: Justification for asset actions.
            lease_id: Lease identifier.
            life_cycle_stage: Current life cycle stage.
            life_cycle_stage_status: Status within the life cycle stage.
            location: Details of the asset's location.
            managed_by: Entity managing the asset.
            model: Details of the asset model.
            model_category: Details of the model category.
            old_status: Previous status of the asset.
            old_substatus: Previous substatus of the asset.
            order_date: Date of order placement.
            owned_by: Owner of the asset.
            parent: Parent record ID or sys_id.
            po_number: Purchase order number.
            pre_allocated: Flag indicating pre-allocation.
            purchase_date: Date of asset purchase.
            quantity: Quantity of the asset.
            request_line: Details of the request line item.
            resale_price: Price at which the asset can be resold.
            reserved_for: Entity for which the asset is reserved.
            residual: Remaining value after depreciation.
            residual_date: Date related to residual value.
            resold_value: Value at which the asset was resold.
            retired: Flag indicating retirement status.
            retirement_date: Date of asset retirement.
            salvage_value: Value of the asset at the end of its useful life.
            serial_number: Serial number of the asset.
            skip_sync: Flag to skip synchronization.
            stockroom: Location of the asset in stockroom.
            substatus: Substatus of the asset.
            support_group: Support group responsible for the asset.
            supported_by: Entity providing support.
            sys_class_name: Name of the system class.
            sys_created_by: User who created the record.
            sys_created_on: Timestamp of record creation.
            sys_domain: Details of the system domain.
            sys_domain_path: Path of the system domain.
            sys_id: Unique identifier for the record.
            sys_mod_count: Number of modifications to the record.
            sys_tags: Tags associated with the record.
            sys_updated_by: User who last updated the record.
            sys_updated_on: Timestamp of the last update.
            vendor: Details of the vendor.
            warranty_expiration: Warranty expiration date.
            work_notes: Notes related to the asset.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_event(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new event in the system.

        Args:
            sysparm_display_value: Return display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to return.
            sysparm_input_display_value: Use display values for input fields.
            sysparm_suppress_auto_sys_field: Suppress automatically generated system fields.
            sysparm_view: Specifies the view to use for the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_hardware(
        self,
        acquisition_method: Optional[str] = None,
        asset_function: Optional[str] = None,
        asset_tag: Optional[str] = None,
        assigned: Optional[str] = None,
        assigned_to: Optional[str] = None,
        beneficiary: Optional[str] = None,
        checked_in: Optional[str] = None,
        checked_out: Optional[str] = None,
        ci: Optional[str] = None,
        comments: Optional[str] = None,
        company: Optional[str] = None,
        cost: Optional[float] = None,
        cost_center: Optional[str] = None,
        delivery_date: Optional[str] = None,
        department: Optional[str] = None,
        depreciated_amount: Optional[float] = None,
        depreciation: Optional[str] = None,
        depreciation_date: Optional[str] = None,
        display_name: Optional[str] = None,
        disposal_reason: Optional[str] = None,
        due: Optional[str] = None,
        due_in: Optional[str] = None,
        eligible_for_refresh: Optional[bool] = None,
        expenditure_type: Optional[str] = None,
        gl_account: Optional[str] = None,
        install_date: Optional[str] = None,
        install_status: Optional[str] = None,
        invoice_number: Optional[str] = None,
        justification: Optional[str] = None,
        lease_id: Optional[str] = None,
        life_cycle_stage: Optional[str] = None,
        life_cycle_stage_status: Optional[str] = None,
        location: Optional[str] = None,
        managed_by: Optional[str] = None,
        model: Optional[str] = None,
        model_category: Optional[str] = None,
        old_status: Optional[str] = None,
        order_date: Optional[str] = None,
        owned_by: Optional[str] = None,
        parent: Optional[str] = None,
        po_number: Optional[str] = None,
        pre_allocated: Optional[bool] = None,
        purchase_date: Optional[str] = None,
        quantity: Optional[int] = None,
        request_line: Optional[str] = None,
        resale_price: Optional[float] = None,
        reserved_for: Optional[str] = None,
        residual: Optional[float] = None,
        residual_date: Optional[str] = None,
        resold_value: Optional[int] = None,
        retired: Optional[bool] = None,
        retirement_date: Optional[str] = None,
        salvage_value: Optional[float] = None,
        serial_number: Optional[str] = None,
        skip_sync: Optional[bool] = None,
        stockroom: Optional[str] = None,
        substatus: Optional[str] = None,
        support_group: Optional[str] = None,
        supported_by: Optional[str] = None,
        sys_class_name: Optional[str] = None,
        sys_created_by: Optional[str] = None,
        sys_created_on: Optional[str] = None,
        sys_domain: Optional[str] = None,
        sys_domain_path: Optional[str] = None,
        sys_id: Optional[str] = None,
        sys_updated_by: Optional[str] = None,
        sys_updated_on: Optional[str] = None,
        vendor: Optional[str] = None,
        warranty_expiration: Optional[str] = None,
        work_notes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new hardware component in the system.

        Args:
            acquisition_method: Acquisition method.
            asset_function: Asset function.
            asset_tag: Asset tag.
            assigned: Assigned to.
            assigned_to: Assigned to user.
            beneficiary: Beneficiary.
            checked_in: Checked in timestamp.
            checked_out: Checked out timestamp.
            ci: CI ID.
            comments: Comments.
            company: Company.
            cost: Cost.
            cost_center: Cost center.
            delivery_date: Delivery date.
            department: Department.
            depreciated_amount: Depreciated amount.
            depreciation: Depreciation method.
            depreciation_date: Depreciation date.
            display_name: Display name.
            disposal_reason: Reason for disposal.
            due: Due date.
            due_in: Due in date.
            eligible_for_refresh: Eligible for refresh.
            expenditure_type: Expenditure type.
            gl_account: General ledger account.
            install_date: Installation date.
            install_status: Installation status.
            invoice_number: Invoice number.
            justification: Justification.
            lease_id: Lease ID.
            life_cycle_stage: Life cycle stage.
            life_cycle_stage_status: Life cycle stage status.
            location: Location.
            managed_by: Managed by.
            model: Model number.
            model_category: Model category.
            old_status: Old status.
            order_date: Order date.
            owned_by: Owned by.
            parent: Parent record ID.
            po_number: Purchase order number.
            pre_allocated: Pre-allocated.
            purchase_date: Purchase date.
            quantity: Quantity.
            request_line: Request line item.
            resale_price: Resale price.
            reserved_for: Reserved for.
            residual: Residual value.
            residual_date: Residual date.
            resold_value: Resold value.
            retired: Retired.
            retirement_date: Retirement date.
            salvage_value: Salvage value.
            serial_number: Serial number.
            skip_sync: Skip synchronization.
            stockroom: Stockroom.
            substatus: Substatus.
            support_group: Support group.
            supported_by: Supported by.
            sys_class_name: System class name.
            sys_created_by: User who created the record.
            sys_created_on: Created timestamp.
            sys_domain: System domain.
            sys_domain_path: System domain path.
            sys_id: System ID.
            sys_updated_by: User who last updated the record.
            sys_updated_on: Last updated timestamp.
            vendor: Vendor.
            warranty_expiration: Warranty expiration date.
            work_notes: Work notes.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_incident(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new incident in the system.

        Args:
            sysparm_display_value: Return display values for fields.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Specify the fields to be returned in the response.
            sysparm_input_display_value: Return input display values for fields.
            sysparm_suppress_auto_sys_field: Suppress automatically generated sys fields in the response.
            sysparm_view: Specify the view to be used for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_model(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new hardware model in the system.

        Args:
            sysparm_display_value: Display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to include in the response.
            sysparm_input_display_value: Use display values for input fields.
            sysparm_suppress_auto_sys_field: Suppress automatically generated system fields.
            sysparm_view: Name of the view to use for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_system_property(
        self,
        choices: Optional[str] = None,
        description: Optional[str] = None,
        ignore_cache: Optional[str] = None,
        is_private: Optional[str] = None,
        name: Optional[str] = None,
        read_roles: Optional[str] = None,
        suffix: Optional[str] = None,
        sys_class_name: Optional[str] = None,
        sys_created_by: Optional[str] = None,
        sys_created_on: Optional[str] = None,
        sys_mod_count: Optional[str] = None,
        sys_name: Optional[str] = None,
        sys_package: Optional[Dict[str, Any]] = None,
        sys_policy: Optional[str] = None,
        sys_scope: Optional[Dict[str, Any]] = None,
        sys_tags: Optional[str] = None,
        sys_update_name: Optional[str] = None,
        sys_updated_by: Optional[str] = None,
        sys_updated_on: Optional[str] = None,
        type: Optional[str] = None,
        value: Optional[str] = None,
        write_roles: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new system property in the system.

        Args:
            choices: Available choices for the field.
            description: Description of the record.
            ignore_cache: Flag to ignore cache.
            is_private: Indicates if the record is private.
            name: Name of the record.
            read_roles: Roles with read access.
            suffix: Suffix for the record name.
            sys_class_name: Name of the system class.
            sys_created_by: User who created the record.
            sys_created_on: Timestamp of record creation.
            sys_mod_count: Number of times the record has been modified.
            sys_name: System name of the record.
            sys_package: Information about the system package.
            sys_policy: System policy associated with the record.
            sys_scope: Information about the system scope.
            sys_tags: Tags associated with the record.
            sys_update_name: Name of the system update.
            sys_updated_by: User who last updated the record.
            sys_updated_on: Timestamp of the last update.
            type: Type of the record.
            value: Value of the field.
            write_roles: Roles with write access.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_asset(
        self,
        sysparm_query_no_domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific asset from the system using its unique identifier.

        Args:
            sysparm_query_no_domain: ServiceNow query parameter (without domain).
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_business_rule(
        self,
        sysparm_query_no_domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific business rule from the system using its unique identifier.

        Args:
            sysparm_query_no_domain: Query parameter for ServiceNow API (excluding domain).
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_event(
        self,
        sysparm_query_no_domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific event from the system using its unique identifier.

        Args:
            sysparm_query_no_domain: Query parameter for the ServiceNow API request (without domain).
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_hardware(
        self,
        sysparm_query_no_domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific hardware component from the system using its unique identifier.

        Args:
            sysparm_query_no_domain: Query parameter for filtering results, excluding domain considerations.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_incident(
        self,
        sysparm_query_no_domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific incident from the system using its unique identifier.

        Args:
            sysparm_query_no_domain: ServiceNow query string without domain specification.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_model(
        self,
        sysparm_query_no_domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes a specific hardware model from the system using its unique identifier.

        Args:
            sysparm_query_no_domain: Query parameter for ServiceNow API (without domain).
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_system_property(
        self,
        sys_id: str,
    ) -> Dict[str, Any]:
        """Deletes a specific system property from the system using its unique identifier.

        Args:
            sys_id: ServiceNow system ID of the target record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        sysId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific webhook from the system using its unique identifier.

        Args:
            sysId: ServiceNow system ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Retrieves an access token for authentication in the system.

        Args:
            client_id: Client ID for the ServiceNow application. (required)
            client_secret: Client secret for the ServiceNow application. (required)
            code: Authorization code received from ServiceNow. (required)
            redirect_uri: Redirect URI registered for the ServiceNow application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_all_events(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_limit: Optional[str] = None,
        sysparm_no_count: Optional[str] = None,
        sysparm_offset: Optional[str] = None,
        sysparm_query: Optional[str] = None,
        sysparm_query_category: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_suppress_pagination_header: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all events recorded in the system.

        Args:
            sysparm_display_value: Retrieve display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_limit: Maximum number of records to return.
            sysparm_no_count: Do not return the total count of records.
            sysparm_offset: Offset for pagination.
            sysparm_query: Advanced query string for filtering records.
            sysparm_query_category: Category for the query.
            sysparm_query_no_domain: Perform query without domain consideration.
            sysparm_suppress_pagination_header: Suppress pagination header in the response.
            sysparm_view: Name of the view to use for filtering.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_asset(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific asset using its unique identifier.

        Args:
            sysparm_display_value: Return display values instead of internal values.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to return.
            sysparm_query_no_domain: Query without domain.
            sysparm_view: View to use for the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_assets(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_limit: Optional[str] = None,
        sysparm_no_count: Optional[str] = None,
        sysparm_offset: Optional[str] = None,
        sysparm_query: Optional[str] = None,
        sysparm_query_category: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_suppress_pagination_header: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all assets currently managed in the system.

        Args:
            sysparm_display_value: Return display values instead of internal keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to return.
            sysparm_limit: Maximum number of records to return.
            sysparm_no_count: Do not return the total count of records.
            sysparm_offset: Offset for pagination.
            sysparm_query: Query string for filtering records.
            sysparm_query_category: Category for the query.
            sysparm_query_no_domain: Query string without domain specification.
            sysparm_suppress_pagination_header: Suppress pagination header in the response.
            sysparm_view: Name of the view to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_business_rules(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_limit: Optional[str] = None,
        sysparm_no_count: Optional[str] = None,
        sysparm_offset: Optional[str] = None,
        sysparm_query: Optional[str] = None,
        sysparm_query_category: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_suppress_pagination_header: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all business rules established in the system.

        Args:
            sysparm_display_value: Retrieve display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_limit: Maximum number of records to return.
            sysparm_no_count: Do not return the total number of records.
            sysparm_offset: Number of records to skip.
            sysparm_query: Query string for filtering records.
            sysparm_query_category: Category for the query.
            sysparm_query_no_domain: Perform query without considering the domain.
            sysparm_suppress_pagination_header: Suppress pagination headers in the response.
            sysparm_view: Name of the view to use for filtering.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_event(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific event using its unique identifier.

        Args:
            sysparm_display_value: Return display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_query_no_domain: Query without domain qualification.
            sysparm_view: View to use for the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_hardware(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific hardware component using its unique identifier.

        Args:
            sysparm_display_value: Display value instead of sys_id.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to return.
            sysparm_query_no_domain: Query without domain.
            sysparm_view: View to use for the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_incident(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific incident using its unique identifier.

        Args:
            sysparm_display_value: Display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_query_no_domain: Perform query without domain consideration.
            sysparm_view: Specify a view for the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_incidents(
        self,
        sysparm_fields: Optional[str] = None,
        sysparm_limit: Optional[str] = None,
        sysparm_offset: Optional[str] = None,
        sysparm_query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all incidents reported in the system.

        Args:
            sysparm_fields: Comma-separated list of fields to retrieve from ServiceNow.
            sysparm_limit: Limit for the number of records to retrieve from ServiceNow.
            sysparm_offset: Offset for pagination in ServiceNow API response.
            sysparm_query: ServiceNow query string for filtering records.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_model(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches details of a specific hardware model using its unique identifier.

        Args:
            sysparm_display_value: Retrieve display values instead of sys_ids.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_query_no_domain: Perform query without domain consideration.
            sysparm_view: Name of the view to use for the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_models_(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_limit: Optional[str] = None,
        sysparm_no_count: Optional[str] = None,
        sysparm_query: Optional[str] = None,
        sysparm_query_category: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_suppress_pagination_header: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all hardware models available in the system.

        Args:
            sysparm_display_value: Retrieve display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_limit: Maximum number of records to retrieve.
            sysparm_no_count: Do not include the total count of records in the response.
            sysparm_query: Advanced query string for filtering records.
            sysparm_query_category: Category for advanced query filtering.
            sysparm_query_no_domain: Perform query without domain qualification.
            sysparm_suppress_pagination_header: Suppress pagination header in the response.
            sysparm_view: Name of the view to use for filtering.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_system_properties(
        self,
        sysparm_limit: Optional[int] = None,
        sysparm_offset: Optional[int] = None,
        sysparm_query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all system properties available in the system.

        Args:
            sysparm_limit: The maximum number of records to return.
            sysparm_offset: The starting record offset for pagination.
            sysparm_query: A ServiceNow query string to filter results.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_system_property(
        self,
        sys_id: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific system property using its unique identifier.

        Args:
            sys_id: The sys_id of the ServiceNow record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def prevent_duplicate_webhooks(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Prevents the creation of duplicate webhooks in the system.

        Args:
            sysparm_display_value: Display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_input_display_value: Use display values for input fields.
            sysparm_suppress_auto_sys_field: Suppress automatically generated system fields.
            sysparm_view: Specify a view to filter the results.
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
        """Refreshes an existing token to maintain session validity in the system.

        Args:
            client_id: Client ID for authentication. (required)
            client_secret: Client secret for authentication. (required)
            refresh_token: Refresh token for authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def register_events_webhook(
        self,
        api_key: str,
        url: str,
    ) -> Dict[str, Any]:
        """Registers a new webhook for event notifications in the system.

        Args:
            api_key: API key for authentication with the Servicenow webhook. (required)
            url: URL of the Servicenow webhook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def register_incident_webhook(
        self,
        api_key: str,
        webhook_url: str,
    ) -> Dict[str, Any]:
        """Registers a new webhook specifically for incident notifications in the system.

        Args:
            api_key: The API key for authentication with the ServiceNow webhook. (required)
            webhook_url: The URL of the ServiceNow webhook. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def register_webhook(
        self,
        action_update: str,
        collection: str,
        name: str,
        order: str,
        script: str,
        when: str,
    ) -> Dict[str, Any]:
        """Registers a new webhook for real-time notifications in the system.

        Args:
            action_update: Specifies the update action to be performed. (required)
            collection: The collection or table name in Servicenow. (required)
            name: Name of the entity or record. (required)
            order: Order or priority of the action. (required)
            script: Script to be executed in Servicenow. (required)
            when: Condition for when the action should be executed. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_event(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates an existing event in the system.

        Args:
            sysparm_display_value: Return display values instead of internal keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to return in the response.
            sysparm_input_display_value: Use display values for input fields.
            sysparm_query_no_domain: Perform query without domain consideration.
            sysparm_suppress_auto_sys_field: Suppress automatically generated system fields.
            sysparm_view: Name of the view to use for the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_incident(
        self,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the details of an existing incident in the system.

        Args:
            sysparm_display_value: Display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_input_display_value: Use display values for input fields.
            sysparm_query_no_domain: Query without domain restrictions.
            sysparm_suppress_auto_sys_field: Suppress automatically generated sys fields.
            sysparm_view: Name of the view to use.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_system_properties(
        self,
        choices: Optional[str] = None,
        description: Optional[str] = None,
        ignore_cache: Optional[str] = None,
        is_private: Optional[str] = None,
        read_roles: Optional[str] = None,
        suffix: Optional[str] = None,
        sys_class_name: Optional[str] = None,
        sys_created_by: Optional[str] = None,
        sys_created_on: Optional[str] = None,
        sys_mod_count: Optional[str] = None,
        sys_name: Optional[str] = None,
        sys_package: Optional[Dict[str, Any]] = None,
        sys_policy: Optional[str] = None,
        sys_scope: Optional[Dict[str, Any]] = None,
        sys_tags: Optional[str] = None,
        sys_update_name: Optional[str] = None,
        sys_updated_by: Optional[str] = None,
        sys_updated_on: Optional[str] = None,
        type: Optional[str] = None,
        value: Optional[str] = None,
        write_roles: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates existing system properties in the system.

        Args:
            choices: Available choices for the field.
            description: Description of the record.
            ignore_cache: Flag to ignore cache.
            is_private: Indicates if the record is private.
            read_roles: Roles with read access to the record.
            suffix: Suffix of the record name.
            sys_class_name: Name of the system class.
            sys_created_by: User who created the record.
            sys_created_on: Timestamp of record creation.
            sys_mod_count: Number of times the record has been modified.
            sys_name: Name of the record.
            sys_package: Information about the system package.
            sys_policy: System policy associated with the record.
            sys_scope: Information about the system scope.
            sys_tags: Tags associated with the record.
            sys_update_name: Name of the system update.
            sys_updated_by: User who last updated the record.
            sys_updated_on: Timestamp of the last record update.
            type: Type of the record.
            value: Value of the field.
            write_roles: Roles with write access to the record.
        Returns:
            API response as a dictionary.
        """
        ...

