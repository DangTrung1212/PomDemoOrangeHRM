from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CandidatePage(BasePage):
    BASE_URL = 'https://opensource-demo.orangehrmlive.com/index.php/recruitment/viewCandidates'
    ADD_LOCATOR = (By.ID, 'btnAdd')
    DELETE_LOCATOR = (By.ID, 'btnDelete')
    CHECKBOX_LIST_LOCATOR = (By.XPATH,'//input[@type="checkbox"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.goto(self.BASE_URL)

    def delete_first_candidate(self):
        pass