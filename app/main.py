from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Any, Dict
import time

app = FastAPI(
    title="Automation-Driven API",
    version="1.0.0",
    description=(
        "A minimal FastAPI service used to demonstrate CI/CD, testing, "
        "and DevOps automation."
    ),
)

# -----------------------------
# Models
# -----------------------------


class Payload(BaseModel):
    name: str = Field(..., example="sensor-01")
    value: float = Field(..., example=42.7)
    metadata: Dict[str, Any] = Field(default_factory=dict)


# -----------------------------
# Routes
# -----------------------------

@app.get("/health")
def health_check():
    """
    Basic health endpoint used for uptime checks.
    """
    return {"status": "ok", "timestamp": time.time()}


@app.post("/validate")
def validate_payload(payload: Payload):
    """
    Validates incoming JSON payloads.
    Demonstrates automation-style input validation.
    """
    if payload.value < 0:
        raise HTTPException(
            status_code=400, detail="Value must be non-negative."
        )

    return {
        "message": "Payload is valid.",
        "payload": payload.dict()
    }


@app.get("/metrics")
def metrics():
    """
    Simple metrics endpoint.
    In a real deployment, you could integrate Prometheus here.
    """
    return {
        "uptime_seconds": time.process_time(),
        "requests_example": 123  # placeholder metric
    }
