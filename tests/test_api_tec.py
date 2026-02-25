from src.api.loan_client import LoanClient

def test_get_loans_business_logic(mocker, mock_api_response):
    # Vi använder fixturen 'mock_api_response' istället för att skapa den här
    mocker.patch(
        "src.api.loan_client.requests.get",
        return_value=mock_api_response
    )

    client = LoanClient()
    response = client.get_loans()

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["amount"] == 5000