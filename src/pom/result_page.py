class ResultPage:
    def __init__(self, page):
        self.page = page
        self.status_message = page.locator(".result-message") # Exempel-selector

    def get_status_text(self):
        return self.status_message.inner_text()