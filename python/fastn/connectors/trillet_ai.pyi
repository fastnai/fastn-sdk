"""Fastn Trillet AI connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TrilletAiConnector:
    """Trillet AI connector ().

    Provides 17 tools.
    """

    def create_call_agent(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Creates a new call agent within the specified communication connector for handling calls.

        Args:
            x_workspace_id: The ID of your workspace (can be set in header or body). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_folder(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Creates a new folder for organizing files within the respective file management connector.

        Args:
            x_workspace_id: The workspace ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_message_flow(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Creates a new message flow to facilitate communication through the messaging connector.

        Args:
            x_workspace_id: The ID of your Trillet AI workspace (passed as a header). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_omni_flow_agent(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Creates an omnichannel flow agent within the communication connector to manage customer interactions across various channels.

        Args:
            x_workspace_id: The ID of the workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_workspace(
        self,
        initials: str,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new workspace in the project management connector for team collaboration and task management.

        Args:
            initials: User's initials. (required)
            name: User's full name. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_call_agent(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Deletes an existing call agent from the communication connector, removing it from active duty.

        Args:
            x_workspace_id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_folder(
        self,
        folderId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified folder from the file management connector, permanently removing its contents.

        Args:
            folderId: The ID of the folder. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_workspace(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Deletes the specified workspace from the project management connector, including all associated data.

        Args:
            x_workspace_id: The ID of the workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_call_agent(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific call agent from the communication connector for review or modification.

        Args:
            x_workspace_id: The ID of the workspace (repeated for clarity). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_call_agents(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of all call agents from the communication connector, providing an overview of available resources.

        Args:
            x_workspace_id: The ID of the workspace to target (can be repeated from auth for clarity). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_conversations(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Retrieves conversations from the communication connector to review past interactions.

        Args:
            x_workspace_id: The ID of your Trillet AI workspace. (This is redundant with the auth field) (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_folders(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Retrieves the folders available in the file management connector for organizational reference.

        Args:
            x_workspace_id: The ID of the workspace to target. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_omni_flow_agents(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Retrieves a list of omnichannel flow agents from the communication connector for management purposes.

        Args:
            x_workspace_id: The ID of the workspace to target (can be specified here or in the auth section). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_workspace(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific workspace from the project management connector for oversight.

        Args:
            x_workspace_id: The ID of the workspace, specified in the header. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def initiate_outbound_call(
        self,
        x_workspace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Initiates an outbound call using the communication connector.

        Args:
            x_workspace_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def invite_team_member(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Invites a new team member to join the workspace within the project management connector, facilitating collaboration.

        Args:
            x_workspace_id: The ID of the workspace (provided in header). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def start_batch_calls(
        self,
        x_workspace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Starts a batch process to make multiple calls simultaneously through the communication connector.

        Args:
            x_workspace_id: 
        Returns:
            API response as a dictionary.
        """
        ...

