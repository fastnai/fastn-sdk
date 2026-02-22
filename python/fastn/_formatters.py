"""LLM tool format converters for OpenAI, Anthropic, Gemini, and Bedrock."""

from __future__ import annotations

from typing import Any, Dict, List


def _unwrap_input_schema(schema: Dict[str, Any]) -> Dict[str, Any]:
    """Unwrap a single wrapper key (body/param/query) from an inputSchema.

    Fastn schemas wrap params under a top-level key like ``body``.  LLMs
    expect a flat object schema with the actual fields, so we unwrap one
    level when the schema has a single object property.
    """
    props = schema.get("properties", {})
    if len(props) == 1:
        wrapper = next(iter(props.values()))
        if isinstance(wrapper, dict) and wrapper.get("type") == "object":
            return {
                "type": "object",
                "properties": wrapper.get("properties", {}),
                "required": wrapper.get("required", []),
            }
    # Already flat or has multiple top-level keys — return as-is
    return schema


def _format_actions(
    actions: List[Dict[str, Any]],
    wrapper_fn,
) -> List[Dict[str, Any]]:
    """Format a list of actions using a provider-specific wrapper function."""
    result = []
    for action in actions:
        params = _unwrap_input_schema(action.get("inputSchema", {}))
        result.append(wrapper_fn(action["name"], action.get("description", ""), params))
    return result


def _wrap_openai(name: str, desc: str, params: dict) -> dict:
    return {"type": "function", "function": {"name": name, "description": desc, "parameters": params}}


def _wrap_anthropic(name: str, desc: str, params: dict) -> dict:
    return {"name": name, "description": desc, "input_schema": params}


def _wrap_gemini(name: str, desc: str, params: dict) -> dict:
    return {"name": name, "description": desc, "parameters": params}


def _wrap_bedrock(name: str, desc: str, params: dict) -> dict:
    return {"toolSpec": {"name": name, "description": desc, "inputSchema": {"json": params}}}


_FORMAT_CONVERTERS = {
    "openai": lambda actions: _format_actions(actions, _wrap_openai),
    "anthropic": lambda actions: _format_actions(actions, _wrap_anthropic),
    "gemini": lambda actions: _format_actions(actions, _wrap_gemini),
    "bedrock": lambda actions: _format_actions(actions, _wrap_bedrock),
}
