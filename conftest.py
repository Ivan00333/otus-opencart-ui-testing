import json
import pytest
from selenium import webdriver
import logging
import allure


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        if not hasattr(item.parent, "failed_tests"):
            item.parent.failed_tests = set()

        if rep.failed:
            item.parent.failed_tests.add(item.nodeid)
        else:
            item.parent.failed_tests.discard(item.nodeid)

@pytest.fixture(scope="class")
def driver(pytestconfig, request):
    browser_name = pytestconfig.getoption("browser")
    driver = None

    if browser_name in ["ch", "chrome"]:
        driver = webdriver.Chrome()
    if browser_name in ["ff", "firefox"]:
        driver = webdriver.Firefox()

    driver.maximize_window()

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON)

    driver.test_name = request.node.name
    driver.log_level = logging.DEBUG

    def teardown():
        if hasattr(request.node, "failed_tests") and request.node.failed_tests:
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

        driver.quit()

    request.addfinalizer(teardown)
    return driver
