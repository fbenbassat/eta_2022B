import time

from pages.ProductsPage import ProductsPage


class Test7:

    def test_filter_product_low_to_high(self, login_saucedemo):
        products_p = ProductsPage(driver=login_saucedemo.driver)
        assert products_p.check_products_page(), 'Products page not found!'
        products_p.filter_by_price_low_to_high()
        assert products_p.check_order_by_price_low_to_high(), 'Incorrect price order.'
