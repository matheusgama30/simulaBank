from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_001_login(login_page) -> None:
    login_page.login("user1", "pass1")
    login_page.verify_login_success()
    