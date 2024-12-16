
from pages.base_page import BasePage
from locators.locators import AdminLoginPageLocators
from data.constants import Urls, AdminAuth


class AdminLoginPage(BasePage):
    def open_admin_login_page(self):
        self.open(Urls.URL_ADMIN_LOGIN_PAGE)
    
    def admin_auth(self):
        self.input(AdminLoginPageLocators.INPUT_USERNAME_LOCATOR, AdminAuth.ADMIN_USERNAME)
        self.input(AdminLoginPageLocators.INPUT_PASSWORD_LOCATOR, AdminAuth.ADMIN_PASSWORD)
        self.click(AdminLoginPageLocators.BUTTON_LOGIN_LOCATOR)
    