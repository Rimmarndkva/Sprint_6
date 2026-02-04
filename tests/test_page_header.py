import pytest
import allure
from data import TestUrl
from pages.page_main import MainPage
from pages.page_header import HeaderPage 

class TestHeaderPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_page = MainPage(driver)
        self.header_page = HeaderPage(driver)
        driver.get(TestUrl.MAIN_URL)
        self.main_page.accept_cookie()

    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката')
    def test_transition_from_order_page_to_main_page(self):
        self.main_page.click_for_order_button_up()
        self.header_page.switch_to_scooter_page()
        assert 'Самокат' in self.header_page.get_scooter_headline_text()

    @allure.title('Проверка перехода на Дзен по клику на лого Дзена')
    def test_transition_from_order_page_to_dzen(self):
        self.header_page.switch_to_dzen_page()
        assert self.header_page.check_dzen_button()