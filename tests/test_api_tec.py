from src.api.loan_client import LoanClient

def test_get_loans_status_and_endpoint():
    client = LoanClient()
    response = client.get_loans()

    assert response.status_code == 200
    assert response.url.endswith("/api/loans")
