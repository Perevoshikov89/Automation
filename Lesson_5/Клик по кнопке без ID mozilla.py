from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Зайди на сайт
driver.get("http://uitestingplayground.com/dynamicid")

# Найди кнопку "синию кнопку" и кликни на нее 3 раза

for _ in range(3):
    button_with_dynamic_id = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    button_with_dynamic_id.click()

driver.quit()