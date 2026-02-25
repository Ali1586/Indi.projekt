import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_api_response():
    """Fixture som skapar ett standardiserat mock-svar för API:et."""
    mock = Mock()
    mock.status_code = 200
    mock.headers = {"Content-Type": "application/json"}
    mock.json.return_value = [{"id": 1, "amount": 5000, "status": "approved"}]
    return mock