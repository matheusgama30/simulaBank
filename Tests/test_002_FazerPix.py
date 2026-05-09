from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_002_FazerPix(common_page, login_page, pix_page, home_page) -> None:
    login_page.login("user1", "pass1")
    home_page.acessarMenu("Fazer Pix")
    pix_page.fazer_pix("chave123", "10.00")
    pix_page.verificar_pix_sucesso()
    pix_page.voltar_home()
    common_page.verificar_text("4.990,00")
    home_page.acessarMenu("Ver Extrato")
    common_page.verificar_text("Pix para chave123 - R$ -10,00")
    