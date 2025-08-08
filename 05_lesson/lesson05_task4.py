from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Открыть браузер Firefox. Перейти на страницу:  http://the-internet.herokuapp.com/login
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("http://the-internet.herokuapp.com/login")

# В поле username ввести значение tomsmith
inpute_username =driver.find_element(By.CSS_SELECTOR, "[id=username]")
inpute_username.send_keys("tomsmith")
sleep(2)

# В поле password ввести значение SuperSecretPassword!
inpute_password =driver.find_element(By.CSS_SELECTOR, "[id=password]")
inpute_password.send_keys("SuperSecretPassword!")
sleep(2)

# Нажать кнопку Login
click_login =driver.find_element(By.CSS_SELECTOR, "[type='submit']")
click_login.click()
sleep(2)

# Вывести текст с зеленой плашки в консоль
green_field = driver.find_element(By.CSS_SELECTOR, "div.flash")
print(green_field.text)


# Закрыть браузер
quit()