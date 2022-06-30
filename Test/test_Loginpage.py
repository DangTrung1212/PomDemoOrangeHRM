from Pages.Login_page import LoginPage
from Test.Base_Test import BaseTest


class Test_LoginPage(BaseTest):
    def test_login_title(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.get_title(self.login_page.LOGIN_PAGE_TITLE)

    def test_login_button_is_enable(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.login_button_is_enable()

    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login()
        self.login_page.implicitly_wait()
