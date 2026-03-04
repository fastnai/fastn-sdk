"""Fastn Breathehr connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _BreathehrCreateEmployeeEmployee(TypedDict, total=False):
    company_join_date: str
    email: str
    first_name: str
    last_name: str

class BreathehrConnector:
    """Breathehr connector ().

    Provides 10 tools.
    """

    def breathehr_create_employee(
        self,
        employee: _BreathehrCreateEmployeeEmployee,
    ) -> Dict[str, Any]:
        """Creates a new employee record in BreatheHR with the provided personal and employment details such as name, role, and start date. Use this when onboarding a new employee who does not yet have a record in the HR system. Do not use this to update an existing employees information. A new employee profile is created immediately and will be visible in the HR system.

        Args:
            employee: Employee details for the Breathehr API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def breathehr_get_absence(
        self,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific absence record in BreatheHR using its unique identifier, including information such as absence type, dates, and status. Use this when you have a known absence ID and need full details for that record. Do not use this to list all absences for a department (use breathehr_list_absences instead) or all absences for an employee (use breathehr_list_employee_absences instead). This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def breathehr_get_employee(
        self,
        employeeId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed profile information for a specific employee in BreatheHR using their unique employee ID, including personal details, role, and employment status. Use this when you need full details for one known employee. Do not use this to list all employees (use breathehr_list_employees instead). This is a read-only operation with no side effects.

        Args:
            employeeId: The ID of the employee. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def breathehr_list_absences(
        self,
        departmentId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all recorded absences for employees within a specified department in BreatheHR. Use this to review absence history at the department level. Do not use this to retrieve absences for a single employee (use breathehr_list_employee_absences instead) or to fetch a single absence record (use breathehr_get_absence instead). This is a read-only operation with no side effects.

        Args:
            departmentId: ID of the department. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def breathehr_list_departments(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all departments configured in the BreatheHR system. Use this to discover available department IDs needed for department-scoped queries such as listing salaries or absences. Do not use this to retrieve employee records (use breathehr_list_employees instead). This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def breathehr_list_employee_absences(
        self,
        employeeId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all absence records for a specific employee in BreatheHR using their unique employee ID. Use this to review the absence history of a particular employee. Do not use this to list absences across a whole department (use breathehr_list_absences instead) or to retrieve a single absence by ID (use breathehr_get_absence instead). This is a read-only operation with no side effects.

        Args:
            employeeId: ID of the employee. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def breathehr_list_employee_benefits(
        self,
        employeeId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of benefit records associated with a specific employee in BreatheHR using their unique employee ID. Use this to review perks and benefit entitlements for a particular employee. Do not use this to retrieve bonus information (use breathehr_list_employee_bonuses instead) or salary data (use breathehr_list_salaries instead). This is a read-only operation with no side effects.

        Args:
            employeeId: ID of the employee. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def breathehr_list_employee_bonuses(
        self,
        employeeId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of bonus records for a specific employee in BreatheHR using their unique employee ID. Use this to review all bonuses awarded to a particular employee. Do not use this to retrieve salary information (use breathehr_list_salaries instead) or benefits (use breathehr_list_employee_benefits instead). This is a read-only operation with no side effects.

        Args:
            employeeId: ID of the employee. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def breathehr_list_employees(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all employee records in the BreatheHR system, including basic profile information for each employee. Use this to get an overview of the workforce or to find employee IDs for use in other calls. Do not use this to retrieve detailed information for a single employee (use breathehr_get_employee instead). This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def breathehr_list_salaries(
        self,
        departmentId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of salary records for all employees within a specified department in BreatheHR. Use this to review compensation data for a department. Do not use this to retrieve bonuses (use breathehr_list_employee_bonuses instead) or benefits. This is a read-only operation with no side effects.

        Args:
            departmentId: ID of the department to access in Breathehr. (required)
        Returns:
            API response as a dictionary.
        """
        ...

