from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Зайди на сайт
driver.get("http://uitestingplayground.com/classattr")

# Найди кнопку "синию кнопку" и кликни на нее
blue_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn class2 btn-primary btn-test']")
blue_button.click()

sleep(10)