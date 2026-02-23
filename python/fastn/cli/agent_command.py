"""Agent command — AI-powered connector discovery and tool execution.

Contains the ``fastn agent`` command and all supporting helpers for
LLM-based parameter extraction, the agentic tool-calling loop, cost
estimation, and evaluation.
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional, Tuple

import click

from fastn.config import FastnConfig, find_fastn_dir, load_config, load_registry, save_config

from fastn.cli import cli, EXECUTE_URL, GET_TOOLS_URL
from fastn.cli._helpers import _verbose_post, _ensure_fresh_token, _extract_input_fields
from fastn.cli._registry import _resolve_friendly_names


# ---------------------------------------------------------------------------
# Tool list extraction
# ---------------------------------------------------------------------------

def _extract_tool_list(data: Any) -> list:
    """Extract the tool list from a getTools API response.

    The API may return tools in various shapes:
        - A plain list: ``[{...}, ...]``
        - ``{"tools": [...]}``, ``{"data": [...]}``
        - ``{"body": [...]}``, ``{"body": {"tools": [...]}}``
        - A single tool dict: ``{actionId: ..., ...}``
    """
    if isinstance(data, list):
        return data

    if not isinstance(data, dict):
        return []

    # Try common wrapper keys
    for key in ("tools", "data"):
        val = data.get(key)
        if isinstance(val, list):
            return val

    # Unwrap body first, then check inside
    body = data.get("body")
    if isinstance(body, list):
        return body
    if isinstance(body, dict):
        for key in ("tools", "data"):
            val = body.get(key)
            if isinstance(val, list):
                return val
        # body itself might be a single tool
        if "actionId" in body:
            return [body]

    # data itself is a single tool
    if "actionId" in data:
        return [data]

    return []


# ---------------------------------------------------------------------------
# LLM provider setup & parameter extraction
# ---------------------------------------------------------------------------

def _setup_llm_provider(config: FastnConfig) -> Optional[FastnConfig]:
    """Interactive LLM provider setup — choose provider, enter API key.

    Returns the updated config with LLM settings, or None if user cancels.
    """
    from fastn.config import LLM_PROVIDERS

    click.echo()
    click.echo("  LLM Setup \u2014 fastn agent uses an LLM to fill in tool parameters")
    click.echo("  from your natural language prompt.")
    click.echo()
    click.echo("  Choose an LLM provider:")
    click.echo()

    providers = list(LLM_PROVIDERS.items())
    for i, (key, info) in enumerate(providers, 1):
        click.echo(f"    {i}. {info['name']}")

    click.echo()
    choice = click.prompt("  Provider number", type=int)
    if choice < 1 or choice > len(providers):
        click.echo("  Invalid choice.")
        return None

    provider_key, provider_info = providers[choice - 1]

    # Check if the API key is already in an environment variable
    env_var = provider_info["env_var"]
    existing_key = os.environ.get(env_var, "")

    if existing_key:
        click.echo(f"  \u2713 Found {env_var} in environment.")
        api_key = existing_key
    else:
        click.echo()
        click.echo(f"  Get your API key from: {provider_info['key_url']}")

        import webbrowser
        if click.confirm("  Open the page in your browser?", default=True):
            try:
                webbrowser.open(provider_info["key_url"])
                click.echo("  (Browser opened)")
            except Exception:
                click.echo("  Open the URL above manually.")

        click.echo()
        api_key = click.prompt(f"  {provider_info['name']} API Key")
        if not api_key.strip():
            click.echo("  No API key provided.")
            return None

    # Verify the SDK package is installed
    pip_package = provider_info["pip_package"]
    try:
        __import__(pip_package.replace("-", "_").split("-")[0])
    except ImportError:
        click.echo(f"\n  \u26a0  Package '{pip_package}' not installed.")
        click.echo(f"  Run: pip install {pip_package}")
        if not click.confirm("  Continue anyway?", default=False):
            return None

    config.llm_provider = provider_key
    config.llm_api_key = api_key
    config.llm_model = provider_info["default_model"]
    save_config(config)

    click.echo(f"\n  \u2713 {provider_info['name']} configured (model: {config.llm_model})")
    click.echo(f"  Saved to .fastn/config.json")
    return config


def _llm_fill_parameters(
    config: FastnConfig,
    prompt_str: str,
    input_schema: dict,
    tool_description: str,
    tool_display_name: str,
) -> Optional[dict]:
    """Use the configured LLM to extract parameters from the prompt.

    Sends the prompt + tool schema to the LLM and asks it to fill in the
    parameter values.  Returns a dict of parameters, or None on failure.
    """
    from fastn.config import LLM_PROVIDERS

    provider = config.llm_provider
    api_key = config.llm_api_key
    model = config.llm_model

    if not provider or not api_key:
        return None

    provider_info = LLM_PROVIDERS.get(provider)
    if not provider_info:
        return None

    model = model or provider_info["default_model"]

    # Build a flat schema for the LLM (unwrap wrappers)
    _pk, fields, required_fields = _extract_input_fields(input_schema)

    if not fields:
        return None

    # Build the schema description for the LLM
    schema_desc = []
    for name, fdata in fields.items():
        ftype = fdata.get("type", "string") if isinstance(fdata, dict) else "string"
        desc = fdata.get("description", "") if isinstance(fdata, dict) else ""
        req = "required" if name in required_fields else "optional"
        line = f"  - {name} ({ftype}, {req})"
        if desc:
            line += f": {desc}"
        schema_desc.append(line)

    schema_text = "\n".join(schema_desc)

    system_msg = (
        f"You are a parameter extraction assistant. "
        f"Given a user request, extract the parameter values for the tool "
        f"'{tool_display_name}'.\n\n"
        f"Tool: {tool_display_name}\n"
    )
    if tool_description:
        system_msg += f"Description: {tool_description}\n"
    system_msg += (
        f"\nParameters:\n{schema_text}\n\n"
        f"Respond with ONLY a valid JSON object containing the extracted "
        f"parameter values. Do not include any other text. "
        f"Only include parameters that can be determined from the user's request. "
        f"Use the exact parameter names shown above."
    )

    try:
        if provider == "openai":
            return _llm_fill_openai(api_key, model, system_msg, prompt_str)
        elif provider == "anthropic":
            return _llm_fill_anthropic(api_key, model, system_msg, prompt_str)
        elif provider == "gemini":
            return _llm_fill_gemini(api_key, model, system_msg, prompt_str)
    except Exception as e:
        click.echo(f"  \u26a0  LLM parameter extraction failed: {e}")
        return None

    return None


def _llm_fill_openai(api_key: str, model: str, system_msg: str, prompt: str) -> Optional[dict]:
    """Extract parameters using OpenAI."""
    try:
        import openai
    except ImportError:
        click.echo("  \u26a0  openai package not installed. Run: pip install openai")
        return None

    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    content = response.choices[0].message.content or ""
    return _parse_llm_json(content)


def _llm_fill_anthropic(api_key: str, model: str, system_msg: str, prompt: str) -> Optional[dict]:
    """Extract parameters using Anthropic."""
    try:
        import anthropic
    except ImportError:
        click.echo("  \u26a0  anthropic package not installed. Run: pip install anthropic")
        return None

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        system=system_msg,
        messages=[{"role": "user", "content": prompt}],
    )

    content = ""
    for block in response.content:
        if hasattr(block, "text"):
            content = block.text
            break
    return _parse_llm_json(content)


def _llm_fill_gemini(api_key: str, model: str, system_msg: str, prompt: str) -> Optional[dict]:
    """Extract parameters using Google Gemini."""
    try:
        from google import genai
    except ImportError:
        click.echo("  \u26a0  google-genai package not installed. Run: pip install google-genai")
        return None

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model,
        contents=f"{system_msg}\n\nUser request: {prompt}",
    )

    content = response.text or ""
    return _parse_llm_json(content)


def _parse_llm_json(content: str) -> Optional[dict]:
    """Parse JSON from LLM response, handling markdown fences."""
    content = content.strip()
    # Strip markdown code fences if present
    if content.startswith("```"):
        lines = content.split("\n")
        # Remove first line (```json or ```) and last line (```)
        lines = [l for l in lines if not l.strip().startswith("```")]
        content = "\n".join(lines).strip()

    try:
        result = json.loads(content)
        if isinstance(result, dict):
            return result
    except (json.JSONDecodeError, ValueError):
        pass
    return None


# ---------------------------------------------------------------------------
# Agent: agentic loop helpers
# ---------------------------------------------------------------------------

_AGENT_MAX_TURNS = 10
def _format_bytes(n: int) -> str:
    """Format byte count as human-readable string."""
    if n < 1024:
        return f"{n} B"
    elif n < 1024 * 1024:
        return f"{n / 1024:.1f} KB"
    return f"{n / (1024 * 1024):.1f} MB"


def _format_duration(seconds: float) -> str:
    """Format duration as human-readable string."""
    if seconds < 1:
        return f"{seconds * 1000:.0f}ms"
    return f"{seconds:.1f}s"


def _format_tokens(n: int) -> str:
    """Format token count with K suffix for large numbers."""
    if n >= 10000:
        return f"{n / 1000:.1f}K"
    return str(n)


def _format_cost(dollars: float) -> str:
    """Format dollar cost."""
    if dollars < 0.001:
        return f"${dollars:.4f}"
    if dollars < 0.01:
        return f"${dollars:.3f}"
    return f"${dollars:.2f}"


# OpenAI pricing per 1M tokens (USD)
_OPENAI_PRICING: Dict[str, tuple] = {
    # (input_per_1M, output_per_1M)
    "gpt-4o": (2.50, 10.00),
    "gpt-4o-mini": (0.15, 0.60),
    "gpt-4-turbo": (10.00, 30.00),
    "gpt-4": (30.00, 60.00),
    "gpt-3.5-turbo": (0.50, 1.50),
}


def _estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """Estimate cost in USD based on model and token counts."""
    # Match model prefix (gpt-4o-mini-2024-07-18 → gpt-4o-mini)
    pricing = None
    for key in sorted(_OPENAI_PRICING.keys(), key=len, reverse=True):
        if model.startswith(key):
            pricing = _OPENAI_PRICING[key]
            break
    if not pricing:
        pricing = _OPENAI_PRICING.get("gpt-4o-mini", (0.15, 0.60))
    in_cost = (input_tokens / 1_000_000) * pricing[0]
    out_cost = (output_tokens / 1_000_000) * pricing[1]
    return in_cost + out_cost


# Each entry: (tool_name, tokens_in, tokens_out, context_tokens,
#               llm_time, tool_time,
#               request_bytes, response_bytes, cumulative_context_bytes, status)
_AgentCallLog = List[tuple]


def _print_agent_summary(
    call_log: _AgentCallLog,
    total_input: int, total_output: int,
    total_llm_time: float, total_tool_time: float,
    model: str = "",
) -> None:
    """Print a single benchmark table of all tool calls."""
    total_time = total_llm_time + total_tool_time

    click.echo()
    click.echo()

    if not call_log:
        cost = _estimate_cost(model, total_input, total_output)
        click.echo("  No tool calls.")
        click.echo(f"  Tokens: {_format_tokens(total_input)} in \u2192 {_format_tokens(total_output)} out")
        click.echo(f"  Time: {_format_duration(total_time)}  Cost: {_format_cost(cost)}")
        return

    # Single consolidated table
    # Columns: #, Tool, LLM, Tool, Context(tokens), In, Out, Cost
    click.echo("  \u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510")
    click.echo("  \u2502  #   Tool                     LLM      Tool     Context      In    Out       Cost      \u2502")
    click.echo("  \u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524")

    total_cost = 0.0
    for i, entry in enumerate(call_log, 1):
        name = entry[0]
        t_in, t_out, ctx = entry[1], entry[2], entry[3]
        llm_t, tool_t = entry[4], entry[5]
        status = entry[9]

        call_cost = _estimate_cost(model, t_in, t_out)
        total_cost += call_cost

        short_name = name if len(name) <= 23 else name[:20] + "..."
        mark = "\u2713" if status == "ok" else "\u2717"

        click.echo(
            f"  \u2502  {mark} {i:<2} {short_name:<23}"
            f" {_format_duration(llm_t):>7}"
            f" {_format_duration(tool_t):>7}"
            f" {_format_tokens(ctx):>9}"
            f" {_format_tokens(t_in):>7}"
            f" {_format_tokens(t_out):>6}"
            f" {_format_cost(call_cost):>10}  \u2502"
        )

    click.echo("  \u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524")
    click.echo(
        f"  \u2502      {'Total':<23}"
        f" {_format_duration(total_llm_time):>7}"
        f" {_format_duration(total_tool_time):>7}"
        f" {_format_tokens(call_log[-1][3]):>9}"
        f" {_format_tokens(total_input):>7}"
        f" {_format_tokens(total_output):>6}"
        f" {_format_cost(total_cost):>10}  \u2502"
    )
    click.echo("  \u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518")
    click.echo()
    click.echo(f"  {_format_duration(total_time)} total  \u00b7  {_format_tokens(total_input + total_output)} tokens  \u00b7  {_format_cost(total_cost)}")


_AGENT_SYSTEM_PROMPT = (
    "You are a helpful assistant with access to tools.\n"
    "Use them to accomplish the user's request, calling multiple in sequence if needed.\n"
    "If a tool call fails, try to recover: look up the correct ID or name using a list/search tool and retry.\n"
    "When done, provide a short summary of what you did."
)


def _build_action_map(
    tool_list: list, registry: dict,
) -> Dict[str, dict]:
    """Build a map from function name \u2192 {actionId, connectorId, display_label, action_info}.

    The getTools API returns tools in OpenAI function-calling format.
    Each tool has ``actionId`` and ``function.name``.  We use the function
    name as the key since that's what the LLM will reference in tool calls.
    """
    action_map: Dict[str, dict] = {}
    for tool in tool_list:
        aid = tool.get("actionId", "")
        fn = tool.get("function", {})
        fn_name = fn.get("name", aid)

        # Resolve friendly names from registry
        friendly_tool, friendly_action, tool_id, action_info = (
            _resolve_friendly_names(aid, fn_name, "", None, registry)
        )
        display_label = (
            f"{friendly_tool}.{friendly_action}"
            if friendly_tool
            else friendly_action or aid
        )

        # Store the raw schema so _execute_tool_call can re-wrap params
        raw_schema = fn.get("parameters", {})
        action_map[fn_name] = {
            "actionId": aid,
            "connectorId": tool_id,
            "display_label": display_label,
            "action_info": action_info,
            "inputSchema": raw_schema,
        }
    return action_map


# ---------------------------------------------------------------------------
# API error detection
# ---------------------------------------------------------------------------

def _detect_api_error(result: Any) -> Tuple[bool, str]:
    """Detect whether an API response body indicates an error.

    Works across diverse API response formats (Slack, GitHub, Stripe,
    generic REST, GraphQL, etc.).  Returns ``(is_error, detail)`` where
    *detail* is a short human-readable error string extracted from the
    response (or ``""`` if no detail could be extracted).

    Detection strategy (checked in order):

    1. **Non-dict responses** \u2013 strings that look like error messages,
       empty responses, etc.
    2. **Explicit error fields** \u2013 ``error``, ``errors``, ``error_message``,
       ``errorMessage``, ``err``, ``fault``, ``failure``.
    3. **Negative success indicators** \u2013 ``ok: false``, ``success: false``,
       ``succeeded: false``, ``status`` with error-like values.
    4. **HTTP status codes in body** \u2013 ``statusCode >= 400``, ``status_code >= 400``,
       ``code`` with well-known error codes.
    5. **GraphQL errors** \u2013 top-level ``errors`` array.
    """

    # ── Non-dict responses ──────────────────────────────────────────────
    if result is None:
        return True, "empty response"

    if isinstance(result, str):
        lower = result.lower().strip()
        if not lower:
            return True, "empty response"
        # Catch plain-text error messages
        if lower.startswith(("error", "fault", "failure", "exception", "fatal")):
            return True, result[:120]
        return False, ""

    if isinstance(result, list):
        # A list is usually a valid data response (array of items)
        return False, ""

    if not isinstance(result, dict):
        return False, ""

    # ── Helper to extract a short detail string ─────────────────────────
    def _extract_detail(val: Any) -> str:
        if isinstance(val, str):
            return val[:200]
        if isinstance(val, dict):
            # Common sub-patterns: {"message": "...", "code": "..."}
            for k in ("message", "msg", "description", "detail", "reason", "text"):
                if k in val:
                    return str(val[k])[:200]
            return json.dumps(val, separators=(", ", ": "))[:200]
        if isinstance(val, list) and val:
            first = val[0]
            if isinstance(first, dict):
                for k in ("message", "msg", "description", "detail", "reason", "text"):
                    if k in first:
                        return str(first[k])[:200]
            return str(first)[:200]
        if isinstance(val, bool) and val:
            return ""  # error: true — no extra detail
        return str(val)[:200] if val else ""

    # ── 1. Explicit error fields ────────────────────────────────────────
    _ERROR_KEYS = ("error", "errors", "error_message", "errorMessage",
                   "err", "fault", "failure")
    for key in _ERROR_KEYS:
        val = result.get(key)
        if val is None:
            continue
        # ``error: false`` or ``errors: []`` means no error
        if val is False or (isinstance(val, (list, str)) and not val):
            continue
        return True, _extract_detail(val)

    # ── 2. Negative success indicators ──────────────────────────────────
    for key in ("ok", "success", "succeeded", "successful"):
        val = result.get(key)
        if val is not None and val is False:
            # Try to find a companion message field
            detail = ""
            for mk in ("message", "msg", "description", "detail", "reason"):
                if mk in result:
                    detail = str(result[mk])[:200]
                    break
            return True, detail

    # ── 3. Status field with error-like values ──────────────────────────
    status_val = result.get("status")
    if isinstance(status_val, str):
        lower_status = status_val.lower()
        _ERROR_STATUSES = (
            "error", "failed", "failure", "fail", "rejected",
            "denied", "unauthorized", "forbidden", "not_found",
            "not found", "invalid", "expired", "timeout", "timed_out",
        )
        if lower_status in _ERROR_STATUSES:
            detail = ""
            for mk in ("message", "msg", "error", "description", "detail", "reason"):
                if mk in result and mk != "status":
                    detail = str(result[mk])[:200]
                    break
            return True, detail or status_val

    # ── 4. HTTP status codes embedded in body ───────────────────────────
    for key in ("statusCode", "status_code", "httpStatusCode", "http_status_code"):
        code = result.get(key)
        if isinstance(code, int) and code >= 400:
            detail = ""
            for mk in ("message", "msg", "error", "body", "description", "detail"):
                if mk in result:
                    detail = str(result[mk])[:200]
                    break
            return True, detail or f"HTTP {code}"

    # Also check "code" but only for well-known error strings
    code_val = result.get("code")
    if isinstance(code_val, str):
        lower_code = code_val.lower()
        _ERROR_CODES = (
            "not_found", "invalid", "unauthorized", "forbidden",
            "rate_limited", "rate_limit_exceeded", "too_many_requests",
            "internal_error", "server_error", "service_unavailable",
            "bad_request", "conflict", "gone", "unprocessable",
            "permission_denied", "unauthenticated", "cancelled",
        )
        if lower_code in _ERROR_CODES:
            detail = ""
            for mk in ("message", "msg", "description", "detail"):
                if mk in result:
                    detail = str(result[mk])[:200]
                    break
            return True, detail or code_val
    if isinstance(code_val, int) and code_val >= 400:
        detail = ""
        for mk in ("message", "msg", "description", "detail"):
            if mk in result:
                detail = str(result[mk])[:200]
                break
        return True, detail or f"code {code_val}"

    # ── No error detected ───────────────────────────────────────────────
    return False, ""


# ---------------------------------------------------------------------------
# Tool execution
# ---------------------------------------------------------------------------

def _execute_tool_call(
    fn_name: str,
    fn_args: dict,
    action_map: Dict[str, dict],
    headers: dict,
    workspace_id: str,
    connection_id: Optional[str],
    auto_confirm: bool = True,
) -> dict:
    """Execute a single tool call and return the result.

    Looks up the actionId from the action_map, calls the executeTool API,
    and prints status.  When *auto_confirm* is False, prompts the user
    before each execution.

    The returned dict includes metadata keys (prefixed with ``_``):

    - ``_tool_duration``: API call latency in seconds
    - ``_payload_bytes``: raw API response size (before truncation)
    - ``_context_bytes``: size actually fed back to LLM (after truncation)
    - ``_request_bytes``: size of the request payload sent to the tool API
    """
    import time as _time

    mapping = action_map.get(fn_name, {})
    action_id = mapping.get("actionId", fn_name)
    connector_id = mapping.get("connectorId", "")
    display_label = mapping.get("display_label", fn_name)

    # Compact one-line display
    compact_args = json.dumps(fn_args, separators=(", ", ": "))
    if len(compact_args) > 60:
        compact_args = compact_args[:57] + "..."
    click.echo(f"  \u25b8 {display_label}({compact_args})")

    # Confirmation gate
    if not auto_confirm:
        if not click.confirm("    Execute?", default=True):
            click.echo("    \u23ed  Skipped")
            return {"skipped": True, "_tool_duration": 0.0, "_payload_bytes": 0,
                    "_context_bytes": 0, "_request_bytes": 0}

    # Re-wrap flat LLM params into the structure the API expects.
    # The LLM sees unwrapped schemas (flat {channel, text}) but the API
    # expects wrapped params ({body: {channel, text}}).
    raw_schema = mapping.get("inputSchema") or {}
    if raw_schema:
        from fastn.client import _build_params_from_schema
        exec_parameters = _build_params_from_schema(
            {"inputSchema": raw_schema}, fn_args,
        )
    else:
        exec_parameters = fn_args

    execute_payload: dict = {
        "input": {
            "actionId": action_id,
            "parameters": exec_parameters,
            "agentId": workspace_id,
        }
    }
    if connector_id:
        execute_payload["input"]["connectorId"] = connector_id
    if connection_id:
        execute_payload["input"]["connectionId"] = connection_id

    request_bytes = len(json.dumps(execute_payload).encode("utf-8"))

    t0 = _time.monotonic()
    resp = _verbose_post(EXECUTE_URL, headers, execute_payload)
    tool_duration = _time.monotonic() - t0

    if resp.status_code >= 400:
        error_text = resp.text
        click.echo(f"    \u2717 Error ({resp.status_code}):")
        click.echo(f"      {error_text}")
        return {"error": True, "status_code": resp.status_code, "message": error_text,
                "_tool_duration": tool_duration, "_payload_bytes": 0,
                "_context_bytes": 0, "_request_bytes": request_bytes}

    result = resp.json()
    if isinstance(result, dict) and "body" in result:
        result = result["body"]

    # Detect errors in the response body (API returned 200 but with error)
    is_error, error_detail = _detect_api_error(result)

    result_str = json.dumps(result, indent=2)
    payload_bytes = len(result_str.encode("utf-8"))

    if is_error:
        err_msg = f" ({error_detail})" if error_detail else ""
        click.echo(f"    \u2717 Error{err_msg}:")
        click.echo(f"      {result_str}")
    elif payload_bytes > 200:
        click.echo(f"    \u2713 {_format_bytes(payload_bytes)}")
    else:
        one_line = json.dumps(result, separators=(", ", ": "))
        if len(one_line) > 60:
            one_line = one_line[:57] + "..."
        click.echo(f"    \u2713 {one_line}")

    # Truncate very large results before feeding back to the LLM
    _MAX_RESULT_CHARS = 4000
    if len(result_str) > _MAX_RESULT_CHARS:
        truncated = result_str[:_MAX_RESULT_CHARS]
        result = {
            "_truncated": True,
            "_original_bytes": len(result_str),
            "preview": truncated,
        }

    context_str = json.dumps(result, default=str)
    context_bytes = len(context_str.encode("utf-8"))

    if is_error:
        # Ensure there's an "error" key the loop can detect.
        # If the API already has its own error field, keep it.
        if not result.get("error"):
            result["error"] = error_detail or True
    result["_tool_duration"] = tool_duration
    result["_payload_bytes"] = payload_bytes
    result["_context_bytes"] = context_bytes
    result["_request_bytes"] = request_bytes
    return result


# ---------------------------------------------------------------------------
# OpenAI tool conversion
# ---------------------------------------------------------------------------

def _convert_tools_for_openai(tool_list: list) -> list:
    """Convert getTools API response to OpenAI function-calling format.

    Schemas are unwrapped so the LLM sees flat params (e.g. ``channel``,
    ``text``) instead of nested wrappers (``body.channel``, ``body.text``).
    The execution side re-wraps via ``_build_params_from_schema``.
    """
    from fastn.client import _unwrap_input_schema

    result = []
    for tool in tool_list:
        fn = tool.get("function", {})
        if fn:
            params = fn.get("parameters", {})
            result.append({
                "type": "function",
                "function": {
                    "name": fn.get("name", ""),
                    "description": fn.get("description", ""),
                    "parameters": _unwrap_input_schema(params),
                },
            })
        else:
            params = tool.get("inputSchema", tool.get("parameters", {}))
            result.append({
                "type": "function",
                "function": {
                    "name": tool.get("name", tool.get("actionId", "")),
                    "description": tool.get("description", ""),
                    "parameters": _unwrap_input_schema(params),
                },
            })
    return result


# ---------------------------------------------------------------------------
# OpenAI agentic loop
# ---------------------------------------------------------------------------

def _agent_loop_openai(
    api_key: str,
    model: str,
    prompt_str: str,
    tools: list,
    action_map: Dict[str, dict],
    headers: dict,
    workspace_id: str,
    connection_id: Optional[str],
    max_turns: int = _AGENT_MAX_TURNS,
    auto_confirm: bool = True,
    max_errors: int = 2,
) -> tuple:
    """Run the agentic loop using OpenAI's function-calling API.

    Returns (final_response, eval_log).
    """
    try:
        import openai
    except ImportError:
        raise click.ClickException(
            "openai package not installed. Run: pip install openai"
        )

    import time as _time

    client = openai.OpenAI(api_key=api_key)
    messages: list = [
        {"role": "system", "content": _AGENT_SYSTEM_PROMPT},
        {"role": "user", "content": prompt_str},
    ]

    total_input = 0
    total_output = 0
    total_llm_time = 0.0
    total_tool_time = 0.0
    cumulative_ctx_bytes = 0
    call_log: _AgentCallLog = []
    eval_log: list = []  # [{tool, args, result, status}] for --eval
    consecutive_errors = 0

    for turn in range(max_turns):
        t0 = _time.monotonic()
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools if tools else None,
        )
        llm_duration = _time.monotonic() - t0
        total_llm_time += llm_duration

        usage = getattr(response, "usage", None)
        turn_in = getattr(usage, "prompt_tokens", 0) or 0
        turn_out = getattr(usage, "completion_tokens", 0) or 0
        total_input += turn_in
        total_output += turn_out

        choice = response.choices[0]
        message = choice.message

        if message.tool_calls:
            messages.append(message)

            # Show what the LLM chose
            num_calls = len(message.tool_calls)
            chosen = [action_map.get(tc.function.name, {}).get("display_label", tc.function.name) for tc in message.tool_calls]
            click.echo(f"\n  LLM \u2192 {num_calls} tool{'s' if num_calls != 1 else ''}: {', '.join(chosen)}")
            click.echo()

            for tool_call in message.tool_calls:
                fn_name = tool_call.function.name
                fn_display = action_map.get(fn_name, {}).get("display_label", fn_name)
                try:
                    fn_args = json.loads(tool_call.function.arguments)
                except (json.JSONDecodeError, TypeError):
                    fn_args = {}

                result = _execute_tool_call(
                    fn_name, fn_args, action_map,
                    headers, workspace_id, connection_id,
                    auto_confirm=auto_confirm,
                )

                tool_dur = result.pop("_tool_duration", 0.0)
                resp_bytes = result.pop("_payload_bytes", 0)
                ctx_bytes = result.pop("_context_bytes", 0)
                req_bytes = result.pop("_request_bytes", 0)
                total_tool_time += tool_dur
                status = "err" if result.get("error") else "ok"

                if status == "err":
                    consecutive_errors += 1
                else:
                    consecutive_errors = 0

                cumulative_ctx_bytes += ctx_bytes
                call_log.append((
                    fn_display, turn_in, turn_out, total_input,
                    llm_duration, tool_dur,
                    req_bytes, resp_bytes, cumulative_ctx_bytes, status,
                ))

                eval_log.append({
                    "tool": fn_display,
                    "args": fn_args,
                    "result": result,
                    "status": status,
                })

                result_content = json.dumps(result, default=str)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result_content,
                })

                if consecutive_errors >= max_errors:
                    _diagnose_agent_failure(
                        client, model, prompt_str, tools,
                        fn_display, fn_args, result,
                    )
                    click.echo(f"  \u26d4 Stopping \u2014 {consecutive_errors} consecutive error(s)")
                    break

            # Break outer loop too if max errors reached
            if consecutive_errors >= max_errors:
                break
        else:
            # Log the final LLM call (no tool, just the response)
            call_log.append((
                "llm \u2192 response", turn_in, turn_out, total_input,
                llm_duration, 0.0,
                0, 0, cumulative_ctx_bytes, "ok",
            ))
            _print_agent_summary(call_log, total_input, total_output, total_llm_time, total_tool_time, model)
            return message.content or "", eval_log

    _print_agent_summary(call_log, total_input, total_output, total_llm_time, total_tool_time, model)
    return "Agent reached maximum turns without a final response.", eval_log


# ---------------------------------------------------------------------------
# Extracted helpers for the agent command
# ---------------------------------------------------------------------------

def _discover_agent_tools(
    headers: dict,
    workspace_id: str,
    prompt_str: str,
    connector: Optional[str],
    tool_filter: Optional[str],
    max_tools: int,
    registry: dict,
    verbose: bool = False,
) -> Tuple[list, Dict[str, dict]]:
    """Discover available connectors/tools via the getTools API.

    Returns ``(tool_list, action_map)`` where *tool_list* is the raw list
    of tool dicts from the API and *action_map* maps function names to
    execution metadata (actionId, connectorId, display_label, etc.).
    """
    reg_connectors = registry.get("connectors", {})

    discovery_payload: dict = {
        "input": {
            "limit": max_tools,
            "prompt": prompt_str,
        }
    }
    if workspace_id:
        discovery_payload["input"]["agentId"] = workspace_id
    if connector:
        discovery_payload["input"]["connectorName"] = connector
        if connector in reg_connectors:
            cid = reg_connectors[connector].get("id", "")
            if cid:
                discovery_payload["input"]["connectorId"] = cid
    if tool_filter:
        discovery_payload["input"]["toolName"] = tool_filter

    resp = _verbose_post(GET_TOOLS_URL, headers, discovery_payload)

    if resp.status_code >= 400:
        raise click.ClickException(
            f"Connector discovery failed: {resp.status_code} {resp.text}"
        )

    data = resp.json()
    tool_list = _extract_tool_list(data)
    if not tool_list:
        return [], {}

    action_map = _build_action_map(tool_list, registry)
    return tool_list, action_map


def _run_agent_eval(
    api_key: str,
    model: str,
    prompt_str: str,
    eval_log: list,
    llm_tools: list,
    final_response: str = "",
) -> None:
    """Evaluate whether the agent called the right tools and achieved the task.

    Uses the LLM as a strict QA judge.  Prints the evaluation results and
    a final PASS/FAIL verdict.
    """
    click.echo("  \u2500\u2500 Evaluation \u2500\u2500")
    click.echo()

    # Build a summary of what happened for the judge
    calls_summary = []
    for i, entry in enumerate(eval_log, 1):
        result_preview = json.dumps(entry["result"], default=str)
        if len(result_preview) > 500:
            result_preview = result_preview[:500] + "..."
        calls_summary.append(
            f"  {i}. {entry['tool']}({json.dumps(entry['args'], separators=(', ', ': '))})"
            f"\n     Status: {entry['status']}"
            f"\n     Result: {result_preview}"
        )

    eval_prompt = (
        f"User prompt: \"{prompt_str}\"\n\n"
        f"Available tools: {', '.join(t.get('function', {}).get('name', '?') for t in llm_tools)}\n\n"
        f"Tool calls made:\n" + "\n".join(calls_summary) + "\n\n"
        f"Agent final response: {final_response}\n\n"
        "Evaluate this agent run:\n\n"
        "1. INTENT \u2014 Did the agent understand what the user wanted?\n"
        "2. TOOL SELECTION \u2014 Did it pick the right tool(s) from the available set? Were any calls unnecessary?\n"
        "3. TARGET \u2014 Did it act on the correct resource the user specified? "
        "Extract the target from the user prompt (e.g. a channel, repo, project, file, user, ticket) "
        "and verify the arguments match. "
        "If an ID was used, cross-reference it against any prior list/get/search result in the call history. "
        "If no lookup exists to verify the ID, mark as UNVERIFIED.\n"
        "4. RESULT \u2014 Did the action succeed? Check the result payload for errors or confirmation.\n\n"
        "Rules:\n"
        "- Using a resource name instead of an ID is fine.\n"
        "- A successful call to the WRONG target is a FAIL.\n"
        "- Unnecessary lookup calls (list/get/search) that don't contribute to the task are a FAIL.\n"
        "- If the task required multiple steps (e.g. lookup then act), that's acceptable.\n\n"
        "Then give an overall verdict: PASS or FAIL.\n"
        "PASS = correct tool, correct target, task completed.\n"
        "FAIL = wrong tool, wrong target, task not completed, or unnecessary calls.\n\n"
        "Be concise. End with a single line: VERDICT: PASS or VERDICT: FAIL"
    )

    try:
        import openai
        eval_client = openai.OpenAI(api_key=api_key)
        eval_response = eval_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": (
                    "You are a strict QA evaluator for an AI agent that uses third-party API tools "
                    "(Slack, Jira, GitHub, Google Sheets, etc). "
                    "Judge whether the agent picked the correct tool, targeted the correct resource, "
                    "and accomplished the user's intent. "
                    "Be strict \u2014 wrong target, wrong tool, or unnecessary calls are failures."
                )},
                {"role": "user", "content": eval_prompt},
            ],
        )
        eval_text = eval_response.choices[0].message.content or ""

        # Print eval results
        for line in eval_text.strip().split("\n"):
            click.echo(f"  {line}")

        # Highlight the verdict
        click.echo()
        if "VERDICT: PASS" in eval_text.upper():
            click.echo("  \u2705 PASS")
        elif "VERDICT: FAIL" in eval_text.upper():
            click.echo("  \u274c FAIL")

    except Exception as e:
        click.echo(f"  Evaluation error: {e}")

    click.echo()


def _diagnose_agent_failure(
    client: Any,
    model: str,
    prompt_str: str,
    tools: list,
    fn_display: str,
    fn_args: dict,
    result: dict,
) -> None:
    """Print debug context and ask the LLM to diagnose a repeated tool failure.

    Called when consecutive errors reach the max-error threshold.  Dumps
    the system prompt, user prompt, tool list, failing call details, and
    then asks the LLM for a short diagnosis.
    """
    click.echo()
    click.echo("  \u2500\u2500 Failed Call Debug \u2500\u2500")
    click.echo()
    click.echo("  System Prompt:")
    for line in _AGENT_SYSTEM_PROMPT.split("\n"):
        click.echo(f"    {line}")
    click.echo()
    click.echo("  User Prompt:")
    click.echo(f"    {prompt_str}")
    click.echo()
    click.echo(f"  Tools ({len(tools)}):")
    click.echo(json.dumps(tools, indent=2))
    click.echo()
    click.echo(f"  Failed Call: {fn_display}({json.dumps(fn_args, separators=(', ', ': '))})")
    click.echo(f"  Response: {json.dumps(result, indent=2, default=str)}")
    click.echo()

    # Ask LLM to diagnose the failure
    click.echo("  \u2500\u2500 LLM Diagnosis \u2500\u2500")
    try:
        diag_response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": (
                    "You are a debugging assistant. A tool call failed "
                    "and recovery was attempted but also failed. "
                    "Analyze the errors and suggest how to prevent "
                    "this in future requests. Be concise (3-5 lines max)."
                )},
                {"role": "user", "content": (
                    f"Tool: {fn_display}\n"
                    f"Args: {json.dumps(fn_args, indent=2)}\n"
                    f"Error: {json.dumps(result, indent=2, default=str)}\n"
                    f"Original prompt: {prompt_str}"
                )},
            ],
        )
        diag_text = diag_response.choices[0].message.content or ""
        for line in diag_text.strip().split("\n"):
            click.echo(f"  {line}")
    except Exception:
        click.echo("  (diagnosis unavailable)")
    click.echo()


# ---------------------------------------------------------------------------
# agent command
# ---------------------------------------------------------------------------

@cli.command(
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    ),
)
@click.argument("prompt", nargs=-1, required=True)
@click.option("--connector", default=None, help="Scope discovery to a specific connector")
@click.option("--tool", "tool_filter", default=None, help="Scope discovery to a specific tool")
@click.option("--connection-id", default=None, help="Connection ID for multi-connection connectors")
@click.option("--max-turns", default=_AGENT_MAX_TURNS, type=int, show_default=True,
              help="Maximum agentic loop iterations")
@click.option("-y", "--yes", "skip_confirm", is_flag=True, default=False,
              help="Skip confirmation prompts for tool calls")
@click.option("--eval", "run_eval", is_flag=True, default=False,
              help="Evaluate whether the agent called the right tools and achieved the task")
@click.option("--max-errors", default=2, type=int, show_default=True,
              help="Stop the agent after this many consecutive tool errors")
@click.option("--max-tools", default=5, type=int, show_default=True,
              help="Maximum number of tools to pass to the LLM")
@click.option("--tenant", default=None, help="Tenant ID (overrides config)")
@click.pass_context
def agent(ctx: click.Context, prompt: tuple, connector: Optional[str],
          tool_filter: Optional[str], connection_id: Optional[str],
          max_turns: int, skip_confirm: bool, run_eval: bool,
          max_errors: int, max_tools: int,
          tenant: Optional[str]) -> None:
    """Give a goal in plain English \u2014 the agent thinks, picks the right skills and tools, and executes.

    \b
    Usage:
      fastn agent "Send hello to #general on Slack"
      fastn agent "Get all users" --connector test
      fastn agent "List slack users and send hello to #general"
      fastn agent "Say hey to general" -y
      fastn agent "Say hey to general" --eval

    \b
    The agent discovers available skills and tools, sends them to your
    configured LLM, and executes in a loop until the task is complete.
    It reasons about which skills to load, handles errors, and adapts.
    Use --connector to scope discovery to a specific connector.
    Each tool call requires confirmation by default. Pass -y to skip.
    Pass --eval to evaluate whether the agent did the right thing.

    \b
    First-time setup will prompt you to choose an LLM provider and enter an
    API key. Configuration is saved to .fastn/config.json.
    """
    # Separate prompt words from extra --key value args
    prompt_words = []
    extra_args = []
    found_flag = False
    args_list = list(prompt) + list(ctx.args)

    i = 0
    while i < len(args_list):
        arg = args_list[i]
        if arg.startswith("--"):
            found_flag = True
        if found_flag:
            extra_args.append(arg)
        else:
            prompt_words.append(arg)
        i += 1

    prompt_str = " ".join(prompt_words)
    if not prompt_str.strip():
        raise click.ClickException("Please provide a prompt describing what you want to do.")

    config = load_config()
    if not config.auth_token and not config.api_key:
        raise click.ClickException("Not authenticated. Run `fastn login` first.")

    _ensure_fresh_token(config)

    # Check if LLM is configured — if not, run setup
    if not config.llm_provider or not config.llm_api_key:
        config = _setup_llm_provider(config) or config
        if not config.llm_provider:
            raise click.ClickException(
                "An LLM provider is required for `fastn agent`. "
                "Run `fastn agent` again to configure one."
            )

    if tenant:
        config.tenant_id = tenant

    headers = config.get_headers()
    workspace_id = config.resolve_project_id()

    # Load the local registry for friendly name resolution
    fastn_dir = find_fastn_dir()
    registry = load_registry(fastn_dir)

    provider = config.llm_provider
    api_key = config.llm_api_key
    model = config.llm_model
    if not model:
        from fastn.config import LLM_PROVIDERS
        provider_info = LLM_PROVIDERS.get(provider, {})
        model = provider_info.get("default_model", "")

    # Step 1: Discover ALL active connectors and tools via getTools API
    click.echo()
    click.echo(f"  \u256d\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500")
    click.echo(f"  \u2502  {prompt_str}")
    if tenant:
        click.echo(f"  \u2502  Tenant: {config.tenant_id}  Project: {workspace_id}")
    if connector:
        click.echo(f"  \u2502  Connector: {connector}")
    if tool_filter:
        click.echo(f"  \u2502  Tool: {tool_filter}")
    click.echo(f"  \u2570\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500")
    click.echo()
    click.echo("  Discovering connectors...")

    tool_list, action_map = _discover_agent_tools(
        headers, workspace_id, prompt_str,
        connector, tool_filter, max_tools, registry,
    )
    if not tool_list:
        click.echo("  No tools found. Try rephrasing or use --connector to scope.")
        return

    tool_names = [v["display_label"] for v in action_map.values()]
    click.echo(f"  \u2713 {len(tool_list)} tool{'s' if len(tool_list) != 1 else ''}: {', '.join(tool_names)}")
    click.echo(f"  \u2713 LLM: {provider} ({model})")

    if provider != "openai":
        raise click.ClickException(
            f"Only OpenAI is supported currently. "
            f"Configured provider: {provider}. "
            f"Run `fastn agent` to reconfigure."
        )

    try:
        llm_tools = _convert_tools_for_openai(tool_list)
        result = _agent_loop_openai(
            api_key, model, prompt_str, llm_tools,
            action_map, headers, workspace_id, connection_id,
            max_turns=max_turns, auto_confirm=skip_confirm,
            max_errors=max_errors,
        )
        final_response, eval_log = result
    except click.ClickException:
        raise
    except Exception as e:
        raise click.ClickException(f"Agent error: {e}")

    # Print the final LLM response
    if final_response:
        click.echo()
        click.echo(f"  {final_response}")
        click.echo()

    # ── Evaluation ──
    if run_eval and eval_log:
        _run_agent_eval(api_key, model, prompt_str, eval_log, llm_tools, final_response)
