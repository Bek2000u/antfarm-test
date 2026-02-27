from pathlib import Path
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from main import app

client = TestClient(app)


def test_get_root_returns_200() -> None:
    response = client.get("/")

    assert response.status_code == 200


def test_get_root_returns_expected_message() -> None:
    response = client.get("/")

    assert response.json() == {"message": "hello world"}
