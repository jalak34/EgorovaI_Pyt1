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
driver.get("http://www.uitestingplayground.com/ajax")

# нажимаем на синюю кнопку с id = "ajaxButton"
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# ищем элемент с id="content"
content = driver.find_element(By.CSS_SELECTOR, "#content")

# получаем текст из зеленой плашки 
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

# выводим полученный текст в консоль
print(txt)

# закрываем браузер
driver.quit()