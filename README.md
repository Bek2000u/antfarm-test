# AntFarm Test

## CI

GitHub Actions runs a minimal pytest baseline on every pull request and on pushes, with the job gated to execute only for the repository default branch on push events. The workflow uses Python 3.12, installs `pytest`, and runs `pytest -q` from the repository root.
