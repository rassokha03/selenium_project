from pages.base_page import BasePage
from pages.locators import sale_locators as loc
import allure


class SalePage(BasePage):
    page_url = 'sale.html'

    @allure.label('owner', 'Андрей')
    @allure.story('Страница распродаж')
    @allure.step('Открытие страницы с мужской распродажей')
    def check_open_men_sale_page(self):
        self.find_element(loc.MEN_SALE).click()
        men_sale_header = self.find_element(loc.MEN_SALE_PAGE).text
        assert men_sale_header == 'Men Sale'

    @allure.label('owner', 'Андрей')
    @allure.story('Страница распродаж')
    @allure.step('Проверка, что заголовок страницы имеет тег h1')
    def header_page_have_tag_h1(self):
        header = self.find_element(loc.HEADER_PAGE)
        assert header.tag_name == 'h1'

    @allure.label('owner', 'Андрей')
    @allure.story('Страница распродаж')
    @allure.step('Открытие страница с женской распродажей')
    def check_open_women_sale_page(self):
        self.find_element(loc.WOMEN_SALE).click()
        men_sale_header = self.find_element(loc.WOMEN_SALE_PAGE).text
        assert men_sale_header == 'Women Sale'
