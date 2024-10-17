import pytest
from selenium import webdriver


def pytest_addoptions(parser):
    parser.addoptin("--browser", default="chrome")
@pytest.fixture
def browser(pytestconfig):
    browser_name = pytestconfig.getoption("browser")
    if browser_name in ["ch", "chrome"]:
        return webdriver.Chrome()
    if browser_name in ["ff", "firefox"]:
        return webdriver.Firefox()
