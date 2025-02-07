import pytest
from selenium import webdriver
import logging
import allure


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

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            name="page_source",
            body=driver.page_source,
            attachment_type=allure.attachment_type.HTML
        )

    driver.close()
