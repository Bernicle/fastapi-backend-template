#############################################################################
# Happy Scenario
#############################################################################

from fastapi.testclient import TestClient
import pytest

from api.v1.tests.authentication.authenthication_test import get_authorization_header


def test_get_user_success(test_client: TestClient):
    #Test account on temp.db
    headers = get_authorization_header(test_client,"poncebernard123", "loremIpsum123")
    #headers = {}
    response = test_client.get("/api/v1/admin/users", headers=headers)
    assert response.status_code == 200, "The expected return status in not 200"
    data = response.json()
    assert isinstance(data, list), "Expected Return Type if in `List`"

