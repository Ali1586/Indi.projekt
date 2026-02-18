class StartPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(
            "https://souderbroder-loan-lab.lovable.app",
            wait_until="networkidle"
        )

    def go_to_loan(self):
        # Direktnavigation pga SPA-routing
        self.page.goto(
            "https://souderbroder-loan-lab.lovable.app/loan",
            wait_until="networkidle"
        )
