import pytest
from src.api.loan_client import LoanClient

@pytest.fixture
def api_client():
    """Returnerar en instans av API-klienten för riktiga anrop."""
    # Ersätt med din faktiska Lovable-URL
    return LoanClient("https://souderbroder-loan-lab.lovable.app")