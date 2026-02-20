"""Auto-apply the 'sdk' marker to all tests in tests/sdk/."""

from pathlib import Path

import pytest

_THIS_DIR = str(Path(__file__).resolve().parent)


def pytest_collection_modifyitems(items):
    for item in items:
        if str(Path(item.fspath).resolve()).startswith(_THIS_DIR):
            item.add_marker(pytest.mark.sdk)
