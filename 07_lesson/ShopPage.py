import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage():
     
     def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(44)

     def autorisation(self):
         self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
         self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
         self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

     def cart(self):
         self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
         self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
         self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
         self.driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container').click()
         self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()
    
     def cart_init(self):
        self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Irina")
        self. driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Egorova")
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

     def total_price(self):
       total =  self.driver.find_element(By.CSS_SELECTOR, '[class="summary_total_label"]').text
       total_value = float(total.split("$")[1])
       assert total_value == 58.29, 'Сумма не равна'