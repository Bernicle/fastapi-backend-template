from fastapi.testclient import TestClient
from .....main import app

print(app)
def test_get_items_success():
    with TestClient(app) as client:
        response = client.get("/api/v1/module1/items")  # Assuming your endpoint path
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
