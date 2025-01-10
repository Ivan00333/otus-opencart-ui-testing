import pytest
from selenium import webdriver
import logging

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture(scope="class")
def driver(pytestconfig, request):
    browser_name = pytestconfig.getoption("browser")
    driver = None

    if browser_name in ["ch", "chrome"]:
        driver = webdriver.Chrome()
    if browser_name in ["ff", "firefox"]:
        driver = webdriver.Firefox()

    driver.maximize_window()

    driver.test_name = request.node.name
    driver.log_level = logging.DEBUG

    yield driver
    driver.close()
