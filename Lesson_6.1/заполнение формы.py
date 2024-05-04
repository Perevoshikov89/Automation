from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Зайди на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# В поле First name введи значение 'Иван'
First_name= driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
First_name.send_keys("Иван")

# В поле Last name введи значение 'Петров'
input_password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
input_password_field.send_keys("Петров")

# В поле Address  введи значение 'Ленина, 55-3'
input_password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
input_password_field.send_keys("Ленина, 55-3")

# В поле Email  введи значение 'test@skypro.com'
input_password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
input_password_field.send_keys("test@skypro.com")

# В поле phonenumber  введи значение '+7985899998787'
input_password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
input_password_field.send_keys("+7985899998787")

# В поле city  введи значение 'Москва'
input_password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
input_password_field.send_keys("Москва")

# В поле country  введи значение 'Россия'
input_password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
input_password_field.send_keys("Россия")

# В поле Job position  введи значение 'QA'
input_password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
input_password_field.send_keys("QA")

# В поле Company  введи значение 'SkyPro'
input_password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
input_password_field.send_keys("SkyPro")

# Нажми кнопку Submit
submit_button = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-outline-primary mt-3"]').click()


driver(quit)
