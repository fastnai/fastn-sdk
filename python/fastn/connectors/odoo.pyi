"""Fastn Odoo connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class OdooConnector:
    """Odoo connector ().

    Provides 3 tools.
    """

    def odoo_authenticate(
        self,
    ) -> Dict[str, Any]:
        """Authenticates a user against the Odoo instance by verifying credentials and establishing a secure session. Use this tool before making other Odoo API calls that require an authenticated session. Returns a session token or user ID upon success. Does not retrieve or modify business data directly.
        Returns:
            API response as a dictionary.
        """
        ...

    def odoo_list_employees(
        self,
        limit: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of employees from the Odoo HR module, including details such as names, job roles, and contact information. Use this tool to enumerate or browse employee records in the organization. Does not modify any data. Note: all Odoo API calls are made via JSON-RPC POST requests to the Odoo endpoint.

        Args:
            limit: 
            offset: 
        Returns:
            API response as a dictionary.
        """
        ...

    def odoo_list_skills(
        self,
        skillIds: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of skills configured in the Odoo HR module, including descriptions and classifications for each skill. Use this tool to browse available skills within the organization. Does not modify any data. Note: all Odoo API calls are made via JSON-RPC POST requests to the Odoo endpoint.

        Args:
            skillIds: 
        Returns:
            API response as a dictionary.
        """
        ...

