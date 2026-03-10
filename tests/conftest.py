import pytest
from src.api.loan_client import LoanClient
from src.helpers.testdata import loan_payload

@pytest.fixture(scope="session")
def api_client():
    return LoanClient()

@pytest.fixture
def default_loan_payload():
    return loan_payload()
