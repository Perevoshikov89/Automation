import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.implicitly_wait(4)
def test_input_fields():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').clear()
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    sleep(5)
    
 # Проверь подсветку полей
    zip_code_field = driver.find_element(By.ID, "zip-code")
    assert "is-invalid" in zip_code_field.get_attribute("class")
    alert_element = driver.find_element(By.CLASS_NAME, "alert.py-2.alert-danger")
    assert alert_element.is_displayed()  # Проверь, что элемент видим
    

driver.quit()

