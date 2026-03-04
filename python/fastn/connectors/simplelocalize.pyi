"""Fastn SimpleLocalize connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class SimplelocalizeConnector:
    """SimpleLocalize connector ().

    Provides 10 tools.
    """

    def simplelocalize_add_translations(
        self,
        key: str,
        language: str,
        text: str,
        customerId: Optional[str] = None,
        namespace: Optional[str] = None,
        reviewStatus: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds or updates translation string values for specified translation keys in your SimpleLocalize project. Use this to supply translated content for existing keys across one or more languages. Do not use this to create new translation keys — use simplelocalize_create_translation_key first. This operation modifies translation data in place on the specified keys.

        Args:
            key: The key for the translation. (required)
            language: The language code for the translation (e.g., en, es, fr). (required)
            text: The text to be translated or localized. (required)
            customerId: The ID of the customer.
            namespace: The namespace for the translation.
            reviewStatus: The review status of the translation.
        Returns:
            API response as a dictionary.
        """
        ...

    def simplelocalize_create_language(
        self,
        key: str,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new language entry in your SimpleLocalize project. Use this when you want to add support for a new locale or language to your translation workspace. Do not use this to update an existing language — use simplelocalize_update_language instead. This operation creates a persistent language record in the project.

        Args:
            key: The key for the localization entry. (required)
            name: The name of the localization entry.
        Returns:
            API response as a dictionary.
        """
        ...

    def simplelocalize_create_translation_key(
        self,
        key: str,
        charactersLimit: Optional[int] = None,
        codeDescription: Optional[str] = None,
        description: Optional[str] = None,
        namespace: Optional[str] = None,
        tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new translation key in your SimpleLocalize project. Use this when you need to register a new string identifier that will later be translated into one or more languages. Do not use this to add translation values — use simplelocalize_add_translations after creating the key. Do not use this to update or delete existing keys. This operation creates a persistent key record in the project.

        Args:
            key: The unique identifier for the localization key. (required)
            charactersLimit: The maximum number of characters allowed for the translation.
            codeDescription: A code-based description of the localization key.
            description: A description of the localization key.
            namespace: The namespace associated with the localization key.
            tags: An array of tags associated with the localization key.
        Returns:
            API response as a dictionary.
        """
        ...

    def simplelocalize_delete_language(
        self,
        languageKey: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a language entry from your SimpleLocalize project, identified by its languageKey. Use this when you need to remove a language and all its associated translations from the project. This action is irreversible — deleted languages and their translation data cannot be recovered. Do not use this to simply disable or hide a language; use simplelocalize_update_language for modifications instead.

        Args:
            languageKey: The language key to specify the target language. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def simplelocalize_delete_translation_keys(
        self,
        key: str,
        namespace: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Permanently deletes one or more translation keys from your SimpleLocalize project, along with all associated translations across all languages. Use this when you need to remove obsolete or unused keys. This action is irreversible — deleted keys and their translations cannot be recovered. Do not use this to remove a single languages translation value; use simplelocalize_add_translations to update individual values instead.

        Args:
            key: The key of the translation. (required)
            namespace: The namespace of the translation.
        Returns:
            API response as a dictionary.
        """
        ...

    def simplelocalize_get_language(
        self,
        languageKey: str,
    ) -> Dict[str, Any]:
        """Retrieves the details of a single language from your SimpleLocalize project, identified by its languageKey. Use this when you need metadata about a specific language such as its name or configuration. Do not use this to retrieve all languages — use simplelocalize_list_languages for that. This is a read-only operation with no side effects.

        Args:
            languageKey: The language key for the requested translation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def simplelocalize_list_languages(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of all languages configured in your SimpleLocalize project. Use this to discover available locales, their language keys, and metadata. Do not use this to retrieve a single specific language — use simplelocalize_get_language for that. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def simplelocalize_list_translation_keys(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all translation keys defined in your SimpleLocalize project. Use this to browse or audit the full set of keys available for translation. Do not use this to retrieve the translated string values — use simplelocalize_list_translations for that. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def simplelocalize_list_translations(
        self,
        baseOnly: Optional[str] = None,
        customerId: Optional[str] = None,
        key: Optional[str] = None,
        language: Optional[str] = None,
        namespace: Optional[str] = None,
        page: Optional[str] = None,
        query: Optional[str] = None,
        reviewStatus: Optional[str] = None,
        size: Optional[str] = None,
        text: Optional[str] = None,
        textStatus: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Retrieves translation values for specific keys from your SimpleLocalize project. Use this to fetch the actual translated strings associated with one or more translation keys, optionally filtered by language. Do not use this to retrieve translation keys without their values — use simplelocalize_list_translation_keys for that. This is a read-only operation with no side effects.

        Args:
            baseOnly: Filter results to include only base translations.
            customerId: Specify a customer ID to filter results.
            key: Filter results by translation key.
            language: Specify the language code to filter results (e.g., en, es, fr).
            namespace: Filter results by namespace.
            page: Specify the page number for pagination.
            query: Search query for translations.
            reviewStatus: Filter by the review status of translations.
            size: Specify the number of results per page for pagination.
            text: Filter results by translation text.
            textStatus: Filter results by the status of the translation text.
        Returns:
            API response as a dictionary.
        """
        ...

    def simplelocalize_update_language(
        self,
        key: str,
        languageKey: str,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates metadata for an existing language in SimpleLocalize, such as its name or custom properties. Use this when you need to modify the configuration of a language that already exists in your project. Do not use this to create a new language (use simplelocalize_create_language) or to delete one (use simplelocalize_delete_language). Requires the languageKey of the target language. This operation overwrites the specified fields on the language record.

        Args:
            key: The key for the translation. (required)
            languageKey: The key representing the target language. (required)
            name: The name associated with the translation.
        Returns:
            API response as a dictionary.
        """
        ...

