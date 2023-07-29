from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class YourCartPage(PageObject):

    url = 'https://www.saucedemo.com/cart.html'
    text_cart_title = 'Your Cart'
    css_checkout_btn = '[data-test="checkout"]'

    def __init__(self, driver):
        super(YourCartPage, self).__init__(driver=driver)

    def check_your_cart_page(self):
        return self.check_page(self.url, self.text_cart_title)

    def click_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_checkout_btn).click()
