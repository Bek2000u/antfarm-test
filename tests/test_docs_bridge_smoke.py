from pathlib import Path


DOC_PATH = Path("docs/opengoat-antfarm-bridge-smoke.md")


def test_bridge_smoke_doc_exists_and_utf8() -> None:
    assert DOC_PATH.exists(), "Expected bridge smoke doc to exist"
    DOC_PATH.read_text(encoding="utf-8")


def test_bridge_smoke_doc_has_required_headings() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()

    top_level = next((line for line in lines if line.startswith("# ")), "")
    assert "OpenGoat" in top_level and "Bridge" in top_level

    assert "## Overview" in text
    assert "## Bridge Smoke Test Description" in text
    assert "## Acceptance Checklist" in text


def test_bridge_smoke_doc_has_checklist_items() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")
    checklist_items = [line for line in text.splitlines() if line.startswith("- [ ]")]
    assert len(checklist_items) >= 3
