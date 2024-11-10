import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAdminLoginPage:
    URI_ADMIN_LOGIN_PAGE = 'administration'

    CARD_HEADER_LOCATOR = (By.XPATH, "//div[text()=' Please enter your login details.']")
    INPUT_USERNAME_LOCATOR = (By.XPATH, "//input[@id='input-username']")
    INPUT_PASSWORD_LOCATOR = (By.XPATH, "//input[@id='input-password']")
    LOGO_OPENCART_LOCATOR = (By.XPATH, "//a/img[@title='OpenCart']")
    BUTTON_LOGIN_LOCATOR = (By.XPATH, "//button[text()=' Login']")

    locators_list = [
        CARD_HEADER_LOCATOR,
        INPUT_USERNAME_LOCATOR,
        INPUT_PASSWORD_LOCATOR,
        LOGO_OPENCART_LOCATOR,
        BUTTON_LOGIN_LOCATOR
    ]

    def open_admin_login_page(self, browser):
        browser.get(f"{browser.base_url}{self.URI_ADMIN_LOGIN_PAGE}")

    def check_element_visible(self, browser, locator):
        WebDriverWait(browser, 30, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    @pytest.mark.parametrize("locator", locators_list)
    def test_check_visible_admin_login_elements(self, browser, locator):
        self.open_admin_login_page(browser)
        self.check_element_visible(browser, locator)

