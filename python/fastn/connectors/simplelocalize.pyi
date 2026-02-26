"""Fastn SimpleLocalize connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class SimplelocalizeConnector:
    """SimpleLocalize connector ().

    Provides 10 tools.
    """

    def add_translations(
        self,
        key: str,
        language: str,
        text: str,
        customerId: Optional[str] = None,
        namespace: Optional[str] = None,
        reviewStatus: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Adds translations to specified translation keys in the translation management system.

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

    def create_language(
        self,
        key: str,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Creates a new language entry in the translation management system.

        Args:
            key: The key for the localization entry. (required)
            name: The name of the localization entry.
        Returns:
            API response as a dictionary.
        """
        ...

    def create_translation_key(
        self,
        key: str,
        charactersLimit: Optional[int] = None,
        codeDescription: Optional[str] = None,
        description: Optional[str] = None,
        namespace: Optional[str] = None,
        tags: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """Creates a new translation key in the translation management system.

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

    def delete_language(
        self,
        languageKey: str,
    ) -> Dict[str, Any]:
        """Deletes a language entry from the translation management system.

        Args:
            languageKey: The language key to specify the target language. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_translation_keys(
        self,
        key: str,
        namespace: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Deletes specified translation keys from the translation management system.

        Args:
            key: The key of the translation. (required)
            namespace: The namespace of the translation.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_language(
        self,
        languageKey: str,
    ) -> Dict[str, Any]:
        """Retrieves details of a specific language from the translation management system.

        Args:
            languageKey: The language key for the requested translation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_languages(
        self,
    ) -> Dict[str, Any]:
        """Lists all languages available in the translation management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_translation_keys(
        self,
    ) -> Dict[str, Any]:
        """Retrieves all translation keys from the translation management system.
        Returns:
            API response as a dictionary.
        """
        ...

    def get_translations(
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
        """Fetches translations for specific keys from the translation management system.

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

    def update_language(
        self,
        key: str,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Updates information for an existing language in the translation management system.

        Args:
            key: The key for the translation. (required)
            name: The name associated with the translation.
        Returns:
            API response as a dictionary.
        """
        ...

