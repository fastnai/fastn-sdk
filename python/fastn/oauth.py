"""Keycloak Device Authorization Grant (RFC 8628) for Fastn CLI.

Provides browser-based login for CLI applications:
1. CLI requests a device code from Keycloak
2. User opens browser, logs in, enters code
3. CLI polls until authorized, receives tokens

Usage:
    from fastn.oauth import request_device_code, poll_for_token

    device = request_device_code()
    print(f"Visit {device.verification_uri} and enter code: {device.user_code}")
    tokens = poll_for_token(device.device_code, device.interval, device.expires_in)
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

import httpx

from fastn.exceptions import OAuthError

# Keycloak configuration
KEYCLOAK_BASE = "https://live.fastn.ai/auth"
KEYCLOAK_REALM = "fastn"
CLIENT_ID = "fastn-sdk"

DEVICE_AUTH_URL = (
    f"{KEYCLOAK_BASE}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/auth/device"
)
TOKEN_URL = (
    f"{KEYCLOAK_BASE}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token"
)
USERINFO_URL = (
    f"{KEYCLOAK_BASE}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/userinfo"
)

GRANT_TYPE_DEVICE = "urn:ietf:params:oauth:grant-type:device_code"
GRANT_TYPE_REFRESH = "refresh_token"


@dataclass
class DeviceCodeResponse:
    """Response from the device authorization endpoint."""

    device_code: str
    user_code: str
    verification_uri: str
    verification_uri_complete: str
    expires_in: int
    interval: int


@dataclass
class TokenResponse:
    """Response from the token endpoint."""

    access_token: str
    refresh_token: str
    expires_in: int
    token_type: str


def request_device_code(
    client: Optional[httpx.Client] = None,
) -> DeviceCodeResponse:
    """Request a device code from Keycloak.

    POST to the device authorization endpoint with client_id.
    Returns device_code, user_code, and verification URIs.

    Args:
        client: Optional httpx.Client. Created internally if not provided.

    Returns:
        DeviceCodeResponse with all fields from Keycloak.

    Raises:
        OAuthError: If the request fails.
    """
    should_close = client is None
    if client is None:
        client = httpx.Client(timeout=30.0)

    try:
        response = client.post(
            DEVICE_AUTH_URL,
            data={
                "client_id": CLIENT_ID,
                "scope": "openid profile email",
            },
        )

        if response.status_code != 200:
            # Parse Keycloak error for a user-friendly message
            try:
                error_data = response.json()
                error_code = error_data.get("error", "")
                error_desc = error_data.get("error_description", "")
            except Exception:
                error_code = ""
                error_desc = ""

            if error_code == "invalid_client":
                raise OAuthError(
                    "Device login is not configured on the server. "
                    f"The Keycloak client '{CLIENT_ID}' must be created with "
                    "'OAuth 2.0 Device Authorization Grant' enabled. "
                    "Contact your Fastn administrator.",
                    error_code="invalid_client",
                )
            elif error_code == "unauthorized_client":
                raise OAuthError(
                    f"The Keycloak client '{CLIENT_ID}' exists but does not have "
                    "'OAuth 2.0 Device Authorization Grant' enabled. "
                    "Contact your Fastn administrator.",
                    error_code="unauthorized_client",
                )

            raise OAuthError(
                f"Device authorization request failed ({response.status_code}): "
                f"{error_desc or response.text}",
                error_code=error_code or "device_request_failed",
            )

        data = response.json()
        return DeviceCodeResponse(
            device_code=data["device_code"],
            user_code=data["user_code"],
            verification_uri=data["verification_uri"],
            verification_uri_complete=data.get(
                "verification_uri_complete", data["verification_uri"]
            ),
            expires_in=data.get("expires_in", 600),
            interval=data.get("interval", 5),
        )
    finally:
        if should_close:
            client.close()


def poll_for_token(
    device_code: str,
    interval: int = 5,
    expires_in: int = 600,
    client: Optional[httpx.Client] = None,
) -> TokenResponse:
    """Poll the token endpoint until the user authorizes.

    Implements RFC 8628 polling behavior:
    - authorization_pending: keep polling
    - slow_down: increase interval by 5 seconds
    - access_denied: raise OAuthError (user denied)
    - expired_token: raise OAuthError (timeout)

    Args:
        device_code: The device code from request_device_code().
        interval: Polling interval in seconds.
        expires_in: Maximum time to wait in seconds.
        client: Optional httpx.Client.

    Returns:
        TokenResponse with access_token and refresh_token.

    Raises:
        OAuthError: If authorization is denied or expires.
    """
    should_close = client is None
    if client is None:
        client = httpx.Client(timeout=30.0)

    poll_interval = interval
    deadline = time.monotonic() + expires_in

    try:
        while time.monotonic() < deadline:
            time.sleep(poll_interval)

            response = client.post(
                TOKEN_URL,
                data={
                    "grant_type": GRANT_TYPE_DEVICE,
                    "device_code": device_code,
                    "client_id": CLIENT_ID,
                },
            )

            if response.status_code == 200:
                data = response.json()
                return TokenResponse(
                    access_token=data["access_token"],
                    refresh_token=data.get("refresh_token", ""),
                    expires_in=data.get("expires_in", 3600),
                    token_type=data.get("token_type", "Bearer"),
                )

            # Handle error responses
            try:
                error_data = response.json()
            except Exception:
                raise OAuthError(
                    f"Token endpoint returned {response.status_code}: {response.text}",
                    error_code="unknown",
                )

            error = error_data.get("error", "")

            if error == "authorization_pending":
                continue

            if error == "slow_down":
                poll_interval += 5
                continue

            if error == "access_denied":
                raise OAuthError(
                    "Authorization was denied. The user declined the login request.",
                    error_code="access_denied",
                )

            if error == "expired_token":
                raise OAuthError(
                    "Device code expired. Please run `fastn login` again.",
                    error_code="expired_token",
                )

            raise OAuthError(
                f"Token request failed: {error_data.get('error_description', error)}",
                error_code=error or "unknown",
            )

        raise OAuthError(
            "Authorization timed out. Please run `fastn login` again.",
            error_code="expired_token",
        )
    finally:
        if should_close:
            client.close()


def refresh_access_token(
    refresh_token: str,
    client: Optional[httpx.Client] = None,
) -> TokenResponse:
    """Refresh an expired access token using a refresh token.

    Args:
        refresh_token: The refresh token from a previous login.
        client: Optional httpx.Client.

    Returns:
        TokenResponse with new access_token and refresh_token.

    Raises:
        OAuthError: If the refresh fails (e.g. refresh token expired).
    """
    should_close = client is None
    if client is None:
        client = httpx.Client(timeout=30.0)

    try:
        response = client.post(
            TOKEN_URL,
            data={
                "grant_type": GRANT_TYPE_REFRESH,
                "client_id": CLIENT_ID,
                "refresh_token": refresh_token,
            },
        )

        if response.status_code != 200:
            raise OAuthError(
                "Session expired. Run `fastn login` to re-authenticate.",
                error_code="invalid_grant",
            )

        data = response.json()
        return TokenResponse(
            access_token=data["access_token"],
            refresh_token=data.get("refresh_token", refresh_token),
            expires_in=data.get("expires_in", 3600),
            token_type=data.get("token_type", "Bearer"),
        )
    finally:
        if should_close:
            client.close()


def _decode_jwt_payload(token: str) -> Dict[str, Any]:
    """Decode the payload from a JWT token without verification.

    This is used as a fallback when the userinfo endpoint is
    unreachable (e.g. blocked by a reverse proxy).

    Args:
        token: A JWT access token string.

    Returns:
        Dict with decoded token claims.

    Raises:
        OAuthError: If the token cannot be decoded.
    """
    import base64
    import json as _json

    parts = token.split(".")
    if len(parts) != 3:
        raise OAuthError("Invalid JWT token format.", error_code="invalid_token")

    payload = parts[1]
    # Add base64 padding
    payload += "=" * (4 - len(payload) % 4)
    try:
        data = _json.loads(base64.urlsafe_b64decode(payload))
    except Exception:
        raise OAuthError("Failed to decode JWT token.", error_code="invalid_token")

    return data


def fetch_userinfo(
    access_token: str,
    client: Optional[httpx.Client] = None,
) -> Dict[str, Any]:
    """Fetch user info from Keycloak using an access token.

    Tries the userinfo endpoint first. If the endpoint is unreachable
    (e.g. returns HTML from a reverse proxy), falls back to decoding
    the JWT token payload directly.

    Args:
        access_token: A valid Keycloak access token.
        client: Optional httpx.Client.

    Returns:
        Dict with user profile (name, email, sub, etc.)

    Raises:
        OAuthError: If the request fails and JWT decoding also fails.
    """
    should_close = client is None
    if client is None:
        client = httpx.Client(timeout=30.0)

    try:
        response = client.get(
            USERINFO_URL,
            headers={"Authorization": f"Bearer {access_token}"},
        )

        if response.status_code == 401:
            raise OAuthError(
                "Access token is invalid or expired.",
                error_code="invalid_token",
            )

        if response.status_code != 200:
            raise OAuthError(
                f"Failed to fetch user info: {response.status_code}",
                error_code="userinfo_failed",
            )

        # Check if response is actually JSON (proxy may return HTML)
        content_type = response.headers.get("content-type", "")
        if "json" in content_type:
            return response.json()

        # Endpoint returned non-JSON (e.g. HTML from reverse proxy)
        # Fall back to decoding the JWT token directly
        return _decode_jwt_payload(access_token)
    except OAuthError:
        raise
    except Exception:
        # Network error or other issue — try JWT fallback
        return _decode_jwt_payload(access_token)
    finally:
        if should_close:
            client.close()


def is_token_expired(token_expiry: str) -> bool:
    """Check if a stored token expiry timestamp has passed.

    Uses a 30-second safety buffer to avoid using tokens
    that are about to expire.

    Args:
        token_expiry: ISO-8601 UTC timestamp string.

    Returns:
        True if the token is expired (or will expire within 30 seconds).
    """
    if not token_expiry:
        return True

    try:
        expiry = datetime.fromisoformat(token_expiry)
        # Ensure timezone-aware
        if expiry.tzinfo is None:
            expiry = expiry.replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        buffer = timedelta(seconds=30)
        return now >= (expiry - buffer)
    except (ValueError, TypeError):
        return True


def compute_token_expiry(expires_in: int) -> str:
    """Compute an ISO-8601 expiry timestamp from expires_in seconds.

    Args:
        expires_in: Token lifetime in seconds.

    Returns:
        ISO-8601 UTC timestamp string.
    """
    expiry = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
    return expiry.isoformat()
