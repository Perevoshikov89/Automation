from mainpage_input_fields import MainPage

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_input_fields():
    browser = webdriver.Chrome(
        service = Service(ChromeDriverManager().install()))
    
    main_page = MainPage(browser)
 # Проверь подсветку полей
    zip_code_color = browser.find_element(By.CSS_SELECTOR, '[name="zip-code"]').value_of_css_property('background_color')
    assert zip_code_color == ("#f8d7da")
    
    other_fields = ['#first_name', '#last_name', '#addres', '#city', '#country', '#e-mail', '#phone', '#job-position', '#company']
    for field in other_fields:
        field_color = browser.find_element(By.CSS_SELECTOR, field). value_of_css_property('background_color')
        assert field_color == ("#d1e7dd")


