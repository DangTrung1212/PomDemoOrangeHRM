from Pages.Add_user_page import AddUserPage
from Pages.Login_page import LoginPage
from Test.Base_Test import BaseTest


class Test_AddUserPage(BaseTest):
    def test_add_user(self):
        # Login in to the website first
        login = LoginPage(self.driver)
        login.login()
        login.implicitly_wait()
        # Navigate to the adding user page
        add_user_page = AddUserPage(self.driver)
        # Fill all the fields
        add_user_page.drop_downlist_select(add_user_page.USER_ROLE_LOCATOR, add_user_page.USER_ROLE_LIST[0])
        add_user_page.send_keys(add_user_page.EMPLOYEE_NAME_LOCATOR, 'Jacqueline White')
        add_user_page.send_keys(add_user_page.USER_NAME_LOCATOR, 'Jacqueline White')
        add_user_page.drop_downlist_select(add_user_page.STATUS_LOCATOR, add_user_page.STATUS_LIST[0])
        add_user_page.send_keys(add_user_page.PASSWORD_LOCATOR, "trung230796")
        add_user_page.send_keys(add_user_page.CONFIRM_PASSWORD_LOCATOR, "trung230796")
        # click on save button
        add_user_page.click(add_user_page.SAVE_BUTTON_LOCATOR)
        assert add_user_page.get_current_url() == 'https://opensource-demo.orangehrmlive.com/index.php/admin' \
                                                  '/viewSystemUsers '
