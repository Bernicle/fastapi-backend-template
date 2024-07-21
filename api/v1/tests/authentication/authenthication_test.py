#############################################################################
# Happy Scenario
#############################################################################

from fastapi import Depends
from fastapi.testclient import TestClient
from pydantic import ValidationError
from sqlalchemy.orm import Session
from api.v1.models.module1.user_model import User
from api.v1.schemas.authentication_schema import LoginResponse
from helper.security import hash_password
from config.database  import get_db
from urllib.parse import urlencode

def get_authorization_header(client: TestClient, username: str, password: str) -> dict:
    """Logs in and returns the Authorization header with Bearer token."""
    login_detail = {"username": username, "password": password}
    response = client.post("/api/v1/login", data=urlencode(login_detail).encode("utf-8"), headers={"Content-Type": "application/x-www-form-urlencoded"})
    
    response.raise_for_status()
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_basic_login(test_client):
    
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
    
    response = test_client.post("/api/v1/module1/users", json=pay_load)
    print(response.json())
    
    assert response.status_code == 201, "Failed to Create a new Record/Data."
    created_data = response.json()
    response = test_client.get(f"/api/v1/module1/users/{created_data.get('id')}")
    assert response.status_code == 200, "Failed to get the data. assuming that the data we retrieve is already created."
    retrieve_data = response.json()
    
    created_data_keys = set(created_data.keys())
    retrieve_data_keys = set(retrieve_data.keys())
    
    assert created_data_keys == retrieve_data_keys, "The Keys/Column Name that inserted is not same with created data."

    login_detail = {
        "username":"poncebernard123", 
        "password":"loremIpsum123",
    }
    response = test_client.post("/api/v1/login", data=urlencode(login_detail).encode("utf-8"), headers={"Content-Type": "application/x-www-form-urlencoded"})
    print(response.json())
    assert response.status_code == 200

    #response = test_client.delete(f"/api/v1/module1/users/{created_data.get('id')}")
    #assert response.status_code == 204, "Failed to delete the data."
