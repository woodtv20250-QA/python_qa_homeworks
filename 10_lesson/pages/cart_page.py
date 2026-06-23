import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    CHECKOUT = (By.CSS_SELECTOR, "#checkout")

    def __init__(self, driver):
        """
        Инициализация страницы.
        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Переход к оформлению заказа")
    def checkout(self) -> None:
        """Переходит к оформлению заказа."""
        self.driver.find_element(*self.CHECKOUT).click()
