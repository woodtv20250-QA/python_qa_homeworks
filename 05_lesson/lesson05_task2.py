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

driver.get("http://uitestingplayground.com/dynamicid")

sleep(1)

blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
blue_button.click()
print("Кнопка с динамическим ID успешно нажата!")

sleep(1)
