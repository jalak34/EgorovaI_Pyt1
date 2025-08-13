#from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# инициализация браузера
edge_driver_path = r"C:\Users\jalak\Downloads\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))
driver.implicitly_wait(20)


# открытие сайта
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# заполнение формы значениями
first_name = driver.find_element(By.CSS_SELECTOR, '[name ="first-name"]')
first_name.send_keys("Иван")

last_name = driver.find_element(By.CSS_SELECTOR, '[name = "last-name"]')
last_name.send_keys("Петров")

address = driver.find_element(By.CSS_SELECTOR, '[name = "address"]')
address.send_keys("Ленина, 55-3")

e_mail = driver.find_element(By.CSS_SELECTOR, '[name = "e-mail"]')
e_mail.send_keys("test@skypro.com")

phone = driver.find_element(By.CSS_SELECTOR, '[name = "phone"]')
phone.send_keys("+7985899998787")

zip_code = driver.find_element(By.CSS_SELECTOR, '[name = "zip-code"]')
zip_code.send_keys("")

city = driver.find_element(By.CSS_SELECTOR, '[name = "city"]')
city.send_keys("Москва")

country = driver.find_element(By.CSS_SELECTOR, '[name = "country"]')
country.send_keys("Россия")

job_position = driver.find_element(By.CSS_SELECTOR, '[name = "job-position"]')
job_position.send_keys("QA")

company = driver.find_element(By.CSS_SELECTOR, '[name = "company"]')
company.send_keys("SkyPro")

# нажатие кнопки Submit
driver.find_element(By.CSS_SELECTOR, '[class = "btn btn-outline-primary mt-3"]').click()

driver.implicitly_wait(10)

# вызов цвета
zip_code_src = (driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property("background-color"))
print(zip_code_src)
e_mail_src = (driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property("background-color"))
print(e_mail_src)
e_mail_src = (driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property("background-color"))
first_name_src = (driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property("background-color"))
last_name_src = (driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property("background-color"))
address_src = (driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property("background-color"))
phone_src = (driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property("background-color"))
city_src = (driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property("background-color"))
country_src = (driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property("background-color"))
job_position_src = (driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property("background-color"))
company_src = (driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property("background-color"))

# проверка (assert), что поле Zip code подсвечено красным, иначе: вывод сообщения
assert zip_code_src == "rgba(248, 215, 218, 1)", "Поле Zip-code не подсвечено красным"

# проверка (assert), что остальные поля подсвечены зеленым, иначе: вывод сообщения
assert e_mail_src == "rgba(209, 231, 221, 1)", "Поле E-mail не подсвечено зеленым"
assert first_name_src == "rgba(209, 231, 221, 1)", "Поле First name не подсвечено зеленым"
assert last_name_src == "rgba(209, 231, 221, 1)", "Поле Last name не подсвечено зеленым"
assert address_src == "rgba(209, 231, 221, 1)", "Поле Address не подсвечено зеленым"
assert phone_src == "rgba(209, 231, 221, 1)", "Поле Phone number не подсвечено зеленым"
assert city_src == "rgba(209, 231, 221, 1)", "Поле City не подсвечено зеленым"
assert country_src == "rgba(209, 231, 221, 1)", "Поле Country не подсвечено зеленым"
assert job_position_src == "rgba(209, 231, 221, 1)", "Поле Job position не подсвечено зеленым"
assert company_src == "rgba(209, 231, 221, 1)", "Поле Company не подсвечено зеленым"

# закрытие браузера
driver.quit()