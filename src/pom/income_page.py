class IncomePage:
    """Steg 3 – Inkomstuppgifter"""

    def __init__(self, page):
        self.page = page

    def is_loaded(self):
        return self.page.locator("#monthlyIncome").is_visible()

    def fill(self, monthly_income="35000", employer="Test AB"):
        self.page.locator("#monthlyIncome").fill(monthly_income)
        self.page.locator("#employer").fill(employer)
        try:
            self.page.locator("select").first.select_option("fulltime")
        except Exception:
            pass

    def click_next(self):
        self.page.get_by_role("button", name="Nästa").click()
        self.page.wait_for_timeout(1500)
