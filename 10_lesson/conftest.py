import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def firefox_driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=FirefoxService(
        GeckoDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
