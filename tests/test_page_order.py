import allure
import pytest
from data import comment, TestUrl
from helpers import info_client, about_scooter_rent
from locators.page_main_locators import MainPageLocators
from pages.page_main import MainPage
from pages.page_order import OrderPage

class TestOrderPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_page = MainPage(driver)
        self.order_page = OrderPage(driver)
        driver.get(TestUrl.MAIN_URL)
        self.main_page.accept_cookie()

    @allure.step('Тестируем оформление заказа с валидными данными')
    @pytest.mark.parametrize('button',
                             [MainPageLocators.order_button_down,
                              MainPageLocators.order_button_up])
    def test_created_order(self, button): 
        self.main_page.created_order(button)
        self.order_page.fill_form_about_info_client(
            name=info_client['name'],
            last_name=info_client['last_name'],
            address=info_client['address'],
            metro=info_client['metro'],
            phone=info_client['phone']
        )
        self.order_page.fill_form_about_rent(
            rent_day=about_scooter_rent['rent_day'],
            colour=about_scooter_rent['colour'],
            comment=comment
        )
        self.order_page.click_button_order_finall()
        self.order_page.confirmation_order()
        assert 'Заказ оформлен' in self.order_page.check_accept_order()