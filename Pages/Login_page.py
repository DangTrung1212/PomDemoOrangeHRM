from Config.config import TestData
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    LOGIN_PAGE_TITLE = 'OrangeHRM'
    USERNAME_LOCATOR = (By.ID, 'txtUsername')
    PASSWORD_LOCATOR = (By.ID, 'txtPassword')
    LOGIN_BUTTON_LOCATOR = (By.ID, 'btnLogin')

    def __init__(self, driver):
        super().__init__(driver)
        self.goto(TestData.BASE_LOGIN_URL)

    def get_login_title(self):
        return self.get_title(self.LOGIN_PAGE_TITLE)

    def login_button_is_enable(self):
        return self.is_enable(self.LOGIN_BUTTON_LOCATOR)

    def login(self):
        self.send_keys(self.USERNAME_LOCATOR, TestData.USER_NAME)
        self.send_keys(self.PASSWORD_LOCATOR, TestData.PASS_WORD)
        self.click(self.LOGIN_BUTTON_LOCATOR)


