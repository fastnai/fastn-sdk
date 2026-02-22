"""Tests for the agent command and its core functions.

Tests tool conversion, action map building, schema unwrapping,
execute_tool_call, and the agent summary printer.
"""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import click
import pytest

from fastn.cli.agent_command import (
    _build_action_map,
    _convert_tools_for_openai,
    _detect_api_error,
    _estimate_cost,
    _execute_tool_call,
    _extract_tool_list,
    _format_bytes,
    _format_cost,
    _format_duration,
    _format_tokens,
    _parse_llm_json,
    _print_agent_summary,
    _AGENT_SYSTEM_PROMPT,
)


# ===================================================================
# _convert_tools_for_openai
# ===================================================================

class TestConvertToolsForOpenai:
    def test_basic_conversion(self):
        tool_list = [
            {
                "actionId": "act_slack_send",
                "function": {
                    "name": "send_message",
                    "description": "Send a message",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "body": {
                                "type": "object",
                                "properties": {
                                    "channel": {"type": "string"},
                                    "text": {"type": "string"},
                                },
                                "required": ["channel", "text"],
                            }
                        },
                    },
                },
            }
        ]
        result = _convert_tools_for_openai(tool_list)
        assert len(result) == 1
        assert result[0]["type"] == "function"
        fn = result[0]["function"]
        assert fn["name"] == "send_message"
        # Schema should be unwrapped — channel/text at top level, not under body
        params = fn["parameters"]
        assert "channel" in params.get("properties", {})
        assert "text" in params.get("properties", {})

    def test_tool_without_function_key(self):
        """Tools with inputSchema instead of function.parameters."""
        tool_list = [
            {
                "actionId": "act_test",
                "name": "test_tool",
                "description": "A test tool",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "value": {"type": "string"},
                    },
                },
            }
        ]
        result = _convert_tools_for_openai(tool_list)
        assert len(result) == 1
        assert result[0]["function"]["name"] == "test_tool"

    def test_multiple_tools(self):
        tool_list = [
            {
                "actionId": "act_1",
                "function": {
                    "name": "tool_a",
                    "description": "Tool A",
                    "parameters": {"type": "object", "properties": {}},
                },
            },
            {
                "actionId": "act_2",
                "function": {
                    "name": "tool_b",
                    "description": "Tool B",
                    "parameters": {"type": "object", "properties": {}},
                },
            },
        ]
        result = _convert_tools_for_openai(tool_list)
        assert len(result) == 2
        names = {r["function"]["name"] for r in result}
        assert names == {"tool_a", "tool_b"}

    def test_empty_tool_list(self):
        result = _convert_tools_for_openai([])
        assert result == []

    def test_already_flat_schema_unchanged(self):
        """Schema without wrapper key should remain flat."""
        tool_list = [
            {
                "actionId": "act_flat",
                "function": {
                    "name": "flat_tool",
                    "description": "Flat schema tool",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string"},
                            "limit": {"type": "integer"},
                        },
                        "required": ["query"],
                    },
                },
            }
        ]
        result = _convert_tools_for_openai(tool_list)
        params = result[0]["function"]["parameters"]
        assert "query" in params["properties"]
        assert "limit" in params["properties"]


# ===================================================================
# _build_action_map
# ===================================================================

class TestBuildActionMapExtended:
    def test_with_registry_resolution(self):
        tool_list = [
            {
                "actionId": "act_slack_send_message",
                "function": {
                    "name": "send_message_fn",
                    "description": "Send a message",
                    "parameters": {"type": "object", "properties": {}},
                },
            }
        ]
        registry = {
            "connectors": {
                "slack": {
                    "id": "conn_slack_001",
                    "display_name": "Slack",
                    "tools": {
                        "send_message": {
                            "actionId": "act_slack_send_message",
                            "name": "sendMessage",
                            "description": "Send a message",
                        },
                    },
                },
            },
        }
        action_map = _build_action_map(tool_list, registry)
        assert "send_message_fn" in action_map
        entry = action_map["send_message_fn"]
        assert entry["actionId"] == "act_slack_send_message"
        assert entry["connectorId"] == "conn_slack_001"

    def test_without_registry(self):
        tool_list = [
            {
                "actionId": "act_unknown",
                "function": {
                    "name": "unknown_tool",
                    "description": "Unknown",
                    "parameters": {},
                },
            }
        ]
        action_map = _build_action_map(tool_list, {"connectors": {}})
        assert "unknown_tool" in action_map
        assert action_map["unknown_tool"]["actionId"] == "act_unknown"

    def test_display_label_format(self):
        tool_list = [
            {
                "actionId": "act_slack_send_message",
                "function": {
                    "name": "send_message",
                    "description": "Send",
                    "parameters": {},
                },
            }
        ]
        registry = {
            "connectors": {
                "slack": {
                    "id": "conn_001",
                    "display_name": "Slack",
                    "tools": {
                        "send_message": {
                            "actionId": "act_slack_send_message",
                        },
                    },
                },
            },
        }
        action_map = _build_action_map(tool_list, registry)
        label = action_map["send_message"]["display_label"]
        assert "slack" in label.lower()


# ===================================================================
# _execute_tool_call
# ===================================================================

class TestExecuteToolCall:
    @patch("fastn.cli.agent_command._verbose_post")
    def test_successful_execution(self, mock_post):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"body": {"ok": True, "ts": "123"}}
        mock_resp.text = '{"body": {"ok": true}}'
        mock_post.return_value = mock_resp

        action_map = {
            "send_message": {
                "actionId": "act_slack_send",
                "connectorId": "conn_001",
                "display_label": "slack.send_message",
                "tool_info": {},
                "inputSchema": {},
            },
        }
        result = _execute_tool_call(
            "send_message", {"channel": "general", "text": "Hi"},
            action_map, {"Authorization": "Bearer test"},
            "ws_123", None, auto_confirm=True,
        )
        assert result.get("ok") is True
        assert result.get("_tool_duration") is not None or "ok" in result

    @patch("fastn.cli.agent_command._verbose_post")
    def test_api_error_status(self, mock_post):
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.json.return_value = {"error": "Server error"}
        mock_resp.text = "Server error"
        mock_post.return_value = mock_resp

        action_map = {
            "test_tool": {
                "actionId": "act_test",
                "connectorId": "",
                "display_label": "test_tool",
                "tool_info": {},
                "inputSchema": {},
            },
        }
        result = _execute_tool_call(
            "test_tool", {},
            action_map, {}, "ws_123", None, auto_confirm=True,
        )
        assert result["error"] is True
        assert result["status_code"] == 500

    @patch("fastn.cli.agent_command._verbose_post")
    def test_api_error_in_body(self, mock_post):
        """200 response but error in body (e.g., Slack channel_not_found)."""
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "body": {"ok": False, "error": "channel_not_found"}
        }
        mock_resp.text = '{"body": {"ok": false, "error": "channel_not_found"}}'
        mock_post.return_value = mock_resp

        action_map = {
            "send_message": {
                "actionId": "act_send",
                "connectorId": "",
                "display_label": "slack.send_message",
                "tool_info": {},
                "inputSchema": {},
            },
        }
        result = _execute_tool_call(
            "send_message", {"channel": "invalid"},
            action_map, {}, "ws_123", None, auto_confirm=True,
        )
        # Should detect the error
        assert result.get("error")

    def test_skipped_when_not_confirmed(self):
        """When auto_confirm is False and user declines, tool is skipped."""
        action_map = {
            "test": {
                "actionId": "act_test",
                "connectorId": "",
                "display_label": "test",
                "tool_info": {},
                "inputSchema": {},
            },
        }
        # Simulate user declining
        with patch("click.confirm", return_value=False):
            result = _execute_tool_call(
                "test", {},
                action_map, {}, "ws_123", None, auto_confirm=False,
            )
            assert result.get("skipped") is True

    @patch("fastn.cli.agent_command._verbose_post")
    def test_connection_id_passed(self, mock_post):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"body": {"ok": True}}
        mock_resp.text = '{"body": {"ok": true}}'
        mock_post.return_value = mock_resp

        action_map = {
            "test": {
                "actionId": "act_test",
                "connectorId": "conn_001",
                "display_label": "test",
                "tool_info": {},
                "inputSchema": {},
            },
        }
        _execute_tool_call(
            "test", {},
            action_map, {}, "ws_123", "conn_abc", auto_confirm=True,
        )
        payload = mock_post.call_args[0][2]
        assert payload["input"]["connectionId"] == "conn_abc"

    @patch("fastn.cli.agent_command._verbose_post")
    def test_large_response_truncated(self, mock_post):
        """Very large responses should be truncated for LLM context."""
        large_data = {"items": [{"id": i, "data": "x" * 100} for i in range(100)]}
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"body": large_data}
        mock_resp.text = json.dumps({"body": large_data})
        mock_post.return_value = mock_resp

        action_map = {
            "list_items": {
                "actionId": "act_list",
                "connectorId": "",
                "display_label": "list_items",
                "tool_info": {},
                "inputSchema": {},
            },
        }
        result = _execute_tool_call(
            "list_items", {},
            action_map, {}, "ws_123", None, auto_confirm=True,
        )
        # If result was truncated, it should have _truncated key
        result_str = json.dumps(large_data, indent=2)
        if len(result_str) > 4000:
            assert result.get("_truncated") is True

    @patch("fastn.cli.agent_command._verbose_post")
    def test_unknown_tool_uses_fn_name_as_action_id(self, mock_post):
        """If tool not in action_map, use fn_name as actionId."""
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"body": {"ok": True}}
        mock_resp.text = '{"body": {"ok": true}}'
        mock_post.return_value = mock_resp

        result = _execute_tool_call(
            "unknown_tool", {},
            {}, {}, "ws_123", None, auto_confirm=True,
        )
        payload = mock_post.call_args[0][2]
        assert payload["input"]["actionId"] == "unknown_tool"


# ===================================================================
# _print_agent_summary
# ===================================================================

class TestPrintAgentSummary:
    def test_no_calls(self, capsys):
        _print_agent_summary([], 100, 50, 0.5, 0.0, "gpt-4o")
        captured = capsys.readouterr()
        assert "No tool calls" in captured.out
        assert "Tokens:" in captured.out

    def test_single_call(self, capsys):
        call_log = [
            ("slack.send_message", 100, 50, 100, 0.25, 0.1, 500, 200, 200, "ok"),
        ]
        _print_agent_summary(call_log, 100, 50, 0.25, 0.1, "gpt-4o")
        captured = capsys.readouterr()
        assert "slack.send_message" in captured.out
        assert "Total" in captured.out

    def test_multiple_calls(self, capsys):
        call_log = [
            ("slack.list_channels", 80, 40, 80, 0.2, 0.1, 400, 1000, 1000, "ok"),
            ("slack.send_message", 120, 60, 200, 0.3, 0.15, 500, 200, 1200, "ok"),
        ]
        _print_agent_summary(call_log, 200, 100, 0.5, 0.25, "gpt-4o")
        captured = capsys.readouterr()
        assert "slack.list_channels" in captured.out
        assert "slack.send_message" in captured.out
        assert "Total" in captured.out

    def test_error_call_marked(self, capsys):
        call_log = [
            ("slack.send_message", 100, 50, 100, 0.25, 0.1, 500, 200, 200, "err"),
        ]
        _print_agent_summary(call_log, 100, 50, 0.25, 0.1, "gpt-4o")
        captured = capsys.readouterr()
        assert "✗" in captured.out  # Error mark

    def test_long_tool_name_truncated(self, capsys):
        call_log = [
            ("very_long_tool_name.very_long_action_name_that_exceeds_limit",
             100, 50, 100, 0.25, 0.1, 500, 200, 200, "ok"),
        ]
        _print_agent_summary(call_log, 100, 50, 0.25, 0.1, "gpt-4o")
        captured = capsys.readouterr()
        assert "..." in captured.out


# ===================================================================
# _AGENT_SYSTEM_PROMPT
# ===================================================================

class TestAgentSystemPrompt:
    def test_system_prompt_exists(self):
        assert len(_AGENT_SYSTEM_PROMPT) > 50
        assert "tool" in _AGENT_SYSTEM_PROMPT.lower()
        assert "recover" in _AGENT_SYSTEM_PROMPT.lower()


# ===================================================================
# _detect_api_error edge cases (supplementary)
# ===================================================================

class TestDetectApiErrorEdgeCases:
    def test_graphql_errors_array(self):
        result = {"errors": [{"message": "Field not found"}]}
        is_err, detail = _detect_api_error(result)
        assert is_err is True
        assert "Field not found" in detail

    def test_nested_stripe_error(self):
        result = {
            "error": {
                "type": "card_error",
                "message": "Your card was declined",
                "code": "card_declined",
            }
        }
        is_err, detail = _detect_api_error(result)
        assert is_err is True
        assert "declined" in detail.lower()

    def test_http_code_with_body_message(self):
        result = {
            "statusCode": 429,
            "message": "Rate limit exceeded",
        }
        is_err, detail = _detect_api_error(result)
        assert is_err is True
        assert "Rate limit exceeded" in detail

    def test_boolean_true_not_error(self):
        """ok: true should NOT be an error."""
        result = {"ok": True, "data": [1, 2, 3]}
        is_err, detail = _detect_api_error(result)
        assert is_err is False

    def test_status_timeout(self):
        result = {"status": "timeout", "message": "Request timed out"}
        is_err, detail = _detect_api_error(result)
        assert is_err is True

    def test_status_expired(self):
        result = {"status": "expired"}
        is_err, detail = _detect_api_error(result)
        assert is_err is True

    def test_code_permission_denied(self):
        result = {"code": "permission_denied", "message": "Access denied"}
        is_err, detail = _detect_api_error(result)
        assert is_err is True
        assert "Access denied" in detail

    def test_code_service_unavailable(self):
        result = {"code": "service_unavailable"}
        is_err, detail = _detect_api_error(result)
        assert is_err is True

    def test_http_status_code_underscore(self):
        result = {"status_code": 503, "detail": "Service unavailable"}
        is_err, detail = _detect_api_error(result)
        assert is_err is True

    def test_integer_result_not_error(self):
        is_err, detail = _detect_api_error(42)
        assert is_err is False

    def test_error_false_not_error(self):
        result = {"error": False, "data": "ok"}
        is_err, detail = _detect_api_error(result)
        assert is_err is False

    def test_empty_errors_list_not_error(self):
        result = {"errors": [], "data": {"id": 1}}
        is_err, detail = _detect_api_error(result)
        assert is_err is False
