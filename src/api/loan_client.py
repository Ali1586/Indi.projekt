import requests

BASE_URL = "https://kzmcpfklrqymzazaxlmv.supabase.co/functions/v1/partner-loan-api"
API_KEY = "0ae0909526eb8f6563dfac7e6b3a7523aa68bdac57fa7590aae3c9762a99ff25"

class LoanClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "x-api-key": API_KEY,
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def get_loans(self):
        return self.session.get(f"{self.base_url}/loans")

    def get_loan(self, loan_id):
        return self.session.get(f"{self.base_url}/loans/{loan_id}")

    def create_loan(self, payload):
        return self.session.post(f"{self.base_url}/loans", json=payload)

    def delete_loan(self, loan_id):
        return self.session.delete(f"{self.base_url}/loans/{loan_id}")
