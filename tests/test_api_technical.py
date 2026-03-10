import pytest
from src.api.loan_client import LoanClient
from src.helpers.testdata import loan_payload, loan_payloads_parametrized

client = LoanClient()

def test_get_loans_status():
    assert client.get_loans().status_code == 200

def test_get_loans_content_type():
    assert "application/json" in client.get_loans().headers.get("Content-Type", "")

def test_get_loans_success_true():
    assert client.get_loans().json().get("success") is True

def test_get_loans_contains_loans_key():
    assert "loans" in client.get_loans().json()

def test_get_loans_is_list():
    assert isinstance(client.get_loans().json()["loans"], list)

def test_create_loan_status():
    assert client.create_loan(loan_payload(10000)).status_code in (200, 201)

def test_create_loan_success_true():
    assert client.create_loan(loan_payload(5000)).json().get("success") is True

def test_create_loan_has_id():
    r = client.create_loan(loan_payload(5000)).json()
    assert "id" in r["application"]

def test_create_loan_has_reference_number():
    r = client.create_loan(loan_payload(15000)).json()
    assert "reference_number" in r["application"]

def test_create_loan_status_approved():
    r = client.create_loan(loan_payload(10000)).json()
    assert r["application"]["status"] == "approved"

@pytest.mark.parametrize("payload", loan_payloads_parametrized())
def test_create_loan_amounts(payload):
    r = client.create_loan(payload)
    assert r.status_code in (200, 201)
    assert "id" in r.json()["application"]
