from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://uitestingplayground.com/classattr")

sleep(1)

blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
blue_button.click()

alert = driver.switch_to.alert
alert_text = alert.text
print(f"Текст в алерте: {alert_text}")
assert alert_text == "Primary button pressed", "Текст в алерте не совпадает!"

alert.accept()
