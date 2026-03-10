class ResultPage:
    def __init__(self, page):
        self.page = page

    def is_loaded(self):
        text = self.page.locator("body").inner_text()
        keywords = ["Bekräftelse", "Sammanställning", "Tack", "ansökan", "Lånebelopp", "Inkomst"]
        return any(w in text for w in keywords)
