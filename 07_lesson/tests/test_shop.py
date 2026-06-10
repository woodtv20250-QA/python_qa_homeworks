from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop(firefox_driver):   # ← фикстура для Firefox
    login_page = LoginPage(firefox_driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(firefox_driver)
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    inventory_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
    inventory_page.add_item_to_cart("sauce-labs-onesie")
    inventory_page.go_to_cart()

    cart_page = CartPage(firefox_driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(firefox_driver)
    checkout_page.fill_form("Татьяна", "Попова", "633159")
    checkout_page.continue_checkout()

    total = checkout_page.get_total()
    assert total == "Total: $58.29"
