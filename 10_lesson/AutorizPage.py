import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class AutorizPage():
     """
        Конструктор класса AutorizPage для страницы авторизации
     """

     @allure.step('Инициализировать драйвер по параметру {driver}') 
     def __init__(self, driver)->None:
         """
        Конструктор класса AutorizPage.
        driver: WebDriver — объект драйвера Selenium.
        """
         self.driver = driver
         self.wait = WebDriverWait(driver, 5)

     @allure.step("Открытие страницы интернет-магазина")
     def open(self):
         """
         Открывает страницу интернет-магазина.
         """
         self.driver.get("https://www.saucedemo.com")

          
     @allure.step("Авторизация на странице авторизации интернет-магазина")
     def autorisation(self):
        """
         Методы для ввода логина и пароля, а также для нажатия кнопки входа
        """
        with allure.step('Заполнить поле Username: standard_user'):
         self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
        with allure.step('Заполнить поле Password: secret_sauce'):
         self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
        with allure.step('Нажать кнопку Login'):
         self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()