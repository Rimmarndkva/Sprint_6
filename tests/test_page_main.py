import allure
import pytest
from data import answer_for_question, TestUrl
from locators.page_order_locators import OrderPageLocators
from pages.page_main import MainPage

class TestsMainPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_page = MainPage(driver)
        driver.get(TestUrl.MAIN_URL)
        self.main_page.accept_cookie()
    
    @allure.title('Проверяем выпадающий список вопросы-ответы')
    @pytest.mark.parametrize("question_id, expected_answer", answer_for_question.items())
    def test_check_answer_for_question(self, question_id, expected_answer):
        assert self.main_page.check_answer_for_question(question_id) == expected_answer

    @allure.title('Проверяем работу верхней кнопки Заказать')
    def test_click_order_button_up(self):
        self.main_page.click_for_order_button_up()
        assert self.main_page.find_element_with_wait(OrderPageLocators.title_order_page)

    @allure.title('Проверяем работу нижней кнопки Заказать')
    def test_click_order_button_down(self):
        self.main_page.scroll_for_order_button_down()
        self.main_page.click_for_order_button_down()
        assert self.main_page.find_element_with_wait(OrderPageLocators.title_order_page)