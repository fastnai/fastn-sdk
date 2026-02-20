"""Tests for authentication module."""

from __future__ import annotations

import pytest

from fastn.auth import build_headers, mask_key
from fastn.config import FastnConfig
from fastn.exceptions import ConfigError


class TestBuildHeaders:
    def test_valid_config(self) -> None:
        config = FastnConfig(
            api_key="test-key",
            project_id="test-project",
        )
        headers = build_headers(config)
        assert headers["x-fastn-api-key"] == "test-key"
        assert headers["x-fastn-space-id"] == "test-project"
        assert headers["realm"] == "fastn"

    def test_invalid_config(self) -> None:
        config = FastnConfig()
        with pytest.raises(ConfigError):
            build_headers(config)


class TestMaskKey:
    def test_long_key(self) -> None:
        masked = mask_key("7ce258be770ef0a0a898da350e6783ae9f65a842")
        assert masked.startswith("7ce258be")
        assert "\u2022" in masked
        assert len(masked) == 20  # 8 visible + 12 masked

    def test_short_key(self) -> None:
        assert mask_key("abc") == "abc"

    def test_exact_8(self) -> None:
        assert mask_key("12345678") == "12345678"
