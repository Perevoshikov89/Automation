from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from byuing_page import ByuingPage



# Установка и запуск драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_byuing():
    driver = webdriver.Chrome(service=ChromeService
                              (ChromeDriverManager().install()))
    byuing = ByuingPage(driver)
    byuing.authorization("standard_user", "secret_sauce")
    price_added = byuing.add_products()
    byuing.go_to_cart()
    byuing.personal_data("Yuri", "Perevoshikov", "123456")
    price_calc = byuing.total_cost()
    assert price_calc == price_added
    byuing.close()



driver.quit()











