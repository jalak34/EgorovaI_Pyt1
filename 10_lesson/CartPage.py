from selenium.webdriver.support.ui import WebDriverWait
import allure
from selenium.webdriver.common.by import By


class CartPage():
    """
    Конструктор класса CartPage
    для страницы добавления товаров в корзину
    """
    @allure.step('Инициализировать драйвер по параметру {driver}')
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def cart(self) -> None:
        """
        Методы для добавления товаров в корзину,
        а также для нажатия кнопки  Checkout
        """

        with allure.step('Добавить товары в корзину'):
            self.driver.find_element(By.CSS_SELECTOR,
                                     '#add-to-cart-sauce-labs-backpack')\
                .click()
            self.driver.find_element(By.CSS_SELECTOR,
                                     '#add-to-cart-sauce-labs-bolt-t-shirt')\
                .click()
            self.driver.find_element(By.CSS_SELECTOR,
                                     '#add-to-cart-sauce-labs-onesie').\
                click()
            self.driver.find_element(By.CSS_SELECTOR,
                                     '#shopping_cart_container').click()

        with allure.step('Нажать кнопку Checkout'):
            self.driver.find_element(By.CSS_SELECTOR,
                                     '#checkout').click()
