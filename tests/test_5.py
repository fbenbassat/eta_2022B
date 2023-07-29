from pages.CheckoutCompletePage import CheckoutCompletePage
from pages.CheckoutOverviewPage import CheckoutOverviewPage
from pages.CheckoutYourInfoPage import CheckoutYourInfoPage
from pages.YourCartPage import YourCartPage


class Test5:

    def test_buy_product(self, has_product_in_cart):
        product_p, product_name = has_product_in_cart
        product_p.open_cart()
        your_cart_p = YourCartPage(driver=product_p.driver)
        assert your_cart_p.check_your_cart_page(), 'Your Cart page not found!'
        your_cart_p.click_checkout()
        checkout_your_info_p = CheckoutYourInfoPage(driver=your_cart_p.driver)
        assert checkout_your_info_p.check_checkout_your_info_page(), 'Checkout Your Info page not found!'
        checkout_your_info_p.fill_your_information()
        checkout_your_info_p.click_continue()
        checkout_p = CheckoutOverviewPage(driver=checkout_your_info_p.driver)
        assert checkout_p.check_checkout_page(), 'Checkout Overview page not found!'
        assert checkout_p.check_product_information(product_name), 'Checkout Overview information is not correct!'
        checkout_p.click_finish_btn()
        checkout_complete_p = CheckoutCompletePage(driver=checkout_p.driver)
        assert checkout_complete_p.check_checkout_complete_page(), 'Checkout Complete page not found!'
        assert checkout_complete_p.check_thank_order(), 'Thank you order message not found!'
