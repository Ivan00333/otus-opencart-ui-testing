import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default='http://192.168.0.10:8081/')


@pytest.fixture(scope="class")
def browser(pytestconfig):
    browser_name = pytestconfig.getoption("browser")
    driver = None
    base_url = pytestconfig.getoption("url")

    if browser_name in ["ch", "chrome"]:
        driver = webdriver.Chrome()
    if browser_name in ["ff", "firefox"]:
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.base_url = base_url

    yield driver
    driver.close()
