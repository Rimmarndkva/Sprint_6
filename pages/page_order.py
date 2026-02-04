import allure
from selenium.webdriver.common.keys import Keys
from helpers import generate_date_rent
from locators.page_order_locators import OrderPageLocators
from pages.page_baze import BasePage


class OrderPage(BasePage):

    @allure.step('Заполняем поле Имя')
    def fill_in_input_name(self, name):
        self.add_text_to_element(OrderPageLocators.input_name, name)

    @allure.step('Заполняем поле Фамилия')
    def fill_in_input_last_name(self, last_name):
        self.add_text_to_element(OrderPageLocators.input_last_name, last_name)

    @allure.step('Заполняем поле Адрес')
    def fill_in_input_address(self, address):
        self.add_text_to_element(OrderPageLocators.input_address, address)

    @allure.step('Заполняем поле Телефон')
    def fill_in_input_phone(self, phone):
        self.add_text_to_element(OrderPageLocators.input_phone, phone)

    @allure.step('Выбираем метро (клавиатурой)')
    def select_metro_station(self, metro_name):
        self.click_to_element(OrderPageLocators.input_metro)
        self.add_text_to_element(OrderPageLocators.input_metro, metro_name)
        self.add_text_to_element(OrderPageLocators.input_metro, Keys.DOWN)
        self.add_text_to_element(OrderPageLocators.input_metro, Keys.ENTER)

    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_form_about_info_client(self, name, last_name, address, metro, phone):
        self.fill_in_input_name(name)
        self.fill_in_input_last_name(last_name)
        self.fill_in_input_address(address)
        self.fill_in_input_phone(phone)
        self.select_metro_station(metro)
        self.click_to_element(OrderPageLocators.button_next)

    @allure.step('Заполняем дату и закрываем календарь')
    def fill_in_input_date_rent(self):
        rent_date = generate_date_rent()
        self.add_text_to_element(OrderPageLocators.input_date_rent, rent_date)
        self.add_text_to_element(OrderPageLocators.input_date_rent, Keys.ENTER)
        self.click_to_element(OrderPageLocators.title_order_rent)

    @allure.step('Выбираем срок аренды')
    def fill_in_input_count_rent_day(self, rent_day):
     
        element = self.find_element_with_wait(OrderPageLocators.input_count_rent_day)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
        locator_item = self.format_locators(OrderPageLocators.list_count_rent_day, rent_day)
        self.click_to_element(locator_item)

    @allure.step('Выбираем цвет')
    def fill_in_checkbox_colour(self, colour):
        locator_colour = self.format_locators(OrderPageLocators.checkbox_colour, colour)
        self.click_to_element(locator_colour)

    @allure.step('Пишем комментарий')
    def fill_in_comment_input(self, comment):
        self.add_text_to_element(OrderPageLocators.input_comment, comment)

    @allure.step('Заполняем форму "Про аренду" и подтверждаем заказ')
    def fill_form_about_rent(self, rent_day, colour, comment):
        self.find_element_with_wait(OrderPageLocators.title_order_rent)
        self.fill_in_input_date_rent()
        self.fill_in_input_count_rent_day(rent_day)
        self.fill_in_checkbox_colour(colour)
        self.fill_in_comment_input(comment)
        self.click_button_order_finall()
        self.confirmation_order()

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_button_order_finall(self):
        self.click_to_element(OrderPageLocators.button_finall_order)

    @allure.step('Подтверждаем (кнопка "Да")')
    def confirmation_order(self):
        self.click_to_element(OrderPageLocators.button_order_confirmation)

    @allure.step('Проверяем всплывающее окно "Заказ оформлен"')
    def check_accept_order(self):
        return self.get_text_from_element(OrderPageLocators.title_order_add)