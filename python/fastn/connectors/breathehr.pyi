"""Fastn Breathehr connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class BreathehrConnector:
    """Breathehr connector ().

    Provides 10 tools.
    """

    def create_employee(
        self,
        employee: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new employee record in the HR system with provided personal and employment details.

        Args:
            employee: Employee details for the Breathehr API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_absence(
        self,
    ) -> Dict[str, Any]:
        """Fetches details of a specific absence using its unique identifier in the HR system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_absences(
        self,
        departmentId: str,
    ) -> Dict[str, Any]:
        """Fetches a list of all recorded absences in the HR system.

        Args:
            departmentId: ID of the department. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_depatments(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all departments in the HR system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employee(
        self,
        employeeId: str,
    ) -> Dict[str, Any]:
        """Fetches detailed information about a specific employee in the HR system using the employee's unique identifier.

        Args:
            employeeId: The ID of the employee. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employee_absences(
        self,
        employeeId: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of absences recorded for a specific employee in the HR system.

        Args:
            employeeId: ID of the employee. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employee_benefits(
        self,
        employeeId: str,
    ) -> Dict[str, Any]:
        """Fetches information about employee benefits associated with a specific employee in the HR system.

        Args:
            employeeId: ID of the employee. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employee_bonuses(
        self,
        employeeId: str,
    ) -> Dict[str, Any]:
        """Retrieves bonus information for a specific employee in the HR system.

        Args:
            employeeId: ID of the employee. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employees(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all employees in the HR system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_salaries(
        self,
        departmentId: str,
    ) -> Dict[str, Any]:
        """Retrieves salary information for all employees within the HR system.

        Args:
            departmentId: ID of the department to access in Breathehr. (required)
        Returns:
            API response as a dictionary.
        """
        ...

