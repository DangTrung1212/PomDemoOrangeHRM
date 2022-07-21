import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BasePage:
    ALL_LINK_LOCATOR = (By.CSS_SELECTOR, "a")
    ALL_IMG_LOCATOR = (By.CSS_SELECTOR, "img")

    def __init__(self, driver):
        self.driver = driver

    def goto(self, url):
        self.driver.get(url)

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).send_keys(text)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_all_link(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(self.ALL_LINK_LOCATOR)

    def get_all_image(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(self.ALL_IMG_LOCATOR)

    def is_enable(self, by_locator):
        button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return button.is_enabled()

    def implicitly_wait(self):
        self.driver.implicitly_wait(10)

    def drop_downlist_select(self, by_locator, element_text):
        select = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
        select.select_by_visible_text(element_text)

    def get_current_url(self):
        self.implicitly_wait()
        return str(self.driver.current_url)

    def select_checkbox(self, by_locator, nth):
        """Get a list of checkbox elements then select the nth checkbox
        nth : integer
        """
        list_of_checkbox = WebDriverWait(self.driver, 10).until((EC.visibility_of_all_elements_located(by_locator)))
        list_of_checkbox.get(nth).click()
