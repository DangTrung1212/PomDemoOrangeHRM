import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service


@pytest.fixture(params=["chrome", "firefox", 'edge'], scope='class')
def init_driver(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if request.param == "firefox":
        # unavailable because of 'ValueError: API Rate limit exceeded. You have to add GH_TOKEN!!!'
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    if request.param == 'edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    request.cls.driver = driver
    yield
    driver.close()
