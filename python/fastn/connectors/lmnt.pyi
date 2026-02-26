"""Fastn LMNT connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class LmntConnector:
    """LMNT connector ().

    Provides 6 tools.
    """

    def account_info(
        self,
    ) -> Dict[str, Any]:
        """Provides account information using the accountInfo connector, allowing users to access details related to their account and its usage.
        Returns:
            API response as a dictionary.
        """
        ...

    def delete_voice(
        self,
        voiceId: str,
    ) -> Dict[str, Any]:
        """Deletes a specified voice from the system using the deleteVoice connector, allowing for management of voice resources in the application.

        Args:
            voiceId: Voice ID for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def list_voices(
        self,
    ) -> Dict[str, Any]:
        """Lists all available voices for speech synthesis using the listVoices connector, enabling users to choose from different voice options for text-to-speech applications.
        Returns:
            API response as a dictionary.
        """
        ...

    def synthesize_speech(
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
        """Generates speech from text input using the synthesizeSpeech connector, allowing for text-to-speech conversion in various applications.

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

    def update_voice(
        self,
        description: str,
        gender: str,
        name: str,
        starred: bool,
        unfreeze: bool,
    ) -> Dict[str, Any]:
        """Updates the characteristics of a specific voice using the updateVoice connector, enabling customization of voice settings and attributes.

        Args:
            description: A description of the item. (required)
            gender: The gender of the user. (required)
            name: The name of the item. (required)
            starred: Indicates if the item is starred. (required)
            unfreeze: Indicates whether to unfreeze the item. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def voice_info(
        self,
        voiceId: str,
    ) -> Dict[str, Any]:
        """Retrieves information about the specifications and capabilities of a specific voice using the voiceInfo connector, useful for understanding voice attributes.

        Args:
            voiceId: Voice ID for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

