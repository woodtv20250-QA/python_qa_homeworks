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
    "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
)

driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
driver.find_element(
    By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
driver.find_element(
    By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').clear()
driver.find_element(
    By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
zip_code_field = driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')
driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
print("Форма заполнена, нажимаем кнопку...")

button = driver.find_element(By.CSS_SELECTOR, ".btn").click()

wait = WebDriverWait(driver, 20)

print("Ждём появления результатов...")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name")))

zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code")
zip_error_msg = "zip-code должен быть красным"
assert "alert-danger" in zip_code.get_attribute("class"), zip_error_msg

green_fields = [
    "first-name", "last-name", "address", "e-mail",
    "phone", "city", "country", "job-position", "company"
]

for field_id in green_fields:
    element = driver.find_element(By.CSS_SELECTOR, f"#{field_id}")
    class_attr = element.get_attribute("class")
    field_error = f"Поле {field_id} должно быть зелёным, а у него {class_attr}"
    assert "alert-success" in class_attr, field_error

print("Все проверки пройдены успешно!")

driver.quit()
