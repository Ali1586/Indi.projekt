class ContactPage:
    URL = "https://souderbroder-loan-lab.lovable.app/contact"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL, wait_until="networkidle")

    def is_loaded(self):
        return "/contact" in self.page.url

    def get_heading(self):
        h = self.page.locator("h1, h2").first
        return h.inner_text() if h.count() > 0 else ""