import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_contact():
    response = client.post("/contacts/", json={
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "janesmith@example.com",
        "phone_number": "987654321",
        "birthday": "1990-05-05"
    })
    assert response.status_code == 200
    assert response.json()["first_name"] == "Jane"
    assert response.json()["email"] == "janesmith@example.com"

# щоб запустити pytest
