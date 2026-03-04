"""Fastn mem0 connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _Mem0SearchMemoriesFilters(TypedDict, total=False):
    AND: List[Any]

class Mem0Connector:
    """mem0 connector ().

    Provides 5 tools.
    """

    def mem0_add_memories(
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
        """Stores one or more new memory entries in mem0 for a specific user, agent, or session. Use this to persist facts, preferences, or context that should be recalled in future interactions to enable personalized AI experiences. Use mem0_search_memories to retrieve previously stored memories. This action creates persistent records in mem0 and cannot be automatically undone.

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

    def mem0_list_entities(
        self,
    ) -> Dict[str, Any]:
        """Returns all entities (such as users or agents) registered in mem0. Use this to discover available entity identifiers that can be used to scope memory retrieval or storage operations. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def mem0_list_organizations(
        self,
    ) -> Dict[str, Any]:
        """Returns all organizations registered in mem0. Use this to discover available organization IDs for use with project or memory management operations. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def mem0_list_projects(
        self,
        orgId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Returns all projects belonging to a specific organization in mem0, identified by organization ID. Use this to discover projects associated with an org, or to retrieve project IDs for use with other project-specific tools. Does not modify any data.

        Args:
            orgId: 
        Returns:
            API response as a dictionary.
        """
        ...

    def mem0_search_memories(
        self,
        filters: Optional[_Mem0SearchMemoriesFilters] = None,
        org_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches and retrieves existing memories from mem0 using a POST request with a query payload. Use this to look up stored knowledge, facts, or context for a specific user, agent, or session to power personalized AI responses. Use mem0_add_memories to store new information. Note: despite using HTTP POST, this operation queries existing data and does not create new memories.

        Args:
            filters: 
            org_id: 
            project_id: 
        Returns:
            API response as a dictionary.
        """
        ...

