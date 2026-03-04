"""Fastn Trello connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _TrelloUpdateCardCover(TypedDict, total=False):
    brightness: str
    color: str
    size: str

class TrelloConnector:
    """Trello connector ().

    Provides 23 tools.
    """

    def get_boards_trello(
        self,
        baseUrl: str,
        boardId: str,
        card_fields: Optional[str] = None,
        cards: Optional[str] = None,
        fields: Optional[str] = None,
        filter: Optional[str] = None,
        key: Optional[str] = None,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves a list of boards from Trello, allowing users to view all projects and workflows associated with their account.

        Args:
            baseUrl: The base URL for the Trello API. (required)
            boardId: The ID of the Trello board. (required)
            card_fields: Specifies the card fields to retrieve.
            cards: Specifies the cards to retrieve.
            fields: Specifies the fields to retrieve.
            filter: Specifies the filter criteria for the request.
            key: Your Trello API key.
            token: Your Trello API token.
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_add_checklist_item(
        self,
        checklistId: Optional[str] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a new item to an existing checklist on a Trello card. Use this when you need to append a sub-task or step to a checklist that already exists on a card. Do not use this to create a new checklist — use trello_create_checklist instead. Requires the target checklist ID. This action modifies the checklist in place.

        Args:
            checklistId: 
            name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_add_comment_to_card(
        self,
        cardId: str,
        text: str,
    ) -> Dict[str, Any]:
        """Posts a new comment on a specific Trello card. Use this to add notes, updates, or communication related to a cards task. Do not use this to edit or delete existing comments. Requires the target card ID and the comment text. The comment is visible to all board members with access to the card.

        Args:
            cardId: The ID of the Trello card. (required)
            text: The text to be processed by the Trello V1 API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_create_board(
        self,
        name: str,
        defaultLabels: Optional[str] = None,
        defaultLists: Optional[str] = None,
        desc: Optional[str] = None,
        idBoardSource: Optional[str] = None,
        idOrganization: Optional[str] = None,
        keepFromSource: Optional[str] = None,
        powerUps: Optional[str] = None,
        prefs_background: Optional[str] = None,
        prefs_cardAging: Optional[str] = None,
        prefs_cardCovers: Optional[str] = None,
        prefs_comments: Optional[str] = None,
        prefs_invitations: Optional[str] = None,
        prefs_permissionLevel: Optional[str] = None,
        prefs_selfJoin: Optional[str] = None,
        prefs_voting: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new Trello board with a specified name and optional settings such as visibility and default lists. Use this to set up a new project workspace. Do not use this to update an existing board — use trello_update_board instead. Returns the newly created board object including its ID for subsequent operations.

        Args:
            name: Name of the new board. (required)
            defaultLabels: Default labels for the new board.
            defaultLists: Default lists for the new board.
            desc: Description of the new board.
            idBoardSource: ID of the source board if copying.
            idOrganization: ID of the organization to create the board in.
            keepFromSource: Data to keep from the source board (if copying).
            powerUps: Enabled Power-Ups for the new board.
            prefs_background: Preferences for the board background.
            prefs_cardAging: Preferences for card aging.
            prefs_cardCovers: Preferences for card covers.
            prefs_comments: Preferences for comments.
            prefs_invitations: Preferences for invitations.
            prefs_permissionLevel: Permission level for the board.
            prefs_selfJoin: Preferences for self-joining.
            prefs_voting: Preferences for voting.
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_create_card(
        self,
        idList: str,
        address: Optional[str] = None,
        coordinates: Optional[str] = None,
        desc: Optional[str] = None,
        due: Optional[str] = None,
        dueComplete: Optional[str] = None,
        fileSource: Optional[str] = None,
        idCardSource: Optional[str] = None,
        idLabels: Optional[str] = None,
        idMembers: Optional[str] = None,
        keepFromSource: Optional[str] = None,
        locationName: Optional[str] = None,
        mimeType: Optional[str] = None,
        name: Optional[str] = None,
        pos: Optional[str] = None,
        start: Optional[str] = None,
        urlSource: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new card in a specified Trello list, enabling task creation within a board. Use this to add a new task, issue, or item to a list. Do not use this to update an existing card — use trello_update_card instead. Requires the target list ID and a card name. Optionally accepts a description, due date, and member assignments.

        Args:
            idList: ID of the list the Trello card belongs to. (required)
            address: Address related to the Trello card.
            coordinates: Coordinates related to the Trello card.
            desc: Description of the Trello card.
            due: Due date of the Trello card.
            dueComplete: Due completion status of the Trello card.
            fileSource: Source of the file attached to the Trello card.
            idCardSource: ID of the source card for the Trello card.
            idLabels: IDs of labels associated with the Trello card.
            idMembers: IDs of members assigned to the Trello card.
            keepFromSource: Data to keep from the source for the Trello card.
            locationName: Name of the location associated with the Trello card.
            mimeType: MIME type of the file attached to the Trello card.
            name: Name of the Trello card.
            pos: Position of the Trello card within its list.
            start: Start date of the Trello card.
            urlSource: URL of the source for the Trello card.
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_create_checklist(
        self,
        cardId: Optional[str] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new checklist on a specific Trello card. Use this when you need to add a structured list of sub-tasks to a card. Do not use this to add items to an existing checklist — use trello_add_checklist_item instead. Requires the target card ID. This action modifies the card by attaching a new checklist.

        Args:
            cardId: 
            name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_create_list(
        self,
        idBoard: str,
        name: str,
        idListSource: Optional[str] = None,
        pos: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new list on a specified Trello board. Use this to add a new column or workflow stage to a board. Do not use this to update an existing list — use trello_update_list instead. Requires the board ID and a name for the new list. The list is created and immediately visible on the board.

        Args:
            idBoard: The ID of the Trello board where the list will be created. (required)
            name: The name of the new list. (required)
            idListSource: The ID of the source list (optional).
            pos: The position of the new list on the board (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_delete_board(
        self,
        boardId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific Trello board by its board ID, along with all of its lists, cards, checklists, and comments. Use this only when the entire board and all its contents should be removed. Do not use this to archive a board — use trello_update_board to close it instead. Requires the board ID. This action is irreversible and cannot be undone.

        Args:
            boardId: The ID of the Trello board. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_delete_card(
        self,
        cardId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific Trello card by its card ID, removing it from its list and board entirely. Use this when a task is no longer needed and should be fully removed. Do not use this if you only want to archive a card — use trello_update_card to set the card to closed instead. Requires the card ID. This action is irreversible; the card and all its data cannot be recovered.

        Args:
            cardId: The ID of the Trello card. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_delete_card_comment(
        self,
        actionId: str,
        cardId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific comment from a Trello card. Use this when you need to remove an outdated, incorrect, or unwanted comment from a card. Do not use this to edit a comment — use an update comment tool if available. Requires both the card ID and the action ID of the comment. This action is irreversible; the deleted comment cannot be recovered.

        Args:
            actionId: The ID of the Trello action. (required)
            cardId: The ID of the Trello card. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_get_board(
        self,
        boardId: str,
        actions: Optional[str] = None,
        boardStars: Optional[str] = None,
        card_pluginData: Optional[str] = None,
        cards: Optional[str] = None,
        checklists: Optional[str] = None,
        customFields: Optional[str] = None,
        fields: Optional[str] = None,
        labels: Optional[str] = None,
        lists: Optional[str] = None,
        members: Optional[str] = None,
        memberships: Optional[str] = None,
        myPrefs: Optional[str] = None,
        organization: Optional[str] = None,
        organization_pluginData: Optional[str] = None,
        pluginData: Optional[str] = None,
        tags: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single Trello board by its unique board ID, including its name, description, visibility, and settings. Use this when you need metadata for one specific board. Do not use this to retrieve all boards for the current user — use trello_list_member_boards instead. Requires the board ID.

        Args:
            boardId: ID of the Trello board. (required)
            actions: Trello actions data.
            boardStars: Data related to board stars.
            card_pluginData: Plugin data associated with Trello cards.
            cards: Trello cards data.
            checklists: Trello checklists data.
            customFields: Trello custom fields data.
            fields: Custom fields data.
            labels: Trello labels data.
            lists: Trello lists data.
            members: Trello members data.
            memberships: Trello memberships data.
            myPrefs: User preferences data.
            organization: Trello organization data.
            organization_pluginData: Plugin data associated with Trello organizations.
            pluginData: Generic plugin data.
            tags: Trello tags data.
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_get_list(
        self,
        listId: str,
        fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single Trello list by its unique list ID, including its name, position, and associated board. Use this when you need metadata for one specific list. Do not use this to retrieve all lists on a board — use trello_list_board_lists instead. Requires the list ID.

        Args:
            listId: The ID of the Trello list. (required)
            fields: Comma-separated list of fields to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_invite_member_to_board(
        self,
        boardId: str,
        email: str,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Invites a member to join a specific Trello board, granting them access to collaborate on its lists and cards. Use this when adding a new collaborator to a board. Do not use this to update an existing members permissions — use trello_update_board instead. Requires the board ID and member details such as email or username.

        Args:
            boardId: ID of the Trello board. (required)
            email: User's email address. (required)
            type: Type of request.
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_list_board_cards(
        self,
        boardId: str,
    ) -> Dict[str, Any]:
        """Retrieves all cards across every list on a specific Trello board. Use this to get a complete view of all tasks on a board at once. Do not use this to retrieve cards from a single list only — use trello_list_list_cards instead. Requires the board ID. Returns a collection of card objects with their details.

        Args:
            boardId: The ID of the Trello board. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_list_board_lists(
        self,
        boardId: str,
        card_fields: Optional[str] = None,
        cards: Optional[str] = None,
        fields: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all lists associated with a specific Trello board. Use this to get a structured view of a boards columns or workflow stages. Do not use this to retrieve cards within those lists — use trello_list_list_cards or trello_list_board_cards instead. Requires the board ID. Returns a collection of list objects.

        Args:
            boardId: The ID of the Trello board. (required)
            card_fields: Specifies which card fields to retrieve.
            cards: Specifies which cards to retrieve.
            fields: Specifies which fields to retrieve.
            filter: Filter criteria for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_list_list_cards(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Retrieves all cards within a specific Trello list. Use this to get an overview of all tasks or items in a given list. Do not use this to retrieve cards across an entire board — use trello_list_board_cards instead. Requires the list ID. Returns a collection of card objects with their details.

        Args:
            listId: The ID of the Trello list. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_list_member_boards(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all Trello boards associated with the currently authenticated member. Use this to get an overview of all boards the current user belongs to. Do not use this to retrieve boards for a different member or to get lists and cards within a board — use trello_list_board_lists or trello_list_board_cards for that. Returns a collection of board objects.
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_remove_board_member(
        self,
        boardId: str,
        memberId: str,
    ) -> Dict[str, Any]:
        """Removes a member from a specific Trello board, revoking their access to the board and its contents. Use this when a collaborator should no longer have access to a board. Do not use this to remove a member from a card or organization — this only affects board-level membership. Requires both the board ID and the member ID. This action is reversible by re-inviting the member.

        Args:
            boardId: ID of the Trello board. (required)
            memberId: ID of the Trello member. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_search(
        self,
        query: str,
        board_fields: Optional[str] = None,
        board_organization: Optional[str] = None,
        boards_limit: Optional[str] = None,
        card_attachments: Optional[str] = None,
        card_board: Optional[str] = None,
        card_fields: Optional[str] = None,
        card_list: Optional[str] = None,
        card_members: Optional[str] = None,
        card_stickers: Optional[str] = None,
        cards_limit: Optional[str] = None,
        cards_page: Optional[str] = None,
        idBoards: Optional[str] = None,
        idCards: Optional[str] = None,
        idOrganizations: Optional[str] = None,
        member_fields: Optional[str] = None,
        members_limit: Optional[str] = None,
        modelTypes: Optional[str] = None,
        organization_fields: Optional[str] = None,
        organizations_limit: Optional[str] = None,
        partial: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Performs a full-text search across Trello, returning matching boards, cards, and members. Use this when you need to locate items by keyword without knowing their IDs. Do not use this to search exclusively for members — use trello_search_members for member-specific searches. Returns categorized results across all accessible Trello entities.

        Args:
            query: Search query for filtering results. (required)
            board_fields: Comma-separated list of board fields to retrieve.
            board_organization: Organization ID to filter boards.
            boards_limit: Maximum number of boards to retrieve.
            card_attachments: Specifies whether to include card attachments.
            card_board: Board ID to filter cards.
            card_fields: Comma-separated list of card fields to retrieve.
            card_list: List ID to filter cards.
            card_members: Specifies whether to include card members.
            card_stickers: Specifies whether to include card stickers.
            cards_limit: Maximum number of cards to retrieve.
            cards_page: Page number for card retrieval.
            idBoards: Comma-separated list of board IDs.
            idCards: Comma-separated list of card IDs.
            idOrganizations: Comma-separated list of organization IDs.
            member_fields: Comma-separated list of member fields to retrieve.
            members_limit: Maximum number of members to retrieve.
            modelTypes: Comma-separated list of model types to retrieve.
            organization_fields: Comma-separated list of organization fields to retrieve.
            organizations_limit: Maximum number of organizations to retrieve.
            partial: Specifies whether to retrieve partial data.
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_search_members(
        self,
        query: str,
        idBoard: Optional[str] = None,
        idOrganization: Optional[str] = None,
        limit: Optional[str] = None,
        onlyOrgMembers: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for Trello members by name or username. Use this to find a members ID or profile before inviting them to a board or assigning them to a card. Do not use this for a general Trello-wide search across boards and cards — use trello_search instead. Returns a list of matching member objects.

        Args:
            query: Search query for Trello entities. (required)
            idBoard: ID of the Trello board.
            idOrganization: ID of the Trello organization.
            limit: Limit the number of results returned.
            onlyOrgMembers: Filter results to only include organization members.
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_update_board(
        self,
        boardId: str,
        closed: Optional[str] = None,
        desc: Optional[str] = None,
        idOrganization: Optional[str] = None,
        labelNamesblue: Optional[str] = None,
        labelNamesgreen: Optional[str] = None,
        labelNamesorange: Optional[str] = None,
        labelNamespurple: Optional[str] = None,
        labelNamesred: Optional[str] = None,
        labelNamesyellow: Optional[str] = None,
        name: Optional[str] = None,
        prefsbackground: Optional[str] = None,
        prefscalendarFeedEnabled: Optional[str] = None,
        prefscardAging: Optional[str] = None,
        prefscardCovers: Optional[str] = None,
        prefscomments: Optional[str] = None,
        prefshideVotes: Optional[str] = None,
        prefsinvitations: Optional[str] = None,
        prefspermissionLevel: Optional[str] = None,
        prefsselfJoin: Optional[str] = None,
        prefsvoting: Optional[str] = None,
        subscribed: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates the properties of an existing Trello board, such as its name, description, visibility, or member permissions. Use this to modify board settings or close a board without deleting it. Do not use this to delete a board — use trello_delete_board instead. Requires the board ID. Changes are applied immediately.

        Args:
            boardId: The ID of the Trello board. (required)
            closed: Indicates if the board is closed (true) or open (false).
            desc: A description of the Trello board.
            idOrganization: The ID of the organization this board belongs to.
            labelNamesblue: Name for blue labels on the board.
            labelNamesgreen: Name for green labels on the board.
            labelNamesorange: Name for orange labels on the board.
            labelNamespurple: Name for purple labels on the board.
            labelNamesred: Name for red labels on the board.
            labelNamesyellow: Name for yellow labels on the board.
            name: The name of the Trello board.
            prefsbackground: Preferences related to the board's background.
            prefscalendarFeedEnabled: Indicates if the calendar feed is enabled (true) or disabled (false).
            prefscardAging: Preferences related to card aging.
            prefscardCovers: Preferences related to card covers.
            prefscomments: Preferences related to comments.
            prefshideVotes: Preferences related to hiding votes.
            prefsinvitations: Preferences related to invitations.
            prefspermissionLevel: Preferences related to permission levels.
            prefsselfJoin: Preferences related to self-joining.
            prefsvoting: Preferences related to voting.
            subscribed: Indicates if the user is subscribed to the board (true) or not (false).
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_update_card(
        self,
        cardId: str,
        address: Optional[str] = None,
        closed: Optional[bool] = None,
        coordinates: Optional[str] = None,
        cover: Optional[_TrelloUpdateCardCover] = None,
        desc: Optional[str] = None,
        due: Optional[str] = None,
        dueComplete: Optional[bool] = None,
        idAttachmentCover: Optional[str] = None,
        idBoard: Optional[str] = None,
        idLabels: Optional[str] = None,
        idList: Optional[str] = None,
        idMembers: Optional[str] = None,
        locationName: Optional[str] = None,
        name: Optional[str] = None,
        pos: Optional[str] = None,
        start: Optional[str] = None,
        subscribed: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates the properties of an existing Trello card, such as its name, description, due date, list assignment, assigned members, or closed state. Use this to modify any card attribute or to move a card between lists. Do not use this to add comments — use trello_add_comment_to_card instead. Requires the card ID. Changes are applied immediately.

        Args:
            cardId: The unique identifier of the Trello card. (required)
            address: Location address associated with the card.
            closed: Whether the card is closed (archived) or open.
            coordinates: Geographical coordinates associated with the card.
            cover: Cover customization options for the card.
            desc: Description or details about the Trello card.
            due: Due date for the card, in ISO 8601 format.
            dueComplete: Whether the due date has been completed.
            idAttachmentCover: ID of the attachment to be used as cover.
            idBoard: ID of the board containing the card.
            idLabels: Comma-separated list of label IDs.
            idList: The ID of the list where the card will be placed.
            idMembers: Comma-separated list of member IDs assigned to the card.
            locationName: Name of the location related to the card.
            name: The name or title of the Trello card.
            pos: Position of the card in the list.
            start: Start date for the card, in ISO 8601 format.
            subscribed: Whether the current member is subscribed to the card.
        Returns:
            API response as a dictionary.
        """
        ...

    def trello_update_list(
        self,
        listId: str,
        closed: Optional[bool] = None,
        idBoard: Optional[str] = None,
        name: Optional[str] = None,
        pos: Optional[str] = None,
        subscribed: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """Updates the properties of an existing Trello list, such as its name, position, or closed state. Use this to rename or reorder a list within a board. Do not use this to create a new list — use trello_create_list instead. Requires the list ID. Changes are applied immediately to the board.

        Args:
            listId: The ID of the Trello list. (required)
            closed: Indicates if the card or entity is closed.
            idBoard: The ID of the Trello board.
            name: The name of the card or entity.
            pos: The position of the card within the list.
            subscribed: Whether to subscribe to updates.
        Returns:
            API response as a dictionary.
        """
        ...

