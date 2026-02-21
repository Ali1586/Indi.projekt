from src.api.loan_client import LoanClient


def test_get_loans_business_logic(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.headers = {"Content-Type": "application/json"}
    mock_response.json.return_value = []

    mocker.patch(
        "src.api.loan_client.requests.get",
        return_value=mock_response
    )

    client = LoanClient()
    response = client.get_loans()

    assert response.status_code == 200
    assert isinstance(response.json(), list)