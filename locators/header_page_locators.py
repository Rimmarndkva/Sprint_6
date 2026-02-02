from selenium.webdriver.common.by import By

class HeaderPageLocators:
 
    SCOOTER_LOGO = (By.XPATH, '//*[contains(@class, "Header_LogoScooter")]')
    YANDEX_LOGO = (By.XPATH, '//*[contains(@class, "Header_LogoYandex")]')
    HOME_HEADER = (By.XPATH, '//*[contains(@class, "Home_Header")]')
    DZEN_LOGO = (By.XPATH, '//*[contains(@class, "desktop-base-header__logo")]')