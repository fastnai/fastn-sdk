"""Fastn SDK authentication and header management.

Builds the HTTP headers required for every Fastn API call. This module
is used internally by FastnClient/AsyncFastnClient — you don't need to
call it directly.

Headers sent on every request:
    Content-Type:         application/json
    realm:                fastn
    stage:                LIVE | STAGING | DEV
    x-fastn-custom-auth:  false
    x-fastn-space-id:     <project_id or JWT-derived workspace ID>
    x-tenant:             <tenant_id, default "organization">
    x-fastn-api-key:      <api_key>           (if using API key auth)
    Authorization:        Bearer <auth_token>  (if using JWT auth)
"""

from __future__ import annotations

from typing import Dict

from fastn.config import FastnConfig


def build_headers(config: FastnConfig) -> Dict[str, str]:
    """Build HTTP headers required for all Fastn API calls.

    Args:
        config: The SDK configuration containing credentials.

    Returns:
        Dict of headers to include in every request.
    """
    config.validate()
    return config.get_headers()


def mask_key(api_key: str) -> str:
    """Mask an API key for display, showing only first 8 chars.

    Args:
        api_key: The full API key.

    Returns:
        Masked string like '7ce258be••••••••••••'.
    """
    if len(api_key) <= 8:
        return api_key
    visible = api_key[:8]
    masked = "\u2022" * min(len(api_key) - 8, 12)
    return f"{visible}{masked}"
