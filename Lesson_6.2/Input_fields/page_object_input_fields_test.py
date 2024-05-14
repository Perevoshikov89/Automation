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
    main_page.color

    browser.quit()

