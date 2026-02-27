from pathlib import Path


def _gitignore_lines() -> set[str]:
    text = Path('.gitignore').read_text(encoding='utf-8')
    return {line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith('#')}


def test_gitignore_contains_progress_and_python_patterns() -> None:
    lines = _gitignore_lines()

    required_patterns = {
        'progress-*.txt',
        '__pycache__/',
        '*.py[cod]',
        '.pytest_cache/',
        '.mypy_cache/',
        '.venv/',
    }

    missing = sorted(required_patterns - lines)
    assert not missing, f'Missing .gitignore patterns: {missing}'
