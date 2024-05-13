from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Submit_button_Page:
    def __init__(self, driver):
        self._driver = driver
 # Проверь подсветку полей
        zip_code_color = self._driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').value_of_css_property('background_color')
        assert zip_code_color == ("#f8d7da")
    
        other_fields = ['#first_name', '#last_name', '#addres', '#city', '#country', '#e-mail', '#phone', '#job-position', '#company']
        for field in other_fields:
            field_color = self._driver.find_element(By.CSS_SELECTOR, field). value_of_css_property('background_color')
            assert field_color == ("#d1e7dd")
