from __future__ import annotations

import os

from fastapi.testclient import TestClient

from app.main import app


def main() -> None:
    client = TestClient(app)
    api_key = os.getenv("API_KEY", "change-me")
    # health
    r = client.get("/healthz")
    assert r.status_code == 200
    # protected request without key
    r = client.get("/v1/example.yaml")
    assert r.status_code == 401
    # with key
    r = client.get("/v1/example.yaml", headers={"X-API-Key": api_key})
    print("Status:", r.status_code)
    print("Content-Type:", r.headers.get("content-type"))
    print("Body:\n", r.text[:200])


if __name__ == "__main__":
    main()
