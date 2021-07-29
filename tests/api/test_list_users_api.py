import mock


@mock.patch("services.users.list_users")
def test_should_return_an_empty_user_list(users_mock, client):
    users_mock.return_value = []

    response = client.get("/api/users")

    assert response.status_code == 200
    assert response.json == []


@mock.patch("services.users.list_users")
def test_should_list_all_users(users_mock, client):
    users_list_mock = [
        {
            "avatar": "https://my-avatar.png",
            "created_at": "2021-07-29T20:28:42.429307+00:00",
            "email": "j@abc.com",
            "id": 1,
            "name": "John",
        },
    ]
    users_mock.return_value = users_list_mock

    response = client.get("/api/users")

    assert response.json == users_list_mock
