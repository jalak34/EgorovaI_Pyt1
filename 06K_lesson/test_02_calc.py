#from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# инициализация браузера
driver = webdriver.Chrome(service=ChromeService(
ChromeDriverManager().install())) 
driver.implicitly_wait(20)


# открытие сайта
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# заполнение формы значениями
input = driver.find_element(By.CSS_SELECTOR, '#delay')
input.clear()
input.send_keys("45")


# нажатие кнопок
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
)
WebDriverWait(driver, 60).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
)

res = driver.find_element(By.CSS_SELECTOR, ".screen").text
assert res == "15"

# закрытие браузера
driver.quit()