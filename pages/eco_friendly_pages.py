from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from pages.locators import eco_friendly_locators as loc
import allure


class EcoFriendly(BasePage):
    page_url = 'collections/eco-friendly.html'

    @allure.label('owner', 'Андрей')
    @allure.story('Страница товаров')
    @allure.step('Проверка на количество отображаемых товаров на странице')
    def check_number_of_products_on_a_page(self):
        products_in_the_title = self.find_element(loc.ELEMENTS_ON_TITLE).text
        counting_products = self.find_elements(loc.ALL_ELEMENTS)
        products = len(counting_products)
        assert int(products_in_the_title) == products

    @allure.label('owner', 'Андрей')
    @allure.story('Страница товаров')
    @allure.step('Открытие карточки товара')
    def open_card_product(self):
        product_name = self.find_element(loc.PRODUCT).text
        self.find_element(loc.PRODUCT).click()
        return product_name

    @allure.label('owner', 'Андрей')
    @allure.story('Страница товаров')
    @allure.step('Сортировка товаров по возрастанию цены')
    def check_sort_by_price(self):
        sorter = self.find_element(loc.SORT_BTN)
        select = Select(sorter)
        select.select_by_value('price')
        sorted_prices = [
            float(price.text.replace('$', ''))
            for price in self.find_elements(loc.PRICE)
            if price.text.strip() and price.text.replace('.', '', 1).isdigit()
        ]
        assert sorted_prices == sorted(sorted_prices), "Список не отсортирован по возрастанию"
