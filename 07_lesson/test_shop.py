
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ShopPage import ShopPage

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(20)

@pytest.fixture
def driver():
         driver = webdriver.Firefox()
         yield driver
         driver.quit()

def test_form(driver):
        driver.get("https://www.saucedemo.com")
        WebDriverWait(driver, 50)
        shop_autoris = ShopPage(driver)
        shop_autoris.autorisation()
        shop_cart = ShopPage(driver)
        shop_cart.cart()
        shop_cart_init = ShopPage(driver)
        shop_cart_init.cart_init()
        shop_total_price = ShopPage(driver)
        shop_total_price.total_price()
        
