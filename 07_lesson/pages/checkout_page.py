from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE = (By.CSS_SELECTOR, "#continue")
    SUMMARY = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_form(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(zip_code)

    def continue_checkout(self):
        self.driver.find_element(*self.CONTINUE).click()

    def get_total(self):
        return self.driver.find_element(*self.SUMMARY).text
