from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Зайди на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# Очисти поле delay и введи значение '45'
delay_rield = driver.find_element(By.ID, 'delay').clear()
delay_rield = driver.find_element(By.ID, 'delay').send_keys("45")


# Найди и нажми кнопку 7
seven_button = driver.find_element(By.CSS_SELECTOR, 'span.btn.btn-outline-primary[value="7"]').click()

# seven_button = driver.find_element(By.CSS_SELECTOR, 'span[class = "btn btn-outline-primary"[value="7"]]').click()




# Нажатие на кнопки

# driver.quit()