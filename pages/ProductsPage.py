from random import randint

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class ProductsPage(PageObject):

    url = 'https://www.saucedemo.com/inventory.html'
    txt_products_title = 'Products'
    class_product_item = 'inventory_item'
    id_menu_btn = "react-burger-menu-btn"
    class_product_card = 'inventory_item'
    class_add_to_cart_btn = 'btn_primary'
    class_cart_badge = 'shopping_cart_badge'
    class_cart_btn = 'shopping_cart_link'
    class_product_name = 'inventory_item_name'
    class_remove_btn = 'btn_secondary'
    text_remove_btn = 'Remove'
    text_add_to_cart_btn = 'Add to cart'
    css_filter_select = '[data-test="product_sort_container"]'
    css_filter_price_low_to_high = '[value="lohi"]'
    class_item_price = '[class="inventory_item_price"]'
    value_low_high = 'lohi'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_url_products(self):
        return self.is_url(self.url)

    def has_products_title(self):
        return self.has_title(self.txt_products_title)

    def check_products_page(self):
        return self.check_page(self.url, self.txt_products_title)

    def validate_products_in_page(self):
        products_list = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)
        return len(products_list) == 6

    def has_menu_button(self):
        try:
            return self.driver.find_element(By.ID, self.id_menu_btn).is_displayed()
        except NoSuchElementException:
            return False

    def add_random_product_to_cart(self):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.class_product_card)
        random_product = randint(0, len(product_list) - 1)
        product_element = product_list[random_product]
        add_to_cart_text = product_element.find_element(By.CLASS_NAME, self.class_add_to_cart_btn).text
        if add_to_cart_text != self.text_add_to_cart_btn:
            raise Exception('Add to cart button not found!')
        product_element.find_element(By.CLASS_NAME, self.class_add_to_cart_btn).click()
        button_remove_text = product_element.find_element(By.CLASS_NAME, self.class_remove_btn).text
        if button_remove_text != self.text_remove_btn:
            raise Exception('Remove button not found!')
        return product_element.find_element(By.CLASS_NAME, self.class_product_name).text

    def get_cart_badge_number(self):
        return int(self.driver.find_element(By.CLASS_NAME, self.class_cart_badge).text)

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.class_cart_btn).click()

    def filter_by_price_low_to_high(self):
        # self.driver.find_element(By.CSS_SELECTOR, self.css_filter_select).click()
        # self.driver.find_element(By.CSS_SELECTOR, self.css_filter_price_low_to_high).click()
        select_element = self.driver.find_element(By.CSS_SELECTOR, self.css_filter_select)
        select = Select(select_element)
        select.select_by_value(self.value_low_high)


    def check_order_by_price_low_to_high(self):
        all_price_items = self.driver.find_elements(By.CSS_SELECTOR, self.class_item_price)

        for i in range(len(all_price_items) - 1):
            current_price = float(all_price_items[i].text.replace('$', ''))
            next_price = float(all_price_items[i + 1].text.replace('$', ''))
            print(f'Current prince: {current_price}')
            print(f'Next prince: {next_price}')
            print('-----------------------------')
            if current_price > next_price:
                return False
        return True


