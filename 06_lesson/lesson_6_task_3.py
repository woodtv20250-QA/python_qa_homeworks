from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

wait = WebDriverWait(driver, 20)
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Done!')]")
    )
)


images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
third_image = images[2]  # третья картинка (индекс 2)
src_value = third_image.get_dom_attribute("src")

print(src_value)

driver.quit()
