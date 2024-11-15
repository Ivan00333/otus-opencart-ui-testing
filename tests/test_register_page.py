import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegisterPage:
    URI_REGISTER_PAGE = "en-gb?route=account/register"

    FIRST_NAME_LOCATOR = (By.XPATH, "//input[@id='input-firstname']")
    LAST_NAME_LOCATOR = (By.XPATH, "//input[@id='input-lastname']")
    EMAIL_LOCATOR = (By.XPATH, "//input[@id='input-email']")
    PASSWORD_LOCATOR = (By.XPATH, "//input[@id='input-password']")
    CONTINUE_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Continue']")

    locators_list = [
        FIRST_NAME_LOCATOR,
        LAST_NAME_LOCATOR,
        EMAIL_LOCATOR,
        PASSWORD_LOCATOR,
        CONTINUE_BUTTON_LOCATOR
    ]

    def open_register_page(self, browser):
        browser.get(f"{browser.base_url}{self.URI_REGISTER_PAGE}")

    def check_element_visible(self, browser, locator):
        WebDriverWait(browser, 15, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    @pytest.mark.parametrize("locator", locators_list)
    def test_check_visible_register_page_elements(self, browser, locator):
        self.open_register_page(browser)
        self.check_element_visible(browser, locator)
