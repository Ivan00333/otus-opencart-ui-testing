import json
from pymysql.cursors import DictCursor
import pymysql
import pytest
from selenium import webdriver
import logging
import allure
from logger.logger import config_logger
from db.db import Db
import bcrypt
from datetime import datetime
from pages.register_page import RegisterPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        choices=["chrome", "firefox", "opera"],
        default="firefox",
        help="Browser to run tests: chrome, firefox, opera"
    )
    parser.addoption(
        "--selenoid_url",
        default=None,
        help="URL of Selenoid server (e.g. http://localhost:4444/wd/hub). If not set, local browser is used."
    )
    parser.addoption(
        "--browser_version",
        default = None,
        help="Browser version to use (e.g. 124.0). If not set, Selenoid default is used."
    )
    parser.addoption(
        "--enable_video",
        action="store_true",
        default=False,
        help="Record video when running via Selenoid"
    )
    parser.addoption(
        "--db_host",
        action="store",
        default="127.0.0.1",
        help="Database host"
    )
    parser.addoption(
        "--db_port",
        action="store",
        default="3306",
        help="Database port"
    )
    parser.addoption(
        "--db_user",
        action="store",
        default="bn_opencart",
        help="Database user"
    )
    parser.addoption(
        "--db_password",
        action="store",
        default="",
        help="Database password"
    )
    parser.addoption(
        "--db_name",
        action="store",
        default="bitnami_opencart",
        help="Database name"
    )

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
    selenoid_url = pytestconfig.getoption("selenoid_url")
    browser_version = pytestconfig.getoption("browser_version")
    record_video = pytestconfig.getoption("enable_video")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    if selenoid_url:
        options.set_capability("browserName", browser_name)
        if browser_version:
            options.set_capability("browserVersion", browser_version)
        selenoid_opts = {"enableVNC": True, "enableLog": True}
        if record_video:
            selenoid_opts["enableVideo"] = True
        options.set_capability("selenoid:options", selenoid_opts)

        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )
    else:
        if browser_name == "chrome":
            driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            driver = webdriver.Firefox(options=options)
        elif browser_name == "opera":
            driver = webdriver.Opera(options=options)

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


@pytest.fixture(scope="session")
def connection(request):
    host = request.config.getoption("--db_host")
    port = int(request.config.getoption("--db_port"))
    user = request.config.getoption("--db_user")
    password = request.config.getoption("--db_password")
    db_name = request.config.getoption("--db_name")

    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=db_name,
        charset="utf8mb4",
        cursorclass=DictCursor
    )

    yield conn
    conn.close()

@pytest.fixture
def logger(request):
    return config_logger(request.node.name)

@pytest.fixture
def db(connection, logger):
    return Db(connection, logger)

@pytest.fixture
def user_data(logger):
    logger.info("Создание данных пользователя для БД")
    new_user = RegisterPage.create_user()

    salt = bcrypt.gensalt(rounds=10)
    hashed = bcrypt.hashpw(new_user["password"].encode(), salt)
    hashed_password = hashed.decode()

    now = datetime.now()
    formatted = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    user_data = {
        "customer_group_id": 0,
        "store_id": 0,
        "language_id": 1,
        "firstname": new_user["firstname"],
        "lastname": new_user["lastname"],
        "email": new_user["email"],
        "telephone": new_user["telephone"],
        "password": hashed_password,
        "custom_field": "",
        "newsletter": 0,
        "ip": '192.168.0.10',
        "status": 1,
        "safe": 0,
        "token": "",
        "code": "",
        "date_added": formatted
    }

    return user_data