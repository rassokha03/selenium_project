from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from faker import Faker
import allure


class CreateAccount(BasePage):
    page_url = 'customer/account/create/'

    @allure.label('owner', 'Андрей')
    @allure.story('Страница регистрации пользователя')
    @allure.step('Регистрация нового пользователя')
    def user_registration(self, first_name, last_name, email, password, confirm_password):
        first_name_field = self.find_element(loc.FIRST_NAME)
        last_name_field = self.find_element(loc.LAST_NAME)
        email_field = self.find_element(loc.EMAIL)
        password_field = self.find_element(loc.PASSWORD)
        confirm_password_field = self.find_element(loc.CONFIRM_PASSWORD)
        create_account_btn = self.find_element(loc.CREATE_ACCOUNT_BTN)
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(confirm_password)
        create_account_btn.click()

    @allure.label('owner', 'Андрей')
    @allure.story('Страница регистрации пользователя')
    @allure.step('Проверка регистрации')
    def check_registration(self, text):
        msg = self.find_element(loc.MSG)
        assert msg.text == text

    def create_fake_email(self):
        fake = Faker()
        return fake.email()

    @allure.label('owner', 'Андрей')
    @allure.story('Страница регистрации пользователя')
    @allure.step('Проверка зарегистрированного пользователя')
    def check_account_information(self, create_name, create_email):
        account_info = self.find_element(loc.ACCOUNT_INFORMATION).text
        lines = account_info.strip().split('\n')
        name = lines[0].strip()
        email = lines[1].strip()
        assert name == create_name
        assert email == create_email

    @allure.story('Страница регистрации пользователя')
    @allure.step('Проверка на то, что пароли разные')
    def error_passwords_different(self):
        error = self.find_element(loc.ERROR_PASSWORD)
        assert error.text == 'Please enter the same value again.'
