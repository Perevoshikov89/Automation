from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# Установка и запуск драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_calculator():
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

# Покажи результат
    wait = WebDriverWait(driver, 45)
    wait.until(EC. text_to_be_present_in_element((By.CSS_SELECTOR, '[class = "screen"]'), '15'))
    result = driver.find_element(By.CSS_SELECTOR, '[class = "screen"]').text()

# sum_nums = result_element.text
    print(result)

driver.quit()
