from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
ChromeDriverManager().install()))

#поместим метод перед переходом на сайт
driver.implicitly_wait(20) 

# переходим на сайт
driver.get("http://uitestingplayground.com/textinput")

# ищем поле ввода
element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

# указываем в поле ввода текст
element.send_keys("SkyPro")

# переименовываем кнопку
click =  driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
buttonNameText = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

# выводим полученный текст в консоль
print(buttonNameText)

# закрываем браузер
driver.quit()