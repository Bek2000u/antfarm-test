# Repository Hygiene

Quick reference for keeping this repository clean and safe.

## Ignored Paths

The `.gitignore` excludes local/runtime artifacts so commits stay portable and reviewable:

- `progress-*.txt` for local workflow progress artifacts
- Python caches such as `__pycache__/`, `*.py[cod]`, `.pytest_cache/`, and `.mypy_cache/`
- Local virtual environments such as `.venv/`, `venv/`, and `env/`

## Rules

- Never commit progress files or other local run artifacts.
- Keep virtual environments local and out of version control.
- Never commit secrets (for example `.env`, `*.key`, `*.pem`, `*.secret`).
