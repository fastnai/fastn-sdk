"""Tests for _detect_api_error in agent_command."""

from __future__ import annotations

from fastn.cli.agent_command import _detect_api_error


class TestNonDictResponses:
    """Non-dict inputs: None, strings, lists."""

    def test_none_returns_error(self) -> None:
        is_err, detail = _detect_api_error(None)
        assert is_err is True
        assert detail == "empty response"

    def test_empty_string_returns_error(self) -> None:
        is_err, detail = _detect_api_error("")
        assert is_err is True
        assert detail == "empty response"

    def test_whitespace_string_returns_error(self) -> None:
        is_err, detail = _detect_api_error("   ")
        assert is_err is True
        assert detail == "empty response"

    def test_error_prefix_string(self) -> None:
        is_err, detail = _detect_api_error("Error: something broke")
        assert is_err is True
        assert "Error: something broke" in detail

    def test_fault_prefix_string(self) -> None:
        is_err, detail = _detect_api_error("Fault detected in service")
        assert is_err is True
        assert "Fault" in detail

    def test_failure_prefix_string(self) -> None:
        is_err, detail = _detect_api_error("Failure: timeout")
        assert is_err is True

    def test_exception_prefix_string(self) -> None:
        is_err, detail = _detect_api_error("Exception in thread main")
        assert is_err is True

    def test_fatal_prefix_string(self) -> None:
        is_err, detail = _detect_api_error("Fatal: out of memory")
        assert is_err is True

    def test_normal_string_no_error(self) -> None:
        is_err, detail = _detect_api_error("All good here")
        assert is_err is False
        assert detail == ""

    def test_list_returns_no_error(self) -> None:
        is_err, detail = _detect_api_error([{"id": 1}, {"id": 2}])
        assert is_err is False
        assert detail == ""

    def test_empty_list_returns_no_error(self) -> None:
        is_err, detail = _detect_api_error([])
        assert is_err is False
        assert detail == ""

    def test_integer_returns_no_error(self) -> None:
        is_err, detail = _detect_api_error(42)
        assert is_err is False


class TestExplicitErrorFields:
    """Dicts with explicit error/errors/errorMessage/fault/failure keys."""

    def test_error_string(self) -> None:
        is_err, detail = _detect_api_error({"error": "something went wrong"})
        assert is_err is True
        assert "something went wrong" in detail

    def test_errors_list(self) -> None:
        is_err, detail = _detect_api_error({"errors": [{"message": "bad input"}]})
        assert is_err is True
        assert "bad input" in detail

    def test_error_message_field(self) -> None:
        is_err, detail = _detect_api_error({"errorMessage": "rate limit hit"})
        assert is_err is True
        assert "rate limit hit" in detail

    def test_fault_field(self) -> None:
        is_err, detail = _detect_api_error({"fault": "service unavailable"})
        assert is_err is True
        assert "service unavailable" in detail

    def test_failure_field(self) -> None:
        is_err, detail = _detect_api_error({"failure": "connection refused"})
        assert is_err is True
        assert "connection refused" in detail

    def test_error_false_is_not_error(self) -> None:
        is_err, _ = _detect_api_error({"error": False})
        assert is_err is False

    def test_errors_empty_list_is_not_error(self) -> None:
        is_err, _ = _detect_api_error({"errors": []})
        assert is_err is False

    def test_nested_error_object_stripe_style(self) -> None:
        result = {"error": {"type": "card_error", "message": "Your card was declined"}}
        is_err, detail = _detect_api_error(result)
        assert is_err is True
        assert "Your card was declined" in detail


class TestNegativeSuccessIndicators:
    """ok: false, success: false, etc."""

    def test_ok_false(self) -> None:
        is_err, _ = _detect_api_error({"ok": False})
        assert is_err is True

    def test_success_false(self) -> None:
        is_err, _ = _detect_api_error({"success": False})
        assert is_err is True

    def test_ok_false_with_message(self) -> None:
        is_err, detail = _detect_api_error({"ok": False, "message": "channel not found"})
        assert is_err is True
        assert "channel not found" in detail

    def test_success_false_with_description(self) -> None:
        is_err, detail = _detect_api_error({"success": False, "description": "invalid token"})
        assert is_err is True
        assert "invalid token" in detail


class TestStatusStrings:
    """status field with error-like string values."""

    def test_status_error(self) -> None:
        is_err, detail = _detect_api_error({"status": "error"})
        assert is_err is True

    def test_status_failed(self) -> None:
        is_err, detail = _detect_api_error({"status": "failed"})
        assert is_err is True

    def test_status_not_found(self) -> None:
        is_err, detail = _detect_api_error({"status": "not_found"})
        assert is_err is True

    def test_status_ok_is_not_error(self) -> None:
        is_err, _ = _detect_api_error({"status": "ok"})
        assert is_err is False

    def test_status_active_is_not_error(self) -> None:
        is_err, _ = _detect_api_error({"status": "active"})
        assert is_err is False


class TestHTTPCodesInBody:
    """statusCode, status_code with numeric HTTP error codes."""

    def test_status_code_404(self) -> None:
        is_err, detail = _detect_api_error({"statusCode": 404})
        assert is_err is True
        assert "404" in detail

    def test_status_code_500(self) -> None:
        is_err, detail = _detect_api_error({"status_code": 500})
        assert is_err is True

    def test_status_code_200_is_not_error(self) -> None:
        is_err, _ = _detect_api_error({"statusCode": 200})
        assert is_err is False

    def test_status_code_with_message(self) -> None:
        is_err, detail = _detect_api_error({"statusCode": 403, "message": "Forbidden"})
        assert is_err is True
        assert "Forbidden" in detail


class TestErrorCodeStrings:
    """code field with well-known error code strings."""

    def test_code_not_found(self) -> None:
        is_err, detail = _detect_api_error({"code": "not_found"})
        assert is_err is True

    def test_code_rate_limited(self) -> None:
        is_err, detail = _detect_api_error({"code": "rate_limited"})
        assert is_err is True

    def test_code_with_message(self) -> None:
        is_err, detail = _detect_api_error({"code": "unauthorized", "message": "bad key"})
        assert is_err is True
        assert "bad key" in detail

    def test_numeric_code_400(self) -> None:
        is_err, detail = _detect_api_error({"code": 400})
        assert is_err is True

    def test_numeric_code_200_is_not_error(self) -> None:
        is_err, _ = _detect_api_error({"code": 200})
        assert is_err is False

    def test_unknown_code_string_is_not_error(self) -> None:
        is_err, _ = _detect_api_error({"code": "my_custom_code"})
        assert is_err is False


class TestCleanSuccess:
    """Responses that should NOT be detected as errors."""

    def test_ok_true_with_data(self) -> None:
        is_err, _ = _detect_api_error({"ok": True, "data": [1, 2, 3]})
        assert is_err is False

    def test_success_true(self) -> None:
        is_err, _ = _detect_api_error({"success": True})
        assert is_err is False

    def test_plain_result(self) -> None:
        is_err, _ = _detect_api_error({"result": "good", "id": 42})
        assert is_err is False

    def test_empty_dict(self) -> None:
        is_err, _ = _detect_api_error({})
        assert is_err is False
