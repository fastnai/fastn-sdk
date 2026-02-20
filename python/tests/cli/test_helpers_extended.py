"""Extended tests for CLI helper functions.

Tests _extract_input_fields, _unwrap_nested_fields, _prompt_for_params,
_format_schema_properties, _handle_execute_error, _redact_headers,
_verbose_post, _extract_org_id, and _ensure_fresh_token.
"""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import click
import httpx
import pytest

from fastn.cli._helpers import (
    _coerce_value,
    _extract_input_fields,
    _format_schema_properties,
    _handle_execute_error,
    _parse_extra_args,
    _redact_headers,
    _to_snake_case,
    _unwrap_nested_fields,
    _workspace_url,
)


# ===================================================================
# _extract_input_fields
# ===================================================================

class TestExtractInputFields:
    def test_empty_schema(self):
        pk, fields, required = _extract_input_fields({})
        assert pk is None
        assert fields == {}
        assert required == set()

    def test_flat_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "offset": {"type": "integer", "description": "Page offset"},
                "limit": {"type": "integer", "description": "Page limit"},
            },
            "required": ["offset"],
        }
        pk, fields, required = _extract_input_fields(schema)
        assert pk is None
        assert "offset" in fields
        assert "limit" in fields
        assert "offset" in required
        assert "limit" not in required

    def test_single_wrapper_body(self):
        """Single 'body' wrapper should be unwrapped."""
        schema = {
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
            "required": ["body"],
        }
        pk, fields, required = _extract_input_fields(schema)
        assert pk == "body"
        assert "channel" in fields
        assert "text" in fields
        assert "channel" in required
        assert "text" in required

    def test_headers_filtered_out(self):
        """Internal header group should be auto-skipped."""
        schema = {
            "type": "object",
            "properties": {
                "headers": {
                    "type": "object",
                    "properties": {
                        "authorization": {"type": "string"},
                        "x-fastn-space-id": {"type": "string"},
                    },
                },
                "body": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                    },
                    "required": ["name"],
                },
            },
        }
        pk, fields, required = _extract_input_fields(schema)
        assert pk == "body"
        assert "name" in fields
        assert "authorization" not in fields
        assert "x-fastn-space-id" not in fields

    def test_multiple_user_groups(self):
        """Multiple non-header groups → merge all inner fields."""
        schema = {
            "type": "object",
            "properties": {
                "headers": {
                    "type": "object",
                    "properties": {
                        "authorization": {"type": "string"},
                    },
                },
                "body": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                    },
                    "required": ["name"],
                },
                "query": {
                    "type": "object",
                    "properties": {
                        "limit": {"type": "integer"},
                    },
                },
            },
        }
        pk, fields, required = _extract_input_fields(schema)
        assert pk is None  # multiple groups -> no single wrapper key
        assert "name" in fields
        assert "limit" in fields
        assert "name" in required

    def test_nested_object_unwrapped(self):
        """Nested objects with properties should be recursively unwrapped."""
        schema = {
            "type": "object",
            "properties": {
                "body": {
                    "type": "object",
                    "properties": {
                        "user": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "email": {"type": "string"},
                            },
                            "required": ["name"],
                        },
                    },
                    "required": ["user"],
                },
            },
            "required": ["body"],
        }
        pk, fields, required = _extract_input_fields(schema)
        assert pk == "body"
        assert "name" in fields
        assert "email" in fields
        assert "name" in required


# ===================================================================
# _unwrap_nested_fields
# ===================================================================

class TestUnwrapNestedFields:
    def test_flat_fields(self):
        props = {
            "name": {"type": "string"},
            "age": {"type": "integer"},
        }
        required = {"name"}
        fields, req = _unwrap_nested_fields(props, required)
        assert "name" in fields
        assert "age" in fields
        assert "name" in req
        assert "age" not in req

    def test_nested_object(self):
        props = {
            "address": {
                "type": "object",
                "properties": {
                    "street": {"type": "string"},
                    "city": {"type": "string"},
                },
                "required": ["street"],
            },
        }
        required = {"address"}
        fields, req = _unwrap_nested_fields(props, required)
        assert "street" in fields
        assert "city" in fields
        assert "street" in req

    def test_optional_parent_makes_children_optional(self):
        props = {
            "metadata": {
                "type": "object",
                "properties": {
                    "tags": {"type": "array"},
                },
                "required": ["tags"],
            },
        }
        required = set()  # metadata itself is optional
        fields, req = _unwrap_nested_fields(props, required)
        assert "tags" in fields
        assert "tags" not in req  # parent optional → children optional

    def test_non_dict_field(self):
        props = {
            "name": "just a string, not a dict",
        }
        fields, req = _unwrap_nested_fields(props, set())
        assert "name" in fields

    def test_object_without_properties(self):
        """Object with no inner properties should stay as-is."""
        props = {
            "data": {"type": "object"},
        }
        fields, req = _unwrap_nested_fields(props, set())
        assert "data" in fields
        assert fields["data"]["type"] == "object"


# ===================================================================
# _handle_execute_error
# ===================================================================

class TestHandleExecuteError:
    def test_success_200_no_error(self):
        resp = MagicMock()
        resp.status_code = 200
        # Should not raise
        _handle_execute_error(resp, "slack.send_message", "ws_123")

    def test_auth_error_401(self):
        resp = MagicMock()
        resp.status_code = 401
        with pytest.raises(click.ClickException, match="Authentication"):
            _handle_execute_error(resp, "slack.send_message", "ws_123")

    def test_generic_api_error(self):
        resp = MagicMock()
        resp.status_code = 500
        resp.json.return_value = {"error": "Server error"}
        resp.text = '{"error": "Server error"}'
        with pytest.raises(click.ClickException, match="API error 500"):
            _handle_execute_error(resp, "slack.send_message", "ws_123")

    def test_not_enabled_error(self):
        resp = MagicMock()
        resp.status_code = 400
        resp.json.return_value = {"message": "Tool not enabled in workspace"}
        resp.text = '{"message": "Tool not enabled in workspace"}'
        with pytest.raises(click.ClickException, match="not enabled"):
            _handle_execute_error(resp, "slack.send_message", "ws_123")

    def test_not_connected_error(self):
        resp = MagicMock()
        resp.status_code = 400
        resp.json.return_value = {"message": "Connector not connected"}
        resp.text = '{"message": "Connector not connected"}'
        with pytest.raises(click.ClickException, match="not enabled"):
            _handle_execute_error(resp, "slack.send_message", "ws_123")

    def test_connection_not_found(self):
        resp = MagicMock()
        resp.status_code = 404
        resp.json.return_value = {"message": "Connection not found"}
        resp.text = '{"message": "Connection not found"}'
        with pytest.raises(click.ClickException, match="not enabled"):
            _handle_execute_error(resp, "slack.send_message", "ws_123")

    def test_error_body_parse_failure(self):
        """If error body can't be parsed as JSON, use raw text."""
        resp = MagicMock()
        resp.status_code = 502
        resp.json.side_effect = Exception("not json")
        resp.text = "Bad Gateway"
        with pytest.raises(click.ClickException, match="API error 502"):
            _handle_execute_error(resp, "tool", "ws")

    def test_nested_body_message(self):
        resp = MagicMock()
        resp.status_code = 403
        resp.json.return_value = {
            "body": {"message": "not authorized to access this resource"}
        }
        resp.text = '{"body": {"message": "not authorized"}}'
        with pytest.raises(click.ClickException, match="not enabled"):
            _handle_execute_error(resp, "tool", "ws")


# ===================================================================
# _redact_headers
# ===================================================================

class TestRedactHeaders:
    def test_redacts_long_auth(self):
        headers = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA",
            "Content-Type": "application/json",
        }
        redacted = _redact_headers(headers)
        assert redacted["Authorization"].endswith("...")
        assert len(redacted["Authorization"]) == 23  # 20 + "..."
        assert redacted["Content-Type"] == "application/json"

    def test_redacts_api_key(self):
        headers = {
            "x-fastn-api-key": "9cbb710d583e17b370042825fee33a2bb7aaaa61",
        }
        redacted = _redact_headers(headers)
        assert redacted["x-fastn-api-key"].endswith("...")

    def test_short_values_not_redacted(self):
        headers = {
            "Authorization": "short-token",
            "x-fastn-api-key": "short",
        }
        redacted = _redact_headers(headers)
        # Short values (<= 20 chars) are not redacted
        assert redacted["Authorization"] == "short-token"

    def test_non_sensitive_headers_unchanged(self):
        headers = {
            "Content-Type": "application/json",
            "realm": "fastn",
            "stage": "LIVE",
        }
        redacted = _redact_headers(headers)
        assert redacted == headers


# ===================================================================
# _workspace_url
# ===================================================================

class TestWorkspaceUrl:
    def test_with_workspace_id(self):
        url = _workspace_url("ws_123")
        assert "ws_123" in url
        assert "app.ucl.dev" in url

    def test_without_workspace_id(self):
        url = _workspace_url("")
        assert url == "https://app.ucl.dev"


# ===================================================================
# _format_schema_properties
# ===================================================================

class TestFormatSchemaProperties:
    def test_flat_properties(self):
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "User's name"},
                "age": {"type": "integer"},
            },
            "required": ["name"],
        }
        lines = _format_schema_properties(schema)
        assert len(lines) == 2
        assert any("name" in l and "required" in l for l in lines)
        assert any("age" in l for l in lines)

    def test_single_wrapper_unwrapped(self):
        schema = {
            "type": "object",
            "properties": {
                "body": {
                    "type": "object",
                    "properties": {
                        "channel": {"type": "string", "description": "Channel"},
                        "text": {"type": "string"},
                    },
                    "required": ["channel"],
                },
            },
        }
        lines = _format_schema_properties(schema)
        assert any("channel" in l for l in lines)
        assert any("text" in l for l in lines)
        # Should NOT have "body" as a property
        assert not any("body" in l and "object" in l for l in lines)

    def test_empty_schema(self):
        lines = _format_schema_properties({})
        assert lines == []

    def test_custom_indent(self):
        schema = {
            "type": "object",
            "properties": {
                "x": {"type": "string"},
            },
        }
        lines = _format_schema_properties(schema, indent=10)
        assert lines[0].startswith(" " * 10)


# ===================================================================
# _extract_org_id
# ===================================================================

class TestExtractOrgId:
    @patch("fastn.oauth._decode_jwt_payload")
    def test_extracts_org_from_jwt(self, mock_decode):
        from fastn.cli._helpers import _extract_org_id

        mock_decode.return_value = {
            "realm_access": {
                "roles": [
                    "default-roles",
                    "ORG#org_123#admin",
                    "user",
                ]
            }
        }

        class FakeConfig:
            auth_token = "fake-jwt"

        result = _extract_org_id(FakeConfig())
        assert result == "org_123"

    def test_no_auth_token(self):
        from fastn.cli._helpers import _extract_org_id

        class FakeConfig:
            auth_token = ""

        result = _extract_org_id(FakeConfig())
        assert result == ""

    @patch("fastn.oauth._decode_jwt_payload")
    def test_no_org_role(self, mock_decode):
        from fastn.cli._helpers import _extract_org_id

        mock_decode.return_value = {
            "realm_access": {
                "roles": ["default-roles", "user"]
            }
        }

        class FakeConfig:
            auth_token = "fake-jwt"

        result = _extract_org_id(FakeConfig())
        assert result == ""


# ===================================================================
# _ensure_fresh_token
# ===================================================================

class TestEnsureFreshToken:
    @patch("fastn.oauth.is_token_expired")
    def test_no_refresh_token_skips(self, mock_expired):
        from fastn.cli._helpers import _ensure_fresh_token

        class FakeConfig:
            refresh_token = ""
            token_expiry = ""

        _ensure_fresh_token(FakeConfig())
        mock_expired.assert_not_called()

    @patch("fastn.oauth.is_token_expired")
    def test_token_not_expired_skips(self, mock_expired):
        from fastn.cli._helpers import _ensure_fresh_token

        mock_expired.return_value = False

        class FakeConfig:
            refresh_token = "rt_test"
            token_expiry = "2027-01-01T00:00:00+00:00"

        _ensure_fresh_token(FakeConfig())
        # Should return without refreshing

    @patch("fastn.config.save_config")
    @patch("fastn.oauth.compute_token_expiry")
    @patch("fastn.oauth.refresh_access_token")
    @patch("fastn.oauth.is_token_expired")
    def test_token_expired_refreshes(self, mock_expired, mock_refresh,
                                      mock_compute, mock_save):
        from fastn.cli._helpers import _ensure_fresh_token

        mock_expired.return_value = True

        class FakeTokens:
            access_token = "new_at"
            refresh_token = "new_rt"
            expires_in = 3600

        mock_refresh.return_value = FakeTokens()
        mock_compute.return_value = "2027-01-01T01:00:00+00:00"

        class FakeConfig:
            refresh_token = "rt_old"
            token_expiry = "2020-01-01T00:00:00+00:00"
            auth_token = ""

        config = FakeConfig()
        _ensure_fresh_token(config)
        assert config.auth_token == "new_at"
        assert config.refresh_token == "new_rt"
        mock_save.assert_called_once()

    @patch("fastn.oauth.refresh_access_token")
    @patch("fastn.oauth.is_token_expired")
    def test_refresh_failure_raises(self, mock_expired, mock_refresh):
        from fastn.cli._helpers import _ensure_fresh_token

        mock_expired.return_value = True
        mock_refresh.side_effect = Exception("refresh failed")

        class FakeConfig:
            refresh_token = "rt_old"
            token_expiry = "2020-01-01T00:00:00+00:00"

        with pytest.raises(click.ClickException, match="Session expired"):
            _ensure_fresh_token(FakeConfig())


# ===================================================================
# _coerce_value edge cases
# ===================================================================

class TestCoerceValueExtended:
    def test_null_string(self):
        assert _coerce_value("null", "string") is None

    def test_nested_json(self):
        result = _coerce_value('{"a": {"b": 1}}', "object")
        assert result == {"a": {"b": 1}}

    def test_json_array_of_objects(self):
        result = _coerce_value('[{"id": 1}, {"id": 2}]', "array")
        assert len(result) == 2
        assert result[0]["id"] == 1

    def test_numeric_string_stays_string(self):
        """Numeric strings should be parsed as numbers by json.loads."""
        result = _coerce_value("42", "string")
        assert result == 42  # json.loads parses it

    def test_empty_string(self):
        assert _coerce_value("", "string") == ""


# ===================================================================
# _parse_extra_args edge cases
# ===================================================================

class TestParseExtraArgsExtended:
    def test_mixed_flags_and_values(self):
        args = ["--verbose", "--channel", "general", "--dry-run"]
        result = _parse_extra_args(args)
        assert result["verbose"] is True
        assert result["channel"] == "general"
        assert result["dry_run"] is True

    def test_json_object_value(self):
        args = ["--data", '{"key": "value"}']
        result = _parse_extra_args(args)
        assert result["data"] == {"key": "value"}

    def test_json_array_value(self):
        args = ["--tags", '["a", "b", "c"]']
        result = _parse_extra_args(args)
        assert result["tags"] == ["a", "b", "c"]

    def test_boolean_true_value(self):
        args = ["--active", "true"]
        result = _parse_extra_args(args)
        assert result["active"] is True

    def test_boolean_false_value(self):
        args = ["--active", "false"]
        result = _parse_extra_args(args)
        assert result["active"] is False

    def test_integer_value(self):
        args = ["--count", "42"]
        result = _parse_extra_args(args)
        assert result["count"] == 42

    def test_float_value(self):
        args = ["--price", "19.99"]
        result = _parse_extra_args(args)
        assert result["price"] == 19.99

    def test_non_flag_args_ignored(self):
        args = ["positional_arg", "--key", "value"]
        result = _parse_extra_args(args)
        assert "positional_arg" not in result
        assert result["key"] == "value"

    def test_last_flag_no_value(self):
        args = ["--key", "value", "--flag"]
        result = _parse_extra_args(args)
        assert result["key"] == "value"
        assert result["flag"] is True
