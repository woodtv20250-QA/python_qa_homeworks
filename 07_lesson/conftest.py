import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--remote-allow-origins=*")
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=FirefoxService(
        GeckoDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
