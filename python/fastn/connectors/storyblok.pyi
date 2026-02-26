"""Fastn Storyblok connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class StoryblokConnector:
    """Storyblok connector ().

    Provides 10 tools.
    """

    def create_space(
        self,
        space: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Creates a new space in the application using the Space Management connector.

        Args:
            space: Information about a Storyblok space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def create_story(
        self,
        story: Dict[str, Any],
        publish: Optional[int] = None,
        release_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new story within a space in the application using the Story Management connector.

        Args:
            story: Details of the story to be created or updated. (required)
            publish: Publish status.
            release_id: ID of the release.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_space(
        self,
        sapceId: str,
    ) -> Dict[str, Any]:
        """Removes a specific space from the application using the Space Management connector.

        Args:
            sapceId: The ID of the Storyblok space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_story(
        self,
        sapceId: str,
        storyId: str,
    ) -> Dict[str, Any]:
        """Deletes a specific story from the application using the Story Management connector.

        Args:
            sapceId: The ID of the Storyblok space. (required)
            storyId: The ID of the Storyblok story. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_space(
        self,
        sapceId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific space by its identifier in the application using the Space Management connector.

        Args:
            sapceId: The ID of the Storyblok space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_spaces(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all spaces from the application using the Space Management connector.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_stories(
        self,
        by_ids: Optional[str] = None,
        by_slugs: Optional[str] = None,
        by_uuids: Optional[str] = None,
        by_uuids_ordered: Optional[str] = None,
        contain_component: Optional[str] = None,
        excluding_ids: Optional[str] = None,
        excluding_slugs: Optional[str] = None,
        favourite: Optional[bool] = None,
        filter_querymy_fieldin: Optional[str] = None,
        folder_only: Optional[bool] = None,
        in_release: Optional[float] = None,
        in_trash: Optional[bool] = None,
        in_workflow_stages: Optional[str] = None,
        is_published: Optional[bool] = None,
        mine: Optional[str] = None,
        page: Optional[float] = None,
        pinned: Optional[bool] = None,
        reference_search: Optional[str] = None,
        scheduled_at_gt: Optional[str] = None,
        scheduled_at_lt: Optional[str] = None,
        search: Optional[str] = None,
        sort_by: Optional[str] = None,
        starts_with: Optional[str] = None,
        story_only: Optional[bool] = None,
        text_search: Optional[str] = None,
        with_parent: Optional[float] = None,
        with_slug: Optional[str] = None,
        with_summary: Optional[float] = None,
        with_tag: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetches a list of all stories within a space in the application using the Story Management connector.

        Args:
            by_ids: Comma-separated list of entry IDs.
            by_slugs: Comma-separated list of entry slugs.
            by_uuids: Comma-separated list of entry UUIDs.
            by_uuids_ordered: Comma-separated list of entry UUIDs (preserving order).
            contain_component: Filter for entries containing specific components.
            excluding_ids: Comma-separated list of entry IDs to exclude.
            excluding_slugs: Comma-separated list of entry slugs to exclude.
            favourite: Filter for favourite entries.
            filter_querymy_fieldin: Filter entries based on a custom field.
            folder_only: Retrieve only folders.
            in_release: Filter entries in a specific release.
            in_trash: Filter for entries in the trash.
            in_workflow_stages: Filter entries based on workflow stages.
            is_published: Filter for published entries.
            mine: Filter for entries belonging to the current user.
            page: Pagination page number.
            pinned: Filter for pinned entries.
            reference_search: Search for entries based on references.
            scheduled_at_gt: Filter entries scheduled after this date/time.
            scheduled_at_lt: Filter entries scheduled before this date/time.
            search: Full-text search query.
            sort_by: Field to sort entries by (e.g., 'created_at').
            starts_with: Filter entries whose names start with this value.
            story_only: Retrieve only story entries.
            text_search: Full-text search query.
            with_parent: Include parent entry data.
            with_slug: Filter entries with this slug.
            with_summary: Include summary data.
            with_tag: Filter entries with this tag.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_story(
        self,
        sapceId: str,
        storyId: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific story by its identifier in the application using the Story Management connector.

        Args:
            sapceId: The ID of the Storyblok space. (required)
            storyId: The ID of the Storyblok story. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_space(
        self,
        space: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Modifies the properties of an existing space in the application using the Space Management connector.

        Args:
            space: Space object with details. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def update_story(
        self,
        story: Dict[str, Any],
        force_update: Optional[str] = None,
        lang: Optional[str] = None,
        publish: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates the content of an existing story in the application using the Story Management connector.

        Args:
            story: Details of the Storyblok story. (required)
            force_update: Force update flag.
            lang: Language code.
            publish: Publish state.
        Returns:
            API response as a dictionary.
        """
        ...

