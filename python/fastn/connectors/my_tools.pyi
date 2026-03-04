"""Fastn My Tools connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class MyToolsConnector:
    """My Tools connector ().

    Provides 3 tools.
    """

    def fastn_activation_flow_v1(
        self,
        authorization: Optional[str] = None,
        input: Optional[Dict[str, Any]] = None,
        x_fastn_space_connection_id: Optional[str] = None,
        x_fastn_space_id: Optional[str] = None,
        x_fastn_space_tenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Executes the activation flow for user accounts in the fastn connector, allowing for the initiation and completion of user registration and activation processes.

        Args:
            authorization: 
            input: Free form JSON
            x_fastn_space_connection_id: 
            x_fastn_space_id: 
            x_fastn_space_tenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def fastn_custom_auth_v1(
        self,
        input: Optional[Dict[str, Any]] = None,
        x_fastn_api_key: Optional[str] = None,
        x_fastn_space_connection_id: Optional[str] = None,
        x_fastn_space_id: Optional[str] = None,
        x_fastn_space_tenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Facilitates custom authentication procedures within the fastn connector, enabling the implementation of tailored user login and verification methods.

        Args:
            input: Free form JSON
            x_fastn_api_key: 
            x_fastn_space_connection_id: 
            x_fastn_space_id: 
            x_fastn_space_tenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

    def testflow_v1(
        self,
        authorization: Optional[str] = None,
        input: Optional[Dict[str, Any]] = None,
        x_fastn_space_connection_id: Optional[str] = None,
        x_fastn_space_id: Optional[str] = None,
        x_fastn_space_tenantid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Runs test workflows in the testflow connector, allowing for the evaluation and debugging of various processes in a controlled environment.

        Args:
            authorization: 
            input: Free form JSON
            x_fastn_space_connection_id: 
            x_fastn_space_id: 
            x_fastn_space_tenantid: 
        Returns:
            API response as a dictionary.
        """
        ...

