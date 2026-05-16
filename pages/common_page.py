from playwright.sync_api import Page, expect

class CommonPage:
    def __init__(self, page: Page):
        self.page = page
        self.voltar_para_home = page.get_by_role("button", name="Voltar para a Home")

    def verificar_text(self, texto):
        self.page.get_by_text(texto).wait_for()
        expect(self.page.get_by_text(texto)).to_be_visible()

    def voltar_home(self):
        self.voltar_para_home.click()

    