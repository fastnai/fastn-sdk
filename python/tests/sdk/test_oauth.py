"""Tests for Fastn OAuth device authorization flow."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest
from pytest_httpx import HTTPXMock

from fastn.exceptions import OAuthError
from fastn.oauth import (
    DEVICE_AUTH_URL,
    TOKEN_URL,
    USERINFO_URL,
    DeviceCodeResponse,
    TokenResponse,
    _decode_jwt_payload,
    compute_token_expiry,
    fetch_userinfo,
    is_token_expired,
    poll_for_token,
    refresh_access_token,
    request_device_code,
)


class TestRequestDeviceCode:
    def test_success(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            url=DEVICE_AUTH_URL,
            method="POST",
            json={
                "device_code": "dev_123",
                "user_code": "ABCD-EFGH",
                "verification_uri": "https://live.fastn.ai/auth/realms/fastn/device",
                "verification_uri_complete": "https://live.fastn.ai/auth/realms/fastn/device?user_code=ABCD-EFGH",
                "expires_in": 600,
                "interval": 5,
            },
        )

        result = request_device_code()
        assert isinstance(result, DeviceCodeResponse)
        assert result.device_code == "dev_123"
        assert result.user_code == "ABCD-EFGH"
        assert result.interval == 5
        assert result.expires_in == 600

    def test_failure(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            url=DEVICE_AUTH_URL,
            method="POST",
            status_code=400,
            text="Bad Request",
        )

        with pytest.raises(OAuthError, match="Device authorization request failed"):
            request_device_code()

    def test_invalid_client(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            url=DEVICE_AUTH_URL,
            method="POST",
            status_code=401,
            json={
                "error": "invalid_client",
                "error_description": "Invalid client or Invalid client credentials",
            },
        )

        with pytest.raises(OAuthError, match="not configured") as exc_info:
            request_device_code()
        assert exc_info.value.error_code == "invalid_client"

    def test_unauthorized_client(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            url=DEVICE_AUTH_URL,
            method="POST",
            status_code=400,
            json={
                "error": "unauthorized_client",
                "error_description": "Client not allowed for device grant",
            },
        )

        with pytest.raises(OAuthError, match="Device Authorization Grant") as exc_info:
            request_device_code()
        assert exc_info.value.error_code == "unauthorized_client"


class TestPollForToken:
    def test_immediate_success(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            url=TOKEN_URL,
            method="POST",
            json={
                "access_token": "at_123",
                "refresh_token": "rt_456",
                "expires_in": 3600,
                "token_type": "Bearer",
            },
        )

        result = poll_for_token("dev_123", interval=0, expires_in=10)
        assert isinstance(result, TokenResponse)
        assert result.access_token == "at_123"
        assert result.refresh_token == "rt_456"

    def test_pending_then_success(self, httpx_mock: HTTPXMock) -> None:
        # First response: authorization_pending
        httpx_mock.add_response(
            url=TOKEN_URL,
            method="POST",
            status_code=400,
            json={"error": "authorization_pending"},
        )
        # Second response: success
        httpx_mock.add_response(
            url=TOKEN_URL,
            method="POST",
            json={
                "access_token": "at_success",
                "refresh_token": "rt_success",
                "expires_in": 3600,
                "token_type": "Bearer",
            },
        )

        result = poll_for_token("dev_123", interval=0, expires_in=10)
        assert result.access_token == "at_success"

    def test_slow_down(self, httpx_mock: HTTPXMock) -> None:
        # First response: slow_down
        httpx_mock.add_response(
            url=TOKEN_URL,
            method="POST",
            status_code=400,
            json={"error": "slow_down"},
        )
        # Second response: success
        httpx_mock.add_response(
            url=TOKEN_URL,
            method="POST",
            json={
                "access_token": "at_after_slow",
                "refresh_token": "rt_after_slow",
                "expires_in": 3600,
                "token_type": "Bearer",
            },
        )

        result = poll_for_token("dev_123", interval=0, expires_in=30)
        assert result.access_token == "at_after_slow"

    def test_access_denied(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            url=TOKEN_URL,
            method="POST",
            status_code=400,
            json={"error": "access_denied"},
        )

        with pytest.raises(OAuthError, match="denied") as exc_info:
            poll_for_token("dev_123", interval=0, expires_in=10)
        assert exc_info.value.error_code == "access_denied"

    def test_expired_token(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            url=TOKEN_URL,
            method="POST",
            status_code=400,
            json={"error": "expired_token"},
        )

        with pytest.raises(OAuthError, match="expired") as exc_info:
            poll_for_token("dev_123", interval=0, expires_in=10)
        assert exc_info.value.error_code == "expired_token"


class TestRefreshAccessToken:
    def test_success(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            url=TOKEN_URL,
            method="POST",
            json={
                "access_token": "new_at",
                "refresh_token": "new_rt",
                "expires_in": 3600,
                "token_type": "Bearer",
            },
        )

        result = refresh_access_token("old_rt")
        assert result.access_token == "new_at"
        assert result.refresh_token == "new_rt"

        # Verify correct form data was sent
        request = httpx_mock.get_request()
        body = request.content.decode()
        assert "grant_type=refresh_token" in body
        assert "client_id=fastn-sdk" in body
        assert "refresh_token=old_rt" in body

    def test_expired_refresh_token(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            url=TOKEN_URL,
            method="POST",
            status_code=400,
            json={"error": "invalid_grant"},
        )

        with pytest.raises(OAuthError, match="Session expired"):
            refresh_access_token("expired_rt")


def _make_test_jwt(payload: dict) -> str:
    """Create a fake JWT with the given payload (no signature verification)."""
    import base64
    import json as _json

    header = base64.urlsafe_b64encode(
        _json.dumps({"alg": "RS256", "typ": "JWT"}).encode()
    ).rstrip(b"=").decode()
    body = base64.urlsafe_b64encode(
        _json.dumps(payload).encode()
    ).rstrip(b"=").decode()
    sig = base64.urlsafe_b64encode(b"fakesig").rstrip(b"=").decode()
    return f"{header}.{body}.{sig}"


class TestDecodeJwtPayload:
    def test_valid_jwt(self) -> None:
        token = _make_test_jwt({"sub": "user-1", "name": "Alice", "email": "alice@example.com"})
        result = _decode_jwt_payload(token)
        assert result["sub"] == "user-1"
        assert result["name"] == "Alice"
        assert result["email"] == "alice@example.com"

    def test_invalid_format(self) -> None:
        with pytest.raises(OAuthError, match="Invalid JWT"):
            _decode_jwt_payload("not-a-jwt")

    def test_corrupt_payload(self) -> None:
        with pytest.raises(OAuthError, match="Failed to decode"):
            _decode_jwt_payload("header.!!!invalid!!!.signature")


class TestFetchUserinfo:
    def test_success(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            url=USERINFO_URL,
            method="GET",
            json={
                "sub": "user-123",
                "name": "Test User",
                "email": "test@example.com",
            },
        )

        result = fetch_userinfo("valid_token")
        assert result["name"] == "Test User"
        assert result["email"] == "test@example.com"

        # Verify Bearer token was sent
        request = httpx_mock.get_request()
        assert request.headers["Authorization"] == "Bearer valid_token"

    def test_invalid_token(self, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            url=USERINFO_URL,
            method="GET",
            status_code=401,
        )

        with pytest.raises(OAuthError, match="invalid or expired"):
            fetch_userinfo("bad_token")

    def test_falls_back_to_jwt_when_html_returned(self, httpx_mock: HTTPXMock) -> None:
        """When the userinfo endpoint returns HTML (reverse proxy), decode JWT instead."""
        httpx_mock.add_response(
            url=USERINFO_URL,
            method="GET",
            status_code=200,
            html="<!DOCTYPE html><html><body>Redirect</body></html>",
        )

        jwt_token = _make_test_jwt({"sub": "user-jwt", "name": "JWT User", "email": "jwt@example.com"})
        result = fetch_userinfo(jwt_token)
        assert result["sub"] == "user-jwt"
        assert result["name"] == "JWT User"
        assert result["email"] == "jwt@example.com"


class TestTokenExpiry:
    def test_expired_token(self) -> None:
        past = (datetime.now(timezone.utc) - timedelta(minutes=5)).isoformat()
        assert is_token_expired(past) is True

    def test_valid_token(self) -> None:
        future = (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()
        assert is_token_expired(future) is False

    def test_about_to_expire(self) -> None:
        # Within 30-second buffer
        almost = (datetime.now(timezone.utc) + timedelta(seconds=10)).isoformat()
        assert is_token_expired(almost) is True

    def test_empty_string(self) -> None:
        assert is_token_expired("") is True

    def test_invalid_format(self) -> None:
        assert is_token_expired("not-a-date") is True

    def test_compute_token_expiry(self) -> None:
        result = compute_token_expiry(3600)
        # Should be approximately 1 hour from now
        expiry = datetime.fromisoformat(result)
        now = datetime.now(timezone.utc)
        diff = (expiry - now).total_seconds()
        assert 3590 < diff < 3610


class TestOAuthError:
    def test_with_error_code(self) -> None:
        err = OAuthError("test error", error_code="access_denied")
        assert str(err) == "test error"
        assert err.error_code == "access_denied"
        assert isinstance(err, OAuthError)

    def test_without_error_code(self) -> None:
        err = OAuthError("test error")
        assert err.error_code is None

    def test_is_auth_error(self) -> None:
        from fastn.exceptions import AuthError
        err = OAuthError("test")
        assert isinstance(err, AuthError)
