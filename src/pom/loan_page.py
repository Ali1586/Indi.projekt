class LoanPage:
    def __init__(self, page):
        self.page = page



    def is_loaded(self):
            # Verifiera att lånesidan är laddad
        return "/loan" in self.page.url
