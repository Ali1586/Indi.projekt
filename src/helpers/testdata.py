from faker import Faker
fake = Faker("sv_SE")
SKATTEVERKET_SSN = ["196408233234", "194910188885", "200002292386"]

def loan_payload(amount=10000, ssn=None):
    return {
        "product_type": "personal",
        "personal_number": ssn or SKATTEVERKET_SSN[0],
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": "Testgatan 1",
        "postcode": "12345",
        "city": "Stockholm",
        "phone": "0701234567",
        "email": fake.email(),
        "employment_type": "employed",
        "employer": "Test AB",
        "income": "35000",
        "loan_amount": str(amount),
        "repayment_months": "24",
    }

def loan_payloads_parametrized():
    return [loan_payload(5000, SKATTEVERKET_SSN[0]), loan_payload(15000, SKATTEVERKET_SSN[1]), loan_payload(50000, SKATTEVERKET_SSN[2])]
