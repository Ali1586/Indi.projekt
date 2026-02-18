from src.pom.start_page import StartPage
from src.pom.loan_page import LoanPage



def test_loan_flow(page):
    start = StartPage(page)
    loan = LoanPage(page)

    start.open()
    start.go_to_loan()

    assert loan.is_loaded()
