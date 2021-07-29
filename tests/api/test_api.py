def test_should_get_the_api_version_success_code(client):

    response = client.get(
        "/api/version",
        headers={"content-type": "application/json"},
    )

    assert response.status_code == 200


def test_should_return_not_found(client):

    response = client.get("/api/invalid/url")

    assert response.status_code == 404
