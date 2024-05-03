from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Установка и запуск драйвера Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Зайди на сайт, найди кнопку "синию кнопку" и кликни на нее
driver.get("http://uitestingplayground.com/ajax")
blue_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()

# Жди 17 секунд
sleep(17)

# Найди появившийся элемент и выведи в консоль текст на элементе
data = driver.find_element(By.CSS_SELECTOR, 'p[class="bg-success"]').text
print(data)

# Закрой браузер
driver.quit()