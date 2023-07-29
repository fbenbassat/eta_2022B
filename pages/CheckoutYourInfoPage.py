from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutYourInfoPage(PageObject):

    url = 'https://www.saucedemo.com/checkout-step-one.html'
    text_title_page = 'Checkout: Your Information'
    css_continue_btn = '[name="continue"]'
    text_first_name_required = 'Error: First Name is required'
    css_error_message = '[data-test="error"]'

    def __init__(self, driver):
        super(CheckoutYourInfoPage, self).__init__(driver=driver)

    def check_checkout_your_info_page(self):
        return self.check_page(self.url, self.text_title_page)

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_continue_btn).click()

    def has_first_name_required_error_message(self):
        error_text = self.driver.find_element(By.CSS_SELECTOR, self.css_error_message).text
        return error_text == self.text_first_name_required
