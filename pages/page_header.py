import allure
from locators.header_page_locators import HeaderPageLocators
from pages.page_baze import BasePage


class HeaderPageLocators(BasePage):
    @allure.step('Переходим на главную страницу')
    def switch_to_scooter_page(self):
        self.click_to_element(HeaderPageLocators.scooter_logo)

    @allure.step('Переходим на страницу Дзена')
    def switch_to_dzen_page(self):
        self.click_to_element(HeaderPageLocators.dzen_logo)
        self.switch_window()

    @allure.step('Получаем текст заголовка главной страницы')
    def get_scooter_headline_text(self):
        return self.get_text_from_element(HeaderPageLocators.title_main_page)

    @allure.step('Находим логотип на странице Дзена')
    def check_dzen_button(self):
        return self.find_element_with_wait(HeaderPageLocators.logo_dzen_main_page)