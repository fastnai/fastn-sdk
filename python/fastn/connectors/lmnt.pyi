"""Fastn LMNT connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class LmntConnector:
    """LMNT connector ().

    Provides 6 tools.
    """

    def lmnt_delete_voice(
        self,
        voiceId: str,
    ) -> Dict[str, Any]:
        """Permanently deletes a specific voice from the LMNT platform identified by its voice ID. Use this when a custom voice is no longer needed. This action is irreversible — the voice cannot be recovered after deletion. Do not use this to update a voice — use lmnt_update_voice instead.

        Args:
            voiceId: Voice ID for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def lmnt_get_account_info(
        self,
    ) -> Dict[str, Any]:
        """Retrieves information about the authenticated LMNT account, including usage statistics and account details. Use this when you need to check account status, remaining credits, or usage limits. Do not use this to retrieve information about a specific voice — use lmnt_get_voice_info instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def lmnt_get_voice_info(
        self,
        voiceId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed specifications and attributes of a specific LMNT voice identified by its voice ID, such as language, gender, and capability details. Use this when you need full details about one particular voice. Do not use this to list all available voices — use lmnt_list_voices instead.

        Args:
            voiceId: Voice ID for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def lmnt_list_voices(
        self,
    ) -> Dict[str, Any]:
        """Lists all voices available for speech synthesis on the LMNT platform. Use this when you need to discover which voices are available before generating speech or selecting a voice for text-to-speech. Returns a collection of voice records. Do not use this to retrieve details about a single voice — use lmnt_get_voice_info instead.
        Returns:
            API response as a dictionary.
        """
        ...

    def lmnt_synthesize_speech(
        self,
        conversational: Optional[str] = None,
        format: Optional[str] = None,
        language: Optional[str] = None,
        length: Optional[str] = None,
        model: Optional[str] = None,
        return_durations: Optional[str] = None,
        sample_rate: Optional[str] = None,
        seed: Optional[int] = None,
        speed: Optional[str] = None,
        text: Optional[str] = None,
        voice: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Generates an audio speech output from a text input using a specified LMNT voice. Use this when you need to convert text to spoken audio for playback or storage. Returns an audio file or stream. Do not use this to list available voices — use lmnt_list_voices first if you need to select a voice.

        Args:
            conversational: Flag indicating whether to use conversational speech.
            format: The audio format of the generated speech.
            language: The language of the generated speech.
            length: Length of generated speech.
            model: The speech synthesis model to use.
            return_durations: Flag to return phoneme durations.
            sample_rate: The sample rate of the generated audio.
            seed: Seed for random number generation (optional).
            speed: The speed of the generated speech.
            text: The text to be converted to speech.
            voice: The voice to use for speech synthesis.
        Returns:
            API response as a dictionary.
        """
        ...

    def lmnt_update_voice(
        self,
        description: str,
        gender: str,
        name: str,
        starred: bool,
        unfreeze: bool,
        voiceId: str,
    ) -> Dict[str, Any]:
        """Updates the characteristics and settings of a specific LMNT voice identified by its voice ID. Use this when you need to modify voice attributes such as name, description, or other configurable properties. This action overwrites the existing voice configuration. Do not use this to delete a voice — use lmnt_delete_voice instead.

        Args:
            description: A description of the item. (required)
            gender: The gender of the user. (required)
            name: The name of the item. (required)
            starred: Indicates if the item is starred. (required)
            unfreeze: Indicates whether to unfreeze the item. (required)
            voiceId: The ID of the voice. (required)
        Returns:
            API response as a dictionary.
        """
        ...

