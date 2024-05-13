from mainpage_input_fields import MainPage
from submit_button_page import Submit_button_Page

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_input_fields(): 
    browser = webdriver.Chrome() #Открываем браузер
    main_page = MainPage(browser) #Переменная хранит экземпляр класса MainPage
    submit_page = Submit_button_Page(browser)


