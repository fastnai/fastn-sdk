"""Fastn HR Partner connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class HrPartnerConnector:
    """HR Partner connector ().

    Provides 10 tools.
    """

    def company_details(
        self,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a company in the specified system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_applicant(
        self,
        applicantEmail: str,
    ) -> Dict[str, Any]:
        """Retrieves information about a specific applicant from the provided database or system.

        Args:
            applicantEmail: Email address of the applicant. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_applicants(
        self,
    ) -> Dict[str, Any]:
        """Obtains a list of all applicants stored in the database, providing an overview of potential candidates.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employee(
        self,
        employeeCode: str,
    ) -> Dict[str, Any]:
        """Fetches information about a specific employee from the defined employee database.

        Args:
            employeeCode: Employee code to identify the employee in the HR Partner system. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employee_absences(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of recorded absences for an employee in the employee management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employee_birthdays(
        self,
    ) -> Dict[str, Any]:
        """Fetches upcoming employee birthdays from the HR database for planning celebrations.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employee_skills(
        self,
        comments: Optional[str] = None,
        department: Optional[str] = None,
        employee: Optional[str] = None,
        skill_name: Optional[str] = None,
        skill_rating: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of skills associated with a specific employee from the skills management system.

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

    def get_employees(
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
        """Obtains a comprehensive list of all employees from the provided employee database.

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

    def get_job(
        self,
        jobID: str,
    ) -> Dict[str, Any]:
        """Fetches details about a specific job listing within the job management system.

        Args:
            jobID: ID of the job. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_jobs(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a comprehensive list of all available job postings from the job management system.
        Returns:
            API response as a dictionary.
        """
        ...

