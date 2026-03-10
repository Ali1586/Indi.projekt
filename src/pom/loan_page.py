class LoanPage:
    def __init__(self, page):
        self.page = page

    def is_loaded(self):
        return self.page.locator("#personalNumber").is_visible()

    def fill(self, ssn, first_name, last_name, email,
             phone="0701234567", address="Testgatan 1",
             postal_code="12345", city="Stockholm"):
        self.page.locator("#personalNumber").fill(ssn)
        self.page.locator("#firstName").fill(first_name)
        self.page.locator("#lastName").fill(last_name)
        self.page.locator("#email").fill(email)
        self.page.locator("#phone").fill(phone)
        self.page.locator("#address").fill(address)
        self.page.locator("#postalCode").fill(postal_code)
        self.page.locator("#city").fill(city)

    def click_next(self):
        self.page.get_by_role("button", name="Nästa").click()
        self.page.wait_for_timeout(1500)
