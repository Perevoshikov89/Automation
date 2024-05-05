from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Зайди на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Разверни окно
driver.maximize_window()

# В поле First name введи значение 'Иван'
First_name= driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")

# В поле Last name введи значение 'Петров'
input_last_name_field = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")

# В поле Address  введи значение 'Ленина, 55-3'
input_address_field = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")

# В поле Email  введи значение 'test@skypro.com'
input_email_field = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")

# В поле phonenumber  введи значение '+7985899998787'
input_phonenumber_field = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")

# В поле city  введи значение 'Москва'
input_city_field = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")

# В поле country  введи значение 'Россия'
input_country_field = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")

# В поле Job position  введи значение 'QA'
input_job_position_field = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")

# В поле Company  введи значение 'SkyPro'
input_company_field = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

# Нажми кнопку Submit
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

# Ожидание, пока страница не обновится после отправки формы
WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

driver.quit()