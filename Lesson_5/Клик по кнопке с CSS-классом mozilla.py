from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


# Зайди на сайт
driver.get("http://uitestingplayground.com/classattr")

# Найди "синию кнопку" и кликни на нее
for _ in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn class2 btn-primary btn-test']")
    blue_button.click()

driver.quit()