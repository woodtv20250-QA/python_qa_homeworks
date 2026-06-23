import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    """Каталог товаров."""
    CART = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        """
        Инициализация страницы.
        Args:
            driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Добавить товары в корзину {item_name}")
    def add_item_to_cart(self, item_name: str) -> None:
        """
        Добавляет товар в корзину.
        Args:
            item_name: Название товара (например, "sauce-labs-backpack").
        """
        item_locator = (By.CSS_SELECTOR, f"#add-to-cart-{item_name}")
        self.driver.find_element(*item_locator).click()

    @allure.step("Перейти к корзине")
    def go_to_cart(self) -> None:
        """Выполняет переход к корзине."""
        self.driver.find_element(*self.CART).click()
