import pytest

def test_signup(client):
    response = client.post(
        "/users/signup", json={"email": "test1@example.com", "password": "password"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "test1@example.com"

def test_login(client):
    response = client.post(
        "/users/login", json={"email": "test@example.com", "password": "password"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
