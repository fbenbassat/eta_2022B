from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutOverviewPage(PageObject):

    url = 'https://www.saucedemo.com/checkout-step-two.html'
    text_title_page = 'Checkout: Overview'
    class_propduct_name = 'inventory_item_name'
    css_finish_btn = '[data-test="finish"]'

    def __init__(self, driver):
        super(CheckoutOverviewPage, self).__init__(driver=driver)

    def check_checkout_page(self):
        return self.check_page(self.url, self.text_title_page)

    def check_product_information(self, product_name):
        return self.driver.find_element(By.CLASS_NAME, self.class_propduct_name).text == product_name

    def click_finish_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_finish_btn).click()


