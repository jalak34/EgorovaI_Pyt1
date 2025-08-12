from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service =ChromeService(ChromeDriverManager().install()))

try:
    # переходим на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # ожидаем загрузки изображений
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Done")
    )

    # получаем значения атрибута src у 3-й картинки
    images = driver.find_elements(By.TAG_NAME, "img")
    if len(images) >= 3:
        image3_src = images[3].get_attribute("src")
        print(image3_src)
    else:
        print("Отсутствует третья картинка")
   
finally:
    # закрываем браузер
    driver.quit()