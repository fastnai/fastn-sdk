"""Fastn Trillet AI connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _TrilletAiCreateCallAgentTtsmodel(TypedDict, total=False):
    language: str
    name: str
    provider: str
    voiceId: str

class _TrilletAiCreateCallAgentSettings(TypedDict, total=False):
    speed: int
    temperature: int
    volume: int

class _TrilletAiCreateMessageFlowSettings(TypedDict, total=False):
    emailSettings: Dict[str, Any]
    responseSettings: Dict[str, Any]
    security: Dict[str, Any]

class _TrilletAiInitiateOutboundCallDynamicVariables(TypedDict, total=False):
    Zipcode: str
    address: str
    email: str
    firstName: str
    lastName: str
    phoneNumber: str

class _TrilletAiStartBatchCallsSmartcallbackconfig(TypedDict, total=False):
    enabled: bool
    gaps: List[Any]
    maxAttempts: int

class TrilletAiConnector:
    """Trillet AI connector ().

    Provides 17 tools.
    """

    def trillet_ai_create_call_agent(
        self,
        llmModel: str,
        name: str,
        ttsModel: _TrilletAiCreateCallAgentTtsmodel,
        x_workspace_id: str,
        _gapBetweenEachAttemptForSmartCallback: Optional[List[Any]] = None,
        _maxAttemptsForSmartCallback: Optional[float] = None,
        _phoneNumberIds: Optional[List[Any]] = None,
        settings: Optional[_TrilletAiCreateCallAgentSettings] = None,
        smartCallback: Optional[bool] = None,
        variables: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new call agent in Trillet AI configured to handle inbound or outbound voice calls according to specified parameters. Use this tool when you need to provision a new AI-powered agent for call handling. Do not use this tool to update an existing call agent or to initiate calls — use the outbound call tool for that. This action creates a persistent call agent resource.

        Args:
            llmModel: The large language model to use for generation. (required)
            name: A name for the generation. (required)
            ttsModel: Settings for the text-to-speech model. (required)
            x_workspace_id: The ID of your workspace (can be set in header or body). (required)
            _gapBetweenEachAttemptForSmartCallback: 
            _maxAttemptsForSmartCallback: 
            _phoneNumberIds: 
            settings: Settings to control the generation process.
            smartCallback: 
            variables: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_create_folder(
        self,
        color: str,
        flowType: str,
        icon: str,
        name: str,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Creates a new flow folder in Trillet AI for organizing flows and related assets. Use this tool when you need a new container to group and manage flows logically. Do not use this tool to list existing folders or to move flows between folders. This action creates a persistent folder resource.

        Args:
            color: The color of the object. (required)
            flowType: The type of flow. (required)
            icon: The icon of the object. (required)
            name: The name of the object. (required)
            x_workspace_id: The workspace ID. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_create_message_flow(
        self,
        agent: str,
        autopilot: bool,
        description: str,
        isActive: bool,
        name: str,
        settings: _TrilletAiCreateMessageFlowSettings,
        x_workspace_id: str,
        direction: Optional[str] = None,
        initiationMessage: Optional[str] = None,
        messageChannel: Optional[str] = None,
        prompt: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new message flow in Trillet AI that defines the sequence and logic of messages sent through a messaging channel. Use this tool when you need to set up a new automated messaging sequence or conversation script. Do not use this tool to update an existing message flow or to send individual messages. This action creates a persistent message flow resource.

        Args:
            agent: Unique identifier for the agent. (required)
            autopilot: Indicates whether the agent should operate in autopilot mode. (required)
            description: A description of the agent. (required)
            isActive: Indicates whether the agent is currently active. (required)
            name: The name of the agent. (required)
            settings: Various settings to customize the agent's behavior. (required)
            x_workspace_id: The ID of your Trillet AI workspace (passed as a header). (required)
            direction: The direction of communication for the agent (e.g., inbound, outbound).
            initiationMessage: The message sent when the agent is initiated.
            messageChannel: The communication channel used by the agent.
            prompt: The initial prompt for the agent.
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_create_omni_flow_agent(
        self,
        llmModel: str,
        name: str,
        x_workspace_id: str,
        settings: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new omnichannel flow agent in Trillet AI capable of managing customer interactions across multiple communication channels such as voice, SMS, and chat. Use this tool when you need to configure a new agent to handle omnichannel workflows. Do not use this tool to update an existing omni-flow agent or to list available agents. This action creates a persistent agent resource.

        Args:
            llmModel: The name of the large language model to use. (required)
            name: Name of the resource to be created. (required)
            x_workspace_id: The ID of the workspace. (required)
            settings: Optional settings for the resource.
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_create_workspace(
        self,
        initials: str,
        name: str,
    ) -> Dict[str, Any]:
        """Creates a new workspace in Trillet AI for team collaboration, agent management, and workflow organization. Use this tool when setting up a new isolated environment for a team or project. Do not use this tool to update an existing workspace or to invite members — use the invite tool after creation. This action creates a persistent workspace resource.

        Args:
            initials: User's initials. (required)
            name: User's full name. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_delete_call_agent(
        self,
        agentId: str,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a call agent identified by its agent ID from Trillet AI, removing it from all workflows and making it unavailable for future calls. Use this tool only when a call agent must be fully decommissioned. Do not use this tool if you only want to disable or update the agent. This action is irreversible — deleted call agents cannot be restored.

        Args:
            agentId: Identifier for the agent. (required)
            x_workspace_id:  (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_delete_folder(
        self,
        folderId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific flow folder identified by its folder ID in Trillet AI, including all flows or assets stored within it. Use this tool only when a folder and its entire contents must be removed. Do not use this tool if you only want to rename or move the folder. This action is irreversible — deleted folders and their contents cannot be recovered.

        Args:
            folderId: The ID of the folder. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_delete_workspace(
        self,
        workspaceID: str,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a Trillet AI workspace identified by its workspace ID, along with all associated data including members, agents, and configurations. Use this tool only when a workspace and all its contents must be fully removed. Do not use this tool if you only want to archive or deactivate a workspace. This action is irreversible — deleted workspaces and their data cannot be recovered.

        Args:
            workspaceID: The ID of the workspace (URL parameter). (required)
            x_workspace_id: The ID of the workspace. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_get_call_agent(
        self,
        agentId: str,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single call agent identified by its agent ID in Trillet AI, including configuration, status, and assigned settings. Use this tool when you need in-depth information about one specific call agent. Do not use this tool to list all agents or to modify agent settings. This is a read-only operation with no side effects.

        Args:
            agentId: The ID of the agent. (required)
            x_workspace_id: The ID of the workspace (repeated for clarity). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_get_workspace(
        self,
        workspaceId: str,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single Trillet AI workspace identified by its workspace ID, including its name, settings, and membership information. Use this tool when you need metadata about one specific workspace. Do not use this tool to list all workspaces or to modify workspace settings. This is a read-only operation with no side effects.

        Args:
            workspaceId: The ID of the workspace to target. (required)
            x_workspace_id: The ID of the workspace, specified in the header. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_initiate_outbound_call(
        self,
        call_agent_id: Optional[str] = None,
        callback_url: Optional[str] = None,
        dynamic_variables: Optional[_TrilletAiInitiateOutboundCallDynamicVariables] = None,
        metadata: Optional[Dict[str, Any]] = None,
        to: Optional[str] = None,
        x_workspace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Initiates a single outbound call to a specified phone number using a configured Trillet AI call agent. Use this tool when you need to programmatically place one outbound call, such as for follow-ups, alerts, or surveys. Do not use this tool for batch or bulk calling — use the start batch calls tool instead. This action immediately places a live call and cannot be cancelled once connected.

        Args:
            call_agent_id: 
            callback_url: 
            dynamic_variables: 
            metadata: 
            to: 
            x_workspace_id: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_invite_team_member(
        self,
        email: str,
        role: str,
        workspaceId: str,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Sends an invitation to a new team member to join a specific Trillet AI workspace. Use this tool when you need to add a collaborator to an existing workspace by their email or identifier. Do not use this tool to create a workspace or to manage existing member permissions. This action sends an invitation email and adds a pending member record to the workspace.

        Args:
            email: The email address. (required)
            role: The role. (required)
            workspaceId: The ID of the workspace. (required)
            x_workspace_id: The ID of the workspace (provided in header). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_list_call_agents(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Returns a list of all call agents configured in Trillet AI. Use this tool when you need an overview of all available call agents and their basic information. Do not use this tool to retrieve detailed information about a single call agent or to create, update, or delete agents. This is a read-only operation with no side effects.

        Args:
            x_workspace_id: The ID of the workspace to target (can be repeated from auth for clarity). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_list_conversations(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Returns a list of conversations recorded in Trillet AI. Use this tool when you need to review past or ongoing interactions across communication channels. Do not use this tool to retrieve a single conversation by ID or to send or modify messages. This is a read-only operation with no side effects.

        Args:
            x_workspace_id: The ID of your Trillet AI workspace. (This is redundant with the auth field) (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_list_folders(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Returns a list of all flow folders available in Trillet AI. Use this tool when you need to browse or enumerate existing folders for organizational or lookup purposes. Do not use this tool to retrieve folder contents or to create, update, or delete folders. This is a read-only operation with no side effects.

        Args:
            x_workspace_id: The ID of the workspace to target. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_list_omni_flow_agents(
        self,
        x_workspace_id: str,
    ) -> Dict[str, Any]:
        """Returns a list of all omnichannel flow agents configured in Trillet AI. Use this tool when you need an overview of available omni-flow agents across all channels. Do not use this tool to retrieve a single agents details or to create, update, or delete agents. This is a read-only operation with no side effects.

        Args:
            x_workspace_id: The ID of the workspace to target (can be specified here or in the auth section). (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trillet_ai_start_batch_calls(
        self,
        agentId: Optional[str] = None,
        csv_info: Optional[List[Any]] = None,
        smartCallbackConfig: Optional[_TrilletAiStartBatchCallsSmartcallbackconfig] = None,
        x_workspace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Starts a batch process that initiates multiple outbound calls simultaneously through Trillet AI. Use this tool when you need to trigger a high-volume calling campaign or notify multiple recipients at once. Do not use this tool for a single outbound call — use the initiate outbound call tool instead. This action immediately starts calls to all specified recipients and cannot be undone once launched.

        Args:
            agentId: 
            csv_info: 
            smartCallbackConfig: 
            x_workspace_id: 
        Returns:
            API response as a dictionary.
        """
        ...

