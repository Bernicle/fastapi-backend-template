# Initialize the Database First Before anything else.
from config.database import initialize_setup
initialize_setup("sqlite:///temp.db")

from faker import Faker
import faker_commerce

import pytest
from main import app  # Import the FastAPI app
from fastapi.testclient import TestClient
import sys, os
sys.path.insert(1,os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def test_app():
    yield app  # Provide the app fixture for tests

@pytest.fixture
def test_client(test_app):
    with  TestClient(test_app) as client:
        yield client  # Provide a test client fixture

@pytest.fixture
def test_faker():
    fake = Faker()
    fake.add_provider(faker_commerce.Provider)
    yield fake
    