"""Fastn Trello connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class TrelloConnector:
    """Trello connector ().

    Provides 23 tools.
    """

    def add_checklist_item(
        self,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds a new item to an existing checklist in the Trello connector, allowing for more detailed task management.

        Args:
            name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def add_comment_to_card(
        self,
        text: str,
    ) -> Dict[str, Any]:
        """Adds a comment to a specific card in the Trello connector, facilitating communication and updates among team members.

        Args:
            text: The text to be processed by the Trello V1 API. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_board(
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
        """Creates a new board in the Trello connector with specified parameters such as title and visibility settings.

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

    def create_card(
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
        """Creates a new card in the Trello connector on a specified board, enabling task management within the specified list.

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

    def create_checklist(
        self,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new checklist within a card in the Trello connector, enabling detailed tracking of tasks associated with that card.

        Args:
            name: 
        Returns:
            API response as a dictionary.
        """
        ...

    def create_list(
        self,
        idBoard: str,
        name: str,
        idListSource: Optional[str] = None,
        pos: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new list within a board in the Trello connector, allowing organization of cards into distinct categories.

        Args:
            idBoard: The ID of the Trello board where the list will be created. (required)
            name: The name of the new list. (required)
            idListSource: The ID of the source list (optional).
            pos: The position of the new list on the board (optional).
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_board(
        self,
        boardId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified board in the Trello connector, permanently removing it along with all its contents.

        Args:
            boardId: The ID of the Trello board. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_card(
        self,
        cardId: str,
    ) -> Dict[str, Any]:
        """Removes a specific card from a board in the Trello connector, eliminating it from task management.

        Args:
            cardId: The ID of the Trello card. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_card_comment(
        self,
        actionId: str,
        cardId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific comment from a card in the Trello connector, removing unwanted or outdated information.

        Args:
            actionId: The ID of the Trello action. (required)
            cardId: The ID of the Trello card. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_board(
        self,
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
        """Fetches details of a specific board from the Trello connector using the board's unique identifier.

        Args:
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

    def get_board_lists(
        self,
        card_fields: Optional[str] = None,
        cards: Optional[str] = None,
        fields: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches all lists associated with a specific board from the Trello connector, providing a structured view of the board's organization.

        Args:
            card_fields: Specifies which card fields to retrieve.
            cards: Specifies which cards to retrieve.
            fields: Specifies which fields to retrieve.
            filter: Filter criteria for the request.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_boards(
        self,
        card_fields: Optional[str] = None,
        cards: Optional[str] = None,
        fields: Optional[str] = None,
        filter: Optional[str] = None,
        key: Optional[str] = None,
        token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves all boards from the Trello connector, providing a list of boards associated with your account.

        Args:
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

    def get_cards_of_board(
        self,
        boardId: str,
    ) -> Dict[str, Any]:
        """Retrieves all cards associated with a specific board from the Trello connector, allowing you to view the tasks within that board.

        Args:
            boardId: The ID of the Trello board. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_list(
        self,
        fields: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific list from the Trello connector using the list's unique identifier.

        Args:
            fields: Comma-separated list of fields to return.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_list_cards(
        self,
        listId: str,
    ) -> Dict[str, Any]:
        """Retrieves all cards within a specific list from the Trello connector, allowing you to see tasks associated with that category.

        Args:
            listId: The ID of the Trello list. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_members_boards(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all boards associated with a specific member in the Trello connector, allowing you to see their collaborative spaces.
        Returns:
            API response as a dictionary.
        """
        ...

    def invite_member_to_board(
        self,
        email: str,
        type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Invites a member to join a board in the Trello connector, allowing for collaboration and task sharing.

        Args:
            email: User's email address. (required)
            type: Type of request.
        Returns:
            API response as a dictionary.
        """
        ...

    def remove_board_member(
        self,
        boardId: str,
        memberId: str,
    ) -> Dict[str, Any]:
        """Removes a member from a board in the Trello connector, restricting their access to the board's contents.

        Args:
            boardId: ID of the Trello board. (required)
            memberId: ID of the Trello member. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def search_members(
        self,
        query: str,
        idBoard: Optional[str] = None,
        idOrganization: Optional[str] = None,
        limit: Optional[str] = None,
        onlyOrgMembers: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Searches for members in the Trello connector, enabling you to find collaborators by name or email.

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

    def search_trello(
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
        """Searches for specific items within Trello using the searchTrello tool, helping you find boards, cards, or members quickly.

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

    def update_board(
        self,
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
        """Updates the properties of an existing board in the Trello connector, allowing adjustments to titles, descriptions, or member permissions.

        Args:
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

    def update_card(
        self,
        address: Optional[str] = None,
        closed: Optional[str] = None,
        coordinates: Optional[str] = None,
        cover: Optional[str] = None,
        desc: Optional[str] = None,
        due: Optional[str] = None,
        dueComplete: Optional[str] = None,
        idAttachmentCover: Optional[str] = None,
        idBoard: Optional[str] = None,
        idLabels: Optional[str] = None,
        idList: Optional[str] = None,
        idMembers: Optional[str] = None,
        locationName: Optional[str] = None,
        name: Optional[str] = None,
        pos: Optional[str] = None,
        start: Optional[str] = None,
        subscribed: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates details of an existing card in the Trello connector, such as status, title, or assigned members.

        Args:
            address: Address of the card location.
            closed: Indicates if the card is closed.
            coordinates: Coordinates of the card location.
            cover: ID of the image used as the card cover.
            desc: Description of the card.
            due: Due date for the card.
            dueComplete: Indicates if the due date is complete.
            idAttachmentCover: ID of the attachment used as the card cover.
            idBoard: ID of the board the card belongs to.
            idLabels: Comma-separated list of IDs for labels attached to the card.
            idList: ID of the list the card belongs to.
            idMembers: Comma-separated list of IDs for members assigned to the card.
            locationName: Name of the card location.
            name: Name of the Trello card.
            pos: Position of the card within the list.
            start: Start date for the card.
            subscribed: Indicates if the user is subscribed to the card.
        Returns:
            API response as a dictionary.
        """
        ...

    def update_list(
        self,
        closed: Optional[str] = None,
        idBoard: Optional[str] = None,
        name: Optional[str] = None,
        pos: Optional[str] = None,
        subscribed: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates properties of an existing list in the Trello connector, allowing for changes in title or position within the board.

        Args:
            closed: Indicates whether to include closed lists (true/false).
            idBoard: ID of the board to filter lists from.
            name: Name of the list to filter by.
            pos: Position of the list on the board.
            subscribed: Indicates whether the user is subscribed to the list (true/false).
        Returns:
            API response as a dictionary.
        """
        ...

