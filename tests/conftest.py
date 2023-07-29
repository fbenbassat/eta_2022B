import time

import pytest

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


def pytest_addoption(parser):
    parser.addoption("--select_browser", default="chrome", help="Select browser")


@pytest.fixture
def select_browser(request):
    yield request.config.getoption("--select_browser").lower()


@pytest.fixture
def setup(select_browser):
    login_page = LoginPage(browser=select_browser)
    yield login_page
    login_page.close()


@pytest.fixture
def run_all_browser(all_browser):
    login_page = LoginPage(browser=all_browser)
    yield login_page
    login_page.close()

@pytest.fixture
def login_saucedemo(setup):
    login_page = setup
    login_page.efetuar_login()
    yield login_page


@pytest.fixture
def has_product_in_cart(login_saucedemo):
    product_p = ProductsPage(driver=login_saucedemo.driver)
    product_p.add_random_product_to_cart()
    assert product_p.get_cart_badge_number() == 1, 'Quantidade de produtos no carrinho está incorreta!'
    yield product_p

