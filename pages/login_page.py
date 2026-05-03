from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Usuário:")
        self.password_input = page.get_by_role("textbox", name="Senha:")
        self.entar_button = page.get_by_role("button", name="Entrar")


    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.entar_button.click()   

    def verify_login_success(self):
        expect(self.page.get_by_role("heading", name="Bem-vindo ao SimulaBank!")).to_be_visible()
