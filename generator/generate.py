"""Fastn SDK Stub Generator.

Reads connector definitions from the Fastn registry API and generates
type stubs (.pyi for Python, .d.ts for TypeScript) for IDE autocomplete.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

from jinja2 import Environment, FileSystemLoader


TEMPLATES_DIR = Path(__file__).parent / "templates"

TYPE_MAP_PYTHON = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "array": "List[Any]",
    "object": "Dict[str, Any]",
}

TYPE_MAP_TYPESCRIPT = {
    "string": "string",
    "integer": "number",
    "number": "number",
    "boolean": "boolean",
    "array": "any[]",
    "object": "Record<string, any>",
}


def _sanitize_identifier(name: str) -> str:
    """Convert a name to a valid Python/TS identifier."""
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    if name and name[0].isdigit():
        name = "_" + name
    return name


def _to_camel_case(snake_str: str) -> str:
    """Convert snake_case to camelCase for TypeScript."""
    parts = snake_str.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


def _to_pascal_case(snake_str: str) -> str:
    """Convert snake_case to PascalCase."""
    return "".join(p.capitalize() for p in snake_str.split("_"))


def _map_type(param_type: str, language: str) -> str:
    """Map a registry type string to the target language type."""
    type_map = TYPE_MAP_PYTHON if language == "python" else TYPE_MAP_TYPESCRIPT
    return type_map.get(param_type, "Any" if language == "python" else "any")


def _extract_tool_params(tool_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Extract the inner user-facing params from a tool's inputSchema.

    The inputSchema has a top-level wrapper key (e.g., "body" or "param")
    whose properties are the actual parameters the user passes as kwargs.
    We extract those inner properties so stubs match the SDK calling convention:

        # Registry inputSchema structure:
        # { "properties": { "param": { "properties": { "email": {...} }, "required": ["email"] } } }
        #
        # SDK usage:  fastn.slack.getuserbyemail(email="khalid@fastn.ai")
        # Stub:       def getuserbyemail(self, email: str) -> Dict[str, Any]: ...
    """
    params: List[Dict[str, Any]] = []
    input_schema = tool_data.get("inputSchema", {})
    schema_props = input_schema.get("properties", {})

    if not schema_props:
        # Fallback: use legacy "params" field if no inputSchema
        raw_params = tool_data.get("params", {})
        for param_name, param_info in sorted(raw_params.items()):
            safe_param_name = _sanitize_identifier(param_name)
            params.append({
                "name": safe_param_name,
                "camel_name": _to_camel_case(safe_param_name),
                "type": param_info.get("type", "string"),
                "required": param_info.get("required", False),
                "description": param_info.get("description", ""),
            })
        return params

    # Get the first (and usually only) top-level property — the wrapper key
    # e.g., "param", "body", "query"
    wrapper_key = next(iter(schema_props), None)
    if wrapper_key is None:
        return params

    wrapper_schema = schema_props[wrapper_key]
    inner_props = wrapper_schema.get("properties", {})
    inner_required = set(wrapper_schema.get("required", []))

    for param_name, param_info in sorted(inner_props.items()):
        safe_param_name = _sanitize_identifier(param_name)
        params.append({
            "name": safe_param_name,
            "camel_name": _to_camel_case(safe_param_name),
            "type": param_info.get("type", "string"),
            "required": param_name in inner_required,
            "description": param_info.get("description", ""),
        })

    return params


def parse_registry(registry_data: Dict[str, Any]) -> Dict[str, Any]:
    """Parse raw registry JSON into a normalized structure for templates.

    Returns a dict with:
        version: str
        connectors: list of connector dicts, each with:
            name: str (snake_case identifier)
            display_name: str
            category: str
            class_name: str (PascalCase)
            tools: list of tool dicts
    """
    connectors = []
    raw_connectors = registry_data.get("connectors", {})

    for connector_name, connector_data in sorted(raw_connectors.items()):
        safe_name = _sanitize_identifier(connector_name)
        tools = []
        raw_tools = connector_data.get("tools", {})

        for tool_name, tool_data in sorted(raw_tools.items()):
            safe_tool_name = _sanitize_identifier(tool_name)
            params = _extract_tool_params(tool_data)

            # Sort: required params first, then optional
            params.sort(key=lambda p: (not p["required"], p["name"]))

            tools.append({
                "name": safe_tool_name,
                "camel_name": _to_camel_case(safe_tool_name),
                "action_id": tool_data.get("actionId", ""),
                "description": tool_data.get("description", ""),
                "params": params,
            })

        connectors.append({
            "name": safe_name,
            "display_name": connector_data.get("display_name", connector_name),
            "category": connector_data.get("category", ""),
            "class_name": _to_pascal_case(safe_name) + "Connector",
            "tools": tools,
            "tool_count": len(tools),
        })

    return {
        "version": registry_data.get("version", "unknown"),
        "connectors": connectors,
    }


def parse_connector(
    connector_name: str, connector_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Parse a single connector's data into normalized form."""
    registry = {
        "version": "",
        "connectors": {connector_name: connector_data},
    }
    parsed = parse_registry(registry)
    if parsed["connectors"]:
        return parsed["connectors"][0]
    return {}


class StubGenerator:
    """Generates type stub files from Fastn registry data."""

    def __init__(self, language: str = "python") -> None:
        if language not in ("python", "typescript"):
            raise ValueError(f"Unsupported language: {language}")
        self.language = language
        template_dir = TEMPLATES_DIR / language
        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )
        self.env.filters["map_type"] = lambda t: _map_type(t, language)
        self.env.filters["camel_case"] = _to_camel_case
        self.env.filters["pascal_case"] = _to_pascal_case

    def generate_index(
        self,
        all_connectors: List[Dict[str, Any]],
        installed_connectors: List[str],
    ) -> str:
        """Generate the root index stub (index.pyi or index.d.ts)."""
        ext = "pyi" if self.language == "python" else "d.ts"
        template = self.env.get_template(f"index.{ext}.j2")
        return template.render(
            connectors=all_connectors,
            installed=installed_connectors,
        )

    def generate_connector(self, connector: Dict[str, Any]) -> str:
        """Generate a full connector stub file."""
        ext = "pyi" if self.language == "python" else "d.ts"
        template = self.env.get_template(f"connector.{ext}.j2")
        return template.render(connector=connector)

    def generate_placeholder(
        self, connectors: List[Dict[str, Any]]
    ) -> str:
        """Generate placeholder stubs for non-installed connectors."""
        ext = "pyi" if self.language == "python" else "d.ts"
        template = self.env.get_template(f"placeholder.{ext}.j2")
        return template.render(connectors=connectors)

    def generate_all(
        self,
        registry_data: Dict[str, Any],
        installed_connectors: List[str],
        output_dir: str,
    ) -> List[str]:
        """Generate all stub files and write them to output_dir.

        Returns list of generated file paths.
        """
        parsed = parse_registry(registry_data)
        all_connectors = parsed["connectors"]
        generated_files: List[str] = []

        output_path = Path(output_dir)

        # For Python, put stubs inside a fastn/ package directory
        # so Pylance resolves them via stubPath setting.
        if self.language == "python":
            stub_root = output_path / "fastn"
        else:
            stub_root = output_path

        connectors_dir = stub_root / "connectors"
        connectors_dir.mkdir(parents=True, exist_ok=True)

        # Generate index
        ext = "pyi" if self.language == "python" else "d.ts"
        index_content = self.generate_index(all_connectors, installed_connectors)
        index_file = stub_root / f"__init__.{ext}" if self.language == "python" else output_path / f"index.{ext}"
        index_file.write_text(index_content)
        generated_files.append(str(index_file))

        # Generate per-connector stubs for installed connectors
        installed_set = set(installed_connectors)
        placeholder_connectors = []

        for connector in all_connectors:
            if connector["name"] in installed_set:
                content = self.generate_connector(connector)
                filename = f"{connector['name']}.{ext}"
                filepath = connectors_dir / filename
                filepath.write_text(content)
                generated_files.append(str(filepath))
            else:
                placeholder_connectors.append(connector)

        # Generate placeholder file
        if placeholder_connectors:
            placeholder_content = self.generate_placeholder(placeholder_connectors)
            placeholder_file = connectors_dir / f"_placeholders.{ext}"
            placeholder_file.write_text(placeholder_content)
            generated_files.append(str(placeholder_file))

        # For Python, add __init__.pyi to connectors/ so it's a package
        if self.language == "python":
            connectors_init = connectors_dir / "__init__.pyi"
            if not connectors_init.exists():
                connectors_init.write_text("")
                generated_files.append(str(connectors_init))

        return generated_files


def generate_stubs(
    registry_data: Dict[str, Any],
    installed_connectors: List[str],
    output_dir: str,
    language: str = "python",
) -> List[str]:
    """Convenience function to generate stubs.

    Args:
        registry_data: Full registry JSON from the API.
        installed_connectors: List of connector names the user has added.
        output_dir: Directory to write stub files to.
        language: 'python' or 'typescript'.

    Returns:
        List of generated file paths.
    """
    generator = StubGenerator(language=language)
    return generator.generate_all(registry_data, installed_connectors, output_dir)
