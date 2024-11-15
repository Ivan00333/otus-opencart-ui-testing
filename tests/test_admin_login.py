from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAdminLogin:
    URI_ADMIN_LOGIN_PAGE = 'administration'
    ADMIN_USERNAME = 'user'
    ADMIN_PASSWORD = 'bitnami'

    INPUT_USERNAME_LOCATOR = (By.XPATH, "//input[@id='input-username']")
    INPUT_PASSWORD_LOCATOR = (By.XPATH, "//input[@id='input-password']")
    BUTTON_LOGIN_LOCATOR = (By.XPATH, "//div[@class='text-end']/button[@type='submit']")
    ADMIN_NAME_LOCATOR = (By.XPATH, "//span[contains(text(), 'John Doe')]")
    BUTTON_LOGOUT_LOCATOR = (By.XPATH, "//span[text()='Logout']")

    def open_admin_login_page(self, browser):
        browser.get(f"{browser.base_url}{self.URI_ADMIN_LOGIN_PAGE}")

    def get_find_element(self, browser, locator):
        return WebDriverWait(browser, 10, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def check_element_visible(self, browser, locator):
        WebDriverWait(browser, 10, poll_frequency=1).until(EC.visibility_of_element_located(locator))

    def test_admin_login(self, browser):
        self.open_admin_login_page(browser)
        username_field = self.get_find_element(browser, self.INPUT_USERNAME_LOCATOR)
        password_field = self.get_find_element(browser, self.INPUT_PASSWORD_LOCATOR)
        username_field.send_keys(self.ADMIN_USERNAME)
        password_field.send_keys(self.ADMIN_PASSWORD)
        self.get_find_element(browser, self.BUTTON_LOGIN_LOCATOR).click()
        self.check_element_visible(browser, self.ADMIN_NAME_LOCATOR)
        self.get_find_element(browser, self.BUTTON_LOGOUT_LOCATOR).click()
        self.check_element_visible(browser, self.BUTTON_LOGIN_LOCATOR)
