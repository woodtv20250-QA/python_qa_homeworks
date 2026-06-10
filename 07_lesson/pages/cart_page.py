from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    CHECKOUT = (By.CSS_SELECTOR, "#checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def checkout(self):
        self.driver.find_element(*self.CHECKOUT).click()
