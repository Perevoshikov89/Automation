from selenium.webdriver.common.by import By
from time import sleep

class MainPage:

# Установка и запуск драйвера Chrome, переход на страницу

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
        self._driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
        self._driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
        self._driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
        self._driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
        self._driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
        self._driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
        self._driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
        self._driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
        self._driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').clear()
        sleep(5)
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        sleep(5)

    def color(self):
        zip_code_color = self._driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').value_of_css_property('background_color')
        assert zip_code_color == ("#f8d7da")
    
        other_fields = ['#first_name', '#last_name', '#addres', '#city', '#country', '#e-mail', '#phone', '#job-position', '#company']
        for field in other_fields:
            field_color = self._driver.find_element(By.CSS_SELECTOR, field). value_of_css_property('background_color')
        assert field_color == ("#d1e7dd")

