from faker import Faker

fake = Faker("sv_SE")

def loan_payload():
    return {
        "name": fake.name(),
        "amount": 10000,
        "interestRate": 5.5,
        "ssn": "199001012389"  # Skatteverkets testpersonnummer
    }
