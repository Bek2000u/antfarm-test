from pathlib import Path


def test_readme_ci_section_documents_baseline_workflow() -> None:
    readme = Path('README.md')
    assert readme.exists()

    content = readme.read_text(encoding='utf-8')

    assert '## CI' in content
    assert '.github/workflows/ci.yml' in content
    assert 'pull requests' in content
    assert 'pushes to the default branch' in content
    assert 'Python 3.12' in content
    assert '`pytest -q`' in content
