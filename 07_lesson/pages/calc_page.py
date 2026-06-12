from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    DELAY_FIELD = (By.CSS_SELECTOR, '#delay')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def open_test_calc(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, value):
        self.driver.find_element(By.XPATH, f"//span[text()='{value}']").click()

    def wait_for_result(self, expected_result):
        self.wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), expected_result)
        )

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
