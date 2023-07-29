import time

from pages.MenuPage import MenuPage


class Test3:

    def test_logout_app(self, login_saucedemo):
        menu_p = MenuPage(driver=login_saucedemo.driver)
        menu_p.open_menu()
        assert menu_p.is_menu_open(), 'Menu não está aberto!'
        menu_p.click_logout()
        assert login_saucedemo.is_url_login(), 'Pagina de login não encontrada!'


