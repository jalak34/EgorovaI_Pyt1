import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
         driver = webdriver.Chrome()
         yield driver
         driver.quit()

   
    
def test_calculator(driver):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        WebDriverWait(driver, 50)
        calculator = CalculatorPage(driver)
        calculator.enter_delay("45")
        calculator.click_button()
        result = calculator.get_result()
       