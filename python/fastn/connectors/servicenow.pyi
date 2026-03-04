"""Fastn ServiceNow connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _ServicenowCreateAssetAssignedTo(TypedDict, total=False):
    link: str
    value: str

class _ServicenowCreateAssetCi(TypedDict, total=False):
    link: str
    value: str

class _ServicenowCreateAssetCompany(TypedDict, total=False):
    link: str
    value: str

class _ServicenowCreateAssetCostCenter(TypedDict, total=False):
    link: str
    value: str

class _ServicenowCreateAssetDepartment(TypedDict, total=False):
    link: str
    value: str

class _ServicenowCreateAssetDepreciation(TypedDict, total=False):
    link: str
    value: str

class _ServicenowCreateAssetLocation(TypedDict, total=False):
    link: str
    value: str

class _ServicenowCreateAssetModel(TypedDict, total=False):
    link: str
    value: str

class _ServicenowCreateAssetModelCategory(TypedDict, total=False):
    link: str
    value: str

class _ServicenowCreateAssetSysDomain(TypedDict, total=False):
    link: str
    value: str

class _ServicenowCreateAssetVendor(TypedDict, total=False):
    link: str
    value: str

class _ServicenowCreateSystemPropertySysPackage(TypedDict, total=False):
    link: str
    value: str

class _ServicenowCreateSystemPropertySysScope(TypedDict, total=False):
    link: str
    value: str

class _ServicenowUpdateSystemPropertySysPackage(TypedDict, total=False):
    link: str
    value: str

class _ServicenowUpdateSystemPropertySysScope(TypedDict, total=False):
    link: str
    value: str

class ServicenowConnector:
    """ServiceNow connector ().

    Provides 36 tools.
    """

    def servicenow_create_asset(
        self,
        acquisition_method: Optional[str] = None,
        asset_function: Optional[str] = None,
        asset_tag: Optional[str] = None,
        assigned: Optional[str] = None,
        assigned_to: Optional[_ServicenowCreateAssetAssignedTo] = None,
        beneficiary: Optional[str] = None,
        checked_in: Optional[str] = None,
        checked_out: Optional[str] = None,
        ci: Optional[_ServicenowCreateAssetCi] = None,
        comments: Optional[str] = None,
        company: Optional[_ServicenowCreateAssetCompany] = None,
        cost: Optional[str] = None,
        cost_center: Optional[_ServicenowCreateAssetCostCenter] = None,
        delivery_date: Optional[str] = None,
        department: Optional[_ServicenowCreateAssetDepartment] = None,
        depreciated_amount: Optional[str] = None,
        depreciation: Optional[_ServicenowCreateAssetDepreciation] = None,
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
        location: Optional[_ServicenowCreateAssetLocation] = None,
        managed_by: Optional[str] = None,
        model: Optional[_ServicenowCreateAssetModel] = None,
        model_category: Optional[_ServicenowCreateAssetModelCategory] = None,
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
        sys_domain: Optional[_ServicenowCreateAssetSysDomain] = None,
        sys_domain_path: Optional[str] = None,
        sys_id: Optional[str] = None,
        sys_mod_count: Optional[str] = None,
        sys_tags: Optional[str] = None,
        sys_updated_by: Optional[str] = None,
        sys_updated_on: Optional[str] = None,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
        vendor: Optional[_ServicenowCreateAssetVendor] = None,
        warranty_expiration: Optional[str] = None,
        work_notes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new asset record in the ServiceNow Asset Management (alm_asset) table. Use this tool to register a new IT or physical asset for tracking, lifecycle management, and reporting. Do not use this tool to update an existing asset — use an update tool instead. The new asset will immediately appear in asset management views and reports.

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
            sysparm_display_value: Return display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_input_display_value: Use display values for input fields.
            sysparm_suppress_auto_sys_field: Suppress automatically generated system fields.
            sysparm_view: Specify a view to filter the results.
            vendor: Details of the vendor.
            warranty_expiration: Warranty expiration date.
            work_notes: Notes related to the asset.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_create_event(
        self,
        additional_info: Optional[str] = None,
        alert: Optional[str] = None,
        bucket: Optional[str] = None,
        ci_identifier: Optional[str] = None,
        ci_type: Optional[str] = None,
        classification: Optional[str] = None,
        cmdb_ci: Optional[str] = None,
        description: Optional[str] = None,
        error_msg: Optional[str] = None,
        event_class: Optional[str] = None,
        event_rule: Optional[str] = None,
        message_key: Optional[str] = None,
        metric_name: Optional[str] = None,
        node: Optional[str] = None,
        processed: Optional[str] = None,
        processing_duration: Optional[str] = None,
        processing_notes: Optional[str] = None,
        processing_sn_node: Optional[str] = None,
        resolution_state: Optional[str] = None,
        resource: Optional[str] = None,
        severity: Optional[str] = None,
        source: Optional[str] = None,
        state: Optional[str] = None,
        sys_created_by: Optional[str] = None,
        sys_created_on: Optional[str] = None,
        sys_domain: Optional[str] = None,
        sys_id: Optional[str] = None,
        sys_mod_count: Optional[str] = None,
        sys_tags: Optional[str] = None,
        sys_updated_by: Optional[str] = None,
        sys_updated_on: Optional[str] = None,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
        time_of_event: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new event record in the ServiceNow Event Management (em_event) table. Use this tool to ingest or report a new event into ServiceNow for processing, alerting, or correlation. Do not use this tool to update an existing event — use servicenow_update_event instead. Creating an event may trigger downstream automation, alert rules, or incident creation workflows.

        Args:
            additional_info: Additional information about the event.
            alert: Alert related to the event.
            bucket: Bucket the event belongs to.
            ci_identifier: Identifier of the configuration item.
            ci_type: Type of the configuration item.
            classification: Classification of the event.
            cmdb_ci: Configuration Item in CMDB.
            description: Description of the event.
            error_msg: Error message if any.
            event_class: Class of the event.
            event_rule: Event rule that triggered the event.
            message_key: Key for the event message.
            metric_name: Name of the metric.
            node: Node where the event occurred.
            processed: Indicates if the event has been processed.
            processing_duration: Duration of event processing.
            processing_notes: Notes on the event processing.
            processing_sn_node: The ServiceNow node processing the event.
            resolution_state: The resolution state of the event.
            resource: Resource related to the event.
            severity: Severity level of the event.
            source: Source of the event.
            state: Current state of the event.
            sys_created_by: User who created the record.
            sys_created_on: Timestamp of record creation.
            sys_domain: System domain of the record.
            sys_id: System ID of the record.
            sys_mod_count: Number of times the record has been modified.
            sys_tags: System tags associated with the record.
            sys_updated_by: User who last updated the record.
            sys_updated_on: Timestamp of the last update.
            sysparm_display_value: Return display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to return.
            sysparm_input_display_value: Use display values for input fields.
            sysparm_suppress_auto_sys_field: Suppress automatically generated system fields.
            sysparm_view: Specifies the view to use for the query.
            time_of_event: Timestamp of the event.
            type: Type of the event.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_create_hardware(
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
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
        vendor: Optional[str] = None,
        warranty_expiration: Optional[str] = None,
        work_notes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new hardware asset record in the ServiceNow Hardware Asset Management (alm_hardware) table. Use this tool to register a new physical hardware item such as a server, laptop, or network device for tracking and lifecycle management. Do not use this tool to create a hardware model definition — use servicenow_create_model instead. The new hardware record will immediately be available in hardware asset management views.

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
            sysparm_display_value: Display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to return.
            sysparm_input_display_value: Use display values for input fields.
            sysparm_suppress_auto_sys_field: Suppress automatic system fields.
            sysparm_view: View to use for the request.
            vendor: Vendor.
            warranty_expiration: Warranty expiration date.
            work_notes: Work notes.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_create_incident(
        self,
        active: Optional[str] = None,
        activity_due: Optional[str] = None,
        additional_assignee_list: Optional[str] = None,
        approval: Optional[str] = None,
        approval_history: Optional[str] = None,
        approval_set: Optional[str] = None,
        assigned_to: Optional[str] = None,
        assignment_group: Optional[str] = None,
        business_duration: Optional[str] = None,
        business_impact: Optional[str] = None,
        business_service: Optional[str] = None,
        business_stc: Optional[str] = None,
        calendar_duration: Optional[str] = None,
        calendar_stc: Optional[str] = None,
        caller_id: Optional[str] = None,
        category: Optional[str] = None,
        cause: Optional[str] = None,
        caused_by: Optional[str] = None,
        child_incidents: Optional[str] = None,
        close_code: Optional[str] = None,
        close_notes: Optional[str] = None,
        closed_at: Optional[str] = None,
        closed_by: Optional[str] = None,
        cmdb_ci: Optional[str] = None,
        comments: Optional[str] = None,
        comments_and_work_notes: Optional[str] = None,
        company: Optional[str] = None,
        contact_type: Optional[str] = None,
        contract: Optional[str] = None,
        correlation_display: Optional[str] = None,
        correlation_id: Optional[str] = None,
        delivery_plan: Optional[str] = None,
        delivery_task: Optional[str] = None,
        description: Optional[str] = None,
        due_date: Optional[str] = None,
        escalation: Optional[str] = None,
        expected_start: Optional[str] = None,
        follow_up: Optional[str] = None,
        group_list: Optional[str] = None,
        hold_reason: Optional[str] = None,
        impact: Optional[str] = None,
        incident_state: Optional[str] = None,
        knowledge: Optional[str] = None,
        location: Optional[str] = None,
        made_sla: Optional[str] = None,
        notify: Optional[str] = None,
        number: Optional[str] = None,
        opened_at: Optional[str] = None,
        opened_by: Optional[str] = None,
        order: Optional[str] = None,
        origin_id: Optional[str] = None,
        origin_table: Optional[str] = None,
        parent: Optional[str] = None,
        parent_incident: Optional[str] = None,
        priority: Optional[str] = None,
        problem_id: Optional[str] = None,
        reassignment_count: Optional[str] = None,
        reopen_count: Optional[str] = None,
        reopened_by: Optional[str] = None,
        reopened_time: Optional[str] = None,
        resolved_at: Optional[str] = None,
        resolved_by: Optional[str] = None,
        rfc: Optional[str] = None,
        route_reason: Optional[str] = None,
        service_offering: Optional[str] = None,
        severity: Optional[str] = None,
        short_description: Optional[str] = None,
        sla_due: Optional[str] = None,
        state: Optional[str] = None,
        subcategory: Optional[str] = None,
        sys_class_name: Optional[str] = None,
        sys_created_by: Optional[str] = None,
        sys_created_on: Optional[str] = None,
        sys_domain: Optional[str] = None,
        sys_domain_path: Optional[str] = None,
        sys_id: Optional[str] = None,
        sys_mod_count: Optional[str] = None,
        sys_tags: Optional[str] = None,
        sys_updated_by: Optional[str] = None,
        sys_updated_on: Optional[str] = None,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
        task_effective_number: Optional[str] = None,
        time_worked: Optional[str] = None,
        universal_request: Optional[str] = None,
        upon_approval: Optional[str] = None,
        upon_reject: Optional[str] = None,
        urgency: Optional[str] = None,
        user_input: Optional[str] = None,
        watch_list: Optional[str] = None,
        work_end: Optional[str] = None,
        work_notes: Optional[str] = None,
        work_notes_list: Optional[str] = None,
        work_start: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new incident record in the ServiceNow incident table. Use this tool to report a new IT issue, outage, or service disruption that requires tracking and resolution. Do not use this tool to update an existing incident — use servicenow_update_incident instead. Creating an incident may trigger SLA timers, assignment rules, and notification workflows.

        Args:
            active: Indicates if the incident is active.
            activity_due: Due date for activity.
            additional_assignee_list: List of additional assignees.
            approval: Approval status.
            approval_history: History of approvals.
            approval_set: Approval set for the incident.
            assigned_to: User assigned to the incident.
            assignment_group: Assigned group for the incident.
            business_duration: Business duration of the incident.
            business_impact: Business impact of the incident.
            business_service: Affected business service.
            business_stc: Business scheduled time code.
            calendar_duration: Calendar duration of the incident.
            calendar_stc: Calendar scheduled time code.
            caller_id: ID of the caller.
            category: Category of the incident.
            cause: Root cause of the incident.
            caused_by: The cause of the incident.
            child_incidents: List of child incidents.
            close_code: Close code for the incident.
            close_notes: Notes upon closure.
            closed_at: Timestamp of incident closure.
            closed_by: User who closed the incident.
            cmdb_ci: Configuration Item (CI) related to the incident.
            comments: Comments related to the incident.
            comments_and_work_notes: Combined comments and work notes.
            company: Company related to the incident.
            contact_type: Type of contact.
            contract: Related contract number.
            correlation_display: Correlation display value.
            correlation_id: Correlation ID.
            delivery_plan: Associated delivery plan.
            delivery_task: Associated delivery task.
            description: Detailed description of the incident.
            due_date: Due date for the incident.
            escalation: Escalation information.
            expected_start: Expected start time.
            follow_up: Follow-up information.
            group_list: List of assigned groups.
            hold_reason: Reason for placing the incident on hold.
            impact: Impact of the incident.
            incident_state: State of the incident.
            knowledge: Knowledge base article related to the incident.
            location: Location of the incident.
            made_sla: Indicates if the SLA is met.
            notify: Notification settings.
            number: The unique number assigned to the incident.
            opened_at: Timestamp of incident opening.
            opened_by: User who opened the incident.
            order: Related order number.
            origin_id: ID of the origin.
            origin_table: The table from which the incident originated.
            parent: The ID of the parent incident.
            parent_incident: ID of the parent incident.
            priority: Priority of the incident.
            problem_id: Related problem ID.
            reassignment_count: Number of reassignments.
            reopen_count: Number of times reopened.
            reopened_by: User who reopened the incident.
            reopened_time: Timestamp of last reopen.
            resolved_at: Timestamp of resolution.
            resolved_by: User who resolved the incident.
            rfc: Request for Change (RFC) number.
            route_reason: Reason for routing the incident.
            service_offering: Service offering related to the incident.
            severity: Severity of the incident.
            short_description: Short description of the incident.
            sla_due: SLA due date.
            state: The current state of the incident.
            subcategory: Subcategory of the incident.
            sys_class_name: Name of the class.
            sys_created_by: User who created the incident.
            sys_created_on: Timestamp of incident creation.
            sys_domain: The domain of the incident.
            sys_domain_path: Path of the domain.
            sys_id: System ID.
            sys_mod_count: Number of modifications.
            sys_tags: System tags.
            sys_updated_by: User who last updated the incident.
            sys_updated_on: Timestamp of the last update.
            sysparm_display_value: Return display values for fields.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Specify the fields to be returned in the response.
            sysparm_input_display_value: Return input display values for fields.
            sysparm_suppress_auto_sys_field: Suppress automatically generated sys fields in the response.
            sysparm_view: Specify the view to be used for the request.
            task_effective_number: Effective number of the task.
            time_worked: Time spent working on the incident.
            universal_request: Universal request ID.
            upon_approval: Action upon approval.
            upon_reject: Action to be taken upon rejection.
            urgency: Urgency of the incident.
            user_input: User input related to the incident.
            watch_list: Indicates if the incident is on a watch list.
            work_end: End time of work.
            work_notes: Work notes for the incident.
            work_notes_list: List of work notes.
            work_start: Start time of work.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_create_model(
        self,
        acquisition_method: Optional[str] = None,
        asset_tracking_strategy: Optional[str] = None,
        asset_tracking_unit: Optional[str] = None,
        barcode: Optional[str] = None,
        bundle: Optional[str] = None,
        certified: Optional[str] = None,
        cmdb_ci_class: Optional[str] = None,
        cmdb_model_category: Optional[str] = None,
        comments: Optional[str] = None,
        cost: Optional[str] = None,
        current: Optional[str] = None,
        current_unit: Optional[str] = None,
        depreciation: Optional[str] = None,
        depth: Optional[str] = None,
        description: Optional[str] = None,
        dimensions_unit: Optional[str] = None,
        display_name: Optional[str] = None,
        energy_star: Optional[str] = None,
        energy_use: Optional[str] = None,
        expected_lifetime_co2e: Optional[str] = None,
        expenditure_type: Optional[str] = None,
        flow_rate: Optional[str] = None,
        full_name: Optional[str] = None,
        height: Optional[str] = None,
        length: Optional[str] = None,
        life_cycle_stage: Optional[str] = None,
        life_cycle_stage_status: Optional[str] = None,
        main_component: Optional[str] = None,
        manufacturer: Optional[str] = None,
        model_number: Optional[str] = None,
        name: Optional[str] = None,
        owner: Optional[str] = None,
        picture: Optional[str] = None,
        power_consumption: Optional[str] = None,
        power_unit: Optional[str] = None,
        product_catalog_item: Optional[str] = None,
        rack_units: Optional[str] = None,
        rated_power: Optional[str] = None,
        salvage_value: Optional[str] = None,
        short_description: Optional[str] = None,
        sla: Optional[str] = None,
        socket_count: Optional[str] = None,
        sound_power: Optional[str] = None,
        status: Optional[str] = None,
        sys_class_name: Optional[str] = None,
        sys_created_by: Optional[str] = None,
        sys_created_on: Optional[str] = None,
        sys_domain: Optional[str] = None,
        sys_domain_path: Optional[str] = None,
        sys_id: Optional[str] = None,
        sys_mod_count: Optional[str] = None,
        sys_tags: Optional[str] = None,
        sys_updated_by: Optional[str] = None,
        sys_updated_on: Optional[str] = None,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
        type: Optional[str] = None,
        unit_of_measure_system: Optional[str] = None,
        useful_life: Optional[str] = None,
        voltage: Optional[str] = None,
        voltage_unit: Optional[str] = None,
        volume: Optional[str] = None,
        volume_unit: Optional[str] = None,
        weight: Optional[str] = None,
        weight_decimal: Optional[str] = None,
        weight_unit: Optional[str] = None,
        width: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new hardware product model record in the ServiceNow CMDB (cmdb_hardware_product_model) table. Use this tool to define a new hardware model that can then be associated with hardware asset records. Do not use this tool to update an existing model — use an update tool instead. The new model record will be immediately available for association with hardware and asset records.

        Args:
            acquisition_method: Method of acquisition.
            asset_tracking_strategy: Strategy for asset tracking.
            asset_tracking_unit: Unit for asset tracking.
            barcode: Barcode of the asset.
            bundle: Bundle information.
            certified: Certification status.
            cmdb_ci_class: CMDB Configuration Item class.
            cmdb_model_category: Category of the CMDB model.
            comments: Comments about the asset.
            cost: Cost of the asset.
            current: Current value.
            current_unit: Unit of measurement for current.
            depreciation: Depreciation value.
            depth: Depth of the asset.
            description: Detailed description of the asset.
            dimensions_unit: Unit of measurement for dimensions.
            display_name: Display name of the asset.
            energy_star: Energy Star rating.
            energy_use: Energy consumption.
            expected_lifetime_co2e: Expected CO2 emissions over the asset's lifetime.
            expenditure_type: Type of expenditure.
            flow_rate: Flow rate of the asset.
            full_name: Full name of the asset.
            height: Height of the asset.
            length: Length of the asset.
            life_cycle_stage: Current life cycle stage of the asset.
            life_cycle_stage_status: Status of the life cycle stage.
            main_component: Main component of the asset.
            manufacturer: Manufacturer of the asset.
            model_number: Model number of the asset.
            name: Name of the asset.
            owner: Owner of the asset.
            picture: Picture of the asset.
            power_consumption: Power consumption of the asset.
            power_unit: Unit of measurement for power.
            product_catalog_item: Associated product catalog item.
            rack_units: Number of rack units.
            rated_power: Rated power of the asset.
            salvage_value: Salvage value of the asset.
            short_description: Short description of the asset.
            sla: Service Level Agreement.
            socket_count: Number of sockets.
            sound_power: Sound power of the asset.
            status: Status of the asset.
            sys_class_name: Name of the system class.
            sys_created_by: User who created the record.
            sys_created_on: Timestamp of record creation.
            sys_domain: System domain of the record.
            sys_domain_path: Path to the system domain.
            sys_id: Unique identifier of the record.
            sys_mod_count: Number of modifications.
            sys_tags: System tags associated with the record.
            sys_updated_by: User who last updated the record.
            sys_updated_on: Timestamp of the last update.
            sysparm_display_value: Display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to include in the response.
            sysparm_input_display_value: Use display values for input fields.
            sysparm_suppress_auto_sys_field: Suppress automatically generated system fields.
            sysparm_view: Name of the view to use for the request.
            type: Type of the asset.
            unit_of_measure_system: System of units used for measurements.
            useful_life: Useful life of the asset.
            voltage: Voltage value.
            voltage_unit: Unit of measurement for voltage.
            volume: Volume of the asset.
            volume_unit: Unit of measurement for volume.
            weight: Weight of the asset.
            weight_decimal: Weight in decimal format.
            weight_unit: Unit of measurement for weight.
            width: Width of the asset.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_create_system_property(
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
        sys_package: Optional[_ServicenowCreateSystemPropertySysPackage] = None,
        sys_policy: Optional[str] = None,
        sys_scope: Optional[_ServicenowCreateSystemPropertySysScope] = None,
        sys_tags: Optional[str] = None,
        sys_update_name: Optional[str] = None,
        sys_updated_by: Optional[str] = None,
        sys_updated_on: Optional[str] = None,
        type: Optional[str] = None,
        value: Optional[str] = None,
        write_roles: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new system property record on the ServiceNow instance. Use this tool when a required configuration property does not yet exist and must be added. Do not use this tool to modify an existing property — use servicenow_update_system_property instead. Creating a system property with an incorrect name or value may affect system or application behavior.

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

    def servicenow_delete_asset(
        self,
        sysId: str,
        sysparm_query_no_domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific asset record from the ServiceNow Asset Management (alm_asset) table, identified by its unique sys_id. Use this tool only when an asset must be completely removed from the system. Do not use this tool to retire or decommission an asset — update the asset state using an update tool instead. This action is irreversible and all associated asset data will be lost.

        Args:
            sysId: ServiceNow system ID. (required)
            sysparm_query_no_domain: ServiceNow query parameter (without domain).
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_delete_business_rule(
        self,
        sysId: str,
        sysparm_query_no_domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a ServiceNow business rule script record identified by its unique sys_id. Use this tool to remove a business rule that is no longer needed, such as a previously registered webhook script. Do not use this tool to deactivate a rule — modify it using an update tool instead. This action is irreversible and will immediately stop the rule from executing; deleting an active webhook rule will stop all associated notifications.

        Args:
            sysId: ServiceNow sys_id. (required)
            sysparm_query_no_domain: Query parameter for ServiceNow API (excluding domain).
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_delete_event(
        self,
        sysId: str,
        sysparm_query_no_domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific event record from the ServiceNow Event Management (em_event) table identified by its unique sys_id. Use this tool only when an event record must be completely removed. Do not use this tool to update event details — use servicenow_update_event instead. This action is irreversible and the deleted event data cannot be recovered.

        Args:
            sysId: ServiceNow sys_id parameter for specifying a specific record. (required)
            sysparm_query_no_domain: Query parameter for the ServiceNow API request (without domain).
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_delete_hardware(
        self,
        sysId: str,
        sysparm_query_no_domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific hardware asset record from the ServiceNow Hardware Asset Management (alm_hardware) table, identified by its unique sys_id. Use this tool only when a hardware record must be completely removed from the system. Do not use this tool to decommission hardware — update the hardware state using an update tool instead. This action is irreversible.

        Args:
            sysId: System ID of the target record in Servicenow. (required)
            sysparm_query_no_domain: Query parameter for filtering results, excluding domain considerations.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_delete_incident(
        self,
        sys_id: str,
        sysparm_query_no_domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific incident record from the ServiceNow incident table, identified by its unique sys_id. Use this tool only when an incident must be completely removed from the system. Do not use this tool to resolve or close an incident — use servicenow_update_incident to change the incident state instead. This action is irreversible and all associated incident data will be lost.

        Args:
            sys_id: ServiceNow system ID. (required)
            sysparm_query_no_domain: ServiceNow query string without domain specification.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_delete_model(
        self,
        sysId: str,
        sysparm_query_no_domain: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific hardware product model record from the ServiceNow CMDB (cmdb_hardware_product_model) table, identified by its unique sys_id. Use this tool only when a hardware model definition must be completely removed. Do not use this tool if assets or hardware records are still associated with this model, as removal may cause data integrity issues. This action is irreversible.

        Args:
            sysId: ServiceNow sys_id parameter. (required)
            sysparm_query_no_domain: Query parameter for ServiceNow API (without domain).
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_delete_system_property(
        self,
        sys_id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a ServiceNow system property record identified by its unique sys_id. Use this tool only when a system property must be completely removed from the instance. Do not use this tool to update or disable a property — use servicenow_update_system_property instead. This action is irreversible and may affect system behavior if the property is actively used by applications or scripts.

        Args:
            sys_id: ServiceNow system ID of the target record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_delete_webhook(
        self,
        sysId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a webhook business rule script record from the ServiceNow instance, identified by its unique sys_id. Use this tool to deregister a previously registered webhook and stop it from sending notifications. Do not use this tool to delete a non-webhook business rule — use servicenow_delete_business_rule for clarity, as both target the same underlying table. This action is irreversible and will immediately halt all notifications associated with the deleted webhook.

        Args:
            sysId: ServiceNow system ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_get_access_token(
        self,
        client_id: str,
        client_secret: str,
        code: str,
        redirect_uri: str,
    ) -> Dict[str, Any]:
        """Obtains a new OAuth access token from ServiceNow using client credentials or authorization code flow. Use this tool to establish an authenticated session before calling any other ServiceNow tool that requires authorization. Do not use this tool to renew an existing token — use servicenow_refresh_token instead. This tool makes a POST request to the ServiceNow OAuth token endpoint.

        Args:
            client_id: Client ID for the ServiceNow application. (required)
            client_secret: Client secret for the ServiceNow application. (required)
            code: Authorization code received from ServiceNow. (required)
            redirect_uri: Redirect URI registered for the ServiceNow application. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_get_asset(
        self,
        sysId: str,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single asset record from the ServiceNow Asset Management (alm_asset) table, identified by its unique sys_id. Use this tool to read all fields of a specific asset. Do not use this tool to list all assets — use servicenow_list_assets instead. This is a read-only operation with no side effects.

        Args:
            sysId: System ID of the record. (required)
            sysparm_display_value: Return display values instead of internal values.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to return.
            sysparm_query_no_domain: Query without domain.
            sysparm_view: View to use for the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_get_event(
        self,
        sysId: str,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single ServiceNow event record from the Event Management (em_event) table, identified by its unique sys_id. Use this tool when you need to read the full details of a specific event. Do not use this tool to retrieve multiple events — use servicenow_list_events instead. This is a read-only operation with no side effects.

        Args:
            sysId: System ID of the record. (required)
            sysparm_display_value: Return display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_query_no_domain: Query without domain qualification.
            sysparm_view: View to use for the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_get_hardware(
        self,
        sysId: str,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single hardware asset record from the ServiceNow Hardware Asset Management (alm_hardware) table, identified by its unique sys_id. Use this tool to read all fields of a specific hardware item. Do not use this tool to list all hardware records — use servicenow_list_hardwares instead. This is a read-only operation with no side effects.

        Args:
            sysId: System ID of the record. (required)
            sysparm_display_value: Display value instead of sys_id.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to return.
            sysparm_query_no_domain: Query without domain.
            sysparm_view: View to use for the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_get_incident(
        self,
        sysId: str,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single ServiceNow incident record identified by its unique sys_id. Use this tool when you need to read all fields of a specific incident. Do not use this tool to retrieve multiple incidents — use servicenow_list_incidents instead. This is a read-only operation with no side effects.

        Args:
            sysId: The sys_id of the ServiceNow record. (required)
            sysparm_display_value: Display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_query_no_domain: Perform query without domain consideration.
            sysparm_view: Specify a view for the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_get_model(
        self,
        sysId: str,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single hardware product model record from the ServiceNow CMDB (cmdb_hardware_product_model) table, identified by its unique sys_id. Use this tool to inspect a specific hardware models attributes. Do not use this tool to list all models — use servicenow_list_models instead. This is a read-only operation with no side effects.

        Args:
            sysId: The sys_id of the record. (required)
            sysparm_display_value: Retrieve display values instead of sys_ids.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_query_no_domain: Perform query without domain consideration.
            sysparm_view: Name of the view to use for the query.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_get_system_property(
        self,
        sys_id: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single ServiceNow system property record identified by its unique sys_id. Use this tool when you need to read the current value or metadata of a specific system property. Do not use this tool to retrieve multiple properties at once — use servicenow_list_system_properties instead. This is a read-only operation with no side effects.

        Args:
            sys_id: The sys_id of the ServiceNow record. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_list_assets(
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
        """Retrieves a list of all asset records currently managed in the ServiceNow Asset Management (alm_asset) table. Use this tool to browse, audit, or search for assets across the system. Do not use this tool to retrieve a single asset by sys_id — use servicenow_get_asset instead. This is a read-only operation with no side effects.

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

    def servicenow_list_business_rules(
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
        """Retrieves a list of all business rule script records on the ServiceNow instance. Use this tool to inspect existing business rules, audit webhook registrations, or find a specific rules sys_id before updating or deleting it. Do not use this tool to retrieve a single business rule by sys_id. This is a read-only operation with no side effects.

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

    def servicenow_list_events(
        self,
        tableName: str,
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
        """Retrieves a list of all event records from a specified ServiceNow table. Use this tool to browse or audit events recorded in the system, or to find a specific events sys_id before performing an update or delete. Do not use this tool to retrieve a single event by sys_id — use servicenow_get_event instead. This is a read-only operation with no side effects.

        Args:
            tableName: Name of the Servicenow table to query. (required)
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

    def servicenow_list_hardwares(
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
        """Retrieves a list of all hardware asset records from the ServiceNow Hardware Asset Management (alm_hardware) table. Use this tool to browse, audit, or search for hardware items tracked in the system. Do not use this tool to retrieve a single hardware record by sys_id — use servicenow_get_hardware instead. This is a read-only operation with no side effects.

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

    def servicenow_list_incidents(
        self,
        sysparm_fields: Optional[str] = None,
        sysparm_limit: Optional[str] = None,
        sysparm_offset: Optional[str] = None,
        sysparm_query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all incident records from the ServiceNow incident table. Use this tool to browse, audit, or search for incidents across the system. Do not use this tool to retrieve a single incident by sys_id — use servicenow_get_incident instead. This is a read-only operation with no side effects.

        Args:
            sysparm_fields: Comma-separated list of fields to retrieve from ServiceNow.
            sysparm_limit: Limit for the number of records to retrieve from ServiceNow.
            sysparm_offset: Offset for pagination in ServiceNow API response.
            sysparm_query: ServiceNow query string for filtering records.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_list_models(
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
        """Retrieves a list of all hardware product model records from the ServiceNow CMDB (cmdb_hardware_product_model) table. Use this tool to browse available hardware models or find a specific models sys_id before associating it with hardware or asset records. Do not use this tool to retrieve a single model by sys_id — use servicenow_get_model instead. This is a read-only operation with no side effects.

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

    def servicenow_list_system_properties(
        self,
        sysparm_limit: Optional[int] = None,
        sysparm_offset: Optional[int] = None,
        sysparm_query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all system property records available on the ServiceNow instance. Use this tool when you need an overview of all configured system properties or want to search for a specific property by browsing the full list. Do not use this tool to fetch a single property by sys_id — use servicenow_get_system_property instead. This is a read-only operation with no side effects.

        Args:
            sysparm_limit: The maximum number of records to return.
            sysparm_offset: The starting record offset for pagination.
            sysparm_query: A ServiceNow query string to filter results.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_prevent_duplicate_webhooks(
        self,
        action_delete: Optional[bool] = None,
        action_insert: Optional[bool] = None,
        action_query: Optional[bool] = None,
        action_update: Optional[bool] = None,
        name: Optional[str] = None,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Checks for and prevents the creation of duplicate webhook business rule scripts on the ServiceNow instance by querying existing scripts before registration. Use this tool before calling any webhook registration tool (servicenow_register_webhook, servicenow_register_events_webhook, or servicenow_register_incident_webhook) to ensure idempotent webhook setup. Do not use this tool as a standalone webhook registration — it does not create a webhook itself.

        Args:
            action_delete: Indicates whether to delete a record.
            action_insert: Indicates whether to insert a new record.
            action_query: Indicates whether to query records.
            action_update: Indicates whether to update an existing record.
            name: Name of the record.
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

    def servicenow_refresh_token(
        self,
        client_id: str,
        client_secret: str,
        refresh_token: str,
    ) -> Dict[str, Any]:
        """Refreshes an existing OAuth access token to maintain an authenticated session with ServiceNow. Use this tool when a previously issued access token has expired and needs to be renewed without requiring the user to re-authenticate. This tool makes a POST request to the ServiceNow OAuth token endpoint. Note: this tool manages authentication credentials — misuse may disrupt active sessions.

        Args:
            client_id: Client ID for authentication. (required)
            client_secret: Client secret for authentication. (required)
            refresh_token: Refresh token for authentication. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_register_events_webhook(
        self,
        api_key: str,
        name: str,
        url: str,
        delete: Optional[bool] = None,
        insert: Optional[bool] = None,
        query: Optional[bool] = None,
        update: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Registers a new business rule script on the ServiceNow instance that acts as a webhook to send event notifications to an external endpoint. Use this tool when you need to receive real-time push notifications for ServiceNow event table changes. Do not use this tool for incident-specific webhooks — use servicenow_register_incident_webhook instead. To avoid duplicates, call servicenow_prevent_duplicate_webhooks before registering. This action creates a persistent server-side script and may affect system performance if overused.

        Args:
            api_key: API key for authentication with the Servicenow webhook. (required)
            name: Name of the integration. (required)
            url: URL of the Servicenow webhook. (required)
            delete: Indicates if delete operations are allowed.
            insert: Indicates if insert operations are allowed.
            query: Indicates if query operations are allowed.
            update: Indicates if update operations are allowed.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_register_incident_webhook(
        self,
        api_key: str,
        name: str,
        query: bool,
        webhook_url: str,
        delete: Optional[bool] = None,
        insert: Optional[bool] = None,
        update: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Registers a new business rule script on the ServiceNow instance that acts as a webhook to send real-time push notifications for incident table changes to an external endpoint. Use this tool when you need to be notified of incident create, update, or delete events. Do not use this tool for generic or event-based webhooks — use servicenow_register_events_webhook or servicenow_register_webhook instead. To avoid duplicates, call servicenow_prevent_duplicate_webhooks before registering. This action creates a persistent server-side script.

        Args:
            api_key: The API key for authentication with the ServiceNow webhook. (required)
            name: A descriptive name for this webhook configuration. (required)
            query: Indicates if query operations are allowed. (required)
            webhook_url: The URL of the ServiceNow webhook. (required)
            delete: Indicates if delete operations are allowed.
            insert: Indicates if insert operations are allowed.
            update: Indicates if update operations are allowed.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_register_webhook(
        self,
        action_update: str,
        collection: str,
        name: str,
        order: str,
        script: str,
        when: str,
    ) -> Dict[str, Any]:
        """Registers a new general-purpose business rule script on the ServiceNow instance to send real-time push notifications to an external endpoint. Use this tool when you need webhook notifications for ServiceNow table changes that are not covered by the incident-specific or event-specific webhook tools. To avoid duplicates, call servicenow_prevent_duplicate_webhooks before registering. This action creates a persistent server-side script and may affect system performance if overused.

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

    def servicenow_update_event(
        self,
        sysId: str,
        additional_info: Optional[str] = None,
        alert: Optional[str] = None,
        bucket: Optional[str] = None,
        ci_identifier: Optional[str] = None,
        ci_type: Optional[str] = None,
        classification: Optional[str] = None,
        cmdb_ci: Optional[str] = None,
        description: Optional[str] = None,
        error_msg: Optional[str] = None,
        event_class: Optional[str] = None,
        event_rule: Optional[str] = None,
        message_key: Optional[str] = None,
        metric_name: Optional[str] = None,
        node: Optional[str] = None,
        processed: Optional[str] = None,
        processing_duration: Optional[str] = None,
        processing_notes: Optional[str] = None,
        processing_sn_node: Optional[str] = None,
        resolution_state: Optional[str] = None,
        resource: Optional[str] = None,
        severity: Optional[str] = None,
        source: Optional[str] = None,
        state: Optional[str] = None,
        sys_created_by: Optional[str] = None,
        sys_created_on: Optional[str] = None,
        sys_domain: Optional[str] = None,
        sys_id: Optional[str] = None,
        sys_mod_count: Optional[str] = None,
        sys_tags: Optional[str] = None,
        sys_updated_by: Optional[str] = None,
        sys_updated_on: Optional[str] = None,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
        time_of_event: Optional[str] = None,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Replaces the details of an existing ServiceNow event record in the Event Management (em_event) table, identified by its unique sys_id, using a full PUT update. Use this tool to modify event properties such as severity, state, or description. Do not use this tool to create a new event — use servicenow_create_event instead. Changes are applied immediately and overwrite existing field values.

        Args:
            sysId: System ID from the URL. (required)
            additional_info: Additional information related to the event.
            alert: Alert related to the event.
            bucket: Bucket for the event.
            ci_identifier: Identifier of the Configuration Item (CI).
            ci_type: Type of the Configuration Item (CI).
            classification: Classification of the event.
            cmdb_ci: Configuration Management Database Configuration Item.
            description: Description of the event.
            error_msg: Error message if any.
            event_class: Class of the event.
            event_rule: Event rule that triggered the event.
            message_key: Key for the event message.
            metric_name: Name of the metric associated with the event.
            node: Node related to the event.
            processed: Indicates if the event has been processed.
            processing_duration: Duration of event processing.
            processing_notes: Notes about the event processing.
            processing_sn_node: ServiceNow node processing the event.
            resolution_state: State of the event resolution.
            resource: Resource related to the event.
            severity: Severity level of the event.
            source: Source of the event.
            state: Current state of the event.
            sys_created_by: User who created the record.
            sys_created_on: Timestamp of record creation.
            sys_domain: System domain of the record.
            sys_id: Unique identifier of the record.
            sys_mod_count: Number of times the record has been modified.
            sys_tags: System tags associated with the record.
            sys_updated_by: User who last updated the record.
            sys_updated_on: Timestamp of the last update.
            sysparm_display_value: Return display values instead of internal keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to return in the response.
            sysparm_input_display_value: Use display values for input fields.
            sysparm_query_no_domain: Perform query without domain consideration.
            sysparm_suppress_auto_sys_field: Suppress automatically generated system fields.
            sysparm_view: Name of the view to use for the query.
            time_of_event: Timestamp of the event.
            type: Type of the event.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_update_incident(
        self,
        sysId: str,
        active: Optional[str] = None,
        activity_due: Optional[str] = None,
        additional_assignee_list: Optional[str] = None,
        approval: Optional[str] = None,
        approval_history: Optional[str] = None,
        approval_set: Optional[str] = None,
        assigned_to: Optional[str] = None,
        assignment_group: Optional[str] = None,
        business_duration: Optional[str] = None,
        business_impact: Optional[str] = None,
        business_service: Optional[str] = None,
        business_stc: Optional[str] = None,
        calendar_duration: Optional[str] = None,
        calendar_stc: Optional[str] = None,
        caller_id: Optional[str] = None,
        category: Optional[str] = None,
        cause: Optional[str] = None,
        caused_by: Optional[str] = None,
        child_incidents: Optional[str] = None,
        close_code: Optional[str] = None,
        close_notes: Optional[str] = None,
        closed_at: Optional[str] = None,
        closed_by: Optional[str] = None,
        cmdb_ci: Optional[str] = None,
        comments: Optional[str] = None,
        comments_and_work_notes: Optional[str] = None,
        company: Optional[str] = None,
        contact_type: Optional[str] = None,
        contract: Optional[str] = None,
        correlation_display: Optional[str] = None,
        correlation_id: Optional[str] = None,
        delivery_plan: Optional[str] = None,
        delivery_task: Optional[str] = None,
        description: Optional[str] = None,
        due_date: Optional[str] = None,
        escalation: Optional[str] = None,
        expected_start: Optional[str] = None,
        follow_up: Optional[str] = None,
        group_list: Optional[str] = None,
        hold_reason: Optional[str] = None,
        impact: Optional[str] = None,
        incident_state: Optional[str] = None,
        knowledge: Optional[str] = None,
        location: Optional[str] = None,
        made_sla: Optional[str] = None,
        notify: Optional[str] = None,
        number: Optional[str] = None,
        opened_at: Optional[str] = None,
        opened_by: Optional[str] = None,
        order: Optional[str] = None,
        origin_id: Optional[str] = None,
        origin_table: Optional[str] = None,
        parent: Optional[str] = None,
        parent_incident: Optional[str] = None,
        priority: Optional[str] = None,
        problem_id: Optional[str] = None,
        reassignment_count: Optional[str] = None,
        reopen_count: Optional[str] = None,
        reopened_by: Optional[str] = None,
        reopened_time: Optional[str] = None,
        resolved_at: Optional[str] = None,
        resolved_by: Optional[str] = None,
        rfc: Optional[str] = None,
        route_reason: Optional[str] = None,
        service_offering: Optional[str] = None,
        severity: Optional[str] = None,
        short_description: Optional[str] = None,
        sla_due: Optional[str] = None,
        state: Optional[str] = None,
        subcategory: Optional[str] = None,
        sys_class_name: Optional[str] = None,
        sys_created_by: Optional[str] = None,
        sys_created_on: Optional[str] = None,
        sys_domain: Optional[str] = None,
        sys_domain_path: Optional[str] = None,
        sys_id: Optional[str] = None,
        sys_mod_count: Optional[str] = None,
        sys_tags: Optional[str] = None,
        sys_updated_by: Optional[str] = None,
        sys_updated_on: Optional[str] = None,
        sysparm_display_value: Optional[str] = None,
        sysparm_exclude_reference_link: Optional[str] = None,
        sysparm_fields: Optional[str] = None,
        sysparm_input_display_value: Optional[str] = None,
        sysparm_query_no_domain: Optional[str] = None,
        sysparm_suppress_auto_sys_field: Optional[str] = None,
        sysparm_view: Optional[str] = None,
        task_effective_number: Optional[str] = None,
        time_worked: Optional[str] = None,
        universal_request: Optional[str] = None,
        upon_approval: Optional[str] = None,
        upon_reject: Optional[str] = None,
        urgency: Optional[str] = None,
        user_input: Optional[str] = None,
        watch_list: Optional[str] = None,
        work_end: Optional[str] = None,
        work_notes: Optional[str] = None,
        work_notes_list: Optional[str] = None,
        work_start: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Replaces the details of an existing ServiceNow incident record identified by its unique sys_id using a full PUT update. Use this tool to modify incident fields such as state, priority, assignment group, or description. Do not use this tool to create a new incident — use servicenow_create_incident instead. Changes are applied immediately and overwrite existing field values.

        Args:
            sysId: System ID of the record to retrieve. (required)
            active: Active status.
            activity_due: Activity due date.
            additional_assignee_list: List of additional assignees.
            approval: Approval status.
            approval_history: Approval history.
            approval_set: Approval set association.
            assigned_to: Assigned to user.
            assignment_group: Assigned group.
            business_duration: Business duration.
            business_impact: Business impact of the incident.
            business_service: Business service association.
            business_stc: Business scheduled time.
            calendar_duration: Calendar duration.
            calendar_stc: Calendar scheduled time.
            caller_id: Caller's sys_id.
            category: Category of the incident.
            cause: Root cause of the incident.
            caused_by: Cause of the incident.
            child_incidents: Child incident records.
            close_code: Close code.
            close_notes: Notes upon closing.
            closed_at: Closed timestamp.
            closed_by: User who closed the incident.
            cmdb_ci: CMDB CI association.
            comments: Comments.
            comments_and_work_notes: Combined comments and work notes.
            company: Company association.
            contact_type: Type of contact.
            contract: Contract association.
            correlation_display: Correlation display value.
            correlation_id: Correlation ID.
            delivery_plan: Delivery plan association.
            delivery_task: Delivery task association.
            description: Description of the incident.
            due_date: Due date.
            escalation: Escalation details.
            expected_start: Expected start time.
            follow_up: Follow-up information.
            group_list: List of assigned groups.
            hold_reason: Reason for holding the incident.
            impact: Impact of the incident.
            incident_state: Incident state.
            knowledge: Knowledge base article association.
            location: Location of the incident.
            made_sla: SLA met indicator.
            notify: Notification settings.
            number: Incident number.
            opened_at: Opened timestamp.
            opened_by: User who opened the incident.
            order: Order number.
            origin_id: Originating record ID.
            origin_table: Originating table.
            parent: Parent record sys_id.
            parent_incident: Parent incident sys_id.
            priority: Priority of the incident.
            problem_id: Problem record sys_id.
            reassignment_count: Number of reassignments.
            reopen_count: Number of times reopened.
            reopened_by: User who reopened the incident.
            reopened_time: Reopened timestamp.
            resolved_at: Resolved timestamp.
            resolved_by: User who resolved the incident.
            rfc: RFC association.
            route_reason: Reason for routing.
            service_offering: Service offering association.
            severity: Severity of the incident.
            short_description: Short description of the incident.
            sla_due: SLA due date.
            state: State of the incident.
            subcategory: Subcategory of the incident.
            sys_class_name: Class name of the record.
            sys_created_by: User who created the record.
            sys_created_on: Creation timestamp.
            sys_domain: Domain of the record.
            sys_domain_path: Domain path.
            sys_id: System ID of the record.
            sys_mod_count: Modification count.
            sys_tags: System tags.
            sys_updated_by: User who last updated the record.
            sys_updated_on: Last updated timestamp.
            sysparm_display_value: Display values instead of keys.
            sysparm_exclude_reference_link: Exclude reference links in the response.
            sysparm_fields: Comma-separated list of fields to retrieve.
            sysparm_input_display_value: Use display values for input fields.
            sysparm_query_no_domain: Query without domain restrictions.
            sysparm_suppress_auto_sys_field: Suppress automatically generated sys fields.
            sysparm_view: Name of the view to use.
            task_effective_number: Effective task number.
            time_worked: Time worked on the incident.
            universal_request: Universal request association.
            upon_approval: Action upon approval.
            upon_reject: Action upon rejection.
            urgency: Urgency of the incident.
            user_input: User input data.
            watch_list: Watch list association.
            work_end: Work end timestamp.
            work_notes: Work notes.
            work_notes_list: List of work notes.
            work_start: Work start timestamp.
        Returns:
            API response as a dictionary.
        """
        ...

    def servicenow_update_system_property(
        self,
        sys_id: str,
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
        sys_package: Optional[_ServicenowUpdateSystemPropertySysPackage] = None,
        sys_policy: Optional[str] = None,
        sys_scope: Optional[_ServicenowUpdateSystemPropertySysScope] = None,
        sys_tags: Optional[str] = None,
        sys_update_name: Optional[str] = None,
        sys_updated_by: Optional[str] = None,
        sys_updated_on: Optional[str] = None,
        type: Optional[str] = None,
        value: Optional[str] = None,
        write_roles: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates one or more fields of an existing ServiceNow system property record identified by its unique sys_id using a PATCH request. Use this tool to change the value, description, or other attributes of a system property. Do not use this tool to create a new property — use servicenow_create_system_property instead. Changes take effect immediately and may impact system or application behavior.

        Args:
            sys_id: Unique identifier for the record. (required)
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

