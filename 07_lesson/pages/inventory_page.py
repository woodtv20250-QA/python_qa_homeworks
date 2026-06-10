from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    CART = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_item_to_cart(self, item_name):
        item_locator = (By.CSS_SELECTOR, f"#add-to-cart-{item_name}")
        self.driver.find_element(*item_locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART).click()
