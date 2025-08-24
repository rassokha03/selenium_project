from pages.base_page import BasePage
from pages.locators import card_product_locators as loc
import allure


class ProductCard(BasePage):
    @allure.label('owner', 'Андрей')
    @allure.story('Страница товаров')
    @allure.step('Получение названия товара в карточке товара')
    def check_product_card(self, name_product):
        product_header = self.find_element(loc.PRODUCT_HEADER).text
        product_name_in_card = self.find_element(loc.PRODUCT_NAME_IN_CARD).text
        assert name_product == product_header == product_name_in_card
