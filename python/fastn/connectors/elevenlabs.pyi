"""Fastn elevenlabs connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


class ElevenlabsConnector:
    """elevenlabs connector ().

    Provides 9 tools.
    """

    def convert_text_to_voice(
        self,
        text: str,
        voice_description: str,
    ) -> Dict[str, Any]:
        """Converts given text into voice output using the Convert Text to Voice connector, providing a straightforward way to generate audio from text inputs.

        Args:
            text: The text you want to convert to speech. (required)
            voice_description: Description or identifier specifying the desired voice. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_voice_by_id(
        self,
        voiceId: str,
    ) -> Dict[str, Any]:
        """Fetches details of a specific voice by its ID using the Get Voice By ID connector, providing users with information such as gender, language, and other attributes for customized text-to-speech.

        Args:
            voiceId: ID of the voice to be used for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def get_voices_(
        self,
    ) -> Dict[str, Any]:
        """Retrieves a list of available voice options using the Voices connector, enabling users to select from different voice styles and accents for their text-to-speech needs.
        Returns:
            API response as a dictionary.
        """
        ...

    def save_voice_from_preview(
        self,
        generated_voice_id: str,
        voice_description: str,
        voice_name: str,
    ) -> Dict[str, Any]:
        """Saves a voice preview as an audio file using the Save Voice from Preview connector, allowing users to store and access their text-to-speech outputs for future use.

        Args:
            generated_voice_id: ID of the generated voice. (required)
            voice_description: Description of the voice. (required)
            voice_name: Name of the voice to be used for generation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def text_to_sound_effects(
        self,
        text: str,
    ) -> Dict[str, Any]:
        """Applies sound effects to generated speech using the Text-to-Sound Effects connector, enhancing the auditory experience of the spoken text with additional audio elements.

        Args:
            text: The text you want ElevenLabs to synthesize into speech. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def text_to_speech(
        self,
        text: str,
    ) -> Dict[str, Any]:
        """Converts text into spoken words using the Text-to-Speech connector, allowing users to generate audio from written content.

        Args:
            text: The text you want ElevenLabs to convert to speech. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def text_to_speech_stream(
        self,
        text: str,
    ) -> Dict[str, Any]:
        """Streams spoken text directly as audio using the Text-to-Speech Stream connector, enabling real-time audio generation without waiting for the entire output to complete.

        Args:
            text: The text you want ElevenLabs to synthesize into speech. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def text_to_speech_stream_with_timing(
        self,
        enable_logging: Optional[str] = None,
        optimize_streaming_latency: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Streams spoken text with precise timing controls using the Text-to-Speech Stream with Timing connector, allowing for real-time audio delivery with specified timing adjustments.

        Args:
            enable_logging: Enable or disable request logging.
            optimize_streaming_latency: Optimize for reduced streaming latency.
        Returns:
            API response as a dictionary.
        """
        ...

    def text_to_speech_with_timing(
        self,
        output_format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Converts text into speech with precise timing control using the Text-to-Speech with Timing connector, allowing users to specify pauses and timing adjustments in their spoken output.

        Args:
            output_format: Desired format for the audio output (e.g., mp3).
        Returns:
            API response as a dictionary.
        """
        ...

