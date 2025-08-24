import pytest
from selenium import webdriver
from pages.create_account_page import CreateAccount
from pages.eco_friendly_pages import EcoFriendly
from pages.sale_page import SalePage
from selenium.webdriver.chrome.options import Options
import allure
from allure_commons.types import AttachmentType


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType)
    driver.quit()


@pytest.fixture()
def create_account(driver):
    return CreateAccount(driver)


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def sale(driver):
    return SalePage(driver)
