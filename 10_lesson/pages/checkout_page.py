import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE = (By.CSS_SELECTOR, "#continue")
    SUMMARY = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        """
        Инициализация страницы.
        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Заполняет форму: {first_name}, {last_name}, {zip_code}")
    def fill_form(
            self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Заполняет форму оформления заказа.
        Args:
            first_name: Имя.
            last_name: Фамилия.
            zip_code: Почтовый индекс.
        """
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(zip_code)

    @allure.step("Нажимает Continue")
    def continue_checkout(self) -> None:
        """Нажимает кнопку Continue."""
        self.driver.find_element(*self.CONTINUE).click()

    @allure.step("Возвращает сумму")
    def get_total(self) -> str:
        """
        Возвращает итоговую сумму заказа.
        Returns:
            str: Текст итоговой суммы.
        """
        return self.driver.find_element(*self.SUMMARY).text
