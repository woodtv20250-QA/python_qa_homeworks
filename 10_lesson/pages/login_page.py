import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """Страница авторизации на сайте SauceDemo."""
    USER_NAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

    def __init__(self, driver):
        """
        Инициализация страницы.
        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Открыть страницу")
    def open(self) -> None:
        """Открывает главную страницу."""
        self.driver.get("https://www.saucedemo.com")

    @allure.step("Ввести логин {username} и пароль {password}")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию.
        Args:
            username: Логин пользователя.
            password: Пароль пользователя.
        Returns:
            None
        """
        self.driver.find_element(*self.USER_NAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
