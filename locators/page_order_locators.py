from selenium.webdriver.common.by import By

class OrderPageLocators:


    title_order_page = (By.XPATH, '//div[text()="Для кого самокат"]')
    input_name = (By.XPATH, '//input[contains(@placeholder, "Имя")]')
    input_last_name = (By.XPATH, '//input[contains(@placeholder, "Фамилия")]')
    input_address = (By.XPATH, '//input[contains(@placeholder, "Адрес")]')
    input_phone = (By.XPATH, '//input[contains(@placeholder, "Телефон")]')
    input_metro = (By.XPATH, '//input[contains(@placeholder, "Станция метро")]')
    metro_lst_element = (By.XPATH, "//*[contains(@class, 'select-search__row')]//*[text()='{}']")
    button_next = (By.XPATH, '//button[text()="Далее"]')

    title_order_rent = (By.XPATH, '//div[text()="Про аренду"]')
    input_date_rent = (By.XPATH, '//input[contains(@placeholder, "Когда привезти")]')
    
    input_count_rent_day = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")

    list_count_rent_day = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and contains(text(), '{}')]")
    
    checkbox_colour = (By.XPATH, '//*[@id="{}"]')
    input_comment = (By.XPATH, '//input[contains(@placeholder, "Комментарий")]')
    button_back = (By.XPATH, '//button[text()="Назад"]')
    button_finall_order = (By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]')

    title_order_confirmation = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    button_order_confirmation = (By.XPATH, '//button[text()="Да"]')
    title_order_add = (By.XPATH, '//div[text()="Заказ оформлен"]')