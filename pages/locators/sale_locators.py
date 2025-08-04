from selenium.webdriver.common.by import By

MEN_SALE = (By.XPATH, '//*[@class="title" and text() ="Men’s Bargains"]')
MEN_SALE_PAGE = (By.XPATH, '//*[@data-ui-id="page-title-wrapper" and text() ="Men Sale"]')
HEADER_PAGE = (By.CSS_SELECTOR, '#page-title-heading')
WOMEN_SALE = (By.XPATH, '//*[@class="info" and text() ="Women’s Deals"]')
WOMEN_SALE_PAGE = (By.CSS_SELECTOR, '#page-title-heading')
