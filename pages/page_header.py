import allure
from locators.header_page_locators import HeaderPageLocators
from pages.page_baze import BasePage

class HeaderPage(BasePage):

    @allure.step('Переходим на главную страницу')
    def switch_to_scooter_page(self):
 
        self.click_to_element(HeaderPageLocators.SCOOTER_LOGO)

    @allure.step('Переходим на страницу Дзена')
    def switch_to_dzen_page(self):
        self.click_to_element(HeaderPageLocators.YANDEX_LOGO)
        self.switch_window()

    @allure.step('Получаем текст заголовка главной страницы')
    def get_scooter_headline_text(self):
        return self.get_text_from_element(HeaderPageLocators.HOME_HEADER)

    @allure.step('Находим логотип на странице Дзена')
    def check_dzen_button(self):
        return self.find_element_with_wait(HeaderPageLocators.DZEN_LOGO)