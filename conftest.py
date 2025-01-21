import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture(scope="class")
def driver(pytestconfig):
    browser_name = pytestconfig.getoption("browser")
    driver = None

    if browser_name in ["ch", "chrome"]:
        driver = webdriver.Chrome()
    if browser_name in ["ff", "firefox"]:
        driver = webdriver.Firefox()

    driver.maximize_window()

    yield driver
    driver.close()
