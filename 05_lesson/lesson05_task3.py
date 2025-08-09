from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Открыть браузер Firefox. Перейти на страницу:  http://the-internet.herokuapp.com/inputs
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("http://the-internet.herokuapp.com/inputs")

# Ввести в поле текст Sky.
inpute_field =driver.find_element(By.CSS_SELECTOR, "input")
inpute_field.send_keys("Sky")
sleep(3)

# Очистить поле
inpute_field.clear()

# Ввести в поле текст Pro
inpute_field =driver.find_element(By.CSS_SELECTOR, "input")
inpute_field.send_keys("Pro")

# Закрыть браузер
driver.quit()
