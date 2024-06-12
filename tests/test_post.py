import pytest

def test_create_post(client):
    login_response = client.post(
        "/users/login", json={"email": "test@example.com", "password": "password"}
    )
    token = login_response.json()["access_token"]
    response = client.post(
        "/posts/", json={"text": "Hello, World!"}, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["text"] == "Hello, World!"

def test_get_posts(client):
    login_response = client.post(
        "/users/login", json={"email": "test@example.com", "password": "password"}
    )
    token = login_response.json()["access_token"]
    response = client.get("/posts/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
import pytest

def test_create_post(client):
    login_response = client.post(
        "/users/login", json={"email": "test@example.com", "password": "password"}
    )
    token = login_response.json()["access_token"]
    response = client.post(
        "/posts/", json={"text": "Hello, World!"}, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["text"] == "Hello, World!"

def test_get_posts(client):
    login_response = client.post(
        "/users/login", json={"email": "test@example.com", "password": "password"}
    )
    token = login_response.json()["access_token"]
    response = client.get("/posts/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
