import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert data["app"] == "EduGenie"


def test_explain_requires_topic(client):
    response = client.post("/api/explain", json={})
    assert response.status_code == 400


def test_qna_requires_question(client):
    response = client.post("/api/qna", json={})
    assert response.status_code == 400
