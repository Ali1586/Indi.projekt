# tests/conftest.py
import pytest

@pytest.fixture
def synthetic_user():
    return {
        "pnr": "19121212-1212", # Skatteverkets testnummer
        "name": "Test Testsson"
    }