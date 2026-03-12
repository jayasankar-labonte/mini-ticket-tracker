import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_ticket():

    response = client.post(
        "/tickets",
        json={
            "title": "Test Ticket",
            "description": "Testing create ticket"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Test Ticket"
    assert data["status"] == "NEW"

def test_get_ticket():

    response = client.get("/tickets/1")

    assert response.status_code in [200, 404]

def test_update_ticket():

    response = client.patch(
        "/tickets/1",
        json={
            "status": "DONE"
        }
    )

    assert response.status_code in [200, 404]

def test_ticket_not_found():

    response = client.get("/tickets/99999")

    assert response.status_code == 404