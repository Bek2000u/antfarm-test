from pathlib import Path


DOC_PATH = Path("docs/repo-hygiene.md")


def test_repo_hygiene_doc_exists_and_is_utf8() -> None:
    assert DOC_PATH.exists(), "Expected docs/repo-hygiene.md to exist"
    text = DOC_PATH.read_text(encoding="utf-8")
    assert isinstance(text, str)


def test_repo_hygiene_doc_has_required_headings() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    assert "# Repository Hygiene" in text
    assert "## Ignored Paths" in text
    assert "## Rules" in text


def test_repo_hygiene_doc_has_at_least_three_rules_bullets() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()

    rules_start = lines.index("## Rules") + 1

    rules_section: list[str] = []
    for line in lines[rules_start:]:
        if line.startswith("## "):
            break
        rules_section.append(line)

    bullet_lines = [
        line for line in rules_section if line.strip().startswith("- ") or line.strip().startswith("* ")
    ]
    assert len(bullet_lines) >= 3, "Expected at least 3 bullet-point rules under ## Rules"
