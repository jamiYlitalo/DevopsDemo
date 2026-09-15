from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_full_flow():
    # Health
    health = client.get("/health")
    assert health.status_code == 200

    # Validate
    payload = {"name": "sensor-x", "value": 5, "metadata": {}}
    validate = client.post("/validate", json=payload)
    assert validate.status_code == 200

    # Metrics
    metrics = client.get("/metrics")
    assert metrics.status_code == 200
