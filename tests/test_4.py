import time

from pages.CheckoutYourInfoPage import CheckoutYourInfoPage
from pages.YourCartPage import YourCartPage


class Test4:

    def test_verify_error_message_in_checkout(self, has_product_in_cart):
        product_p, product_name = has_product_in_cart
        product_p.open_cart()
        your_cart_p = YourCartPage(driver=product_p.driver)
        assert your_cart_p.check_your_cart_page(), 'Your Cart page not found!'
        your_cart_p.click_checkout()
        checkout_your_info_p = CheckoutYourInfoPage(driver=your_cart_p.driver)
        assert checkout_your_info_p.check_checkout_your_info_page(), 'Checkout Your Info page not found!'
        checkout_your_info_p.click_continue()
        assert checkout_your_info_p.has_first_name_required_error_message(), 'Error message not found!'




