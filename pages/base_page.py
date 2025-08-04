from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.locators import base_locators as loc
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Открытие страницы')
    def open_page(self):
        if self.base_url:
            self.driver.get(f'{self.base_url}/{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find_element(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def wait_element(self, locator):
        element = (WebDriverWait(self.driver, 4).until(
            EC.presence_of_element_located(locator)))
        return element

    @allure.step('Принятие кук')
    def accept_cookie(self):
        try:
            self.wait_element(loc.COOKIE).click()
        except TimeoutException:
            print('Модалка с куками не появилась')

    @allure.step('Скролл страницы до конца')
    def scroll_page(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Скролл страницы до нужного элемента')
    def scroll_400_px(self):
        return self.driver.execute_script("window.scroll(0,400)")
