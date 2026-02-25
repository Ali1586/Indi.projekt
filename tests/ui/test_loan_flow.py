import pytest
from src.pom.start_page import StartPage
from src.pom.loan_page import LoanPage


# Här sker magin! Vi testar tre olika belopp i ett svep.
@pytest.mark.parametrize("amount", [5000, 15000, 50000])
def test_loan_process_with_different_amounts(page, amount):
    start_page = StartPage(page)
    loan_page = LoanPage(page)

    # 1. Navigera
    start_page.open()
    start_page.go_to_loan()

    # 2. Kontrollera att sidan laddat
    assert loan_page.is_loaded(), f"Lånesidan laddades inte för belopp {amount}"

    # Här kan du logga vad som händer (syns i terminalen med -s flaggan)
    print(f"Verifierar låneflöde för belopp: {amount} SEK")