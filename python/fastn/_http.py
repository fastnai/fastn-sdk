"""HTTP and GraphQL call helpers for the Fastn SDK."""

from __future__ import annotations

import json
from typing import Any, Dict, Optional

from fastn._constants import GRAPHQL_URL
from fastn.exceptions import APIError, AuthError, FlowNotFoundError, RunNotFoundError


# ---------------------------------------------------------------------------
# Shared HTTP/GraphQL helpers — error handling extracted to reduce duplication
# ---------------------------------------------------------------------------

def _check_api_response(
    response: Any,
    payload: Optional[Dict[str, Any]] = None,
) -> Any:
    """Check an API response for errors and return parsed data.

    Raises AuthError, FlowNotFoundError, RunNotFoundError, or APIError
    depending on the HTTP status code and response body.
    """
    if response.status_code == 401:
        raise AuthError("Authentication failed. Check your API key and credentials.")
    if response.status_code >= 400:
        body = None
        try:
            body = response.json()
        except (ValueError, RuntimeError):
            pass
        # Map specific error codes to typed exceptions
        error_code = (body or {}).get("error", "")
        if error_code == "FLOW_NOT_FOUND":
            raise FlowNotFoundError((payload or {}).get("flow_id", "unknown"))
        if error_code == "RUN_NOT_FOUND":
            raise RunNotFoundError((payload or {}).get("run_id", "unknown"))
        raise APIError(
            f"API error {response.status_code}: {response.text}",
            status_code=response.status_code,
            response_body=body,
        )
    data = response.json()
    if isinstance(data, dict) and "body" in data:
        return data["body"]
    return data


def _check_gql_response(response: Any) -> Dict[str, Any]:
    """Check a GraphQL response for errors and return the data dict.

    Raises AuthError or APIError on HTTP errors. Also checks for
    GraphQL-level errors in the response body.
    """
    if response.status_code == 401:
        raise AuthError("Authentication failed. Check your API key and credentials.")
    if response.status_code >= 400:
        body = None
        try:
            body = response.json()
        except (ValueError, RuntimeError):
            pass
        raise APIError(
            f"GraphQL error {response.status_code}: {response.text}",
            status_code=response.status_code,
            response_body=body,
        )

    data = response.json() or {}
    if data.get("errors"):
        msg = data["errors"][0].get("message", "Unknown GraphQL error")
        raise APIError(f"GraphQL error: {msg}")

    return data.get("data", {})


def _redact_headers(headers: Dict[str, str]) -> Dict[str, str]:
    """Redact sensitive header values for logging."""
    redacted = {}
    for k, v in headers.items():
        if k.lower() in ("authorization", "x-fastn-api-key") and len(str(v)) > 20:
            redacted[k] = str(v)[:20] + "..."
        else:
            redacted[k] = v
    return redacted


def _log_request(client: Any, method: str, url: str, payload: Any = None) -> None:
    """Log an outgoing HTTP request (verbose mode)."""
    client._log(f"{method} {url}")
    client._log(f"Headers: {json.dumps(_redact_headers(dict(client._headers)), indent=2)}")
    client._log(f"Payload: {json.dumps(payload or {}, indent=2, default=str)}")


def _api_call_sync(
    client: Any,
    method: str,
    url: str,
    payload: Optional[Dict[str, Any]] = None,
) -> Any:
    """Shared HTTP call with error handling (sync)."""
    client._ensure_fresh_token()
    headers = dict(client._headers)
    _log_request(client, method, url, payload)

    if method == "POST":
        response = client._http.post(url, json=payload or {}, headers=headers)
    else:
        response = client._http.get(url, headers=headers)

    client._log(f"Response {response.status_code}: {response.text[:2000]}")
    return _check_api_response(response, payload)


async def _api_call_async(
    client: Any,
    method: str,
    url: str,
    payload: Optional[Dict[str, Any]] = None,
) -> Any:
    """Shared HTTP call with error handling (async)."""
    client._ensure_fresh_token()
    headers = dict(client._headers)
    _log_request(client, method, url, payload)

    if method == "POST":
        response = await client._http.post(url, json=payload or {}, headers=headers)
    else:
        response = await client._http.get(url, headers=headers)

    client._log(f"Response {response.status_code}: {response.text[:2000]}")
    return _check_api_response(response, payload)


def _gql_call_sync(
    client: Any,
    query: str,
    variables: Dict[str, Any],
) -> Any:
    """Shared GraphQL call with error handling (sync)."""
    client._ensure_fresh_token()
    headers = dict(client._headers)
    gql_payload = {"query": query, "variables": variables}
    _log_request(client, "POST", GRAPHQL_URL, gql_payload)

    response = client._http.post(GRAPHQL_URL, json=gql_payload, headers=headers)
    client._log(f"Response {response.status_code}: {response.text[:2000]}")
    return _check_gql_response(response)


async def _gql_call_async(
    client: Any,
    query: str,
    variables: Dict[str, Any],
    extra_headers: Dict[str, str] | None = None,
) -> Any:
    """Shared GraphQL call with error handling (async)."""
    client._ensure_fresh_token()
    headers = dict(client._headers)
    if extra_headers:
        headers.update(extra_headers)
    gql_payload = {"query": query, "variables": variables}
    _log_request(client, "POST", GRAPHQL_URL, gql_payload)

    response = await client._http.post(GRAPHQL_URL, json=gql_payload, headers=headers)
    client._log(f"Response {response.status_code}: {response.text[:2000]}")
    return _check_gql_response(response)
