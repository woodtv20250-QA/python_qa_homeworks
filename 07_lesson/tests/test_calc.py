from pages.calc_page import CalcPage


def test_calc(chrome_driver):
    page = CalcPage(chrome_driver)

    page.open_test_calc()
    page.set_delay("45")
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")
    page.wait_for_result("15")
    assert page.get_result() == "15"
