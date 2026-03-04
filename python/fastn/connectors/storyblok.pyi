"""Fastn Storyblok connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class _StoryblokCreateSpaceSpace(TypedDict, total=False):
    ai_translation_disabled: bool
    domain: str
    environments: List[Any]
    has_pending_tasks: bool
    name: str
    searchblok_id: int
    story_published_hook: str

class _StoryblokCreateStoryStory(TypedDict, total=False):
    content: Dict[str, Any]
    default_root: str
    disable_fe_editor: bool
    first_published_at: str
    group_id: str
    is_folder: bool
    is_startpage: bool
    meta_data: Dict[str, Any]
    name: str
    parent_id: int
    path: str
    pinned: bool
    position: int
    slug: str
    sort_by_date: str
    translated_slugs_attributes: List[Any]

class _StoryblokUpdateSpaceSpace(TypedDict, total=False):
    ai_translation_disabled: bool
    billing_address: Dict[str, Any]
    default_root: str
    domain: str
    environments: List[Any]
    has_pending_tasks: bool
    name: str
    options: Dict[str, Any]
    owner_id: int
    parent_id: int
    routes: List[Any]
    searchblok_id: int
    story_published_hook: str
    uniq_domain: str

class _StoryblokUpdateStoryStory(TypedDict, total=False):
    content: Dict[str, Any]
    default_root: str
    disable_fe_editor: bool
    first_published_at: str
    group_id: str
    is_folder: bool
    is_startpage: bool
    meta_data: Dict[str, Any]
    name: str
    parent_id: int
    path: str
    pinned: bool
    position: int
    release_id: int
    slug: str
    sort_by_date: str
    tag_list: List[Any]
    translated_slugs_attributes: List[Any]

class StoryblokConnector:
    """Storyblok connector ().

    Provides 10 tools.
    """

    def storyblok_create_space(
        self,
        space: _StoryblokCreateSpaceSpace,
    ) -> Dict[str, Any]:
        """Creates a new space in Storyblok under the authenticated account. Use this tool when you need to provision a new content project or environment in Storyblok, providing a name and any required configuration. Returns the newly created space object including its assigned space ID. Do not use this tool to modify an existing space — use storyblok_update_space instead. This action creates a persistent resource in Storyblok.

        Args:
            space: Information about a Storyblok space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def storyblok_create_story(
        self,
        sapceId: str,
        story: _StoryblokCreateStoryStory,
        publish: Optional[int] = None,
        release_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Creates a new story within a specified Storyblok space. Use this tool when you need to add a new content entry to a space, providing content fields, name, slug, and any other required story properties. Returns the newly created story object including its assigned ID. Do not use this tool to modify an existing story — use storyblok_update_story instead. This action creates a persistent record in Storyblok.

        Args:
            sapceId: The ID of your Storyblok space. (required)
            story: Details of the story to be created or updated. (required)
            publish: Publish status.
            release_id: ID of the release.
        Returns:
            API response as a dictionary.
        """
        ...

    def storyblok_delete_space(
        self,
        sapceId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specified Storyblok space by its space ID, removing the entire project including all its stories and associated content from the CMS. Use this tool only when a space must be fully and irreversibly removed. This action cannot be undone — all data within the space will be lost. Do not use this tool if you only want to update or reconfigure a space — use storyblok_update_space instead.

        Args:
            sapceId: The ID of the Storyblok space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def storyblok_delete_story(
        self,
        sapceId: str,
        storyId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific story from a Storyblok space by its story ID. Use this tool when a story must be fully removed from the CMS. This action is irreversible — the story and all its content cannot be recovered after deletion. Do not use this tool if you only want to unpublish or archive a story; use storyblok_update_story to change its status instead.

        Args:
            sapceId: The ID of the Storyblok space. (required)
            storyId: The ID of the Storyblok story. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def storyblok_get_space(
        self,
        sapceId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single Storyblok space by its space ID, including its name, domain, plan, and configuration settings. Use this tool when you need complete information about one specific space. Do not use this tool to list all available spaces — use storyblok_list_spaces instead. Does not modify any data.

        Args:
            sapceId: The ID of the Storyblok space. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def storyblok_get_story(
        self,
        sapceId: str,
        storyId: str,
    ) -> Dict[str, Any]:
        """Retrieves the full details of a single story in a Storyblok space by its story ID, including its content fields, slug, name, publish status, and metadata. Use this tool when you need complete information about one specific story. Do not use this tool to retrieve multiple stories at once — use storyblok_list_stories instead. Does not modify any data.

        Args:
            sapceId: The ID of the Storyblok space. (required)
            storyId: The ID of the Storyblok story. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def storyblok_list_spaces(
        self,
    ) -> Dict[str, Any]:
        """Lists all Storyblok spaces accessible to the authenticated account. Use this tool when you need an overview of all available spaces, for example to select a space ID for use in other operations. Returns a collection of space objects including their IDs, names, and basic configuration. Do not use this tool to retrieve the full details of a single space — use storyblok_get_space instead. Does not modify any data.
        Returns:
            API response as a dictionary.
        """
        ...

    def storyblok_list_stories(
        self,
        spaceId: str,
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
        """Lists all stories in a specific Storyblok space. Use this tool when you need to retrieve an overview of all content stories within a given space, for example to audit, display, or filter content entries. Returns a collection of story objects including their IDs, names, slugs, and status. Do not use this tool to retrieve the full details of a single story — use storyblok_get_story instead. Does not modify any data.

        Args:
            spaceId: Your Storyblok space ID. (required)
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

    def storyblok_update_space(
        self,
        sapceId: str,
        space: _StoryblokUpdateSpaceSpace,
    ) -> Dict[str, Any]:
        """Updates the settings or configuration of an existing Storyblok space by its space ID. Use this tool to modify space-level properties such as its name, domain, or other configurable parameters. Requires the space ID. Do not use this tool to modify individual stories within a space — use storyblok_update_story instead. Changes are applied immediately upon a successful response.

        Args:
            sapceId: The ID of the Storyblok space. (required)
            space: Space object with details. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def storyblok_update_story(
        self,
        sapceId: str,
        story: _StoryblokUpdateStoryStory,
        storyId: str,
        force_update: Optional[str] = None,
        lang: Optional[str] = None,
        publish: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Updates the content, settings, or metadata of an existing story in a Storyblok space by its story ID. Use this tool to modify story fields such as name, slug, content body, status (e.g. draft or published), or any other editable properties. Requires the space ID and story ID. Do not use this tool to create a new story — use storyblok_create_story instead. Modifies the story in place; changes take effect immediately upon success.

        Args:
            sapceId: The ID of the space containing the story. (required)
            story: Details of the Storyblok story. (required)
            storyId: The ID of the story. (required)
            force_update: Force update flag.
            lang: Language code.
            publish: Publish state.
        Returns:
            API response as a dictionary.
        """
        ...

