import pytest
from faker import Faker
from src.pom.start_page import StartPage
from src.pom.loan_page import LoanPage
from src.pom.income_page import IncomePage
from src.pom.result_page import ResultPage
from src.pom.contact_page import ContactPage

fake = Faker("sv_SE")
SSN = "196408233234"


def test_start_page_loads(page):
    start = StartPage(page)
    start.open()
    assert start.is_loaded()


def test_contact_page_loads(page):
    contact = ContactPage(page)
    contact.open()
    assert contact.is_loaded()


def test_full_loan_flow(page):
    start = StartPage(page)
    start.open()
    start.select_loan_type_and_continue("Bil")

    loan = LoanPage(page)
    assert loan.is_loaded()
    loan.fill(SSN, "Test", "Person", fake.email())
    loan.click_next()

    income = IncomePage(page)
    assert income.is_loaded()
    income.fill("35000", "Test AB")
    income.click_next()

    result = ResultPage(page)
    assert result.is_loaded()


@pytest.mark.parametrize("loan_type", ["Bil", "Båt", "Bröllop"])
def test_loan_flow_different_types(page, loan_type):
    start = StartPage(page)
    start.open()
    start.select_loan_type_and_continue(loan_type)

    loan = LoanPage(page)
    assert loan.is_loaded()
    loan.fill(SSN, "Test", "Person", fake.email())
    loan.click_next()

    income = IncomePage(page)
    assert income.is_loaded()
