class StartPage:
    URL = "https://souderbroder-loan-lab.lovable.app"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL, wait_until="networkidle")
        self.page.wait_for_timeout(2000)

    def is_loaded(self):
        return self.page.title() != ""

    def select_loan_type_and_continue(self, loan_type="Bil"):
        self.page.get_by_role("heading", name=loan_type).click()
        self.page.get_by_role("button", name="Nästa").click()
        self.page.wait_for_timeout(1500)
