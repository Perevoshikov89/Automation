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
    zip_code_color = main_page.get_zip_code_color("zip-code")
    assert zip_code_color == ("#f8d7da")

    other_fields = main_page.get_other_fields_color_except("zip-code")
    for color in other_fields:
        assert color == ("#d1e7dd")


    browser.quit()

