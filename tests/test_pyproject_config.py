from pathlib import Path
import tomllib


def test_pyproject_has_required_sections() -> None:
    pyproject_path = Path(__file__).resolve().parents[1] / "pyproject.toml"
    data = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

    assert "project" in data
    assert "tool" in data
    assert "pytest" in data["tool"]
    assert "mypy" in data["tool"]


def test_project_dependencies_match_requirements() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    pyproject = tomllib.loads((repo_root / "pyproject.toml").read_text(encoding="utf-8"))
    requirements = [
        line.strip()
        for line in (repo_root / "requirements.txt").read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]

    assert pyproject["project"]["dependencies"] == requirements


def test_pytest_and_mypy_config_values() -> None:
    pyproject = tomllib.loads(
        (Path(__file__).resolve().parents[1] / "pyproject.toml").read_text(encoding="utf-8")
    )

    assert pyproject["tool"]["pytest"]["ini_options"]["testpaths"] == ["."]
    assert pyproject["tool"]["mypy"]["strict"] is False
    assert pyproject["tool"]["mypy"]["python_version"] == "3.12"
