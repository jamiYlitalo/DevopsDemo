from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_validate_positive_value():
    payload = {
        "name": "sensor-01",
        "value": 10.5,
        "metadata": {"unit": "C"}
    }
    response = client.post("/validate", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Payload is valid."


def test_validate_negative_value():
    payload = {
        "name": "sensor-02",
        "value": -1,
        "metadata": {}
    }
    response = client.post("/validate", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Value must be non-negative."
