"""Tests for _detect_languages() — SDK language detection for stub generation."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from fastn.cli._registry import _detect_languages


@pytest.fixture
def fastn_dir(tmp_path: Path) -> Path:
    """Create a .fastn directory inside a temporary project root."""
    d = tmp_path / ".fastn"
    d.mkdir()
    return d


class TestDetectLanguages:
    """Tests for _detect_languages()."""

    def test_returns_python_when_importable(self, fastn_dir: Path) -> None:
        """Should detect Python when the fastn package is importable."""
        # fastn is importable in the test environment
        result = _detect_languages(fastn_dir)
        assert "python" in result

    def test_returns_python_only_when_no_package_json(self, fastn_dir: Path) -> None:
        """Should return only Python when no package.json exists."""
        result = _detect_languages(fastn_dir)
        assert result == ["python"]

    @patch.dict("sys.modules", {"fastn": None})
    def test_returns_empty_when_fastn_not_importable(self, fastn_dir: Path) -> None:
        """Should return empty list when fastn is not importable and no package.json."""
        # Patching sys.modules to make `import fastn` raise ImportError
        with patch("builtins.__import__", side_effect=_import_blocker("fastn")):
            result = _detect_languages(fastn_dir)
        assert result == []

    def test_detects_typescript_from_package_json(self, fastn_dir: Path) -> None:
        """Should detect TypeScript when package.json has @fastn/sdk dependency."""
        project_root = fastn_dir.parent
        pkg = {"dependencies": {"@fastn/sdk": "^1.0.0"}}
        (project_root / "package.json").write_text(json.dumps(pkg))

        result = _detect_languages(fastn_dir)
        assert "python" in result
        assert "typescript" in result

    def test_detects_typescript_from_dev_dependencies(self, fastn_dir: Path) -> None:
        """Should detect TypeScript when @fastn/sdk is in devDependencies."""
        project_root = fastn_dir.parent
        pkg = {"devDependencies": {"@fastn/sdk": "^1.0.0"}}
        (project_root / "package.json").write_text(json.dumps(pkg))

        result = _detect_languages(fastn_dir)
        assert "typescript" in result

    def test_detects_typescript_from_fastn_npm_package(self, fastn_dir: Path) -> None:
        """Should detect TypeScript when package.json has 'fastn' (not @fastn/sdk) dep."""
        project_root = fastn_dir.parent
        pkg = {"dependencies": {"fastn": "^1.0.0"}}
        (project_root / "package.json").write_text(json.dumps(pkg))

        result = _detect_languages(fastn_dir)
        assert "typescript" in result

    def test_no_typescript_when_package_json_has_no_fastn(self, fastn_dir: Path) -> None:
        """Should not detect TypeScript when package.json doesn't have fastn deps."""
        project_root = fastn_dir.parent
        pkg = {"dependencies": {"express": "^4.0.0"}}
        (project_root / "package.json").write_text(json.dumps(pkg))

        result = _detect_languages(fastn_dir)
        assert "typescript" not in result

    def test_handles_malformed_package_json(self, fastn_dir: Path) -> None:
        """Should handle malformed package.json gracefully (no crash)."""
        project_root = fastn_dir.parent
        (project_root / "package.json").write_text("not valid json {{{")

        result = _detect_languages(fastn_dir)
        # Should still detect Python, just skip TypeScript
        assert "python" in result
        assert "typescript" not in result

    def test_handles_empty_package_json(self, fastn_dir: Path) -> None:
        """Should handle empty package.json (no dependencies key)."""
        project_root = fastn_dir.parent
        (project_root / "package.json").write_text("{}")

        result = _detect_languages(fastn_dir)
        assert "typescript" not in result

    def test_both_python_and_typescript(self, fastn_dir: Path) -> None:
        """Should return both languages when both are present."""
        project_root = fastn_dir.parent
        pkg = {"dependencies": {"@fastn/sdk": "^1.0.0", "express": "^4.0.0"}}
        (project_root / "package.json").write_text(json.dumps(pkg))

        result = _detect_languages(fastn_dir)
        assert result == ["python", "typescript"]

    def test_order_is_python_first(self, fastn_dir: Path) -> None:
        """Python should always come before TypeScript in the result."""
        project_root = fastn_dir.parent
        pkg = {"dependencies": {"@fastn/sdk": "^1.0.0"}}
        (project_root / "package.json").write_text(json.dumps(pkg))

        result = _detect_languages(fastn_dir)
        python_idx = result.index("python")
        ts_idx = result.index("typescript")
        assert python_idx < ts_idx


def _import_blocker(blocked_module: str):
    """Create an import function that blocks a specific module."""
    real_import = __builtins__.__import__ if hasattr(__builtins__, "__import__") else __import__

    def _blocked_import(name, *args, **kwargs):
        if name == blocked_module:
            raise ImportError(f"Blocked: {name}")
        return real_import(name, *args, **kwargs)

    return _blocked_import
