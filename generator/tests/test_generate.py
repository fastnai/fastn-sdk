"""Tests for the Fastn stub generator."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

import pytest

from generator.generate import (
    StubGenerator,
    generate_stubs,
    parse_connector,
    parse_registry,
    _sanitize_identifier,
    _to_camel_case,
    _to_pascal_case,
    _map_type,
)


SAMPLE_REGISTRY = {
    "version": "2025.02.14",
    "connectors": {
        "slack": {
            "display_name": "Slack",
            "category": "communication",
            "tools": {
                "send_message": {
                    "actionId": "act_slack_send_message",
                    "description": "Send a message to a Slack channel",
                    "params": {
                        "text": {
                            "type": "string",
                            "required": True,
                            "description": "Message text",
                        },
                        "channel": {
                            "type": "string",
                            "required": True,
                            "description": "Channel name",
                        },
                    },
                },
                "create_channel": {
                    "actionId": "act_slack_create_channel",
                    "description": "Create a new Slack channel",
                    "params": {
                        "name": {
                            "type": "string",
                            "required": True,
                            "description": "Channel name",
                        },
                        "is_private": {
                            "type": "boolean",
                            "required": False,
                            "description": "Private channel",
                        },
                    },
                },
            },
        },
        "jira": {
            "display_name": "Jira",
            "category": "project_management",
            "tools": {
                "create_issue": {
                    "actionId": "act_jira_create_issue",
                    "description": "Create a Jira issue",
                    "params": {
                        "summary": {
                            "type": "string",
                            "required": True,
                            "description": "Issue summary",
                        },
                        "project_key": {
                            "type": "string",
                            "required": True,
                            "description": "Project key",
                        },
                        "issue_type": {
                            "type": "string",
                            "required": False,
                            "description": "Issue type",
                        },
                    },
                },
            },
        },
    },
}


class TestHelpers:
    def test_sanitize_identifier(self) -> None:
        assert _sanitize_identifier("send_message") == "send_message"
        assert _sanitize_identifier("my-tool") == "my_tool"
        assert _sanitize_identifier("123abc") == "_123abc"
        assert _sanitize_identifier("hello world") == "hello_world"

    def test_to_camel_case(self) -> None:
        assert _to_camel_case("send_message") == "sendMessage"
        assert _to_camel_case("create_channel") == "createChannel"
        assert _to_camel_case("name") == "name"

    def test_to_pascal_case(self) -> None:
        assert _to_pascal_case("slack") == "Slack"
        assert _to_pascal_case("google_drive") == "GoogleDrive"

    def test_map_type_python(self) -> None:
        assert _map_type("string", "python") == "str"
        assert _map_type("integer", "python") == "int"
        assert _map_type("boolean", "python") == "bool"
        assert _map_type("array", "python") == "List[Any]"
        assert _map_type("unknown", "python") == "Any"

    def test_map_type_typescript(self) -> None:
        assert _map_type("string", "typescript") == "string"
        assert _map_type("integer", "typescript") == "number"
        assert _map_type("boolean", "typescript") == "boolean"
        assert _map_type("array", "typescript") == "any[]"
        assert _map_type("unknown", "typescript") == "any"


class TestParseRegistry:
    def test_parse_basic(self) -> None:
        parsed = parse_registry(SAMPLE_REGISTRY)
        assert parsed["version"] == "2025.02.14"
        assert len(parsed["connectors"]) == 2

    def test_connector_names(self) -> None:
        parsed = parse_registry(SAMPLE_REGISTRY)
        names = [c["name"] for c in parsed["connectors"]]
        assert "jira" in names
        assert "slack" in names

    def test_connector_class_names(self) -> None:
        parsed = parse_registry(SAMPLE_REGISTRY)
        for c in parsed["connectors"]:
            if c["name"] == "slack":
                assert c["class_name"] == "SlackConnector"
            elif c["name"] == "jira":
                assert c["class_name"] == "JiraConnector"

    def test_tool_params_sorted(self) -> None:
        parsed = parse_registry(SAMPLE_REGISTRY)
        slack = next(c for c in parsed["connectors"] if c["name"] == "slack")
        send_msg = next(t for t in slack["tools"] if t["name"] == "send_message")
        # Required params should come first
        required = [p for p in send_msg["params"] if p["required"]]
        optional = [p for p in send_msg["params"] if not p["required"]]
        assert all(p["required"] for p in send_msg["params"][:len(required)])

    def test_empty_registry(self) -> None:
        parsed = parse_registry({"version": "1", "connectors": {}})
        assert parsed["connectors"] == []


class TestParseConnector:
    def test_single_connector(self) -> None:
        connector_data = SAMPLE_REGISTRY["connectors"]["slack"]
        parsed = parse_connector("slack", connector_data)
        assert parsed["name"] == "slack"
        assert parsed["class_name"] == "SlackConnector"
        assert len(parsed["tools"]) == 2


class TestStubGenerator:
    def test_invalid_language(self) -> None:
        with pytest.raises(ValueError, match="Unsupported language"):
            StubGenerator(language="ruby")

    def test_generate_python_connector(self) -> None:
        gen = StubGenerator(language="python")
        parsed = parse_registry(SAMPLE_REGISTRY)
        slack = next(c for c in parsed["connectors"] if c["name"] == "slack")
        result = gen.generate_connector(slack)
        assert "class SlackConnector" in result
        assert "def send_message" in result
        assert "def create_channel" in result
        assert "channel: str" in result

    def test_generate_typescript_connector(self) -> None:
        gen = StubGenerator(language="typescript")
        parsed = parse_registry(SAMPLE_REGISTRY)
        slack = next(c for c in parsed["connectors"] if c["name"] == "slack")
        result = gen.generate_connector(slack)
        assert "class SlackConnector" in result
        assert "sendMessage" in result
        assert "createChannel" in result

    def test_generate_python_index(self) -> None:
        gen = StubGenerator(language="python")
        parsed = parse_registry(SAMPLE_REGISTRY)
        result = gen.generate_index(parsed["connectors"], ["slack"])
        assert "class Fastn" in result
        assert "class AsyncFastn" in result
        assert "slack" in result
        assert "from .connectors.slack import SlackConnector" in result

    def test_generate_typescript_index(self) -> None:
        gen = StubGenerator(language="typescript")
        parsed = parse_registry(SAMPLE_REGISTRY)
        result = gen.generate_index(parsed["connectors"], ["slack"])
        assert "class Fastn" in result
        assert "slack" in result

    def test_generate_placeholder(self) -> None:
        gen = StubGenerator(language="python")
        parsed = parse_registry(SAMPLE_REGISTRY)
        non_installed = [c for c in parsed["connectors"] if c["name"] != "slack"]
        result = gen.generate_placeholder(non_installed)
        assert "class JiraConnector" in result
        assert "fastn add jira" in result

    def test_generate_all_python(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            files = generate_stubs(
                SAMPLE_REGISTRY,
                ["slack"],
                tmpdir,
                language="python",
            )
            assert any("index.pyi" in f for f in files)
            assert any("slack.pyi" in f for f in files)
            assert any("_placeholders.pyi" in f for f in files)

            # Verify content
            index_path = Path(tmpdir) / "index.pyi"
            assert index_path.exists()
            content = index_path.read_text()
            assert "SlackConnector" in content

    def test_generate_all_typescript(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            files = generate_stubs(
                SAMPLE_REGISTRY,
                ["slack"],
                tmpdir,
                language="typescript",
            )
            assert any("index.d.ts" in f for f in files)
            assert any("slack.d.ts" in f for f in files)
            assert any("_placeholders.d.ts" in f for f in files)

    def test_no_placeholders_when_all_installed(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            files = generate_stubs(
                SAMPLE_REGISTRY,
                ["slack", "jira"],
                tmpdir,
                language="python",
            )
            assert not any("_placeholders" in f for f in files)
