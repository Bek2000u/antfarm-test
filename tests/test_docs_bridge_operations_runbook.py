from pathlib import Path


DOC_PATH = Path("docs/bridge-operations-runbook.md")


REQUIRED_HEADINGS = [
    "# Bridge Operations Runbook",
    "## Overview",
    "## Normal Flow",
    "## Failure Modes",
    "## Manual Recovery Commands",
    "## Rollback",
]


def test_bridge_operations_runbook_exists_and_is_utf8() -> None:
    assert DOC_PATH.exists(), "Expected docs/bridge-operations-runbook.md to exist"

    content = DOC_PATH.read_text(encoding="utf-8")
    assert content.strip(), "Runbook should not be empty"


def test_bridge_operations_runbook_contains_required_headings() -> None:
    content = DOC_PATH.read_text(encoding="utf-8")

    for heading in REQUIRED_HEADINGS:
        assert heading in content, f"Missing required heading: {heading}"
