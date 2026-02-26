"""Fastn Odoo connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class OdooConnector:
    """Odoo connector ().

    Provides 3 tools.
    """

    def authenticate(
        self,
    ) -> Dict[str, Any]:
        """Authenticates a user in the system, verifying credentials and establishing a secure session.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_employees(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of employees from the organization, providing details such as names, roles, and contact information.

        Args:
            limit: 
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_skills(
        self,
        skillIds: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of skills available within the organization, including descriptions and classifications for each skill.

        Args:
            skillIds: 
        Returns:
            API response as a dictionary.
        """
        ...

