from playwright.sync_api import Page, expect

class PixPage:
    def __init__(self, page: Page):
        self.page = page
        self.chave_pix = page.get_by_role("textbox", name="Chave Pix:")
        self.valor_pix = page.get_by_role("textbox", name="Valor:")
        self.fazer_pix_button = page.get_by_role("button", name="Enviar Pix")
        self.voltar_para_home = page.get_by_role("button", name="Voltar para a Home")

    def fazer_pix(self, chave, valor):
        self.chave_pix.fill(chave)
        self.valor_pix.fill(valor)
        self.fazer_pix_button.click()

    def verificar_pix_sucesso(self):
        expect(self.page.get_by_text("Transação Realizada com Sucesso!")).to_be_visible()



