import allure
from mainpage_input_fields import MainPage

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Поля ввода")
@allure.description("Тест проверяет, что фон незаполненного поля ввода при попытке перейте на следующую страницу красный")
@allure.feature("CREATE")
@allure.severity("blocker")

def test_input_fields():


    with allure.step("Запуск браузера Chrome, переход на страницу с полями ввода"):
        driver = webdriver.Chrome(service=ChromeService
                              (ChromeDriverManager().install()))
        mainpaige_input_fields = MainPage(driver)

    with allure.step("Заполнение полей ввода"):
        mainpaige_input_fields.personal_data("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
        
    with allure.step("Проверка: фон заполненных полей зеленый, незаполненного - красный"):
        assert mainpaige_input_fields.zip_code_red() == 'rgba(248, 215, 218, 1)'
        
        assert mainpaige_input_fields.other_fields_green() == 'rgba(209, 231, 221, 1)'

    with allure.step("Закрытие браузера Chrome"):
        mainpaige_input_fields.close_driver()


