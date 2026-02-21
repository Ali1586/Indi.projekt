import os
import requests
from dotenv import load_dotenv

load_dotenv()


class LoanClient:
    def __init__(self):
        # Hämtar nyckeln och sätter bas-URL
        self.api_key = os.getenv("API_KEY_PRIMARY")
        if not self.api_key:
            # Reserv om .env inte laddas
            self.api_key = "0ae0909526eb8f6563dfac7e6b3a7523aa68bdac57fa7590aae3c9762a99ff25"

        self.base_url = "https://souderbroder-loan-lab.lovable.app/api"

    # Se till att denna rad börjar på samma nivå som def __init__
    def get_loans(self):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        }
        response = requests.get(f"{self.base_url}/loans", headers=headers)
        return response