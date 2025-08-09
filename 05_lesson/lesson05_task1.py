from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Открыть браузер Google Chrome.Перейти на страницу: http://uitestingplayground.com/classattr
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/classattr")

# кликнуть синюю кнопку три раза
for i in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn class1 btn-primary btn-test']")
    blue_button.click()
sleep(15)


driver.quit()



