import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartInitPage():
     """
        Конструктор класса CartInitPage 
        для страницы оформления заказа
     """
     @allure.step('Инициализировать драйвер по параметру {driver}') 
     def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

     @allure.step("Заполнить форму данными")
     def cart_init(self):
        """
        Mетоды для заполнения 
        формы данными (имя, фамилия, почтовый индекс)
        """
        with allure.step('Заполнить поле First name: Irina'):
         self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Irina")
        with allure.step('Заполнить поле Last name: Egorova'):
         self. driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Egorova")
        with allure.step('Заполнить поле Zip/Postal Code: 123456'):
         self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("123456")
        with allure.step('Нажать кнопку Continue'):
         self.driver.find_element(By.CSS_SELECTOR, '#continue').click()