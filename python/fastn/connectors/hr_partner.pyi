"""Fastn HR Partner connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class HrPartnerConnector:
    """HR Partner connector ().

    Provides 10 tools.
    """

    def hr_partner_get_applicant(
        self,
        applicantEmail: str,
    ) -> Dict[str, Any]:
        """Retrieves full details for a single applicant in HR Partner identified by their email address. Use this when you need complete information about one specific candidate. To browse all applicants, use hr_partner_list_applicants instead. No data is modified by this call.

        Args:
            applicantEmail: Email address of the applicant. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hr_partner_get_company_details(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the company profile and configuration details from HR Partner. Use this to access company-level information such as name, address, and HR settings. Does not return employee or recruitment data — use the relevant employee or applicant tools for those. No data is modified by this call.
        Returns:
            API response as a dictionary.
        """
        ...

    def hr_partner_get_employee(
        self,
        employeeCode: str,
    ) -> Dict[str, Any]:
        """Retrieves full profile information for a single employee in HR Partner identified by their employee code. Use this when you need detailed data about one specific employee. To list all employees, use hr_partner_list_employees instead. No data is modified by this call.

        Args:
            employeeCode: Employee code to identify the employee in the HR Partner system. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hr_partner_get_job(
        self,
        jobID: str,
    ) -> Dict[str, Any]:
        """Retrieves full details for a single job posting in HR Partner identified by its job ID. Use this when you know the specific job ID and need complete information about that posting. To browse all jobs, use hr_partner_list_jobs instead. No data is modified by this call.

        Args:
            jobID: ID of the job. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def hr_partner_list_applicants(
        self,
    ) -> Dict[str, Any]:
        """Lists all recruitment applicants stored in HR Partner. Use this to get an overview of all candidates in the hiring pipeline. Does not return details for a single applicant — use hr_partner_get_applicant for that. No data is modified by this call.
        Returns:
            API response as a dictionary.
        """
        ...

    def hr_partner_list_employee_absences(
        self,
    ) -> Dict[str, Any]:
        """Lists all recorded employee absences in HR Partner. Use this to review absence history or track leave across the workforce. Does not return details for a single employees absences in isolation — filter results as needed. No data is modified by this call.
        Returns:
            API response as a dictionary.
        """
        ...

    def hr_partner_list_employee_birthdays(
        self,
    ) -> Dict[str, Any]:
        """Lists upcoming employee birthdays from HR Partner. Use this when planning birthday celebrations or generating birthday reports. Returns birthday dates across all employees. No data is modified by this call.
        Returns:
            API response as a dictionary.
        """
        ...

    def hr_partner_list_employee_skills(
        self,
        comments: Optional[str] = None,
        department: Optional[str] = None,
        employee: Optional[str] = None,
        skill_name: Optional[str] = None,
        skill_rating: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all skills recorded in HR Partner across employees. Use this to retrieve the full skills inventory. To filter by a single employee, use additional endpoint parameters or filtering. No data is modified by this call.

        Args:
            comments: 
            department: 
            employee: 
            skill_name: 
            skill_rating: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hr_partner_list_employees(
        self,
        can_logon: Optional[str] = None,
        department: Optional[str] = None,
        eligible_for_rehire: Optional[str] = None,
        employment_status: Optional[str] = None,
        gender_identity: Optional[str] = None,
        group: Optional[str] = None,
        is_active: Optional[str] = None,
        is_terminated: Optional[str] = None,
        location: Optional[str] = None,
        pay_point: Optional[str] = None,
        position: Optional[str] = None,
        reports_to: Optional[str] = None,
        search: Optional[str] = None,
        tag: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Lists all employees stored in HR Partner. Use this to get a full directory of employees. Does not return detailed information for a single employee — use hr_partner_get_employee for that. No data is modified by this call.

        Args:
            can_logon: 
            department: 
            eligible_for_rehire: 
            employment_status: 
            gender_identity: 
            group: 
            is_active: 
            is_terminated: 
            location: 
            pay_point: 
            position: 
            reports_to: 
            search: 
            tag: 
        Returns:
            API response as a dictionary.
        """
        ...

    def hr_partner_list_jobs(
        self,
    ) -> Dict[str, Any]:
        """Lists all available job postings in HR Partner. Use this when you need a full overview of open or active job listings. Does not return details for a single job — use hr_partner_get_job for that. No data is modified by this call.
        Returns:
            API response as a dictionary.
        """
        ...

