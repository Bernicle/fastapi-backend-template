
def test_get_items_success(test_client):
    response = test_client.get("/api/v1/module1/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_basic_register(test_client):
    response = test_client.get("/api/v1/module1/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

