#from time import sleep
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# инициализация браузера
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(20)

# открытие сайта
driver.get("https://www.saucedemo.com")

# авторизация
input = driver.find_element(By.CSS_SELECTOR, '#user-name')
input.send_keys("standard_user")
input = driver.find_element(By.CSS_SELECTOR, '#password')
input.send_keys("secret_sauce")

input = driver.find_element(By.CSS_SELECTOR, '#login-button').click()

# добавление товаров в корзину
input = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
input = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
input = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

# переход в корзину
input = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container').click()

# нажатие Checkout
driver.find_element(By.CSS_SELECTOR, '#checkout').click()

# заполнение формы своими данными
first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
first_name.send_keys("Irina")
last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
last_name.send_keys("Egorova")
zip = driver.find_element(By.CSS_SELECTOR, '#postal-code')
zip.send_keys("123456")

# нажатие Continue
driver.find_element(By.CSS_SELECTOR, '#continue').click()

# чтение со страницы итоговой стоимости
total = driver.find_element(By.CSS_SELECTOR, '[class="summary_total_label"]').text
total_value = float(total.split("$")[1])

# закрытие браузера
driver.quit()


assert total_value == 58.29, 'Сумма не равна'

