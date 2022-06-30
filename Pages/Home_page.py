from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class HomePage(BasePage):
    ADMIN_LOCATOR = (By.ID, "//a[@id='menu_admin_viewAdminModule']")

    def __init__(self, driver):
        super().__init__(driver)
