"""Fastn ElevenLabs connector — auto-generated type stubs.

Do not edit manually. Regenerate with `fastn connector sync`.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class ElevenlabsConnector:
    """ElevenLabs connector ().

    Provides 9 tools.
    """

    def elevenlabs_convert_text_to_voice(
        self,
        text: str,
        voice_description: str,
    ) -> Dict[str, Any]:
        """Generates one or more voice preview audio samples from a text input using ElevenLabs voice design (POST /v1/text-to-voice/create-previews). Use this when you want to preview what a generated voice sounds like before saving it permanently. To save a selected preview as a reusable voice, follow up with elevenlabs_save_voice_from_preview. Do not use this for standard text-to-speech with an existing voice ID — use elevenlabs_text_to_speech instead.

        Args:
            text: The text you want to convert to speech. (required)
            voice_description: Description or identifier specifying the desired voice. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elevenlabs_get_voice(
        self,
        voiceId: str,
    ) -> Dict[str, Any]:
        """Retrieves detailed information about a specific ElevenLabs voice by its voice ID (GET /v1/voices/{voiceId}), including attributes such as name, gender, language, and available settings. Use this when you need metadata about a single known voice before using it in text-to-speech operations. Do not use this to browse all available voices — use elevenlabs_list_voices instead. This is a read-only operation with no side effects.

        Args:
            voiceId: ID of the voice to be used for the request. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elevenlabs_list_voices(
        self,
    ) -> Dict[str, Any]:
        """Retrieves the full list of available voices from ElevenLabs (GET /v1/voices), including details such as voice name, ID, language, gender, and accent. Use this when you need to discover or present voice options before selecting one for text-to-speech generation. Do not use this to get detailed information about a single specific voice — use elevenlabs_get_voice instead. This is a read-only operation with no side effects.
        Returns:
            API response as a dictionary.
        """
        ...

    def elevenlabs_save_voice_from_preview(
        self,
        generated_voice_id: str,
        voice_description: str,
        voice_name: str,
    ) -> Dict[str, Any]:
        """Saves a previously generated voice preview as a permanent voice in ElevenLabs (POST /v1/text-to-voice/create-voice-from-preview). Use this after generating voice previews with elevenlabs_convert_text_to_voice when you want to persist a selected voice for future text-to-speech use. Do not use this to generate new previews — use elevenlabs_convert_text_to_voice first. This operation creates a new stored voice resource in your ElevenLabs account.

        Args:
            generated_voice_id: ID of the generated voice. (required)
            voice_description: Description of the voice. (required)
            voice_name: Name of the voice to be used for generation. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elevenlabs_text_to_sound_effects(
        self,
        text: str,
    ) -> Dict[str, Any]:
        """Generates a sound effect audio file from a text description using ElevenLabs sound generation (POST /v1/sound-generation). Use this when you need to create ambient sounds, effects, or audio textures described in natural language (e.g., rain on a window, forest birds). Do not use this to convert spoken text into speech — use elevenlabs_text_to_speech or its streaming variants instead.

        Args:
            text: The text you want ElevenLabs to synthesize into speech. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elevenlabs_text_to_speech(
        self,
        text: str,
        voiceId: str,
    ) -> Dict[str, Any]:
        """Converts a text input into a complete spoken audio file using a specified ElevenLabs voice (POST /v1/text-to-speech/{voiceId}). Use this when you need a full audio file returned at once for a given text and voice ID. Do not use this for real-time audio streaming — use elevenlabs_text_to_speech_stream instead. Do not use this if you also need timing/timestamp data — use elevenlabs_text_to_speech_with_timing instead.

        Args:
            text: The text you want ElevenLabs to convert to speech. (required)
            voiceId: The ID of the voice you want to use from ElevenLabs. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elevenlabs_text_to_speech_stream(
        self,
        text: str,
        voiceId: str,
    ) -> Dict[str, Any]:
        """Streams text-to-speech audio in real time for a specified voice without waiting for the full audio to be generated (POST /v1/text-to-speech/{voiceId}/stream). Use this when low-latency audio delivery is required, such as in live voice assistants or real-time applications. Do not use this if you need timestamp/timing metadata — use elevenlabs_text_to_speech_stream_with_timing instead. Do not use this if you need the complete audio file returned at once — use elevenlabs_text_to_speech instead.

        Args:
            text: The text you want ElevenLabs to synthesize into speech. (required)
            voiceId: The ID of the voice to use for speech synthesis. (required)
        Returns:
            API response as a dictionary.
        """
        ...

    def elevenlabs_text_to_speech_stream_with_timing(
        self,
        text: str,
        voiceId: str,
        enable_logging: Optional[str] = None,
        optimize_streaming_latency: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Streams text-to-speech audio in real time for a specified voice, with character-level timestamp data included in the response (POST /v1/text-to-speech/{voiceId}/stream/with-timestamps). Use this when you need both real-time audio streaming and precise timing metadata for lip-syncing, subtitles, or synchronized animation. Do not use this if you do not need timing data — use elevenlabs_text_to_speech_stream for lower-overhead streaming instead.

        Args:
            text: The text to be synthesized by the ElevenLabs API. (required)
            voiceId: The ID of the voice to be used for text synthesis. (required)
            enable_logging: Enable or disable request logging.
            optimize_streaming_latency: Optimize for reduced streaming latency.
        Returns:
            API response as a dictionary.
        """
        ...

    def elevenlabs_text_to_speech_with_timing(
        self,
        text: str,
        voiceId: str,
        model_id: Optional[str] = None,
        output_format: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Converts text to speech for a specified voice and returns the complete audio file along with character-level timestamp metadata (POST /v1/text-to-speech/{voiceId}/with-timestamps). Use this when you need the full audio output plus timing data for post-processing tasks such as subtitle generation or animation synchronization. Do not use this for real-time streaming — use elevenlabs_text_to_speech_stream_with_timing instead.

        Args:
            text: The text you want to convert to speech. (required)
            voiceId: The ID of the voice to use for text-to-speech synthesis. (required)
            model_id: The ID of the ElevenLabs voice model to use.
            output_format: Desired format for the audio output (e.g., mp3).
        Returns:
            API response as a dictionary.
        """
        ...

