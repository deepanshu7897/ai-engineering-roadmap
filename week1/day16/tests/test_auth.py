import uuid


def test_register_user(test_client):
    username = f"pytest_{uuid.uuid4().hex[:8]}"

    response = test_client.post(
        "/auth/register",
        json={
            "username": username,
            "password": "123456",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["username"] == username
    assert "id" in data