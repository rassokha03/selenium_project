import pytest
from selenium import webdriver
from pages.create_account_page import CreateAccount
from pages.eco_friendly_pages import EcoFriendly
from pages.sale_page import SalePage
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope='function')
def driver():
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('window-size=1920,1080')
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
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
