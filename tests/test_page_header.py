import allure

from data import TestUrl
from pages.page_main import MainPage
from pages.page_header import HeaderPageLocators
from conftest import driver


class HeaderPageLocators:
    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката')
    def test_transition_from_order_page_to_main_page(self, driver,):
        switch_page = HeaderPageLocators(driver)
        main_page = MainPage(driver)
        driver.get(TestUrl.MAIN_URL)
        main_page.accept_cookie()
        main_page.click_for_order_button_up()
        switch_page.switch_to_scooter_page()
        assert 'Самокат' in switch_page.get_scooter_headline_text()

    @allure.title('Проверка перехода на Дзен по клику на лого Дзена')
    def test_transition_from_order_page_to_dzen(self, driver):
        switch_page = HeaderPageLocators(driver)
        main_page = MainPage(driver)
        driver.get(TestUrl.MAIN_URL)
        main_page.accept_cookie()
        switch_page.switch_to_dzen_page()
        assert switch_page.check_dzen_button()