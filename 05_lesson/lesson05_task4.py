from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

firefox_options = FirefoxOptions()
firefox_options.set_preference(
    "security.insecure_field_warning.contextual.enabled", False)
firefox_options.set_preference("security.certerrors.permanentOverride", True)

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=firefox_options)

driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

search_field_username = driver.find_element(By.ID, "username")
search_field_username.send_keys("tomsmith")

search_field_password = driver.find_element(By.ID, "password")
search_field_password.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

flash_message = driver.find_element(By.ID, "flash")
print(flash_message.text)

sleep(2)

driver.quit()
