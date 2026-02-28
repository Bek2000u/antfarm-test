from pathlib import Path


def test_ci_workflow_contains_expected_baseline_steps() -> None:
    workflow = Path('.github/workflows/ci.yml')
    assert workflow.exists()

    content = workflow.read_text(encoding='utf-8')

    assert 'pull_request:' in content
    assert 'push:' in content
    assert "github.event.repository.default_branch" in content
    assert "python-version: '3.12'" in content
    assert 'python -m pip install pytest' in content
    assert 'pytest -q' in content
