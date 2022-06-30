from Pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class AddUserPage(BasePage):
    BASE_URL = 'https://opensource-demo.orangehrmlive.com/index.php/admin/saveSystemUser'
    USER_ROLE_LIST = ['ESS', "Admin"]
    USER_ROLE_LOCATOR = (By.ID, 'systemUser_userType')
    EMPLOYEE_NAME_LOCATOR = (By.ID, 'systemUser_employeeName_empName')
    USER_NAME_LOCATOR = (By.ID, 'systemUser_userName')
    STATUS_LOCATOR = (By.ID, "systemUser_status")
    STATUS_LIST = ['Enabled', 'Disabled']
    PASSWORD_LOCATOR = (By.ID, 'systemUser_password')
    CONFIRM_PASSWORD_LOCATOR = (By.ID, 'systemUser_confirmPassword')
    SAVE_BUTTON_LOCATOR = (By.ID, 'btnSave')

    def __init__(self, driver):
        super().__init__(driver)
        self.goto(self.BASE_URL)

