# tests/conftest.py
import pytest
from app import create_app
from app.config import TestingConfig

@pytest.fixture(scope='module')
def app():
    """
    Creates a test instance of the application.
    """
    app = create_app(TestingConfig)
    return app

@pytest.fixture(scope='module')
def client(app):
    """
    Provides a test client for the application.
    """
    return app.test_client()

# If you need fixtures for application context or database, they can also be defined here.
