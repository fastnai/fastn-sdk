"""Fastn mem0 connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class Mem0Connector:
    """mem0 connector ().

    Provides 5 tools.
    """

    def add_memories(
        self,
        agent_id: Optional[str] = None,
        app_id: Optional[str] = None,
        custom_categories: Optional[Dict[str, Any]] = None,
        excludes: Optional[str] = None,
        includes: Optional[str] = None,
        infer: Optional[bool] = None,
        messages: Optional[List[Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        org_id: Optional[str] = None,
        project_id: Optional[str] = None,
        run_id: Optional[str] = None,
        user_id: Optional[str] = None,
        version: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds new memories to the specified memory management system.

        Args:
            agent_id: 
            app_id: 
            custom_categories: 
            excludes: 
            includes: 
            infer: 
            messages: 
            metadata: 
            org_id: 
            project_id: 
            run_id: 
            user_id: 
            version: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_entities(
        self,
    ) -> Dict[str, Any]:
        """Obtains entities from the specified entity recognition system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_memories(
        self,
        filters: Optional[Dict[str, Any]] = None,
        org_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves existing memories from the specified memory management system.

        Args:
            filters: 
            org_id: 
            project_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def get_organizations(
        self,
    ) -> Dict[str, Any]:
        """Fetches a list of organizations from the specified organizational management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_projects(
        self,
        orgId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves project information from the specified project management system.

        Args:
            orgId: 
        Returns:
            API response as a dictionary.
        """
        ...

