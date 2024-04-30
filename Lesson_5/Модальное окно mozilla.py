from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Зайди на сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Зайди на сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(10)

# Найди кнопку "close" и кликни на нее

close_button = driver.find_element(By.CSS_SELECTOR, ".close-modal")
close_button.click()
sleep(5)

driver.quit()