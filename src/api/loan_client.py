import requests

BASE_URL = "https://souderbroder-loan-lab.lovable.app"

class LoanClient:
    def get_loans(self):
        return requests.get(
            f"{BASE_URL}/api/loans",
            headers={
                "Accept": "application/json"
            }

        )

    def create_loan(self, payload):
        return requests.post(
            f"{BASE_URL}/api/loans",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
