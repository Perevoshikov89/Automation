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


# Нажми 7 + 8 =
seven_button = driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[1]').click()
plus_button = driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[4]').click()
eigth_button = driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[2]').click()
result_button = driver.find_element(By.XPATH, '//html/body/main/div/div[4]/div/div/div[2]/span[15]').click()



# Нажатие на кнопки

# driver.quit()