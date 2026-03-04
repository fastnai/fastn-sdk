"""Fastn Workable connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _WorkableCreateEmployeeEmployee(TypedDict, total=False):
    address: Dict[str, Any]
    bank_details_group: Dict[str, Any]
    birthdate: str
    chat_group: List[Any]
    citizenship: List[Any]
    contact_group: List[Any]
    country: str
    department: str
    education_group: List[Any]
    employment_group: List[Any]
    firstname: str
    gender: str
    hire_date: str
    job_title: str
    language: List[Any]
    lastname: str
    legal_entity: str
    marital_status_group: Dict[str, Any]
    national_identification_number_group: Dict[str, Any]
    nationality: str
    passport_group: List[Any]
    personal_email: List[Any]
    phone_group: List[Any]
    preferred_name: str
    reports_to: str
    salary_group: List[Any]
    skills: List[Any]
    social_group: List[Any]
    social_insurance_number_group: List[Any]
    social_security_number_group: Dict[str, Any]
    start_date: str
    tax_identification_number_group: Dict[str, Any]
    work_email: str
    work_experience_group: List[Any]
    work_schedule: str

class _WorkableCreateWebhookArgs(TypedDict, total=False):
    account_id: str
    job_shortcode: str
    stage_slug: str

class _WorkableUpdateEmployeeEmployee(TypedDict, total=False):
    address: Dict[str, Any]
    bank_details_group: Dict[str, Any]
    birthdate: str
    chat_group: List[Any]
    citizenship: List[Any]
    contact_group: List[Any]
    country: str
    department: str
    education_group: List[Any]
    employment_group: List[Any]
    firstname: str
    gender: str
    hire_date: str
    job_title: str
    language: List[Any]
    lastname: str
    legal_entity: str
    marital_status_group: Dict[str, Any]
    national_identification_number_group: Dict[str, Any]
    nationality: str
    passport_group: List[Any]
    personal_email: List[Any]
    phone_group: List[Any]
    preferred_name: str
    reports_to: str
    salary_group: List[Any]
    skills: List[Any]
    social_group: List[Any]
    social_insurance_number_group: List[Any]
    social_security_number_group: Dict[str, Any]
    start_date: str
    tax_identification_number_group: Dict[str, Any]
    work_email: str
    work_experience_group: List[Any]
    work_schedule: str

class WorkableConnector:
    """Workable connector ().

    Provides 13 tools.
    """

    def workable_create_department(
        self,
        name: str,
        parent_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new department in the Workable account. Use this when a new organizational unit needs to be added for grouping employees and job openings. Do not use this to modify an existing department — use workable_update_department instead.

        Args:
            name: Name of the Workable object. (required)
            parent_id: Parent ID for the Workable object.
        Returns:
            API response as a dictionary.
        """
        ...

    def workable_create_employee(
        self,
        employee: Optional[_WorkableCreateEmployeeEmployee] = None,
        member_id: Optional[str] = None,
        state: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new employee record in Workable for the configured subdomain account. Use this when onboarding a new hire and their profile does not yet exist in Workable. Do not use this to update an existing employee — use workable_update_employee instead. A new employee ID is generated upon successful creation.

        Args:
            employee: 
            member_id: 
            state: 
        Returns:
            API response as a dictionary.
        """
        ...

    def workable_create_webhook(
        self,
        args: _WorkableCreateWebhookArgs,
        event: str,
        target: str,
    ) -> Dict[str, Any]:
        """Creates a new Workable webhook subscription that sends HTTP event notifications to a specified URL when configured events occur (e.g., candidate stage changes, job postings). Use this when you need to receive real-time event callbacks from Workable. Do not use this if a subscription for the same endpoint and event type already exists, as duplicates may cause repeated deliveries.

        Args:
            args: Additional arguments for the Workable API request. (required)
            event: The type of event. (required)
            target: The target of the event. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def workable_delete_webhook(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes an existing Workable webhook subscription by its ID, stopping all future event deliveries for that subscription. Use this when a webhook endpoint is no longer needed or must be rotated. This action is irreversible — the subscription cannot be restored after deletion and must be recreated if needed again.

        Args:
            id: The ID of the resource to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def workable_get_employee(
        self,
        id: str,
        member_id: str,
    ) -> Dict[str, Any]:
        """Retrieves the full profile of a single Workable employee by their ID, including personal details, role, department, and employment status. Use this when you need complete information about one specific employee. Do not use this to list multiple employees — use workable_list_employees instead.

        Args:
            id:  (required)
            member_id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def workable_list_accounts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of Workable accounts accessible via the API. Use this to enumerate accounts when operating across multiple Workable tenants or to verify account availability. This is a top-level resource list and does not return employee, department, or member data.
        Returns:
            API response as a dictionary.
        """
        ...

    def workable_list_departments(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all departments defined in the Workable account. Use this to enumerate available departments, for example when populating department options or validating a department name before assigning an employee. Does not return individual employee records.
        Returns:
            API response as a dictionary.
        """
        ...

    def workable_list_employee_fields(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the list of all available employee profile fields defined in the Workable account, including standard and custom fields. Use this to discover which fields can be set or updated on employee records. Do not use this to retrieve employee data itself — use workable_get_employee or workable_list_employees instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def workable_list_employees(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all employees in the Workable account for the configured subdomain. Use this to get an overview of the full workforce or to search for employees by iterating results. For a single employees full details, use workable_get_employee instead.

        Args:
            limit: Limit for pagination.
            offset: Offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def workable_list_members(
        self,
        email: Optional[str] = None,
        limit: Optional[str] = None,
        max_id: Optional[str] = None,
        name: Optional[str] = None,
        role: Optional[str] = None,
        shortcode: Optional[str] = None,
        since_id: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of all members (Workable account users) in the configured subdomain, including their roles and access levels. Use this to audit account access or look up a members details. Members differ from employees — for employee records, use workable_list_employees.

        Args:
            email: Filter results by email.
            limit: Limit the number of results returned.
            max_id: Specify the maximum ID for pagination.
            name: Filter results by name.
            role: Filter results by role.
            shortcode: Filter results by shortcode.
            since_id: Specify the minimum ID for pagination.
            status: Filter results by status.
        Returns:
            API response as a dictionary.
        """
        ...

    def workable_list_recruiters(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all recruiters configured in the Workable account. Use this to identify available recruiters when assigning them to job openings or reviewing hiring team composition. Does not return members or employees — use workable_list_members or workable_list_employees for those.
        Returns:
            API response as a dictionary.
        """
        ...

    def workable_update_department(
        self,
        id: str,
        name: str,
    ) -> Dict[str, Any]:
        """Replaces the full details of an existing department in Workable with the data provided in the request body. Use this to rename a department or update its attributes. Do not use this to create a new department — use workable_create_department instead. This is a full replacement (PUT), so all required department fields must be included.

        Args:
            id: ID of the entity. (required)
            name: Name of the entity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def workable_update_employee(
        self,
        id: str,
        employee: Optional[_WorkableUpdateEmployeeEmployee] = None,
        state: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Partially updates an existing employee record in Workable by its ID, modifying only the fields provided in the request body. Use this to change employee details such as job title, department, or contact information. Do not use this to create a new employee — use workable_create_employee instead. Changes are applied immediately and overwrite existing field values.

        Args:
            id: ID of the resource. (required)
            employee: Details of the employee.
            state: State of the employee record.
        Returns:
            API response as a dictionary.
        """
        ...

