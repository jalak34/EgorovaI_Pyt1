from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class PricePage():
    """
    Конструктор класса PricePage
    """
    @allure.step('Инициализировать драйвер по параметру {driver}')
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Прочитать со страницы итоговую стоимость\
               Проверить, что итоговая сумма равна $58.29.")
    def total_price(self) -> None:
        total = self.driver.find_element(By.CSS_SELECTOR,
                                         '[class="summary_total_label"]').text
        total_value = float(total.split("$")[1])
        assert total_value == 58.29, 'Сумма не равна'
