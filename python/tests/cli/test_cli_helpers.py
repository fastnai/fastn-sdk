"""Tests for helper functions in fastn.cli._helpers."""

from __future__ import annotations

from fastn.cli._helpers import _coerce_value, _parse_extra_args, _to_snake_case


# ---------------------------------------------------------------------------
# _to_snake_case
# ---------------------------------------------------------------------------

class TestToSnakeCase:
    def test_camel_case(self) -> None:
        assert _to_snake_case("sendMessage") == "send_message"

    def test_pascal_case(self) -> None:
        assert _to_snake_case("SendMessage") == "send_message"

    def test_already_snake(self) -> None:
        assert _to_snake_case("already_snake") == "already_snake"

    def test_all_lowercase(self) -> None:
        assert _to_snake_case("testauth") == "testauth"

    def test_consecutive_caps(self) -> None:
        assert _to_snake_case("HTMLParser") == "html_parser"

    def test_multi_word_camel(self) -> None:
        assert _to_snake_case("getUserByEmail") == "get_user_by_email"

    def test_hyphenated(self) -> None:
        assert _to_snake_case("some-name") == "some_name"

    def test_spaced(self) -> None:
        assert _to_snake_case("some name") == "some_name"

    def test_consecutive_caps_middle(self) -> None:
        assert _to_snake_case("getHTTPResponse") == "get_http_response"


# ---------------------------------------------------------------------------
# _parse_extra_args
# ---------------------------------------------------------------------------

class TestParseExtraArgs:
    def test_key_value_pairs(self) -> None:
        args = ["--channel", "general", "--text", "hello"]
        result = _parse_extra_args(args)
        assert result == {"channel": "general", "text": "hello"}

    def test_json_value(self) -> None:
        args = ["--tags", '["a","b"]']
        result = _parse_extra_args(args)
        assert result == {"tags": ["a", "b"]}

    def test_numeric_value(self) -> None:
        args = ["--count", "5"]
        result = _parse_extra_args(args)
        assert result == {"count": 5}

    def test_boolean_value(self) -> None:
        args = ["--verbose", "true"]
        result = _parse_extra_args(args)
        assert result == {"verbose": True}

    def test_flag_without_value(self) -> None:
        args = ["--dry_run"]
        result = _parse_extra_args(args)
        assert result == {"dry_run": True}

    def test_flag_before_next_flag(self) -> None:
        args = ["--flag", "--key", "val"]
        result = _parse_extra_args(args)
        assert result == {"flag": True, "key": "val"}

    def test_empty_args(self) -> None:
        assert _parse_extra_args([]) == {}

    def test_hyphens_in_key_become_underscores(self) -> None:
        args = ["--my-key", "val"]
        result = _parse_extra_args(args)
        assert result == {"my_key": "val"}

    def test_non_flag_args_ignored(self) -> None:
        args = ["positional", "--key", "val"]
        result = _parse_extra_args(args)
        assert result == {"key": "val"}


# ---------------------------------------------------------------------------
# _coerce_value
# ---------------------------------------------------------------------------

class TestCoerceValue:
    def test_integer(self) -> None:
        assert _coerce_value("42", "integer") == 42

    def test_float(self) -> None:
        assert _coerce_value("3.14", "number") == 3.14

    def test_boolean_true(self) -> None:
        assert _coerce_value("true", "boolean") is True

    def test_boolean_false(self) -> None:
        assert _coerce_value("false", "boolean") is False

    def test_json_array(self) -> None:
        assert _coerce_value('["a", "b"]', "array") == ["a", "b"]

    def test_json_object(self) -> None:
        assert _coerce_value('{"k": "v"}', "object") == {"k": "v"}

    def test_plain_string(self) -> None:
        assert _coerce_value("hello world", "string") == "hello world"

    def test_empty_string(self) -> None:
        assert _coerce_value("", "string") == ""

    def test_string_that_looks_numeric(self) -> None:
        # JSON parsing will convert "5" to int 5 regardless of field_type
        assert _coerce_value("5", "string") == 5

    def test_invalid_json_stays_string(self) -> None:
        assert _coerce_value("not json {", "object") == "not json {"
