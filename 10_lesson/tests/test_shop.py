import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Оформление заказа с тремя товарами")
@allure.description(
    "Авторизация, добавление трёх товаров, "
    "заполнение формы и проверка итоговой суммы")
@allure.feature("Корзина и оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(firefox_driver):

    with allure.step("Открыть страницу логина и авторизоваться"):
        login_page = LoginPage(firefox_driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        inventory_page = InventoryPage(firefox_driver)
        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
        inventory_page.add_item_to_cart("sauce-labs-onesie")
        inventory_page.go_to_cart()

    with allure.step("Перейти в корзину, нажать Checkout"):
        cart_page = CartPage(firefox_driver)
        cart_page.checkout()

    with allure.step("Заполнить форму"):
        checkout_page = CheckoutPage(firefox_driver)
        checkout_page.fill_form("Татьяна", "Попова", "633159")
        checkout_page.continue_checkout()

    with allure.step("Проверить итоговую сумму"):
        total = checkout_page.get_total()
        with allure.step(f"Итоговая сумма: {total}"):
            assert total == "Total: $58.29"
