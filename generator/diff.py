"""Breaking change detection and migration generation for Fastn connector stubs.

Compares old and new registry data to detect backward-incompatible
changes in connector tools. When breaking changes are found, generates
migration records that the SDK runtime uses to keep old code working
with deprecation warnings.

Migration flow:
    1. `fastn sync` / `fastn add` detects breaking changes via diff_registries()
    2. User confirms the update
    3. build_migrations() generates migration records from the diff
    4. Records are saved to .fastn/migrations.json
    5. At runtime, DynamicConnector reads migrations and auto-maps old
       calling conventions to new ones, emitting deprecation warnings
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Set

from generator.generate import _extract_tool_params


class ChangeType(Enum):
    """Categories of breaking changes."""

    TOOL_REMOVED = "tool_removed"
    TOOL_ADDED = "tool_added"
    PARAM_REMOVED = "param_removed"
    PARAM_ADDED_REQUIRED = "param_added_required"
    PARAM_TYPE_CHANGED = "param_type_changed"
    PARAM_NOW_REQUIRED = "param_now_required"
    PARAM_NOW_OPTIONAL = "param_now_optional"


# Changes that break existing user code
BREAKING_CHANGES: Set[ChangeType] = {
    ChangeType.TOOL_REMOVED,
    ChangeType.PARAM_REMOVED,
    ChangeType.PARAM_ADDED_REQUIRED,
    ChangeType.PARAM_TYPE_CHANGED,
    ChangeType.PARAM_NOW_REQUIRED,
}


@dataclass
class Change:
    """A single detected change."""

    connector: str
    tool: str
    change_type: ChangeType
    detail: str
    breaking: bool = False
    # Extra context for migration generation
    param_name: str = ""
    old_type: str = ""
    new_type: str = ""

    def __post_init__(self) -> None:
        self.breaking = self.change_type in BREAKING_CHANGES

    def __str__(self) -> str:
        icon = "\u26a0" if self.breaking else "\u2022"
        return f"  {icon} {self.connector}.{self.tool}: {self.detail}"


@dataclass
class DiffResult:
    """Summary of all changes detected between old and new registry data."""

    changes: List[Change] = field(default_factory=list)

    @property
    def has_breaking_changes(self) -> bool:
        return any(c.breaking for c in self.changes)

    @property
    def breaking_changes(self) -> List[Change]:
        return [c for c in self.changes if c.breaking]

    @property
    def non_breaking_changes(self) -> List[Change]:
        return [c for c in self.changes if not c.breaking]

    def summary(self) -> str:
        """Human-readable summary for CLI output."""
        if not self.changes:
            return ""

        lines: List[str] = []

        breaking = self.breaking_changes
        if breaking:
            lines.append(f"\u26a0 {len(breaking)} breaking change(s) detected:")
            for c in breaking:
                lines.append(str(c))

        non_breaking = self.non_breaking_changes
        if non_breaking:
            lines.append(f"\u2022 {len(non_breaking)} non-breaking change(s):")
            for c in non_breaking:
                lines.append(str(c))

        return "\n".join(lines)


def _extract_params_map(
    tool_data: Dict[str, Any],
) -> Dict[str, Dict[str, Any]]:
    """Extract tool params as a name -> info dict for easy comparison."""
    params = _extract_tool_params(tool_data)
    return {p["name"]: p for p in params}


def _diff_tool_params(
    connector_name: str,
    tool_name: str,
    old_params: Dict[str, Dict[str, Any]],
    new_params: Dict[str, Dict[str, Any]],
) -> List[Change]:
    """Compare params of a single tool between old and new versions."""
    changes: List[Change] = []

    # Removed params
    for name in old_params:
        if name not in new_params:
            changes.append(Change(
                connector=connector_name,
                tool=tool_name,
                change_type=ChangeType.PARAM_REMOVED,
                detail=f"parameter '{name}' removed",
                param_name=name,
            ))

    # Added or changed params
    for name, new_info in new_params.items():
        if name not in old_params:
            if new_info.get("required", False):
                changes.append(Change(
                    connector=connector_name,
                    tool=tool_name,
                    change_type=ChangeType.PARAM_ADDED_REQUIRED,
                    detail=f"new required parameter '{name}' added",
                    param_name=name,
                    new_type=new_info.get("type", "string"),
                ))
            # Non-breaking: new optional param (no warning needed)
            continue

        old_info = old_params[name]

        # Type changed
        old_type = old_info.get("type", "string")
        new_type = new_info.get("type", "string")
        if old_type != new_type:
            changes.append(Change(
                connector=connector_name,
                tool=tool_name,
                change_type=ChangeType.PARAM_TYPE_CHANGED,
                detail=f"parameter '{name}' type changed: {old_type} \u2192 {new_type}",
                param_name=name,
                old_type=old_type,
                new_type=new_type,
            ))

        # Required status changed
        old_req = old_info.get("required", False)
        new_req = new_info.get("required", False)
        if old_req != new_req:
            if new_req:
                changes.append(Change(
                    connector=connector_name,
                    tool=tool_name,
                    change_type=ChangeType.PARAM_NOW_REQUIRED,
                    detail=f"parameter '{name}' is now required (was optional)",
                    param_name=name,
                ))
            else:
                changes.append(Change(
                    connector=connector_name,
                    tool=tool_name,
                    change_type=ChangeType.PARAM_NOW_OPTIONAL,
                    detail=f"parameter '{name}' is now optional (was required)",
                    param_name=name,
                ))

    return changes


def diff_connector(
    connector_name: str,
    old_connector: Dict[str, Any],
    new_connector: Dict[str, Any],
) -> List[Change]:
    """Compare a single connector between old and new registry versions."""
    changes: List[Change] = []

    old_tools = old_connector.get("tools", {})
    new_tools = new_connector.get("tools", {})

    # Removed tools
    for tool_name in old_tools:
        if tool_name not in new_tools:
            changes.append(Change(
                connector=connector_name,
                tool=tool_name,
                change_type=ChangeType.TOOL_REMOVED,
                detail=f"tool '{tool_name}' removed",
            ))

    # Added tools (non-breaking, informational)
    for tool_name in new_tools:
        if tool_name not in old_tools:
            changes.append(Change(
                connector=connector_name,
                tool=tool_name,
                change_type=ChangeType.TOOL_ADDED,
                detail=f"new tool '{tool_name}' added",
            ))

    # Compare params of tools that exist in both
    for tool_name in old_tools:
        if tool_name in new_tools:
            old_params = _extract_params_map(old_tools[tool_name])
            new_params = _extract_params_map(new_tools[tool_name])
            changes.extend(_diff_tool_params(
                connector_name, tool_name, old_params, new_params,
            ))

    return changes


def diff_registries(
    old_registry: Dict[str, Any],
    new_registry: Dict[str, Any],
    connector_names: Optional[List[str]] = None,
) -> DiffResult:
    """Compare old and new registries, optionally scoped to specific connectors.

    Args:
        old_registry: Previous registry data (from disk).
        new_registry: Updated registry data (from API).
        connector_names: If provided, only compare these connectors.
            If None, compare all connectors present in either registry.

    Returns:
        DiffResult with all detected changes.
    """
    result = DiffResult()

    old_connectors = old_registry.get("connectors", {})
    new_connectors = new_registry.get("connectors", {})

    if connector_names is None:
        connector_names = sorted(
            set(old_connectors.keys()) | set(new_connectors.keys())
        )

    for name in connector_names:
        old_data = old_connectors.get(name)
        new_data = new_connectors.get(name)

        if old_data is None or new_data is None:
            continue

        result.changes.extend(diff_connector(name, old_data, new_data))

    return result


def compute_schema_hash(
    registry: Dict[str, Any],
    connector_name: str,
) -> str:
    """Compute a stable hash of a connector's tool schemas.

    Used to quickly check if anything changed without doing a full diff.
    """
    connectors = registry.get("connectors", {})
    connector_data = connectors.get(connector_name, {})
    tools = connector_data.get("tools", {})

    canonical: Dict[str, Any] = {}
    for tool_name in sorted(tools.keys()):
        tool = tools[tool_name]
        canonical[tool_name] = {
            "actionId": tool.get("actionId", ""),
            "inputSchema": tool.get("inputSchema", {}),
        }

    raw = json.dumps(canonical, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Migration generation
# ---------------------------------------------------------------------------

# Default values used when a new required param is added and the user's
# existing code doesn't provide it.
_TYPE_DEFAULTS: Dict[str, Any] = {
    "string": "",
    "integer": 0,
    "number": 0.0,
    "boolean": False,
    "array": [],
    "object": {},
}


def build_migrations(
    diff_result: DiffResult,
    old_registry: Dict[str, Any],
) -> Dict[str, Any]:
    """Convert breaking changes into a migrations map for runtime compat.

    The returned structure is saved to .fastn/migrations.json and loaded
    by DynamicConnector at runtime.

    Structure:
    {
        "version": 1,
        "created_at": "...",
        "connectors": {
            "slack": {
                "deprecated_tools": {
                    "old_tool_name": {
                        "message": "...",
                        "removed_at": "..."
                    }
                },
                "tools": {
                    "sendmessage": {
                        "deprecated_params": {
                            "old_param": {
                                "action": "removed",
                                "message": "..."
                            }
                        },
                        "param_defaults": {
                            "new_required_param": "default_value"
                        },
                        "type_coercions": {
                            "param_name": {
                                "from": "string",
                                "to": "object",
                                "message": "..."
                            }
                        }
                    }
                }
            }
        }
    }
    """
    now = datetime.now(timezone.utc).isoformat()

    # Start from empty or merge with existing
    migrations: Dict[str, Any] = {
        "version": 1,
        "created_at": now,
        "connectors": {},
    }

    for change in diff_result.breaking_changes:
        conn_name = change.connector
        tool_name = change.tool

        # Ensure connector entry
        if conn_name not in migrations["connectors"]:
            migrations["connectors"][conn_name] = {
                "deprecated_tools": {},
                "tools": {},
            }
        conn_mig = migrations["connectors"][conn_name]

        if change.change_type == ChangeType.TOOL_REMOVED:
            # Keep a record of the removed tool so the SDK can give a
            # helpful error instead of a generic ToolNotFoundError
            old_tools = (
                old_registry.get("connectors", {})
                .get(conn_name, {})
                .get("tools", {})
            )
            old_tool = old_tools.get(tool_name, {})
            conn_mig["deprecated_tools"][tool_name] = {
                "actionId": old_tool.get("actionId", ""),
                "paramKey": _get_param_key_from_tool(old_tool),
                "message": (
                    f"'{conn_name}.{tool_name}()' has been removed. "
                    f"Update your code to use an alternative."
                ),
                "removed_at": now,
            }
            continue

        # Per-tool param migrations
        if tool_name not in conn_mig["tools"]:
            conn_mig["tools"][tool_name] = {
                "deprecated_params": {},
                "param_defaults": {},
                "type_coercions": {},
            }
        tool_mig = conn_mig["tools"][tool_name]

        if change.change_type == ChangeType.PARAM_REMOVED:
            tool_mig["deprecated_params"][change.param_name] = {
                "action": "ignored",
                "message": (
                    f"Parameter '{change.param_name}' in "
                    f"'{conn_name}.{tool_name}()' has been removed. "
                    f"It will be silently ignored. "
                    f"Remove it from your code."
                ),
            }

        elif change.change_type == ChangeType.PARAM_ADDED_REQUIRED:
            default = _TYPE_DEFAULTS.get(change.new_type, "")
            tool_mig["param_defaults"][change.param_name] = {
                "default": default,
                "type": change.new_type,
                "message": (
                    f"'{conn_name}.{tool_name}()' now requires "
                    f"'{change.param_name}' ({change.new_type}). "
                    f"A default value is being used. "
                    f"Update your code to pass it explicitly."
                ),
            }

        elif change.change_type == ChangeType.PARAM_TYPE_CHANGED:
            tool_mig["type_coercions"][change.param_name] = {
                "from": change.old_type,
                "to": change.new_type,
                "message": (
                    f"Parameter '{change.param_name}' in "
                    f"'{conn_name}.{tool_name}()' changed type: "
                    f"{change.old_type} \u2192 {change.new_type}. "
                    f"Update your code to pass the new type."
                ),
            }

        elif change.change_type == ChangeType.PARAM_NOW_REQUIRED:
            tool_mig["param_defaults"][change.param_name] = {
                "default": None,
                "type": "",
                "message": (
                    f"Parameter '{change.param_name}' in "
                    f"'{conn_name}.{tool_name}()' is now required "
                    f"(was optional). Update your code to always pass it."
                ),
            }

    # Clean up empty entries
    for conn_name in list(migrations["connectors"].keys()):
        conn_mig = migrations["connectors"][conn_name]
        for tool_name in list(conn_mig["tools"].keys()):
            tool_mig = conn_mig["tools"][tool_name]
            if not any(tool_mig.values()):
                del conn_mig["tools"][tool_name]
        if not conn_mig["deprecated_tools"] and not conn_mig["tools"]:
            del migrations["connectors"][conn_name]

    return migrations


def merge_migrations(
    existing: Dict[str, Any],
    new: Dict[str, Any],
) -> Dict[str, Any]:
    """Merge new migration records into existing ones.

    New entries overwrite old entries for the same connector/tool/param.
    This handles the case where `fastn sync` is run multiple times.
    """
    if not existing or not existing.get("connectors"):
        return new
    if not new or not new.get("connectors"):
        return existing

    merged = {
        "version": 1,
        "created_at": new.get("created_at", existing.get("created_at", "")),
        "connectors": dict(existing.get("connectors", {})),
    }

    for conn_name, conn_mig in new.get("connectors", {}).items():
        if conn_name not in merged["connectors"]:
            merged["connectors"][conn_name] = conn_mig
            continue

        existing_conn = merged["connectors"][conn_name]

        # Merge deprecated_tools
        existing_conn.setdefault("deprecated_tools", {}).update(
            conn_mig.get("deprecated_tools", {})
        )

        # Merge per-tool migrations
        for tool_name, tool_mig in conn_mig.get("tools", {}).items():
            if tool_name not in existing_conn.setdefault("tools", {}):
                existing_conn["tools"][tool_name] = tool_mig
                continue

            existing_tool = existing_conn["tools"][tool_name]
            existing_tool.setdefault("deprecated_params", {}).update(
                tool_mig.get("deprecated_params", {})
            )
            existing_tool.setdefault("param_defaults", {}).update(
                tool_mig.get("param_defaults", {})
            )
            existing_tool.setdefault("type_coercions", {}).update(
                tool_mig.get("type_coercions", {})
            )

    return merged


def _get_param_key_from_tool(tool_data: Dict[str, Any]) -> str:
    """Extract the wrapper key from a tool's inputSchema."""
    schema = tool_data.get("inputSchema", {})
    props = schema.get("properties", {})
    if props:
        return next(iter(props))
    return "body"
