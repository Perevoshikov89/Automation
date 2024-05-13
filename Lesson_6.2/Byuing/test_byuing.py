from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



# Установка и запуск драйвера Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_byuing():
# Зайди на сайт
    driver.get("https://www.saucedemo.com/")

# В поле username  введи значение 'standard_user'
    username = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').clear()
    username = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys("standard_user")

# В поле password введи значение 'secret_sauce'
    password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').clear()
    password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys("secret_sauce")

    sleep(2)
# Нажми кнопку Login
    login_button = driver.find_element(By.ID,"login-button").click()


# Добавь товары в корзину
    add_button_backpack = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    add_button_t_shirt = driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
    add_button_onesie = driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click()

# Перейди в корзину
    cart_button = driver.find_element(By.XPATH, "//html/body/div/div/div/div[1]/div[1]/div[3]/a").click()

# Нажми checkout
    checkout_button = driver.find_element(By.XPATH, "//*[@id='checkout']").click()

# Введи данные покупателя
    first_name = driver.find_element(By.ID, "first-name").clear()
    first_name = driver.find_element(By.ID, "first-name").send_keys("Yuri")
    last_name = driver.find_element(By.ID, "last-name").clear()
    last_name = driver.find_element(By.ID, "last-name").send_keys("Perevoshikov")
    zip_code = driver.find_element(By.ID, "postal-code").clear()
    zip_code = driver.find_element(By.ID, "postal-code").send_keys("123456")


# Нажми кнопку Continue
    continue_button = driver.find_element(By.CSS_SELECTOR, 'input[name="continue"]').click()

    total = driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]').text
    print(total)

    sleep(3)

    assert total == "Total: $58.29"

driver.quit()











