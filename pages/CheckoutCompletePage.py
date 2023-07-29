from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutCompletePage(PageObject):

    url = 'https://www.saucedemo.com/checkout-complete.html'
    text_title_page = 'Checkout: Complete!'
    class_thank_you_order = 'complete-header'
    text_thank_you_order = 'Thank you for your order!'

    def __init__(self, driver):
        super(CheckoutCompletePage, self).__init__(driver=driver)

    def check_checkout_complete_page(self):
        return self.check_page(self.url, self.text_title_page)

    def check_thank_order(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_thank_you_order).text == self.text_thank_you_order

