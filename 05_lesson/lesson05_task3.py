from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

firefox_options = FirefoxOptions()
firefox_options.add_argument('--ignore-certificate-errors')

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=firefox_options)


driver.get("http://the-internet.herokuapp.com/inputs")
sleep(2)

search_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
search_field.send_keys("12345")
sleep(1)

search_field.clear()
sleep(1)
search_field.send_keys("54321")
sleep(1)
driver.quit()
