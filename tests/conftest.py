import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture(scope="class")
def setup(request):
    browser = 'chrome'

    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'fire fox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())
    else:
        print("Please select Browser")

    driver.get("http://the-internet.herokuapp.com/")
    driver.maximize_window()
    driver.title
    driver.delete_all_cookies()
    request.cls.driver = driver
    yield
    driver.close()
