
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from AutorizPage import AutorizPage
from CartPage import CartPage
from CartInitPage import CartInitPage
from PricePage import PricePage


@pytest.fixture
def driver():
         driver = webdriver.Firefox()
         #driver.get("https://www.saucedemo.com")
         yield driver
         driver.quit()

@allure.id("ShopTest-1")
@allure.story("Проверка функциональности интернет-магазина")
@allure.feature("READ")
@allure.title("Тестирование магазина")
def test_form(driver):
      driver.get("https://www.saucedemo.com")
      with allure.step("Авторизация на странице интернет магазина"):
        shop_autoris = AutorizPage(driver)
        shop_autoris.autorisation()

      with allure.step("Добавление товаров в корзину, нажатие кнопки Checkout"):
        shop_cart = CartPage(driver)
        shop_cart.cart()

      with allure.step("Заполнение формы своими данными"):
        shop_cart_init = CartInitPage(driver)
        shop_cart_init.cart_init()

      with allure.step("Прочитать со страницы итоговую стоимость" \
      "сравнить с заявленной"): 
        shop_total_price = PricePage(driver)
        shop_total_price.total_price()
        
