from selenium.webdriver.common.by import By

FIRST_NAME = (By.CSS_SELECTOR, '#firstname')
LAST_NAME = (By.CSS_SELECTOR, '#lastname')
EMAIL = (By.CSS_SELECTOR, '#email_address')
PASSWORD = (By.CSS_SELECTOR, '#password')
CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#password-confirmation')
CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, '[title= "Create an Account"]')
MSG = (By.CSS_SELECTOR, '.page.messages')
ACCOUNT_INFORMATION = (By.CSS_SELECTOR, '.box-content')
ERROR_PASSWORD = (By.CSS_SELECTOR, '#password-confirmation-error')
