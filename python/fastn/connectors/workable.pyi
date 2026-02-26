"""Fastn Workable connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class WorkableConnector:
    """Workable connector ().

    Provides 13 tools.
    """

    def create_department(
        self,
        name: str,
        parent_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new department in the organization using the specified connector.

        Args:
            name: Name of the Workable object. (required)
            parent_id: Parent ID for the Workable object.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_employee(
        self,
        employee: Optional[Dict[str, Any]] = None,
        member_id: Optional[str] = None,
        state: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new employee record in the organization via the specified connector.

        Args:
            employee: 
            member_id: 
            state: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_webhook(
        self,
        args: Dict[str, Any],
        event: str,
        target: str,
    ) -> Dict[str, Any]:
        """Sets up a new webhook to capture events in the system using the connector.

        Args:
            args: Additional arguments for the Workable API request. (required)
            event: The type of event. (required)
            target: The target of the event. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_webhook(
        self,
        id: str,
    ) -> Dict[str, Any]:
        """Deletes an existing webhook from the system using the specified connector.

        Args:
            id: The ID of the resource to access. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_accounts(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of accounts in the system using the appropriate connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_departments(
        self,
    ) -> Dict[str, Any]:
        """Fetches the departments available in the organization's system using the connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employee(
        self,
        member_id: str,
    ) -> Dict[str, Any]:
        """Fetches the detailed information of a specific employee using the relevant connector.

        Args:
            member_id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employee_fields(
        self,
    ) -> Dict[str, Any]:
        """Gets the fields associated with an employee in the system using the connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employees(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the list of employees in the organization through the designated connector.

        Args:
            limit: Limit for pagination.
            offset: Offset for pagination.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_members(
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
        """Fetches the members associated with the connector and returns their details.

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

    def get_recruiters(
        self,
    ) -> Dict[str, Any]:
        """Obtains a list of recruiters present in the system through the relevant connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_department(
        self,
        id: str,
        name: str,
    ) -> Dict[str, Any]:
        """Updates the existing department information within the system via the connector.

        Args:
            id: ID of the entity. (required)
            name: Name of the entity. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_employee(
        self,
        employee: Optional[Dict[str, Any]] = None,
        state: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the existing employee information in the system using the appropriate connector.

        Args:
            employee: Details of the employee.
            state: State of the employee record.
        Returns:
            API response as a dictionary.
        """
        ...

