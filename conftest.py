import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.pix_page import PixPage
from pages.common_page import CommonPage
from pages.emprestimos_page import EmprestimoPage
import os


@pytest.fixture
def common_page(page):
    return CommonPage(page)

@pytest.fixture
def page(page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://leogcarvalho.github.io/simulabank/login.html")
    return page

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture(scope="session")
def launch_browser_args():
    return {
        "headless": os.getenv("CI") == "true"
    }

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def pix_page(page):
    return PixPage(page)

@pytest.fixture
def emprestimo_page(page):
    return EmprestimoPage(page)