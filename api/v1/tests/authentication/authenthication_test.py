#############################################################################
# Happy Scenario
#############################################################################

from fastapi import Depends
from fastapi.testclient import TestClient
from pydantic import ValidationError
from sqlalchemy.orm import Session
from api.v1.models.admin.user_model import User
from api.v1.schemas.authentication_schema import LoginResponse
from api.v1.services.admin.user_service import UserService, get_user_service
from helper.security import hash_password
from config.database  import get_db
from urllib.parse import urlencode

def get_authorization_header(client: TestClient, username: str, password: str) -> dict:
    """Logs in and returns the Authorization header with Bearer token."""
    login_detail = {"username": username, "password": password}
    response = client.post("/api/v1/login", content=urlencode(query=login_detail).encode("utf-8"), headers={"Content-Type": "application/x-www-form-urlencoded"})
    
    response.raise_for_status()
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_basic_login(test_client: TestClient):
    #Since during conftest.py, the Initialization of Database is Redirect to temp.db, We will create a default use that we will use for every authentication in the system during testing.
    pay_load = {
        "username":"poncebernard123",
        "password":"loremIpsum123",
        "first_name":"Bernard",
        "middle_name":None,
        "last_name":"Ponce",
        "extension_name": None,
        "address": None,
        "mobile_number":"09189911991"
    }
    user_service : UserService = next(get_user_service(next(get_db())))

    existing_user = user_service.are_keys_taken(pay_load["mobile_number"], pay_load["username"])
    if (not existing_user):
        user_service.create_user(pay_load)
    
    login_detail = {
        "username":"poncebernard123", 
        "password":"loremIpsum123",
    }
    response = test_client.post("/api/v1/login", content=urlencode(login_detail).encode("utf-8"), headers={"Content-Type": "application/x-www-form-urlencoded"})
    print(response.json())
    assert response.status_code == 200

    #response = test_client.delete(f"/api/v1/admin/users/{created_data.get('id')}")
    #assert response.status_code == 204, "Failed to delete the data."
