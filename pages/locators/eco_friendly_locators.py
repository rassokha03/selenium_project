from selenium.webdriver.common.by import By

ALL_ELEMENTS = (By.CSS_SELECTOR, '.item.product')
SELECT = (By.CSS_SELECTOR, '.label[for="limiter"]')
ELEMENTS_ON_TITLE = (By.XPATH, '//*[@class= "toolbar-number"][2]')
PRODUCT = (By.CSS_SELECTOR, '.product-item-link')
PRODUCT_HEADER = (By.XPATH, '//li[@class="item product"]')
PRODUCT_NAME_IN_CARD = (By.XPATH, '//span[@itemprop="name"]')
SORT_BTN = (By.CSS_SELECTOR, '#sorter')
PRICE = (By.CSS_SELECTOR, '.price')
