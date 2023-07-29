from pages.ProductsPage import ProductsPage


class Test2:

    def test_efetuar_login(self, setup):
        login_page = setup
        login_page.efetuar_login()
        products_page = ProductsPage(driver=login_page.driver)
        assert products_page.is_url_products(), 'URL de produtos não encontrada!'
        assert products_page.has_products_title(), 'Título da página diferente de Products!'
        assert products_page.validate_products_in_page(), 'Lista de produtos incorreta!'
        assert products_page.has_menu_button(), 'Botão de Menu não encontrado!'

