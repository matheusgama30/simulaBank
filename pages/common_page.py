from playwright.sync_api import Page, expect

class CommonPage:
    def __init__(self, page: Page):
        self.page = page

    def verificar_text(self, texto):
        expect(self.page.get_by_text(texto)).to_be_visible()