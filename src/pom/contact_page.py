class NavigationBar:
    def __init__(self, page):
        self.page = page
        self.home_link = page.get_by_role("link", name="Hem")
        self.loan_link = page.get_by_role("link", name="Sök lån")

    def click_home(self):
        self.home_link.click()